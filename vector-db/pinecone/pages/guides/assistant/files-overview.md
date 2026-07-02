---
title: "Files in Pinecone Assistant"
source: https://docs.pinecone.io/guides/assistant/files-overview
path: guides/assistant/files-overview
---

Understand supported file types and metadata in Pinecone Assistant.

Before you can chat with the assistant, you need to [upload files](/guides/assistant/manage-files#upload-a-local-file). The files provide your assistant with context and information to reference when generating responses. Files are not shared across assistants.

### Supported file types

Pinecone Assistant supports the following file types:

* DOCX (.docx)
* JSON (.json)
* Markdown (.md)
* PDF (.pdf)
* Text (.txt)

<Note>
  For PDF files, assistants support [multimodal context](/guides/assistant/multimodal), allowing them to analyze and gather context from images. This feature is in [public preview](/release-notes/feature-availability).
</Note>

For information about file size and storage limits, see [Pricing and limits](/guides/assistant/pricing-and-limits).

### File storage

Files are uploaded to Google Cloud Storage (`us-central1` region) and to your organization's Pinecone vector database. The assistant processes the files, so data is not sent outside of blob storage or Pinecone.

Some API responses include a `signed_url` field, which provides temporary, read-only access to one of the assistant's files. The URL is [signed](https://cloud.google.com/storage/docs/access-control/signed-urls) and hard to guess, but publicly accessible, so treat it as sensitive. `signed_url` links expire in one hour.

### File identifiers

Each file in an assistant has a unique identifier. File IDs can be:

* **System-generated**: When you [upload a file](/guides/assistant/upload-files#upload-a-local-file) using `POST`, the system assigns a UUID as the file ID.
* **User-provided**: When you [upsert a file](/guides/assistant/upload-files#upsert-a-file) using `PUT`, you provide a custom file ID. User-provided IDs must be 1-128 characters long and can contain alphanumeric characters, hyphens, and underscores. Requires [API version](/reference/api/versioning) `2026-04` or later.

### File metadata

You can [upload a file with metadata](/guides/assistant/upload-files#upload-a-file-with-metadata), which allows you to store additional information about the file as key-value pairs.

<Warning>
  File metadata can be set only when the file is uploaded. You cannot update metadata after the file is uploaded.
</Warning>

File metadata can be used for the following purposes:

* [Filtering chat responses](/guides/assistant/chat-with-assistant#filter-chat-with-metadata): Specify filters on assistant responses so only files that match the metadata filter are referenced in the response. Chat requests without metadata filters do not consider metadata.
* [Viewing a filtered list of files](/guides/assistant/manage-files#view-a-filtered-list-of-files): Use metadata filters to list files in an assistant that match specific criteria.

#### Supported metadata size and format

Pinecone Assistant supports 16 KB of metadata per file.

* Metadata fields must be key-value pairs in a flat JSON object. Nested JSON objects are not supported.
* Keys must be strings and must not start with a `$`.
* Values must be one of the following data types:
  * String
  * Integer (converted to a 64-bit floating point by Pinecone)
  * Floating point
  * Boolean (`true`, `false`)
  * List of strings
* Null metadata values aren't supported. Instead of setting a key to `null`, remove the key from the metadata payload.

**Examples**

<CodeGroup>
  ```json Valid metadata theme={null}
  {
    "document_id": "document1",
    "document_title": "Introduction to Vector Databases",
    "chunk_number": 1,
    "chunk_text": "First chunk of the document content...",
    "is_public": true,
    "tags": ["beginner", "database", "vector-db"],
    "scores": ["85", "92"]
  }
  ```

  ```json Invalid metadata theme={null}
  {
    "document": {       // Nested JSON objects are not supported
      "document_id": "document1",
      "document_title": "Introduction to Vector Databases",
    },
    "$chunk_number": 1, // Keys must not start with a `$`
    "chunk_text": null, // Null values are not supported
    "is_public": true,
    "tags": ["beginner", "database", "vector-db"],
    "scores": [85, 92]  // Lists of non-strings are not supported
  }
  ```
</CodeGroup>

#### Metadata query language

Pinecone's filtering language supports the following operators:

| Operator  | Function                                                                                                                   | Supported types         |
| :-------- | :------------------------------------------------------------------------------------------------------------------------- | :---------------------- |
| `$eq`     | Matches  with metadata values that are equal to a specified value. Example: `{"genre": {"$eq": "documentary"}}`            | Number, string, boolean |
| `$ne`     | Matches  with metadata values that are not equal to a specified value. Example: `{"genre": {"$ne": "drama"}}`              | Number, string, boolean |
| `$gt`     | Matches  with metadata values that are greater than a specified value. Example: `{"year": {"$gt": 2019}}`                  | Number                  |
| `$gte`    | Matches  with metadata values that are greater than or equal to a specified value. Example:`{"year": {"$gte": 2020}}`      | Number                  |
| `$lt`     | Matches  with metadata values that are less than a specified value. Example: `{"year": {"$lt": 2020}}`                     | Number                  |
| `$lte`    | Matches  with metadata values that are less than or equal to a specified value. Example: `{"year": {"$lte": 2020}}`        | Number                  |
| `$in`     | Matches  with metadata values that are in a specified array. Example: `{"genre": {"$in": ["comedy", "documentary"]}}`      | String, number          |
| `$nin`    | Matches  with metadata values that are not in a specified array. Example: `{"genre": {"$nin": ["comedy", "documentary"]}}` | String, number          |
| `$exists` | Matches  with the specified metadata field. Example: `{"genre": {"$exists": true}}`                                        | Number, string, boolean |
| `$and`    | Joins query clauses with a logical `AND`. Example: `{"$and": [{"genre": {"$eq": "drama"}}, {"year": {"$gte": 2020}}]}`     | -                       |
| `$or`     | Joins query clauses with a logical `OR`. Example: `{"$or": [{"genre": {"$eq": "drama"}}, {"year": {"$gte": 2020}}]}`       | -                       |

<Note>
  Only `$and` and `$or` are allowed at the top level of the query expression.
</Note>

<Note>
  Each `$in` or `$nin` operator accepts a maximum of 10,000 values. Exceeding this limit will cause the request to fail. For more information, see [Metadata filter limits](/reference/api/database-limits#metadata-filter-limits).
</Note>

For example, the following has a `"genre"` metadata field with a list of strings:

```JSON JSON theme={null}
{ "genre": ["comedy", "documentary"] }
```

This means `"genre"` takes on both values, and requests with the following filters will match:

```JSON JSON theme={null}
{"genre":"comedy"}

{"genre": {"$in":["documentary","action"]}}

{"$and": [{"genre": "comedy"}, {"genre":"documentary"}]}
```

However, requests with the following filter will **not** match:

```JSON JSON theme={null}
{ "$and": [{ "genre": "comedy" }, { "genre": "drama" }] }
```

Additionally, requests with the following filters will **not** match because they are invalid. They will result in a compilation error:

```json JSON theme={null}
# INVALID QUERY:
{"genre": ["comedy", "documentary"]}
```

```json JSON theme={null}
# INVALID QUERY:
{"genre": {"$eq": ["comedy", "documentary"]}}
```
