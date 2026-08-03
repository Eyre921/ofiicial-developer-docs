---
title: "Kubernetes"
source: https://developers.deepgram.com/docs/kubernetes.md
path: docs/kubernetes
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Kubernetes

## Should I use this for my self-hosted environment?

Kubernetes is a powerful ecosystem that can be customized to meet almost any business requirement. It is a great option for environments with extensive security, availability, and scaling requirements, such as production environments handling high levels of API traffic.

The power of Kubernetes is bundled with a greater level of complexity when compared with lighter platforms such as Docker or Podman. The following environment types usually only require a small, static number of Deepgram containers, which you may consider deploying with [Docker/Podman](/docs/dockerpodman) instead:

* Development environments
* Proof-of-concept implementations
* Production environment handling low levels of API traffic

---

What’s Next

If you'll deploy with Kubernetes, choose where you will deploy your infrastructure to begin setting up your deployment environment.

* [Amazon Web Services](/docs/aws-k8s)
* [Google Cloud Platform](/docs/gcp-k8s)
* [Self-Managed Kubernetes](/docs/self-managed-kubernetes)
