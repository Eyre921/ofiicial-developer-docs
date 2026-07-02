---
title: "Build an AI search engine"
source: https://docs.together.ai/docs/ai-search-engine
path: docs/ai-search-engine
---

Build an open source AI search engine inspired by Perplexity with Next.js and Together AI.

[TurboSeek](https://www.turboseek.io/) is an app that answers questions using [Together AI’s](https://www.together.ai/) open-source LLMs. It pulls multiple sources from the web using Exa's API, then summarizes them to present a single answer to the user.

<Frame>
  <img alt="" />
</Frame>

In this post, you’ll learn how to build the core parts of TurboSeek. The app is [open-source](https://github.com/Nutlope/turboseek/) and built with Next.js and Tailwind, but Together’s API can be used with any language or framework.

## Building the input prompt

TurboSeek’s core interaction is a text field where the user can enter a question:

<Frame>
  <img alt="" />
</Frame>

In our page, we’ll render an `<input>` and control it using some new React state:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  let [question, setQuestion] = useState('');

  return (
    <form>
      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask anything"
      />
    </form>
  );
}
```

When the user submits our form, we need to do two things:

1. Use the Exa API to fetch sources from the web, and
2. Pass the text from the sources to an LLM to summarize and generate an answer

Let’s start by fetching the sources. We’ll wire up a submit handler to our form that makes a POST request to a new endpoint, `/getSources`:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  let [question, setQuestion] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();

    let response = await fetch("/api/getSources", {
      method: "POST",
      body: JSON.stringify({ question }),
    });

    let sources = await response.json();

    // This fetch() will 404 for now
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask anything"
      />
    </form>
  );
}
```

If we submit the form, we see our React app makes a request to `/getSources`:

<Frame>
  <img alt="" />
</Frame>

Our frontend is ready! Let’s add an API route to get the sources.

## Getting web sources with Exa

To create our API route, we’ll make a new `app/api/getSources/route.js` file:

```jsx JSX theme={null}
// app/api/getSources/route.js
export async function POST(req) {
  let json = await req.json();

  // `json.question` has the user's question
}
```

We’re ready to send our question to Exa API to return back nine sources from the web.

The [Exa API SDK](https://exa.ai/) lets you make a fetch request to get back search results including content, so we’ll use it to build up our list of sources:

```jsx JSX theme={null}
// app/api/getSources/route.js
import Exa from "exa-js";
import { NextResponse } from "next/server";

const exaClient = new Exa(process.env.EXA_API_KEY);

export async function POST(req) {
  const json = await req.json();

    const response = await exaClient.searchAndContents(json.question, {
      numResults: 9,
      type: "auto",
    });

  return NextResponse.json(
    response.results.map((result) => ({
      title: result.title || undefined,
      url: result.url,
      content: result.text
    })),
  );
}
```

In order to make a request to Exa API, you’ll need to get an [API key from Exa](https://exa.ai/). Once you have it, set it in `.env.local`:

```jsx JSX theme={null}
// .env.local
EXA_API_KEY=xxxxxxxxxxxx
```

and our API handler should work.

Let’s try it out from our React app! We’ll log the sources in our event handler:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  let [question, setQuestion] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();

    let response = await fetch("/api/getSources", {
      method: "POST",
      body: JSON.stringify({ question }),
    });

    let sources = await response.json();

    // log the response from our new endpoint
    console.log(sources);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask anything"
      />
    </form>
  );
}
```

and if we try submitting a question, we’ll see an array of pages logged in the console!

<Frame>
  <img alt="" />
</Frame>

Let’s create some new React state to store the responses and display them in our UI:

```jsx JSX theme={null}
function Page() {
  let [question, setQuestion] = useState("");
  let [sources, setSources] = useState([]);

  async function handleSubmit(e) {
    e.preventDefault();

    let response = await fetch("/api/getSources", {
      method: "POST",
      body: JSON.stringify({ question }),
    });

    let sources = await response.json();

    // Update the sources with our API response
    setSources(sources);
  }

  return (
    <>
      <form onSubmit={handleSubmit}>
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask anything"
        />
      </form>

      {/* Display the sources */}
      {sources.length > 0 && (
        <div>
          <p>Sources</p>
          <ul>
            {sources.map((source) => (
              <li key={source.url}>
                <a href={source.url}>{source.title}</a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </>
  );
}
```

If we try it out, our app is working great so far! We’re taking the user’s question, fetching nine relevant web sources from Exa, and displaying them in our UI.

Next, let’s work on summarizing the sources.

## Fetching the content from each source

Now that our React app has the sources, we can send them to a second endpoint where we’ll use Together to summarize them into our final answer.

Let’s add that second request to a new endpoint we’ll call `/api/getAnswer`, passing along the question and sources in the request body:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  // ...

  async function handleSubmit(e) {
    e.preventDefault();

    const response = await fetch("/api/getSources", {
      method: "POST",
      body: JSON.stringify({ question }),
    });

    const sources = await response.json();
    setSources(sources);

    // Send the question and sources to a new endpoint
    const answerResponse = await fetch("/api/getAnswer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, sources }),
    });

    // The second fetch() will 404 for now
  }

  // ...
}
```

If we submit a new question, we’ll see our React app make a second request to `/api/getAnswer`. Let’s create the second route!

Make a new `app/api/getAnswer/route.js` file:

```jsx JSX theme={null}
// app/api/getAnswer/route.js
export async function POST(req) {
  let json = await req.json();

  // `json.question` and `json.sources` has our data
}
```

## Summarizing the sources

Now that we have the text content from each source, we can pass it along with a prompt to Together to get a final answer.

Let’s install Together’s node SDK:

```jsx JSX theme={null}
npm i together-ai
```

and use it to query Llama 3.1 8B Turbo:

```jsx JSX theme={null}
import { Together } from "togetherai";

const together = new Together();

export async function POST(req) {
  const json = await req.json();

  // Since exa already gave us the content of the pages we can simply use it 
  const results = json.sources

  // Ask Together to answer the question using the results but limiting content
  // of each page to the first 10k characters to prevent overflowing context
  const systemPrompt = `
    Given a user question and some context, please write a clean, concise
    and accurate answer to the question based on the context. You will be
    given a set of related contexts to the question. Please use the
    context when crafting your answer.

    Here are the set of contexts:

    <contexts>
    ${results.map((result) => `${result.content.slice(0, 10_000)}\n\n`)}
    </contexts>
  `;
  const runner = await together.chat.completions.stream({
    model: "Qwen/Qwen3.5-9B",
    reasoning: { enabled: false },
    messages: [
      { role: "system", content: systemPrompt },
      { role: "user", content: json.question },
    ],
  });

  return new Response(runner.toReadableStream());
}
```

Now we’re ready to read it in our React app!

## Displaying the answer in the UI

Back in our page, let’s create some new React state called `answer` to store the text from our LLM:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  const [answer, setAnswer] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();

    const response = await fetch("/api/getSources", {
      method: "POST",
      body: JSON.stringify({ question }),
    });

    const sources = await response.json();
    setSources(sources);

    // Send the question and sources to a new endpoint
    const answerStream = await fetch("/api/getAnswer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, sources }),
    });
  }

  // ...
}
```

We can use the `ChatCompletionStream` helper from Together’s SDK to read the stream and update our `answer` state with each new chunk:

```jsx JSX theme={null}
// app/page.tsx
import { ChatCompletionStream } from "together-ai/lib/ChatCompletionStream";

function Page() {
  const [answer, setAnswer] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();

    const response = await fetch("/api/getSources", {
      method: "POST",
      body: JSON.stringify({ question }),
    });

    const sources = await response.json();
    setSources(sources);

    // Send the question and sources to a new endpoint
    const answerResponse = await fetch("/api/getAnswer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, sources }),
    });

    const runner = ChatCompletionStream.fromReadableStream(answerResponse.body);
    runner.on("content", (delta) => setAnswer((prev) => prev + delta));
  }

  // ...
}
```

Our new React state is ready!

Let’s update our UI to display it:

```jsx JSX theme={null}
function Page() {
  let [question, setQuestion] = useState("");
  let [sources, setSources] = useState([]);

  async function handleSubmit(e) {
    //
  }

  return (
    <>
      <form onSubmit={handleSubmit}>
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask anything"
        />
      </form>

      {/* Display the sources */}
      {sources.length > 0 && (
        <div>
          <p>Sources</p>
          <ul>
            {sources.map((source) => (
              <li key={source.url}>
                <a href={source.url}>{source.title}</a>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Display the answer */}
      {answer && <p>{answer}</p>}
    </>
  );
}
```

If we try submitting a question, we’ll see the sources come in, and once our `getAnswer` endpoint responds with the first chunk, we’ll see the answer text start streaming into our UI!

The core features of our app are working great.

## Digging deeper

We’ve built out the main flow of our app using just two endpoints: one that blocks on an API request to Exa AI, and one that returns a stream using Together’s Node SDK.

React and Next.js were a great fit for this app, giving us all the tools and flexibility we needed to make a complete full-stack web app with secure server-side logic and reactive client-side updates.

[TurboSeek](https://www.turboseek.io/) is fully open-source and has even more features like suggesting similar questions, so if you want to keep working on the code from this tutorial, be sure to check it out on GitHub:

[https://github.com/Nutlope/turboseek/](https://github.com/Nutlope/turboseek/)

And if you’re ready to add streaming LLM features like the chat completions we saw above to your own apps, [sign up for Together AI today](https://www.together.ai/), get \$5 for free to start out, and make your first query in minutes!

***
