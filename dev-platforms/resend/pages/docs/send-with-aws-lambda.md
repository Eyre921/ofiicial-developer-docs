---
title: "Send emails with AWS Lambda"
source: https://resend.com/docs/send-with-aws-lambda
path: docs/send-with-aws-lambda
---

Learn how to send your first email using AWS Lambda.

## Prerequisites

Before you start, you'll need:

* A Resend [API key](/docs/create-an-api-key)
* A [verified domain](/docs/add-a-domain)

## 1. Create a AWS Lambda function

Go to [aws.amazon.com](https://aws.amazon.com) and create a new Lambda function using the Node.js 20.x or later runtime.

<img alt="AWS Lambda - New Function" />

## 2. Edit the handler function

Paste the following code into the browser editor:

```js index.mjs theme={"theme":{"light":"github-light","dark":"vesper"}}
const RESEND_API_KEY = 're_xxxxxxxxx';

export const handler = async (event) => {
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

  if (res.ok) {
    const data = await res.json();

    return {
      statusCode: 200,
      body: data,
    };
  }
};
```

## 3. Deploy and send email

Click on `Deploy` and then `Test` at the top of the screen.

<img alt="AWS Lambda - Edit Function" />

## 4. Try it yourself

<Card title="AWS Lambda Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-aws-lambda-example">
  See the full source code.
</Card>
