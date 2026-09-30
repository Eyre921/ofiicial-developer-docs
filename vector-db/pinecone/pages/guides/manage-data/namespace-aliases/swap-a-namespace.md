---
title: "Swap a namespace without downtime"
source: https://docs.pinecone.io/guides/manage-data/namespace-aliases/swap-a-namespace
path: guides/manage-data/namespace-aliases/swap-a-namespace
---

Refresh the data behind a namespace alias with no downtime: create an alias, ingest a new namespace, then atomically repoint reads to it.

<Note>
  Creating and managing aliases requires API version `2026-07` or later and is available through the REST API. Reading through an alias works on any API version, including the current SDKs.
</Note>

The primary use case for a [namespace alias](/guides/manage-data/namespace-aliases/overview) is swapping the data an application reads without a redeploy: re-ingest into a new namespace, validate it, then flip live reads to it in one call. This guide refreshes the data behind an alias named `example-alias`, moving it from `example-namespace-v1` to `example-namespace-v2` with no downtime. The examples use the vector API; the same alias substitution works on any read endpoint.

## Before you begin

Ensure you have the following:

* An existing index containing the namespace serving live traffic.
* A project role that can manage namespaces, such as [`DataPlaneEditor`](/guides/production/manage-rbac), `ProjectOwner`, or `ProjectManager`. Managing aliases needs the same access as managing namespaces directly.

## Swap the namespace

<Steps>
  <Step title="Create an alias">
    Create an alias pointing at the namespace serving live traffic. Specify a `name` for the alias and the `target_namespace` it points at.

    ```shell curl theme={null}
    # To get the unique host for an index,
    # see https://docs.pinecone.io/guides/manage-data/target-an-index
    PINECONE_API_KEY="YOUR_API_KEY"
    INDEX_HOST="INDEX_HOST"

    curl "https://$INDEX_HOST/namespace-aliases" \
      -H "Accept: application/json" \
      -H "Content-Type: application/json" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-07" \
      -d '{
            "name": "example-alias",
            "target_namespace": "example-namespace-v1"
          }'
    ```

    The response returns the alias:

    ```json curl theme={null}
    {
      "name": "example-alias",
      "target_namespace": "example-namespace-v1",
      "created_at": "2026-09-01T12:00:00Z",
      "updated_at": "2026-09-01T12:00:00Z"
    }
    ```
  </Step>

  <Step title="Read through the alias">
    Point your application's reads at the alias name. Pass it wherever you'd pass a namespace name; here, that's the `namespace` field in a query request.

    ```shell curl theme={null}
    PINECONE_API_KEY="YOUR_API_KEY"
    INDEX_HOST="INDEX_HOST"

    curl "https://$INDEX_HOST/query" \
      -H "Content-Type: application/json" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-07" \
      -d '{
            "namespace": "example-alias",
            "vector": [0.1, 0.2, 0.3, ...],
            "topK": 3,
            "includeMetadata": true
          }'
    ```

    The response's `namespace` field reports the namespace that served the read. You sent `example-alias`, and the read came back from `example-namespace-v1`, so you can verify what the alias points at from the read itself.
  </Step>

  <Step title="Ingest the new data">
    Ingest the refreshed data into a new namespace. Writes never use the alias, so live read traffic keeps landing on `example-namespace-v1` while you build `example-namespace-v2`.

    ```shell curl theme={null}
    PINECONE_API_KEY="YOUR_API_KEY"
    INDEX_HOST="INDEX_HOST"

    curl "https://$INDEX_HOST/vectors/upsert" \
      -H "Content-Type: application/json" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-07" \
      -d '{
            "namespace": "example-namespace-v2",
            "vectors": [
              { "id": "vec1", "values": [0.1, 0.2, 0.3, ...] }
            ]
          }'
    ```

    Validate `example-namespace-v2` by reading it directly by its own name.
  </Step>

  <Step title="Cut over in one call">
    Repoint the alias to the new namespace. The repoint is atomic (all or nothing, no partial state), and when the call returns success, all reads resolve to the new target.

    <Note>
      A paginated read (a list, or a filtered fetch) that's already in progress when you repoint finishes its remaining pages against the new target.
    </Note>

    ```shell curl theme={null}
    PINECONE_API_KEY="YOUR_API_KEY"
    INDEX_HOST="INDEX_HOST"

    curl -X PATCH "https://$INDEX_HOST/namespace-aliases/example-alias" \
      -H "Accept: application/json" \
      -H "Content-Type: application/json" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-07" \
      -d '{
            "target_namespace": "example-namespace-v2"
          }'
    ```
  </Step>

  <Step title="Verify the cutover">
    Describe the alias to confirm the current target and the last repoint time:

    ```shell curl theme={null}
    PINECONE_API_KEY="YOUR_API_KEY"
    INDEX_HOST="INDEX_HOST"

    curl -X GET "https://$INDEX_HOST/namespace-aliases/example-alias" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-Api-Version: 2026-07"
    ```

    The `target_namespace` now reads `example-namespace-v2`, and `updated_at` has advanced to the repoint time:

    ```json curl theme={null}
    {
      "name": "example-alias",
      "target_namespace": "example-namespace-v2",
      "created_at": "2026-09-01T12:00:00Z",
      "updated_at": "2026-09-01T12:30:00Z"
    }
    ```
  </Step>

  <Step title="Retire the old namespace">
    When you're ready, [delete](/guides/manage-data/manage-namespaces#delete-a-namespace) the old `example-namespace-v1` namespace. The delete succeeds now that no alias targets it. Before the repoint, the delete would have been rejected because the alias still pointed at it.
  </Step>
</Steps>

## See also

* [Namespace aliases overview](/guides/manage-data/namespace-aliases/overview)
* [Manage aliases](/guides/manage-data/namespace-aliases/manage-aliases)
