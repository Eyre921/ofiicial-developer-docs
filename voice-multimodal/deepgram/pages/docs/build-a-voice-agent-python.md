---
title: "Build a Voice Agent with Python"
source: https://developers.deepgram.com/docs/build-a-voice-agent-python.md
path: docs/build-a-voice-agent-python
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Build a Voice Agent with Python

This tutorial walks you through building a basic voice agent using Python and the Deepgram SDK. You will learn how to connect to the Agent API, configure its behavior, and stream audio for processing.

## Prerequisites

Before you begin, ensure you have the following:

* A Deepgram API key. You can get one in the [Deepgram Console](https://console.deepgram.com/).
* Python installed on your machine.

## 1. Set up your environment

Create a new directory for your project and a file for your code.

```shell
mkdir deepgram-agent-demo
cd deepgram-agent-demo
touch main.py
```

Export your Deepgram API key as an environment variable.

```shell
export DEEPGRAM_API_KEY="your_api_key"
```

## 2. Install the Deepgram SDK

Install the Deepgram Python SDK and the `requests` library for audio streaming.

```shell
pip install deepgram-sdk requests
```

## 3. Create the Voice Agent

Open `main.py` and add the following code. This script connects to Deepgram, configures the agent with specific models, and streams a sample audio file.

```python
import requests
import time
import os
import json
import threading

from deepgram import DeepgramClient
from deepgram.core.events import EventType
from deepgram.agent.v1.types import (
    AgentV1Settings,
    AgentV1SettingsAgent,
    AgentV1SettingsAudio,
    AgentV1SettingsAudioInput,
    AgentV1SettingsAudioOutput,
    AgentV1SettingsAgentListen,
    AgentV1SettingsAgentListenProvider_V1,
)
from deepgram.types.think_settings_v1 import ThinkSettingsV1
from deepgram.types.think_settings_v1provider import ThinkSettingsV1Provider_OpenAi
from deepgram.types.speak_settings_v1 import SpeakSettingsV1
from deepgram.types.speak_settings_v1provider import SpeakSettingsV1Provider_Deepgram

def main():
    try:
        api_key = os.getenv("DEEPGRAM_API_KEY")
        if not api_key:
            raise ValueError("DEEPGRAM_API_KEY environment variable is not set")
        
        client = DeepgramClient(api_key=api_key)

        with client.agent.v1.connect() as connection:
            print("Created WebSocket connection...")

            settings = AgentV1Settings(
                audio=AgentV1SettingsAudio(
                    input=AgentV1SettingsAudioInput(
                        encoding="linear16",
                        sample_rate=24000,
                    ),
                    output=AgentV1SettingsAudioOutput(
                        encoding="linear16",
                        sample_rate=24000,
                        container="wav",
                    ),
                ),
                agent=AgentV1SettingsAgent(
                    language="en",
                    listen=AgentV1SettingsAgentListen(
                        provider=AgentV1SettingsAgentListenProvider_V1(
                            type="deepgram",
                            model="nova-3",
                        )
                    ),
                    think=ThinkSettingsV1(
                        provider=ThinkSettingsV1Provider_OpenAi(
                            type="open_ai",
                            model="gpt-4o-mini",
                        ),
                        prompt="You are a friendly AI assistant.",
                    ),
                    speak=SpeakSettingsV1(
                        provider=SpeakSettingsV1Provider_Deepgram(
                            type="deepgram",
                            model="aura-2-thalia-en",
                        )
                    ),
                    greeting="Hello! How can I help you today?",
                ),
            )

            audio_buffer = bytearray()
            file_counter = 0
            processing_complete = False

            def on_message(message):
                nonlocal audio_buffer, file_counter, processing_complete

                if isinstance(message, bytes):
                    audio_buffer.extend(message)
                    return

                msg_type = getattr(message, "type", "Unknown")
                
                if msg_type == "ConversationText":
                    print(f"Conversation: {message}")
                    with open("chatlog.txt", 'a') as chatlog:
                        chatlog.write(f"{json.dumps(message.__dict__)}\n")

                elif msg_type == "AgentAudioDone":
                    print("Agent audio done")
                    if len(audio_buffer) > 0:
                        with open(f"output-{file_counter}.wav", 'wb') as f:
                            f.write(create_wav_header())
                            f.write(audio_buffer)
                        print(f"Created output-{file_counter}.wav")
                    audio_buffer = bytearray()
                    file_counter += 1
                    processing_complete = True

            connection.on(EventType.MESSAGE, on_message)
            connection.send_settings(settings)

            listener_thread = threading.Thread(target=connection.start_listening, daemon=True)
            listener_thread.start()

            time.sleep(1)

            print("Streaming audio...")
            response = requests.get("https://dpgr.am/spacewalk.wav", stream=True)
            header = response.raw.read(44)

            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    connection.send_media(chunk)
                    time.sleep(0.1)

            print("Waiting for agent response...")
            start_time = time.time()
            while not processing_complete and (time.time() - start_time) < 30:
                time.sleep(1)

            print("Finished")

    except Exception as e:
        print(f"Error: {str(e)}")

def create_wav_header(sample_rate=24000, bits_per_sample=16, channels=1):
    byte_rate = sample_rate * channels * (bits_per_sample // 8)
    block_align = channels * (bits_per_sample // 8)
    header = bytearray(44)
    header[0:4] = b'RIFF'
    header[4:8] = b'\x00\x00\x00\x00'
    header[8:12] = b'WAVE'
    header[12:16] = b'fmt '
    header[16:20] = b'\x10\x00\x00\x00'
    header[20:22] = b'\x01\x00'
    header[22:24] = channels.to_bytes(2, 'little')
    header[24:28] = sample_rate.to_bytes(4, 'little')
    header[28:32] = byte_rate.to_bytes(4, 'little')
    header[32:34] = block_align.to_bytes(2, 'little')
    header[34:36] = bits_per_sample.to_bytes(2, 'little')
    header[36:40] = b'data'
    header[40:44] = b'\x00\x00\x00\x00'
    return header

if __name__ == "__main__":
    main()
```

## 4. Run the Voice Agent

Run your script using Python.

```shell
python main.py
```

The agent will process the audio and generate responses. You can find the conversation transcript in `chatlog.txt` and the agent's audio responses in `output-*.wav` files.

## Next steps

Now that you have built a basic agent, you can customize its behavior:

* [Configure the Voice Agent](/docs/configure-voice-agent): Explore all available settings for models and voices.
* [Build a Voice Agent](/docs/build-a-voice-agent): Return to the overview to see other language options.
