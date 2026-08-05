---
title: "Together mixture of agents (MoA)"
source: https://docs.together.ai/docs/mixture-of-agents
path: docs/mixture-of-agents
---

<Frame>
  <img alt="" />
</Frame>

## What is Together MoA?

Mixture of Agents (MoA) is a novel approach that leverages the collective strengths of multiple LLMs to enhance performance, achieving state-of-the-art results. By employing a layered architecture where each layer comprises several LLM agents, **MoA significantly outperforms** GPT-4 Omni’s 57.5% on AlpacaEval 2.0 with a score of 65.1%, using only open-source models!

The way Together MoA works is that given a prompt, like `tell me the best things to do in SF`, it sends it to 4 different OSS LLMs. It then combines results from all 4, sends it to a final LLM, and asks it to combine all 4 responses into an ideal response. That’s it! It’s just the idea of combining the results of 4 different LLMs to produce a better final output. It’s slower than using a single LLM, but it can be great for use cases where latency doesn't matter as much, like synthetic data generation.

For a quick summary and 3-minute demo on how to implement MoA with code, watch the video below:

<Frame>
  <iframe title="YouTube embed" />
</Frame>

## Together MoA in 50 lines of code

To get started with using MoA in your own apps, you'll need to install the Together python library, get your Together API key, and run the code below which uses our chat completions API to interact with OSS models.

1. Install the Together Python library

```bash Shell theme={null}
pip install together
```

2. Get your [Together API key](https://api.together.ai/settings/projects/~current/api-keys) & export it

```bash Shell theme={null}
export TOGETHER_API_KEY='xxxx'
```

3. Run the code below, which interacts with our chat completions API.

This implementation of MoA uses 2 layers and 4 LLMs. We’ll define our 4 initial LLMs and our aggregator LLM, along with our prompt. We’ll also add in a prompt to send to the aggregator to combine responses effectively. Now that we have this, we’ll send the prompt to the 4 LLMs and compute all results simultaneously. Finally, we'll send the results from the four LLMs to our final LLM, along with a system prompt instructing it to combine them into a final answer, and we’ll stream results back.

```py Python theme={null}
# Mixture-of-Agents in 50 lines of code
import asyncio
import os
from together import AsyncTogether, Together

client = Together()
async_client = AsyncTogether()

user_prompt = "What are some fun things to do in SF?"
reference_models = [
    "zai-org/GLM-5.2",
    "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "moonshotai/Kimi-K2.6",
    "MiniMaxAI/MiniMax-M3",
]
aggregator_model = "moonshotai/Kimi-K2.6"
aggreagator_system_prompt = """You have been provided with a set of responses from various open-source models to the latest user query. Your task is to synthesize these responses into a single, high-quality response. It is crucial to critically evaluate the information provided in these responses, recognizing that some of it may be biased or incorrect. Your response should not simply replicate the given answers but should offer a refined, accurate, and comprehensive reply to the instruction. Ensure your response is well-structured, coherent, and adheres to the highest standards of accuracy and reliability.

Responses from models:"""


async def run_llm(model):
    """Run a single LLM call with a reference model."""
    response = await async_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": user_prompt}],
        temperature=0.7,
        max_tokens=512,
    )
    print(model)
    return response.choices[0].message.content


async def main():
    results = await asyncio.gather(
        *[run_llm(model) for model in reference_models]
    )

    finalStream = client.chat.completions.create(
        model=aggregator_model,
        messages=[
            {"role": "system", "content": aggreagator_system_prompt},
            {
                "role": "user",
                "content": ",".join(str(element) for element in results),
            },
        ],
        stream=True,
    )

    for chunk in finalStream:
        if chunk.choices:
            print(chunk.choices[0].delta.content or "", end="", flush=True)


asyncio.run(main())
```

## Advanced MoA example

In the previous example, we went over how to implement MoA with 2 layers (4 LLMs answering and one LLM aggregating). However, one strength of MoA is being able to go through several layers to get an even better response. In this example, we'll go through how to run MoA with 3+ layers.

<Frame>
  <img alt="" />
</Frame>

```py Python theme={null}
# Advanced Mixture-of-Agents example – 3 layers
import asyncio
import os
from together import AsyncTogether, Together
from together.error import RateLimitError

client = Together()
async_client = AsyncTogether()

user_prompt = "What are 3 fun things to do in SF?"
reference_models = [
    "zai-org/GLM-5.2",
    "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "moonshotai/Kimi-K2.6",
    "MiniMaxAI/MiniMax-M3",
]
aggregator_model = "moonshotai/Kimi-K2.6"
aggreagator_system_prompt = """You have been provided with a set of responses from various open-source models to the latest user query. Your task is to synthesize these responses into a single, high-quality response. It is crucial to critically evaluate the information provided in these responses, recognizing that some of it may be biased or incorrect. Your response should not simply replicate the given answers but should offer a refined, accurate, and comprehensive reply to the instruction. Ensure your response is well-structured, coherent, and adheres to the highest standards of accuracy and reliability.

Responses from models:"""
layers = 3


def getFinalSystemPrompt(system_prompt, results):
    """Construct a system prompt for layers 2+ that includes the previous responses to synthesize."""
    return (
        system_prompt
        + "\n"
        + "\n".join(
            [f"{i+1}. {str(element)}" for i, element in enumerate(results)]
        )
    )


async def run_llm(model, prev_response=None):
    """Run a single LLM call with a model while accounting for previous responses + rate limits."""
    for sleep_time in [1, 2, 4]:
        try:
            messages = (
                [
                    {
                        "role": "system",
                        "content": getFinalSystemPrompt(
                            aggreagator_system_prompt, prev_response
                        ),
                    },
                    {"role": "user", "content": user_prompt},
                ]
                if prev_response
                else [{"role": "user", "content": user_prompt}]
            )
            response = await async_client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=512,
            )
            print("Model: ", model)
            break
        except RateLimitError as e:
            print(e)
            await asyncio.sleep(sleep_time)
    return response.choices[0].message.content


async def main():
    """Run the main loop of the MOA process."""
    results = await asyncio.gather(
        *[run_llm(model) for model in reference_models]
    )

    for _ in range(1, layers - 1):
        results = await asyncio.gather(
            *[
                run_llm(model, prev_response=results)
                for model in reference_models
            ]
        )

    finalStream = client.chat.completions.create(
        model=aggregator_model,
        messages=[
            {
                "role": "system",
                "content": getFinalSystemPrompt(
                    aggreagator_system_prompt, results
                ),
            },
            {"role": "user", "content": user_prompt},
        ],
        stream=True,
    )
    for chunk in finalStream:
        if chunk.choices:
            print(chunk.choices[0].delta.content or "", end="", flush=True)


asyncio.run(main())
```

## Resources

* [Together MoA GitHub Repo](https://github.com/togethercomputer/MoA) (includes an interactive demo)
* [Together MoA blog post](https://www.together.ai/blog/together-moa)
* [MoA Technical Paper](https://arxiv.org/abs/2406.04692)
