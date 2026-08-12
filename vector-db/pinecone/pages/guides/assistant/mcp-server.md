---
title: "Use an Assistant MCP server"
source: https://docs.pinecone.io/guides/assistant/mcp-server
path: guides/assistant/mcp-server
---

Connect AI agents to a Pinecone Assistant MCP server via remote or local Model Context Protocol endpoints, including Cursor and Claude Desktop.

Every Pinecone Assistant has a dedicated MCP server that gives AI agents direct access to context from the assistant's uploaded files through the standardized [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). This page shows you how to connect an assistant's MCP server with Cursor, Claude Desktop, and LangChain.

<Note>
  Pinecone also provides an MCP server for managing indexes, upserting data, and querying your Pinecone database directly from an AI agent. See [Use the Pinecone MCP server](/guides/operations/mcp-server).
</Note>

There are two ways to connect to an assistant MCP server:

* [Remote MCP server](#remote-mcp-server) - Use a dedicated MCP endpoint to connect directly to an assistant.
* [Local MCP server](#local-mcp-server) - Run a Docker container locally that connects to an assistant

Both options support a context tool that allows agents to retrieve relevant context snippets from your assistant's uploaded files. This is similar to the [context API](/guides/assistant/retrieve-context-snippets) but fine-tuned for MCP clients. Additional capabilities, such as file access, will be added in future releases.

## Remote MCP server

Every Pinecone Assistant has a dedicated MCP endpoint that you can connect directly to your AI applications. This option doesn't require running any infrastructure and is managed by Pinecone.

The MCP endpoint for an assistant is:

```
https://<YOUR_PINECONE_ASSISTANT_HOST>/mcp/assistants/<YOUR_ASSISTANT_NAME>
```

<Warning>
  The previous SSE-based endpoint (with `/sse` suffix) is deprecated and will stop working on August 31, 2025 at 11:59:59 PM UTC. Before then, update to the [streamable HTTP transport](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http) MCP endpoint shown above, which implements the current MCP specification and provides improved flexibility and compatibility.
</Warning>

### Prerequisites

Before you begin, make sure you have the following values, which you'll use in the commands below:

* `<YOUR_PINECONE_API_KEY>`: [A Pinecone API key](/guides/projects/manage-api-keys).
* `<YOUR_PINECONE_ASSISTANT_HOST>`: In the Pinecone console, this is your assistant's **Host** value.
* `<YOUR_ASSISTANT_NAME>`: Your assistant's name, as displayed in the Pinecone console. For example, `example-assistant`.

### Use with Claude Code

You can use the Claude CLI to configure Claude Code to use your assistant's remote MCP server. For more information, see [Claude Code's MCP documentation](https://docs.anthropic.com/en/docs/claude-code/mcp).

1. Add the MCP server using the Claude CLI:

   ```bash theme={null}
   claude mcp add --transport http my-assistant https://<YOUR_PINECONE_ASSISTANT_HOST>/mcp/assistants/<YOUR_ASSISTANT_NAME> --header "Authorization: Bearer <YOUR_PINECONE_API_KEY>"
   ```

   Replace `<YOUR_PINECONE_API_KEY>` with your Pinecone API key, `<YOUR_PINECONE_ASSISTANT_HOST>` with your Pinecone Assistant host, and `<YOUR_ASSISTANT_NAME>` with your assistant's name.

2. Verify the server was added successfully:

   ```bash theme={null}
   claude mcp get my-assistant
   ```

3. The MCP server tools should now be available in Claude Code's chat interface.

### Use with Claude Desktop

You can configure Claude Desktop to use your assistant's remote MCP server. However, at this early stage of **remote** MCP server adoption, the Claude Desktop application does not support remote server URLs. In the example below, we work around this by using a local proxy server, [supergateway](https://github.com/supercorp-ai/supergateway), to forward requests to the remote MCP server with your API key.

<Warning>
  [supergateway](https://github.com/supercorp-ai/supergateway) is an open-source third-party tool. Use at your own risk.
</Warning>

1. Open [Claude Desktop](https://claude.ai/download) and go to **Settings**.

2. On the **Developer** tab, click **Edit Config** to open the configuration file.

3. Add the following configuration:

   ```json theme={null}
   {
     "mcpServers": {
       "Assistant over supergateway": {
         "command": "npx",
         "args": [
           "-y",
           "supergateway",
           "--streamableHttp",
           "https://<YOUR_PINECONE_ASSISTANT_HOST>/mcp/assistants/<YOUR_ASSISTANT_NAME>",
           "--header",
           "Authorization: Bearer <YOUR_PINECONE_API_KEY>"
         ]
       }
     }
   }
   ```

   Replace `<YOUR_PINECONE_API_KEY>` with your Pinecone API key and `<YOUR_PINECONE_ASSISTANT_HOST>` with your Pinecone Assistant host.

4. Save the configuration file and restart Claude Desktop.

5. From the new chat screen, you should see a hammer (MCP) icon appear with the new MCP server available.

### Use with Cursor

You can configure Cursor to use your assistant's remote MCP server directly through the `.cursor/mcp.json` configuration file.

1. Open [Cursor](https://www.cursor.com/) and create a `.cursor` directory in your project root if it doesn't exist.

2. Open `.cursor/mcp.json` (create it if necessary). To learn more, refer to [Cursor's MCP documentation](https://docs.cursor.com/context/mcp).

3. Add the following configuration:

   ```json theme={null}
   {
     "mcpServers": {
       "pinecone-assistant": {
         "url": "https://<YOUR_PINECONE_ASSISTANT_HOST>/mcp/assistants/<YOUR_ASSISTANT_NAME>",
         "headers": {
           "Authorization": "Bearer <YOUR_PINECONE_API_KEY>"
         }
       }
     }
   }
   ```

   Replace `<YOUR_PINECONE_API_KEY>` with your Pinecone API key, `<YOUR_PINECONE_ASSISTANT_HOST>` with your Pinecone Assistant host, and `<YOUR_ASSISTANT_NAME>` with your assistant's name.

4. Save the configuration file.

5. The MCP server tools should now be available in Cursor's chat interface.

### Use with LangChain

You can use the [LangChain MCP client](https://github.com/langchain-ai/langchain-mcp-adapters) to integrate with LangChain to create a powerful multi-agent workflow.

For example, the following code integrates Langchain with two assistants, one called `ai-news` and the other called `industry-reports`:

```python Python theme={null}
# Example code for integrating with LangChain
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model_name="claude-3-7-sonnet-latest", api_key="YOUR_ANTHROPIC_API_KEY")
pinecone_api_key = "<YOUR_PINECONE_API_KEY>"

async with MultiServerMCPClient(
    {
        "assistant_ai_news": {
            "url": "https://prod-1-data.ke.pinecone.io/mcp/assistants/ai-news",
            "transport": "streamable_http",
            "headers": {
                "Authorization": f"Bearer {pinecone_api_key}"
            }
        },
        "assistant_industry_reports": {
            "url": "https://prod-1-data.ke.pinecone.io/mcp/assistants/industry-reports",
            "transport": "streamable_http",
            "headers": {
                "Authorization": f"Bearer {pinecone_api_key}"
            }
        }
    }
) as client:
    agent = create_react_agent(model, client.get_tools())

    response = await agent.ainvoke({"messages": "Your task is research the next trends in AI, and form a report with the most undervalued companies in the space. You have access to two assistants, one that can help you find the latest trends in AI, and one that can help you find reports on companies."})
    print(response["messages"][-1].content)
```

## Local MCP server

Pinecone provides an open-source Pinecone Assistant MCP server that you can run locally with Docker. This option is useful for development, testing, or when you want to run the MCP server within your own infrastructure or expand the MCP server to include additional capabilities.

For the most up-to-date information on the local MCP server, see the [Pinecone Assistant MCP server repository](https://github.com/pinecone-io/assistant-mcp).

### Prerequisites

* Docker is installed and running on your system.
* A Pinecone API key. You can create a new key in the [Pinecone console](https://app.pinecone.io/organizations/-/keys).
* Your Pinecone Assistant host. To find it, go to your assistant in the [Pinecone console](https://app.pinecone.io/organizations/-/assistants). You'll see the assistant **Host** in the sidebar.

### Start the MCP server

Download the `assistant-mcp` Docker image:

```bash theme={null}
docker pull ghcr.io/pinecone-io/assistant-mcp
```

Start the MCP server, providing your Pinecone API key and Pinecone Assistant host:

```bash theme={null}
docker run -i --rm \
  -e PINECONE_API_KEY=<PINECONE_API_KEY> \
  -e PINECONE_ASSISTANT_HOST=<PINECONE_ASSISTANT_HOST> \
  pinecone/assistant-mcp
```

### Use with Claude Desktop

1. Open [Claude Desktop](https://claude.ai/download) and go to **Settings**.

2. On the **Developer** tab, click **Edit Config** to open the configuration file.

3. Add the following configuration:

   ```json theme={null}
   {
     "mcpServers": {
       "pinecone-assistant": {
         "command": "docker",
         "args": [
           "run", 
           "-i", 
           "--rm", 
           "-e", 
           "PINECONE_API_KEY", 
           "-e", 
           "PINECONE_ASSISTANT_HOST", 
           "pinecone/assistant-mcp"
         ],
         "env": {
           "PINECONE_API_KEY": "<YOUR_PINECONE_API_KEY>",
           "PINECONE_ASSISTANT_HOST": "<YOUR_PINECONE_ASSISTANT_HOST>"
         }
       }
     }
   }
   ```

   Replace `<YOUR_PINECONE_API_KEY>` with your Pinecone API key and `<YOUR_PINECONE_ASSISTANT_HOST>` with your Pinecone Assistant host.

4. Save the configuration file and restart Claude Desktop.

5. From the new chat screen, you should see a hammer (MCP) icon appear with the new MCP server available.

### Use with Cursor

1. Open [Cursor](https://www.cursor.com/) and create a `.cursor` directory in your project root if it doesn't exist.

2. Open `.cursor/mcp.json` (create it if necessary). To learn more, refer to [Cursor's MCP documentation](https://docs.cursor.com/context/mcp).

3. Add the following configuration:

   ```json theme={null}
   {
     "mcpServers": {
       "pinecone-assistant": {
         "command": "docker",
         "args": [
           "run", 
           "-i", 
           "--rm", 
           "-e", 
           "PINECONE_API_KEY", 
           "-e", 
           "PINECONE_ASSISTANT_HOST", 
           "pinecone/assistant-mcp"
         ],
         "env": {
           "PINECONE_API_KEY": "<YOUR_PINECONE_API_KEY>",
           "PINECONE_ASSISTANT_HOST": "<YOUR_PINECONE_ASSISTANT_HOST>"
         }
       }
     }
   }
   ```

   Replace `<YOUR_PINECONE_API_KEY>` with your Pinecone API key and `<YOUR_PINECONE_ASSISTANT_HOST>` with your Pinecone Assistant host.

4. Save the configuration file.

## Next Steps

* Visit the [Pinecone Assistant MCP Server repository](https://github.com/pinecone-io/assistant-mcp) for detailed installation and usage instructions

* Learn about [Model Context Protocol](https://modelcontextprotocol.io/) and how it enables AI agents to interact with tools and data

* Explore [retrieve context snippets](/guides/assistant/retrieve-context-snippets) to understand the underlying API functionality
