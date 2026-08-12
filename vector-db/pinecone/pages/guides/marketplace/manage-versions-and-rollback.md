---
title: "Manage versions and rollback"
source: https://docs.pinecone.io/guides/marketplace/manage-versions-and-rollback
path: guides/marketplace/manage-versions-and-rollback
---

Use versioned publishing in Pinecone Marketplace to stage edits, compare active and building versions, and roll back a deployment when needed.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

Marketplace treats every change to an active deployment as a new version. This makes it safe to iterate on operating parameters, content, and configuration without disrupting end users.

## Versions

A deployment has up to one active version and zero or more building versions:

* **Active version**: what end users see right now.
* **Building version**: an in-progress edit that is not yet live.

When you edit an active deployment, Marketplace creates a building version automatically. You can keep editing without publishing; nothing is sent to end users until you publish the building version. See [Publish a deployment](/guides/marketplace/publish-a-deployment).

## Version history

Every published version is preserved in the deployment's version history. The history includes:

* The version number and publish timestamp.
* The operator who published it.
* A summary of changes from the previous version.
* The evaluation result for that version.

## Rollback

If a new version regresses, you can roll back to a previous version from the version history. Rollback:

1. Promotes the selected previous version to active.
2. Returns end users to the prior behavior on their next interaction.
3. Preserves the regressed version in history so you can inspect what changed.

Rollback is fast because the previous version's underlying assistants and indexes are still provisioned.

## Best practices

* Make small changes between publishes so that evaluations and end-user feedback give you a clear signal.
* Review the evaluation result before promoting a publish to wider end-user traffic.
* Keep notes on each publish so the version history stays meaningful.
* Use rollback freely. The cost of rolling back is low; the cost of leaving a regression in front of end users is higher.

## Limits

All published versions are retained for rollback. There is no manual cleanup or version-count limit.
