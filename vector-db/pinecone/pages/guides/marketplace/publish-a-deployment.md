---
title: "Publish a deployment"
source: https://docs.pinecone.io/guides/marketplace/publish-a-deployment
path: guides/marketplace/publish-a-deployment
---

How to publish a Pinecone Marketplace deployment so end users can use it.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

Publishing promotes a building version of a deployment to active. End users interact with the active version. Publishing is non-blocking: provisioning runs in the background, and you can navigate away and return when the deployment is ready.

## What happens on publish

When you publish a building version, Marketplace:

1. Returns immediately and starts provisioning in the background.
2. Creates or updates the underlying Pinecone assistants for each knowledge base.
3. Uploads any staged files and waits for processing to complete.
4. Runs introspection to build [manifests](/guides/marketplace/kat-overview#manifests).
5. Generates suggested starter prompts for the consumer interface.
6. Runs an automatic [evaluation](/guides/marketplace/evaluations) on a sample of generated questions.
7. Marks the version active when all steps succeed, or marks it failed and surfaces the error.

The previous active version remains live until the new version is fully ready.

## Before you publish

* Confirm the connected sources are in sync. See [Sync and freshness](/guides/marketplace/connectors-overview#sync-and-freshness).
* Review operating parameters and starter prompts. See [Configure operating parameters](/guides/marketplace/configure-operating-parameters).
* Confirm the consumer authentication policy. See [Consumer authentication overview](/guides/marketplace/consumer-auth-overview).

## Publish

From the deployment dashboard, open the building version and select **Publish**. Marketplace shows the version transitioning through provisioning steps in the dashboard.

## Monitor publish progress

The dashboard reports per-step status:

* **Provisioning**: assistants are being created or updated.
* **Processing files**: staged files are being indexed.
* **Introspecting**: manifests are being generated.
* **Generating starters**: starter prompts are being created.
* **Evaluating**: the automatic evaluation is running.
* **Active**: the version is live.
* **Failed**: a step failed; the error is shown.

If publish fails, fix the underlying issue and republish. The previous active version remains untouched.

## After publish

* Share the deployment URL with end users.
* Watch the [event log](/guides/marketplace/analytics-and-event-logs) for early traffic and refusals.
* Review the [evaluation](/guides/marketplace/evaluations) results.
* Iterate on operating parameters or content and publish a new version when needed.

## Publishing again

Editing an active deployment creates a new building version automatically. Publish the building version when you are ready. Each publish is preserved in the version history; see [Manage versions and rollback](/guides/marketplace/manage-versions-and-rollback).
