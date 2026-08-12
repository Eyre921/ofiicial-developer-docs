---
title: "Deployer authentication"
source: https://docs.pinecone.io/guides/marketplace/deployer-auth
path: guides/marketplace/deployer-auth
---

Sign in to Pinecone Marketplace as an operator to create deployments, manage sessions across devices, and audit deployer actions in the event log.

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

Deployer authentication controls who can sign in to Marketplace, create deployments, edit configuration, and publish versions. This is separate from [consumer authentication](/guides/marketplace/consumer-auth-overview), which controls who can use a published knowledge application.

## Sign in or sign up

Operators sign in to Marketplace at [marketplace.pinecone.io](https://marketplace.pinecone.io). The Marketplace homepage offers `Sign up free` and `Log in` from the header. Sign-in is linked to your Pinecone organization and project, so apps and assistants you create are scoped correctly.

Operators with an existing Pinecone account can also reach Marketplace through the **Marketplace ↗** entry in the Pinecone console sidebar.

## Sessions

Sessions are stored on Marketplace's backend. Signing out ends the active session. Operators can sign in from multiple devices.

## Roles

Every deployment is owned by the operator who created it. Org and team membership with role-based access (admin, editor, viewer) is not supported.

## Audit

Significant operator actions are recorded in the deployment event log. See [Analytics and event logs](/guides/marketplace/analytics-and-event-logs).
