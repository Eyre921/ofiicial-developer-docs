---
title: "Curation"
source: https://docs.pinecone.io/guides/nexus/how-curation-works
path: guides/nexus/how-curation-works
---

The write path that turns sources into chunks and artifacts, incrementally, driven by the manifest.

Curation is how Pinecone Nexus turns a context's source documents into the chunks and artifacts that queries read from. One generic runtime, the Context Compiler, drives it, parameterized by the context's [manifest](/guides/nexus/context-design).

## Curate up front

Curation does the hard work *up front* so retrieval gets a head start at query time. Sources aren't just chopped into chunks. They're reorganized into typed artifacts (summaries, entities, events) connected by edges, with structure captured for exact answers.

<img alt="Sources curated by the runtime under a manifest into a knowledge tree of chunks, artifacts, edges, and structured tables" />

<img alt="Sources curated by the runtime under a manifest into a knowledge tree of chunks, artifacts, edges, and structured tables" />

## The curation runtime

A curate run is a single generic entrypoint the orchestrator launches for the context. There's no per-context code. Every context runs the same runtime, and the manifest decides what to chunk, embed, and extract. A run moves through these phases:

1. **Delta:** Hash every source and compare to the curation ledger to find what's new, changed, or deleted.
2. **Replay:** Add back any sources that share an artifact with a changed or deleted one, since their artifacts may need rewriting.
3. **Cleanup deletes:** Drop deleted sources from the knowledge tree and the index, and record the removal.
4. **Per-source curate:** For each source to process: chunk, embed into the index pair, and extract its document-scoped artifacts.
5. **Corpus aggregation:** A single pass derives cross-document artifacts and the typed, cited edges that connect them into a knowledge graph.
6. **Finalize:** Commit counts and usage, and the orchestrator copies the knowledge tree back to the context's store.

## Per-source steps

For each source the delta says to process, the runtime runs the same three steps:

* **Chunk:** The source is split into spans, format-aware, with size enforcement.
* **Embed:** Each span is embedded into the semantic (and optional keyword) index, ready for hybrid search.
* **Extract:** The manifest's document-scoped artifact types are distilled out of the source, each carrying provenance back to its chunks.

## Incremental curation

Curation never rebuilds the world unless you ask it to. It keeps a ledger of every source it has already processed, so a run only touches what actually changed:

* **Content-addressed:** Sources are tracked by content hash, so identical files are never re-processed.
* **Only what changed:** Editing a document re-embeds just the changed spans and re-extracts just that source, not the whole corpus.
* **Artifact-aware replay:** When a source feeding a shared artifact changes, the sources it connects to are replayed so edges stay consistent.

Need a clean slate? Curate with *force re-curate* to wipe the index and ledger and rebuild everything from scratch.

## Outputs

When a run finishes, the context has everything a query needs, on disk, in the index, and as queryable structure:

* **The knowledge tree:** Chunks plus condensed artifacts written under the context's knowledge store on disk.
* **The index pair:** Chunks land in the default namespace and artifacts in the artifacts namespace of the context's semantic index (keyword too, when enabled).
* **Structured tables:** A per-context SQLite mirror exposes typed artifact types as queryable tables, which queries reach for on counts and enumerations.
* **The curation ledger:** Every processed source is recorded, so the next run computes its delta against it instead of starting over.
