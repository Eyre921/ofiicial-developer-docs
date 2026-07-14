---
title: "IP allowlisting"
source: https://elevenlabs.io/docs/eleven-api/resources/ip-allowlisting.md
path: docs/eleven-api/resources/ip-allowlisting
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# IP allowlisting

## Overview

If your infrastructure requires IP-based access controls, you can add ElevenLabs' static egress IP addresses to your firewall allowlist. All outbound requests from ElevenLabs services—including webhooks, WebSocket connections, and MCP server requests—originate from these addresses.

## Static egress IPs

The following IP addresses are used for all ElevenLabs services:

| Region       | IP Address     |
| ------------ | -------------- |
| US (Default) | 34.67.146.145  |
| US (Default) | 34.59.11.47    |
| EU           | 35.204.38.71   |
| EU           | 34.147.113.54  |
| Asia         | 35.185.187.110 |
| Asia         | 35.247.157.189 |

## Data residency IPs

If you are using a [data residency region](/docs/overview/administration/data-residency), outbound requests use the following IPs:

| Region              | IP Address     |
| ------------------- | -------------- |
| EU Residency        | 34.77.234.246  |
| EU Residency        | 34.140.184.144 |
| India Residency     | 34.93.26.174   |
| India Residency     | 34.93.252.69   |
| Singapore Residency | 34.87.23.17    |
| Singapore Residency | 34.126.179.103 |

These static IPs are used across all ElevenLabs services and will remain consistent. If ElevenLabs
adds new IPs, we will communicate changes in advance through the [changelog](/docs/changelog).

## When to use IP allowlisting

IP allowlisting is useful when:

* Your webhook endpoints are behind a firewall that restricts inbound traffic
* Your [Speech Engine](/docs/overview/capabilities/speech-engine) server only accepts connections from known sources
* Your [MCP server](/docs/eleven-agents/customization/tools/mcp/security) integration requires IP-based access controls
* Your SIP trunk provider requires IP allowlisting for authentication

## Services that use these IPs

The static egress IPs apply to all outbound requests from ElevenLabs, including:

* **Post-call webhooks**: Notifications sent after ElevenAgents calls complete. See [post-call webhooks](/docs/eleven-agents/workflows/post-call-webhooks).
* **Speech Engine**: WebSocket connections from ElevenLabs to your server. See [Speech Engine](/docs/overview/capabilities/speech-engine).
* **MCP server requests**: Requests to your Model Context Protocol servers. See [MCP security](/docs/eleven-agents/customization/tools/mcp/security).
* **Webhook tools**: Outbound calls from agent webhook tools.

## Security recommendations

Combine IP allowlisting with other authentication mechanisms for defense in depth.

For webhook endpoints, use IP allowlisting together with [HMAC signature validation](/docs/eleven-agents/workflows/post-call-webhooks#authentication) to verify that requests originate from ElevenLabs.

For Speech Engine servers, IP allowlisting can replace or supplement JWT verification. If your server sits behind infrastructure that restricts traffic to ElevenLabs' egress IPs, you can disable JWT verification by setting `disableAuth: true` (TypeScript) or `disable_auth=True` (Python). See the [JavaScript SDK reference](/docs/eleven-api/resources/libraries/speech-engine/javascript-sdk-reference#disabling-authentication) or [Python SDK reference](/docs/eleven-api/resources/libraries/speech-engine/python-sdk-reference#disabling-authentication) for details.

Only disable authentication if you have IP allowlisting or equivalent network-level restrictions
in place. Without one, anyone on the internet can open a session and consume your resources.

## API key IP restrictions

You can also restrict your ElevenLabs API keys to only work from specific IP addresses. This is a separate feature from egress IP allowlisting and controls which IPs can make requests *to* the ElevenLabs API.

See [API key IP allowlisting](/docs/overview/administration/workspaces/api-keys#ip-allowlisting) for details.
