---
title: "Hugging Face Inference Endpoints"
source: https://docs.pinecone.io/integrations/hugging-face-inference-endpoints
path: integrations/hugging-face-inference-endpoints
---

Generate embeddings with Hugging Face Inference Endpoints and index them in Pinecone for semantic search, RAG, and transformer model deployment.

Hugging Face Inference Endpoints offers a secure production solution for deploying any Hugging Face Transformers, Sentence-Transformers, and Diffusion models from the Hub on dedicated, autoscaling infrastructure managed by Hugging Face.

With Pinecone, you can use Hugging Face to generate and index vector embeddings.

## Setup guide

Hugging Face Inference Endpoints provides access to model inference. In this guide, you create an endpoint that generates vector embeddings, index the embeddings in Pinecone, and search them.

<Steps>
  <Step title="Create an endpoint">
    In [Hugging Face Inference Endpoints](https://ui.endpoints.huggingface.co/endpoints), create an endpoint for a sentence-embedding model from the Hub, such as [`sentence-transformers/all-mpnet-base-v2`](https://huggingface.co/sentence-transformers/all-mpnet-base-v2), which outputs 768-dimensional embeddings like the examples in this guide. A CPU instance costs less, and a GPU instance embeds faster. Endpoints are billed while they run, so delete yours when you finish.

    When the endpoint's status is **Running**, copy its endpoint URL from the endpoint's overview page:

    ```Python Python theme={null}
    endpoint = "<ENDPOINT_URL>"
    ```

    You also need a Hugging Face access token that can call your endpoints. Create a fine-grained token in your Hugging Face account settings under **Access Tokens**:

    ```Python Python theme={null}
    hf_token = "<HF_TOKEN>"
    ```
  </Step>

  <Step title="Create embeddings">
    Define a helper that sends text to the endpoint and returns the embeddings. Depending on the serving engine, an endpoint returns either `{"embeddings": [...]}` or a bare list of embeddings, so the helper handles both.

    ```Python Python theme={null}
    import requests

    headers = {'Authorization': f'Bearer {hf_token}'}

    def embed(texts):
        res = requests.post(endpoint, headers=headers, json={"inputs": texts})
        res.raise_for_status()
        data = res.json()
        return data["embeddings"] if isinstance(data, dict) else data

    embeddings = embed(["a happy dog", "a sad dog"])
    len(embeddings)
    ```

    ```text Response theme={null}
    2
    ```

    Check the dimensionality of the embeddings. You need it when you create the index.

    ```Python Python theme={null}
    dim = len(embeddings[0])
    dim
    ```

    ```text Response theme={null}
    768
    ```

    You need more than two items to search through, so download a larger dataset with Hugging Face Datasets.

    ```Python Python theme={null}
    from datasets import load_dataset

    snli = load_dataset("stanfordnlp/snli", split='train')
    snli
    ```

    ```text Response theme={null}
    Dataset({
        features: ['premise', 'hypothesis', 'label'],
        num_rows: 550152
    })
    ```

    SNLI contains 550K sentence pairs, and many of them include duplicate items, so take just one set of these (the `hypothesis` column) and deduplicate it.

    ```Python Python theme={null}
    passages = list(set(snli['hypothesis']))
    len(passages)
    ```

    ```text Response theme={null}
    480042
    ```

    To keep the example quick to run, reduce the set to 50K sentences. If you have time, you can keep the full 480K.

    ```Python Python theme={null}
    passages = passages[:50_000]
    ```
  </Step>

  <Step title="Create an index">
    With your endpoint and dataset ready, all that's missing is a Pinecone index. First, initialize your connection to Pinecone, which requires an [API key](https://app.pinecone.io/).

    ```Python Python theme={null}
    from pinecone import Pinecone, ServerlessSpec

    # initialize connection to pinecone (get API key at app.pinecone.io)
    pc = Pinecone(api_key="YOUR_API_KEY")
    ```

    Now create a new index called `'hf-endpoints'`. You can use any name. The `dimension` must match your endpoint model's output dimensionality (which you found in `dim` earlier), and the metric must match the model (`cosine` typically works, but not for all models).

    ```Python Python theme={null}
    index_name = 'hf-endpoints'

    # check if the hf-endpoints index exists
    if not pc.has_index(index_name):
        # create the index if it does not exist
        pc.create_index(
            name=index_name,
            dimension=dim,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )

    # connect to hf-endpoints index we created
    index = pc.Index(index_name)
    ```
  </Step>

  <Step title="Store the embeddings">
    With the endpoint, dataset, and Pinecone index ready, create embeddings for the dataset and index them in Pinecone.

    ```Python Python theme={null}
    from tqdm.auto import tqdm

    # we will use batches of 64
    batch_size = 64

    for i in tqdm(range(0, len(passages), batch_size)):
        # find end of batch
        i_end = min(i+batch_size, len(passages))
        # extract batch
        batch = passages[i:i_end]
        # generate embeddings for batch via endpoints
        emb = embed(batch)
        # get metadata (just the original text)
        meta = [{'text': text} for text in batch]
        # create IDs
        ids = [str(x) for x in range(i, i_end)]
        # add all to upsert list
        to_upsert = list(zip(ids, emb, meta))
        # upsert/insert these records to pinecone
        _ = index.upsert(vectors=to_upsert)

    # check that we have all vectors in index
    index.describe_index_stats()
    ```

    ```text Response theme={null}
    100%|██████████| 782/782 [11:02<00:00,  1.18it/s]

    DescribeIndexStatsResponse(dimension=768, total_vector_count=50000, metric='cosine', namespaces=1)
    ```
  </Step>

  <Step title="Run a semantic search">
    With everything indexed, you can begin querying. Use a few examples from the `premise` column of the dataset as queries.

    ```Python Python theme={null}
    query = snli['premise'][0]
    print(f"Query: {query}")
    # encode with HF endpoints
    xq = embed([query])[0]
    # query and return top 5
    xc = index.query(vector=xq, top_k=5, include_metadata=True)
    # iterate through results and print text
    print("Answers:")
    for match in xc['matches']:
        print(match['metadata']['text'])
    ```

    ```text Response theme={null}
    Query: A person on a horse jumps over a broken down airplane.
    Answers:
    The horse jumps over a toy airplane.
    a lady rides a horse over a plane shaped obstacle
    A person getting onto a horse.
    person rides horse
    A woman riding a horse jumps over a bar.
    ```

    These results are relevant. Try a couple more examples.

    ```Python Python theme={null}
    query = snli['premise'][100]
    print(f"Query: {query}")
    # encode with HF endpoints
    xq = embed([query])[0]
    # query and return top 5
    xc = index.query(vector=xq, top_k=5, include_metadata=True)
    # iterate through results and print text
    print("Answers:")
    for match in xc['matches']:
        print(match['metadata']['text'])
    ```

    ```text Response theme={null}
    Query: A woman is walking across the street eating a banana, while a man is following with his briefcase.
    Answers:
    A woman eats a banana and walks across a street, and there is a man trailing behind her.
    A woman eats a banana split.
    A woman is carrying two small watermelons and a purse while walking down the street.
    The woman walked across the street.
    A woman walking on the street with a monkey on her back.
    ```

    Try one more example.

    ```Python Python theme={null}
    query = snli['premise'][200]
    print(f"Query: {query}")
    # encode with HF endpoints
    xq = embed([query])[0]
    # query and return top 5
    xc = index.query(vector=xq, top_k=5, include_metadata=True)
    # iterate through results and print text
    print("Answers:")
    for match in xc['matches']:
        print(match['metadata']['text'])
    ```

    ```text Response theme={null}
    Query: People on bicycles waiting at an intersection.
    Answers:
    A pair of people on bikes are waiting at a stoplight.
    Bike riders wait to cross the street.
    people on bicycles
    Group of bike riders stopped in the street.
    There are bicycles outside.
    ```
  </Step>

  <Step title="Clean up">
    Shut down the endpoint by navigating to the Inference Endpoints **Overview** page and selecting **Delete endpoint**. Delete the Pinecone index with:

    ```Python Python theme={null}
    pc.delete_index(index_name)
    ```

    <Note>Once the index is deleted, you can't use it again.</Note>
  </Step>
</Steps>
