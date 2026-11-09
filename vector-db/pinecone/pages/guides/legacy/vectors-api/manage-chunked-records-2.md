---
title: "Manage chunked records in a legacy index"
source: https://docs.pinecone.io/guides/legacy/vectors-api/manage-chunked-records
path: guides/legacy/vectors-api/manage-chunked-records
---

Fetch, search, delete, and replace all chunks of a source document in a legacy vector index using ID prefixes and a document_id metadata field.

> [!NOTE]
>
> New projects should use the [Documents API](/guides/indexes/create-an-index#create-a-document-index). To move an existing index, see [Move to the Documents API](/guides/indexes/move-to-the-documents-api).

When you split a long source document into chunks, each chunk is stored as its own record in a legacy vector index. To work with all of a source document's chunks at once, give each chunk a [structured ID](/guides/indexes/data-modeling#use-structured-ids) prefixed with the source document's ID, and a `document_id` metadata field. The code on this page assumes you generate the vectors yourself. For a document index, see [Manage document chunks](/guides/data/manage-document-chunks).

> [!NOTE]
>
> Pinecone is [eventually consistent](/guides/data/check-data-freshness), so a read right after a write (upsert, update, or delete) may not return the latest data. If you need to read immediately after writing, add a short delay or [retry logic](/guides/production/error-handling#implement-retry-logic).

## Upsert chunks

[Upsert](/guides/legacy/vectors-api/upsert-vectors) each chunk with its structured ID and `document_id`, plus any other metadata you want to filter on or display:

```python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST", grpc=True)

# Replace with each chunk's embedding, which must match the index's dimension (1536 in this example)
chunk1_vector = [0.1, 0.2] * 768
chunk2_vector = [0.2, 0.1] * 768
chunk3_vector = [0.3, 0.1] * 768

index.upsert(
  namespace="example-namespace",
  vectors=[
    {
      "id": "document1#chunk1", 
      "values": chunk1_vector,
      "metadata": {
        "document_id": "document1",
        "document_title": "Introduction to Vector Databases",
        "chunk_number": 1,
        "chunk_text": "First chunk of the document content...",
        "document_url": "https://example.com/docs/document1",
        "created_at": "2024-01-15",
        "document_type": "tutorial"
      }
    },
    {
      "id": "document1#chunk2", 
      "values": chunk2_vector,
      "metadata": {
        "document_id": "document1",
        "document_title": "Introduction to Vector Databases", 
        "chunk_number": 2,
        "chunk_text": "Second chunk of the document content...",
        "document_url": "https://example.com/docs/document1",
        "created_at": "2024-01-15",
        "document_type": "tutorial"
      }
    },
    {
      "id": "document1#chunk3", 
      "values": chunk3_vector,
      "metadata": {
        "document_id": "document1",
        "document_title": "Introduction to Vector Databases",
        "chunk_number": 3, 
        "chunk_text": "Third chunk of the document content...",
        "document_url": "https://example.com/docs/document1",
        "created_at": "2024-01-15",
        "document_type": "tutorial"
      }
    }
  ]
)
```

## Search within a document

To search only one source document's chunks, add a [metadata filter](/guides/search/filter-by-metadata#metadata-filter-expressions) on `document_id`:

```python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST", grpc=True)

# Replace with your query embedding, which must match the index's dimension (1536 in this example)
query_vector = [0.1, 0.2] * 768

filtered_results = index.query(
    namespace="example-namespace",
    vector=query_vector,
    top_k=3,
    filter={
        "document_id": {"$eq": "document1"}
    },
    include_metadata=True,
    include_values=False
)

print(filtered_results)
```

## Fetch all chunks of a document

To retrieve all of a source document's chunks, [list](/guides/legacy/vectors-api/list-vector-ids) their IDs by prefix, and then [fetch](/guides/legacy/vectors-api/fetch-vectors) them:

```python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST", grpc=True)

# List all chunks for document1 using ID prefix.
# Each iteration yields one page of IDs.
chunk_ids = []
for page in index.list(prefix='document1#', namespace='example-namespace'):
    chunk_ids.extend(item.id for item in page.vectors)

print(f"Found {len(chunk_ids)} chunks for document1")

# Fetch the complete records by ID
if chunk_ids:
    records = index.fetch(ids=chunk_ids, namespace='example-namespace')
    
    for record_id, record_data in records['vectors'].items():
        print(f"Chunk ID: {record_id}")
        print(f"Chunk text: {record_data['metadata']['chunk_text']}")
        # Process the vector values and metadata as needed
```

## Delete chunks

To [delete](/guides/legacy/vectors-api/delete-vectors) some or all of a source document's chunks, filter on their metadata:

```python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST", grpc=True)

# Delete chunks 1 and 3
index.delete(
    namespace="example-namespace",
    filter={
        "document_id": {"$eq": "document1"},
        "chunk_number": {"$in": [1, 3]}
    }
)

# Delete all chunks for a document
index.delete(
    namespace="example-namespace",
    filter={
        "document_id": {"$eq": "document1"}
    }
)
```

## Replace a chunked document

When the number or order of a source document's chunks changes, delete all of its chunks with a metadata filter, and then upsert the new ones. To change one chunk's content without changing the chunk count, [update](/guides/legacy/vectors-api/update-vectors) it by ID instead.

```python Python theme={null}
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# To get the unique host for an index,
# see https://docs.pinecone.io/guides/indexes/target-an-index
index = pc.index(host="INDEX_HOST", grpc=True)

# Step 1: Delete all existing chunks for the document
index.delete(
    namespace="example-namespace",
    filter={
        "document_id": {"$eq": "document1"}
    }
)

print("Deleted existing chunks for document1")

# Step 2: Upsert the updated document chunks
# Replace with each chunk's embedding, which must match the index's dimension (1536 in this example)
chunk1_vector = [0.1, 0.2] * 768
chunk2_vector = [0.2, 0.1] * 768
index.upsert(
  namespace="example-namespace", 
  vectors=[
    {
      "id": "document1#chunk1",
      "values": chunk1_vector,
      "metadata": {
        "document_id": "document1",
        "document_title": "Introduction to Vector Databases - Updated Edition",
        "chunk_number": 1,
        "chunk_text": "Updated first chunk with new content...",
        "document_url": "https://example.com/docs/document1",
        "created_at": "2024-02-15",
        "document_type": "tutorial",
        "version": "2.0"
      }
    },
    {
      "id": "document1#chunk2",
      "values": chunk2_vector,
      "metadata": {
        "document_id": "document1",
        "document_title": "Introduction to Vector Databases - Updated Edition",
        "chunk_number": 2,
        "chunk_text": "Updated second chunk with new content...",
        "document_url": "https://example.com/docs/document1",
        "created_at": "2024-02-15",
        "document_type": "tutorial",
        "version": "2.0"
      }
    }
    # Add more chunks as needed for the updated document
  ]
)

print("Successfully updated document1 with new chunks")
```
