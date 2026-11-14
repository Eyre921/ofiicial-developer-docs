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
3. **Agent loop:** The model writes Python into a persistent read-eval-print loop (REPL) that calls the retrieval SDK to read artifacts, run searches, walk the graph, and query structured tables. The runtime posts each step as it happens, which powers the live answer stream. You can replay the full sequence for any query in its [query trace](/guides/nexus/query-tracing).
4. **Answer:** When the model can answer, it writes the answer with inline citations and ends the turn. The runtime then builds `citations` from what the loop retrieved and the files the answer names.

## Agent loop

The model's primary tool is `run_python`, a persistent REPL. Variables carry over between calls, so in one block the model can find an artifact, read it, filter its sources, and pull a verbatim quote. It processes results in code and prints only what it needs.

For example, this block finds a summary artifact about acquisition terms, reads it, and searches that artifact's sources for the purchase price:

```python Python theme={null}
art = await search_knowledge("acquisition terms", kind="summary")
srcs = read_artifact(art[0].fields["artifact_name"]).sources
for h in await search_in_sources(srcs, "purchase price"):
    print(h.fields["source_path"], "::", h.fields["chunk_text"][:160])
```

If the first pass misses, the model refines its code and searches again, so a hard question gets more steps. The loop stops as soon as the model can answer.

Independent searches run concurrently, and the model reuses lookups it already holds in a variable. The loop has a step cap, so the model aims to gather what it needs and answer in a few steps.

## Retrieval SDK

The Composable Retriever, the Nexus component that serves artifacts to queries, loads these primitives into the REPL. The model reads artifacts off disk first because it's cheapest, falls back to search over the index, and uses SQL for counts and enumerations.

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

## Answers and citations

The model writes the answer at the end of the agent loop. These rules shape what the answer draws on and how it cites sources.

* **Evidence:** The model answers from the evidence its code surfaced rather than from whole documents, so it reasons over a small, relevant context.
* **Citations:** Each citation names its source file, plus the pages and sections of the passages it drew on when they're available.
* **Duplicate sources:** When several sources contain the same content and the answer draws on one of them, the model is prompted to say which one it used and why. It's also prompted to name each of the others by its full file name, so they're cited too. If your question names the source, the answer uses it without listing the others. With more than five other copies, the answer gives their count instead.
* **Earlier-turn citations:** In a session, a follow-up answer can cite a file that an earlier turn retrieved, if the answer names it. These citations are file-level, so they include the `source` but no pages or sections. Their `grounding` is `carried` because the current turn didn't retrieve the file itself.
* **Structured output:** When a query includes a `shape`, a second model call turns the answer into a document built to that schema. Nexus checks the document against the schema, and the model rewrites it up to two times if it breaks a rule, such as a `maxLength`. If it still doesn't conform, the query returns the last version. The document's values don't include inline citation markers, and the sources are in `citations`.

## Session instructions

A session can have its own system prompt. It adds to the context's default instructions and shapes every answer in the session. See [Set session instructions](/guides/nexus/set-session-instructions).
