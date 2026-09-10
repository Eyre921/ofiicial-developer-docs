---
title: "Context design overview"
source: https://docs.pinecone.io/guides/nexus/context-design
path: guides/nexus/context-design
---

Learn how a Pinecone Nexus context's manifest turns your sources into queryable knowledge.

A context is shaped by its manifest, which turns your sources into knowledge.

## The manifest

A *manifest* is a single validated JSON document that describes how a context curates its sources into knowledge. One generic runtime reads it, the same for every context. Its main section, `curate`, defines how to build knowledge from the sources, what to chunk and embed, and which artifacts to derive. Change the manifest, change the behavior. A never-tuned context still works, because the schema ships sensible defaults.

You author a context's manifest during setup. Pinecone Nexus scans your sources and suggests templates that match, then you choose how to proceed:

* Start from a template, a prebuilt manifest for a common corpus shape. Use the one Nexus matched, or pick any other from the catalog.
* Define artifact and edge types yourself with [**Design your own**](/guides/nexus/design-your-own-manifest), no template needed.
* Supply your own manifest JSON with **Import your own manifest**.

Both **Design your own** and **Import your own manifest** appear under **Or start from scratch**.

You then review the artifact types, edge types, model, and estimated cost before curating. Curation executes the manifest against the sources.

You can update a context's manifest later from its **Manifest** tab with **Update design**, importing a new manifest or applying a different template, or author it through the [Nexus API](/reference/api/nexus/introduction) by supplying a `manifest` field when you create or update a context.

## Knowledge layers

When Nexus curates a context, it builds two layers of knowledge:

### Chunks

Sources are split into spans and embedded for hybrid (semantic + keyword) search. Chunks are content-addressed, so editing a document re-embeds only what changed. Every query can fall back to chunks.

### Artifacts

Artifacts sit above the chunks. Each artifact has a *type* and a *kind*, a *scope*, a *format*, *provenance* linking back to its source chunks, and optional *edges*, which are typed, directed, source-cited relationships to other artifacts. The *type* is the artifact's classification, defined by your manifest and shown in the console (a template might define types such as Note, Concept, Entity, and Workstream). The *kind* is a built-in config within a type.

Corpus-scoped artifacts plus typed edges form a cross-document knowledge graph. Factual queries dive straight to chunks. Synthesizing or "connect-the-dots" queries enter at artifacts, walk the edges, then drill down to chunks for evidence.

## Artifact kinds

| Kind       | Scope                  | Description                                                                    |
| ---------- | ---------------------- | ------------------------------------------------------------------------------ |
| `summary`  | `corpus` or `document` | A condensed overview of the whole corpus or a single document.                 |
| `topic`    | `corpus`               | A theme or subject distilled across the sources.                               |
| `entity`   | `corpus`               | A named thing (account, person, product) with its relationships.               |
| `event`    | `corpus`               | Something that happened, often time-stamped, good for timelines and counts.    |
| `doc`      | `document`             | A per-document artifact, scoped to one source file.                            |
| `page`     | `document`             | A single source page, the finest grain, for exact quotes and figures.          |
| `glossary` | `corpus`               | A term-and-definition pair, collected across the corpus into a shared lexicon. |

## Artifact formats

Each artifact type is written in one of two formats:

* **`markdown`** (the default) writes a prose file per artifact, best for summaries, notes, and descriptions.
* **`sqlite`** writes rows into the context's structured database, so the type becomes a queryable table.

A `sqlite` type declares its `columns`, each with a name, a SQLite type (`TEXT`, `INTEGER`, `REAL`, or `NUMERIC`), and a description that steers what curation extracts into it. It can also set a `natural_key`, the columns that identify a row, so re-curating a source upserts its rows instead of duplicating them. Structured types let queries count and list exactly, rather than inferring from prose.

Because a structured type needs a column schema, you author it by [importing a manifest](/guides/nexus/design-your-own-manifest#import-a-manifest-instead), not in the builder.
