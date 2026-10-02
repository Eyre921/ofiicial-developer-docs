---
title: "Webhooks"
source: https://developers.notion.com/workers/guides/webhooks
path: workers/guides/webhooks
---

Receive HTTP events from external services in a Notion Worker.

Webhooks expose an HTTP endpoint that external services can call. Use them to push events from external systems into Notion, such as a GitHub push, Stripe event, Zendesk ticket update, or any service that can send an HTTP webhook.

## Basic webhook

Define a webhook capability on your worker like this:

```typescript theme={null}
import { Worker } from "@notionhq/workers";

const worker = new Worker();
export default worker;

worker.webhook("onExternalEvent", {
  title: "External Event Handler",
  description: "Processes incoming webhook requests",
  execute: async (events) => {
    for (const event of events) {
      console.log("Delivery:", event.deliveryId);
      console.log("Method:", event.method);
      console.log("Body:", event.body);
    }
  },
});
```

After you deploy, Notion creates a URL for each webhook capability. Give that URL to the external service as its webhook destination:

```bash theme={null}
ntn workers deploy
ntn workers webhooks list
```

## The event object

The `execute` function receives an array of `WebhookEvent` objects. The array currently contains one event, but may contain multiple events in the future.

| Property | Type | Description |
| :- | :- | :- |
| `deliveryId` | `string` | Unique ID for this Notion delivery. It is stable across retries for the same inbound request. |
| `body` | `Record<string, unknown>` | Parsed JSON body. If the request body is not a JSON object, this is `{}`. |
| `rawBody` | `string` | Original request body as a string. Use this for signature verification. |
| `headers` | `Record<string, string>` | Request headers. Header names are lowercased. |
| `method` | `string` | HTTP method used by the sender. Webhook URLs accept `POST` requests. |

<Tip>
  Use the external provider's own event ID for idempotency when the payload includes one.
  `deliveryId` is useful when Notion retries running your worker, but a provider may
  redeliver the same event as a new HTTP request.
</Tip>

## Webhook URLs

Webhook URLs include a unique ID that acts as a shared secret:

```text theme={null}
https://{spaceShortId}.webhook.notionusercontent.com/webhooks/worker/{spaceId}/{workerId}/{uniqueWebhookId}/{webhookName}
```

Use the CLI to print the URLs for a deployed worker:

```bash theme={null}
ntn workers webhooks list
```

For scripts, use JSON or tab-separated output:

```bash theme={null}
ntn workers webhooks list --json
ntn workers webhooks list --plain
```

<Warning>
  Treat webhook URLs as secrets. Anyone with the full URL can send events to the
  webhook endpoint unless you add provider-specific signature verification inside your worker.
</Warning>

## Verify requests in execute

Most webhook providers can sign requests with a shared [secret](/workers/guides/secrets). Store the signing secret as a worker secret, verify each request using `event.rawBody` and `event.headers`, and throw `WebhookVerificationError` when verification fails:

```typescript theme={null}
import * as crypto from "node:crypto";
import { WebhookVerificationError, Worker } from "@notionhq/workers";

const worker = new Worker();
export default worker;

/**
 * Verify a GitHub webhook signature.
 * GitHub sends the HMAC-SHA256 signature in the X-Hub-Signature-256 header
 * as "sha256={hex}". The raw body must be used for verification.
 */
function verifyGitHubSignature(
  rawBody: string,
  headers: Record<string, string>,
): void {
  const secret = process.env.GITHUB_WEBHOOK_SECRET;
  if (!secret) {
    throw new WebhookVerificationError("GITHUB_WEBHOOK_SECRET not configured");
  }

  const signature = headers["x-hub-signature-256"];
  if (!signature?.startsWith("sha256=")) {
    throw new WebhookVerificationError("Invalid GitHub signature");
  }

  const expected = `sha256=${crypto
    .createHmac("sha256", secret)
    .update(rawBody)
    .digest("hex")}`;

  if (signature.length !== expected.length) {
    throw new WebhookVerificationError("Invalid GitHub signature");
  }

  // Use timing-safe comparison to prevent timing attacks.
  if (!crypto.timingSafeEqual(Buffer.from(signature), Buffer.from(expected))) {
    throw new WebhookVerificationError("Invalid GitHub signature");
  }
}

worker.webhook("onGithubPush", {
  title: "GitHub Push Webhook",
  description: "Handles push events from GitHub repositories",
  execute: async (events) => {
    for (const event of events) {
      verifyGitHubSignature(event.rawBody, event.headers);
      console.log("Verified GitHub event:", event.body);
    }
  },
});
```

Set the secret before deploying or push it from your local `.env` file:

```bash theme={null}
ntn workers env set GITHUB_WEBHOOK_SECRET=your-secret
```

See [Secrets](/workers/guides/secrets) for more ways to manage worker environment variables.

