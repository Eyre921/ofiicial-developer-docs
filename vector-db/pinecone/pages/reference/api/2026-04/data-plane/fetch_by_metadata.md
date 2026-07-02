---
title: "Fetch records by metadata"
source: https://docs.pinecone.io/reference/api/2026-04/data-plane/fetch_by_metadata
path: reference/api/2026-04/data-plane/fetch_by_metadata
---

https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2026-04/db_data_2026-04.oas.yaml post /vectors/fetch_by_metadata
Look up and return records by metadata from a single namespace. The returned records include the vector data and metadata.
For guidance and examples, see [Fetch data](https://docs.pinecone.io/guides/manage-data/fetch-data).

<RequestExample>
  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X POST "https://$INDEX_HOST/vectors/fetch_by_metadata" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "Content-Type: application/json" \
    -H "X-Pinecone-Api-Version: 2026-04" \
    -d '{
      "namespace": "__default__",
      "filter": {"genre": {"$eq": "Action/Adventure"}},
      "limit": 2
    }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "vectors": {
      "0": {
        "id": "0",
        "values": [
          0.0234527588, 0.0291595459 ...
        ],
        "metadata": {
          "box-office": 2923706026,
          "genre": "Action/Adventure",
          "summary": "On the alien world of Pandora, paraplegic Marine Jake Sully uses an avatar to walk again and becomes torn between his mission and protecting the planet's indigenous Na'vi people. The film stars Sam Worthington, Zoe Saldana, and Sigourney Weaver.",
          "title": "Avatar",
          "year": 2009
        }
      },
      "1": {
        "id": "1",
        "values": [
          0.0397644043, 0.013053894, ...
        ],
        "metadata": {
          "box-office": 2799439100,
          "genre": "Action/Adventure",
          "summary": "In the aftermath of Thanos wiping out half of the universe, the remaining Avengers assemble once more to undo the chaos, leading to a time-traveling adventure. Stars Robert Downey Jr., Chris Evans, and Scarlett Johansson.",
          "title": "Avengers: Endgame",
          "year": 2019
        }
      }
    },
    "namespace": "__default__",
    "usage": {
      "readUnits": 1
    },
    "pagination": {
      "next": "Tm90aGluZyB0byBzZWUgaGVyZQo="
    }
  }
  ```
</ResponseExample>
