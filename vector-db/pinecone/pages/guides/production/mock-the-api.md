---
title: "Mock the Pinecone API for testing"
source: https://docs.pinecone.io/guides/production/mock-the-api
path: guides/production/mock-the-api
---

Run a local mock of the Pinecone API from its OpenAPI specs so tests and CI can exercise your Pinecone client code without an account or calls to Pinecone.

> [!NOTE]
>
> Pinecone Local, the in-memory emulator, reached end of life on October 7, 2026. If you used it for testing, the mock in this guide covers request and error-handling tests. It doesn't cover tests that write data and read it back, or tests that need real search results.

You can run a local mock of the Pinecone API from Pinecone's public [OpenAPI specs](https://github.com/pinecone-io/pinecone-api) using [Prism](https://github.com/stoplightio/prism), an open-source mock server. The mock checks each request against the spec, rejecting bad request bodies and missing headers, and answers with the example response from the spec. Use it in unit tests and CI to confirm that your code builds valid requests and handles responses and errors, without a Pinecone account or calls to Pinecone.

The mock doesn't store anything, and every call returns the same canned response no matter what you send. If you upsert a document and then fetch or search for it, you get the spec's example document, not yours. So you can't use the mock to test a write followed by a read, or to test search relevance. Run those tests against a [separate project](/admin/projects/create-a-project) in your Pinecone account.

## Before you begin

Ensure you have the following:

