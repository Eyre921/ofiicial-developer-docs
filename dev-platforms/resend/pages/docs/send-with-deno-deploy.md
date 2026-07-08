---
title: "Send emails with Deno Deploy"
source: https://resend.com/docs/send-with-deno-deploy
path: docs/send-with-deno-deploy
---

Learn how to send your first email using Deno Deploy.

## Prerequisites

Before you start, you'll need:

* A Resend [API key](/docs/create-an-api-key)
* A [verified domain](/docs/add-a-domain)

## Guide

<Steps>
  <Step title="Create a Deno Deploy project">
    Go to [dash.deno.com/projects](https://dash.deno.com/projects) and create a new playground project.

    <img alt="Deno Deploy - New Project" />
  </Step>

  <Step title="Edit the handler function">
    Paste the following code into the browser editor:

    ```ts main.ts theme={"theme":{"light":"github-light","dark":"vesper"}}
    import { Resend } from 'npm:resend';

    const resend = new Resend('re_123456789');

    Deno.serve(async () => {
      try {
        const response = await resend.emails.send({
          from: 'Acme <onboarding@resend.dev>',
          to: ['delivered@resend.dev'],
          subject: 'Hello World',
          html: '<strong>It works!</strong>',
        });

        return new Response(JSON.stringify(response), {
          status: response.error ? 500 : 200,
          headers: {
            'Content-Type': 'application/json',
          },
        });
      } catch (error) {
        console.error(error);
        return new Response(null, {
          status: 500,
        });
      }
    });
    ```
  </Step>

  <Step title="Deploy and send email">
    Click on `Save & Deploy` at the top of the screen.

    <img alt="Deno Deploy - Playground" />
  </Step>
</Steps>

## Examples

<Card title="Deno Deploy Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-deno-deploy-example">
  See the full source code.
</Card>
