---
title: "LangChain"
source: https://docs.pinecone.io/integrations/langchain
path: integrations/langchain
---

Use Pinecone with LangChain to build RAG apps, agents, and chatbots, and manage embeddings, vector stores, retrievers, and chains for LLM-powered search.

LangChain provides modules for managing and optimizing the use of large language models (LLMs) in applications. Its core philosophy is to support data-aware applications where the language model interacts with other data sources and its environment. The framework includes several parts that simplify the application lifecycle:

* Write your applications in LangChain or LangChain.js.
* Use LangSmith to inspect, test, and monitor your chains so you can keep improving them and deploy with confidence.

By integrating Pinecone with LangChain, you can add knowledge to LLMs with retrieval-augmented generation (RAG), which improves what LLMs can do in autonomous agents, chatbots, question-answering, and multi-agent systems.

<PrimarySecondaryCTA />

## Setup guide

This guide shows you how to integrate Pinecone Database with [LangChain](https://www.langchain.com/).

<Note>
  This guide shows one of many ways to use LangChain and Pinecone together. For more examples, see the following:

  * [LangChain AI Handbook](https://www.pinecone.io/learn/series/langchain/)
  * [Retrieval Augmentation for LLMs](https://github.com/pinecone-io/examples/blob/main/learn/generation/langchain/handbook/05-langchain-retrieval-augmentation.ipynb)
  * [Retrieval Augmented Conversational Agent](https://github.com/pinecone-io/examples/blob/main/learn/generation/langchain/handbook/08-langchain-retrieval-agent.ipynb)
</Note>

## Key concepts

The `PineconeVectorStore` class from LangChain lets you interact with Pinecone indexes. You must have an existing Pinecone index before you can create a `PineconeVectorStore` object.

### Initialize a vector store

To initialize a `PineconeVectorStore` object, you must provide the name of the Pinecone index and an `Embeddings` object initialized through LangChain. You can initialize a `PineconeVectorStore` object in two ways:

1. Initialize without adding records:

```Python Python theme={null}
import os
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings

os.environ['OPENAI_API_KEY'] = '<YOUR_OPENAI_API_KEY>'
os.environ['PINECONE_API_KEY'] = '<YOUR_PINECONE_API_KEY>'

index_name = "<YOUR_PINECONE_INDEX_NAME>"
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
```

You can also use the `from_existing_index` method of LangChain's `PineconeVectorStore` class to initialize a vector store.

2. Initialize while adding records:

The `from_documents` and `from_texts` methods of LangChain's `PineconeVectorStore` class add records to a Pinecone index and return a `PineconeVectorStore` object.

The `from_documents` method accepts a list of LangChain's `Document` class objects, which you can create with LangChain's `CharacterTextSplitter` class. The `from_texts` method accepts a list of strings. As with the first approach, you must provide the name of an existing Pinecone index and an `Embeddings` object.

Both of these methods handle the embedding of the provided text data and the creation of records in your Pinecone index.

```Python Python theme={null}
import os
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

os.environ['OPENAI_API_KEY'] = '<YOUR_OPENAI_API_KEY>'
os.environ['PINECONE_API_KEY'] = '<YOUR_PINECONE_API_KEY>'

index_name = "<YOUR_PINECONE_INDEX_NAME>"
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# path to an example text file
loader = TextLoader("../../modules/state_of_the_union.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

vectorstore_from_docs = PineconeVectorStore.from_documents(
    docs,
    index_name=index_name,
    embedding=embeddings
)

texts = ["Tonight, I call on the Senate to: Pass the Freedom to Vote Act.", "One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.", "One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence."]

vectorstore_from_texts = PineconeVectorStore.from_texts(
    texts,
    index_name=index_name,
    embedding=embeddings
)
```

### Add more records

After you initialize a `PineconeVectorStore` object, you can add more records to the underlying Pinecone index (and thus also the linked LangChain object) with the `add_documents` or `add_texts` method.

Like `from_documents` and `from_texts`, both of these methods handle the embedding of the provided text data and the creation of records in your Pinecone index.

To add documents, use `add_documents`:

```Python Python theme={null}
# path to an example text file
loader = TextLoader("../../modules/inaugural_address.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)

vectorstore.add_documents(docs)
```

To add raw text, use `add_texts`:

```Python Python theme={null}
vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)

vectorstore.add_texts(["More text to embed and add to the index!"])
```

### Perform a similarity search

A `similarity_search` on a `PineconeVectorStore` object returns a list of LangChain `Document` objects most similar to the query provided. While the `similarity_search` uses a Pinecone query to find the most similar results, this method includes additional steps and returns results of a different type.

The `similarity_search` method accepts raw text and automatically embeds it using the `Embedding` object provided when you initialized the `PineconeVectorStore`. You can also provide a `k` value to determine the number of LangChain `Document` objects to return. The default value is `k=4`.

```Python Python theme={null}
query = "Who is Ketanji Brown Jackson?"
vectorstore.similarity_search(query)
```

You can also apply a metadata filter to your similarity search. The filtering query language is the same as for Pinecone queries, as detailed in [Filtering with metadata](/guides/index-data/indexing-overview#metadata).

```Python Python theme={null}
query = "Tell me more about Ketanji Brown Jackson."
vectorstore.similarity_search(query, filter={'source': '../../modules/state_of_the_union.txt'})
```

### Namespaces

Several methods of the `PineconeVectorStore` class support using [namespaces](/guides/index-data/indexing-overview#namespaces). You can also initialize your `PineconeVectorStore` object with a namespace to restrict all further operations to that space.

```Python Python theme={null}
index_name = "<YOUR_PINECONE_INDEX_NAME>"
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings, namespace="example-namespace")
```

If you initialize your `PineconeVectorStore` object without a namespace, you can specify the target namespace within the operation.

```Python Python theme={null}
# path to an example text file
loader = TextLoader("../../modules/congressional_address.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

vectorstore_from_docs = PineconeVectorStore.from_documents(
    docs,
    index_name=index_name,
    embedding=embeddings,
    namespace="example-namespace"
)

vectorstore_from_texts = PineconeVectorStore.from_texts(
    texts,
    index_name=index_name,
    embedding=embeddings,
    namespace="example-namespace"
)

vectorstore_from_docs.add_documents(docs, namespace="example-namespace")

vectorstore_from_texts.add_texts(["More text!"], namespace="example-namespace")
```

To search a namespace, pass it to `similarity_search`:

```Python Python theme={null}
query = "Who is Ketanji Brown Jackson?"
vectorstore.similarity_search(query, namespace="example-namespace")
```

## Tutorial

<Steps>
  <Step title="Set up the environment">
    Install the libraries:

    ```shell Shell theme={null}
    pip install -qU \
      "pinecone[grpc]==7.3.0" \
      pinecone-datasets==1.0.2 \
      langchain-pinecone==0.2.13 \
      langchain-openai==1.6.7 \
      langchain==1.4.3
    ```

    Set your Pinecone and OpenAI API keys as environment variables:

    ```shell Shell theme={null}
    export PINECONE_API_KEY="{{YOUR_API_KEY}}"  # Get from app.pinecone.io
    export OPENAI_API_KEY="your-openai-api-key"  # Get from platform.openai.com/api-keys
    ```

    Then read the keys in Python:

    ```Python Python theme={null}
    import os
    pinecone_api_key = os.environ.get('PINECONE_API_KEY')
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    ```
  </Step>

  <Step title="Build the knowledge base">
    Load a sample dataset and prepare it for Pinecone:

    1. Load a [sample Pinecone dataset](/guides/data/use-public-pinecone-datasets) into memory:

       ```Python Python theme={null}
       import pinecone_datasets  
       dataset = pinecone_datasets.load_dataset('wikipedia-simple-text-embedding-ada-002-100K')  
       len(dataset)  
       ```

       ```text Response theme={null}
       100000
       ```

    2. Reduce the dataset and format it for upserting into Pinecone:

       ```Python Python theme={null}
       # we will use rows of the dataset up to index 30_000
       dataset.documents.drop(dataset.documents.index[30_000:], inplace=True)
       # replace the metadata column with blob, which includes the text field
       dataset.documents.drop(['metadata'], axis=1, inplace=True)  
       dataset.documents.rename(columns={'blob': 'metadata'}, inplace=True)  
       ```
  </Step>

  <Step title="Index the data in Pinecone">
    Create an index and upsert the prepared data:

    1. Initialize your client connection to Pinecone and create an index. This step uses the Pinecone API key you set as an environment variable [earlier](#set-up-the-environment).

       ```Python Python theme={null}
       from pinecone.grpc import PineconeGRPC as Pinecone
       from pinecone import ServerlessSpec  
       import time  
       # configure client  
       pc = Pinecone(api_key=pinecone_api_key)  
       spec = ServerlessSpec(cloud='aws', region='us-east-1')  
       # check for and delete index if already exists  
       index_name = 'langchain-retrieval-augmentation-fast'  
       if pc.has_index(index_name):  
           pc.delete_index(name=index_name)  
       # create a new index  
       pc.create_index(  
           index_name,  
           dimension=1536,  # dimensionality of text-embedding-ada-002  
           metric='dotproduct',  
           spec=spec  
       )  
       ```

    2. Target the index and check its current stats:

       ```Python Python theme={null}
       index = pc.Index(index_name)  
       index.describe_index_stats()  
       ```

       ```text Response theme={null}
       {'dimension': 1536,  
       'namespaces': {},  
       'total_vector_count': 0}  
       ```

       The index has a `total_vector_count` of `0` because you haven't added any vectors yet.

    3. Upsert the data to Pinecone:

       ```Python Python theme={null}
       for batch in dataset.iter_documents(batch_size=100):  
           index.upsert(batch)  
       ```

    4. After the data is indexed, check the index stats again:

       ```Python Python theme={null}
       index.describe_index_stats()  
       ```

       ```text Response theme={null}
       {'dimension': 1536,  
       'namespaces': {'': {'vector_count': 30000}},  
       'total_vector_count': 30000} 
       ```
  </Step>

  <Step title="Initialize a LangChain vector store">
    Now that you've built your Pinecone index, initialize a LangChain vector store that uses it. This step uses the OpenAI API key you set as an environment variable [earlier](#set-up-the-environment). OpenAI is a paid service, so running the rest of this tutorial may incur a small cost.

    1. Initialize a LangChain embedding object:

       ```Python Python theme={null}
       from langchain_openai import OpenAIEmbeddings  
       # get openai api key from platform.openai.com  
       model_name = 'text-embedding-ada-002'  
       embeddings = OpenAIEmbeddings(  
           model=model_name,  
           openai_api_key=openai_api_key  
       )  
       ```

    2. Initialize the LangChain vector store:

       The `text_field` parameter sets the name of the metadata field that stores the raw text when you upsert records using a LangChain operation such as `vectorstore.from_documents` or `vectorstore.add_texts`.
       This metadata field is used as the `page_content` in the `Document` objects retrieved from query-like LangChain operations such as `vectorstore.similarity_search`.
       If you don't specify a value for `text_field`, it defaults to `"text"`.

       ```Python Python theme={null}
       from langchain_pinecone import PineconeVectorStore  
       text_field = "text"  
       vectorstore = PineconeVectorStore(  
           index, embeddings, text_field  
       )  
       ```

    3. Query the vector store directly using `vectorstore.similarity_search`:

       ```Python Python theme={null}
       query = "who was Benito Mussolini?"  
       vectorstore.similarity_search(  
           query,  # our search query  
           k=3  # return 3 most relevant docs  
       )  
       ```

       ```text Response theme={null}
       [Document(page_content='Benito Amilcare Andrea Mussolini KSMOM GCTE (29 July 1883 – 28 April 1945) was an Italian politician and journalist...', metadata={'chunk': 0.0, 'source': 'https://simple.wikipedia.org/wiki/Benito%20Mussolini', 'title': 'Benito Mussolini', 'wiki-id': '6754'}),  
       Document(page_content='Fascism as practiced by Mussolini\nMussolini\'s form of Fascism, "Italian Fascism"- unlike Nazism, the racist ideology...', metadata={'chunk': 1.0, 'source': 'https://simple.wikipedia.org/wiki/Benito%20Mussolini', 'title': 'Benito Mussolini', 'wiki-id': '6754'}),  
       Document(page_content='Veneto was made part of Italy in 1866 after a war with Austria. Italian soldiers won Latium in 1870. That was when...', metadata={'chunk': 5.0, 'source': 'https://simple.wikipedia.org/wiki/Italy', 'title': 'Italy', 'wiki-id': '363'})]
       ```

    All of these sample results are relevant. You can also use the vector store for other tasks. One that LangChain supports well is generative question answering (GQA).
  </Step>

  <Step title="Use Pinecone and LangChain for RAG">
    In RAG, you pass the query to an LLM as a question, and the LLM must answer it based on the information it gets from the vector store. Follow these steps:

    1. Build a RAG chain that retrieves context from the vector store and passes it to the LLM with the question:

       ```Python Python theme={null}
       from langchain_openai import ChatOpenAI  
       from langchain_core.prompts import ChatPromptTemplate  
       from langchain_core.output_parsers import StrOutputParser  
       from langchain_core.runnables import RunnablePassthrough  
       # completion llm  
       llm = ChatOpenAI(  
           openai_api_key=openai_api_key,  
           model_name='gpt-4o-mini',  
           temperature=0.0  
       )  
       retriever = vectorstore.as_retriever()  
       prompt = ChatPromptTemplate.from_template(  
           "Answer the question based only on the following context:\n\n"  
           "{context}\n\n"  
           "Question: {question}"  
       )  

       def format_docs(docs):  
           return "\n\n".join(doc.page_content for doc in docs)  

       rag_chain = (  
           {"context": retriever | format_docs, "question": RunnablePassthrough()}  
           | prompt  
           | llm  
           | StrOutputParser()  
       )  
       rag_chain.invoke(query)  
       ```

       ```text Response theme={null}
       Benito Mussolini was an Italian politician and journalist who served as the Prime Minister of Italy from 1922 until 1943. He was the leader of the National Fascist Party and is known for creating the ideology of Fascism...
       ```

    2. To include the sources the LLM uses to answer your question, return the retrieved documents alongside the answer:

       ```Python Python theme={null}
       from langchain_core.runnables import RunnableParallel  
       rag_chain_with_sources = RunnableParallel(  
           {"docs": retriever, "question": RunnablePassthrough()}  
       ).assign(  
           answer=(  
               {"context": lambda x: format_docs(x["docs"]), "question": lambda x: x["question"]}  
               | prompt  
               | llm  
               | StrOutputParser()  
           )  
       )  
       result = rag_chain_with_sources.invoke(query)  
       {  
           "question": result["question"],  
           "answer": result["answer"],  
           "sources": sorted({doc.metadata["source"] for doc in result["docs"]}),  
       }  
       ```

       ```text Response theme={null}
       {'question': 'who was Benito Mussolini?',  
       'answer': "Benito Mussolini was an Italian politician and journalist who served as the Prime Minister of Italy from 1922 until 1943. He was the leader of the National Fascist Party and is known for creating the ideology of Fascism...",  
       'sources': ['https://simple.wikipedia.org/wiki/Benito%20Mussolini', ...]}  
       ```
  </Step>

  <Step title="Clean up">
    When you no longer need the index, use the `delete_index` operation to delete it:

    ```Python Python theme={null}
    pc.delete_index(name=index_name)
    ```
  </Step>
</Steps>

## Resources

* [LangChain AI Handbook](https://www.pinecone.io/learn/series/langchain/)
