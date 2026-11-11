---
title: "Webhooks"
source: https://developers.notion.com/reference/webhooks
path: reference/webhooks
---

Learn how your connection can automatically respond to workspace activity in real-time.

Webhooks let your connection receive real-time updates from Notion. Whenever a page or database changes, Notion sends a secure HTTP POST request to your webhook endpoint. This allows your application to respond to workspace activity as it happens — whether that's syncing data, triggering automation, or keeping your UI in sync with user activity.

![When a page or database changes, Notion sends an event to the subscribed endpoint.](https://mintcdn.com/notion-demo/kSI9TVzPayvF1_1o/images/reference/cf4e4b4cbb5de9c5b1277b35386a21574b4960af36c14fe7d648d905377db478-image.png?fit=max\&auto=format\&n=kSI9TVzPayvF1_1o\&q=85\&s=1c744340e3bd893d14a8a63faeee7e69)

**Think of it like this:** Instead of repeatedly polling the Notion API to check if anything has changed, Notion will tell you the moment something important happens.

## How webhooks work: A simple example

**Let’s walk through an example from start to finish:**

**Step 1**

Your connection is subscribed to `page.content_updated` events.

**Step 2**

A user edits the title of a page in Notion.

**Step 3**

Within a minute, Notion sends a webhook request to your configured endpoint.

**Step 4**

The event payload includes metadata such as the page ID, the event type, and a timestamp.

**Step 5**

Your server receives the event, verifies it, and calls the Notion API to fetch the updated title using the page ID from the event.

**Step 6**

Your application updates its internal data or takes any other action you’ve defined.

This flow lets you react quickly to user activity, without polling or guessing when something has changed.

## Getting started with webhooks

### Step 1 - Creating a webhook subscription

To receive webhook events, you’ll need to create a subscription through your connection settings.

**You’ll need to:**

**Step 1**

Visit your [connection settings](https://app.notion.com/developers/connections).

**Step 2**

Either create a new connection or select an existing one.

**Step 3**

Navigate to the **Webhooks** tab and click **+ Create a subscription**.

![The Webhooks tab offers a button to start a subscription.](https://mintcdn.com/notion-demo/kSI9TVzPayvF1_1o/images/reference/522e40363df1bd7437239b25a1caacc8cc607426f45fc90febfff5f00647aeb4-webhooks-1.png?fit=max\&auto=format\&n=kSI9TVzPayvF1_1o\&q=85\&s=d749482045c385e3bd2b0200208e1cb3)

**Step 4**

Enter your public **Webhook URL** — this is the public endpoint where you want Notion to send events. It must be a secure (SSL) and publicly available endpoint. Endpoints in localhost are not reachable.

![The subscription form asks for a webhook URL and the event types to send.](https://mintcdn.com/notion-demo/kSI9TVzPayvF1_1o/images/reference/1ef497d7b9b3622de379e6907cd722167766413693ac9f1885b59eb028b4e7dd-webhooks-2.png?fit=max\&auto=format\&n=kSI9TVzPayvF1_1o\&q=85\&s=b0448cd6aabad1fb6be140e4cfddddd9)

**Step 5**

Choose which event types you'd like to subscribe to. You can modify these later if needed.

**Step 6**

Click **Create subscription**.

![The subscription is listed with a Verify control while verification is pending.](https://mintcdn.com/notion-demo/kSI9TVzPayvF1_1o/images/reference/6e68cad7be75acc8165e29eb2a56a282edba31fdcba78238831466b83a115b8f-webhooks-3.png?fit=max\&auto=format\&n=kSI9TVzPayvF1_1o\&q=85\&s=d3b26ec8514419ade5461e627d40def9)

At this point, your webhook is created but not yet verified. To complete the setup, you’ll need to confirm that your endpoint can receive and respond to verification.

### Step 2 - Verifying the subscription

When you create a subscription, Notion sends a one-time POST request to your webhook URL. The body of the request contains a `verification_token`, which proves that Notion can successfully reach your endpoint.

**Example payload with `verification_token`**:

```json JSON theme={null}
{
  "verification_token": "secret_tMrlL1qK5vuQAh1b6cZGhFChZTSYJlce98V0pYn7yBl"
}
```

**You’ll need to:**

**Step 1**

Inspect the incoming request at your endpoint and extract the `verification_token` from the JSON payload.

1. (Optional): Securely store this token for payload validation setup later, [in step 3](#step-3-validating-event-payloads-recommended).

**Step 2**

Go back to the **Webhooks** tab within your Notion connection UI and click **⚠️ Verify** on the bottom left of the page

![The subscription is listed with a Verify control while verification is pending.](https://mintcdn.com/notion-demo/kSI9TVzPayvF1_1o/images/reference/6e68cad7be75acc8165e29eb2a56a282edba31fdcba78238831466b83a115b8f-webhooks-3.png?fit=max\&auto=format\&n=kSI9TVzPayvF1_1o\&q=85\&s=d3b26ec8514419ade5461e627d40def9)

**Step 3**

Paste the `verification_token` value into the form and click **Verify subscription.**

![The verification dialog asks for the token sent to the webhook URL.](https://mintcdn.com/notion-demo/kSI9TVzPayvF1_1o/images/reference/42b82e16a49278f78ecfdfb6a8f5acafe1ae251376bdc636d43c68abf4f685e5-webhooks-4.png?fit=max\&auto=format\&n=kSI9TVzPayvF1_1o\&q=85\&s=88f55f71314ea42a4ca48806f1921e29)

If you did not receive a `verification_token`, you can click **Resend token** from the webhook verification modal.

Once submitted, your webhook subscription is considered active, and will start receiving events.

> [!NOTE]
>
> **Changing your webhook URL or event subscriptions**
>
> You can only change the webhook URL before verification. After verification, if you need to change the URL, you must delete and recreate the subscription. You can change the subscribed events at any time.

### Step 3 - Validating event payloads (Recommended)

To help ensure the security of your connection, Notion includes a cryptographic signature with every webhook event we send. This allows you to verify that the payload was sent by Notion and hasn’t been modified in transit.

While payload validation is optional, we recommend implementing it for any production environment.

> [!NOTE]
>
> **Using a no-code or low-code platform?**
>
> If you're using a no-code or low-code platform (like Zapier, Make, or Pipedream), you may not have access to custom code for signature verification — and that’s okay. Validation is encouraged, but not required for webhooks to work.

#### How it works

In the previous step, Notion sent a one-time `verification_token` to your webhook URL. You’ll use this token to verify the authenticity of all subsequent webhook events.

Every webhook request from Notion includes an `X-Notion-Signature` header, which contains an HMAC-SHA256 hash of the request body, signed with your `verification_token`.

**Sample `X-Notion-Signature` from Notion**:

```json JSON theme={null}
{
  "X-Notion-Signature": "sha256=461e8cbcba8a75c3edd866f0e71280f5a85cbf21eff040ebd10fe266df38a735"
}
```

To validate the request, you can use the `verification_token` along with the event's payload to recompute the signature and verify the request's authenticity. If they match, the payload is trustworthy.

> [!TIP]
>
> **Using the SDK for JavaScript and TypeScript?**
>
> [`@notionhq/client`](https://github.com/makenotion/notion-sdk-js) v5.23.0 and later includes a `verifyWebhookSignature()` helper that performs this check for you, including the constant-time comparison. Pass the raw request body exactly as it arrived (re-serialized JSON produces different bytes and fails verification), the `X-Notion-Signature` header value, and your `verification_token`:
>
> ```javascript theme={null}
> import { verifyWebhookSignature } from "@notionhq/client"
>
> const isTrustedPayload = await verifyWebhookSignature({
>   body: rawRequestBody,
>   signature: request.headers["x-notion-signature"],
>   verificationToken,
> })
> ```
>
> It works without configuration in Node.js 18+, Bun, Deno, Cloudflare Workers, Vercel Edge Functions, and browsers. The SDK also exports `signWebhookPayload()` for generating signatures when testing your handler.

**Sample code for computing the signature and validating the webhook payload:**

```javascript JavaScript theme={null}
import { createHmac, timingSafeEqual } from "crypto"

// Retrieve the `verification_token` from the initial request
// (subscription verification; Step 2)
const verificationToken = "secret_tMrlL1qK5vuQAh1b6cZGhFChZTSYJlce98V0pYn7yBl"

// This body should come from your request body for subsequent validations
const body = {"verification_token":"secret_tMrlL1qK5vuQAh1b6cZGhFChZTSYJlce98V0pYn7yBl"}

const calculatedSignature = `sha256=${createHmac("sha256", verificationToken).update(JSON.stringify(body)).digest("hex")}`

const isTrustedPayload = timingSafeEqual(
  Buffer.from(calculatedSignature),
  Buffer.from(headers["X-Notion-Signature"]),
)

if (!isTrustedPayload) {
  // Ignore the event
  return
}
```

```python Python theme={null}
import hmac
import hashlib
import json

# Retrieve the `verification_token` from initial request
# (subscription verification; Step 2)
verification_token = "secret_tMrlL1qK5vuQAh1b6cZGhFChZTSYJlce98V0pYn7yBl"

# This body should come from your request body for subsequent validations
body = {"verification_token": "secret_tMrlL1qK5vuQAh1b6cZGhFChZTSYJlce98V0pYn7yBl"}

# Calculate the signature
body_json = json.dumps(body, separators=(",", ":"))  # Minified JSON, matches JSON.stringify
hmac_obj = hmac.new(
    verification_token.encode("utf-8"),
    body_json.encode("utf-8"),
    hashlib.sha256
)
calculated_signature = "sha256=" + hmac_obj.hexdigest()

# Assume headers is a dict containing HTTP headers
# Example:
# headers = {"X-Notion-Signature": "<signature from request>"}

# Use hmac.compare_digest for timing-safe comparison
is_trusted_payload = hmac.compare_digest(
    calculated_signature,
    headers["X-Notion-Signature"]
)

if not is_trusted_payload:
    # Ignore the event
    return
```

```ruby Ruby theme={null}
require 'openssl'
require 'json'

# Retrieve the verification_token from initial request
verification_token = "secret_tMrlL1qK5vuQAh1b6cZGhFChZTSYJlce98V0pYn7yBl"

# This body should come from your request body for subsequent validations
body = { "verification_token" => "secret_tMrlL1qK5vuQAh1b6cZGhFChZTSYJlce98V0pYn7yBl" }

# Calculate the signature (minified JSON to match JSON.stringify)
body_json = JSON.generate(body)
digest = OpenSSL::HMAC.hexdigest("SHA256", verification_token, body_json)
calculated_signature = "sha256=#{digest}"

# Assume headers is a Hash containing HTTP headers
# Example:
# headers = { "X-Notion-Signature" => "<signature from request>" }

# Constant-time comparison
is_trusted_payload = ActiveSupport::SecurityUtils.secure_compare(
  calculated_signature,
  headers["X-Notion-Signature"]
)

unless is_trusted_payload
  # Ignore the event
  return
end
```

Implementing this validation step is a small lift that adds a strong layer of security to your webhook connection. If you ever rotate or recreate your webhook subscription, be sure to update your stored `verification_token`.

## Testing your webhook subscription

Once your webhook subscription is set up and verified, it’s a good idea to test that everything is working as expected.

Below are three common test scenarios you can try, each corresponding to a supported event type. These tests simulate typical content updates and help ensure your endpoint is receiving and processing events correctly.

### Test 1 - Change a page title

This test checks your webhook’s ability to handle aggregated events, which are delivered with a short delay to avoid sending redundant updates.

**You’ll need to:**

**Step 1**

In your Notion workspace, add the connection to a page.

**Step 2**

Change the title of that page.

**Step 3**

Wait a minute or two because aggregated events like `page.content_updated` are batched and may not be sent immediately.

**Step 4**

Check your server logs or webhook handler. You should receive a `page.content_updated` event.

**Step 5**

Use the entity.id value from the payload to call the `retrieve a page` endpoint and confirm the new title.

### Test 2 - Add a comment

This test checks event delivery for comments, which require specific capabilities.

**You’ll need to:**

**Step 1**

In a page your connection has access to, add a new comment.

**Step 2**

Your webhook should receive a `comment.created` event within a few seconds.

**Important:**

To receive this event, your connection must include the `comment read` capability in its configuration. You can confirm this by opening your connection's **Configuration** tab and scrolling to the Capabilities section.

### Test 3 - Modify a database schema

This test verifies that structural changes to databases are triggering events.

**You’ll need to:**

**Step 1**

Open any database your connection is connected to.

**Step 2**

Make a schema change — for example, add a new property (column), rename an existing one, or delete a property.

**Step 3**

Your webhook should receive a `data_source.schema_updated` (in the new 2025-09-03 API version) or `database.schema_updated` (deprecated after 2022-06-28 API version) event shortly after the change.

## Troubleshooting tips

If your webhook isn’t receiving events as expected, here are a few things to double-check. These are the most common reasons developers miss events during setup or testing.

### 🔒 1. Check access permissions

Make sure the connection has access to the object that triggered the event. For example, if a new page is created inside a private page your connection doesn’t have access to, the event won’t be triggered.

### ✅ 2. Confirm capabilities

Some event types require specif# Authentication
Source: https://developers.notion.com/cli/get-started/authentication

Log in to your Notion workspace and manage CLI credentials.

## Log in

Authenticate with your Notion workspace:

```bash theme={null}
ntn login
```

This opens your browser to an authorization page. Confirm that the code in the browser matches the code printed in your terminal before approving. This prevents another page from completing the login in your name.

Your workspace-scoped token will be stored securely in your system's keychain.

If you've already logged in to one or more workspaces, you can pick existing workspace to switch the default, or pick **Authenticate with new workspace** to start a fresh browser flow and add another workspace.

> [!NOTE]
>
> `ntn login` requires full workspace membership. [Guests](https://www.notion.com/help/whos-who-in-a-workspace) and [restricted members](https://www.notion.com/help/whos-who-in-a-workspace) cannot log in with the Notion CLI. If you need CLI access, ask a workspace admin to upgrade your role. See [Personal access tokens](/guides/connections-and-tokens/personal-access-tokens) for more on who can create tokens.

## Log in without a browser

On a remote machine, container, or CI runner that can't open a browser, use `--no-browser` to get a two-step login flow:

1. Run `ntn login --no-browser`. It prints a URL, a verification code, and a `ntn login poll` command.
2. Open the URL in any browser, sign in, and confirm the verification code.
3. Run `ntn login poll` on the original machine to redeem the token.

`ntn login` also falls back to this flow automatically when it detects there is no terminal (e.g. piped input).

Login sessions expire after a short window. If polling fails because the session expired, run `ntn login` again to start over.

For unattended use (CI, scripts, bots), prefer a [personal access token](#use-a-personal-access-token) instead.

## Target a specific workspace

To run a single command against a non-default workspace without switching defaults, set `NOTION_WORKSPACE_ID`:

```bash theme={null}
NOTION_WORKSPACE_ID=<workspace-id> ntn api v1/users/me
```

Workspace IDs are listed in the output of `ntn debug`.

## Use a personal access token

For unattended use, authenticate with a [personal access token](/guides/connections-and-tokens/personal-access-tokens) (PAT) by exporting it as `NOTION_API_TOKEN`:

```bash theme={null}
export NOTION_API_TOKEN=ntn_xxx...
ntn api v1/users/me
```

`NOTION_API_TOKEN` takes precedence over anything stored in the keychain, so the same shell can mix `ntn login`-based commands and PAT-based commands depending on what's exported.

## Inspect your session

```bash theme={null}
ntn doctor
```

## Log out

```bash theme={null}
ntn logout
```

This forgets every cached workspace, deletes each one's token from the keychain, and clears the default workspace. The `config.json` and `workspaces.json` files themselves stay in place — run `ntn login` to repopulate them.

## Where credentials are stored

Tokens live in your OS credential store (Keychain on macOS, Secret Service on Linux) under the service name `notion-cli`, with the workspace ID as the account.

Two files sit alongside them in the CLI config directory:

* `config.json` — CLI version, default workspace per, and the optional `keyring` toggle.
* `workspaces.json` — cached workspace IDs and names for the interactive picker.

The config directory is `NOTION_HOME` if set, otherwise `$XDG_CONFIG_HOME/notion`, `$HOME/.config/notion`, or `$HOME/.notion` as fallbacks.

### Opt out of the OS keychain

On systems without a usable keychain, `ntn login` fails with a keychain error. Common examples include Docker containers, CI runners, SSH sessions to a Linux server, etc.

Set `NOTION_KEYRING=0` to store tokens in plain JSON at `auth.json` in the config directory instead. Treat that file like any other secret.

```bash theme={null}
NOTION_KEYRING=0 ntn login
```

To make it permanent, set `"keyring": false` in `config.json`. The env var always wins.

## Environment variables

| Variable | Purpose |
| :- | :- |
| `NOTION_API_TOKEN` | When this is set, it'll take precedence over `ntn login`'s keychain entry. Handy for scripts and CI. |
| `NOTION_WORKSPACE_ID` | Override the default workspace for a single command. |
| `NOTION_KEYRING` | Set to `0` to use file-based storage instead of the OS keychain. |
| `NOTION_HOME` | Override the config directory. |
| `NOTION_ENV` | Same as `--env`. Rarely needed. |

Run `ntn login --help` for the full list.

## Next steps

> [card] [Workers quickstart](/workers/get-started/quickstart)
>
> Create and deploy your first Notion Worker.

> [card] [API requests](/cli/guides/api-requests)
>
> Make Notion API requests from the terminal.

> [card] [Command reference](/cli/reference/commands)
>
> Full reference for every ntn command.

> [card] [Personal access tokens](/guides/connections-and-tokens/personal-access-tokens)
>
> Create tokens for scripts and CI.
