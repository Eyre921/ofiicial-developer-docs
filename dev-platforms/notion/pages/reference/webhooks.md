---
title: "Webhooks"
source: https://developers.notion.com/reference/webhooks
path: reference/webhooks
---

Learn how your connection can automatically respond to workspace activity in real-time.

Webhooks let your connection receive real-time updates from Notion. Whenever a page or database changes, Notion sends a secure HTTP POST request to your webhook endpoint. This allows your application to respond to workspace activity as it happens — whether that's syncing data, triggering automation, or keeping your UI in sync with user activity.

<Frame>
  <img alt="" />
</Frame>

**Think of it like this:** Instead of repeatedly polling the Notion API to check if anything has changed, Notion will tell you the moment something important happens.

## How webhooks work: A simple example

**Let’s walk through an example from start to finish:**

<Steps>
  <Step>
    Your connection is subscribed to `page.content_updated` events.
  </Step>

  <Step>
    A user edits the title of a page in Notion.
  </Step>

  <Step>
    Within a minute, Notion sends a webhook request to your configured endpoint.
  </Step>

  <Step>
    The event payload includes metadata such as the page ID, the event type, and a timestamp.
  </Step>

  <Step>
    Your server receives the event, verifies it, and calls the Notion API to fetch the updated title using the page ID from the event.
  </Step>

  <Step>
    Your application updates its internal data or takes any other action you’ve defined.
  </Step>
</Steps>

This flow lets you react quickly to user activity, without polling or guessing when something has changed.

## Getting started with webhooks

### Step 1 - Creating a webhook subscription

To receive webhook events, you’ll need to create a subscription through your connection settings.

**You’ll need to:**

<Steps>
  <Step>
    Visit your <a href={developerConnectionsUrl}>connection settings</a>.
  </Step>

  <Step>
    Either create a new connection or select an existing one.
  </Step>

  <Step>
    Navigate to the **Webhooks** tab and click **+ Create a subscription**.

    <Frame>
      <img alt="" />
    </Frame>
  </Step>

  <Step>
    Enter your public **Webhook URL** — this is the public endpoint where you want Notion to send events. It must be a secure (SSL) and publicly available endpoint. Endpoints in localhost are not reachable.

    <Frame>
      <img alt="" />
    </Frame>
  </Step>

  <Step>
    Choose which event types you'd like to subscribe to. You can modify these later if needed.
  </Step>

  <Step>
    Click **Create subscription**.

    <Frame>
      <img alt="" />
    </Frame>
  </Step>
</Steps>

At this point, your webhook is created but not yet verified. To complete the setup, you’ll need to confirm that your endpoint can receive and respond to verification.

### Step 2 - Verifying the subscription

When you create a subscription, Notion sends a one-time POST request to your webhook URL. The body of the request contains a `verification_token`, which proves that Notion can successfully reach your endpoint.

**Example payload with `verification_token`**:

<CodeGroup>
  ```json JSON theme={null}
  {
    "verification_token": "secret_tMrlL1qK5vuQAh1b6cZGhFChZTSYJlce98V0pYn7yBl"
  }
  ```
</CodeGroup>

**You’ll need to:**

