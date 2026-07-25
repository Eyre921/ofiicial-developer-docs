---
title: "Model Context Protocol"
source: https://elevenlabs.io/docs/eleven-agents/customization/tools/mcp.md
path: docs/eleven-agents/customization/tools/mcp
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Model Context Protocol

#### User Responsibility

You are responsible for the security, compliance, and behavior of any third-party MCP server you
integrate with your ElevenLabs conversational agents. ElevenLabs provides the platform for
integration but does not manage, endorse, or secure external MCP servers.

## Overview

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) is an open standard that defines how applications provide context to Large Language Models (LLMs). Think of MCP as a universal connector that enables AI models to seamlessly interact with diverse data sources and tools. By integrating servers that implement MCP, you can significantly extend the capabilities of your ElevenLabs conversational agents.

MCP support is not currently available for users on Zero Retention Mode or those requiring HIPAA
compliance.

ElevenLabs allows you to connect your conversational agents to external MCP servers. This enables your agents to:

* Access and process information from various data sources via the MCP server
* Utilize specialized tools and functionalities exposed by the MCP server
* Create more dynamic, knowledgeable, and interactive conversational experiences

## Getting started

ElevenLabs supports both SSE (Server-Sent Events) and HTTP streamable transport MCP servers.

In this example, we'll use [Zapier MCP](https://zapier.com/mcp), which lets you connect ElevenAgents to hundreds of tools and services.

MCP servers are not yet manageable via the ElevenLabs CLI — use the dashboard or SDK.

#### Add via the dashboard

#### Open MCP integrations

