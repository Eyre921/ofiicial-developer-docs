---
title: "Nexus queries"
source: https://docs.pinecone.io/guides/nexus/queries
path: guides/nexus/queries
---

Pinecone Nexus queries gather evidence and compose a grounded, cited answer.

A query is a single turn that takes a question and returns a grounded answer, and a multi-turn conversation is a session. To answer, Pinecone Nexus runs an agent loop in which the model writes Python against a retrieval SDK to gather the evidence it needs, then composes an answer with citations.

![In a query turn, the agent loops, writing code against a retrieval SDK to gather evidence, then composes a cited answer](https://mintcdn.com/pinecone/EWF4J3kPxqsT4ELV/images/nexus/queries-light.svg?fit=max\&auto=format\&n=EWF4J3kPxqsT4ELV\&q=85\&s=fbb7818dc5c26a7ede110869e776d556)

## Retrieval as code

Two common ways to answer over a corpus have drawbacks. Agentic retrieval-augmented generation (RAG) issues many retrieval calls and spends tokens stitching the results together. A coding agent that greps and parses raw files is flexible, but it's slow and expensive, and its results are unreliable.

A query turn does the hard retrieval work in one place. The model writes Python that reads artifacts, runs search, walks the graph, and queries structured tables, then answers from only the evidence it surfaced. Raw tool output never enters the model's context.

## Query runtime

The Nexus runtime runs each query. It's a single generic Python image that the orchestrator launches fresh for each turn, with no per-context code. Every context runs the same entrypoint, parameterized by its [manifest](/guides/nexus/context-design).

1. **Container:** Each query starts one isolated container that runs that turn, then exits. It pulls the scoped contexts' curated knowledge: artifacts on disk plus their vector index.
2. **Orientation:** The runtime reads the manifests and an artifact outline up front, so the model starts knowing what knowledge exists and where.
3. **Agent loop:** The model writes Python into a persistent REPL that calls the retrieval SDK to read artifacts, run searches, walk the graph, and query structured tables.
4. **Step events:** The runtime posts each step as it happens, which powers the live answer stream. You can replay the full sequence for any query in its [query trace](/guides/nexus/query-tracing).
5. **Synthesis:** Once enough evidence is gathered, the runtime composes a grounded answer with inline citations, then finalizes the turn.

## Agent loop

The model's primary tool is `run_python`, a persistent REPL. Variables survive across calls, so the model chains operations together: find an artifact, read it, filter its sources, drill for a verbatim quote, all in one block. It processes results in code and prints only what it needs.

If the first pass misses, the model refines its code and searches again, so a hard question gets more steps. The loop stops as soon as the model can answer.

```python theme={null}
# One turn: find an artifact, read it, drill its sources.
art = await search_knowledge("acquisition terms", kind="summary")
srcs = read_artifact(art[0].name).sources
for h in await search_in_sources(srcs, "purchase price"):
    print(h.fields["source_path"], "::", h.fields["chunk_text"][:160])
```

Independent searches run concurrently, and the model reuses lookups it already holds in a variable. The loop has a step cap, so the model aims to gather what it needs and answer in a few steps.

## Retrieval SDK

The Composable Retriever loads these primitives into the REPL. The model reads artifacts off disk first because it's cheapest, falls back to search over the index, and uses SQL for counts and enumerations.

### Read artifacts

| Primitive | What it does |
| - | - |
| `outline_knowledge()` | a map of every artifact in the context |
| `read_artifact(name)` | a condensed artifact: its body, edges, and sources |
| `read_rosters()` | "all X" rosters for list-everything questions |
| `describe_type(name)` | the full manifest spec for an artifact type |

### Search

| Primitive | What it does |
| - | - |
| `search_knowledge(query)` | semantic search over artifacts (optionally by kind) |
| `search_source(query)` | semantic search over raw source chunks |
| `search_source_by_keyword(query)` | keyword (BM25) search for exact IDs, codes, and phrases |
| `search_in_sources(sources, query)` | semantic search within a specific artifact's source chunks |
| `cite_from_artifact(name)` | drill an artifact's sources for a verbatim span |

### Structured tables

| Primitive | What it does |
| - | - |
| `query_db(sql)` | read-only SQL over typed artifact tables, the first choice for counts and per-item questions |
| `walk_graph(name)` | an N-hop subgraph around an artifact, following typed edges |

## Synthesis

* **Evidence:** The model composes the answer from the evidence its code surfaced, so it reasons over a small, relevant context.
* **Citations:** Each inline citation marker maps to a source span, with the file, page, and verbatim text behind the claim.
* **Structured output:** When a query includes a `shape`, synthesis returns a document that conforms to that schema.

## Session instructions

A session can carry its own instructions, a system prompt layered over the context's default that shapes every answer in the session. See [Set session instructions](/guides/nexus/set-session-instructions).
