---
title: "Quickstart: Next.js"
source: https://docs.together.ai/docs/nextjs-chat-quickstart
path: docs/nextjs-chat-quickstart
---

Build an app that can ask a single question or chat with an LLM using Next.js and Together AI.

In this guide you'll learn how to use Together AI and Next.js to build two common AI features:

* Ask a question and get a response
* Have a long-running chat with a bot

We'll first build these features using the Together AI SDK directly, then show how to build a chat app using popular frameworks like Vercel AI SDK and Mastra.

[Here's the live demo](https://together-nextjs-chat.vercel.app/), and [here's the source on GitHub](https://github.com/samselikoff/together-nextjs-chat).

Let's get started!

## Installation

After [creating a new Next.js app](https://nextjs.org/docs/app/getting-started/installation), install the [Together AI TypeScript SDK](https://www.npmjs.com/package/together-ai):

```
npm i together-ai
```

## Ask a single question

To ask a question with Together AI, we'll need an API route, and a page with a form that lets the user submit their question.

**1. Create the API route**

Make a new POST route that takes in a `question` and returns a chat completion as a stream:

```js TypeScript theme={null}
// app/api/answer/route.ts
import Together from "together-ai";

const together = new Together();

export async function POST(request: Request) {
  const { question } = await request.json();

  const res = await together.chat.completions.create({
    model: "Qwen/Qwen3.5-9B",
    reasoning: { enabled: false },
    messages: [{ role: "user", content: question }],
    stream: true,
  });

  return new Response(res.toReadableStream());
}
```

**2. Create the page**

Add a form that sends a POST request to your new API route, and use the `ChatCompletionStream` helper to read the stream and update some React state to display the answer:

```js TypeScript theme={null}
// app/page.tsx
"use client";

import { FormEvent, useState } from "react";
import { ChatCompletionStream } from "together-ai/lib/ChatCompletionStream";

export default function Chat() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  async function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();

    setIsLoading(true);
    setAnswer("");

    const res = await fetch("/api/answer", {
      method: "POST",
      body: JSON.stringify({ question }),
    });

    if (!res.body) return;

    ChatCompletionStream.fromReadableStream(res.body)
      .on("content", (delta) => setAnswer((text) => text + delta))
      .on("end", () => setIsLoading(false));
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask me a question"
          required
        />

        <button disabled={isLoading} type="submit">
          Submit
        </button>
      </form>

      <p>{answer}</p>
    </div>
  );
}
```

That's it! Submitting the form will update the page with the LLM's response. You can now use the `isLoading` state to add additional styling, or a Reset button if you want to reset the page.

## Have a long-running chat

To build a chatbot with Together AI, we'll need an API route that accepts an array of messages, and a page with a form that lets the user submit new messages. The page will also need to store the entire history of messages between the user and the AI assistant.

**1. Create an API route**

Make a new POST route that takes in a `messages` array and returns a chat completion as a stream:

```js TypeScript theme={null}
// app/api/chat/route.ts
import Together from "together-ai";

const together = new Together();

export async function POST(request: Request) {
  const { messages } = await request.json();

  const res = await together.chat.completions.create({
    model: "Qwen/Qwen3.5-9B",
    reasoning: { enabled: false },
    messages,
    stream: true,
  });

  return new Response(res.toReadableStream());
}
```

**2. Create a page**

Create a form to submit a new message, and some React state to store the `messages` for the session. In the form's submit handler, send over the new array of messages, and use the `ChatCompletionStream` helper to read the stream and update the last message with the LLM's response.

```js TypeScript theme={null}
// app/page.tsx
"use client";

import { FormEvent, useState } from "react";
import type { ChatCompletionMessageParam } from "together-ai/resources/chat/completions";
import { ChatCompletionStream } from "together-ai/lib/ChatCompletionStream";

export default function Chat() {
  const [prompt, setPrompt] = useState("");
  const [messages, setMessages] = useState<ChatCompletionMessageParam[]>([]);
  const [isPending, setIsPending] = useState(false);

  async function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();

    setPrompt("");
    setIsPending(true);
    setMessages((messages) => [...messages, { role: "user", content: prompt }]);

    const res = await fetch("/api/chat", {
      method: "POST",
      body: JSON.stringify({
        messages: [...messages, { role: "user", content: prompt }],
      }),
    });

    if (!res.body) return;

    ChatCompletionStream.fromReadableStream(res.body)
      .on("content", (delta, content) => {
        setMessages((messages) => {
          const lastMessage = messages.at(-1);

          if (lastMessage?.role !== "assistant") {
            return [...messages, { role: "assistant", content }];
          } else {
            return [...messages.slice(0, -1), { ...lastMessage, content }];
          }
        });
      })
      .on("end", () => {
        setIsPending(false);
      });
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <fieldset>
          <input
            placeholder="Send a message"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
          />
          <button type="submit" disabled={isPending}>
            Submit
          </button>
        </fieldset>
      </form>

      {messages.map((message, i) => (
        <p key={i}>
          {message.role}: {message.content}
        </p>
      ))}
    </div>
  );
}
```

You've just built a simple chatbot with Together AI!

***

## Using Vercel AI SDK

The Vercel AI SDK provides React hooks that simplify streaming and state management. Install it with:

```bash theme={null}
npm i ai @ai-sdk/togetherai
```

The API route uses `streamText` instead of the Together SDK directly:

```js TypeScript theme={null}
// app/api/chat/route.ts
import { streamText, convertToModelMessages } from "ai";
import { createTogetherAI } from "@ai-sdk/togetherai";

const togetherAI = createTogetherAI({
  apiKey: process.env.TOGETHER_API_KEY,
});

export async function POST(req: Request) {
  const { messages } = await req.json();

  const result = streamText({
    model: togetherAI("Qwen/Qwen3.5-9B"),
    messages: convertToModelMessages(messages),
  });

  return result.toUIMessageStreamResponse();
}
```

The page uses the `useChat` hook which handles all message state and streaming automatically:

```js TypeScript theme={null}
// app/page.tsx
"use client";

import { useChat } from "@ai-sdk/react";
import { useState } from "react";

export default function Chat() {
  const [input, setInput] = useState("");
  const { messages, sendMessage } = useChat();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (input.trim()) {
      sendMessage({
        role: "user",
        parts: [{ type: "text", text: input }],
      });
      setInput("");
    }
  };

  return (
    <div>
      {messages.map((message) => (
        <div key={message.id}>
          <strong>{message.role}:</strong>
          {message.parts.map((part, i) =>
            part.type === "text" ? <span key={i}> {part.text}</span> : null
          )}
        </div>
      ))}

      <form onSubmit={handleSubmit}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Send a message"
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}
```

***

## Using Mastra

Mastra is an AI framework that provides built-in integrations and abstractions for building AI applications. Install it with:

```bash theme={null}
npm i @mastra/core
```

The API route uses Mastra's Together AI integration:

```js TypeScript theme={null}
// app/api/chat/route.ts
import { Agent } from "@mastra/core/agent";
import { NextRequest } from "next/server";

const agent = new Agent({
  name: "my-agent",
  instructions: "You are a helpful assistant",
  model: "togetherai/meta-llama/Llama-3.3-70B-Instruct-Turbo"
});

export async function POST(request: NextRequest) {
  const { messages } = await request.json();

  const conversationHistory = messages
    .map((msg: { role: string; content: string }) => `${msg.role}: ${msg.content}`)
    .join('\n');

  const streamResponse = await agent.stream(conversationHistory);
  
  const encoder = new TextEncoder();
  const readableStream = new ReadableStream({
    async start(controller) {
      for await (const chunk of streamResponse.textStream) {
        controller.enqueue(encoder.encode(`data: ${JSON.stringify(chunk)}\n\n`));
      }
      controller.close();
    },
  });

  return new Response(readableStream, {
    headers: {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
    },
  });
}
```

The page uses Mastra's chat hooks to manage conversation state:

```js TypeScript theme={null}
// app/page.tsx
"use client";

import { useState } from "react";

export default function Chat() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<Array<{ role: string; content: string }>>([]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    const newMessages = [...messages, { role: "user", content: input }];
    setMessages([...newMessages, { role: "assistant", content: "" }]);
    setInput("");

    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages: newMessages }),
    });

    const reader = res.body?.getReader();
    const decoder = new TextDecoder();
    let assistantMessage = "";

    if (reader) {
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const lines = decoder.decode(value).split("\n");
        for (const line of lines) {
          if (line.startsWith("data: ")) {
            const chunk = JSON.parse(line.slice(6));
            assistantMessage += typeof chunk === "string" ? chunk : "";
            setMessages((prev) => [
              ...prev.slice(0, -1),
              { role: "assistant", content: assistantMessage }
            ]);
          }
        }
      }
    }
  };

  return (
    <div>
      {messages.map((m, i) => (
        <div key={i}>
          <strong>{m.role}:</strong> {m.content}
        </div>
      ))}
      <form onSubmit={handleSubmit}>
        <input value={input} onChange={(e) => setInput(e.target.value)} placeholder="Send a message" />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}
```

***
