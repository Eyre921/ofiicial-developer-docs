---
title: "Haystack"
source: https://docs.pinecone.io/integrations/haystack
path: integrations/haystack
---

Use deepset Haystack's PineconeDocumentStore to build production NLP pipelines that index, embed, and query documents for question answering and RAG.

Haystack is the open-source Python framework by deepset for building custom apps with large language models (LLMs). It lets you try out the latest models in natural language processing (NLP), and it's flexible to work with. Its community of users and builders has helped shape Haystack into a complete framework for building NLP apps for production.

You can use the Haystack and Pinecone integration to keep your NLP-driven apps up to date, with Haystack's indexing pipelines to help you prepare and maintain your data.

## Setup guide

This guide shows how to integrate Pinecone and the [Haystack library](https://github.com/deepset-ai/haystack) for question answering. It uses OpenAI models to create embeddings and generate answers.

<Steps>
  <Step title="Install Haystack">
    Install the latest version of Haystack, the Pinecone integration for Haystack, and Hugging Face Datasets.

    ```shell Shell theme={null}
    pip install -U "haystack-ai>=3.3.0" "pinecone-haystack>=6.4.1" "datasets"
    ```
  </Step>

  <Step title="Set your API keys">
    The `PineconeDocumentStore` reads your Pinecone API key from the `PINECONE_API_KEY` environment variable, and Haystack's OpenAI components read your OpenAI API key from `OPENAI_API_KEY`. [Create an account](https://app.pinecone.io) to get your free Pinecone API key.

    ```Python Python theme={null}
    import os

    os.environ["PINECONE_API_KEY"] = "YOUR_API_KEY"
    os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
    ```
  </Step>

  <Step title="Initialize the PineconeDocumentStore">
    Initialize a `PineconeDocumentStore`. If the index doesn't exist, the document store creates a serverless index with the dimension, metric, and spec you provide. The dimension matches the `text-embedding-3-small` embedding model used later in this guide.

    ```Python Python theme={null}
    from haystack_integrations.document_stores.pinecone import PineconeDocumentStore

    document_store = PineconeDocumentStore(
        index="haystack-qa",
        namespace="squad",
        dimension=1536,
        metric="cosine",
        spec={"serverless": {"cloud": "aws", "region": "us-east-1"}},
    )
    ```
  </Step>

  <Step title="Prepare data">
    Before you add data to the document store, you must download the data and convert it into the Document format that Haystack uses.

    This guide uses the SQuAD dataset available from Hugging Face Datasets.

    ```Python Python theme={null}
    from datasets import load_dataset

    # load the squad dataset
    data = load_dataset("rajpurkar/squad", split="train")
    ```

    Next, remove duplicates and unnecessary columns.

    ```Python Python theme={null}
    # convert to a pandas dataframe
    df = data.to_pandas()
    # select only title and context column
    df = df[["title", "context"]]
    # drop rows containing duplicate context passages
    df = df.drop_duplicates(subset="context")
    df.head()
    ```

    | | title | context |
    | - | - | - |
    | 0 | University\_of\_Notre\_Dame | Architecturally, the school has a Catholic cha... |
    | 5 | University\_of\_Notre\_Dame | As at most other universities, Notre Dame's st... |
    | 10 | University\_of\_Notre\_Dame | The university is the major seat of the Congre... |
    | 15 | University\_of\_Notre\_Dame | The College of Engineering was established in ... |
    | 20 | University\_of\_Notre\_Dame | All of Notre Dame's undergraduate students are... |

    Then convert these records into the Document format.

    ```Python Python theme={null}
    from haystack import Document

    docs = [
        Document(content=row["context"], meta={"title": row["title"]})
        for _, row in df.iterrows()
    ]
    ```

    This `Document` format contains two fields: `content` for the text content or paragraphs, and `meta` for any additional information you can later use to apply metadata filtering in your search.
  </Step>

  <Step title="Embed and upsert documents">
    Build an indexing pipeline that creates an embedding for each document with OpenAI's `text-embedding-3-small` model and writes the documents and their embeddings to Pinecone.

    ```Python Python theme={null}
    from haystack import Pipeline
    from haystack.components.embedders import OpenAIDocumentEmbedder
    from haystack.components.writers import DocumentWriter

    indexing = Pipeline()
    indexing.add_component("embedder", OpenAIDocumentEmbedder(model="text-embedding-3-small"))
    indexing.add_component("writer", DocumentWriter(document_store=document_store))
    indexing.connect("embedder.documents", "writer.documents")

    indexing.run({"embedder": {"documents": docs}})
    ```
  </Step>

  <Step title="Inspect documents and embeddings">
    You can get documents by their metadata with the `PineconeDocumentStore.filter_documents` method.

    ```Python Python theme={null}
    docs_found = document_store.filter_documents(
        filters={"field": "meta.title", "operator": "==", "value": "Egypt"}
    )
    d = docs_found[0]
    ```

    From here, you can view document content with `d.content` and the document embedding with `d.embedding`.
  </Step>

  <Step title="Initialize a question-answering pipeline">
    A retrieval-augmented question-answering pipeline contains four components:

    * a text embedder that creates an embedding for the question
    * a retriever (`PineconeEmbeddingRetriever`) that finds the most relevant documents in Pinecone
    * a prompt builder that adds the retrieved documents and the question to a prompt
    * a generator that answers the question with an LLM

    This guide uses OpenAI's `gpt-4o-mini` model as the generator.

    ```Python Python theme={null}
    from haystack.components.builders import ChatPromptBuilder
    from haystack.components.embedders import OpenAITextEmbedder
    from haystack.components.generators.chat import OpenAIChatGenerator
    from haystack.dataclasses import ChatMessage
    from haystack_integrations.components.retrievers.pinecone import PineconeEmbeddingRetriever

    template = [
        ChatMessage.from_user(
            """Answer the question using only the context below.

    Context:
    {% for document in documents %}
    {{ document.content }}
    {% endfor %}

    Question: {{ question }}
    Answer:"""
        )
    ]

    pipe = Pipeline()
    pipe.add_component("text_embedder", OpenAITextEmbedder(model="text-embedding-3-small"))
    pipe.add_component("retriever", PineconeEmbeddingRetriever(document_store=document_store))
    pipe.add_component("prompt_builder", ChatPromptBuilder(template=template, required_variables=["question", "documents"]))
    pipe.add_component("llm", OpenAIChatGenerator(model="gpt-4o-mini"))
    pipe.connect("text_embedder.embedding", "retriever.query_embedding")
    pipe.connect("retriever.documents", "prompt_builder.documents")
    pipe.connect("prompt_builder.prompt", "llm.messages")
    ```
  </Step>

  <Step title="Ask questions">
    Define a helper function that runs the pipeline and prints the answer along with the title and score of each retrieved document. The `top_k` parameter sets how many documents the retriever passes to the LLM.

    ```Python Python theme={null}
    def ask(question, top_k=1):
        result = pipe.run(
            {
                "text_embedder": {"text": question},
                "retriever": {"top_k": top_k},
                "prompt_builder": {"question": question},
            },
            include_outputs_from={"retriever"},
        )
        print("Query:", question)
        print("Answer:", result["llm"]["replies"][0].text)
        for doc in result["retriever"]["documents"]:
            print("Source:", doc.meta["title"], round(doc.score, 3))
    ```

    Use your QA pipeline to ask a few questions:

    ```Python Python theme={null}
    ask("What was Albert Einstein famous for?")
    ask("How much oil is Egypt producing in a day?")
    ask("Who founded YouTube?")
    ```

    ```text Response theme={null}
    Query: What was Albert Einstein famous for?
    Answer: Albert Einstein was famous for his theories of special relativity and general relativity, as well as his contributions to statistical mechanics, quantum mechanics, and quantum field theory.
    Source: Modern_history 0.635

    Query: How much oil is Egypt producing in a day?
    Answer: Egypt was producing 691,000 bbl/d of oil.
    Source: Egypt 0.674

    Query: Who founded YouTube?
    Answer: Hurley and Chen founded YouTube.
    Source: YouTube 0.636
    ```

    You can pass more context to the LLM by setting the `top_k` parameter.

    ```Python Python theme={null}
    ask("Who was the first person to step foot on the moon?", top_k=3)
    ```

    ```text Response theme={null}
    Query: Who was the first person to step foot on the moon?
    Answer: Neil Armstrong was the first person to step foot on the Moon.
    Source: Space_Race 0.639
    Source: Space_Race 0.613
    Source: Space_Race 0.516
    ```
  </Step>

  <Step title="Clean up">
    When you're finished with the index, delete it.

    ```Python Python theme={null}
    from pinecone import Pinecone

    pc = Pinecone()  # reads PINECONE_API_KEY
    pc.delete_index(name="haystack-qa")
    ```
  </Step>
</Steps>
