---
title: "Official models"
source: https://replicate.com/docs/topics/models/official-models.md
path: docs/topics/models/official-models
---

We maintain [over 100 official models](https://replicate.com/collections/official) that are always on, predictably priced, and have a stable API.

Official models are just like other models on Replicate, but with a few extra benefits:

*   **Always on**: Official models are always warm and ready to respond to requests, so you can run them without worrying about cold boots.
*   **Stable API**: The input and output API for every official model is stable. You can reliably use official models without having to worry about breaking changes or unexpected changes in the API.
*   **Predictable pricing**: Unlike other models which are [priced by the hardware they use and the amount of time they run](https://replicate.com/pricing), official models are priced by predictable metrics, like the number of output image, seconds of video output, number of input and output tokens, etc.
*   **Actively maintained**: Replicate maintains the official models, and we work with the authors to make sure they’re high quality. We also make sure they’re always up to date with the latest version of the model.

[](#api)API
-----------

The way you call official models is a little different from other models. If you’re using a Replicate library like the [JavaScript](https://github.com/replicate/replicate-javascript) or [Python](https://github.com/replicate/replicate-python) client, you don’t need to specify a version.

Here’s an example for running [black-forest-labs/flux-1.1-pro](https://replicate.com/black-forest-labs/flux-1.1-pro) in Node.js. Notice that the `model` identifer is just the owner and name (`black-forest-labs/flux-1.1-pro`), without a version:

```tsx
import Replicate from "replicate";
const replicate = new Replicate();
const model = "black-forest-labs/flux-1.1-pro";
const input = { prompt: "A t-rex on a skateboard looking cool" };
const output = await replicate.run(model, { input });
console.log(output);
```

If you’re using the HTTP API to run an official model, you use the `POST /models/<owner>/<name>/predictions` endpoint and you don’t need to specify a version. For example:

```bash
curl https://api.replicate.com/v1/models/black-forest-labs/flux-1.1-pro/predictions \
	--request POST \
	--header "Authorization: Bearer $REPLICATE_API_TOKEN" \
	--header "Content-Type: application/json" \
	--header "Prefer: wait" \
	--data @- <<'EOM'
{
	"input": {
      "prompt": "A t-rex on a skateboard looking cool"
	}
}
EOM
```

Nothing has changed about how you run other models. The best way to find out how to run a model is [the API documentation on a model](https://replicate.com/black-forest-labs/flux-dev/api).

[](#pricing)Pricing
-------------------

Instead of being charged by the amount of time a model runs, you’re charged by output (or in some cases, input). For example, [black-forest-labs/flux-1.1-pro](https://replicate.com/black-forest-labs/flux-1.1-pro) is charged for each image it generates, but for other models this might be things like the number of tokens or the duration of a video.

You can find out about each model’s pricing [on the pricing section of the model](https://replicate.com/black-forest-labs/flux-1.1-pro#pricing).

[](#models)Models
-----------------

Replicate maintains [over 100 official models](https://replicate.com/collections/official), including:

*   [bytedance/seedance-1-pro](https://replicate.com/bytedance/seedance-1-pro)
*   [bytedance/seedance-1-lite](https://replicate.com/bytedance/seedance-1-lite)
*   [kwaiyeij/kling-v2.1](https://replicate.com/kwaiyeij/kling-v2.1)
*   [google/veo-3](https://replicate.com/google/veo-3)
*   [google/imagen-4-ultra](https://replicate.com/google/imagen-4-ultra)
*   [replicate/fast-flux-trainer](https://replicate.com/replicate/fast-flux-trainer)
*   [black-forest-labs/flux-kontext-pro](https://replicate.com/black-forest-labs/flux-kontext-pro)
*   [black-forest-labs/flux-kontext-max](https://replicate.com/black-forest-labs/flux-kontext-max)
*   [ideogram-ai/ideogram-v3-turbo](https://replicate.com/ideogram-ai/ideogram-v3-turbo)
*   [minimax/video-01](https://replicate.com/minimax/video-01)
*   [meta/meta-llama-3-70b](https://replicate.com/meta/meta-llama-3-70b)
*   [recraft-ai/recraft-v3](https://replicate.com/recraft-ai/recraft-v3)

For the full list, [take a look at the official models collection](https://replicate.com/collections/official).

[](#adding-new-official-models)Adding new official models
---------------------------------------------------------

The collection of official models is always growing. If you know of a model that you think should be official, please [let us know](https://replicate.com/contact).
