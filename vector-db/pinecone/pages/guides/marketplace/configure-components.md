---
title: "Configure components"
source: https://docs.pinecone.io/guides/marketplace/configure-components
path: guides/marketplace/configure-components
---

Enable visual components like comparison tables, timelines, and coverage matrices in a Pinecone Marketplace knowledge application interface.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

A component is a visual primitive a knowledge application can render in addition to text. Components let an answer take the most useful shape for the question instead of forcing every response into prose.

Components are read-only and retrieval-oriented. They render information from the connected sources; they do not write back to source systems.

## Available components

| Component         | Use it for                                                               |
| ----------------- | ------------------------------------------------------------------------ |
| Comparison tables | Side-by-side comparisons of products, plans, policies, or options        |
| Content cards     | Browsable summaries of documents, people, or items with links to sources |
| Timelines         | Sequences of dated events, such as case milestones or release histories  |
| Progress trackers | Step-by-step processes such as onboarding checklists                     |
| Coverage matrices | Two-dimensional lookups, such as benefits coverage by plan and region    |
| Geolocation maps  | Locations and venue context                                              |

## Enabling components

From the deployment dashboard, enable the components you want the application to use. Components must be compatible with the [layout](/guides/marketplace/configure-layouts):

* Chat layouts can render any component inline in an answer.
* Search layouts work best with content cards and comparison tables.
* Structured and hybrid layouts work best with comparison tables, coverage matrices, timelines, and progress trackers.

## How the application picks a component

The application chooses a component based on the question, the response shape, and the components you have enabled. If a question is best answered with text, the application returns text even if components are enabled.

## Component output and citations

Every component cites the documents it was built from. End users can click into a cited source to see the original document. See [Citations](/guides/marketplace/end-user/citations).
