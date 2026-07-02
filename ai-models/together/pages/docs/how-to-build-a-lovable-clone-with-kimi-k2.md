---
title: "Build a lovable clone with Kimi K2"
source: https://docs.together.ai/docs/how-to-build-a-lovable-clone-with-kimi-k2
path: docs/how-to-build-a-lovable-clone-with-kimi-k2
---

Learn how to build a full-stack Next.js app that can generate React apps with a single prompt.

[LlamaCoder](https://llamacoder.together.ai/) is a Lovable-inspired app that shows off how easy it is to use Together AI’s hosted LLM endpoints to build AI applications.

<Frame>
  <img alt="" />
</Frame>

In this post, we’re going to learn how to build the core parts of the app. LlamaCoder is a Next.js app, but Together’s APIs can be used with any web framework or language!

## Scaffolding the initial UI

The core interaction of LlamaCoder is a text field where the user can enter a prompt for an app they’d like to build. So to start, we need that text field:

<Frame>
  <img alt="" />
</Frame>

We’ll render a text input inside of a form, and use some new React state to control the input’s value:

```jsx JSX theme={null}
function Page() {
  let [prompt, setPrompt] = useState('');

  return (
    <form>
      <input
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder='Build me a calculator app...'
        required
      />

      <button type='submit'>
        <ArrowLongRightIcon />
      </button>
    </form>
  );
}
```

Next, let’s wire up a submit handler to the form. We’ll call it `createApp`, since it’s going to take the user’s prompt and generate the corresponding app code:

```jsx JSX theme={null}
function Page() {
  let [prompt, setPrompt] = useState('');

  function createApp(e) {
    e.preventDefault();

    // TODO:
    // 1. Generate the code
    // 2. Render the app
  }

  return <form onSubmit={createApp}>{/* ... */}</form>;
}
```

To generate the code, we’ll have our React app query a new API endpoint. Let’s put it at `/api/generateCode`, and we’ll make it a POST endpoint so we can send along the `prompt` in the request body:

```jsx JSX theme={null}
async function createApp(e) {
  e.preventDefault();

  // TODO:
  // 1. Generate the code
  await fetch('/api/generateCode', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt }),
  });

  // 2. Render the app
}
```

Looks good – let’s go implement it!

## Generating code in an API route

To create an API route in the Next.js 14 app directory, we can make a new `route.js` file:

```jsx JSX theme={null}
// app/api/generateCode/route.js
export async function POST(req) {
  let json = await req.json();

  console.log(json.prompt);
}
```

If we submit the form, we’ll see the user’s prompt logged to the console. Now we’re ready to send it off to our LLM and ask it to generate our user’s app! We tested many open source LLMs and found that Kimi K2 was the only one that did a good job at generating small apps, so that’s what we decided to use for the app.

We’ll install Together’s node SDK:

```bash Shell theme={null}
npm i together-ai
```

and use it to kick off a chat with Kimi K2.

Here’s what it looks like:

```jsx JSX theme={null}
// app/api/generateCode/route.js
import Together from 'together-ai';

let together = new Together();

export async function POST(req) {
  let json = await req.json();

  let completion = await together.chat.completions.create({
    model: 'moonshotai/Kimi-K2.5',
    messages: [
      {
        role: 'system',
        content: 'You are an expert frontend React engineer.',
      },
      {
        role: 'user',
        content: json.prompt,
      },
    ],
  });

  return Response.json(completion);
}
```

We call `together.chat.completions.create` to get a new response from the LLM. We’ve supplied it with a “system” message telling the LLM that it should behave as if it’s an expert React engineer. Finally, we provide it with the user’s prompt as the second message.

Since we return a JSON object, let’s update our React code to read the JSON from the response:

```jsx JSX theme={null}
async function createApp(e) {
  e.preventDefault();

  // 1. Generate the code
  let res = await fetch('/api/generateCode', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt }),
  });
  let json = await res.json();

  console.log(json);

  // 2. Render the app
}
```

And now let’s give it a shot!

We’ll use something simple for our prompt like “Build me a counter”:

<Frame>
  <img alt="" />
</Frame>

When we submit the form, our API response takes several seconds, but then sends our React app the response.

If you take a look at your logs, you should see something like this:

<Frame>
  <img alt="" />
</Frame>

Not bad – Kimi K2 has generated some code that looks pretty good and matches our user’s prompt!

However, for this app, we’re only interested in the code, since we’re going to be actually running it in our user’s browser. So we need to do some prompt engineering to get Llama to only return the code in a format we expect.

## Engineering the system message to only return code

We spent some time tweaking the system message to make sure it output the best code possible – here’s what we ended up with for LlamaCoder:

```jsx JSX theme={null}
// app/api/generateCode/route.js
import Together from 'together-ai';

let together = new Together();

export async function POST(req) {
  let json = await req.json();

   let res = await together.chat.completions.create({
    model: 'moonshotai/Kimi-K2.5',
    messages: [
      {
        role: 'system',
        content: systemPrompt,
      },
      {
        role: 'user',
        content: json.prompt,
      },
    ],
    stream: true,
  });

  return new Response(res.toReadableStream(), {
    headers: new Headers({
      'Cache-Control': 'no-cache',
    }),
  });
}

let systemPrompt = `
  You are an expert frontend React engineer who is also a great UI/UX designer. Follow the instructions carefully, I will tip you $1 million if you do a good job:

  - Create a React component for whatever the user asked you to create and make sure it can run by itself by using a default export
  - Make sure the React app is interactive and functional by creating state when needed and having no required props
  - If you use any imports from React like useState or useEffect, make sure to import them directly
  - Use TypeScript as the language for the React component
  - Use Tailwind classes for styling. DO NOT USE ARBITRARY VALUES (e.g. \`h-[600px]\`). Make sure to use a consistent color palette.
  - Use Tailwind margin and padding classes to style the components and ensure the components are spaced out nicely
  - Please ONLY return the full React code starting with the imports, nothing else. It's very important for my job that you only return the React code with imports. DO NOT START WITH \`\`\`typescript or \`\`\`javascript or \`\`\`tsx or \`\`\`.

  NO LIBRARIES (e.g. zod, hookform) ARE INSTALLED OR ABLE TO BE IMPORTED.
`;
```

Now if we try again, we’ll see something like this:

<Frame>
  <img alt="" />
</Frame>

Much better –this is something we can work with!

## Running the generated code in the browser

Now that we’ve got a pure code response from our LLM, how can we actually execute it in the browser for our user?

This is where the phenomenal [Sandpack](https://sandpack.codesandbox.io/) library comes in.

Once we install it:

```bash Shell theme={null}
npm i @codesandbox/sandpack-react
```

we now can use the `<Sandpack>` component to render and execute any code we want!

Let’s give it a shot with some hard-coded sample code:

```jsx JSX theme={null}
<Sandpack
  template='react-ts'
  files={{
    'App.tsx': `export default function App() { return <p>Hello, world!</p> }`,
  }}
/>
```

If we save this and look in the browser, we’ll see that it works!

<Frame>
  <img alt="" />
</Frame>

All that’s left is to swap out our sample code with the code from our API route instead.

Let’s start by storing the LLM’s response in some new React state called `generatedCode`:

```jsx JSX theme={null}
function Page() {
  let [prompt, setPrompt] = useState('');
  let [generatedCode, setGeneratedCode] = useState('');

  async function createApp(e) {
    e.preventDefault();

    let res = await fetch('/api/generateCode', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt }),
    });
    let json = await res.json();

    setGeneratedCode(json.choices[0].message.content);
  }

  return (
    <div>
      <form onSubmit={createApp}>{/* ... */}</form>
    </div>
  );
}
```

Now, if `generatedCode` is not empty, we can render `<Sandpack>` and pass it in:

```jsx JSX theme={null}
function Page() {
  let [prompt, setPrompt] = useState('');
  let [generatedCode, setGeneratedCode] = useState('');

  async function createApp(e) {
    // ...
  }

  return (
    <div>
      <form onSubmit={createApp}>{/* ... */}</form>

      {generatedCode && (
        <Sandpack
          template='react-ts'
          files={{
            'App.tsx': generatedCode,
          }}
        />
      )}
    </div>
  );
}
```

Let’s give it a shot! We’ll try “Build me a calculator app” as the prompt, and submit the form.

Once our API endpoint responds, `<Sandpack>` renders our generated app!

<Frame>
  <img alt="" />
</Frame>

The basic functionality is working great! Together AI (with Kimi K2) + Sandpack have made it a breeze to run generated code right in our user’s browser.

## Streaming the code for immediate UI feedback

Our app is working well –but we’re not showing our user any feedback while the LLM is generating the code. This makes our app feel broken and unresponsive, especially for more complex prompts.

To fix this, we can use Together AI’s support for streaming. With a streamed response, we can start displaying partial updates of the generated code as soon as the LLM responds with the first token.

To enable streaming, there are two changes we need to make:

1. Update our API route to respond with a stream
2. Update our React app to read the stream

Let’s start with the API route.

To get Together to stream back a response, we need to pass the `stream: true` option into `together.chat.completions.create()`. We also need to update our response to call `res.toReadableStream()`, which turns the raw Together stream into a newline-separated ReadableStream of JSON stringified values.

Here’s what that looks like:

```jsx JSX theme={null}
// app/api/generateCode/route.js
import Together from 'together-ai';

