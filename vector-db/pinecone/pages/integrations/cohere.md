---
title: "Cohere"
source: https://docs.pinecone.io/integrations/cohere
path: integrations/cohere
---

Generate embeddings with the Cohere Embed API, index them in Pinecone, and run semantic search queries against the index.

The Cohere platform builds natural language processing and generation into your product with a few lines of code. Cohere's large language models (LLMs) can solve a broad spectrum of natural language use cases, including classification, semantic search, paraphrasing, summarization, and content generation.

Use the Cohere Embed API endpoint to generate language embeddings, and then index those embeddings in Pinecone for fast and scalable vector search.

## Setup guide

In this guide, you'll learn how to use the [Cohere Embed API endpoint](https://docs.cohere.com/reference/embed) to generate language embeddings, and then index those embeddings in [Pinecone Database](/guides/get-started/overview) for fast and scalable vector search.

This is a common combination for building semantic search, question-answering, threat-detection, and other applications that rely on NLP and search over a large corpus of text data.

The basic workflow looks like this:

* Embed and index
  * Use the Cohere Embed API endpoint to generate vector embeddings of your documents (or any text data).
  * Upload those vector embeddings into Pinecone, which can store and index millions or billions of these vector embeddings and search through them at low latency.
* Search
  * Pass your query text or document through the Cohere Embed API endpoint again.
  * Take the resulting vector embedding and send it as a [query](/guides/search/search-overview) to Pinecone.
  * Get back semantically similar documents, even if they don't share any keywords with the query.

<img alt="Basic workflow of Cohere with Pinecone" />

