---
title: "Hugging Face Inference quickstart"
source: https://docs.together.ai/docs/quickstart-using-hugging-face-inference
path: docs/quickstart-using-hugging-face-inference
---

Use Together models with Hugging Face Inference.

This documentation provides a concise guide for developers to integrate and use Together AI inference capabilities via the Hugging Face ecosystem.

## Authentication and billing

When using Together AI through Hugging Face, you have two options for authentication:

* Direct Requests: Use your Together AI API key in your Hugging Face user account settings. In this mode, inference requests are sent directly to Together AI, and billing is handled by your Together AI account.
* Routed Requests: If you don't configure a Together AI API key, your requests will be routed through Hugging Face. In this case, you can use a Hugging Face token for authentication. Billing for routed requests is applied to your Hugging Face account at standard provider API rates. You don’t need an account on Together AI to do this. Use your HF one!

To add a Together AI API key to your Hugging Face settings, follow these steps:

1. Go to your [Hugging Face user account settings](https://huggingface.co/settings/inference-providers).
2. Locate the "Inference Providers" section.
3. You can add your API keys for different providers, including Together AI
4. You can also set your preferred provider order, which will influence the display order in model widgets and code snippets.

<Info>
  You can search for all [Together AI models](https://huggingface.co/models?inference_provider=together\&sort=trending) on the hub and directly try out the available models via the Model Page widget too.
</Info>

## Usage examples

The examples below demonstrate how to interact with various models using Python and JavaScript.

First, ensure you have the `huggingface_hub` library installed (version v0.29.0 or later):

<CodeGroup>
  ```sh Shell theme={null}
  pip install huggingface_hub>=0.29.0
  ```

  ```sh Shell theme={null}
  npm install @huggingface/inference
  ```
</CodeGroup>

## 1. Text generation - LLMs

### a. Chat completion with Hugging Face Hub library

<CodeGroup>
  ```py Python theme={null}
  from huggingface_hub import InferenceClient

  # Initialize the InferenceClient with together as the provider

  client = InferenceClient(
      provider="together",
      api_key="xxxxxxxxxxxxxxxxxxxxxxxx",  # Replace with your API key (HF or custom)
  )

  # Define the chat messages

  messages = [{"role": "user", "content": "What is the capital of France?"}]

  # Generate a chat completion

  completion = client.chat.completions.create(
      model="deepseek-ai/DeepSeek-R1",
      messages=messages,
      max_tokens=500,
  )

  # Print the response

  print(completion.choices[0].message)
  ```

  ```js TypeScript theme={null}
  import { HfInference } from "@huggingface/inference";

  // Initialize the HfInference client with your API key
  const client = new HfInference("xxxxxxxxxxxxxxxxxxxxxxxx");

  // Generate a chat completion
  const chatCompletion = await client.chatCompletion({
      model: "deepseek-ai/DeepSeek-R1",  // Replace with your desired model
      messages: [
          {
              role: "user",
              content: "What is the capital of France?"
          }
      ],
      provider: "together",  // Replace with together's provider name
      max_tokens: 500
  });

  // Log the response
  console.log(chatCompletion.choices[0].message);
  ```
</CodeGroup>

You can swap this for any compatible LLM from Together AI, here’s a handy [URL](https://huggingface.co/models?inference_provider=together\&other=text-generation-inference\&sort=trending) to find the list.

### b. OpenAI client library

You can also call inference providers via the [OpenAI python client](https://github.com/openai/openai-python). You will need to specify the `base_url` and `model` parameters in the client and call respectively.

The easiest way is to go to [a model’s page](https://huggingface.co/deepseek-ai/DeepSeek-R1?inference_api=true\&inference_provider=together\&language=python) on the hub and copy the snippet.

```py Python theme={null}
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/together",
    api_key="hf_xxxxxxxxxxxxxxxxxxxxxxxx",  # together or Hugging Face api key
)

messages = [{"role": "user", "content": "What is the capital of France?"}]

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1",
    messages=messages,
    max_tokens=500,
)

print(completion.choices[0].message)
```

## 2. Text-to-image generation

<CodeGroup>
  ```py Python theme={null}
  from huggingface_hub import InferenceClient

  # Initialize the InferenceClient with together as the provider

  client = InferenceClient(
      provider="together",  # Replace with together's provider name
      api_key="xxxxxxxxxxxxxxxxxxxxxxxx",  # Replace with your API key
  )

  # Generate an image from text

  image = client.text_to_image(
      "Bob Marley in the style of a painting by Johannes Vermeer",
      model="black-forest-labs/FLUX.1-schnell",  # Replace with your desired model
  )

  # `image` is a PIL.Image object

  image.show()
  ```

  ```js TypeScript theme={null}
  import { HfInference } from "@huggingface/inference";

  // Initialize the HfInference client with your API key
  const client = new HfInference("xxxxxxxxxxxxxxxxxxxxxxxx");

  // Generate a chat completion
  const generatedImage = await client.textToImage({
      model: "black-forest-labs/FLUX.1-schnell",  // Replace with your desired model
      inputs: "Bob Marley in the style of a painting by Johannes Vermeer",
      provider: "together",  // Replace with together's provider name
      max_tokens: 500
  });
  ```
</CodeGroup>

Similar to LLMs, you can use any compatible text-to-image model from the [list here](https://huggingface.co/models?inference_provider=together\&pipeline_tag=text-to-image\&sort=trending).

You can search for all [Together AI models](https://huggingface.co/models?inference_provider=together\&sort=trending) on the hub and directly try out the available models via the Model Page widget too.

The number of models and ways to try them out will continue to grow!
