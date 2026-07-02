---
title: "Build an interactive AI tutor with Llama 3.1"
source: https://docs.together.ai/docs/ai-tutor
path: docs/ai-tutor
---

Learn how to create LlamaTutor from scratch, an open source AI tutor with 90k users.

[LlamaTutor](https://llamatutor.together.ai/) is an app that creates an interactive tutoring session for a given topic using [Together AI’s](https://www.together.ai/) open-source LLMs.

<Frame>
  <img alt="" />
</Frame>

It pulls multiple sources from the web with the [Exa](https://exa.ai/) search API, then uses the text from the sources to kick off an interactive tutoring session with the user.

<Frame>
  <img alt="" />
</Frame>

In this post, you’ll learn how to build the core parts of LlamaTutor. The app is open-source and built with Next.js and Tailwind, but Together’s API works great with any language or framework.

## Building the input prompt and education dropdown

LlamaTutor’s core interaction is a text field where the user can enter a topic, and a dropdown that lets the user choose which education level the material should be taught at:

<Frame>
  <img alt="" />
</Frame>

In the main page component, we’ll render an `<input>` and `<select>`, and control both using some new React state:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  const [topic, setTopic] = useState('');
  const [grade, setGrade] = useState('');

  return (
    <form>
      <input
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        placeholder="Teach me about..."
      />
      <select value={grade} onChange={(e) => setGrade(e.target.value)}>
        <option>Elementary School</option>
        <option>Middle School</option>
        <option>High School</option>
        <option>College</option>
        <option>Undergrad</option>
        <option>Graduate</option>
      </select>
    </form>
  );
}
```

When the user submits our form, our submit handler ultimately needs to do three things:

1. Use the Exa API to fetch six different websites related to the topic
2. Parse the text from each website
3. Pass all the parsed text, as well as the education level, to Together AI to kick off the tutoring session

Let’s start by fetching the websites with Exa. We’ll wire up a submit handler to our form that makes a POST request to a new `/getSources` endpoint:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  const [topic, setTopic] = useState('');
  const [grade, setGrade] = useState('');

  async function handleSubmit(e) {
    e.preventDefault();

    let response = await fetch('/api/getSources', {
      method: 'POST',
      body: JSON.stringify({ topic }),
    });

    let sources = await response.json();

    // This fetch() will 404 for now
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        placeholder="Teach me about..."
      />
      <select value={grade} onChange={(e) => setGrade(e.target.value)}>
        <option>Elementary School</option>
        <option>Middle School</option>
        <option>High School</option>
        <option>College</option>
        <option>Undergrad</option>
        <option>Graduate</option>
      </select>
    </form>
  );
}
```

If we submit the form, we see our React app makes a request to `/getSources`:

<Frame>
  <img alt="" />
</Frame>

Let’s go implement this API route.

## Getting web sources with Exa

To create our API route, we’ll make a new `app/api/getSources/route.js` file:

```jsx JSX theme={null}
// app/api/getSources/route.js
export async function POST(req) {
  let json = await req.json();

  // `json.topic` has the user's text
}
```

The [Exa API](https://exa.ai/) lets you make a fetch request to get back search results, so we’ll use it to build up our list of sources:

```jsx JSX theme={null}
// app/api/getSources/route.js
import { NextResponse } from 'next/server';

export async function POST(req) {
  const json = await req.json();

  const response = await fetch('https://api.exa.ai/search', {
    method: 'POST',
    headers: {
      'x-api-key': process.env['EXA_API_KEY'],
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      query: json.topic,
      numResults: 6,
      type: 'auto',
    }),
  });
  const { results } = await response.json();

  return NextResponse.json(
    results.map((result) => ({
      name: result.title,
      url: result.url,
    }))
  );
}
```

In order to make a request to Exa's API, you'll need to [get an API key from Exa](https://dashboard.exa.ai/api-keys). Once you have it, set it in `.env.local`:

```jsx JSX theme={null}
// .env.local
EXA_API_KEY=xxxxxxxxxxxx
```

and our API handler should work.

Let’s try it out from our React app! We’ll log the sources in our submit handler:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  const [topic, setTopic] = useState('');
  const [grade, setGrade] = useState('');

  async function handleSubmit(e) {
    e.preventDefault();

    const response = await fetch('/api/getSources', {
      method: 'POST',
      body: JSON.stringify({ topic }),
    });

    const sources = await response.json();

    // log the response from our new endpoint
    console.log(sources);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        placeholder="Teach me about..."
      />
      <select value={grade} onChange={(e) => setGrade(e.target.value)}>
        <option>Elementary School</option>
        <option>Middle School</option>
        <option>High School</option>
        <option>College</option>
        <option>Undergrad</option>
        <option>Graduate</option>
      </select>
    </form>
  );
}
```

and if we try submitting a topic, we’ll see an array of pages logged in the console!

<Frame>
  <img alt="" />
</Frame>

Let’s create some new React state to store the responses and display them in our UI:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  const [topic, setTopic] = useState('');
  const [grade, setGrade] = useState('');
  const [sources, setSources] = useState([]);

  async function handleSubmit(e) {
    e.preventDefault();

    const response = await fetch('/api/getSources', {
      method: 'POST',
      body: JSON.stringify({ topic }),
    });

    const sources = await response.json();

    // Update the sources with our API response
    setSources(sources);
  }

  return (
    <>
      <form onSubmit={handleSubmit}>{/* ... */}</form>

      {/* Display the sources */}
      {sources.length > 0 && (
        <div>
          <p>Sources</p>
          <ul>
            {sources.map((source) => (
              <li key={source.url}>
                <a href={source.url}>{source.name}</a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </>
  );
}
```

If we try it out, our app is working great so far!

<Frame>
  <img alt="" />
</Frame>

We’re taking the user’s topic, fetching six relevant web sources from Exa, and displaying them in our UI.

Next, let’s get the text content from each website so that our AI model has some context for its first response.

## Fetching the content from each source

Let’s make a request to a second endpoint called `/api/getParsedSources`, passing along the sources in the request body:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  // ...

  async function handleSubmit(e) {
    e.preventDefault();

    const response = await fetch('/api/getSources', {
      method: 'POST',
      body: JSON.stringify({ question }),
    });

    const sources = await response.json();
    setSources(sources);

    // Send the sources to a new endpoint
    const parsedSourcesRes = await fetch('/api/getParsedSources', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ sources }),
    });

    // The second fetch() will 404 for now
  }

  // ...
}
```

We’ll create a file at `app/api/getParsedSources/route.js` for our new route:

```jsx JSX theme={null}
// app/api/getParsedSources/route.js
export async function POST(req) {
  let json = await req.json();

  // `json.sources` has the websites from Exa
}
```

Now we’re ready to actually get the text from each one of our sources.

Let’s write a new `getTextFromURL` function and outline our general approach:

```jsx JSX theme={null}
async function getTextFromURL(url) {
  // 1. Use fetch() to get the HTML content
  // 2. Use the `jsdom` library to parse the HTML into a JavaScript object
  // 3. Use `@mozilla/readability` to clean the document and
  //    return only the main text of the page
}
```

Let’s implement this new function. We’ll start by installing the `jsdom` and `@mozilla/readability` libraries:

```jsx JSX theme={null}
npm i jsdom @mozilla/readability
```

Next, let’s implement the steps:

```jsx JSX theme={null}
async function getTextFromURL(url) {
  // 1. Use fetch() to get the HTML content
  const response = await fetch(url);
  const html = await response.text();

  // 2. Use the `jsdom` library to parse the HTML into a JavaScript object
  const virtualConsole = new jsdom.VirtualConsole();
  const dom = new JSDOM(html, { virtualConsole });

  // 3. Use `@mozilla/readability` to clean the document and
  //    return only the main text of the page
  const { textContent } = new Readability(doc).parse();
}
```

Looks good - let’s try it out!

We’ll run the first source through `getTextFromURL`:

```jsx JSX theme={null}
// app/api/getParsedSources/route.js
export async function POST(req) {
  let json = await req.json();

  let textContent = await getTextFromURL(json.sources[0].url);

  console.log(textContent);
}
```

If we submit our form, we’ll see the text show up in our server terminal from the first page!

<Frame>
  <img alt="" />
</Frame>

Let’s update the code to get the text from all the sources.

Since each source is independent, we can use `Promise.all` to kick off our functions in parallel:

```jsx JSX theme={null}
// app/api/getAnswer/route.js
export async function POST(req) {
  let json = await req.json();

  let results = await Promise.all(
    json.sources.map((source) => getTextFromURL(source.url))
  );

  console.log(results);
}
```

If we try again, we’ll now see an array of each web page’s text logged to the console:

<Frame>
  <img alt="" />
</Frame>

We’re ready to use the parsed sources in our React frontend!

## Using the sources for the chatbot’s initial messages

Back in our React app, we now have the text from each source in our submit handler:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  // ...

  async function handleSubmit(e) {
    e.preventDefault();

    const response = await fetch('/api/getSources', {
      method: 'POST',
      body: JSON.stringify({ question }),
    });

    const sources = await response.json();
    setSources(sources);

    const parsedSourcesRes = await fetch('/api/getParsedSources', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ sources }),
    });

    // The text from each source
    const parsedSources = await parsedSourcesRes.json();
  }

  // ...
}
```

