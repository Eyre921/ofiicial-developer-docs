---
title: "Summarization"
source: https://developers.deepgram.com/docs/text-summarization.md
path: docs/text-summarization
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Summarization

Deepgram API Playground


Try this feature out in our API Playground.

\


`summarize` *boolean*   Default: `false`

&#x20;Text Intelligence

&#x20;English (all available regions)

Summarization accepts an input text and analyzes the text. It then summarizes the content of the submitted text and returns a brief summary in the JSON response.

```json JSON
 "results": {
    "summary": {
      "text": "Jake calls the Honda dealership and speaks with Josh about the new Honda Civic 2023. Jake schedules a test drive for the hybrid model on Friday and provides his contact information.Josh confirms the appointment and tells Jake to call if he has any further questions."
    }
  }
```

## Enable Feature

To enable Summarization, use the following parameter in the query string when you call Deepgram’s `/read` endpoint :

`summarize=true`

### Basic Text Request

To analyze text from a file on your computer, run the following curl command in a terminal or your favorite API client.

```bash cURL
 curl -vX POST \
	-H "Authorization: Token YOUR_DEEPGRAM_API_KEY" \
	-H "Content-Type: application/json" \
	-d '{"text": "YOUR_TEXT_HERE"}' \
	"https://api.deepgram.com/v1/read?summarize=true&language=en"
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

### Basic URL Request

To analyze text from a hosted file, run the following curl command in a terminal or your favorite API client. (Try testing it out with the hosted file [https://static.deepgram.com/examples/aura.txt](https://static.deepgram.com/examples/aura.txt))

```bash cURL
curl -vX POST \
 -H "Authorization: Token YOUR_DEEPGRAM_API_KEY" \
 -H "Content-Type: application/json" \
 -d '{"url": "https://YOUR_FILE_URL.txt"}' \
 "https://api.deepgram.com/v1/read?summarize=true&language=en"
```

Read our [Text Intelligence Getting Started guide](/docs/text-intelligence), which will walk you through making a basic text request and a basic URL request with the Deepgram SDKs.

### Query Parameters

| Parameter   | Value  | Type    | Description                                                                                                                                                                   |
| ----------- | ------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `summarize` | `true` | boolean | Enables summarization. The output response will include a `summary` object, and within that object will be a `text`property that contains a short summary of the entire text. |
| `language`  | `en`   | string  | The language of your input text (Only English is supported at this time)                                                                                                      |

Summarization requires a minimum of greater than 50 words for summarization. For shorter inputs (less than 50 words), the original input will be returned. In this case, no tokens in or out are billed as summarization usage.

## Analyze Response

When the file is finished processing, you’ll receive a JSON response that has the following basic structure:

```json JSON
{
  "metadata": {
    "request_id": "6ab1afe9-da49-4688-86f5-ae2fde420ad4",
    "created": "2023-11-28T04:49:56.034Z",
    "language": "en",
    "summary_info": {
      "model_uuid": "67875a7f-c9c4-48a0-aa55-5bdb8a91c34a",
      "input_tokens": 103,
      "output_tokens": 33
    }
  },
  "results": {
    "summary": {
      "text": "Jake calls the Honda dealership and speaks with Josh about the new Honda Civic 2023. Jake schedules a test drive for the hybrid model on Friday and provides his contact information. Josh confirms the appointment and tells Jake to call if he has any further questions."
    }
  }
}
```

The `summary` object contains:

* `text`: Short summary of the audio being summarized.

## API Error Responses

### Unsupported Language

**Status** 400

If you request Summarization with an unsupported language by specifying a language code such as `summarize=true&language=es` or `summarize=true&detect_language=true` where the detected language is unsupported, you will get the error message below.

```json JSON
{
  "err_code":"INVALID_QUERY_PARAMETER",
  "err_msg":"Request specified unsupported language: <language_name>. Only English is supported.",
  "request_id":"XXXX"
}
```

### Token Limit Exceeded

**Status** 400

If the request's input length exceeded the 150k token rate limit per request, you will get the error message below.

```json JSON
{
  "err_code": "TOKEN_LIMIT_EXCEEDED",
  "err_msg": "Text input for <api_name> currently supports up to 150K tokens. Please revise your text input to fit within the defined token limit. For more information, please visit our API documentation.",
  "request_id": "XXXX"
}
```

### Missing Query Parameter

**Status** 400

If the request sent contained only the feature parameter (`summarize`) but not the `language` parameter, you will receive this error.

```json JSON
{
  "err_code":"INVALID_QUERY_PARAMETER",
  "err_msg":"Failed to deserialize query parameters: missing field `language`",
  "request_id":"XXX"
}
```
