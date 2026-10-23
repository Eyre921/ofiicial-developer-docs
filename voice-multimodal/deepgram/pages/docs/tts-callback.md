---
title: "TTS Callback"
source: https://developers.deepgram.com/docs/tts-callback.md
path: docs/tts-callback
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# TTS Callback

`callback` *string*

Text to Speech Request  Text to Speech Stream

Deepgram’s Callback feature allows you to supply a callback URL to which generated text-to-speech audio can be returned. When passed, Deepgram will immediately respond with a `request_id` before processing your text asynchronously.

## Enable Feature

To enable Callback, when you call Deepgram’s API, add a `callback` parameter in the query string and set it to the URL to which you would like transcriptions sent:

`callback=URL`

To synthesize text-to-speech and generate an audio file, run the following cURL command in a terminal or your favorite API client:

**`cURL`**

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{"text": "Hello, how can I help you today?"}'
  --url 'https://api.deepgram.com/v1/speak?model=aura-2-thalia-en&callback=URL'
```

## URL Structure

An example URL is `https://example.com/callback`.

Your callback URLs may reference the `http` or `https` protocols.

## Authenticating Callback Requests

Authenticate callback requests to confirm that they come from Deepgram. Use Basic Auth: embed username-password credentials in the callback URL in the format `https://username:password@example.com`. Deepgram includes these credentials when it sends results to your callback server, which can then reject any request without the expected credentials.

> **Warning**
>
> Only ports 80, 443, 8080, and 8443 are permitted for callbacks.

## Results

When Deepgram has finished analyzing the text, it will send a `POST` request to the provided callback URL with an appropriate HTTP status code.

If the HTTP status code of the response to the callback `POST` request is unsuccessful (not 200-299), Deepgram will retry the callback up to 10 times with a 30 second delay between attempts.

## Using `CallBack_Method`

To enable the Callback Method, include the `callback_method` parameter in the query string. By default, the method supports `POST`, but you can specify `PUT` instead.

**`cURL`**

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: text/plain' \
  --data 'Your Text.' \
  --url 'https://api.deepgram.com/v1/speak?callback=URL&callback_method=put'
```

---
