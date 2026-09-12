---
title: "Configure metadata indexing"
source: https://docs.pinecone.io/guides/index-data/configure-metadata-indexing
path: guides/index-data/configure-metadata-indexing
---

Limit metadata indexing in Pinecone to the fields you filter on, to keep index building and query execution fast.

<Note>
  Setting metadata indexing requires the `2026-07` version of the API or later.
</Note>

Pinecone indexes all metadata fields by default. However, large amounts of metadata can cause slower [index building](/guides/core-concepts/architecture#index-builder) as well as slower [query execution](/guides/core-concepts/architecture#query-executors), particularly when data is not cached in a query executor's memory and local SSD and must be fetched from object storage.

To prevent performance issues due to excessive metadata, you can limit metadata indexing to the fields that you plan to use for [query filtering](/guides/search/filter-by-metadata).

## Set metadata indexing

You can limit metadata indexing when you create an index with [integrated embedding](/guides/index-data/indexing-overview#integrated-embedding), or at [namespace creation](/reference/api/latest/data-plane/createnamespace) for any index:

* Index-level metadata indexing rules apply to all namespaces that don't have their own rules.
* Namespace-level metadata indexing rules override index-level rules.

A document index doesn't accept metadata fields in its schema at creation, so limit its metadata indexing at the namespace level.

For example, if you store records that represent chunks of a document, each with many metadata fields, but you plan to filter on only a few, index just those fields. Set `filterable` to `true` for each field to index. To leave a field unindexed, omit it (`filterable: false` isn't supported).

<Warning>
  Metadata indexing cannot be changed after index or namespace creation.
</Warning>

<CodeGroup>
  ```shell Index-level metadata indexing theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/indexes/create-for-model" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
          "name": "example-index-metadata",
          "cloud": "aws",
          "region": "us-east-1",
          "embed": {
            "model": "llama-text-embed-v2",
            "field_map": {
              "text": "chunk_text"
            }
          },
          "schema": {
            "fields": {
              "document_id": {
                "filterable": true
              },
              "document_title": {
                "filterable": true
              },
              "chunk_number": {
                "filterable": true
              },
              "document_url": {
                "filterable": true
              },
              "created_at": {
                "filterable": true
              }
            }
          },
          "deletion_protection": "disabled"
        }'
  ```

  ```shell Namespace-level metadata indexing theme={null}
  # To learn how to get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl "https://$INDEX_HOST/namespaces" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2026-07" \
    -d '{
          "name": "example-namespace",
          "schema": {
            "fields": {
              "document_id": {
                "filterable": true
              },
              "document_title": {
                "filterable": true
              },
              "chunk_number": {
                "filterable": true
              },
              "document_url": {
                "filterable": true
              },
              "created_at": {
                "filterable": true
              }
            }
          }
        }'
  ```
</CodeGroup>

## Check metadata indexing

To check which metadata fields are indexed, you can describe the index or namespace:

<CodeGroup>
  ```shell Describe index theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X GET "https://api.pinecone.io/indexes/example-index-metadata" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-Api-Version: 2026-07"
  ```

  ```shell Describe namespace theme={null}
  # To learn how to get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/namespaces/example-namespace" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-Api-Version: 2026-07"
  ```
</CodeGroup>

The response includes the `schema` object with the names of the metadata fields explicitly indexed during index or namespace creation, alongside any search fields declared on the index.

<Note>
  The response does not include unindexed metadata fields or metadata fields indexed by default.
</Note>

<CodeGroup>
  ```json Describe index theme={null}
  {
    "name": "example-index-metadata",
    "host": "example-index-metadata-fa77d8e.svc.aped-4627-b74a.pinecone.io",
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "deployment": {
      "deployment_type": "managed",
      "region": "us-east-1",
      "cloud": "aws",
      "environment": "aped-4627-b74a"
    },
    "read_capacity": {
      "mode": "OnDemand",
      "status": {
        "state": "Ready",
        "current_shards": null,
        "current_replicas": null
      }
    },
    "schema": {
      "fields": {
        "chunk_text": {
          "type": "semantic_text",
          "description": null,
          "model": "llama-text-embed-v2",
          "dimension": 1024,
          "metric": "cosine",
          "write_parameters": {
            "dimension": 1024,
            "input_type": "passage",
            "truncate": "END"
          },
          "read_parameters": {
            "dimension": 1024,
            "input_type": "query",
            "truncate": "END"
          }
        },
        "document_id": {
          "filterable": true
        },
        "document_title": {
          "filterable": true
        },
        "chunk_number": {
          "filterable": true
        },
        "document_url": {
          "filterable": true
        },
        "created_at": {
          "filterable": true
        }
      }
    },
    "tags": null,
    "deletion_protection": "disabled"
  }
  ```

  ```json Describe namespace theme={null}
  {
    "name": "example-namespace",
    "record_count": "20000",
    "size_bytes": "10000000",
    "schema": {
      "fields": {
        "document_title": {
          "filterable": true
        },
        "document_url": {
          "filterable": true
        },
        "chunk_number": {
          "filterable": true
        },
        "document_id": {
          "filterable": true
        },
        "created_at": {
          "filterable": true
        }
      }
    }
  }
  ```
</CodeGroup>