<Steps>
  <Step>
    Inspect the incoming request at your endpoint and extract the `verification_token` from the JSON payload.

    1. (Optional): Securely store this token for payload validation setup later, [in step 3](#step-3-validating-event-payloads-recommended).
  </Step>

  <Step>
    Go back to the **Webhooks** tab within your Notion connection UI and click **⚠️ Verify** on the bottom left of the page

    <Frame>
      <img alt="" />
    </Frame>
  </Step>

  <Step>
    Paste the `verification_token` value into the form and click **Verify subscription.**

    <Frame>
      <img alt="" />
    </Frame>

    If you did not receive a `verification_token`, you can click **Resend token** from the webhook verification modal.
  </Step>
</Steps>

Once submitted, your webhook subscription is considered active, and will start receiving events.

<Info>
  **Changing your webhook URL or event subscriptions**

  You can only change the webhook URL before verification. After verification, if you need to change the URL, you must delete and recreate the subscription. You can change the subscribed events at any time.
</Info>

### Step 3 - Validating event payloads (Recommended)

To help ensure the security of your connection, Notion includes a cryptographic signature with every webhook event we send. This allows you to verify that the payload was sent by Notion and hasn’t been modified in transit.

While payload validation is optional, we recommend implementing it for any production environment.

<Info>
  **Using a no-code or low-code platform?**

  If you're using a no-code or low-code platform (like Zapier, Make, or Pipedream), you may not have access to custom code for signature verification — and that’s okay. Validation is encouraged, but not required for webhooks to work.
</Info>

#### How it works

In the previous step, Notion sent a one-time `verification_token` to your webhook URL. You’ll use this token to verify the authenticity of all subsequent webhook events.

Every webhook request from Notion includes an `X-Notion-Signature` header, which contains an HMAC-SHA256 hash of the request body, signed with your `verification_token`.

**Sample `X-Notion-Signature` from Notion**:

<CodeGroup>
  ```json JSON theme={null}
  {
    "X-Notion-Signature": "sha256=461e8cbcba8a75c3edd866f0e71280f5a85cbf21eff040ebd10fe266df38a735"
  }
  ```
</CodeGroup>

To validate the request, you can use the `verification_token` along with the event's payload to recompute the signature and verify the request's authenticity. If they match, the payload is trustworthy.

**Sample code for computing the signature and validating the webhook payload:**

<CodeGroup>
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
</CodeGroup>

Implementing this validation step is a small lift that adds a strong layer of security to your webhook connection. If you ever rotate or recreate your webhook subscription, be sure to update your stored `verification_token`.

## Testing your webhook subscription

Once your webhook subscription is set up and verified, it’s a good idea to test that everything is working as expected.

Below are three common test scenarios you can try, each corresponding to a supported event type. These tests simulate typical content updates and help ensure your endpoint is receiving and processing events correctly.

### Test 1 - Change a page title

This test checks your webhook’s ability to handle aggregated events, which are delivered with a short delay to avoid sending redundant updates.

**You’ll need to:**

<Steps>
  <Step>
    In your Notion workspace, add the connection to a page.
  </Step>

  <Step>
    Change the title of that page.
  </Step>

  <Step>
    Wait a minute or two because aggregated events like `page.content_updated` are batched and may not be sent immediately.
  </Step>

  <Step>
    Check your server logs or webhook handler. You should receive a `page.content_updated` event.
  </Step>

  <Step>
    Use the entity.id value from the payload to call the `retrieve a page` endpoint and confirm the new title.
  </Step>
</Steps>

### Test 2 - Add a comment

This test checks event delivery for comments, which require specific capabilities.

**You’ll need to:**

<Steps>
  <Step>
    In a page your connection has access to, add a new comment.
  </Step>

  <Step>
    Your webhook should receive a `comment.created` event within a few seconds.
  </Step>
</Steps>

**Important:**

To receive this event, your connection must include the `comment read` capability in its configuration. You can confirm this by opening your connection's **Configuration** tab and scrolling to the Capabilities section.

### Test 3 - Modify a database schema

This test verifies that structural changes to databases are triggering events.

**You’ll need to:**

<Steps>
  <Step>
    Open any database your connection is connected to.
  </Step>

  <Step>
    Make a schema change — for example, add a new property (column), rename an existing one, or delete a property.
  </Step>

  <Step>
    Your webhook should receive a `data_source.schema_updated` (in the new 2025-09-03 API version) or `database.schema_updated` (deprecated after 2022-06-28 API version) event shortly after the change.
  </Step>
</Steps>

## Troubleshooting tips

If your webhook isn’t receiving events as expected, here are a few things to double-check. These are the most common reasons developers miss events during setup or testing.

### 🔒 1. Check access permissions

Make sure the connection has access to the object that triggered the event. For example, if a new page is created inside a private page your connection doesn’t have access to, the event won’t be triggered.

### ✅ 2. Confirm capabilities

Some event types require specific capabilities to be enabled for your connection.

For instance, to receive `comment.created` events, your connection must have the "**comment read**" capability selected. Without it, even if your connection has access to the page, the comment event won’t be delivered.

You can view and update your connection’s capabilities in the **Capabilities** section of your connection settings.

### ⏳ 3. Understand aggregated event timing

Not all webhook events are sent immediately. Some, like page.content\_updated, are aggregated to reduce noise from frequent edits (e.g., typing, formatting, moving blocks). This is normal and helps group multiple rapid changes into a single webhook event.

See [Event Delivery ](/reference/webhooks-events-delivery#event-delivery)for a deeper explanation.

<Tip>
  **Tip:**

  If you're testing and expecting an instant response, start with non-aggregated events like `comment.created` or `page.locked`.
</Tip>

### ☑️ Confirm your subscription status

Even if everything else is configured correctly, your webhook won’t receive events unless the subscription is active.

Head to the **Webhooks** tab under your connection settings and make sure your subscription is **active**. If the status shows as **paused**, **pending verification**, or if the subscription was deleted, events won’t be delivered to your endpoint.

## Related resources

* [Event types & delivery](/reference/webhooks-events-delivery) — Full list of supported event types, payload structure, and delivery behavior.
* [Webhook event reference](/reference/webhooks/page-created) — API reference pages for each webhook event type with payload schemas.
