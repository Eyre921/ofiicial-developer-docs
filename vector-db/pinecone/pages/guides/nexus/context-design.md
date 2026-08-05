---
title: "Context design"
source: https://docs.pinecone.io/guides/nexus/context-design
path: guides/nexus/context-design
---

The manifest, the information stack (chunks, artifacts, and edges), and the artifact-kind reference.

How a context is shaped: the manifest that drives it and the knowledge curation builds from your sources.

## The manifest

A context doesn't ship custom Python. Instead, one generic runtime reads a single validated JSON document, the *manifest*, that describes how this context should curate its sources into knowledge. Its main section, `curate`, defines how to build knowledge from the sources, what to chunk and embed and which artifacts to derive. Change the manifest, change the behavior. A never-tuned context still works, because the schema ships sane defaults.

On the **Design** page, let **Explore** propose a manifest from your sources (or start from a template), review it, then curate. Curation executes the manifest against the sources.

## The information stack

When Pinecone Nexus curates a context, it builds two layers of knowledge:

### Chunks

Sources are split into spans and embedded for hybrid (semantic + keyword) search. Content-addressed, so editing a document re-embeds only what changed. Every query can fall back to chunks.

### Artifacts

Artifacts sit above the chunks. Each artifact has a *type* and a *kind*, a *scope*, *provenance* linking back to its source chunks, and optional *edges*, which are typed, directed, source-cited relationships to other artifacts. The *type* is the artifact's classification, defined by your manifest and shown in the console (a template might define types such as Note, Concept, Entity, and Workstream). The *kind* is a built-in config within a type.

Corpus-scoped artifacts plus typed edges form a cross-document knowledge graph. Factual queries dive straight to chunks. Synthesizing or "connect-the-dots" queries enter at artifacts, walk the edges, then drill down to chunks for evidence.

## Artifact kinds

| Kind       | Scope         | Description                                                                    |
| ---------- | ------------- | ------------------------------------------------------------------------------ |
| `summary`  | corpus or doc | A condensed overview, of the whole corpus or a single document.                |
| `topic`    | corpus        | A theme or subject distilled across the sources.                               |
| `entity`   | corpus        | A named thing (account, person, product) with its relationships.               |
| `event`    | corpus        | Something that happened, often time-stamped, good for timelines and counts.    |
| `doc`      | per-document  | A per-document artifact, scoped to one source file.                            |
| `page`     | per-document  | A single source page, the finest grain, for exact quotes and figures.          |
| `glossary` | corpus        | A term-and-definition pair, collected across the corpus into a shared lexicon. |
