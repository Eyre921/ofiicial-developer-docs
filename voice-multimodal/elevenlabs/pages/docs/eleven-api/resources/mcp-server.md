---
title: "ElevenLabs MCP server"
source: https://elevenlabs.io/docs/eleven-api/resources/mcp-server.md
path: docs/eleven-api/resources/mcp-server
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# ElevenLabs MCP server

## Overview

The ElevenLabs MCP server is a remote [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that gives AI assistants access to your ElevenLabs workspace. Once connected, an assistant such as Claude, ChatGPT or Cursor can generate speech, images, video and sound, design voices, build [Flows](/docs/eleven-creative/products/flows) and manage your agents through natural language, with nothing to install or run locally.

The server is available at:

```
https://api.elevenlabs.io/v1/mcp
```

Authentication uses OAuth. When you connect, you sign in with your ElevenLabs account, choose a workspace and approve the permissions the assistant requests. No API keys are copied into the client, and generations use the credits of the workspace you sign in with.

> **Note**
>
> Looking to give your ElevenLabs agent access to external MCP servers instead? See the [MCP integration guide](/docs/eleven-agents/customization/tools/mcp).

## What it is for

Use the MCP server when you want to work with ElevenLabs from the assistant you already use, instead of switching to the ElevenLabs app or writing code against the API. It suits two kinds of work:

* **Creative work**: generating voiceovers, images, video, sound effects and music from a conversation, and refining them over several turns.
* **Agent work**: creating, configuring, testing and reviewing [ElevenAgents](/docs/eleven-agents/overview) agents.

To build ElevenLabs into your own application, use the [API](/docs/api-reference/introduction) and [SDKs](/docs/eleven-api/resources/libraries) instead.

## Connect from Claude

Add the server as a custom connector. This gives Claude every tool the server offers.

#### Open the connector menu

In Claude, go to **Settings** > **Connectors** and select **Add custom connector**. You can also
select the **+** button in a new chat, then **Add connector** > **Add custom connector**.

#### Enter the server URL

Name the connector "ElevenLabs" and enter `https://api.elevenlabs.io/v1/mcp`. Select **Add**.

#### Sign in and authorize

Complete the OAuth flow with your ElevenLabs account. Choose the workspace, review the requested
permissions, and select **Authorize**.

> **Warning**
>
> The ElevenLabs connector listed in the Claude connector directory is a restricted version. It
> covers speech, voices, transcription and agents, but cannot generate images, video or music. Add
> the custom connector above for the full set of tools.

Other MCP clients work the same way: point the client at the server URL and complete the OAuth flow. No client registration is needed for clients that support hosted client metadata (CIMD). If your workspace is in an isolated data residency environment, use your region's URL, listed in [Data residency regions](/docs/eleven-agents/operate/hosted-mcp#data-residency-regions).

## Creative tools

Every creative generation lands on a [Flow](/docs/eleven-creative/products/flows): an editable canvas that holds the prompts, references and results. The assistant returns a link to the flow, so you can open it in the ElevenLabs app to review the results, adjust a node or run it again. Clients that support MCP Apps, such as Claude, also show the flow and its results inline in the chat.

With the creative tools, an assistant can:

* Generate images and video, and edit existing images
* Generate speech from text with any voice in your workspace, and transcribe audio
* Generate sound effects, music and other audio through Flow nodes
* Design a new voice from a description and save the one you pick
* Chain generations on one flow, such as a video with a voiceover or a lipsync from generated speech
* Use your own files as references, uploaded from your computer or fetched from a URL
* Manage brand kits so generations follow your brand's colors, fonts and logos
* Look up the available models, their parameters and prompting guides

Image and video generations return several variations by default, and speech returns two takes. Tell the assistant which variation to use, and it carries that one into the next step.

> **Note**
>
> Generating spends credits in the same way as generating in the ElevenLabs app. Avoid asking the
> assistant to retry a generation that is still running, because each retry starts and charges a new
> generation.

### Example prompts

* "Generate a product shot of a ceramic coffee mug on a marble counter, morning light, 16:9."
* "Turn the second image into a five-second video with a slow push-in."
* "Write a 20-second voiceover for this video in a warm British voice, and add it to the same flow."
* "Design a voice for a gruff old sea captain and let me hear three previews."
* "Transcribe the attached interview and list the speakers."

## Agent tools

The agent tools create, configure and manage the agents in your workspace. They cover agent settings, conversations and transcripts, procedures, tools, knowledge base documents, tests, branches, deployments and issues. See [Hosted MCP for ElevenAgents](/docs/eleven-agents/operate/hosted-mcp) for the full list, example prompts and the behavior of agent updates.

## Generated files

The server returns generated files as links on `elevenlabsusercontent.com`, the ElevenLabs domain for user content. ElevenLabs serves user content from a separate domain so that files in your workspace cannot read or set cookies for `elevenlabs.io`.

These links are signed and expire about two hours after the assistant receives them. To get a new link, ask the assistant to fetch the generation again, or open the flow in the ElevenLabs app. If your network or your MCP client restricts which domains can load media, allow `elevenlabsusercontent.com`.

## Permissions

The OAuth consent screen lists the permissions the assistant requests, such as ElevenAgents, Text to Speech, Flows, and Image & Video Generation. The assistant can only perform actions covered by the permissions you approve and by your role in the workspace. You can revoke the connection at any time from your MCP client or from your ElevenLabs account settings.

MCP clients such as Claude also let you choose which of the connector's tools the assistant can use and which require your approval before each call. Workspace administrators can configure these controls for their whole organization.

## Related resources

#### [Hosted MCP for ElevenAgents](/docs/eleven-agents/operate/hosted-mcp)

Agent tools, data residency URLs and agent permissions.

#### [Flows](/docs/eleven-creative/products/flows)

The canvas every creative generation lands on.

#### [Agent tooling](/docs/eleven-api/resources/agent-tooling)

Agent skills and other tools for coding assistants.

#### [API reference](/docs/api-reference/introduction)

Full REST API for programmatic control of the platform.