We’re ready to kick off our chatbot. We’ll use the selected grade level and the parsed sources to write a system prompt, and pass in the selected topic as the user’s first message:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  const [messages, setMessages] = useState([]);
  // ...

  async function handleSubmit(e) {
    // ...

    // The text from each source
    const parsedSources = await parsedSourcesRes.json();

    // Start our chatbot
    const systemPrompt = `
      You're an interactive personal tutor who is an expert at explaining topics. Given a topic and the information to teach, please educate the user about it at a ${grade} level.

      Here's the information to teach:

      <teaching_info>
      ${parsedSources.map(
        (result, index) =>
          `## Webpage #${index}:\\n ${result.fullContent} \\n\\n`
      )}
      </teaching_info>
    `;

    const initialMessages = [
      { role: 'system', content: systemPrompt },
      { role: 'user', content: topic },
    ];
    setMessages(initialMessages);

    // This will 404 for now
    const chatRes = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages: initialMessages }),
    });
  }

  // ...
}
```

We also created some new React state to store all the messages so that we can display and update the chat history as the user sends new messages.

We’re ready to implement our final API endpoint at `/chat`!

## Implementing the chatbot endpoint with Together AI’s SDK

Let’s install Together AI’s node SDK:

```jsx JSX theme={null}
npm i together-ai
```

