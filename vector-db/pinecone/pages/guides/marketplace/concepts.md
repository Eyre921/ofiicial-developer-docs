---
title: "Marketplace concepts"
source: https://docs.pinecone.io/guides/marketplace/concepts
path: guides/marketplace/concepts
---

Learn Pinecone Marketplace concepts including knowledge applications, deployments, templates, manifests, KAT routing, layouts, and visual components.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

This page defines the core concepts in Pinecone Marketplace. For a hands-on introduction, see the [Quickstart](/guides/marketplace/quickstart).

## Knowledge application

A **knowledge application** is the consumer-facing product an operator publishes. It has a branded interface, one or more knowledge domains, and a defined access policy. End users interact with a knowledge application; they do not interact directly with the underlying Pinecone assistants.

## Deployment

A **deployment** is the unit an operator owns and manages. It contains the configuration, connected sources, versions, and access settings for a single knowledge application. Each deployment has its own dashboard, analytics, and event log.

## Template

A **template** is a vertical configuration that bundles operating parameters, suggested layout, recommended sources, and starter prompts for a specific use case. Marketplace ships with a catalog of templates (presented as **Apps** in the catalog UI), such as Customer Support, HR Benefits, Legal Document Search, and Sales Enablement. See [Template catalog](/guides/marketplace/template-catalog).

A template provides a starting point. Operators customize it through the setup wizard, then can keep iterating after the deployment is published.

## Version

A **version** is a snapshot of a deployment that you can publish, evaluate, and roll back to. When an operator edits an active deployment, Marketplace creates a new building version. Publishing promotes that version to active and triggers background provisioning, introspection, starter generation, and evaluation. Previous versions remain available for rollback.

See [Manage versions and rollback](/guides/marketplace/manage-versions-and-rollback).

## Knowledge base

A **knowledge base** is a single knowledge domain inside a deployment, backed by a Pinecone assistant. A deployment can have one or many knowledge bases. Multi-knowledge-base deployments use [KAT](#kat) to route between domains.

## Manifest

A **manifest** is an automatically generated description of what a knowledge base can answer, what is in scope, and what is out of scope. Marketplace builds manifests through progressive introspection: after publish, it probes each assistant with sampled questions and uses the responses to construct the manifest. KAT uses manifests at query time to route, disambiguate, and refuse out-of-scope questions.

See [Manifests](/guides/marketplace/kat-overview#manifests).

## KAT

**KAT** (Knowledge Agent Toolkit) is the orchestration layer that turns one or more knowledge bases into a coherent multi-domain application. KAT handles intent extraction, slot filling, multi-domain routing, disambiguation, and guardrails.

KAT supports two execution modes:

* `full`: runs the complete pipeline, including answer synthesis.
* `disambiguation_only`: routes and disambiguates, then delegates synthesis to Pinecone Assistant.

For single-knowledge-base deployments, you can use simpler strategies: `single`, `fan_out`, or `llm_classify`.

See [KAT overview](/guides/marketplace/kat-overview).

## Slot filling

A **slot** is a piece of context KAT needs to answer correctly, such as a region, a product line, or a date. When a question is missing a required slot, KAT returns an `ASK_SLOT` outcome and the consumer interface prompts the end user for the missing information. Slots are preserved across turns through `AgentContext`.

See [Disambiguation and slot filling](/guides/marketplace/kat-overview#disambiguation-and-slot-filling).

## Disambiguation outcomes

Every KAT decision resolves to one of four outcomes:

* `CALL_KB`: route the query to one or more specific knowledge bases.
* `ASK_SLOT`: ask the end user for missing context.
* `BLOCKED`: refuse the query because it violates a guardrail.
* `OUT_OF_SCOPE`: refuse the query and list what the application can help with instead.

## Layout

A **layout** is the high-level shape of the consumer interface. Marketplace provides four layouts:

* **Chat**: conversational thread with citations and follow-up suggestions.
* **Search**: query box with ranked results and previews.
* **Structured**: form-style inputs that produce a structured output.
* **Hybrid**: chat plus a persistent structured panel.

See [Configure layouts](/guides/marketplace/configure-layouts).

## Component

A **component** is a visual primitive a knowledge application can render in addition to text. Marketplace provides six components:

* Comparison tables
* Content cards
* Timelines
* Progress trackers
* Coverage matrices
* Geolocation maps

Components are read-only and retrieval-oriented. See [Configure components](/guides/marketplace/configure-components).

## Operator and end user

An **operator** is a person who builds, configures, and publishes a deployment. An **end user** is a person who uses a published knowledge application. Operators authenticate to Marketplace itself (deployer authentication). End users authenticate per deployment (consumer authentication).

See [Deployer authentication](/guides/marketplace/deployer-auth) and [Consumer authentication overview](/guides/marketplace/consumer-auth-overview).

## Connector

A **connector** is the integration that ingests documents from a source system. Google Drive is the launch connector. Manual upload is also supported. See [Connectors overview](/guides/marketplace/connectors-overview).

## Evaluation

An **evaluation** is an automatic quality check that runs on publish. Marketplace generates test questions from the connected sources, asks the application to answer them, and scores responses on faithfulness and relevance. Results are visible from the deployment dashboard. See [Evaluations](/guides/marketplace/evaluations).
