---
title: "Build a Voice Agent with JavaScript"
source: https://developers.deepgram.com/docs/build-a-voice-agent-javascript.md
path: docs/build-a-voice-agent-javascript
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Build a Voice Agent with JavaScript

This tutorial walks you through building a basic voice agent using JavaScript and the Deepgram SDK. You will learn how to connect to the Agent API, configure its behavior, and stream audio for processing.

## Prerequisites

Before you begin, ensure you have the following:

* A Deepgram API key. You can get one in the [Deepgram Console](https://console.deepgram.com/).
* Node.js installed on your machine.

## 1. Set up your environment

Create a new directory for your project and initialize it.

```shell
mkdir deepgram-agent-demo
cd deepgram-agent-demo
npm init -y
touch index.js
```

Export your Deepgram API key as an environment variable.

```shell
export DEEPGRAM_API_KEY="your_api_key"
```

## 2. Install the Deepgram SDK

Install the Deepgram JavaScript SDK and `cross-fetch` for audio streaming.

```shell
npm install @deepgram/sdk cross-fetch
```

## 3. Create the Voice Agent

Open `index.js` and add the following code. This script connects to Deepgram, configures the agent, and streams a sample audio file.

```javascript
const { writeFile, appendFile } = require("fs/promises");
const { DeepgramClient } = require("@deepgram/sdk");
const fetch = require("cross-fetch");
const { join } = require("path");

const deepgram = new DeepgramClient({ apiKey: process.env.DEEPGRAM_API_KEY });

const agent = async () => {
  let audioBuffer = Buffer.alloc(0);
  let i = 0;
  const url = "https://dpgr.am/spacewalk.wav";
  const connection = await deepgram.agent.v1.connect();

  connection.on("message", async (data) => {
    if (data.type === "Welcome") {
      console.log("Welcome to the Deepgram Voice Agent!");

      connection.sendSettings({
        type: "Settings",
        audio: {
          input: {
            encoding: "linear16",
            sample_rate: 24000,
          },
          output: {
            encoding: "linear16",
            sample_rate: 16000,
            container: "wav",
          },
        },
        agent: {
          language: "en",
          listen: {
            provider: {
              type: "deepgram",
              model: "nova-3",
            },
          },
          think: {
            provider: {
              type: "open_ai",
              model: "gpt-4o-mini",
            },
            prompt: "You are a friendly AI assistant.",
          },
          speak: {
            provider: {
              type: "deepgram",
              model: "aura-2-thalia-en",
            },
          },
          greeting: "Hello! How can I help you today?",
        },
      });

      console.log("Deepgram agent configured!");

      setInterval(() => {
        console.log("Keep alive!");
        connection.sendKeepAlive({ type: "KeepAlive" });
      }, 5000);

      fetch(url)
        .then((r) => r.body)
        .then((res) => {
          res.on("readable", () => {
            const chunk = res.read();
            if (chunk) {
              console.log("Sending audio chunk");
              connection.sendMedia(chunk);
            }
          });
        });
    } else if (data.type === "ConversationText") {
      await appendFile(join(__dirname, `chatlog.txt`), JSON.stringify(data) + "\n");
    } else if (data.type === "UserStartedSpeaking") {
      if (audioBuffer.length) {
        console.log("Interrupting agent.");
        audioBuffer = Buffer.alloc(0);
      }
    } else if (typeof Blob !== "undefined" && data instanceof Blob) {
      console.log("Audio chunk received");
      const chunk = Buffer.from(await data.arrayBuffer());
      audioBuffer = Buffer.concat([audioBuffer, chunk]);
    } else if (data.type === "AgentAudioDone") {
      console.log("Agent audio done");
      await writeFile(join(__dirname, `output-${i}.wav`), audioBuffer);
      audioBuffer = Buffer.alloc(0);
      i++;
    }
  });

  connection.on("open", () => {
    console.log("Connection opened");
  });

  connection.on("close", () => {
    console.log("Connection closed");
    process.exit(0);
  });

  connection.on("error", (err) => {
    console.error("Error:", err.message);
  });

  connection.connect();
  await connection.waitForOpen();
};

void agent();
```

## 4. Run the Voice Agent

Run your script using Node.js.

```shell
node index.js
```

The agent will process the audio and generate responses. You can find the conversation transcript in `chatlog.txt` and the agent's audio responses in `output-*.wav` files.

## Next steps

Now that you have built a basic agent, you can customize its behavior:

* [Configure the Voice Agent](/docs/configure-voice-agent): Explore all available settings for models and voices.
* [Build a Voice Agent](/docs/build-a-voice-agent): Return to the overview to see other language options.