* [Docker](https://docs.docker.com/get-started/get-docker/) with Docker Compose
* [Git](https://git-scm.com/downloads)
* The [Pinecone Python SDK](/reference/sdks/python/overview) v10 or later, or the [Pinecone Node.js SDK](/reference/sdks/node/overview) v9 or later

## Run the mock

**1. Get the API specs**

Clone the repository that holds Pinecone's OpenAPI specs. Each API version has its own directory, such as `2026-07`.

```bash Terminal theme={null}
git clone --depth 1 https://github.com/pinecone-io/pinecone-api.git
```

**2. Define the mock services**

The Pinecone API is split across three specs, so you run one Prism container for each. In the directory that contains `pinecone-api`, create a `docker-compose.yaml` file with the following content:

```yaml docker-compose.yaml theme={null}
services:
  # Control plane: create, describe, list, and delete indexes
  pinecone-control-mock:
    image: stoplight/prism:5.14.3
    platform: linux/amd64
    command: mock -h 0.0.0.0 -p 5080 /specs/2026-07/db_control_2026-07.oas.yaml
    ports:
      - "5080:5080"
    volumes:
      - ./pinecone-api:/specs:ro

  # Data plane: upsert, query, fetch, and search data
  pinecone-data-mock:
    image: stoplight/prism:5.14.3
    platform: linux/amd64
    command: mock -h 0.0.0.0 -p 5081 /specs/2026-07/db_data_2026-07.oas.yaml
    ports:
      - "5081:5081"
    volumes:
      - ./pinecone-api:/specs:ro

  # Inference: embed and rerank
  pinecone-inference-mock:
    image: stoplight/prism:5.14.3
    platform: linux/amd64
    command: mock -h 0.0.0.0 -p 5082 /specs/2026-07/inference_2026-07.oas.yaml
    ports:
      - "5082:5082"
    volumes:
      - ./pinecone-api:/specs:ro
```

This guide uses the `2026-07` specs, the API version that the Pinecone Python SDK v10 and Pinecone Node.js SDK v9 send.

Prism publishes images only for Intel and AMD processors (`linux/amd64`), with no ARM build. On a Mac with Apple silicon, Docker runs them under emulation. The `platform` setting makes that explicit and silences Docker's platform warning.

> [!NOTE]
>
> Pin the Prism image to a version that starts. Every 5.15 image, including the `5` and `latest` tags, exits on startup with `TypeError: Cannot read properties of undefined (reading 'isPrimary')` on both Intel and Apple silicon. `5.14.3` is the newest version that works.

**3. Start the mock**

Start the three containers in the background:

```bash Terminal theme={null}
docker compose up -d
```

Prism takes several seconds to load each spec. When all three are ready, `docker compose logs` shows a line like this for each port:

```text Output theme={null}
pinecone-control-mock-1  | [4:00:17 AM] › [CLI] ▶  start     Prism is listening on http://0.0.0.0:5080
```

**4. Point the SDK at the mock**

Set the client's host to the control-plane mock, and target the index by host with the data-plane mock. Any API key works, but the SDK requires one. In Python, use the HTTP client, not the gRPC client, because the mock doesn't serve gRPC.

Don't target the index by name. The SDK would describe the index to look up its host, and the mock returns the spec's example host on `pinecone.io`, not the mock.

```python Python theme={null}
from pinecone import Pinecone

pc = Pinecone(api_key="test-key", host="http://localhost:5080")
index = pc.index(host="http://localhost:5081")

description = pc.indexes.describe("example-index")
print(description.name)

upserted = index.documents.upsert(
    namespace="example-namespace",
    documents=[{"_id": "article-1", "title": "Mocking APIs", "body": "Mock servers return canned responses."}],
)
print(upserted.upserted_count)

results = index.documents.search(
    namespace="example-namespace",
    top_k=3,
    score_by=[{"type": "text", "fields": ["body"], "query": "canned responses"}],
)
print(results.matches[0].id)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone';

const pc = new Pinecone({ apiKey: 'test-key', controllerHostUrl: 'http://localhost:5080' });
const index = pc.index({ host: 'http://localhost:5081', namespace: 'example-namespace' });

const description = await pc.describeIndex('example-index');
console.log(description.name);

const upserted = await index.documents.upsert({
  documents: [{ _id: 'article-1', title: 'Mocking APIs', body: 'Mock servers return canned responses.' }],
});
console.log(upserted.upsertedCount);

const results = await index.documents.search({
  scoreBy: [{ type: 'text', fields: ['body'], query: 'canned responses' }],
  topK: 3,
});
console.log(results.matches[0]._id);
```

All three calls succeed, and all three return the spec's examples instead of results based on your request. The index you described is named `my-index`, the upsert reports two documents even though you sent one, and the top match is `doc-1`:

```text Output theme={null}
my-index
2
doc-1
```

The Vectors API methods, such as `upsert`, `query`, and `fetch`, work against the mock the same way.

## Mock inference calls

The Pinecone Inference endpoints, such as `embed` and `rerank`, are in a separate spec, so they're served from a separate port. Create a second client with the inference mock as its host:

```python Python theme={null}
from pinecone import Pinecone

pc_inference = Pinecone(api_key="test-key", host="http://localhost:5082")

result = pc_inference.inference.rerank(
    model="bge-reranker-v2-m3",
    query="What is the capital of France?",
    documents=["Paris is the capital of France.", "Berlin is the capital of Germany."],
    top_n=2,
)
print(result.data[0].score)
```

```javascript JavaScript theme={null}
import { Pinecone } from '@pinecone-database/pinecone';

const pcInference = new Pinecone({ apiKey: 'test-key', controllerHostUrl: 'http://localhost:5082' });

const result = await pcInference.inference.rerank({
  model: 'bge-reranker-v2-m3',
  query: 'What is the capital of France?',
  documents: ['Paris is the capital of France.', 'Berlin is the capital of Germany.'],
  topN: 2,
});
console.log(result.data[0].score);
```

The top result's score is the spec's example score:

```text Output theme={null}
0.5
```

## Test error handling

To test how your code handles API errors, ask Prism for a specific status code with the `Prefer` header. Prism returns that code for every request from a client that sets the header. Data-plane endpoints return any `4xx` or `5xx` code. Control-plane and inference endpoints return only the codes their spec lists. For any other code, Prism responds with a `404` that says the requested status code isn't defined. For more on handling errors, see [Error handling](/guides/production/error-handling).

### Example

Return `503 Service Unavailable` from a document search to test your retry handling:

```python Python theme={null}
from pinecone import Pinecone
from pinecone.errors import ServiceError

pc = Pinecone(
    api_key="test-key",
    host="http://localhost:5080",
    additional_headers={"Prefer": "code=503"},
)
index = pc.index(host="http://localhost:5081")

try:
    index.documents.search(
        namespace="example-namespace",
        top_k=3,
        score_by=[{"type": "text", "fields": ["body"], "query": "canned responses"}],
    )
except ServiceError as e:
    print(f"Service unavailable: {e.status_code}")
```

```javascript JavaScript theme={null}
import { Pinecone, Errors } from '@pinecone-database/pinecone';

const pc = new Pinecone({
  apiKey: 'test-key',
  controllerHostUrl: 'http://localhost:5080',
  additionalHeaders: { Prefer: 'code=503' },
});
const index = pc.index({ host: 'http://localhost:5081', namespace: 'example-namespace' });

try {
  await index.documents.search({
    scoreBy: [{ type: 'text', fields: ['body'], query: 'canned responses' }],
    topK: 3,
  });
} catch (e) {
  if (e instanceof Errors.PineconeMaxRetriesExceededError) {
    console.log(`Service unavailable: ${e.name}`);
  } else {
    throw e;
  }
}
```

Both SDKs retry a `503` three times before they raise an error, so this test takes a few seconds. The Python SDK raises `ServiceError`, and the Node.js SDK raises `PineconeMaxRetriesExceededError`.

## Run the mock in CI

In a [GitHub Actions](https://docs.github.com/en/actions) workflow, start the mock with Docker Compose as a step before your tests run. GitHub's `services` containers can't pass Prism its `mock` command or mount the specs, so you can't use them here.

The following workflow assumes your repository has the `docker-compose.yaml` file from this guide at its root and your tests in a `tests` directory. It clones the specs, starts the mock, waits until all three ports respond, and runs the tests:

```yaml .github/workflows/test.yaml theme={null}
name: Test

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository code
        uses: actions/checkout@v7

      - name: Get the Pinecone API specs
        run: git clone --depth 1 https://github.com/pinecone-io/pinecone-api.git

      - name: Start the mock
        run: |
          docker compose up -d
          for port in 5080 5081 5082; do
            timeout 60 sh -c "until curl -s localhost:$port > /dev/null; do sleep 1; done"
          done

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install "pinecone>=10" "pytest"

      - name: Run tests
        run: pytest tests/

      - name: Show mock logs on failure
        if: failure()
        run: docker compose logs
```

## Limitations

Some calls fail against the mock even though they work against Pinecone:

* **Upserting records into a legacy integrated index**: The legacy Records API methods, `upsert_records` and `upsertRecords`, send newline-delimited JSON, which Prism can't parse, so the mock rejects them with a `422`. Searching a legacy integrated index works, and so does upserting into a document index.
* **Embedding with the Node.js SDK**: The mock's embed response doesn't include a valid `vector_type` for each embedding, so `inference.embed()` throws `No variant of Embedding exists with 'vectorType=undefined'`. Embedding works with the Python SDK, and reranking works with both.

## Stop the mock

Stop and remove the containers:

```bash Terminal theme={null}
docker compose down
```
