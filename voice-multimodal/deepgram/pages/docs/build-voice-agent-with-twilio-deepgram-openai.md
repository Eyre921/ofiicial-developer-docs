---
title: "Build a Voice Agent with Twilio & OpenAI & Deepgram"
source: https://developers.deepgram.com/docs/build-voice-agent-with-twilio-deepgram-openai.md
path: docs/build-voice-agent-with-twilio-deepgram-openai
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Build a Voice Agent with Twilio & OpenAI & Deepgram

Twilio handles the phone call. Deepgram handles speech-to-text and text-to-speech. OpenAI handles the LLM. Together they form a streaming voice agent that answers an inbound call, listens, thinks, and talks back. This guide walks through the working sample server end to end.

## Before you begin

This guide assumes basic JavaScript and Node.js knowledge and familiarity with [OpenAI](https://openai.com/), [Twilio](https://www.twilio.com/), and [Ngrok](https://ngrok.com/).

The full sample lives in the [deepgram-twilio-streaming-voice-agent](https://github.com/deepgram/deepgram-twilio-streaming-voice-agent) repository.

### Get a Deepgram API key

[Create a Deepgram account](https://console.deepgram.com/signup?jump=keys) first. Signup is free and includes **\$200** in free credit.

[Create a Deepgram API key](https://console.deepgram.com/signup?jump=keys) and keep it handy. You will export it as an environment variable later.

### Get Twilio credentials

This demo uses Twilio Voice to start a phone call that the server records and transcribes. [Sign up for a Twilio account](https://twilio.com), then grab the Account SID and Auth Token from your [Twilio Admin Dashboard](https://console.twilio.com/).

### Get OpenAI credentials

The agent uses OpenAI for the LLM. [Sign up for an OpenAI account](https://platform.openai.com/signup/) and create an API key.

## What you will build

A Node.js server that wires together six streaming components:

* a callable Twilio phone number
* Twilio inbound media stream (caller audio)
* Deepgram streaming speech-to-text
* Streaming OpenAI LLM
* Deepgram streaming text-to-speech
* Twilio outbound media stream (agent audio)

The implementation is a working reference, not a production deployment. Use it as a starting point for your own application logic.

## Clone the repository

```shell
git clone https://github.com/deepgram/deepgram-twilio-streaming-voice-agent.git
cd deepgram-twilio-streaming-voice-agent
```

## Set up the server

Read the [`server.js`](https://github.com/deepgram/deepgram-twilio-streaming-voice-agent/blob/main/server.js) file in the repository to see the full server-side implementation.

### Set environment variables

Export your API keys so the server can authenticate with OpenAI and Deepgram:

```shell
export OPENAI_API_KEY=xxx
export DEEPGRAM_API_KEY=xxx
```

Verify they are set:

```shell
echo $OPENAI_API_KEY
echo $DEEPGRAM_API_KEY
```

### Install and run

Requires Node v12.1.0 or later.

```shell
npm install
npm run start
```

## Set up the demo

### Install ngrok

ngrok exposes your local server so Twilio can reach it.

* macOS: `brew install ngrok/ngrok/ngrok`
* Windows or Linux: follow the [ngrok install instructions](https://ngrok.com/docs/getting-started/)

[Sign up for an ngrok account](https://dashboard.ngrok.com/get-started/setup/macos), copy your authtoken from the [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken), and connect the agent:

```shell
ngrok config add-authtoken <TOKEN>
```

### Buy a Twilio phone number

Use the [Twilio CLI](https://www.twilio.com/docs/twilio-cli/quickstart) or the [Twilio Admin Dashboard](https://help.twilio.com/articles/223135247-How-to-Search-for-and-Buy-a-Twilio-Phone-Number-from-Console). The CLI version:

```shell
twilio api:core:available-phone-numbers:local:list \
  --country-code="US" --voice-enabled --properties="phoneNumber"
```

Then purchase a number (replace `+123456789` with one from the list above):

```shell
twilio api:core:incoming-phone-numbers:create --phone-number="+123456789"
```

### Point Twilio at your ngrok URL

Start ngrok in a separate terminal from the one running the server:

```shell
ngrok http 8080
```

ngrok prints a forwarding URL on the `Forwarding` row. Copy it.

Edit [`templates/streams.xml`](https://github.com/deepgram/deepgram-twilio-streaming-voice-agent/blob/main/templates/streams.xml) and replace `<ngrok url>` with your ngrok host. Use `wss://` and include `/streams`. For example: `wss://yourdomain.ngrok-free.app/streams`.

In your Twilio dashboard, open the active phone number. Under the **Configure** tab, set "A call comes in" to your TwiML URL: `https://yourdomain.ngrok-free.app/twiml`.

Restarting ngrok generates a new URL. Update the Twilio webhook every time.

### Make the call

Dial the Twilio number from any phone, or trigger an outbound call from the CLI (replace `+123456789` with your Twilio number, `+19876543210` with the phone you want to call, and `abcdef.ngrok.io` with your ngrok host):

```shell
twilio api:core:calls:create \
  --from="+123456789" \
  --to="+19876543210" \
  --url="https://abcdef.ngrok.io/twiml"
```