let together = new Together();

export async function POST(req) {
  let json = await req.json();

  let res = await together.chat.completions.create({
    model: 'moonshotai/Kimi-K2.5',
    messages: [
      {
        role: 'system',
        content: systemPrompt,
      },
      {
        role: 'user',
        content: json.prompt,
      },
    ],
    stream: true,
  });

  return new Response(res.toReadableStream(), {
    headers: new Headers({
      'Cache-Control': 'no-cache',
    }),
  });
}
```

That’s it for the API route! Now, let’s update our React submit handler.

Currently, it looks like this:

```jsx JSX theme={null}
async function createApp(e) {
  e.preventDefault();

  let res = await fetch('/api/generateCode', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt }),
  });
  let json = await res.json();

  setGeneratedCode(json.choices[0].message.content);
}
```

Now that our response is a stream, we can’t just `res.json()` it. We need a small helper function to read the text from the actual bytes that are being streamed over from our API route.

Here’s the helper function. It uses an [AsyncGenerator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator) to yield out each chunk of the stream as it comes over the network. It also uses a TextDecoder to turn the stream’s data from the type Uint8Array (which is the default type used by streams for their chunks, since it’s more efficient and streams have broad applications) into text, which we then parse into a JSON object.

So let’s copy this function to the bottom of our page:

```jsx JSX theme={null}
async function* readStream(response) {
  let decoder = new TextDecoder();
  let reader = response.getReader();

  while (true) {
    let { done, value } = await reader.read();
    if (done) {
      break;
    }
    let text = decoder.decode(value, { stream: true });
    let parts = text.split('\\n');

    for (let part of parts) {
      if (part) {
        yield JSON.parse(part);
      }
    }
  }

  reader.releaseLock();
}
```

Now, we can update our `createApp` function to iterate over `readStream(res.body)`:

```jsx JSX theme={null}
async function createApp(e) {
  e.preventDefault();

  let res = await fetch('/api/generateCode', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt }),
  });

  for await (let result of readStream(res.body)) {
    setGeneratedCode(
      (prev) => prev + result.choices.map((c) => c.text ?? '').join('')
    );
  }
}
```

This is the cool thing about Async Generators –we can use `for...of` to iterate over each chunk right in our submit handler!

By setting `generatedCode` to the current text concatenated with the new chunk’s text, React automatically re-renders our app as the LLM’s response streams in, and we see `<Sandpack>` updating its UI as the generated app takes shape.

<Frame>
  <img alt="" />
</Frame>

Pretty nifty, and now our app is feeling much more responsive!

## Digging deeper

And with that, you now know how to build the core functionality of Llama Coder!

There’s plenty more tricks in the production app including animated loading states, the ability to update an existing app, and the ability to share a public version of your generated app using a Neon Postgres database.

The application is open-source, so check it out here to learn more: **[https://github.com/Nutlope/llamacoder](https://github.com/Nutlope/llamacoder)**

And if you’re ready to start querying LLMs in your own apps to add powerful AI features just like the kind we saw in this post, [sign up for Together AI](https://api.together.ai/) today and make your first query in minutes!
