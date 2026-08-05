---
title: "Queries"
source: https://docs.pinecone.io/guides/nexus/how-queries-work
path: guides/nexus/how-queries-work
---

The query runtime that gathers evidence and composes a grounded, cited answer.

A query is a single turn: a question in, a grounded answer out. A multi-turn conversation is a session. Rather than stuffing raw chunks into a prompt, Pinecone Nexus runs an agent loop in which the model writes Python against a retrieval SDK to gather just the evidence it needs, then composes a grounded answer with citations.

<img alt="A query turn: the agent loops, writing code against a retrieval SDK to gather evidence, then composes a cited answer" />

<img alt="A query turn: the agent loops, writing code against a retrieval SDK to gather evidence, then composes a cited answer" />

## Retrieval as code

The usual ways to answer over a corpus both struggle. Agentic RAG issues many retrieval calls and burns tokens stitching them together, and a coding agent greps and parses raw files, which is powerful but slow, expensive, and unreliable.

A query turn does the hard retrieval work in one place. The model writes Python that reads artifacts, runs search, walks the graph, and queries structured tables, then answers from only the evidence it surfaced. Raw tool output never enters the model's context.

## The query runtime

A query is run by the Nexus runtime, a single generic Python image the orchestrator launches fresh for each turn. There is no per-context code. Every context runs the same entrypoint, parameterized by its [manifest](/guides/nexus/context-design).

1. **A fresh container per turn:** Each query spawns one isolated container that runs exactly that turn, then exits. It pulls the scoped contexts' curated knowledge: artifacts on disk plus their vector index.
2. **Orientation:** The runtime reads the manifests and an artifact outline up front, so the model starts knowing what knowledge exists and where.
3. **The agent loop:** The model writes Python into a persistent REPL to call the retrieval SDK, reading artifacts, running search, walking the graph, querying structured tables.
4. **Step events:** Each step is posted back as it happens, powering the live answer stream you see in the console. You can replay the full sequence for any query with [query tracing](/guides/nexus/query-tracing).
5. **Synthesis:** Once enough evidence is gathered, the runtime composes a grounded answer with inline citations, then finalizes the turn.

## The agent loop

The model's primary tool is `run_python`, a persistent REPL. Variables survive across calls, so the model chains operations together: find an artifact, read it, filter its sources, drill for a verbatim quote, all in one block. It processes results in code and prints only what it needs.

If the first pass misses, the model refines its code and searches again, so hard questions get more work, not a worse answer. The loop stops as soon as the model can answer.

```python theme={null}
# One turn: find an artifact, read it, drill its sources.
art = await search_knowledge("acquisition terms", kind="summary")
srcs = read_artifact(art[0].name).sources
for h in await search_in_sources(srcs, "purchase price"):
    print(h.fields["source_path"], "::", h.fields["chunk_text"][:160])
```

Independent searches run concurrently, and lookups already held in a variable are never repeated. The loop is capped, so the model is pushed to extract everything it needs and answer in a few steps.

## The retrieval SDK

The Composable Retriever pre-binds these primitives into the REPL. Read artifacts cheaply off disk, fall back to search over the index, and reach for SQL when the question is a count or enumeration.

### Read artifacts

| Primitive             | What it does                                       |
| --------------------- | -------------------------------------------------- |
| `outline_knowledge()` | a map of every artifact in the context             |
| `read_artifact(name)` | a condensed artifact: its body, edges, and sources |
| `read_rosters()`      | "all X" rosters for list-everything questions      |
| `describe_type(name)` | the full manifest spec for an artifact type        |

### Search

| Primitive                           | What it does                                               |
| ----------------------------------- | ---------------------------------------------------------- |
| `search_knowledge(query)`           | semantic search over artifacts (optionally by kind)        |
| `search_source(query)`              | semantic search over raw source chunks                     |
| `search_source_by_keyword(query)`   | lexical/BM25 for exact IDs, codes, and phrases             |
| `search_in_sources(sources, query)` | semantic search within a specific artifact's source chunks |
| `cite_from_artifact(name)`          | drill an artifact's sources for a verbatim span            |

### Structured tables

| Primitive          | What it does                                                                             |
| ------------------ | ---------------------------------------------------------------------------------------- |
| `query_db(sql)`    | read-only SQL over typed artifact tables, the first resort for how-many / counts / per-X |
| `walk_graph(name)` | an N-hop subgraph around an artifact, following typed edges                              |

## Synthesis

**Synthesis from surfaced evidence.** The answer is composed from just the evidence the code surfaced, never the raw corpus, so the model reasons over a small, relevant context instead of the whole document set.

**Citations that trace to a source.** Inline citation markers map back to real source spans: the file, page, and verbatim text behind every claim.

**Optional structured output.** When a `shape` is supplied, the answer is routed through structured synthesis to produce a schema-conforming document instead of prose.
