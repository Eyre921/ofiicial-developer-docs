---
title: "Docker/Podman"
source: https://developers.deepgram.com/docs/dockerpodman.md
path: docs/dockerpodman
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Docker/Podman

## Should I use this for my self-hosted environment?

Docker and Podman are a simple, fast approach for deploying containers. They are best used in environments that require a small, static number of Deepgram containers. This may include development environments, proof-of-concept implementations, and production environments handling low levels of API traffic.

Larger production environments often have certain security, availability, and scaling requirements, such as:

* Fine-grained Role-Based Access Control (RBAC) and other security policies
* Zero downtime maintenance and upgrades
* Auto-scaling system capacity based on system load

If any of the above apply to you, a [Kubernetes cluster](/docs/kubernetes) may better fulfill these requirements.

***

What’s Next

If you'll deploy with Docker or Podman, choose where you will deploy your infrastructure to begin setting up your deployment environment.

* [Amazon Web Services](/docs/aws-docker-podman)
* [Google Cloud Platform](/docs/gcp-docker-podman)
* [Oracle Cloud Infrastructure](/docs/oci-docker-podman)
* [Microsoft Azure](/docs/azure-docker-podman)
* [Bare-Metal Servers](/docs/bare-metal)
