---
title: "Files overview"
source: https://docs.pinecone.io/guides/assistant/files-overview
path: guides/assistant/files-overview
---

Learn which file types Pinecone Assistant supports (PDF, DOCX, JSON, Markdown, text) and how file metadata, storage, and signed-URL access work.

Before you can chat with the assistant, you need to [upload files](/guides/assistant/upload-files). The files give the assistant context to reference when generating responses. Files aren't shared across assistants. You can also [add metadata to files](/guides/assistant/file-metadata) to filter and organize them.

## Supported file types

Pinecone Assistant supports the following file types:

* DOCX (`.docx`)
* JSON (`.json`)
* Markdown (`.md`)
* PDF (`.pdf`)
* Text (`.txt`)

> [!NOTE]
>
> For PDF files, assistants support [multimodal context](/guides/assistant/multimodal-context), allowing them to analyze and gather context from images. This feature is in [public preview](/release-notes/feature-availability).

For information about file size and storage limits, see [Pricing and limits](/guides/assistant/pricing-and-limits).

## File storage

Files are uploaded to Google Cloud Storage in the assistant's region (`us` or `eu`). The assistant processes the files and stores the resulting embeddings in a Pinecone-managed index, separate from the indexes in your projects.

Some API responses include a `signed_url` field, which provides temporary, read-only access to one of the assistant's files. The URL is [signed](https://cloud.google.com/storage/docs/access-control/signed-urls) and hard to guess, but publicly accessible, so treat it as sensitive. `signed_url` links expire in one hour.

## File identifiers

Each file in an assistant has a unique identifier. File IDs can be:

* System-generated: When you [upload a file](/guides/assistant/upload-files#upload-a-local-file) using `POST`, the system assigns a UUID as the file ID.
* User-provided: When you [upsert a file](/guides/assistant/upload-files#upsert-a-file) using `PUT`, you provide a custom file ID. User-provided IDs must be 1-128 characters long and can contain alphanumeric characters, hyphens, and underscores. Requires [API version](/reference/api/versioning) `2026-04` or later.
