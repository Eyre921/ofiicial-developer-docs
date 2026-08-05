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

&#x20;Pre-recorded

&#x20;Streaming:Nova

&#x20;All available languages

Deepgram’s Callback feature allows you to supply a callback URL to which transcriptions can be returned. When passed, Deepgram will immediately respond with a `request_id` before processing your audio asynchronously.

## Enable Feature

To enable Callback, when you call Deepgram’s API, add a `callback` parameter in the query string and set it to the URL to which you would like transcriptions sent:

`callback=URL`

To transcribe audio from a file on your computer, run the following cURL command in a terminal or your favorite API client.

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

Authentication ensures the security and integrity of callback requests. There are two main methods for authenticating callback requests: using Basic Auth and utilizing the dg-token request header.

### Using Basic Auth

You may embed username-password authentication credentials in the callback URL in the format `https://username:[email protected]`. However, it's important to note that only ports 80, 443, 8080, and 8443 are permitted for callbacks.

Only ports 80, 443, 8080, and 8443 are permitted for callbacks.

### Using the `dg-token` Request Header

Alternatively, the callback request itself contains a header named dg-token. This header is automatically set to the API Key Identifier associated with the API Key used to submit the original request. This method provides a secure and straightforward means of authentication.

## Results

Depending on the type of submitted audio, the response will vary.

### Pre-recorded Audio

When Deepgram has finished analyzing the audio, it will send a `POST` request to the provided callback URL with an appropriate HTTP status code.

If the HTTP status code of the response to the callback `POST` request is unsuccessful (not 200-299), Deepgram will retry the callback up to 10 times with a 30 second delay between attempts.

## Using `CallBack_Method`

To enable the Callback Method, include the `callback_method` parameter in the query string. By default, the method supports `POST`, but you can specify `PUT` instead.

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

If a WebSocket callback connection is disconnected at any point, the entire real-time transcription stream is killed; this maintains the strong guarantee of a one-to-one relationship between incoming real-time connections and outgoing WebSocket callback connections.

***