and use it to query Llama 3.1 8B Turbo:

```jsx JSX theme={null}
// api/chat/route.js
import Together from 'together-ai';

const together = new Together();

export async function POST(req) {
  const json = await req.json();

  const res = await together.chat.completions.create({
    model: 'Qwen/Qwen3.5-9B',
    reasoning: { enabled: false },
    messages: json.messages,
    stream: true,
  });

  return new Response(res.toReadableStream());
}
```

Since we’re passing the array of messages directly from our React app, and the format is the same as what Together’s `chat.completions.create` method expects, our API handler is mostly acting as a simple passthrough.

We’re also using the `stream: true` option so our frontend will be able to show partial updates as soon as the LLM starts its response.

We’re ready to display our chatbot’s first message in our React app!

## Displaying the chatbot’s response in the UI

Back in our page, we’ll use the `ChatCompletionStream` helper from Together’s SDK to update our `messages` state as our API endpoint streams in text:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  const [messages, setMessages] = useState([]);
  // ...

  async function handleSubmit(e) {
    // ...

    const chatRes = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages: initialMessages }),
    });

    ChatCompletionStream.fromReadableStream(chatRes.body).on(
      'content',
      (delta) => {
        setMessages((prev) => {
          const lastMessage = prev[prev.length - 1];

          if (lastMessage.role === 'assistant') {
            return [
              ...prev.slice(0, -1),
              { ...lastMessage, content: lastMessage.content + delta },
            ];
          } else {
            return [...prev, { role: 'assistant', content: delta }];
          }
        });
      }
    );
  }

  // ...
}
```

Note that because we’re storing the entire history of messages as an array, we check the last message’s `role` to determine whether to append the streamed text to it, or push a new object with the assistant’s initial text.

Now that our `messages` React state is ready, let’s update our UI to display it:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  const [topic, setTopic] = useState('');
  const [grade, setGrade] = useState('');
  const [sources, setSources] = useState([]);
  const [messages, setMessages] = useState([]);

  async function handleSubmit(e) {
    // ...
  }

  return (
    <>
      <form onSubmit={handleSubmit}>{/* ... */}</form>

      {/* Display the sources */}
      {sources.length > 0 && (
        <div>
          <p>Sources</p>
          <ul>
            {sources.map((source) => (
              <li key={source.url}>
                <a href={source.url}>{source.name}</a>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Display the messages */}
      {messages.map((message, i) => (
        <p key={i}>{message.content}</p>
      ))}
    </>
  );
}
```

