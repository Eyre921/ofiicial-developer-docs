---
title: "Use Provider-Specific Video Options"
source: https://openrouter.ai/docs/cookbook/video-generation/provider-specific-video-options.md
path: docs/cookbook/video-generation/provider-specific-video-options
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Provider-Specific Video Options

> Inspect allowed passthrough parameters and send provider-specific video controls safely

Use this guide when you need to add video model controls that aren't part of OpenRouter's normalized video schema.

By the end, your implementation should inspect a model's allowed passthrough parameters and send one through `provider.options`.

> [!TIP]
>
> For reusable agent knowledge across projects, install the [openrouter-video skill](https://github.com/OpenRouterTeam/skills/tree/main/skills/openrouter-video).

## Before you start

You need:

* Node.js 20 or newer
* An OpenRouter API key available as `OPENROUTER_API_KEY` only when you submit the video job
* A target video model for the provider-specific options you want to send

> [!TIP]
>
> If you aren't already targeting a specific provider model, read [Choose a Video Generation Model](https://openrouter.ai/docs/cookbook/video-generation/choose-video-model.md) first. It helps you pick one based on clip duration, output shape, input type, audio, provider controls, and cost.

Use the API reference pages as the source of truth for exact fields:

* [Create video generation request](https://openrouter.ai/docs/api/api-reference/video-generation/submit-a-video-generation-request.md)
* [List video generation models](https://openrouter.ai/docs/api/api-reference/video-generation/list-all-video-generation-models.md)
* [TypeScript SDK video generation reference](https://openrouter.ai/docs/client-sdks/typescript/sdks/videogeneration/README.md)

Provider-specific options can change by model and provider. Always check `allowed_passthrough_parameters` before relying on one.

> [!WARNING]
>
> Submitting `POST /api/v1/videos` starts a real video generation job and may spend OpenRouter credits.

## Step 1: Inspect allowed passthrough parameters

Start by reading `allowed_passthrough_parameters` from the selected model. This keeps provider-specific controls behind a model metadata check instead of hard-coding unsupported request keys.

Example metadata check:

```js lines theme={null}
const response = await fetch("https://openrouter.ai/api/v1/videos/models");

if (!response.ok) {
  throw new Error(await response.text());
}

const { data } = await response.json();
const models = data;
const veo = models.find(
  (model) => model.id === "google/veo-3.1-lite",
);

if (!veo) {
  throw new Error("google/veo-3.1-lite was not found in the video model list.");
}

console.log(veo.allowed_passthrough_parameters);
```

```python title="Python" lines theme={null}
import json

import requests

response = requests.get("https://openrouter.ai/api/v1/videos/models")

if not response.ok:
    raise RuntimeError(response.text)

models = response.json()["data"]
veo = next(
    (model for model in models if model["id"] == "google/veo-3.1-lite"),
    None,
)

if veo is None:
    raise RuntimeError("google/veo-3.1-lite was not found in the video model list.")

print(json.dumps(veo["allowed_passthrough_parameters"], indent=2))
```

```go title="Go" lines theme={null}
resp, err := http.Get("https://openrouter.ai/api/v1/videos/models")
if err != nil {
	log.Fatal(err)
}
defer resp.Body.Close()

if resp.StatusCode != http.StatusOK {
	body, _ := io.ReadAll(resp.Body)
	log.Fatal(string(body))
}

var payload struct {
	Data []struct {
		ID                           string   `json:"id"`
		AllowedPassthroughParameters []string `json:"allowed_passthrough_parameters"`
	} `json:"data"`
}
if err := json.NewDecoder(resp.Body).Decode(&payload); err != nil {
	log.Fatal(err)
}

found := false
for _, model := range payload.Data {
	if model.ID == "google/veo-3.1-lite" {
		found = true
		out, err := json.MarshalIndent(model.AllowedPassthroughParameters, "", "  ")
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(string(out))
		break
	}
}

if !found {
	log.Fatal("google/veo-3.1-lite was not found in the video model list.")
}
```

```bash title="cURL" lines theme={null}
curl -sSf https://openrouter.ai/api/v1/videos/models \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  | jq -e '.data[] | select(.id == "google/veo-3.1-lite") | .allowed_passthrough_parameters'

```

Example output:

```json lines theme={null}
[
  "personGeneration",
  "aspectRatio",
  "negativePrompt",
  "conditioningScale",
  "enhancePrompt"
]
```

For example, `google/veo-3.1-lite` may expose passthrough controls such as `negativePrompt`, `enhancePrompt`, `personGeneration`, or `conditioningScale`. OpenRouter lists supported parameter names; check the provider docs for valid values when a parameter has an enum.

Before submitting a paid job, assert that every passthrough key you plan to send is allowed for the selected model:

```js lines theme={null}
const providerParameters = {
  negativePrompt: "blurry, low quality, distorted petals",
  enhancePrompt: true,
};

const unsupportedParameters = Object.keys(providerParameters).filter(
  (key) => !veo.allowed_passthrough_parameters?.includes(key),
);

if (unsupportedParameters.length > 0) {
  throw new Error(
    `Unsupported passthrough parameters: ${unsupportedParameters.join(", ")}`,
  );
}

console.log("All provider parameters are supported.");
```

```python title="Python" lines theme={null}
provider_parameters = {
    "negativePrompt": "blurry, low quality, distorted petals",
    "enhancePrompt": True,
}

allowed = veo.get("allowed_passthrough_parameters") or []
unsupported_parameters = [key for key in provider_parameters if key not in allowed]

if unsupported_parameters:
    raise RuntimeError(
        f"Unsupported passthrough parameters: {', '.join(unsupported_parameters)}"
    )

print("All provider parameters are supported.")

```

```go title="Go" lines theme={null}
providerParameters := map[string]any{
	"negativePrompt": "blurry, low quality, distorted petals",
	"enhancePrompt":  true,
}

var unsupportedParameters []string
for key := range providerParameters {
	if !slices.Contains(veo.AllowedPassthroughParameters, key) {
		unsupportedParameters = append(unsupportedParameters, key)
	}
}

if len(unsupportedParameters) > 0 {
	log.Fatalf("Unsupported passthrough parameters: %s", strings.Join(unsupportedParameters, ", "))
}

fmt.Println("All provider parameters are supported.")
```

```bash title="cURL" lines theme={null}
PROVIDER_PARAMETERS='{
  "negativePrompt": "blurry, low quality, distorted petals",
  "enhancePrompt": true
}'

ALLOWED_PARAMS=$(curl -sSf https://openrouter.ai/api/v1/videos/models \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  | jq -c '.data[] | select(.id == "google/veo-3.1-lite") | .allowed_passthrough_parameters')

if [ -z "$ALLOWED_PARAMS" ]; then
  echo "google/veo-3.1-lite was not found in the video model list." >&2
  exit 1
fi

UNSUPPORTED=$(jq -rn \
  --argjson params "$PROVIDER_PARAMETERS" \
  --argjson allowed "$ALLOWED_PARAMS" \
  '$params | keys - ($allowed // []) | join(", ")')

if [ -n "$UNSUPPORTED" ]; then
  echo "Unsupported passthrough parameters: $UNSUPPORTED" >&2
  exit 1
fi

echo "All provider parameters are supported."
```

Metadata assertion output:

```text lines theme={null}
All provider parameters are supported.
```

## Step 2: Add provider options to the video request

Provider options are keyed by provider slug. Only the options for the matched provider are forwarded. For the Google Vertex video endpoint, use the `google-vertex` provider slug.

Google Veo models are the only video models that nest options in a `parameters` object. Other video models, including other Google video models, take their allowed passthrough keys directly under the slug of the provider the request is routed to. A `parameters` object sent to them is not forwarded, and Runway video upscale rejects any provider options. For example, Seedance 2.0 is served by the Seed provider, so it takes `watermark` directly under the `seed` slug:

```json lines theme={null}
{
  "provider": {
    "options": {
      "seed": {
        "watermark": false
      }
    }
  }
}
```

A Seedance request routed to BytePlus uses the `byteplus` slug instead of `seed`.

Example request shape:

```js expandable lines theme={null}
const apiKey = process.env.OPENROUTER_API_KEY;

if (!apiKey) {
  throw new Error("Set OPENROUTER_API_KEY before submitting a video job.");
}

const response = await fetch("https://openrouter.ai/api/v1/videos", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${apiKey}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model: "google/veo-3.1-lite",
    prompt:
      "A 4-second time-lapse of a white orchid blooming on a dark tabletop, macro lens, gentle studio light",
    duration: 4,
    resolution: "720p",
    aspect_ratio: "16:9",
    generate_audio: false,
    provider: {
      options: {
        "google-vertex": {
          parameters: providerParameters,
        },
      },
    },
  }),
});

if (!response.ok) {
  throw new Error(await response.text());
}

console.log(await response.json());
```

The submit call returns the job fields immediately. In the QA run, the submitted job later completed and downloaded with this final summary:

```json lines theme={null}
{
  "id": "2hAwXrT31ZpCI8MsjBEe",
  "status": "completed",
  "polling_url": "https://openrouter.ai/api/v1/videos/2hAwXrT31ZpCI8MsjBEe",
  "downloaded_path": "provider-options.mp4",
  "downloaded_bytes": 794331
}
```

To wait for the playable MP4, use the polling and download helper from [Generate and Download a Video from Text](https://openrouter.ai/docs/cookbook/video-generation/text-to-video.md) after submission.

## Step 3: Keep a fallback without passthrough options

If your app can route across multiple video models, keep the normalized request separate from model-specific options:

```js expandable lines theme={null}
const baseRequest = {
  prompt: "A short cinematic product shot of a white orchid blooming",
  duration: 4,
  resolution: "720p",
  aspect_ratio: "16:9",
};

const selectedModel = {
  id: "google/veo-3.1-lite",
};

const requestBody =
  selectedModel.id === "google/veo-3.1-lite"
    ? {
        ...baseRequest,
        model: selectedModel.id,
        provider: {
          options: {
            "google-vertex": {
              parameters: {
                negativePrompt: "blurry, low quality",
              },
            },
          },
        },
      }
    : {
        ...baseRequest,
        model: selectedModel.id,
      };
```

```python title="Python" lines theme={null}
base_request = {
    "prompt": "A short cinematic product shot of a white orchid blooming",
    "duration": 4,
    "resolution": "720p",
    "aspect_ratio": "16:9",
}

selected_model = {
    "id": "google/veo-3.1-lite",
}

if selected_model["id"] == "google/veo-3.1-lite":
    request_body = {
        **base_request,
        "model": selected_model["id"],
        "provider": {
            "options": {
                "google-vertex": {
                    "parameters": {
                        "negativePrompt": "blurry, low quality",
                    },
                },
            },
        },
    }
else:
    request_body = {
        **base_request,
        "model": selected_model["id"],
    }
```

```go title="Go" lines theme={null}
baseRequest := map[string]any{
	"prompt":       "A short cinematic product shot of a white orchid blooming",
	"duration":     4,
	"resolution":   "720p",
	"aspect_ratio": "16:9",
}

selectedModel := struct{ ID string }{
	ID: "google/veo-3.1-lite",
}

requestBody := map[string]any{"model": selectedModel.ID}
maps.Copy(requestBody, baseRequest)

if selectedModel.ID == "google/veo-3.1-lite" {
	requestBody["provider"] = map[string]any{
		"options": map[string]any{
			"google-vertex": map[string]any{
				"parameters": map[string]any{
					"negativePrompt": "blurry, low quality",
				},
			},
		},
	}
}
```

```bash title="cURL" lines theme={null}
BASE_REQUEST='{
  "prompt": "A short cinematic product shot of a white orchid blooming",
  "duration": 4,
  "resolution": "720p",
  "aspect_ratio": "16:9"
}'

SELECTED_MODEL="google/veo-3.1-lite"

if [ "$SELECTED_MODEL" = "google/veo-3.1-lite" ]; then
  REQUEST_BODY=$(jq -n --argjson base "$BASE_REQUEST" --arg model "$SELECTED_MODEL" \
    '$base + {model: $model, provider: {options: {"google-vertex": {parameters: {negativePrompt: "blurry, low quality"}}}}}')
else
  REQUEST_BODY=$(jq -n --argjson base "$BASE_REQUEST" --arg model "$SELECTED_MODEL" \
    '$base + {model: $model}')
fi
```

Request shape for `google/veo-3.1-lite`:

```json lines theme={null}
{
  "prompt": "A short cinematic product shot of a white orchid blooming",
  "duration": 4,
  "resolution": "720p",
  "aspect_ratio": "16:9",
  "model": "google/veo-3.1-lite",
  "provider": {
    "options": {
      "google-vertex": {
        "parameters": {
          "negativePrompt": "blurry, low quality"
        }
      }
    }
  }
}
```

## Check your work

The metadata assertion should pass before you submit a job. If you submit the request, it should return a video job. If the provider option is invalid for the selected model, remove it or re-check the current `allowed_passthrough_parameters` list. To verify the final output, poll the returned `polling_url` until `completed`, then download the MP4.

