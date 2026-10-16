---
title: "Context design overview"
source: https://docs.pinecone.io/guides/nexus/context-design
path: guides/nexus/context-design
---

Learn how a Pinecone Nexus context's manifest turns your sources into queryable knowledge.

A context turns your sources into queryable knowledge. Its manifest tells curation what to build, and curation produces two layers of knowledge, searchable chunks and distilled artifacts.

## The manifest

A *manifest* is a single validated JSON document that describes how a context curates its sources into knowledge. One generic runtime reads it, the same for every context. Its main section, `curate`, defines how to build knowledge from the sources, what to chunk and embed, and which artifacts to derive. A `search` section sets query-time defaults, like standing instructions every answer should follow. Change the manifest, change the behavior. A never-tuned context still works, because the schema ships sensible defaults.

You author a manifest through the [Nexus API](/reference/api/nexus/authentication), supplying it in the `manifest` field when you create or update a context, then curating. You can start from a prebuilt template or write the types yourself:

* Start from a template, a prebuilt manifest for a common corpus shape, and adjust it. Nexus suggests templates that match your sources. To see the full catalog, use `GET /manifest/templates`.
* [Design your own manifest](/guides/nexus/design-your-own-manifest) by defining artifact and edge types directly.
* Configure [artifact formats](/guides/nexus/configure-artifact-formats) to write a type as prose or as a queryable SQLite table.

Curation executes the manifest against the sources. To change a context later, send a new manifest with `PUT /contexts/{slug}` and re-curate, or edit it on the context's **Manifest** tab in the console, including SQLite table formats. These guides use the API.

## Knowledge layers

When Nexus curates a context, it builds two layers of knowledge:

### Chunks

Sources are split into spans and embedded for hybrid (semantic + keyword) search. Chunks are content-addressed, so editing a document re-embeds only what changed. Every query can fall back to chunks.

### Artifacts

Artifacts sit above the chunks. Each artifact has a *type* and a *kind*, a *scope*, a *format*, *provenance* linking back to its source chunks, and optional *edges*, which are typed, directed, source-cited relationships to other artifacts. The *type* is the artifact's classification, defined by your manifest and shown in the console (a template might define types such as Note, Concept, Entity, and Workstream). The *kind* is a built-in config within a type.

Corpus-scoped artifacts plus typed edges form a cross-document knowledge graph. Factual queries dive straight to chunks. Synthesizing or "connect-the-dots" queries enter at artifacts, walk the edges, then drill down to chunks for evidence.

## Artifact kinds

| Kind | Scope | Description |
| - | - | - |
| `summary` | `corpus` or `document` | A condensed overview of the whole corpus or a single document. |
| `topic` | `corpus` | A theme or subject distilled across the sources. |
| `entity` | `corpus` | A named thing (account, person, product) with its relationships. |
| `event` | `corpus` | Something that happened, often time-stamped, good for timelines and counts. |
| `doc` | `document` | A per-document artifact, scoped to one source file. |
| `page` | `document` | A single source page, the finest grain, for exact quotes and figures. |
| `glossary` | `corpus` | A term-and-definition pair, collected across the corpus into a shared lexicon. |

## Artifact formats

Each artifact type is written in one of two formats: `markdown`, a prose file per artifact, or `sqlite`, rows in a queryable table with a column schema. To set a type's format and, for `sqlite`, its columns and keys, see [Configure artifact formats](/guides/nexus/configure-artifact-formats).

## Context-default instructions

A context's default instructions act as a system prompt for every query against the context: the role to take, the tone to use, how to format answers, or how to handle conflicting sources. You set them once on the context instead of resending them with every query.

Set them in the manifest's `search.instructions` field, alongside `curate`:

```json theme={null}
{
  "curate": {
    "artifacts": {
      "enabled": true,
      "artifact_types": [
        { "name": "Filing", "kind": "entity", "scope": "corpus",
          "description": "One regulatory filing in the corpus." },
        { "name": "Risk", "kind": "topic", "scope": "corpus",
          "description": "A risk factor disclosed across the filings." }
      ]
    }
  },
  "search": {
    "instructions": "You're a financial analyst. Keep answers precise and neutral, and cite the filing and section behind every figure. When filings disagree, prefer the most recent and note the discrepancy."
  }
}
```

Supply the manifest in the `manifest` field when you create or update a context, as described in [Design your own manifest](/guides/nexus/design-your-own-manifest). Nexus reads the instructions at query time, so a change takes effect on your next query without a re-curate.

The instructions apply to every query against the context. When a query's `scope` lists more than one context, the instructions from the first context in the list apply. The field accepts up to 16,000 characters, and a longer value fails the manifest save with a `400` error. It defaults to empty, so a context has no default instructions until you set some.

A single session can layer its own instructions on top of this default. See [Set session instructions](/guides/nexus/set-session-instructions).
