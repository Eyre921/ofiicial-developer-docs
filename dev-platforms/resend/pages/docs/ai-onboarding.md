---
title: "AI Onboarding"
source: https://resend.com/docs/ai-onboarding
path: docs/ai-onboarding
---

Everything you need to onboard your AI agent to Resend.

If you're developing with AI, Resend offers several resources to improve your experience.

* [Resend MCP Server](#resend-mcp-server)
* [Resend CLI](#resend-cli)
* [Resend Docs for Agents](#resend-docs-for-agents)
* [Email Skills for Agents](#email-skills-for-agents)
* [Quick Start Guides](#quick-start-guides)
* [OpenClaw Guide](#openclaw-guide)
* [Chat SDK](#chat-sdk)
* [AI Builder Guides](#ai-builder-guides)
* [AI Integrations](#ai-integrations)

## Prerequisite: Create an API Key

We require a human to create a Resend account. Once you have an account, you'll need to [create an API key](https://resend.com/api-keys). With an API key, your agent can perform many other tasks.

<Info>
  To send or receive with Resend, you'll need to [verify a domain](https://resend.com/domains). While an agent can [create a domain](/docs/api-reference/domains/create-domain), the API returns DNS records you will need to add in your DNS provider before [verifying your DNS records](/docs/api-reference/domains/verify-domain). You may find it easier to verify your domain in the dashboard.
</Info>

## Resend MCP Server

MCP is an open protocol that standardizes how applications provide context to LLMs. Among other benefits, it provides LLMs tools to act on your behalf. Our [MCP server](https://github.com/resend/resend-mcp) is open-source and covers our full API surface area.

Resend hosts the MCP server, so you can connect any MCP client without installing anything:

```
https://mcp.resend.com/mcp
```

For example, with Claude Code:

```bash theme={"theme":{"light":"github-light","dark":"vesper"}}
claude mcp add --transport http resend https://mcp.resend.com/mcp
```

When you connect, your client authenticates with OAuth by opening a browser to log in to Resend. Clients that can't complete a browser login can pass an API key as a Bearer token instead. You can also run the server locally with `npx` using the `resend-mcp` package on NPM.

<Card title="MCP Server" icon="microchip-ai" href="/mcp-server">
  View setup instructions for Claude, Cursor, Codex, Copilot, Windsurf, and
  more.
</Card>

## Resend CLI

The Resend CLI lets you send emails, manage your account, and develop locally, all from the terminal. It's built for humans, AI agents, and CI/CD pipelines.

```bash theme={"theme":{"light":"github-light","dark":"vesper"}}
# Authenticate
resend login

# Send an email
resend emails send \
  --from "you@example.com" \
  --to hello@example.com \
  --subject "Hello" \
  --text "Sent from my terminal."
```

The CLI also includes a full local webhook setup for developing with inbound email events without deploying anything.

<Card title="Resend CLI" icon="terminal" href="/cli">
  Install the CLI and set up a local webhook development environment.
</Card>

## Resend Docs for Agents

You can give your agent current docs in a context-aware way in three ways:

1. **Markdown docs**

   Every doc includes a markdown version (append `md` to any page)

   ```
   Docs for this page: https://resend.com/docs/ai-onboarding.md
   ```

2. **Full llms.txt**

   Give your agent all our docs in a single file.

   ```
   Here are the Resend docs: https://resend.com/docs/llms-full.txt
   ```

3. **MCP Docs server**

   For a more structured approach using MCP tools, you can install our MCP docs server in any MCP client, like Cursor, Codex, or Claude Code.

   ```
   npx add-mcp https://resend.com/docs/mcp
   ```

## Email Skills for Agents

Skills give AI agents specialized knowledge for specific tasks.

Install skills with a single command:

```bash theme={"theme":{"light":"github-light","dark":"vesper"}}
npx skills add resend/resend-skills
```

Or install individually:

| Skill                                               | Install                                      | What it does                                                                                                       |
| --------------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| [Resend](/docs/resend-skill)                             | `npx skills add resend/resend-skills`        | Send and receive emails, handle errors, and prevent duplicate sends. Get code examples from various SDKs.          |
| [React Email](/docs/react-email-skill)                   | `npx skills add resend/react-email`          | Build emails in React, Tailwind, and TypeScript. Audit existing React emails for style and cross-client rendering. |
| [Email Best Practices](/docs/email-best-practices-skill) | `npx skills add resend/email-best-practices` | Audit SPF/DKIM/DMARC setup, compliance (CAN-SPAM, GDPR), webhook handling                                          |

## Quick Start Guides

Throughout our documentation, we provide quick start guides for common tasks with Resend. They contain step-by-step instructions for sending emails, creating templates, and more. Copy the prompt for your agent or click to open in Cursor.

<Prompt description="Example agent quick start guide for sending emails." icon="envelope">
  Resend provides two endpoints for sending emails:

  | Approach   | Endpoint             | Use Case                                                                  |
  | ---------- | -------------------- | ------------------------------------------------------------------------- |
  | **Single** | `POST /emails`       | Individual transactional emails, emails with attachments, scheduled sends |
  | **Batch**  | `POST /emails/batch` | Multiple distinct emails in one request (max 100), bulk notifications     |

  **Choose batch when:**

  * Sending 2+ distinct emails at once
  * Reducing API calls is important (by default, rate limit is 2 requests per second)
  * No attachments or scheduling needed

  **Choose single when:**

  * Sending one email
  * Email needs attachments
  * Email needs to be scheduled
  * Different recipients need different timing

  ## Quick Start

  1. **Detect project language** from config files (package.json, requirements.txt, go.mod, etc.)
  2. **Install SDK** (preferred) or use cURL
  3. **Choose single or batch** based on the decision matrix above
  4. **Implement best practices** - Idempotency keys, error handling, retries

  ## Best Practices (Critical for Production)

  Always implement these for production email sending.

  ### Idempotency Keys

  Prevent duplicate emails when retrying failed requests.

  | Key Facts             |                                                                  |
  | --------------------- | ---------------------------------------------------------------- |
  | **Format (single)**   | `<event-type>/<entity-id>` (e.g., `welcome-email/user-123`)      |
  | **Format (batch)**    | `batch-<event-type>/<batch-id>` (e.g., `batch-orders/batch-456`) |
  | **Expiration**        | 24 hours                                                         |
  | **Max length**        | 256 characters                                                   |
  | **Duplicate payload** | Returns original response without resending                      |
  | **Different payload** | Returns 409 error                                                |

  ### Error Handling

  | Code     | Action                                                                                      |
  | -------- | ------------------------------------------------------------------------------------------- |
  | 400, 422 | Fix request parameters, don't retry                                                         |
  | 401, 403 | Check API key / verify domain, don't retry                                                  |
  | 409      | Idempotency conflict - use new key or fix payload                                           |
  | 429      | Rate limited - retry with exponential backoff (by default, rate limit is 2 requests/second) |
  | 500      | Server error - retry with exponential backoff                                               |

  ### Retry Strategy

  * **Backoff:** Exponential (1s, 2s, 4s...)
  * **Max retries:** 3-5 for most use cases
  * **Only retry:** 429 (rate limit) and 500 (server error)
  * **Always use:** Idempotency keys when retrying

  ## Single Email

  **Endpoint:** `POST /emails` (prefer SDK over cURL)

  ### Required Parameters

  | Parameter        | Type      | Description                                         |
  | ---------------- | --------- | --------------------------------------------------- |
  | `from`           | string    | Sender address. Format: `"Name <email@domain.com>"` |
  | `to`             | string\[] | Recipient addresses (max 50)                        |
  | `subject`        | string    | Email subject line                                  |
  | `html` or `text` | string    | Email body content                                  |

  ### Optional Parameters

  | Parameter        | Type      | Description                       |
  | ---------------- | --------- | --------------------------------- |
  | `cc`             | string\[] | CC recipients                     |
  | `bcc`            | string\[] | BCC recipients                    |
  | `reply_to`\*     | string\[] | Reply-to addresses                |
  | `scheduled_at`\* | string    | Schedule send time (ISO 8601)     |
  | `attachments`    | array     | File attachments (max 40MB total) |
  | `tags`           | array     | Key/value pairs for tracking      |
  | `headers`        | object    | Custom headers                    |

  \*Parameter naming varies by SDK (e.g., `replyTo` in Node.js, `reply_to` in Python).

  ### Minimal Example (Node.js)

  ```typescript theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('YOUR_RESEND_API_KEY');

  const { data, error } = await resend.emails.send(
    {
      from: 'Acme <onboarding@resend.dev>',
      to: ['delivered@resend.dev'],
      subject: 'Hello World',
      html: '<p>Email body here</p>',
    },
    { idempotencyKey: `welcome-email/${userId}` },
  );

  if (error) {
    console.error('Failed:', error.message);
    return;
  }
  console.log('Sent:', data.id);
  ```

  ## Batch Email

  **Endpoint:** `POST /emails/batch` (but prefer SDK over cURL)

  ### Limitations

  * **No attachments** - Use single sends for emails with attachments
  * **No scheduling** - Use single sends for scheduled emails
  * **Atomic** - If one email fails validation, the entire batch fails
  * **Max 100 emails** per request
  * **Max 50 recipients** per individual email in the batch

  ### Pre-validation

  Since the entire batch fails on any validation error, validate all emails before sending:

  * Check required fields (from, to, subject, html/text)
  * Validate email formats
  * Ensure batch size is less than or equal to 100

  ### Minimal Example (Node.js)

  ```typescript theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('YOUR_RESEND_API_KEY');

  const { data, error } = await resend.batch.send(
    [
      {
        from: 'Acme <hello@example.com>',
        to: ['delivered@resend.dev'],
        subject: 'Order Shipped',
        html: '<p>Your order has shipped!</p>',
      },
      {
        from: 'Acme <hello@example.com>',
        to: ['delivered@resend.dev'],
        subject: 'Order Confirmed',
        html: '<p>Your order is confirmed!</p>',
      },
    ],
    { idempotencyKey: `batch-orders/${batchId}` },
  );

  if (error) {
    console.error('Batch failed:', error.message);
    return;
  }
  console.log(
    'Sent:',
    data.map((e) => e.id),
  );
  ```
</Prompt>

## OpenClaw Guide

Equipping your agent with its own email inbox can be a powerful tool to unlock new workflows. Alternatively, give it access to your Resend account to support agentic flows for sending and receiving emails.

<Card title="Email Automation for OpenClaw using Resend" icon="lobster" href="/openclaw-guide">
  View the OpenClaw guide.
</Card>

## Chat SDK

The `@resend/chat-sdk-adapter` package is a Vercel Chat SDK adapter that turns email into a two-way communication channel. Receive inbound emails through webhooks, reply through the Resend API, and let the adapter handle threading automatically. It also supports card emails, attachments, and proactive outreach.

<Card title="Chat SDK" icon="comments" href="/chat-sdk">
  Build conversational email experiences with the Chat SDK adapter.
</Card>

## AI Builder Guides

We offer guides to using Resend with popular AI builders to help you get started with AI agents.

* [Anything Integration](/docs/anything-integration)
* [Lovable Integration](/docs/lovable-integration)
* [v0 Integration](/docs/v0-integration)
* [Bolt.new Integration](/docs/bolt-new-integration)
* [Replit Integration](/docs/replit-integration)
* [Base44 Integration](/docs/base44-integration)
* [Leap.new Integration](/docs/leap-new-integration)

## AI Integrations

Several AI tools have created integrations for working with Resend. Visit their documentation for information on integrating Resend with their tools.

<CardGroup>
  <Card title="Lovable" href="https://docs.lovable.dev/integrations/resend" icon={<LovableIcon />}>
    Tell the Lovable AI to send emails
  </Card>

  <Card title="Anything" href="https://www.createanything.com/docs/integrations/resend" icon={<AnythingIcon />}>
    Add email to your Anything projects
  </Card>

  <Card title="Wildcard" href="https://github.com/wild-card-ai/agents-json/blob/master/examples/resend.ipynb" icon={<WildcardIcon />}>
    Send natural language emails using Wildcard
  </Card>

  <Card title="mcp.run" href="https://www.mcp.run/nilslice/resend" icon={<McpRunIcon />}>
    Build email AI agents using mcp.run
  </Card>

  <Card title="Rocket" href="https://docs.rocket.new/integrations/resend" icon={<RocketIcon />}>
    Send emails from apps built with Rocket
  </Card>

  <Card title="Base44" href="https://docs.base44.com/Integrations/Resend-integration" icon={<Base44Icon />}>
    Add email to your Base44 apps
  </Card>

  <Card title="Leap.new" href="https://docs.leap.new/integrations/resend" icon={<LeapNewIcon />}>
    Add email to your Leap apps
  </Card>

  <Card title="Parsley" href="https://www.parsley.id/integrations/resend" icon={<ParsleyIcon />}>
    Send alerts and follow-ups with Parsley
  </Card>

  <Card title="Pica" href="https://www.picaos.com/integrations/resend" icon={<PicaIcon />}>
    Integrate Pica with Resend
  </Card>
</CardGroup>
