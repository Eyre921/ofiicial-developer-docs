---
title: "Nexus key terms"
source: https://docs.pinecone.io/guides/nexus/concepts
path: guides/nexus/concepts
---

Learn the key Pinecone Nexus terms, from sources and contexts to artifacts, sessions, and queries, and how they connect.

Pinecone Nexus compiles your data into queryable knowledge that AI agents reach through a single interface. This page defines the key terms and how they fit together, from the sources you bring in to the answers agents get back. For a high-level diagram of how they connect, see [Nexus architecture](/guides/nexus/how-it-works).

## Sources

Sources are your data, wherever it lives: docs and wikis, databases, APIs and SaaS, object storage, event streams, and code repos. Upload files directly, pull from a public Hugging Face or GitHub repository URL, or connect a Box or Google Drive account through a *connector*.

## Workspace

A workspace is the top-level container you work in. It holds your contexts and the tasks that build and query them. It's backed by a Pinecone project, which provides identity and access and is the tenancy boundary. You can have more than one workspace, each with a name that's unique within its Pinecone project.

## Context

A context is the unit of knowledge: *Sources → Manifest → Knowledge*. The manifest turns sources into knowledge. You create one context per dataset, and a query reads one or more. A context holds up to 10 GB across 100,000 files, with each file up to 250 MB.

## Manifest

A manifest is the JSON plan that turns a context's sources into knowledge, so you configure a context instead of writing code. It defines what to chunk, embed, and distill into artifacts, and curation runs it. Set it when you create a context, or replace it later with `PUT /contexts/{slug}`. [More on context design](/guides/nexus/context-design).

## Tasks and workflows

A *task* runs a *workflow* in a sandbox. **Import** ingests and cleans sources, **Curate** builds artifacts per the manifest, **Explore** recommends starter manifest templates that fit your sources, and **Optimize** self-tunes the manifest from real query traffic. **Search** answers a query via KnowQL. Each workflow may ensemble multiple models as needed.

## Artifacts (the knowledge)

Artifacts are the condensed knowledge that curation produces. Each artifact has a *type* (its classification) and a *kind* (a config within the type), plus a scope and provenance, and can be linked to others by typed edges into a knowledge graph. [See the artifact reference](/guides/nexus/context-design#artifact-kinds).

## Query

A query is a question asked against one or more curated contexts, and it's the single interface into Pinecone Nexus. Nexus plans its own retrieval and answers with citations. Send queries from your own code through the [Nexus API](/reference/api/nexus/introduction). See the [quickstart](/guides/nexus/quickstart#3-query-your-context). To steer how a context answers every query, set [context-default instructions](/guides/nexus/context-design#context-default-instructions) in its manifest.

## KnowQL

KnowQL is the declarative query language agents use to query Nexus. A KnowQL query names a `scope` (the contexts to read) and an `ask` (the question), plus an optional typed `shape` for structured output. Nexus plans and runs its own retrieval, then returns a grounded, cited answer.

## Sessions

A session is a multi-turn conversation. A single query is one turn: a question in, an answer out. A session keeps state across turns, so follow-up questions resolve against what came before, and it can draw on more than one context at once. A query without `previous_query_id` starts a new session, and a query that passes one continues that session.