<Steps>
  <Step title="Set up the environment">
    Start by installing the Cohere and Pinecone clients, along with Hugging Face Datasets for downloading the TREC dataset used in this guide:

    ```shell Shell theme={null}
    pip install -U cohere pinecone datasets
    ```
  </Step>

  <Step title="Create embeddings">
    Sign up for an API key at [Cohere](https://dashboard.cohere.com/api-keys) and then use it to initialize your connection.

    ```Python Python theme={null}
    import cohere

    co = cohere.ClientV2(api_key="<YOUR_COHERE_API_KEY>")
    ```

    Load the Text REtrieval Conference (TREC) question classification dataset, which contains 5.5K labeled questions. You'll take only the first 1K samples for this walkthrough, but you can scale this to millions or even billions of samples.

    ```Python Python theme={null}
    from datasets import load_dataset

    # load the first 1K rows of the TREC dataset
    trec = load_dataset('CogComp/trec', revision='refs/convert/parquet', split='train[:1000]')
    ```

    Each sample in `trec` contains two label features and the `text` feature. Pass the questions from the `text` feature to Cohere to create embeddings. The Embed API accepts up to 96 texts per request, so send them in batches.

    ```Python Python theme={null}
    embeds = []
    batch_size = 96

    for i in range(0, len(trec['text']), batch_size):
        res = co.embed(
            texts=trec['text'][i:i+batch_size],
            model='embed-english-v3.0',
            input_type='search_document',
            embedding_types=['float'],
            truncate='END'
        )
        embeds.extend(res.embeddings.float_)
    ```

    Check the dimensionality of the returned vectors. Save the embedding dimensionality, because you need it when you create your Pinecone index later.

    ```Python Python theme={null}
    import numpy as np

    shape = np.array(embeds).shape
    print(shape)
    ```

    ```text Response theme={null}
    (1000, 1024)
    ```

    You can see the `1024` embedding dimensionality produced by Cohere's `embed-english-v3.0` model, and the `1000` samples you built embeddings for.
  </Step>

  <Step title="Store the embeddings">
    Now that you have your embeddings, you can move on to indexing them in Pinecone Database. For this, you need a [Pinecone API key](/guides/projects/manage-api-keys).

    First, initialize your connection to Pinecone, and then create a new index called `cohere-pinecone-trec` for storing the embeddings. When you create the index, specify the cosine similarity metric to align with Cohere's embeddings, and pass the embedding dimensionality of `1024`.

    ```Python Python theme={null}
    from pinecone import Pinecone, ServerlessSpec

    # initialize connection to pinecone (get API key at app.pinecone.io)
    pc = Pinecone(api_key='<YOUR_PINECONE_API_KEY>')

    index_name = 'cohere-pinecone-trec'

    # if the index does not exist, we create it
    if not pc.has_index(index_name):
        pc.create_index(
            name=index_name,
            dimension=shape[1],
            metric="cosine",
            spec=ServerlessSpec(
                cloud='aws', 
                region='us-east-1'
            ) 
        )

    # connect to index
    index = pc.Index(index_name)
    ```

    Now you can begin populating the index with your embeddings. Pinecone expects you to provide a list of tuples in the format `(id, vector, metadata)`, where the `metadata` field is an optional extra field where you can store anything you want in a dictionary format. For this example, you'll store the original text of the embeddings.

    Upload the data in batches to avoid pushing too much data at once.

    ```Python Python theme={null}
    batch_size = 128

    ids = [str(i) for i in range(shape[0])]
    # create list of metadata dictionaries
    meta = [{'text': text} for text in trec['text']]

    # create list of (id, vector, metadata) tuples to be upserted
    to_upsert = list(zip(ids, embeds, meta))

    for i in range(0, shape[0], batch_size):
        i_end = min(i+batch_size, shape[0])
        index.upsert(vectors=to_upsert[i:i_end])

    # let's view the index statistics
    print(index.describe_index_stats())
    ```

    ```text Response theme={null}
    DescribeIndexStatsResponse(dimension=1024, total_vector_count=1000, metric='cosine', namespaces=1)
    ```

    You can see from `index.describe_index_stats` that you have a 1024-dimensional index populated with 1000 embeddings.
  </Step>

  <Step title="Run a semantic search">
    Now that you have your indexed vectors, you can perform a few search queries. To search, first embed your query with Cohere, and then search Pinecone with the returned vector.

    ```Python Python theme={null}
    query = "What caused the 1929 Great Depression?"

    # create the query embedding
    xq = co.embed(
        texts=[query],
        model='embed-english-v3.0',
        input_type='search_query',
        embedding_types=['float'],
        truncate='END'
    ).embeddings.float_[0]

    # query, returning the top 5 most similar results
    res = index.query(vector=xq, top_k=5, include_metadata=True)
    ```

    The response from Pinecone includes your original text in the `metadata` field. Print the `top_k` most similar questions and their similarity scores.

    ```Python Python theme={null}
    for match in res['matches']:
        print(f"{match['score']:.2f}: {match['metadata']['text']}")
    ```

    ```text Response theme={null}
    0.62: Why did the world enter a global depression in 1929 ?
    0.49: When was `` the Great Depression '' ?
    0.38: What crop failure caused the Irish Famine ?
    0.32: What caused Harry Houdini 's death ?
    0.31: What causes pneumonia ?
    ```

    The top results are relevant. To make the search harder, replace "depression" with the incorrect term "recession."

    ```Python Python theme={null}
    query = "What was the cause of the major recession in the early 20th century?"

    # create the query embedding
    xq = co.embed(
        texts=[query],
        model='embed-english-v3.0',
        input_type='search_query',
        embedding_types=['float'],
        truncate='END'
    ).embeddings.float_[0]

    # query, returning the top 5 most similar results
    res = index.query(vector=xq, top_k=5, include_metadata=True)

    for match in res['matches']:
        print(f"{match['score']:.2f}: {match['metadata']['text']}")
    ```

    ```text Response theme={null}
    0.43: When was `` the Great Depression '' ?
    0.40: Why did the world enter a global depression in 1929 ?
    0.39: When did World War I start ?
    0.35: What are some of the significant historical events of the 1990s ?
    0.32: What crop failure caused the Irish Famine ?
    ```

    Finally, search using the definition of depression rather than the word or related words.

    ```Python Python theme={null}
    query = "Why was there a long-term economic downturn in the early 20th century?"

    # create the query embedding
    xq = co.embed(
        texts=[query],
        model='embed-english-v3.0',
        input_type='search_query',
        embedding_types=['float'],
        truncate='END'
    ).embeddings.float_[0]

    # query, returning the top 10 most similar results
    res = index.query(vector=xq, top_k=10, include_metadata=True)

    for match in res['matches']:
        print(f"{match['score']:.2f}: {match['metadata']['text']}")
    ```

    ```text Response theme={null}
    0.40: When was `` the Great Depression '' ?
    0.39: Why did the world enter a global depression in 1929 ?
    0.35: When did World War I start ?
    0.32: What are some of the significant historical events of the 1990s ?
    0.31: What war did the Wanna-Go-Home Riots occur after ?
    0.31: What do economists do ?
    0.29: What historical event happened in Dogtown in 1899 ?
    0.28: When did the Dow first reach ?
    0.28: Who earns their money the hard way ?
    0.28: What were popular songs and types of songs in the 1920s ?
    ```

    This example shows that the semantic search pipeline can identify the meaning behind each of your queries. Using these embeddings with Pinecone lets you return the most semantically similar questions from the already indexed TREC dataset.
  </Step>

  <Step title="Clean up">
    When you're finished with the index, delete it.

    ```Python Python theme={null}
    pc.delete_index(name=index_name)
    ```
  </Step>
</Steps>
