---
title: "Send emails with Supabase Edge Functions"
source: https://resend.com/docs/send-with-supabase-edge-functions
path: docs/send-with-supabase-edge-functions
---

Learn how to send your first email using Supabase Edge Functions.

## Prerequisites

Before you start, you'll need:

* A Resend [API key](/docs/create-an-api-key)
* A [verified domain](/docs/add-a-domain)

Make sure you have the latest version of the [Supabase CLI](https://supabase.com/docs/guides/cli#installation) installed.

## 1. Create Supabase function

Create a new function locally:

```bash theme={"theme":{"light":"github-light","dark":"vesper"}}
supabase functions new resend
```

## 2. Edit the handler function

Paste the following code into the `index.ts` file:

```ts index.ts theme={"theme":{"light":"github-light","dark":"vesper"}}
const RESEND_API_KEY = Deno.env.get('RESEND_API_KEY');

const handler = async (_request: Request): Promise<Response> => {
  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${RESEND_API_KEY}`,
    },
    body: JSON.stringify({
      from: 'Acme <onboarding@resend.dev>',
      to: ['delivered@resend.dev'],
      subject: 'hello world',
      html: '<strong>it works!</strong>',
    }),
  });

  const data = await res.json();

  return new Response(JSON.stringify(data), {
    status: 200,
    headers: {
      'Content-Type': 'application/json',
    },
  });
};

Deno.serve(handler);
```

## 3. Deploy and send email

Run function locally:

```bash theme={"theme":{"light":"github-light","dark":"vesper"}}
supabase functions start
supabase functions serve resend --no-verify-jwt
```

Deploy function to Supabase:

```bash theme={"theme":{"light":"github-light","dark":"vesper"}}
supabase functions deploy resend
```

Open the endpoint URL to send an email:

<img alt="Supabase Edge Functions - Deploy Function" />

## 4. Try it yourself

<Card title="Supabase Edge Functions Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-supabase-edge-functions-example">
  See the full source code.
</Card>