If we try it out, we’ll see the sources come in, and once our `chat` endpoint responds with the first chunk, we’ll see the answer text start streaming into our UI!

<Frame>
  <img alt="" />
</Frame>

## Letting the user ask follow-up questions

To let the user ask our tutor follow-up questions, let’s make a new form that only shows up once we have some messages in our React state:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  // ...
  const [newMessageText, setNewMessageText] = useState('');

  return (
    <>
      {/* Form for initial messages */}
      {messages.length === 0 && (
        <form onSubmit={handleSubmit}>{/* ... */}</form>
      )}

      {sources.length > 0 && <>{/* ... */}</>}

      {messages.map((message, i) => (
        <p key={i}>{message.content}</p>
      ))}

      {/* Form for follow-up messages */}
      {messages.length > 0 && (
        <form>
          <input
            value={newMessageText}
            onChange={(e) => setNewMessageText(e.target.value)}
            type="text"
          />
        </form>
      )}
    </>
  );
}
```

We’ll make a new submit handler called `handleMessage` that will look a lot like the end of our first `handleSubmit` function:

```jsx JSX theme={null}
// app/page.tsx
function Page() {
  const [messages, setMessages] = useState([]);
  // ...

  async function handleMessage(e) {
    e.preventDefault();

    const newMessages = [
      ...messages,
      {
        role: 'user',
        content: newMessageText,
      },
    ];

    const chatRes = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages: newMessages }),
    });
    setMessages(newMessages);

    ChatCompletionStream.fromReadableStream(chatRes.body).on(
      'content',
      (delta) => {
        setMessages((prev) => {
          const lastMessage = prev[prev.length - 1];

          if (lastMessage.role === 'assistant') {
            return [
              ...prev.slice(0, -1),
              { ...lastMessage, content: lastMessage.content + delta },
            ];
          } else {
            return [...prev, { role: 'assistant', content: delta }];
          }
        });
      }
    );
  }

  // ...
}
```

Because we have all the messages in React state, we can just create a new object for the user’s latest message, send it over to our existing `chat` endpoint, and reuse the same logic to update our app’s state as the latest response streams in.

The core features of our app are working great!

## Digging deeper

React and Together AI are a perfect match for building powerful chatbots like LlamaTutor.

The app is fully open-source, so if you want to keep working on the code from this tutorial, be sure to check it out on GitHub:

[https://github.com/Nutlope/llamatutor](https://github.com/Nutlope/llamatutor)

And if you’re ready to start building your own chatbots, [sign up for Together AI today](https://www.together.ai/) and make your first query in minutes!

***
