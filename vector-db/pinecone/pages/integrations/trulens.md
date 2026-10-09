---
title: "TruLens"
source: https://docs.pinecone.io/integrations/trulens
path: integrations/trulens
---

Use TruLens to evaluate and track a RAG app built on Pinecone and LangChain, and compare configurations such as the distance metric, model, and top k.

[TruLens](https://www.trulens.org/) is an open-source library for evaluating and tracking large language model (LLM) applications. It scores each request with feedback functions, such as answer relevance and context relevance, and records latency and cost, so you can compare app configurations as you iterate.

## Setup guide

This guide builds a retrieval-augmented generation (RAG) app on Pinecone Database with LangChain, evaluates it with TruLens, and compares configurations.

<Steps>
  <Step title="Set up the environment">
    Install the libraries, and set your OpenAI API key as the `OPENAI_API_KEY` environment variable. LangChain and the TruLens OpenAI provider both read it.

    ```shell Shell theme={null}
    pip install -qU trulens trulens-apps-langchain trulens-providers-openai \
      langchain-openai langchain-pinecone pinecone-datasets
    ```
  </Step>

  <Step title="Create the index">
    Load a pre-embedded dataset from `pinecone-datasets`, so you can skip the embedding step:

    ```Python Python theme={null}
    import pinecone_datasets

    dataset = pinecone_datasets.load_dataset('wikipedia-simple-text-embedding-ada-002-100K')
    # The text and title are in the blob column, so use it as the metadata.
    dataset.documents.drop(['metadata'], axis=1, inplace=True)
    dataset.documents.rename(columns={'blob': 'metadata'}, inplace=True)
    ```

    Create an index and upsert the documents. The dataset was embedded with `text-embedding-ada-002`, so the index has 1536 dimensions. The distance metric is the first configuration choice you compare later.

    ```Python Python theme={null}
    from pinecone import Pinecone, ServerlessSpec

    pc = Pinecone(api_key="YOUR_API_KEY")

    index_name_v1 = 'langchain-rag-cosine'
    if not pc.has_index(index_name_v1):
        pc.create_index(
            name=index_name_v1,
            metric='cosine',
            dimension=1536,
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )

    index = pc.Index(index_name_v1)

    for batch in dataset.iter_documents(batch_size=100):
        index.upsert(batch)
    ```
  </Step>

  <Step title="Build the RAG chain">
    Create a LangChain vector store on the index, and build a chain that retrieves documents and passes them to the LLM with the question. Queries must use the same embedding model as the dataset.

    ```Python Python theme={null}
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.runnables import RunnablePassthrough
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings
    from langchain_pinecone import PineconeVectorStore

    embed = OpenAIEmbeddings(model='text-embedding-ada-002')
    vectorstore = PineconeVectorStore(index=index, embedding=embed, text_key="text")

    llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.0)

    prompt = ChatPromptTemplate.from_template(
        "Answer the question based only on the following context:\n\n"
        "{context}\n\nQuestion: {question}"
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    retriever = vectorstore.as_retriever()

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    ```
  </Step>

  <Step title="Define feedback functions">
    Feedback functions score each request. This guide uses two:

    * Context relevance is the average relevance (0 to 1) of each context chunk the retriever returns.
    * Answer relevance is the relevance (0 to 1) of the final answer to the question.

    ```Python Python theme={null}
    from trulens.apps.langchain import TruChain
    from trulens.core import Metric, Selector, TruSession
    from trulens.providers.openai import OpenAI
    import numpy as np

    session = TruSession()
    provider = OpenAI(model_engine="gpt-4o-mini")

    f_answer_relevance = Metric(
        implementation=provider.relevance,
        name="Answer Relevance",
        selectors={
            "prompt": Selector.select_record_input(),
            "response": Selector.select_record_output(),
        },
    )

    f_context_relevance = Metric(
        implementation=provider.context_relevance,
        name="Context Relevance",
        selectors={
            "question": Selector.select_record_input(),
            "context": Selector.select_context(collect_list=False),
        },
        agg=np.mean,
    )
    ```

    Selectors tell TruLens which parts of a request to score. `select_record_input()` and `select_record_output()` are the app's question and final answer. `select_context(collect_list=False)` is each context chunk the retriever returns, scored separately, and `agg=np.mean` averages those scores.
  </Step>

  <Step title="Record queries">
    Wrap the chain with TruLens and run queries inside the recorder's context. TruLens computes feedback in the background, so `retrieve_feedback_results` waits for the scores and returns one row per query.

    ```Python Python theme={null}
    truchain_v1 = TruChain(
        rag_chain,
        app_name='WikipediaQA',
        app_version='Chain1',
        feedbacks=[f_answer_relevance, f_context_relevance],
    )

    with truchain_v1 as recording:
        rag_chain.invoke("Which state is Washington D.C. in?")
        rag_chain.invoke("Which year was Hawaii's state song written?")

    record_ids = [record.record_id for record in recording.records]
    print(truchain_v1.retrieve_feedback_results(record_ids=record_ids))
    ```

    Compare the scores, latency, and cost of each app version with the leaderboard, or explore individual records in the TruLens dashboard:

    ```Python Python theme={null}
    print(session.get_leaderboard())

    from trulens.dashboard import run_dashboard
    run_dashboard(session=session)
    ```
  </Step>

  <Step title="Compare configurations">
    To compare configurations, change one component, wrap the new chain with a new `app_version`, and run the same queries. Then check the leaderboard again.

    The distance metric is set when you create the index. To try `euclidean` or `dotproduct`, create and populate a second index, and point a new vector store and chain at it. OpenAI embeddings are normalized to length 1, so all three metrics return the same ranking, and any difference shows up in latency rather than quality.

    ```Python Python theme={null}
    index_name_v2 = 'langchain-rag-euclidean'
    if not pc.has_index(index_name_v2):
        pc.create_index(
            name=index_name_v2,
            metric='euclidean',
            dimension=1536,
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )

    index_v2 = pc.Index(index_name_v2)
    for batch in dataset.iter_documents(batch_size=100):
        index_v2.upsert(batch)

    vectorstore = PineconeVectorStore(index=index_v2, embedding=embed, text_key="text")
    retriever = vectorstore.as_retriever()
    ```

    To try a different model or a different amount of context (top k), swap the LLM or set `k` on the retriever:

    ```Python Python theme={null}
    llm = ChatOpenAI(model='gpt-4.1-nano', temperature=0)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 1})
    ```

    After each change, rebuild the chain, wrap it with a new version, and record the same queries. Use a new variable for each version, so earlier recorders keep running until their feedback finishes.

    ```Python Python theme={null}
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    truchain_v2 = TruChain(
        rag_chain,
        app_name='WikipediaQA',
        app_version='Chain2',
        feedbacks=[f_answer_relevance, f_context_relevance],
    )

    with truchain_v2 as recording:
        rag_chain.invoke("Which state is Washington D.C. in?")
        rag_chain.invoke("Which year was Hawaii's state song written?")

    record_ids = [record.record_id for record in recording.records]
    print(truchain_v2.retrieve_feedback_results(record_ids=record_ids))
    print(session.get_leaderboard())
    ```
  </Step>

  <Step title="Clean up">
    When you're finished with the index, delete both indexes.

    ```Python Python theme={null}
    pc.delete_index(name=index_name_v1)
    pc.delete_index(name=index_name_v2)
    ```
  </Step>
</Steps>
