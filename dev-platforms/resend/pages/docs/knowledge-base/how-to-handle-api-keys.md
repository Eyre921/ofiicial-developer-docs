---
title: "How to Handle API Keys"
source: https://resend.com/docs/knowledge-base/how-to-handle-api-keys
path: docs/knowledge-base/how-to-handle-api-keys
---

Learn our suggested practices for handling API keys.

<Info>
  For more help creating, deleting, and managing API keys, see the [API Keys
  documentation](/docs/dashboard/api-keys/introduction).
</Info>

## Best Practices

It's crucial you handle your API keys securely. Do not share your API key with others or expose it in the browser or other client-side code.

Here are some general guidelines:

* Store API keys in environment variables.
* Never commit API keys to version control.
* Never hard-code API keys in your code or share them publicly.
* Rotate API keys regularly. If an API key hasn't been used in the last 30 days, consider deleting it to keep your account secure.

<Info>
  When you create an API key in Resend, you can view the key only once. This
  practice helps encourage these best practices.
</Info>

## Key Rotation

Resend API keys do not expire automatically. Keys remain valid until you manually delete them. Resend includes no built-in expiration date or automatic rotation mechanism, but it is a good security practice to rotate keys regularly.

To rotate an API key:

1. **Create a new key** in the [API Keys Dashboard](https://resend.com/api-keys) or [via the API](/docs/api-reference/api-keys/create-api-key) with the same permission level and domain scope as the key you are replacing.
2. **Update your services** to use the new key. Deploy the change to all environments that reference the old key.
3. **Verify the new key is working** by [filtering by API Key on the logs page](https://resend.com/logs) and checking for recent requests.
4. **Delete the old key** once you have confirmed the new key is active across all services.

<Warning>
  Do not delete the old key before the new key is deployed everywhere. Both keys
  will work simultaneously, so ensure your new key is working before deleting
  your old key so you do not experience downtime during the transition. You can
  programmatically [create](/docs/api-reference/api-keys/create-api-key),
  [list](/docs/api-reference/api-keys/list-api-keys), and
  [delete](/docs/api-reference/api-keys/delete-api-key) API keys to rotate keys.
</Warning>

Rotate keys at least every 90 days, or immediately if you suspect a key has been compromised. Resend flags keys unused for 30+ days in the dashboard to help you identify keys to review or delete.
