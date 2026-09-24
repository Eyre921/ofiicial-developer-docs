---
title: "Text Chunking for TTS"
source: https://developers.deepgram.com/docs/tts-text-chunking.md
path: docs/tts-text-chunking
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Text Chunking for TTS

## Why Text Chunking Matters

Text chunking significantly reduces perceived latency in TTS applications by allowing audio playback to begin sooner. This is especially important for conversational AI and voice agents where responsiveness is critical.

> **Info**
>
> **Using Flux TTS (`/v2/speak`)?** This guidance applies to Aura (`/v1/speak`). On Flux TTS, the server places flush boundaries internally — stream text in as it's produced and don't chunk client-side. See [Getting Started with Flux TTS](/docs/flux-tts/quickstart).

Instead of waiting for the entire audio to be generated, chunking lets you:

* Begin audio playback much faster
* Create more responsive voice experiences
* Maintain natural-sounding speech

## Basic Sentence Chunking

The simplest and most effective approach is to split text at sentence boundaries. This preserves natural speech patterns while enabling faster time-to-first-byte:

```python
# For more Python SDK migration guides, visit:
# https://github.com/deepgram/deepgram-python-sdk/tree/main/docs

import re

def chunk_by_sentence(text):
    # Split text at sentence boundaries (periods, question marks, exclamation points)
    # while preserving the punctuation
    sentences = re.split(r'(?<=[.!?])\s+', text)

    # Remove any empty chunks
    return [sentence for sentence in sentences if sentence]

# Example usage
text = "Hello, welcome to Deepgram. This is an example of text chunking. How does it sound?"
chunks = chunk_by_sentence(text)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")

# Output:
# Chunk 1: Hello, welcome to Deepgram.
# Chunk 2: This is an example of text chunking.
# Chunk 3: How does it sound?
```

**`Node.Js`**

```javascript Node.Js
function chunkBySentence(text) {
  // Split text at sentence boundaries (periods, question marks, exclamation points)
  // while preserving the punctuation
  const sentences = text.split(/(?<=[.!?])\s+/);

  // Remove any empty chunks
  return sentences.filter(sentence => sentence);
}

// Example usage
const text = "Hello, welcome to Deepgram. This is an example of text chunking. How does it sound?";
const chunks = chunkBySentence(text);

chunks.forEach((chunk, index) => {
  console.log(`Chunk ${index + 1}: ${chunk}`);
});

// Output:
// Chunk 1: Hello, welcome to Deepgram.
// Chunk 2: This is an example of text chunking.
// Chunk 3: How does it sound?
```

## Processing Streaming Text with REST TTS

When working with streaming text from an LLM, collect tokens until you have complete sentences. This example sends each sentence to REST TTS and saves its completed MP3 response.

```python
# For more Python SDK migration guides, visit:
# https://github.com/deepgram/deepgram-python-sdk/tree/main/docs

import re
import asyncio
from deepgram import AsyncDeepgramClient

class SimpleTextChunker:
    def __init__(self, deepgram_client):
        self.queue = []  # Queue to store incoming paragraph chunks
        self.deepgram_client = deepgram_client
        self.chunk_number = 0
        self.pending_text = ""

    async def synthesize_and_save(self, text):
        audio_response = self.deepgram_client.speak.v1.audio.generate(
            text=text,
            model="aura-2-thalia-en"
        )
        audio_data = b"".join([chunk async for chunk in audio_response])
        self.chunk_number += 1
        filename = f"chunk_{self.chunk_number}.mp3"
        with open(filename, "wb") as audio_file:
            audio_file.write(audio_data)
        print(f"Audio saved to {filename}")

    async def process_text_stream(self, paragraph):
        """Process an array of paragraph chunks, each containing 1-2 sentences"""

        # Queue paragraph as it arrives (simulating fast reception)
        self.queue.append(paragraph)
        print(f"Received and queued paragraph: {paragraph}")

        # You could preprocess paragraphs here and split them by more than just sentence boundaries

        # Process the queue
        while self.queue:
            # Get the next paragraph from the queue
            paragraph = self.queue.pop(0)

            self.pending_text += paragraph
            matches = list(re.finditer(r'[^.!?]+[.!?]', self.pending_text))
            if not matches:
                continue

            self.pending_text = self.pending_text[matches[-1].end():].lstrip()

            # Process each sentence
            for match in matches:
                sentence = match.group().strip()
                # Send the sentence to TTS
                print(f"Sending sentence to TTS: {sentence}")
                await self.synthesize_and_save(sentence)

    async def flush(self):
        if self.pending_text.strip():
            await self.synthesize_and_save(self.pending_text.strip())
            self.pending_text = ""

# Example usage with an array of paragraph chunks
async def main():
    # This simulates text coming in as paragraph chunks from an LLM
    paragraph_chunks = [
        "Hello",
        " world. Deepgram's TTS API offers low latency.",
        "It works great for voice agents.",
        "This approach simulates receiving chunks as paragraphs. Each paragraph may contain one or two sentences.",
        "Try it today! You'll be impressed with the results."
    ]

    # Set up TTS client
    deepgram = AsyncDeepgramClient()

    chunker = SimpleTextChunker(deepgram)
    # Process each paragraph sequentially
    for paragraph in paragraph_chunks:
        await chunker.process_text_stream(paragraph)
    await chunker.flush()

# Run the example
if __name__ == "__main__":
    asyncio.run(main())
```

