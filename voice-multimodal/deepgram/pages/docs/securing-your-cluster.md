---
title: "Securing Your Cluster"
source: https://developers.deepgram.com/docs/securing-your-cluster.md
path: docs/securing-your-cluster
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Securing Your Cluster

# Secrets

Deepgram strongly recommends following best practices for configuring Kubernetes Secrets. Resources offered by Deepgram assist your secrets security posture as follows:

* The `deepgram-self-hosted` Helm chart includes options to configure RBAC rules for all resources.
* Deepgram documentation instructs users to deploy Deepgram services in a dedicated namespace in your cluster.
  * This prevents workloads in other namespaces from reading Secrets intended for Deepgram-related resources, and restricts Deepgram-related resources from reading Secrets deployed in other namespaces in your cluster.
* Deepgram documentation recommends using an external Secret store provider.
