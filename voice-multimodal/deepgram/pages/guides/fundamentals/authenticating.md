---
title: "Authenticating"
source: https://developers.deepgram.com/guides/fundamentals/authenticating.md
path: guides/fundamentals/authenticating
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Authenticating

If you need to create and distribute short-lived tokens for API requests, you can use the [token-based Auth API](/reference/auth/tokens/grant).

Deepgram's API uses API keys to authenticate requests. You can view and manage your API keys in the [Deepgram Console](https://console.deepgram.com) or through the [Deepgram API](/reference/deepgram-api-overview).

Your API keys grant many privileges, so be sure to keep them secure. Do not share your secret API keys in publicly accessible areas such as GitHub or client-side code.

For best results, use different API keys for testing and production. To help filter usage, you can also use different API keys for different consumers or teams at your organization.

If you still need an API key, you can [sign up to Deepgram today for free](https://console.deepgram.com/signup)!

## Authenticating with the API Key

Once you have created an API key, you can use it as credentials to call Deepgram's API.

Send requests to the API with an `Authorization` header that references your project's API key:

```text Text
Authorization: Token YOUR_DEEPGRAM_API_KEY
```

All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests made without authentication will also fail.

## Test Request

A quick test to see if your key is validating correctly, is to make a request to the `/auth/token` endpoint on our API. This will return an `invalid credentials` error if your key is invalid, and a `JSON` response with details about your key if it's valid.

```bash cURL
curl https://api.deepgram.com/v1/auth/token \
  -H "Authorization: Token YOUR_DEEPGRAM_API_KEY"
```

## Additional Keys

To create additional API keys, be sure that the API key you are using to authenticate your request has been assigned either the `administrator` role or the following permissions: `keys:read`, `keys:write`.

Make sure you are sending API requests over HTTPS. Calls made over plain HTTP will fail. API requests made without authentication will also fail.

---
