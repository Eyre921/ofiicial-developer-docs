---
title: "Summarization"
source: https://developers.deepgram.com/docs/summarization.md
path: docs/summarization
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Summarization

Deepgram API Playground
Try this feature out in our API Playground.

<br />

`summarize` *string*.

&#x20;Pre-recorded

&#x20;Streaming:Nova

&#x20;English (all available regions)

Deepgram’s Summarization feature summarizes the content of the submitted audio and returns a brief summary in the JSON response.

## Enable Feature

To enable Summarization, use the following parameter in the query string when you call Deepgram's `/listen` endpoint:

`summarize=v2`

You can also use `summarize=true`, which will return the V2 response structure.

To transcribe audio from a file on your computer, run the following curl command in a terminal or your favorite API client.

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?summarize=v2'
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

### Query Parameters

| Parameter   | Value   | Type    | Description                                                                                                                                                                    |
| ----------- | ------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `summarize` | `v2`    | string  | Enables summarization. The output response will include a single object with a result and short summary of the entire audio. It will generate one summary across all channels. |
| `summarize` | `true`  | boolean | Enables summarization. Returns the same V2 response structure as `summarize=v2`.                                                                                               |
| `summarize` | `false` | boolean | Disables the summarization feature.                                                                                                                                            |

Summarization requires a minimum of greater than 50 words for summarization. For shorter inputs (less than 50 words), the original input will be returned. In this case, no tokens in or out are billed as summarization usage.

## Analyze Response

When the file is finished processing, you’ll receive a JSON response that has the following basic structure:

```json JSON
{
  "metadata": {...},
  "results": {
        "channels": [
            {
                "alternatives": [...]
            }
        ],
        "summary": {
            "result":"success",
            "short": "Jake calls the Honda dealership and speaks with Josh about the new Honda Civic 2023. Jake schedules a test drive for the hybrid model on Friday and provides his contact information.Josh confirms the appointment and tells Jake to call if he has any further questions."
        }
  }
}
```

The `summary` object contains:

* `result`: Status of the request (success | failure).
* `short`: Short summary of the audio being summarized.

This summarization feature produces one summary across all channels so that the `summary` field ranks at the same place in the JSON response as the `channels` array.

### API Error and Warning Response

#### Error

If you request Summarization with an unsupported language by specifying a language code such as `summarize=v2&language=es`, you will get an error message like the one below.

```json JSON
{
    "err_code": "Bad Request",
    "err_msg": "Summarization v2 not supported for non-English languages",
    "request_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

#### Warning

If you request Summarization with automatic language detection such as `summarize=v2&detect_language=true`, where the detected language is unsupported (Spanish, for example), you will get the response, including a transcript and a warning object.

```json JSON
"warnings": [
    {
      "parameter": "TEXT",
      "type": "unsupported_language",
      "message": "TEXT"
    }
]
```

| Warning Name           | Warning Message                                                  |
| ---------------------- | ---------------------------------------------------------------- |
| `unsupported_language` | Feature isn't supported with the specified or detected language. |

**Example Warning**

Here is an example of the JSON structure of a request with warning object:

```json JSON
{
 "metadata": {
...
       },
       "warnings": [
           {
            "parameter": "summarize",
            "type": "unsupported_language",
            "message": "Summarization isn’t supported for the detected language."
           }
       ],
   },
 "results": {
       "channels": [
            {
                "alternatives": [...]
            }
        ],
        "summary":
          {
            "result": "failure",
            "short": "The summarization feature is currently only available in English. Please check out our API documentation for more details."
      }
    }
}
```
