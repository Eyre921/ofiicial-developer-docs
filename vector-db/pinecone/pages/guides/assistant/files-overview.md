---
title: "Files in Pinecone Assistant"
source: https://docs.pinecone.io/guides/assistant/files-overview
path: guides/assistant/files-overview
---

Overview of Pinecone Assistant files: supported file types (PDF, DOCX, JSON, MD, TXT), metadata filters, storage, and signed URL access.

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
| `$exists` | Matches  with the specified metadata field. Exam# Architecture
Source: https://docs.pinecone.io/guides/core-concepts/architecture

Learn how Pinecone is built, from organizations, projects, indexes, and namespaces down to the infrastructure that stores and serves your data.

Pinecone's architecture has two layers: the resource hierarchy that organizes your data, and the serverless infrastructure that stores and serves it.

## Resource hierarchy

Your data in Pinecone is organized as a hierarchy of resources. An [organization](/guides/core-concepts/key-terms#organization) contains [projects](/guides/core-concepts/key-terms#project), a project contains [indexes](/guides/core-concepts/key-terms#index), and an index is divided into [namespaces](/guides/core-concepts/key-terms#namespace) that hold your [records](/guides/core-concepts/key-terms#record) or [documents](/guides/core-concepts/key-terms#document). For a definition of each object, see [Key terms](/guides/core-concepts/key-terms).

<img />

<img />

## Serverless infrastructure

Pinecone runs as a managed service on AWS, GCP, and Azure cloud platforms. When you send a request to Pinecone, it goes through an [API gateway](#api-gateway) that routes it to either a global [control plane](#control-plane) or a regional [data plane](#data-plane). All your vector data is stored in highly efficient, distributed [object storage](#object-storage).

<img />

<img />

### API gateway

Every request to Pinecone includes an [API key](/guides/projects/manage-api-keys) that's assigned to a specific [project](/guides/projects/understanding-projects). The API gateway first validates your API key to make sure you have permission to access the project. Once validated, it routes your request to either the global control plane (for managing projects and indexes) or a regional data plane (for reading and writing data), depending on what you're trying to do.

### Control plane

The global control plane manages your organizational resources like projects and indexes. It uses a dedicated database to keep track of all these objects. The control plane also handles billing, user management, and coordinates operations across different regions.

### Data plane

The data plane handles all requests to write and read records in [indexes](/guides/index-data/indexing-overview) within a specific [cloud region](/guides/index-data/create-an-index#cloud-regions). Each index is divided into one or more logical [namespaces](/guides/index-data/indexing-overview#namespaces), and all your data read and write requests target a specific namespace.

Pinecone separates write and read operations into different paths, with each scaling independently based on demand. This separation ensures that your queries never slow down your writes, and your writes never slow down your queries.

### Object storage

For each namespace in a serverless index, Pinecone organizes records into immutable files called slabs. These slabs are [optimized for fast querying](#index-builder) and stored in distributed object storage that provides virtually unlimited scalability and high availability.

## Write path

<img />

<img />

### Request log

When you send a write request (to add, update, or delete records), the [data plane](#data-plane) first logs the request details with a unique sequence number (LSN). This ensures all operations happen in the correct order and provides a way to track the state of the index.

Pinecone immediately returns a `200 OK` response, guaranteeing that your write is durable and won't be lost. The system then processes your write in the background.

### Index builder

The index builder stores your write data in an in-memory structure called a memtable. This includes your vector data, any metadata you've attached, and the sequence number. If you're updating or deleting a record, the system also tracks how to handle the old version during queries.

Periodically, the index builder moves data from the memtable to permanent storage. In [object storage](#object-storage), your data is organized into immutable files called slabs. These slabs are optimized for query performance. Smaller slabs use fast indexing techniques that provide good performance with minimal resource requirements. As slabs grow, the system merges them into larger slabs that use more sophisticated methods that provide better performance at scale. This adaptive process both optimizes query performance for each slab and amortizes the cost of more expensive indexing through the lifetime of the namespace.

<Note>
  All read operations check the memtable first, so you can immediately search data that you've just written, even before it's moved to permanent storage. For more details, see [Query executors](#query-executors).
</Note>

## Read path

<img />

<img />

### Query routers

When you send a search query, the [data plane](#data-plane) first validates your request and checks that it meets system limits like [rate and object limits](/reference/api/database-limits). The query router then identifies which slabs contain relevant data and routes your query to the appropriate executors. It also searches the memtable for any recent data that hasn't been moved to permanent storage yet.

### Query executors

Each query executor searches through its assigned slabs and returns the most relevant candidates to the query router. If your query includes metadata filters, the executors exclude records that don't match your criteria before finding the best matches.

Most of the time, the slabs are cached in memory or on local SSD, which provides very fast query performance. If a slab isn't cached (which happens when it's accessed for the first time or hasn't been used recently), the executor fetches it from object storage and caches it for future queries.

The query router then combines results from all executors, removes duplicates, merges them with results from the memtable, and returns the final set of best matches to you.
