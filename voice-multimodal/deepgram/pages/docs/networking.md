---
title: "Networking"
source: https://developers.deepgram.com/docs/networking.md
path: docs/networking
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Networking

When scaling a self-hosted Deepgram deployment for real-time streaming, the ingress and network layer in front of your API pods is a key part of your scaling strategy. In many deployments, the network layer — instead of Engine or GPU capacity — limits total concurrent connections. Plan and configure it deliberately alongside your pod scaling.

## Why Networking Matters When Scaling Streaming

Streaming uses long-lived WebSocket connections, so the load balancer and network path must sustain a high number of concurrent, long-lived connections.

Adding Engine pods increases inference capacity, but concurrent-stream capacity will not scale with it if the network layer throttles connections first. In that case you may see WebSocket handshake timeouts or dropped connections while Engine and GPU utilization still look healthy.

Plan network capacity — load balancer settings, connection limits, and client-side network configuration — as part of scaling, not just pod count.

## Reviewing Your Network Configuration

When validating that your network layer can scale with your deployment, review:

* **Ingress manifest and ALB annotations** — or the AWS Load Balancer Controller config. Confirm connection limits, idle timeouts, and target group settings support the number of concurrent WebSocket connections you expect.
* **ALB CloudWatch metrics and access logs** — especially connection counts, rejected connections, and errors during load. These surface whether the load balancer is the bottleneck before Engine pods saturate.
* **Client-side network configuration** — any connection limits on the path to your deployment (proxy pools, NAT gateways, DNS TTLs) can cap total concurrent connections independently of Deepgram.
