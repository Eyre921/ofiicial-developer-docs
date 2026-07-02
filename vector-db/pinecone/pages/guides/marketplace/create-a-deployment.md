---
title: "Create a deployment"
source: https://docs.pinecone.io/guides/marketplace/create-a-deployment
path: guides/marketplace/create-a-deployment
---

Create a new deployment in Pinecone Marketplace from a vertical template.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

This page shows you how to create a [deployment](/guides/marketplace/concepts#deployment) in Pinecone Marketplace.

## Before you begin

* A Marketplace account. See the [Quickstart](/guides/marketplace/quickstart) for access.
* A clear use case in mind, so you can pick a starting [template](/guides/marketplace/template-catalog).

## 1. Open the catalog

Go to [marketplace.pinecone.io](https://marketplace.pinecone.io) and select **New deployment**. The catalog lists the available vertical templates.

## 2. Pick a template

Choose the template that most closely matches your use case. Templates set the initial system prompt, recommended layout, suggested components, and starter prompts. You can change any of these later.

## 3. Name the deployment

In the setup wizard:

* Give the deployment a short, descriptive name.
* Add a one-line description that end users see in the application header.
* Select the Pinecone organization and project the deployment belongs to.

## 4. Choose a layout

Pick the consumer layout that fits the experience you want: chat, search, structured, or hybrid. The template suggests a default, which you can override. See [Configure layouts](/guides/marketplace/configure-layouts).

## 5. Configure operating parameters

Tune the system prompt, response style, and other operating parameters. For details, see [Configure operating parameters](/guides/marketplace/configure-operating-parameters).

## 6. Add a knowledge base

A deployment must have at least one knowledge base. For each knowledge base:

* Give it a name that describes the domain (for example, `policies`, `product-docs`).
* Connect a source. See [Connectors](/guides/marketplace/connectors-overview).

You can add additional knowledge bases now or later. Multi-knowledge-base deployments use the [Knowledge Agent Toolkit (KAT)](/guides/marketplace/kat-overview) to route between domains.

## 7. Save as a building version

When you finish the wizard, Marketplace saves your work as a building version. The deployment is not yet live. From the dashboard, you can:

* Continue editing the building version.
* Publish it. See [Publish a deployment](/guides/marketplace/publish-a-deployment).

<Note>
  You can edit a building version as many times as you want before publishing. Each edit replaces the in-progress configuration; nothing is sent to end users until you publish.
</Note>
