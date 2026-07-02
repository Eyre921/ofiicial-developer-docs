---
title: "Templates overview"
source: https://docs.pinecone.io/guides/marketplace/templates-overview
path: guides/marketplace/templates-overview
---

How Pinecone Marketplace templates work, what they define, and how operators customize a deployment after creating it from a template.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

A template is a vertical configuration that bundles operating parameters, a recommended layout, suggested sources, and starter prompts for a specific use case. Templates compress the time from picking a use case to publishing a working knowledge application.

For the full list, see [Template catalog](/guides/marketplace/template-catalog).

## How resolution works

When you create a deployment from a template, Marketplace resolves configuration in three layers:

1. **Framework defaults**: baseline values that apply to every knowledge application.
2. **Vertical config**: values defined by the template, such as the system prompt, recommended layout, and starter prompts.
3. **Operator inputs**: values you provide in the setup wizard. These override the template defaults.

Each layer can override the previous one. Most operators only need to set values in the wizard.

## What a template defines

A template defines:

* The recommended consumer layout (chat, search, structured, or hybrid).
* A system prompt and operating parameters tuned for the vertical.
* Suggested visual components for the consumer interface.
* Starter prompts that surface to end users on the empty state.
* Recommended source types and structure.

A template does not define:

* The actual documents the application uses; you connect those during setup.
* The deployment name, description, or branding.
* Access policies; you choose those during setup or in the dashboard.

## Choosing a template

Pick the template that most closely matches the use case. If none match exactly, pick the closest fit and override the operating parameters. The choice of template does not lock you into a vertical; it only sets the initial configuration.

## Customize a deployment after creating it

A template is a starting point. After creating a deployment, you can override most template defaults from the deployment dashboard.

### What you can customize

The setup wizard and the deployment dashboard let you change:

* The name, description, and branding of the knowledge application.
* The system prompt and operating parameters that shape responses. See [Configure operating parameters](/guides/marketplace/configure-operating-parameters).
* The consumer layout. See [Configure layouts](/guides/marketplace/configure-layouts).
* Which visual components the application can render. See [Configure components](/guides/marketplace/configure-components).
* The connected sources and how they sync. See [Connectors](/guides/marketplace/connectors-overview).
* Starter prompts shown to end users on the empty state.
* Access policy, including the consumer authentication provider.

### What requires a new template

Structural changes that go beyond wizard inputs, such as defining a brand new vertical that other deployments will reuse, are handled by introducing a new template configuration. Operator-level template authoring is not supported.

### Edit and republish flow

1. Open the deployment dashboard.
2. Make your changes. Marketplace creates a new building version automatically when you edit an active deployment.
3. Publish the building version. Marketplace runs background provisioning, introspection, and evaluation. The previous version remains active until the new one is ready.
4. If a new version regresses, roll back from the version history. See [Manage versions and rollback](/guides/marketplace/manage-versions-and-rollback).

<Tip>
  Make small changes between publishes so that evaluations and end-user feedback give you a clear signal about what changed.
</Tip>
