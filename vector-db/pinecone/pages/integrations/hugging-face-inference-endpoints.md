---
title: "Hugging Face Inference Endpoints"
source: https://docs.pinecone.io/integrations/hugging-face-inference-endpoints
path: integrations/hugging-face-inference-endpoints
---

Generate embeddings with Hugging Face Inference Endpoints and index them in Pinecone for semantic search, RAG, and transformer model deployment.

Hugging Face Inference Endpoints offers a secure production solution for deploying any Hugging Face Transformers, Sentence-Transformers, and Diffusion models from the Hub on dedicated, autoscaling infrastructure managed by Hugging Face.

With Pinecone, you can use Hugging Face to generate and index vector embeddings.

<PrimarySecondaryCTA />

## Setup guide

Hugging Face Inference Endpoints provides access to model inference. In this guide, you create an Inference Endpoint that generates vector embeddings, index the embeddings in Pinecone, and search them.

### Create an endpoint

Go to the [Hugging Face Inference Endpoints homepage](https://ui.endpoints.huggingface.co/endpoints) and sign up for an account if needed. You should then see this page:

<img alt="endpoints 0" />

Click **Create new endpoint**, choose a model repository (e.g., the name of the model) and an endpoint name (this can be anything), and select a cloud environment. Before you move on, make sure you set **Task** to **Sentence Embeddings** (in the **Advanced configuration** settings).

<img alt="endpoints 1" />

<img alt="endpoints 2" />

Another important option is **Instance Type**. By default, this uses a CPU, which is cheaper but also slower. For faster processing, you need a GPU instance. Finally, set your privacy setting near the end of the page.

After you set your options, click **Create Endpoint** at the bottom of the page. This takes you to the next page, where you can see the current status of your endpoint.

<img alt="endpoints 3" />

Once the status has moved from **Building** to **Running** (this can take some time), you're ready to create embeddings with it.

### Create embeddings

Each endpoint has an **Endpoint URL**, which you can find on the endpoint **Overview** page. Assign this endpoint URL to the `endpoint` variable.

<img alt="endpoints 4" />

```Python Python theme={null}
endpoint = "<ENDPOINT_URL>"
```

You also need the organization API token, which you can find in the organization settings on Hugging Face (`https://huggingface.co/organizations/<ORG_NAME>/settings/profile`). Assign it to the `api_org` variable.

<img alt="endpoints 5" />

```Python Python theme={null}
api_org = "<API_ORG_TOKEN>"
```

Now you're ready to create embeddings with Inference Endpoints. Start with a small example.

```Python Python theme={null}
import requests

# add the api org token to the headers
headers = {
    'Authorization': f'Bearer {api_org}'
}
# we add sentences to embed like so
json_data = {"inputs": ["a happy dog", "a sad dog"]}
# make the request
res = requests.post(
    endpoint,
    headers=headers,
    json=json_data
)
```

You should see a `200` response.

```Python Python theme={null}
res
```

```
<Response [200]>
```

The response should contain two embeddings.

```Python Python theme={null}
len(res.json()['embeddings'])
```

```
2
```

You can also check the dimensionality of your embeddings.

```Python Python theme={null}
dim = len(res.json()['embeddings'][0])
dim
```

```
768
```

You need more than two items to search through, so download a larger dataset with Hugging Face Datasets.

```Python Python theme={null}
from datasets import load_dataset

snli = load_dataset("snli", split='train')
snli
```

```
Downloading: 100%|██████████| 1.93k/1.93k [00:00<00:00, 992kB/s]
Downloading: 100%|██████████| 1.26M/1.26M [00:00<00:00, 31.2MB/s]
Downloading: 100%|██████████| 65.9M/65.9M [00:01<00:00, 57.9MB/s]
Downloading: 100%|██████████| 1.26M/1.26M [00:00<00:00, 43.6MB/s]

Dataset({
    features: ['premise', 'hypothesis', 'label'],
    num_rows: 550152
})
```

SNLI contains 550K sentence pairs, and many of them include duplicate items, so take just one set of these (the `hypothesis` column) and deduplicate it.

```Python theme={null}
passages = list(set(snli['hypothesis']))
len(passages)
```

```
480042
```

To keep the example quick to run, reduce the set to 50K sentences. If you have time, you can keep the full 480K.

```Python Python theme={null}
passages = passages[:50_000]
```

### Create an index

With your endpoint and dataset ready, all that's missing is a Pinecone index. First, initialize your connection to Pinecone, which requires a [free API key](https://app.pinecone.io/).

```Python Python theme={null}
import pinecone

# initialize connection to pinecone (get API key at app.pinecone.io)
pinecone.init(api_key="YOUR_API_KEY", environment="YOUR_ENVIRONMENT")

```

Now create a new index called `'hf-endpoints'`. You can use any name. The `dimension` must match your endpoint model's output dimensionality (which you found in `dim` earlier), and the metric must match the model (`cosine` typically works, but not for all models).

```Python Python theme={null}
index_name = 'hf-endpoints'

# check if the hf-endpoints index exists
if index_name not in pinecone.list_indexes():
    # create the index if it does not exist
    pinecone.create_index(
        index_name,
        dimension=dim,
        metric="cosine"
    )

# connect to hf-endpoints index we created
index = pinecone.Index(index_name)
```

### Store the embeddings

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
    res = requests.post(
        endpoint,
        headers=headers,
        json={"inputs": batch}
    )
    emb = res.json()['embeddings']
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

```
100%|██████████| 782/782 [11:02<00:00,  1.18it/s]

{'dimension': 768,
 'index_fullness': 0.1,
 'namespaces': {'': {'vector_count': 50000}},
 'total_vector_count': 50000}
```

### Run a semantic search

With everything indexed, you can begin querying. Use a few examples from the `premise` column of the dataset as queries.

```Python Python theme={null}
query = snli['premise'][0]
print(f"Query: {query}")
# encode with HF endpoints
res = requests.post(endpoint, headers=headers, json={"inputs": query})
xq = res.json()['embeddings']
# query and return top 5
xc = index.query(xq, top_k=5, include_metadata=True)
# iterate through results and print text
print("Answers:")
for match in xc['matches']:
    print(match['metadata']['text'])
```

```
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
res = requests.post(endpoint, headers=headers, json={"inputs": query})
xq = res.json()['embeddings']
# query and return top 5
xc = index.query(xq, top_k=5, include_metadata=True)
# iterate through results and print text
print("Answers:")
for match in xc['matches']:
    print(match['metadata']['text'])
```

```
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
res = requests.post(endpoint, headers=headers, json={"inputs": query})
xq = res.json()['embeddings']
# query and return top 5
xc = index.query(xq, top_k=5, include_metadata=True)
# iterate through results and print text
print("Answers:")
for match in xc['matches']:
    print(match['metadata']['text'])
```

```
Query: People on bicycles waiting at an intersection.
Answers:
A pair of people on bikes are waiting at a stoplight.
Bike riders wait to cross the street.
people on bicycles
Group of bike riders stopped in the street.
There are bicycles outside.
```

### Clean up

Shut down the endpoint by navigating to the Inference Endpoints **Overview** page and selecting **Delete endpoint**. Delete the Pinecone index with:

```Python Python theme={null}
pinecone.delete_index(index_name)
```

<Note>Once the index is deleted, you can't use it again.</Note>
