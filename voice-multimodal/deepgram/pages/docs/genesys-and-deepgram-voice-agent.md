---
title: "Genesys Cloud CX and Deepgram Voice Agent"
source: https://developers.deepgram.com/docs/genesys-and-deepgram-voice-agent.md
path: docs/genesys-and-deepgram-voice-agent
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Genesys Cloud CX and Deepgram Voice Agent

> Learn how to integrate Genesys Cloud CX with the Deepgram Voice Agent API for real-time conversational AI using the Genesys Audio Connector.

# Genesys Cloud CX and Deepgram Voice Agent

The Deepgram [Voice Agent API](/docs/voice-agent) integrates with Genesys Cloud CX through the Genesys Audio Connector, establishing a bidirectional WebSocket connection for real-time voice input and output.

The Voice Agent API bundles speech-to-text, LLM reasoning, and text-to-speech into a single pipeline, delivering approximately 425 ms round-trip latency.

---

## How it works

1. A caller enters your Genesys call flow
2. Genesys connects to your Voice Agent through a WebSocket
3. Audio streams to Deepgram (STT, LLM, TTS)
4. The agent responds with synthesized voice
5. The caller can interrupt naturally with barge-in support

---

## Before you begin

You will need:

* A Deepgram API key with Voice Agent enabled
* A Genesys Cloud CX account with Audio Connector access
* A public server endpoint connected to Deepgram

Before you can use Deepgram, you'll need to [create a Deepgram account](https://console.deepgram.com/signup?jump=keys). Signup is free and includes **\$200** in free credit and access to all of Deepgram's features!

---

## Step 1: Create an Audio Connector in Genesys

1. Go to **Admin > Integrations**
2. Add **Audio Connector**
3. Name the integration (for example, `Deepgram Voice Agent`)
4. Set **Connection URI** to `wss://integrations.deepgram.com/genesys/ac`
5. Add your Deepgram API key under **Credentials**
6. Activate the integration

---

## Step 2: Add the connector to your Architect flow

1. Open **Architect** in Genesys Cloud
2. Open or create an **Inbound Call Flow**
3. Add a **Call Audio Connector** action
4. Select the integration you created in Step 1

This action hands the call to the Deepgram Voice Agent.

---

## Step 3: Configure your AI agent

In the Audio Connector's **Session Variables**, add a variable:

* **Name:** `config`
* **Value:** a JSON string containing your agent configuration

For optimal audio quality, include the following in your agent configuration:

```json
"audio": {
  "input": {
    "encoding": "mulaw",
    "sample_rate": 8000
  },
  "output": {
    "encoding": "mulaw",
    "sample_rate": 8000,
    "container": "none"
  }
}
```

To allow the Voice Agent to end the call, add an `end_conversation` function to the agent configuration. The function's properties are sent back to Genesys and can be mapped as session output variables.

### Example end conversation function

```json
{
  "name": "end_conversation",
  "description": "Call this function when the user says goodbye or the conversation ends.",
  "parameters": {
    "type": "object",
    "properties": {
      "needs_escalation": {
        "type": "boolean",
        "description": "Set to true if the user requests a human or manager."
      }
    }
  }
}
```

---

## Step 4: Set up middleware server (self-hosted only)

If you use a self-hosted setup, deploy a middleware server to connect Genesys with the Deepgram Voice Agent. Contact your Deepgram account executive for access and setup instructions.

---

## Customization options

You can adjust your agent's behavior using these configuration fields:

| Setting               | Field                  |
| --------------------- | ---------------------- |
| Personality           | `think.prompt`         |
| Voice                 | `speak.provider.model` |
| Greeting              | `greeting`             |
| Knowledge / abilities | `think.functions`      |

---

## Additional resources

* [Deepgram Voice Agent documentation](/docs/voice-agent)
* [Genesys and Deepgram STT integration](/docs/genesys-deepgram)