<Warning>
  After 5 consecutive `WebhookVerificationError` failures, Notion blocks that
  webhook before running your handler. To reset the failure counter, redeploy
  the worker or [change the synchronous verification setting](#turn-synchronous-verification-off).
</Warning>

This check runs after Notion has already answered the provider with `202 Accepted`, so the provider never sees the result. Use it when all you need is to drop unsigned events. If the provider expects verification in the HTTP response itself, add a `verify` handler instead.

## Verify requests synchronously

<Note>
  Synchronous webhook verification requires `@notionhq/workers >= 0.9.0`
  and `ntn` CLI version `0.23.1`.
</Note>

Some providers will not accept a webhook until the endpoint answers completes a synchronous challenge flow. You can add a `verify` handler for these. It runs synchronously before Notion answers the provider, and allows you to control some elements of the webhook HTTP response such as the body and status code.

`verify` runs in the same sandbox as `execute`, with the full Node.js standard library. Read signing secrets from `process.env` and use `node:crypto` for signature checks.

```typescript theme={null}
import * as crypto from "node:crypto";
import { Worker } from "@notionhq/workers";

const worker = new Worker();
export default worker;

worker.webhook("onProviderEvent", {
  title: "Provider Events",
  description: "Handles events from an external provider",
  verify: (request) => {
    const secret = process.env.PROVIDER_WEBHOOK_SECRET;
    if (!secret) {
      return { status: 400, body: "PROVIDER_WEBHOOK_SECRET not configured" };
    }

    const signature = request.headers["x-signature-256"] ?? "";
    const expected = crypto
      .createHmac("sha256", secret)
      .update(request.rawBody)
      .digest("hex");

    // Compare lengths first: timingSafeEqual throws on buffers of
    // different lengths.
    if (
      signature.length !== expected.length ||
      !crypto.timingSafeEqual(Buffer.from(signature), Buffer.from(expected))
    ) {
      return { status: 401, body: "Invalid signature" };
    }

    return { status: 200 };
  },
  execute: async (events) => {
    for (const event of events) {
      console.log("Verified event:", event.body);
    }
  },
});
```

### The request object

`verify` receives the inbound HTTP request, not the array of `WebhookEvent` objects that `execute` receives.

| Property | Type | Description |
| :- | :- | :- |
| `method` | `"GET" \| "HEAD" \| "POST"` | Uppercase HTTP method. Deliveries are `POST`; `GET` and `HEAD` are handshake probes. |
| `url` | `string` | The full webhook URL as received, including the query string. |
| `query` | `Record<string, string>` | Query string parameters. A repeated parameter keeps its last value. |
| `headers` | `Record<string, string>` | Request headers. Header names are lowercased. |
| `rawBody` | `string` | Original request body as a string. Empty for `GET` and `HEAD`. |

Like `execute`, `verify` receives the capability context as its second argument.

### The response object

| Property | Type | Description |
| :- | :- | :- |
| `status` | `number` | Response status code. Only 2xx and 4xx are allowed. |
| `body` | `string` | Optional response body, at most 8KB. |
| `contentType` | `"application/json" \| "text/plain"` | Optional response content type. Defaults to `"text/plain"`. |
| `deliver` | `boolean` | Optional. Whether to queue the request for `execute`. When omitted, Notion decides from the status. |

### Choose whether `execute` runs

Notion always returns your status, body, and content type to the provider. Separately, it decides whether to queue the request for `execute`. By default, any 2xx status code queues the request for execution, while any non-2xx status does not. You can optionally set a `deliver` field in your response to control delivery for execution. Setting `deliver` overrides the status code.

Set `deliver` when the answer to the provider and the delivery decision differ. `deliver` always wins over the status.

| `verify` returns | Provider sees | Queued for `execute` |
| :- | :- | :- |
| `{ status: 200 }` | `200` | Yes |
| `{ status: 401 }` | `401` | No |
| `{ status: 200, deliver: false }` | `200` | No |
| `{ status: 401, deliver: true }` | `401` | Yes |

A common case is a subscription challenge. The provider needs a `200` with the challenge echoed back, but the challenge isn't an event, so there's nothing for `execute` to do:

```typescript theme={null}
verify: (request) => {
  const body = JSON.parse(request.rawBody || "{}");
  if (body.type === "url_verification") {
    return { status: 200, body: body.challenge, deliver: false };
  }
  // ...check the signature, then:
  return { status: 200 };
},
```

Without `deliver: false`, `execute` would receive the challenge and would need to skip it.

The opposite case is a request you reject but still want to keep. For example, you can answer `401` to a request with a bad signature and still queue it, so `execute` can log it for auditing:

```typescript theme={null}
return { status: 401, body: "Invalid signature", deliver: true };
```

### Timing and failures

`verify` answers the provider inline, so the run has a wall-clock budget of about 5 seconds that includes starting your worker's sandbox. Keep it to local computation. Avoid network calls, including `context.notion` requests, which usually will not fit the budget.

| Outcome | Provider sees | Queued for `execute` |
| :- | :- | :- |
| Returns 2xx | Your status and body | Yes, unless `deliver` is `false` |
| Returns 4xx | Your status and body | No, unless `deliver` is `true` |
| Throws, or returns a status outside 2xx and 4xx, or a body over 8KB | `400` | No |
| Exceeds the time budget | `503` with `Retry-After` | No |

<Warning>
  A handler that throws or returns an invalid response counts toward the same
  five-consecutive-failure limit as `WebhookVerificationError`, after which
  Notion blocks the webhook until you redeploy or change the synchronous
  verification setting. Deliberately returning a 4xx is not a failure and
  resets the counter.
</Warning>

Exceeding the budget is usually a cold sandbox start. The provider can retry, and will generally land on a warm sandbox.

### Turn synchronous verification off

You can turn off a webhook's `verify` handler without redeploying the worker. This helps when a `verify` bug is rejecting real events, or when a webhook is blocked by repeated failures and you need events flowing again right away.

Turn it off or back on with the webhook's key:

```bash theme={null}
ntn workers webhooks verification disable onProviderEvent
ntn workers webhooks verification enable onProviderEvent
```

The commands use the worker in `workers.json`. Pass `--worker-id` to pick a different worker, and `--json` or `--plain` for scripted output. You can also use the **Sync verification** switch in the webhooks table on the worker's **Overview** tab.

While synchronous verification is off, the webhook acts as if it had no `verify` handler:

* `POST` requests get `202 Accepted` and are queued for `execute`.
* `GET` and `HEAD` requests get `405 Method Not Allowed`, so handshake probes fail.
* `execute` still runs, so any signature check you do there still applies.

The setting stays in place across deploys. Deploying a new version doesn't turn synchronous verification back on. Changing the setting in either direction also resets the verification failure counter, which unblocks a blocked webhook.

## Execution and retries

When a webhook request reaches Notion, Notion validates the URL, enqueues the event, and responds with `202 Accepted`. Your worker runs asynchronously after the HTTP response is sent.

A webhook with a `verify` handler answers with whatever `verify` returned instead of `202`. It enqueues the event when `deliver` is `true`, or when `deliver` is omitted and the status is 2xx.

If your handler throws `WebhookVerificationError`, Notion records a verification failure and does not retry that event. If your handler throws another error, Notion retries the worker run up to 3 times.

Successful runs reset the consecutive verification failure counter.

Incoming webhook requests can be rejected with `429` before they are queued. A `202 Accepted` response means the event was queued for asynchronous processing, not that your handler has run successfully. Queued webhook executions are rate-limited separately and retried when they reach a rate limit. See [Limits](/workers/reference/limits) for the standard thresholds.

## Use Notion from a webhook

Webhook handlers receive the same context object as other capabilities, including `context.notion`, the Notion API SDK client:

```typescript theme={null}
worker.webhook("createPageFromWebhook", {
  title: "Create Page From Webhook",
  description: "Creates a page when an external event is received",
  execute: async (events, { notion }) => {
    const databaseId = process.env.MY_WEBHOOK_DATABASE_ID;

    if (!databaseId) {
      throw new Error("MY_WEBHOOK_DATABASE_ID is not configured");
    }

    for (const event of events) {
      const externalId =
        typeof event.body.id === "string" ? event.body.id : event.deliveryId;

      await notion.pages.create({
        parent: { database_id: databaseId },
        properties: {
          Name: {
            title: [
              {
                text: {
                  content: `Webhook event ${externalId}`,
                },
              },
            ],
          },
        },
      });
    }
  },
});
```

For webhooks, `context.notion` is not automatically authenticated. To call the Notion API, create an internal integration, give it access to the relevant pages or databases, and store the integration token in `NOTION_API_TOKEN`:

```bash theme={null}
ntn workers env set NOTION_API_TOKEN=secret_xxx
```

At runtime, `context.notion` reads `process.env.NOTION_API_TOKEN` and uses it as the Notion API client token.

For more information about creating an integration token for a worker, see [Using Notion API from a worker](/workers/guides/api-client).

## Inspect runs

Use worker run logs to debug webhook executions:

```bash theme={null}
ntn workers runs list
ntn workers runs logs <run-id>
```

To find recent webhook runs quickly:

```bash theme={null}
ntn workers runs list --plain | grep webhook
```

See the [CLI command reference](/cli/reference/commands) for all `ntn workers` flags and options.

## Next steps

<CardGroup>
  <Card title="Secrets" icon="lock" href="/workers/guides/secrets">
    Store webhook signing secrets and API keys.
  </Card>

  <Card title="Notion API" icon="database" href="/workers/guides/api-client">
    Read and write Notion data from a webhook handler.
  </Card>

  <Card title="OAuth" icon="key" href="/workers/guides/oauth">
    Authenticate with third-party APIs from your webhook.
  </Card>

  <Card title="SDK reference" icon="book-open" href="/workers/reference/sdk#worker-webhook">
    Detailed API docs for worker.webhook() and WebhookVerificationError.
  </Card>

  <Card title="Limits" icon="bolt" href="/workers/reference/limits">
    Webhook ingress and run rate limits.
  </Card>
</CardGroup>
