---
title: "Model Metadata"
source: https://developers.deepgram.com/guides/fundamentals/model-metadata.md
path: guides/fundamentals/model-metadata
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Model Metadata

The Models endpoint allows users to efficiently query all available public models or private models and determine which models they have access to.

For additional details on these API endpoints refer to our [API Reference](/reference/deepgram-api-overview)

## Enable Feature

### GET /models

Returns metadata on all the latest public models. If multiple versions exist, the latest model version is returned. If you wish to return all models you can use the `include_outdated=true` parameter in your request.\`

If you need to get information on a custom model (non-public) you can use the Get Project Models endpoints.

#### Request

```bash cURL
curl --location 'https://api.deepgram.com/v1/models' \
```

For this endpoint you **do not** need to provide your [Deepgram API Key](/docs/create-additional-api-keys).

#### Result

```json JSON
{
  "stt": [
  	{
      "name": "general",
      "canonical_name": "nova-3-general",
      "architecture": "nova3",
      "languages": [
        "en",
        "en-US"
      ],
      "version": "2025-01-09.0",
      "uuid": "bf05427e-a1f1-4ced-a976-38b2f3533d8d",
      "batch": false,
      "streaming": true,
      "formatted_output": false
    },
    // ... other STT models
  ],
  "tts": [
    {
      "name": "angus",
      "canonical_name": "aura-angus-en",
      "architecture": "aura",
      "languages": [
        "en",
        "en-IE"
      ],
      "version": "2024-11-19.0",
      "uuid": "b50880e3-4e2e-4e53-ba27-ea0472bf2cf4",
      "metadata": {
        "accent": "Irish",
        "color": "#BA80F5",
        "image": "https://static.deepgram.com/examples/avatars/angus.jpg",
        "sample": "https://static.deepgram.com/examples/voices/angus.wav",
        "tags": [
          "masculine"
        ]
      }
    },
    // ... other TTS models
  ]
}
```

### GET /projects/\{project}/models

Returns metadata on all the latest models that a specific project has access to, including non-public models. If multiple versions exist, the latest model version is returned. If you wish to return all models you can use the `include_outdated=true` parameter in your request.

#### Request

```bash cURL
curl --location 'https://api.deepgram.com/v1/projects/YOUR_PROJECT_ID/models' \
--header 'Authorization: Token YOUR_DEEPGRAM_API_KEY'
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys) and replace `YOUR_PROJECT_ID`with your [Deepgram Project ID](/guides/deep-dives/managing-projects).

#### Result

```json JSON
{
  "stt": [
    {
      "name": "general",
      "canonical_name": "nova-3-general",
      "architecture": "nova3",
      "languages": [
        "en",
        "en-US"
      ],
      "version": "2025-01-09.0",
      "uuid": "bf05427e-a1f1-4ced-a976-38b2f3533d8d",
      "batch": false,
      "streaming": true,
      "formatted_output": false
    },
		... additional STT Models.
  ],
  "tts": [
    {
      "name": "angus",
      "canonical_name": "aura-angus-en",
      "architecture": "aura",
      "languages": [
        "en",
        "en-IE"
      ],
      "version": "2024-11-19.0",
      "uuid": "b50880e3-4e2e-4e53-ba27-ea0472bf2cf4",
      "metadata": {
        "accent": "Irish",
        "color": "#BA80F5",
        "image": "https://static.deepgram.com/examples/avatars/angus.jpg",
        "sample": "https://static.deepgram.com/examples/voices/angus.wav",
        "tags": [
          "masculine"
        ]
      }
    },
		... additional TTS Models.
  ]
}
```

### GET /models/\{modelId}

Returns the metadata for a specific model. If the model is not found a `404` error is returned. This endpoint works for public models only.

#### Request

```bash cURL
curl --location 'https://api.deepgram.com/v1/models/MODEL_UUID' \
```

For this endpoint you **do not** need to provide your [Deepgram API Key](/docs/create-additional-api-keys).

#### Results

```json JSON
{
    "name": "angus",
    "canonical_name": "aura-angus-en",
    "architecture": "aura",
    "language": ["en"],
    "version": "2024-03-28.0",
    "uuid": "af6e9977-99f6-4d8f-b6f5-dfdf6fb6e291",
    "metadata": {
        "accent": "Irish",
        "color": "#BA80F5",
        "tags": ["masculine"],
        "image": "https://static.deepgram.com/examples/avatars/angus.jpg",
        "sample": "https://static.deepgram.com/examples/voices/angus.wav"
    }
}
```

### GET /projects/\{project}/models/\{modelId}

Returns the metadata for a specific model that a particular project has access to. If the model is not found a `404` error is returned. This endpoint works for both public models and models accessible by the specified project.

#### Request

```bash cURL
curl --location 'https://api.deepgram.com/v1/projects/YOUR_PROJECT_ID/models/MODEL_UUID' \
--header 'Authorization: Token YOUR_DEEPGRAM_API_KEY'
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys) and replace `YOUR_PROJECT_ID`with your [Deepgram Project ID](/guides/deep-dives/managing-projects) and replace `MODEL_UUID`with the specific Model UUID.

#### Results

```json JSON
{
    "name": "angus",
    "canonical_name": "aura-angus-en",
    "architecture": "aura",
    "language": ["en"],
    "version": "2024-03-28.0",
    "uuid": "af6e9977-99f6-4d8f-b6f5-dfdf6fb6e291",
    "metadata": {
        "accent": "Irish",
        "color": "#BA80F5",
        "tags": ["masculine"],
        "image": "https://static.deepgram.com/examples/avatars/angus.jpg",
        "sample": "https://static.deepgram.com/examples/voices/angus.wav"
    }
}
```

---