**`Node.Js`**

```javascript Node.Js
const fs = require("fs");
const { Readable } = require("stream");
const { pipeline } = require("stream/promises");

class SimpleTextChunker {
  constructor(deepgram) {
    this.queue = []; // Queue to store incoming paragraph chunks
    this.deepgram = deepgram;
    this.chunkNumber = 0;
    this.pendingText = "";
  }

  async synthesizeAndSave(text) {
    const audioResponse = await this.deepgram.speak.v1.audio.generate({
      text,
      model: "aura-2-thalia-en",
    });

    this.chunkNumber += 1;
    const filename = `chunk-${this.chunkNumber}.mp3`;
    await pipeline(
      Readable.fromWeb(audioResponse.stream()),
      fs.createWriteStream(filename)
    );
    console.log(`Audio saved to ${filename}`);
  }

  async processTextStream(paragraph) {
    // Queue paragraph as it arrives
    this.queue.push(paragraph);
    console.log(`Received and queued paragraph: ${paragraph}`);

    // Process the queue
    while (this.queue.length > 0) {
      // Get the next paragraph from the queue
      const paragraph = this.queue.shift();

      this.pendingText += paragraph;
      const matches = [...this.pendingText.matchAll(/[^.!?]+[.!?]/g)];
      if (matches.length === 0) continue;

      const lastMatch = matches[matches.length - 1];
      this.pendingText = this.pendingText
        .slice(lastMatch.index + lastMatch[0].length)
        .trimStart();

      // Process each sentence sequentially
      for (const match of matches) {
        const sentence = match[0].trim();
        // Send the sentence to TTS
        console.log(`Sending sentence to TTS: ${sentence}`);

        try {
          await this.synthesizeAndSave(sentence);
        } catch (error) {
          console.error('Error generating speech:', error);
        }
      }
    }
  }

  async flush() {
    if (this.pendingText.trim()) {
      await this.synthesizeAndSave(this.pendingText.trim());
      this.pendingText = "";
    }
  }
}

// Example usage with an array of paragraph chunks
async function main() {
  const { DeepgramClient } = require('@deepgram/sdk');

  // This simulates text coming in as paragraph chunks from an LLM
  const paragraphChunks = [
    "Hello",
    " world. Deepgram's TTS API offers low latency.",
    "It works great for voice agents.",
    "This approach simulates receiving chunks as paragraphs. Each paragraph may contain one or two sentences.",
    "Try it today! You'll be impressed with the results."
  ];

  const deepgram = new DeepgramClient({ apiKey: process.env.DEEPGRAM_API_KEY });
  const chunker = new SimpleTextChunker(deepgram);

  // Process each paragraph sequentially
  for (const paragraph of paragraphChunks) {
    await chunker.processTextStream(paragraph);
  }
  await chunker.flush();
}

// Run the example
main().catch(console.error);
```

For low-latency playback over a persistent connection, see [Real-Time TTS with WebSockets](/docs/tts-websocket-streaming).

## Processing Chunked Text

After creating chunks, you have two main options for processing them:

### Sequential Processing

Process each chunk in sequence, prioritizing the first chunk:

```python
# For more Python SDK migration guides, visit:
# https://github.com/deepgram/deepgram-python-sdk/tree/main/docs

async def process_chunks_sequential(chunks, tts_function):
    results = []
    for i, chunk in enumerate(chunks):
        # You might prioritize the first chunk for faster response
        result = await tts_function(chunk)
        results.append(result)
    return results
```

**`Node.Js`**

```javascript Node.Js
async function processChunksSequential(chunks, ttsFunction) {
  const results = [];
  for (let i = 0; i < chunks.length; i++) {
    const chunk = chunks[i];
    // You might prioritize the first chunk for faster response
    const result = await ttsFunction(chunk);
    results.push(result);
  }
  return results;
}
```

### Setting Chunk Size

For most applications, sentences work well as chunks. If you need finer control:

* **Voice assistants**: Aim for 50-100 character chunks
* **Call center bots**: Use complete sentences (most natural)
* **Long-form content**: Larger chunks (200-400 characters) preserve intonation

## Other Chunking Strategies

If you need more advanced chunking methods, search for these techniques:

* **Clause-based chunking**: Splits long sentences at commas and semicolons
* **NLP-based chunking**: Uses natural language processing to find semantic boundaries
* **Adaptive chunking**: Adjusts chunk size based on content complexity
* **First-chunk optimization**: Specially optimizes the first chunk for minimal latency
* **SSML chunking**: Handles Speech Synthesis Markup Language tags when chunking

> **Info**
>
> For WebSocket implementation details to stream the chunked audio, see our guide on [Real-Time TTS with WebSockets](/docs/tts-websocket-streaming).
