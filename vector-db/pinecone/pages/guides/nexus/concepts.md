---
title: "Nexus key concepts"
source: https://docs.pinecone.io/guides/nexus/concepts
path: guides/nexus/concepts
---

Contexts, manifests, artifacts, sessions, and the Query API, and how they fit together.

Pinecone Nexus compiles your data into queryable knowledge that AI agents reach through a single interface. This page defines the core concepts and how they fit together, from the sources you bring in to the answers agents get back. For a high-level diagram of how they connect, see [How Nexus works](/guides/nexus/how-it-works).

## Sources

Your data, wherever it lives: docs and wikis, databases, APIs and SaaS, object storage, event streams, code repos. Upload files directly, or import them through a *connector* (Box and Google Drive). Import and manage sources from a context's **Sources** tab, using **+ Import**.

## Workspace

The top-level container you work in. A workspace holds your contexts and the tasks that build and query them. It is backed by a Pinecone project, which provides identity and access and is the tenancy boundary. You can have more than one workspace, each with a name that is unique within its Pinecone project.

## Context

The unit of knowledge: *Sources → Manifest → Knowledge*. The manifest turns sources into knowledge. One context per dataset, and a query reads one or more. A context holds up to 10 GB across 100,000 files, with each file up to 250 MB.

## Manifest

Configuration, not code: the plan that turns sources into knowledge (what to chunk, embed, and distill into artifacts). Shape it on **Design**, and curation executes it. [More on context design](/guides/nexus/context-design).

## Tasks and workflows

A *task* runs a *workflow* in a sandbox. **Import** ingests and cleans sources, **Curate** builds artifacts per the manifest, **Explore** proposes a manifest from your sources, and **Optimize** self-tunes the manifest from real query traffic. **Search** answers a query via KnowQL. Each workflow may ensemble multiple models as needed. Track them, and watch curation and query spend, under **Activity**.

## Artifacts (the knowledge)

The condensed knowledge that curation produces. Each artifact has a *type* (its classification, shown in the console) and a *kind* (a config within the type), plus a scope and provenance, and can be linked to others by typed edges into a knowledge graph. Browse them by type on a context's **Knowledge** tab. [See the artifact reference](/guides/nexus/context-design#artifact-kinds).

## Query

The single interface into Pinecone Nexus. A *query* asks a question scoped to one or more curated contexts. Pinecone Nexus plans its own retrieval and answers with citations. Query a single context from its **Search this context** box, or drive it from your own code via the [KnowQL query endpoint](/reference/api/nexus/query). See the [quickstart](/guides/nexus/quickstart#3-query-your-context).

## KnowQL

The declarative query language agents use to query Nexus. A KnowQL query names a `scope` (the contexts to read) and an `ask` (the question), plus an optional typed `shape` for structured output. Nexus plans and runs its own retrieval, then returns a grounded, cited answer. The Composable Retriever serves your artifacts through KnowQL, and the Context Compiler is what builds those artifacts during curation.

## Sessions

A multi-turn conversation. A single query is one turn: a question in, an answer out. A session keeps state across turns, so follow-up questions resolve against what came before, and it can draw on more than one context at once. Start one from the workspace **Home** or **Sessions > + New session**, or from a context's **Query** tab, where the **Search this context** box opens a session scoped to that context.

## Use

Query your contexts from other systems: an [MCP server](/guides/nexus/mcp-server) for Claude Desktop and other MCP clients, or the [KnowQL query endpoint](/reference/api/nexus/query) over HTTP.
