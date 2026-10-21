---
title: "STT Callback"
source: https://developers.deepgram.com/docs/callback.md
path: docs/callback
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# STT Callback

`callback` *string*

Pre-recorded  Streaming:Nova  All available languages

Deepgram’s Callback feature allows you to supply a callback URL to which transcriptions can be returned. When passed, Deepgram will immediately respond with a `request_id` before processing your audio asynchronously.

## Enable Feature

To enable Callback, when you call Deepgram’s API, add a `callback` parameter in the query string and set it to the URL to which you would like transcriptions sent:

`callback=URL`

To transcribe audio from a file on your computer, run the following cURL command in a terminal or your favorite API client.

**`cURL`**

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?callback=URL'
```

## URL Structure

An example URL is `https://example.com/callback`.

Your callback URLs may reference the following protocols:

* For pre-recorded audio: `http` or `https`
* For streaming audio, `http`, `https`, `ws`, or `wss:`

## Authenticating Callback Requests

Authenticate callback requests to confirm that they come from Deepgram. Use Basic Auth where possible. As an alternative, verify a shared secret passed with [Extra Metadata](/docs/extra-metadata).

### Using Basic Auth (recommended)

Embed username-password credentials in the callback URL in the format `https://username:password@example.com`. Deepgram includes these credentials when it sends results to your callback server, which can then reject any request without the expected credentials.

> **Warning**
>
> Only ports 80, 443, 8080, and 8443 are permitted for callbacks.

### Using a Secret in Extra Metadata

Alternatively, use the [`extra`](/docs/extra-metadata) parameter to pass a secret key-value pair with your request. Deepgram returns every `extra` key-value pair in the `metadata.extra` field of the response body it sends to your callback URL.

1. Generate a random URL-safe secret, such as a hex string (`openssl rand -hex 32`), and store it where your callback server can access it. A `+` in the value arrives as a space, so avoid base64 secrets.

2. Add the secret as an `extra` key-value pair when you submit your request:

   **`cURL`**

   ```bash cURL
   curl \
     --request POST \
     --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
     --header 'Content-Type: audio/wav' \
     --data-binary @youraudio.wav \
     --url 'https://api.deepgram.com/v1/listen?callback=https://example.com/callback&extra=callback_secret:YOUR_SECRET_VALUE'
   ```

3. On your callback server, read `metadata.extra.callback_secret` from the response body and confirm it matches the expected secret. Reject any request where the value is missing or does not match.

   **`JSON`**

   ```json JSON
   {
     "metadata": {
       "extra": {
         "callback_secret": "YOUR_SECRET_VALUE"
       }
       ...
     }
     ...
   }
   ```

This method keeps the secret private. Requests to Deepgram's public endpoints use SSL, which encrypts query parameters, including `extra`. Deepgram returns the secret in the body of the callback request, which is also encrypted in transit when your callback URL uses `https://` or `wss://`.

## Results

Depending on the type of submitted audio, the response will vary.

### Pre-recorded Audio

When Deepgram has finished analyzing the audio, it will send a `POST` request to the provided callback URL with an appropriate HTTP status code.

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
  --url 'https://api.deepgram.com/v1/listen?callback=URL&callback_method=put'
```

### Streaming Audio

As Deepgram analyzes the audio, the way in which it sends requests back to the provided callback URL varies:

* If your callback URL begins with `http://` or `https://`, then Deepgram will send `POST` requests to the callback server for each streaming response.
* If your callback URL begins with `ws://` or `wss://`, then Deepgram will establish a WebSocket connection with the callback server and send WebSocket text messages that contain the streaming responses.

> **Warning**
>
> If a WebSocket callback connection is disconnected at any point, the entire real-time transcription stream is killed; this maintains the strong guarantee of a one-to-one relationship between incoming real-time connections and outgoing WebSocket callback connections.

---
