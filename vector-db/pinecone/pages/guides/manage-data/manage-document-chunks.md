---
title: "Manage document chunks"
source: https://docs.pinecone.io/guides/manage-data/manage-document-chunks
path: guides/manage-data/manage-document-chunks
---

Fetch, search, delete, and replace all chunks of a source document in Pinecone using structured ID prefixes and a document_id metadata field.

When you split a long source document into chunks, each chunk is stored as its own document (in a document index) or record (in a vector index). To work with all of a source document's chunks at once, give each chunk a [structured ID](/guides/index-data/data-modeling#use-structured-ids) prefixed with the source document's ID, and a `document_id` metadata field.

Each task shows a document index first, then a vector index. The document-index code assumes a `chunk_text` field declared with `embed` for [integrated embedding](/guides/search/integrated-embedding), so Pinecone generates the vectors, and requires API version `2026-07` (Python SDK `10.1.0` or later). The vector-index code assumes you generate the vectors yourself.

> [!NOTE]
>
> Pinecone is [eventually consistent](/guides/index-data/check-data-freshness), so a read right after a write (upsert, update, or delete) may not return the latest data. If you need to read immediately after writing, add a short delay or [retry logic](/guides/production/error-handling#implement-retry-logic).

## Upsert chunks

[Upsert](/guides/index-data/upsert-data) each chunk with its structured ID and `document_id`, plus any other metadata you want to filter on or display. On a document index with integrated embedding, each upsert is capped at 96 documents instead of 1,000:

> [tab] Document index
>
> ```python Python theme={null}
> from pinecone import Pinecone
>
> pc = Pinecone(api_key="YOUR_API_KEY")
>
> # To get the unique host for an index,
> # see https://docs.pinecone.io/guides/manage-data/target-an-index
> index = pc.index(host="INDEX_HOST")
>
> # Pinecone embeds `chunk_text` on write.
> # The other fields are stored as metadata.
> index.documents.upsert(
>     namespace="example-namespace",
>     documents=[
>         {
>             "_id": "document1#chunk1",
>             "chunk_text": "First chunk of the document content...",
>             "document_id": "document1",
>             "document_title": "Introduction to Vector Databases",
>             "chunk_number": 1,
>             "document_url": "https://example.com/docs/document1",
>             "created_at": "2024-01-15",
>             "document_type": "tutorial"
>         },
>         {
>             "_id": "document1#chunk2",
>             "chunk_text": "Second chunk of the document content...",
>             "document_id": "document1",
>             "document_title": "Introduction to Vector Databases",
>             "chunk_number": 2,
>             "document_url": "https://example.com/docs/document1",
>             "created_at": "2024-01-15",
>             "document_type": "tutorial"
>         },
>         {
>             "_id": "document1#chunk3",
>             "chunk_text": "Third chunk of the document content...",
>             "document_id": "document1",
>             "document_title": "Introduction to Vector Databases",
>             "chunk_number": 3,
>             "document_url": "https://example.com/docs/document1",
>             "created_at": "2024-01-15",
>             "document_type": "tutorial"
>         },
>     ],
> )
> ```

> [tab] Vector index
>
> ```python Python theme={null}
> from pinecone.grpc import PineconeGRPC as Pinecone
>
> pc = Pinecone(api_key="YOUR_API_KEY")
>
> # To get the unique host for an index,
> # see https://docs.pinecone.io/guides/manage-data/target-an-index
> index = pc.index(host="INDEX_HOST", grpc=True)
>
> # Replace with each chunk's embedding, which must match the index's dimension (1536 in this example)
> chunk1_vector = [0.1, 0.2] * 768
> chunk2_vector = [0.2, 0.1] * 768
> chunk3_vector = [0.3, 0.1] * 768
>
> index.upsert(
>   namespace="example-namespace",
>   vectors=[
>     {
>       "id": "document1#chunk1", 
>       "values": chunk1_vector,
>       "metadata": {
>         "document_id": "document1",
>         "document_title": "Introduction to Vector Databases",
>         "chunk_number": 1,
>         "chunk_text": "First chunk of the document content...",
>         "document_url": "https://example.com/docs/document1",
>         "created_at": "2024-01-15",
>         "document_type": "tutorial"
>       }
>     },
>     {
>       "id": "document1#chunk2", 
>       "values": chunk2_vector,
>       "metadata": {
>         "document_id": "document1",
>         "document_title": "Introduction to Vector Databases", 
>         "chunk_number": 2,
>         "chunk_text": "Second chunk of the document content...",
>         "document_url": "https://example.com/docs/document1",
>         "created_at": "2024-01-15",
>         "document_type": "tutorial"
>       }
>     },
>     {
>       "id": "document1#chunk3", 
>       "values": chunk3_vector,
>       "metadata": {
>         "document_id": "document1",
>         "document_title": "Introduction to Vector Databases",
>         "chunk_number": 3, 
>         "chunk_text": "Third chunk of the document content...",
>         "document_url": "https://example.com/docs/document1",
>         "created_at": "2024-01-15",
>         "document_type": "tutorial"
>       }
>     }
>   ]
> )
> ```

## Search within a document

To search only one source document's chunks, add a [metadata filter](/guides/search/filter-by-metadata#metadata-filter-expressions) on `document_id`. On a document index, you search with query text and Pinecone embeds it:

> [tab] Document index
>
> ```python Python theme={null}
> from pinecone import Pinecone
>
> pc = Pinecone(api_key="YOUR_API_KEY")
>
> # To get the unique host for an index,
> # see https://docs.pinecone.io/guides/manage-data/target-an-index
> index = pc.index(host="INDEX_HOST")
>
> filtered_results = index.documents.search(
>     namespace="example-namespace",
>     top_k=3,
>     score_by=[
>         {"type": "embed", "fields": ["chunk_text"], "query": "What is a vector database?"}
>     ],
>     filter={"document_id": {"$eq": "document1"}},
>     include_fields=["chunk_text"],
> )
>
> for match in filtered_results.matches:
>     print(match._id, match._score, match.chunk_text)
> ```

> [tab] Vector index
>
> ```python Python theme={null}
> from pinecone.grpc import PineconeGRPC as Pinecone
>
> pc = Pinecone(api_key="YOUR_API_KEY")
>
> # To get the unique host for an index,
> # see https://docs.pinecone.io/guides/manage-data/target-an-index
> index = pc.index(host="INDEX_HOST", grpc=True)
>
> # Replace with your query embedding, which must match the index's dimension (1536 in this example)
> query_vector = [0.1, 0.2] * 768
>
> filtered_results = index.query(
>     namespace="example-namespace",
>     vector=query_vector,
>     top_k=3,
>     filter={
>         "document_id": {"$eq": "document1"}
>     },
>     include_metadata=True,
>     include_values=False
> )
>
> print(filtered_results)
> ```

## Fetch all chunks of a document

To retrieve all of a source document's chunks, [list](/guides/manage-data/list-record-ids) their IDs by prefix, and then [fetch](/guides/manage-data/fetch-data) them. On a document index, you can also fetch them by passing a `filter` such as `{"document_id": {"$eq": "document1"}}` to `documents.fetch`, which returns up to 100 matches per page by default (set `limit` for up to 10,000):

> [tab] Document index
>
> ```python Python theme={null}
> from pinecone import Pinecone
>
> pc = Pinecone(api_key="YOUR_API_KEY")
>
> # To get the unique host for an index,
> # see https://docs.pinecone.io/guides/manage-data/target-an-index
> index = pc.index(host="INDEX_HOST")
>
> # List all chunks for document1 using ID prefix
> chunk_ids = []
> for doc in index.documents.list(namespace="example-namespace", prefix="document1#"):
>     chunk_ids.append(doc._id)
>
> print(f"Found {len(chunk_ids)} chunks for document1")
>
> # Fetch the complete documents by ID
> if chunk_ids:
>     response = index.documents.fetch(
>         namespace="example-namespace",
>         ids=chunk_ids,
>         include_fields=["chunk_text", "chunk_number"],
>     )
>
>     for doc_id, doc in response.documents.items():
>         print(f"Chunk ID: {doc_id}")
>         print(f"Chunk text: {doc.chunk_text}")
> ```

> [tab] Vector index
>
> ```python Python theme={null}
> from pinecone.grpc import PineconeGRPC as Pinecone
>
> pc = Pinecone(api_key="YOUR_API_KEY")
>
> # To get the unique host for an index,
> # see https://docs.pinecone.io/guides/manage-data/target-an-index
> index = pc.index(host="INDEX_HOST", grpc=True)
>
> # List all chunks for document1 using ID prefix.
> # Each iteration yields one page of IDs.
> chunk_ids = []
> for page in index.list(prefix='document1#', namespace='example-namespace'):
>     chunk_ids.extend(item.id for item in page.vectors)
>
> print(f"Found {len(chunk_ids)} chunks for document1")
>
> # Fetch the complete records by ID
> if chunk_ids:
>     records = index.fetch(ids=chunk_ids, namespace='example-namespace')
>
>     for record_id, record_data in records['vectors'].items():
>         print(f"Chunk ID: {record_id}")
>         print(f"Chunk text: {record_data['metadata']['chunk_text']}")
>         # Process the vector values and metadata as needed
> ```

## Delete chunks

To [delete](/guides/manage-data/delete-data) some or all of a source document's chunks, filter on their metadata:

> [tab] Document index
>
> ```python Python theme={null}
> from pinecone import Pinecone
>
> pc = Pinecone(api_key="YOUR_API_KEY")
>
> # To get the unique host for an index,
> # see https://docs.pinecone.io/guides/manage-data/target-an-index
> index = pc.index(host="INDEX_HOST")
>
> # Delete chunks 1 and 3
> index.documents.delete(
>     namespace="example-namespace",
>     filter={
>         "document_id": {"$eq": "document1"},
>         "chunk_number": {"$in": [1, 3]}
>     }
> )
>
> # Delete all chunks for a document
> index.documents.delete(
>     namespace="example-namespace",
>     filter={
>         "document_id": {"$eq": "document1"}
>     }
> )
> ```

> [tab] Vector index
>
> ```python Python theme={null}
> from pinecone.grpc import PineconeGRPC as Pinecone
>
> pc = Pinecone(api_key="YOUR_API_KEY")
>
> # To get the unique host for an index,
> # see https://docs.pinecone.io/guides/manage-data/target-an-index
> index = pc.index(host="INDEX_HOST", grpc=True)
>
> # Delete chunks 1 and 3
> index.delete(
>     namespace="example-namespace",
>     filter={
>         "document_id": {"$eq": "document1"},
>         "chunk_number": {"$in": [1, 3]}
>     }
> )
>
> # Delete all chunks for a document
> index.delete(
>     namespace="example-namespace",
>     filter={
>         "document_id": {"$eq": "document1"}
>     }
> )
> ```

## Replace a chunked document

When the number or order of a source document's chunks changes, delete all of its chunks with a metadata filter, and then upsert the new ones. To change one chunk's content without changing the chunk count, [update](/guides/manage-data/update-data) it by ID instead.

> [!TIP]
>
> To update most of the data in a large namespace, [contact Support](https://app.pinecone.io/organizations/-/settings/support/ticket) about a faster, cheaper approach based on an export.

> [tab] Document index
>
> ```python Python theme={null}
> from pinecone import Pinecone
>
> pc = Pinecone(api_key="YOUR_API_KEY")
>
> # To get the unique host for an index,
> # see https://docs.pinecone.io/guides/manage-data/target-an-index
> index = pc.index(host="INDEX_HOST")
>
> # Step 1: Delete all existing chunks for the document
> index.documents.delete(
>     namespace="example-namespace",
>     filter={
>         "document_id": {"$eq": "document1"}
>     }
> )
>
> print("Deleted existing chunks for document1")
>
> # Step 2: Upsert the updated document chunks
> index.documents.upsert(
>     namespace="example-namespace",
>     documents=[
>         {
>             "_id": "document1#chunk1",
>             "chunk_text": "Updated first chunk with new content...",
>             "document_id": "document1",
>             "document_title": "Introduction to Vector Databases - Updated Edition",
>             "chunk_number": 1,
>             "document_url": "https://example.com/docs/document1",
>             "created_at": "2024-02-15",
>             "document_type": "tutorial",
>             "version": "2.0"
>         },
>         {
>             "_id": "document1#chunk2",
>             "chunk_text": "Updated second chunk with new content...",
>             "document_id": "document1",
>             "document_title": "Introduction to Vector Databases - Updated Edition",
>             "chunk_number": 2,
>             "document_url": "https://example.com/docs/document1",
>             "created_at": "2024-02-15",
>             "document_type": "tutorial",
>             "version": "2.0"
>         },
>         # Add more chunks as needed for the updated document
>     ],
> )
>
> print("Successfully updated document1 with new chunks")
> ```

> [tab] Vector index
>
> ```python Python theme={null}
> from pinecone.grpc import PineconeGRPC as Pinecone
>
> pc = Pinecone(api_key="YOUR_API_KEY")
>
> # To get the unique host for an index,
> # see https://docs.pinecone.io/guides/manage-data/target-an-index
> index = pc.index(host="INDEX_HOST", grpc=True)
>
> # Step 1: Delete all existing chunks for the document
> index.delete(
>     namespace="example-namespace",
>     filter={
>         "document_id": {"$eq": "document1"}
>     }
> )
>
> print("Deleted existing chunks for document1")
>
> # Step 2: Upsert the updated document chunks
> # Replace with each chunk's embedding, which must match the index's dimension (1536 in this example)
> chunk1_vector = [0.1, 0.2] * 768
> chunk2_vector = [0.2, 0.1] * 768
> index.upsert(
>   namespace="example-namespace", 
>   vectors=[
>     {
>       "id": "document1#chunk1",
>       "values": chunk1_vector,
>       "metadata": {
>         "document_id": "document1",
>         "document_title": "Introduction to Vector Databases - Updated Edition",
>         "chunk_number": 1,
>         "chunk_text": "Updated first chunk with new content...",
>         "document_url": "https://example.com/docs/document1",
>         "created_at": "2024-02-15",
>         "document_type": "tutorial",
>         "version": "2.0"
>       }
>     },
>     {
>       "id": "document1#chunk2",
>       "values": chunk2_vector,
>       "metadata": {
>         "document_id": "document1",
>         "document_title": "Introduction to Vector Databases - Updated Edition",
>         "chunk_number": 2,
>         "chunk_text": "Updated second chunk with new content...",
>         "document_url": "https://example.com/docs/document1",
>         "created_at": "2024-02-15",
>         "document_type": "tutorial",
>         "version": "2.0"
>       }
>     }
>     # Add more chunks as needed for the updated document
>   ]
> )
>
> print("Successfully updated document1 with new chunks")
> ```
