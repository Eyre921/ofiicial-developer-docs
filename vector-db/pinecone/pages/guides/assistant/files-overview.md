---
title: "Files in Pinecone Assistant"
source: https://docs.pinecone.io/guides/assistant/files-overview
path: guides/assistant/files-overview
---

Overview of Pinecone Assistant files: supported file types (PDF, DOCX, JSON, MD, TXT), metadata filters, storage, and signed URL access.

Before you can chat with the assistant, you need to [upload files](/guides/assistant/manage-files#upload-a-local-file). The files provide your assistant with context and information to reference when generating responses. Files aren't shared across assistants.

### Supported file types

Pinecone Assistant supports the following file types:

* DOCX (.docx)
* JSON (.json)
* Markdown (.md)
* PDF (.pdf)
* Text (.txt)

> [!NOTE]
>
> For PDF files, assistants support [multimodal context](/guides/assistant/multimodal), allowing them to analyze and gather context from images. This feature is in [public preview](/release-notes/feature-availability).

For information about file size and storage limits, see [Pricing and limits](/guides/assistant/pricing-and-limits).

### File storage

Files are uploaded to Google Cloud Storage in the assistant's region (`us` or `eu`). The assistant processes the files and stores the resulting embeddings in a Pinecone-managed index, separate from the indexes in your projects.

Some API responses include a `signed_url` field, which provides temporary, read-only access to one of the assistant's files. The URL is [signed](https://cloud.google.com/storage/docs/access-control/signed-urls) and hard to guess, but publicly accessible, so treat it as sensitive. `signed_url` links expire in one hour.

### File identifiers

Each file in an assistant has a unique identifier. File IDs can be:

* **System-generated**: When you [upload a file](/guides/assistant/upload-files#upload-a-local-file) using `POST`, the system assigns a UUID as the file ID.
* **User-provided**: When you [upsert a file](/guides/assistant/upload-files#upsert-a-file) using `PUT`, you provide a custom file ID. User-provided IDs must be 1-128 characters long and can contain alphanumeric characters, hyphens, and underscores. Requires [API version](/reference/api/versioning) `2026-04` or later.

### File metadata

You can [upload a file with metadata](/guides/assistant/upload-files#upload-a-file-with-metadata), which allows you to store additional information about the file as key-value pairs.

> [!WARNING]
>
> File metadata can be set only when the file is uploaded. You cannot update metadata after the file is uploaded.

File metadata can be used for the following purposes:

* [Filtering chat responses](/guides/assistant/chat-with-assistant#filter-chat-with-metadata): Specify filters on assistant responses so only files that match the metadata filter are referenced in the response. Chat requests without metadata filters don't consider metadata.
* [Viewing a filtered list of files](/guides/assistant/manage-files#view-a-filtered-list-of-files): Use metadata filters to list files in an assistant that match specific criteria.

#### Supported metadata size and format

Pinecone Assistant supports 16 KB of metadata per file.

* Metadata fields must be key-value pairs in a flat JSON object. Nested JSON objects aren't supported.
* Keys must be strings and must not start with a `$`.
* Values must be one of the following data types:
  * String
  * Integer (converted to a 64-bit floating point by Pinecone)
  * Floating point
  * Boolean (`true`, `false`)
  * List of strings
* Null metadata values aren't supported. Instead of setting a key to `null`, remove the key from the metadata payload.

**Examples**

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

#### Metadata query language

Pinecone's filtering language supports the following operators:

| Operator | Function | Supported types |
| :- | :- | :- |
| `$eq` | Matches files with metadata values that are equal to a specified value. Example: `{"genre": {"$eq": "documentary"}}` | Number, string, boolean |
| `$ne` | Matches files with metadata values that aren't equal to a specified value. Example: `{"genre": {"$ne": "drama"}}` | Number, string, boolean |
| `$gt` | Matches files with metadata values that are greater than a specified value. Example: `{"year": {"$gt": 2019}}` | Number |
| `$gte` | Matches files with metadata values that are greater than or equal to a specified value. Example:`{"year": {"$gte": 2020}}` | Number |
| `$lt` | Matches files with metadata values that are less than a specified value. Example: `{"year": {"$lt": 2020}}` | Number |
| `$lte` | Matches files with metadata values that are less than or equal to a specified value. Example: `{"year": {"$lte": 2020}}` | Number |
| `$in` | Matches files with metadata values that are in a specified array. The array can hold up to [10,000 values](/reference/api/database-limits/operation-limits#metadata-filter-limits). Example: `{"genre": {"$in": ["comedy", "documentary"]}}` | String, number |
| `$nin` | Matches files with metadata values that aren't in a specified array. The array can hold up to [10,000 values](/reference/api/database-limits/operation-limits#metadata-filter-limits). Example: `{"genre": {"$nin": ["comedy", "documentary"]}}` | String, number |
| `$exists` | Matches files with the specified metadata field. Example: `{"genre": {"$exists": true}}` | Number, string, boolean |
| `$and` | Joins query clauses with a logical `AND`. Example: `{"$and": [{"genre": {"$eq": "drama"}}, {"year": {"$gte": 2020}}]}` | - |
| `$or` | Joins query clauses with a logical `OR`. Example: `{"$or": [{"genre": {"$eq": "drama"}}, {"year": {"$gte": 2020}}]}` | - |
| `$not` | Matches files that don't match the wrapped clause. Example: `{"genre": {"$not": {"$eq": "drama"}}}` | - |

At the top level, list one or more fields (combined with implicit AND) or combine clauses with the logical operators `$and` and `$or`. Use `$not` to negate a clause, as shown in the table. A bare comparison operator (like `$gt`) can't appear at the top level. Nest it under a field.

A metadata field can hold an array of strings, such as `{"genre": ["comedy", "documentary"]}`. A filter on that field matches when any value in the array satisfies it, so each of these filters matches:

```json JSON theme={null}
{"genre": "comedy"}
{"genre": {"$in": ["documentary", "action"]}}
{"$and": [{"genre": "comedy"}, {"genre": "documentary"}]}
```

These filters don't match, because the array has no `"drama"` value and because `$ne` and `$nin` exclude an item when any of its values matches:

```json JSON theme={null}
{"$and": [{"genre": "comedy"}, {"genre": "drama"}]}
{"genre": {"$ne": "comedy"}}
```

A filter value can't be an array. To match several values, use `$in`. These filters are invalid and return a `400` error:

```json JSON theme={null}
{"genre": ["comedy", "documentary"]}
{"genre": {"$eq": ["comedy", "documentary"]}}
```
