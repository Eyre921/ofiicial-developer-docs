---
title: "Tagging TTS Requests"
source: https://developers.deepgram.com/docs/tts-tagging.md
path: docs/tts-tagging
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Tagging TTS Requests

`tag` *string*

&#x20;Text to Speech Request

&#x20;Text to Speech Stream

&#x20;All available languages

Deepgram's Tagging feature allows you to label your Text-to-Speech API requests for the purpose of identification during usage reporting. You can also apply tags to API Keys; if you do, any tags applied to the API Key running the API request will also be applied to the request itself.

## Enable Feature

To enable Tagging, when you call Deepgram's Text-to-Speech API, add a `tag` parameter in the query string and set it to the tag you would like to recognize:

`tag=VALUE`

To generate speech from text, run the following cURL command in a terminal or your favorite API client. Please be aware that once you have set a tag, you cannot modify it.

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{"text": "Hello, how can I help you today?"}' \
  --url 'https://api.deepgram.com/v1/speak?model=aura-2-thalia-en&tag=VALUE'\
  --output test_audio.wav
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys).

## Filter Requests by Tag

Once applied, you can identify tags associated with API requests returned by the [Get All Requests](/reference/manage/requests/list), [Get Request](/reference/manage/requests/get), and [Get Fields](/reference/manage/billing/fields/get) endpoints.

You can also directly query requests by tag at the [Summarize Usage](/reference/manage/usage/get) endpoint.

```bash cURL
curl \
  --request GET \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'content-type: application/json' \
  --url 'https://api.deepgram.com/v1/projects/PROJECT_ID/usage?tag=TEST'
```

Replace the placeholder `PROJECT_ID` with your Deepgram Console Project ID, `VALUE` with your tag, and `YOUR_DEEPGRAM_API_KEY` with your Deepgram API Key.

## Tag Limits

Tags are limited to 128 characters per tag and 500 unique tags per day.

## Special Considerations

### White Space or Special Characters

If your tag or extra metadata includes spaces or special characters, be sure to URL encode it:

`tag=marketing%20team` or `tag=marketing+team`

### Apply Multiple Instances

To apply multiple tags or multiple extra key-value pairs, submit the query parameter multiple times in your API request:

`tag=marketing&tag=legal`

## Comparison to Extra Metadata

[Extra Metadata](/docs/extra-metadata) is a similar feature to Tagging. Where Tagging is primarily intended for tracking and filtering usage, Extra Metadata is useful for passing data to downstream processing steps.

Below is a comparison table summarizing the main differences between the two features:

|                                                           | Tagging   | Extra Metadata |
| --------------------------------------------------------- | --------- | -------------- |
| Primarily for passing data to downstream processing steps | ❌         | ✅              |
| Primarily for tracking usage                              | ✅         | ❌              |
| Configurable per request                                  | ✅         | ✅              |
| Configurable per API key                                  | ✅         | ❌              |
| Character limit per value                                 | 128 chars | 2048 chars     |
| Can be used to filter usage                               | ✅         | ❌              |
| Can specify a key in a key-value pair                     | ❌         | ✅              |
| Can specify a value in a key-value pair                   | ✅         | ✅              |

---
