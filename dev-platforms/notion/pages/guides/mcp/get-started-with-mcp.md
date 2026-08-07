---
title: "Connect to Notion MCP"
source: https://developers.notion.com/guides/mcp/get-started-with-mcp
path: guides/mcp/get-started-with-mcp
---

Connect an MCP client to your Notion workspace.

Follow the instructions for your MCP client. After you authorize the connection, the client can read and update content that you can access in the selected Notion workspace.

## Claude Code

Run this command in your terminal:

```bash theme={null}
claude mcp add --transport http notion https://mcp.notion.com/mcp
```

Then authenticate by running `/mcp` in Claude Code and following the OAuth flow.

<Accordion title="Using --scope flag for different installation scopes">
  * `--scope local` (default): Available only to you in the current project
  * `--scope project`: Shared with your team via `.mcp.json` file
  * `--scope user`: Available to you across all projects
</Accordion>

Use the `/mcp` command to list and manage the MCP servers you have installed, and use the `/context` command to understand the context token usage of your current session, including the number of tokens used by each MCP server that's enabled.

<Tip>
  Install the [Notion plugin for Claude Code](https://github.com/makenotion/claude-code-notion-plugin) to add the MCP server, Skills, and slash commands for common Notion workflows.
</Tip>

## Cursor

<Steps>
  <Step>
    Open **Cursor Settings** → **MCP** → **Add new global MCP server**
  </Step>

  <Step>
    Paste the following configuration:

    ```json theme={null}
    {
      "mcpServers": {
        "notion": {
          "url": "https://mcp.notion.com/mcp"
        }
      }
    }
    ```
  </Step>

  <Step>
    Save and restart Cursor. When you use a Notion tool for the first time, complete the OAuth flow to connect your workspace.
  </Step>
</Steps>

<Accordion title="Project-level configuration">
  To share the Notion MCP configuration with your team, create a `.cursor/mcp.json` file in your project root:

  ```json theme={null}
  {
    "mcpServers": {
      "notion": {
        "url": "https://mcp.notion.com/mcp"
      }
    }
  }
  ```
</Accordion>

## VS Code (GitHub Copilot)

<Steps>
  <Step>
    Create a `.vscode/mcp.json` file in your workspace:

    ```json theme={null}
    {
      "servers": {
        "notion": {
          "type": "http",
          "url": "https://mcp.notion.com/mcp"
        }
      }
    }
    ```
  </Step>

  <Step>
    Open the Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`) and run **MCP: List Servers**
  </Step>

  <Step>
    Start the Notion server and complete the OAuth flow when prompted
  </Step>
</Steps>

<Accordion title="User-level configuration">
  To configure Notion MCP across all workspaces, run **MCP: Open User Configuration** from the Command Palette and add the server configuration there.
</Accordion>

## Claude Desktop

<Steps>
  <Step>
    Open **Settings** → **Connectors**
  </Step>

  <Step>
    Select **Add Connector** and enter the URL:

    ```
    https://mcp.notion.com/mcp
    ```
  </Step>

  <Step>
    Complete the OAuth flow to connect your Notion workspace
  </Step>
</Steps>

<Note>
  Remote MCP servers in Claude Desktop are configured through Settings → Connectors, not the `claude_desktop_config.json` file. Available on Pro, Max, Team, and Enterprise plans.
</Note>

## Windsurf

<Steps>
  <Step>
    Open **Windsurf Settings** (`Cmd+,` on Mac) → search for **MCP**
  </Step>

  <Step>
    Select **View raw config** to open `mcp_config.json`
  </Step>

  <Step>
    Add the Notion server configuration:

    ```json theme={null}
    {
      "mcpServers": {
        "notion": {
          "serverUrl": "https://mcp.notion.com/mcp"
        }
      }
    }
    ```
  </Step>

  <Step>
    Save and restart Windsurf. Complete the OAuth flow when prompted.
  </Step>
</Steps>

## ChatGPT

<Steps>
  <Step>
    Go to [chatgpt.com/#settings/Connectors](https://chatgpt.com/#settings/Connectors) (requires login)
  </Step>

  <Step>
    Select **Add Connector** and enter the URL:

    ```
    https://mcp.notion.com/mcp
    ```
  </Step>

  <Step>
    Complete the OAuth flow to connect your Notion workspace
  </Step>
</Steps>

## Codex

For more details, see the [Codex MCP documentation](https://developers.openai.com/codex/mcp/).

<Steps>
  <Step>
    Add the Notion server to your Codex configuration at `~/.codex/config.toml`:

    ```toml theme={null}
    [mcp_servers.notion]
    url = "https://mcp.notion.com/mcp"
    ```
  </Step>

  <Step>
    Authenticate by running:

    ```bash theme={null}
    codex mcp login notion
    ```

    Complete the OAuth flow to connect your Notion workspace.
  </Step>
</Steps>

<Accordion title="Project-level configuration">
  To share the Notion MCP configuration with your team, create a `.codex/config.toml` file in your project root with the same server configuration.
</Accordion>

## Antigravity

We recommend connecting to Notion MCP as a custom server rather than using the pre-configured "Notion" connector in the Antigravity MCP gallery, which uses the deprecated [`notion-mcp-server`](https://github.com/makenotion/notion-mcp-server) package.

<Steps>
  <Step>
    Follow the [Antigravity instructions for connecting custom MCP servers](https://antigravity.google/docs/mcp#connecting-custom-mcp-servers) and add the following to your `mcp_config.json`:

    ```json theme={null}
    {
      "mcpServers": {
        "notion": {
          "serverUrl": "https://mcp.notion.com/mcp"
        }
      }
    }
    ```
  </Step>

  <Step>
    Save the configuration. Antigravity will prompt you to complete the OAuth flow to connect your Notion workspace.
  </Step>
</Steps>

## Other MCP clients

If your MCP client isn't listed above, use one of these URLs:

| Transport                         | URL                          | Notes                                          |
| :-------------------------------- | :--------------------------- | :--------------------------------------------- |
| **Streamable HTTP** (recommended) | `https://mcp.notion.com/mcp` | Recommended for new clients                    |
| **SSE** (Server-Sent Events)      | `https://mcp.notion.com/sse` | For clients that don't support Streamable HTTP |

### JSON configuration format

Most MCP clients accept a JSON configuration. Use the format supported by your client:

<CodeGroup>
  ```json Streamable HTTP theme={null}
  {
    "mcpServers": {
      "notion": {
        "url": "https://mcp.notion.com/mcp"
      }
    }
  }
  ```

  ```json SSE theme={null}
  {
    "mcpServers": {
      "notion": {
        "type": "sse",
        "url": "https://mcp.notion.com/sse"
      }
    }
  }
  ```

  ```json STDIO (via mcp-remote) theme={null}
  {
    "mcpServers": {
      "notion": {
        "command": "npx",
        "args": ["-y", "mcp-remote", "https://mcp.notion.com/mcp"]
      }
    }
  }
  ```
</CodeGroup>

Use the STDIO configuration if your client doesn't support remote HTTP connections.

## Connect through the Notion app

You can also start the connection from Notion:

<Steps>
  <Step>
    Open **Settings** in the Notion app
  </Step>

  <Step>
    Go to **Connections** → **Notion MCP**
  </Step>

  <Step>
    Choose your MCP client from the list and complete the OAuth flow
  </Step>
</Steps>

## Troubleshooting

<AccordionGroup>
  <Accordion title="My MCP client doesn't support remote MCP servers">
    Some MCP clients only support local stdio servers. You can still connect to Notion MCP using the [mcp-remote](https://www.npmjs.com/package/mcp-remote) bridge:

    ```json theme={null}
    {
      "mcpServers": {
        "notion": {
          "command": "npx",
          "args": ["-y", "mcp-remote", "https://mcp.notion.com/mcp"]
        }
      }
    }
    ```

    As a last resort, you can run our [open-source MCP server](https://github.com/makenotion/notion-mcp-server) locally, though this package is no longer actively maintained.
  </Accordion>

  <Accordion title="Authentication issues">
    * Complete the OAuth flow when prompted.
    * Disconnect and reconnect the client. Look for **Clear authentication** or **Disconnect** in its MCP settings.
    * Check your permissions in the Notion workspace that you're trying to access.
  </Accordion>

  <Accordion title="My MCP client isn't listed here">
    Check the client's documentation for how to add a remote MCP server. Most MCP clients accept a URL or JSON configuration. If the client doesn't support MCP, contact its developer.
  </Accordion>
</AccordionGroup>

## FAQ

<AccordionGroup>
  <Accordion title="Can I use Notion MCP without interactive authorization?">
    Yes. Notion MCP accepts a [personal access token (PAT)](/guides/get-started/personal-access-tokens) from MCP clients that can send custom HTTP headers. Connect to `https://mcp.notion.com/mcp` and send the PAT in the authorization header:

    ```http theme={null}
    Authorization: Bearer {PERSONAL_ACCESS_TOKEN}
    ```

    The PAT must have the **Notion API** capability. It uses the permissions of the person who created it, so store it in an environment variable or secret manager and don't put it in shared client configuration.

    Not every MCP client supports custom HTTP headers. PAT-authenticated requests also don't appear in [List MCP client connections](/reference/admin/list-mcp-client-connections). Organization owners can manage these credentials with [List personal access tokens](/reference/admin/list-personal-access-tokens) and [Revoke a personal access token](/reference/admin/revoke-personal-access-token).

    Review [security best practices](/guides/mcp/mcp-security-best-practices) before allowing an MCP client to take actions without confirmation.
  </Accordion>

  <Accordion title="Does Notion MCP support file uploads?">
    Yes. Use the [`notion-create-file-upload` tool](/guides/mcp/mcp-supported-tools#create-a-file-upload-url) to upload images and other files up to 20 MiB. Workspace file-size limits still apply.

    The tool returns a short-lived upload URL and the headers and form field that the MCP client must use to send the file. After the upload succeeds, pass the response's `suggested_markdown` directly to `notion-create-pages` or `notion-update-page`, or include it on a separate line in `notion-create-comment` markdown to attach the file. For larger files, use the [file upload API](/guides/data-apis/working-with-files-and-media).
  </Accordion>

  <Accordion title="What's the difference between Notion MCP and the open-source server?">
    **Notion MCP** (`https://mcp.notion.com/mcp`) is our hosted, actively maintained server. It supports OAuth and PAT bearer authentication and requires no infrastructure setup.

    The **open-source server** ([`notion-mcp-server`](https://github.com/makenotion/notion-mcp-server)) is no longer actively maintained. It supports bearer token authentication and the original JSON-based v1 APIs, which may be useful for automated workflows, but requires you to manage your own connection and deployment.

    For most users, we recommend Notion MCP.
  </Accordion>

  <Accordion title="I'm building my own MCP client">
    If you're integrating Notion MCP into your own application, see
    [Build an MCP client for Notion](/guides/mcp/build-mcp-client) for OAuth
    and connection requirements.
  </Accordion>
</AccordionGroup>

## Next steps

See the [Notion MCP tools](/guides/mcp/mcp-supported-tools) that a connected client can use.