Navigate to the [MCP server integrations dashboard](https://elevenlabs.io/app/agents/integrations) and click **Add Custom MCP Server**.

![Creating your first MCP server](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/335d1d8fced3cd82eed4ed43ba0058d3a8dbc431f81cdb387bf3d5964e5ead80/assets/images/conversational-ai/mcp-create.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T083752Z&X-Amz-Expires=604800&X-Amz-Signature=47d95136510540320b90217226800f4413c77a7b6f692400b247567732a6a833&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Configure the MCP server

Enter the following details:

* **Name**: The name of the MCP server (e.g., "Zapier MCP Server")
* **Description**: A description of what the MCP server can do
* **Server URL**: The URL of the MCP server. If this contains a secret key, treat it like a password and store it as a workspace secret.
* **Secret Token** (optional): Authorization header value
* **HTTP Headers** (optional): Any additional headers the server requires

#### Save and test the connection

Click **Add Integration** to save the integration and test the connection to list available tools.

![Zapier example tools](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/7c9d83baedd0e2dc74014d4a690159333bbef0eec37c36fa9ee0fd6cd455df0e/assets/images/conversational-ai/mcp-zapier.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T083752Z&X-Amz-Expires=604800&X-Amz-Signature=5495df0086465cd610d9124e3a2b84284da96ff5bacf0b0e56615c7332a1a93a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Attach the server to an agent

The MCP server is now available to add to your agents. MCP support is available for both public and private agents.

![Adding the MCP server to an agent](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/b18756710b4466a5fa462080d6f3b237d84f76f898d5c94d4583f31d2fa0395b/assets/images/conversational-ai/mcp-add.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T083752Z&X-Amz-Expires=604800&X-Amz-Signature=ebc57b8790d176e956c461b4aada43bfd0bfc0e2fe12b93a97c588efabf1e485&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Add via the API

```python
from elevenlabs import ElevenLabs

elevenlabs = ElevenLabs()

server = elevenlabs.conversational_ai.mcp_servers.create(
    config={
        "url": "https://mcp.zapier.com/api/mcp/...",
        "name": "Zapier MCP Server",
        "description": "An MCP server with access to Zapier's tools and services",
        "approval_policy": "always_ask",
        "transport": "SSE",
    },
)

elevenlabs.conversational_ai.agents.update(
    agent_id="agent_7101k5zvyjhmfg983brhmhkd98n6",
    conversation_config={
        "agent": {"prompt": {"mcp_server_ids": [server.id]}},
    },
)
```

```typescript
import { ElevenLabsClient } from "@elevenlabs/elevenlabs-js";

const elevenlabs = new ElevenLabsClient();

const server = await elevenlabs.conversationalAi.mcpServers.create({
  config: {
    url: "https://mcp.zapier.com/api/mcp/...",
    name: "Zapier MCP Server",
    description: "An MCP server with access to Zapier's tools and services",
    approvalPolicy: "always_ask",
    transport: "SSE",
  },
});

await elevenlabs.conversationalAi.agents.update("agent_7101k5zvyjhmfg983brhmhkd98n6", {
  conversationConfig: {
    agent: { prompt: { mcpServerIds: [server.id] } },
  },
});
```

## Tool approval modes

ElevenLabs provides flexible approval controls to manage how agents request permission to use tools from MCP servers. You can configure approval settings at both the MCP server level and individual tool level for maximum security control.

![Tool approval mode settings](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/9f4c208459131622478de5010e2234d3af8a03dc9bc5b7ec2fcab48a7be3bde3/assets/images/conversational-ai/mcp-approval.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T083752Z&X-Amz-Expires=604800&X-Amz-Signature=ceccebcd761235fb44a2faf1f2b312a9b9b0f3a4837e6e000b3c468392e89b1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Available approval modes

* **Always Ask (Recommended)**: Maximum security. The agent will request your permission before each tool use.
* **Fine-Grained Tool Approval**: Disable and pre-select tools which can run automatically and those requiring approval.
* **No Approval**: The assistant can use any tool without approval.

### Fine-grained tool control

The Fine-Grained Tool Approval mode allows you to configure individual tools with different approval requirements, giving you precise control over which tools can run automatically and which require explicit permission.

![Fine-grained tool approval
settings](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/041cad753319ed92189ee8d4f70a9d3ed07177303bf71777ce36a90270a5dd24/assets/images/conversational-ai/mcp-finegrained-approvals.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260725T083752Z&X-Amz-Expires=604800&X-Amz-Signature=51adb955e3cb8c817d9d771d5dcd70a1952f16fa92e7d2b249096475453255f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

For each tool, you can set:

* **Auto-approved**: Tool runs automatically without requiring permission
* **Requires approval**: Tool requires explicit permission before execution
* **Disabled**: Tool is completely disabled and cannot be used

Use Fine-Grained Tool Approval to allow low-risk read-only tools to run automatically while
requiring approval for tools that modify data or perform sensitive operations.

## Key considerations for ElevenLabs integration

* **External servers**: You are responsible for selecting the external MCP servers you wish to integrate. ElevenLabs provides the means to connect to them.
* **Supported features**: ElevenLabs supports MCP servers that communicate over SSE (Server-Sent Events) and HTTP streamable transports for real-time interactions.
* **Dynamic tools**: The tools and capabilities available from an integrated MCP server are defined by that external server and can change if the server's configuration is updated.

## Security and disclaimer

Integrating external MCP servers can expose your agents and data to third-party services. It is crucial to understand the security implications.

#### Important Disclaimer

By enabling MCP server integrations, you acknowledge that this may involve data sharing with
third-party services not controlled by ElevenLabs. This could incur additional security risks.
Please ensure you fully understand the implications, vet the security of any MCP server you
integrate, and review our [MCP Integration Security
Guidelines](/docs/eleven-agents/customization/tools/mcp/security) before proceeding.

Refer to our [MCP Integration Security Guidelines](/docs/eleven-agents/customization/tools/mcp/security) for detailed best practices.

## Finding or building MCP servers

* Utilize publicly available MCP servers from trusted providers
* Develop your own MCP server to expose your proprietary data or tools
* Explore the Model Context Protocol community and resources for examples and server implementations

### Resources

* [Anthropic's MCP server examples](https://docs.anthropic.com/en/docs/agents-and-tools/remote-mcp-servers#remote-mcp-server-examples) - A list of example servers by Anthropic
* [Awesome Remote MCP Servers](https://github.com/jaw9c/awesome-remote-mcp-servers) - A curated, open-source list of remote MCP servers
* [Remote MCP Server Directory](https://remote-mcp.com/) - A searchable list of Remote MCP servers
