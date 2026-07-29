---
title: "Build"
source: https://elevenlabs.io/docs/eleven-agents/build/overview.md
path: docs/eleven-agents/build/overview
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Build

The Build section covers everything you need to create sophisticated conversational agents, from defining their behavior and voice to connecting external tools and knowledge sources.

#### Build agents from your AI assistant

Everything on this page can also be configured conversationally. Connect the [hosted MCP
server](/docs/eleven-agents/operate/hosted-mcp) to Claude or another MCP client to create and
update agents through natural language.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/aa4e5442250b80183bf690e4bcc3bf9517932e1c5a569e5acb539c98604a213e/assets/images/agents/agents-overview-build.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260729%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260729T233231Z&X-Amz-Expires=604800&X-Amz-Signature=c94e3a4db1e7bcae0bceb91d2a01413534406ab049ef54db7e10ac2d48f6b3c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Build your agent" />

### Design and configure

| Goal                          | Guide                                                                    | Description                                                            |
| ----------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| Create conversation workflows | [Workflows](/docs/eleven-agents/customization/agent-workflows)           | Build multi-step workflows with visual workflow builder                |
| Write system prompts          | [System prompt](/docs/eleven-agents/best-practices/prompting-guide)      | Learn best practices for crafting effective agent prompts              |
| Select language model         | [Models](/docs/eleven-agents/customization/llm)                          | Choose from supported LLMs or bring your own custom model              |
| Control conversation flow     | [Conversation flow](/docs/eleven-agents/customization/conversation-flow) | Configure turn-taking, interruptions, and timeout settings             |
| Configure voice & language    | [Voice & language](/docs/eleven-agents/customization/voice)              | Select from 5k+ voices across 31 languages with customization options  |
| Add knowledge to agent        | [Knowledge base](/docs/eleven-agents/customization/knowledge-base)       | Upload documents and enable RAG for grounded responses                 |
| Connect tools                 | [Tools](/docs/eleven-agents/customization/tools)                         | Enable agents to call clients & APIs to perform actions                |
| Personalize each conversation | [Personalization](/docs/eleven-agents/customization/personalization)     | Use dynamic variables and overrides for per-conversation customization |
| Secure agent access           | [Authentication](/docs/eleven-agents/customization/authentication)       | Implement custom authentication for protected agent access             |

## Core components

### Agent behavior

Control how your agent thinks and responds:

* **Workflows**: Visual workflow builder for complex conversation flows
* **System Prompt**: Define agent personality, tone, and capabilities
* **Models**: Choose from leading LLMs or bring your own
* **Conversation Flow**: Configure turn-taking, interruptions, and pacing

### Voice & language

Customize the agent's voice and language capabilities:

* **Voice Selection**: Choose from 5k+ professional voices
* **Multi-voice Support**: Use different voices within conversations
* **Language Support**: Deploy in 31+ languages
* **Voice Design**: Create custom voices from text descriptions

### Knowledge & tools

Extend agent capabilities with external data and actions:

* **Knowledge Base**: Upload documents to ground agent responses
* **Tools**: Connect to APIs and external services
* **MCP Integration**: Use Model Context Protocol tools
* **System Tools**: Built-in capabilities like call transfer and voicemail detection

### Personalization

Tailor each conversation to your users:

* **Dynamic Variables**: Inject runtime data into conversations
* **Overrides**: Customize agent behavior per interaction
* **Authentication**: Secure agent access with custom auth flows

## Next steps

#### [Workflows](/docs/eleven-agents/customization/agent-workflows)

Build visual conversation flows

#### [System Prompt](/docs/eleven-agents/best-practices/prompting-guide)

Learn prompting best practices

#### [Voice & Language](/docs/eleven-agents/customization/voice)

Configure voice settings

#### [Knowledge Base](/docs/eleven-agents/customization/knowledge-base)

Add domain knowledge
