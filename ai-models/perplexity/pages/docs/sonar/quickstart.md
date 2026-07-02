---
title: "Sonar API"
source: https://docs.perplexity.ai/docs/sonar/quickstart
path: docs/sonar/quickstart
---

Get started with Perplexity's Sonar API for web-grounded AI responses. Make your first API call in minutes.

## Overview

Perplexity's Sonar API provides web-grounded AI responses with support for streaming, tools, search options, and more. You can use it with OpenAI-compatible client libraries or our native SDKs for type safety and enhanced features.

Use the Sonar API when you need web search capabilities built-in, streaming responses, or Perplexity's Sonar models. For structured outputs and third-party models, use our [Agent API](/docs/agent-api/quickstart).

<Tip>
  Keep using your existing OpenAI SDKs to get started fast; switch to our [native SDKs](/docs/sdk/overview) later as needed.
</Tip>

<Card title="Pricing" icon="receipt" href="/docs/getting-started/pricing">
  Pay-as-you-go pricing for all APIs. No subscription required.
</Card>

## Installation

Install the SDK for your preferred language:

<CodeGroup>
  ```bash Python theme={null}
  pip install perplexityai
  ```

  ```bash Typescript theme={null}
  npm install @perplexity-ai/perplexity_ai
  ```

  ```bash OpenAI Python (Compatible) theme={null}
  pip install openai
  ```

  ```bash OpenAI Typescript (Compatible) theme={null}
  npm install openai
  ```
</CodeGroup>

## Authentication

Set your API key as an environment variable. The SDK will automatically read it:

<Tabs>
  <Tab title="macOS/Linux">
    ```bash theme={null}
    export PERPLEXITY_API_KEY="your_api_key_here"
    ```
  </Tab>

  <Tab title="Windows">
    ```powershell theme={null}
    setx PERPLEXITY_API_KEY "your_api_key_here"
    ```
  </Tab>
</Tabs>

<Info>
  All SDK examples below automatically use the `PERPLEXITY_API_KEY` environment variable. You can also pass the key explicitly if needed.
</Info>

## Generating an API Key

<Card title="Get your Perplexity API Key" icon="key" href="https://console.perplexity.ai">
  Navigate to the **API Keys** tab in the API Portal and generate a new key.
</Card>

<Note>
  **OpenAI SDK Compatible:** Perplexity's API supports the OpenAI Chat Completions format. You can use OpenAI client libraries by pointing to our endpoint.
</Note>

## Basic Usage

### Non-Streaming Request

<CodeGroup>
  ```python Python SDK theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  completion = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {"role": "user", "content": "What is quantum computing, what is a qubit, and what distinguishes NISQ-era machines from fault-tolerant systems?"}
      ]
  )

  print(completion.choices[0].message.content)
  ```

  ```typescript Typescript SDK theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const completion = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
          { role: "user", content: "What is quantum computing, what is a qubit, and what distinguishes NISQ-era machines from fault-tolerant systems?" }
      ],
  });

  console.log(completion.choices[0].message.content);
  ```

  ```python OpenAI Python SDK theme={null}
  import os
  from openai import OpenAI

  client = OpenAI(
      api_key=os.environ.get("PERPLEXITY_API_KEY"),
      base_url="https://api.perplexity.ai"
  )

  resp = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {"role": "user", "content": "What is quantum computing, what is a qubit, and what distinguishes NISQ-era machines from fault-tolerant systems?"}
      ]
  )
  print(resp.choices[0].message.content)
  ```

  ```typescript OpenAI Typescript SDK theme={null}
  import OpenAI from 'openai';

  const client = new OpenAI({
      apiKey: process.env.PERPLEXITY_API_KEY,
      baseURL: "https://api.perplexity.ai"
  });

  const resp = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
          { role: "user", content: "What is quantum computing, what is a qubit, and what distinguishes NISQ-era machines from fault-tolerant systems?" }
      ],
  });
  console.log(resp.choices[0].message.content);
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/sonar \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "sonar-pro",
      "messages": [
        {
          "role": "user",
          "content": "What is quantum computing, what is a qubit, and what distinguishes NISQ-era machines from fault-tolerant systems?"
        }
      ]
    }' | jq
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "74c299b6-fac7-45af-a69f-e0d08be695e5",
    "choices": [
      {
        "delta": {
          "content": "",
          "role": "assistant",
          "reasoning_steps": null,
          "tool_call_id": null,
          "tool_calls": null
        },
        "index": 0,
        "message": {
          "content": "Quantum computing is a model of computation that uses **quantum-mechanical effects such as superposition and entanglement** to process information in ways that can outperform classical computers on certain problems.[1][2][7] A **qubit** is the basic unit of quantum information: unlike a classical bit that is strictly 0 or 1, a qubit can be in a **superposition** of 0 and 1 and can be **entangled** with other qubits.[1][2][7] **NISQ-era machines** are today’s small, noisy quantum processors with limited qubit counts and high error rates, while **fault-tolerant systems** are future quantum computers designed to operate reliably at scale using quantum error correction to suppress noise and run long, complex algorithms.[1][2][7]  \n\n---\n\n### 1. What is quantum computing?\n\n- Quantum computing is a **computing paradigm that uses quantum mechanics**—the physics of very small systems—to perform computation.[1][2][5][7]  \n- A quantum computer manipulates **qubits** using quantum gates and algorithms, exploiting:\n  - **Superposition**: a qubit can exist in a combination of \\(|0\\rangle\\) and \\(|1\\rangle\\) simultaneously until measured.[1][2][4][7]  \n  - **Entanglement**: correlations between qubits such that the state of one is linked to the state of another, even when separated.[1][4][7]  \n  - **Quantum interference**: amplitudes for different computational paths can add or cancel, allowing algorithms to amplify correct answers and suppress wrong ones.[2][4][7]  \n\nThese properties allow quantum computers to potentially solve certain specialized problems (e.g., some optimization, simulation, factoring, and chemistry problems) **much faster or more efficiently** than any classical computer can.[1][2][6][9]  \n\n---\n\n### 2. What is a qubit?\n\n- A **qubit (quantum bit)** is the quantum analogue of the classical bit and is the **fundamental unit of information** in a quantum computer.[1][2][7][8]  \n- A classical bit is always **either** 0 **or** 1 at any given time.[1][2]  \n- A qubit can be in a state  \n  \\[\n  |\\psi\\rangle = \\alpha|0\\rangle + \\beta|1\\rangle,\n  \\]\n  where \\(\\alpha\\) and \\(\\beta\\) are complex numbers with \\(|\\alpha|^2 + |\\beta|^2 = 1\\). This is **superposition** of 0 and 1.[1][2][4][7]  \n- When you **measure** a qubit, you get 0 with probability \\(|\\alpha|^2\\) and 1 with probability \\(|\\beta|^2\\); the state “collapses” to the outcome.[4][7]  \n- Multiple qubits can be prepared in **entangled states**, where you cannot describe each qubit independently—measuring one instantaneously constrains the possible outcomes for the others.[1][4][7]  \n\n**Physical realizations of qubits** include:[1][4][6][7]  \n- **Superconducting circuits** (used by IBM, Google, etc.)  \n- **Trapped ions** (charged atoms held by electromagnetic fields)  \n- **Photons** (polarization or path as qubits)  \n- **Spin of electrons or nuclei**, quantum dots, and other “artificial atoms”  \n\nWhat matters is that the physical system has two well-defined quantum states that can be controlled and measured as \\(|0\\rangle\\) and \\(|1\\rangle\\), plus the ability to create superposition and entanglement between them.[1][4]  \n\n---\n\n### 3. NISQ-era machines vs. fault-tolerant systems\n\nResearchers often divide practical quantum hardware into two broad regimes:\n\n| Aspect | **NISQ-era machines** | **Fault-tolerant quantum computers** |\n|-------|------------------------|--------------------------------------|\n| Acronym / meaning | **NISQ** = *Noisy Intermediate-Scale Quantum* | Large-scale, **error-corrected** quantum systems |\n| Qubit count | Tens to a few hundred **physical** qubits | Thousands to millions of **physical** qubits to realize thousands–millions of **logical** qubits |\n| Noise & errors | High error rates; **noisy qubits and gates**; limited coherence times | Logical qubits have very **low effective error rates** via quantum error correction |\n| Error correction | Generally **no full error correction**; at best small error-mitigation techniques | **Full quantum error correction**, using many physical qubits to protect each logical qubit |\n| Algorithm depth | Can run only **shallow circuits** (limited gate depth) before noise destroys the computation | Can run **deep, long-running algorithms** (e.g., full-scale Shor, large simulations) |\n| Practical status | Represents **current quantum processors** from major vendors; useful mainly for research, demonstrations, and early applications | **Still a goal**; no fully fault-tolerant, large-scale machine exists yet[1][2][6][7] |\n| Use cases | Exploratory work: small-scale optimization, chemistry toy models, benchmarking, development of algorithms and compilers | Targeted for **scalable, reliable quantum advantage** in cryptography, complex simulation, large optimization, etc.[1][2][6][7] |\n\n**Key distinguishing ideas:**\n\n1. **Noise vs. fault tolerance**  \n   - NISQ devices are *inherently noisy*; each gate, measurement, and qubit has a significant chance of error, and computations quickly become unreliable as circuits grow.[1][2][7][8]  \n   - Fault-tolerant systems use **quantum error-correcting codes** to detect and correct errors without measuring and destroying the underlying quantum information (using operations like syndrome extraction). This lets them run long algorithms while keeping the overall error probability acceptably low.[1][2][7]  \n\n2. **Physical vs. logical qubits**  \n   - A **physical qubit** is one directly implemented in hardware (e.g., a single superconducting circuit or trapped ion). Current machines are described by their physical qubit counts (e.g., 50–100 qubits).[1][2]  \n   - A **logical qubit** is a robust, error-corrected qubit encoded across many physical qubits. Fault-tolerant machines will be described in terms of logical qubits, but will require many more physical qubits underneath.  \n\n3. **Scale and algorithm capability**  \n   - NISQ devices can demonstrate interesting quantum behavior and may achieve **limited, problem-specific advantages**, but they are not reliable enough for general-purpose quantum algorithms at useful scales.[1][2][6]  \n   - Fault-tolerant systems are the theoretical model assumed in most major quantum algorithms (e.g., large-scale Shor and Grover), enabling **provable, large quantum speedups** on certain tasks.  \n\nIf you’d like, I can follow up with a more math-focused explanation of qubits (Dirac notation, Bloch sphere) or a more application-focused view (what NISQ devices might realistically be used for in the near term).",
          "role": "assistant",
          "reasoning_steps": null,
          "tool_call_id": null,
          "tool_calls": null
        },
        "finish_reason": "stop"
      }
    ],
    "created": 1779896060,
    "model": "sonar-pro",
    "citations": [
      "https://scienceexchange.caltech.edu/topics/quantum-science-explained/quantum-computing-computers",
      "https://aws.amazon.com/what-is/quantum-computing/",
      "https://www.youtube.com/watch?v=B3U1NDUiwSA",
      "https://www.youtube.com/watch?v=Kv8N9alyYNc",
      "https://www.nist.gov/quantum-information-science/quantum-computing-explained",
      "https://www.ibm.com/think/topics/quantum-computing",
      "https://en.wikipedia.org/wiki/Quantum_computing",
      "https://www.bluequbit.io/blog/quantum-computing-basics",
      "https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-quantum-computing"
    ],
    "object": "chat.completion",
    "search_results": [
      {
        "title": "What Is Quantum Computing? - Caltech Science Exchange",
        "url": "https://scienceexchange.caltech.edu/topics/quantum-science-explained/quantum-computing-computers",
        "date": null,
        "last_updated": "2026-05-26",
        "snippet": "Quantum computers will help us learn about, model, and manipulate other quantum systems. That ability will improve our understanding of physics.",
        "source": "web"
      },
      {
        "title": "What is Quantum Computing? - AWS",
        "url": "https://aws.amazon.com/what-is/quantum-computing/",
        "date": "2026-05-13",
        "last_updated": "2026-05-18",
        "snippet": "Quantum computing is a multidisciplinary field comprising aspects of computer science, physics, and mathematics that utilizes quantum mechanics to solve ...",
        "source": "web"
      },
      {
        "title": "Quantum Computers Explained: How Quantum Computing Works",
        "url": "https://www.youtube.com/watch?v=B3U1NDUiwSA",
        "date": "2024-09-23",
        "last_updated": "2026-05-16",
        "snippet": "Quantum Computing is the ability to predict the outcome of all possible paths simultaneously and choosing the best path to achieve the ...",
        "source": "web"
      },
      {
        "title": "Quantum Computers: Explained VISUALLY - YouTube",
        "url": "https://www.youtube.com/watch?v=Kv8N9alyYNc",
        "date": "2025-04-22",
        "last_updated": "2026-05-24",
        "snippet": "In this video we take a visual look at the math of quantum computing. Also, check out this video on different types of quantum computers ...",
        "source": "web"
      },
      {
        "title": "Quantum Computing Explained | NIST",
        "url": "https://www.nist.gov/quantum-information-science/quantum-computing-explained",
        "date": "2025-03-18",
        "last_updated": "2026-05-23",
        "snippet": "These computers work by harnessing quantum physics — the strange, often counterintuitive laws that govern the universe at its smallest scales ...",
        "source": "web"
      },
      {
        "title": "What Is Quantum Computing? - IBM",
        "url": "https://www.ibm.com/think/topics/quantum-computing",
        "date": "2025-06-10",
        "last_updated": "2026-03-31",
        "snippet": "Quantum computing is an emergent field of computer science and engineering that harnesses the unique qualities of quantum mechanics to solve problems",
        "source": "web"
      },
      {
        "title": "Quantum computing - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Quantum_computing",
        "date": "2001-10-21",
        "last_updated": "2026-05-27",
        "snippet": "A quantum computer is a real or theoretical computer that exploits quantum phenomena like superposition and entanglement in an essential way.",
        "source": "web"
      },
      {
        "title": "Quantum Computing Basics: A Beginner's Guide - BlueQubit",
        "url": "https://www.bluequbit.io/blog/quantum-computing-basics",
        "date": "2026-04-27",
        "last_updated": "2026-05-11",
        "snippet": "Quantum computing is a type of computing that uses the principles of quantum mechanics to process information. Unlike classical computers, which ...",
        "source": "web"
      },
      {
        "title": "What is quantum computing? - McKinsey",
        "url": "https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-quantum-computing",
        "date": "2025-03-31",
        "last_updated": "2026-05-27",
        "snippet": "Quantum computing is a new approach to calculation that uses principles of fundamental physics to solve extremely complex problems very quickly.",
        "source": "web"
      }
    ],
    "status": null,
    "type": null,
    "usage": {
      "completion_tokens": 1541,
      "cost": {
        "input_tokens_cost": 8e-05,
        "output_tokens_cost": 0.02312,
        "total_cost": 0.0292,
        "citation_tokens_cost": null,
        "reasoning_tokens_cost": null,
        "request_cost": 0.006,
        "search_queries_cost": null
      },
      "prompt_tokens": 28,
      "total_tokens": 1569,
      "citation_tokens": null,
      "num_search_queries": null,
      "reasoning_tokens": null,
      "search_context_size": "low"
    }
  }
  ```
</Accordion>

### Streaming Response

<CodeGroup>
  ```python Python SDK theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  stream = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {"role": "user", "content": "What are the most widely used open-source large language models that serve as alternatives to OpenAI's GPT models?"}
      ],
      stream=True
  )

  for chunk in stream:
      if chunk.choices[0].delta.content:
          print(chunk.choices[0].delta.content, end="")
  ```

  ```typescript Typescript SDK theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const stream = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [
          { role: "user", content: "What are the most widely used open-source large language models that serve as alternatives to OpenAI's GPT models?" }
      ],
      stream: true,
  });

  for await (const chunk of stream) {
      if (chunk.choices[0].delta.content) {
          process.stdout.write((chunk.choices[0]?.delta?.content ?? '') as string);
      }
  }
  ```

  ```bash cURL theme={null}
  curl https://api.perplexity.ai/v1/sonar \
    -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "sonar-pro",
      "messages": [
        {
          "role": "user",
          "content": "What are the most popular open-source alternatives to OpenAI'\''s GPT models?"
        }
      ],
      "stream": true
    }'
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "38678936-bd01-4447-ad3a-196dce1cea08",
    "choices": [
      {
        "delta": {
          "content": "",
          "role": "assistant",
          "reasoning_steps": null,
          "tool_call_id": null,
          "tool_calls": null
        },
        "index": 0,
        "message": {
          "content": "Here are the most widely used and actively maintained open‑source (or open‑weight) alternatives to OpenAI’s GPT models, based on the sources you provided plus current ecosystem reality. I’ll group them by how general‑purpose and “GPT‑like” they are.\n\n---\n\n## 1. Llama 3 (and Llama 2) – Meta\n\n**Why it’s popular**\n\n- Currently the *de facto* standard open‑weight GPT alternative for general use.\n- Strong performance on coding, chat, and general reasoning.\n- Huge ecosystem: quantized builds, fine‑tunes, tools, and UIs (Ollama, LM Studio, etc.).\n\n**Key points**\n\n- **Developer**: Meta (FAIR).\n- **Models**: Llama 3 8B, 70B (and Llama 2 7B/13B/70B).\n- **Use cases**: Chatbots, coding assistants, content generation, RAG apps.\n- **License**: Custom “open‑weight” license (free but with some restrictions for large‑scale commercial use).\n\n---\n\n## 2. Qwen – Alibaba\n\n**Why it’s popular**\n\n- Competitive performance with Llama in many benchmarks.\n- Strong multilingual support (especially English + Chinese).\n- Many model variants and sizes.\n\n**Key points**\n\n- **Developer**: Alibaba Cloud.\n- **Models**: Qwen 2 and Qwen 1.5 in sizes from small (1.8B) to large (72B), plus code and vision variants.\n- **Use cases**: Chat, code, multilingual assistants.\n- **License**: Generally permissive for most commercial uses, with some conditions.\n\n---\n\n## 3. DeepSeek\n\n**Why it’s popular**\n\n- Frequently cited as one of the best **reasoning and coding** open models.\n- Very attractive **cost‑performance** ratio and strong support in hosted and local stacks.\n\n**Key points**\n\n- **Focus**: Technical reasoning, math, and programming.\n- **Use cases**: Code assistants, analysis tools, agents.\n- **License**: Open‑weight; needs license review for large‑scale commercial deployments.\n\n---\n\n## 4. Mistral & Mixtral – Mistral AI\n\n**Why it’s popular**\n\n- High‑quality models with efficient Mixture‑of‑Experts (MoE) architectures.\n- Strong performance on many standard benchmarks.\n- Widely integrated by infra providers and tools.\n\n**Key points**\n\n- **Developer**: Mistral AI.\n- **Models**: Mistral 7B, Mixtral 8x7B, 8x22B, etc.\n- **Use cases**: General chat, code, RAG, production APIs.\n- **License**: Apache 2.0 or similar for many models (good for commercial).\n\n---\n\n## 5. GPT‑OSS – OpenAI’s open‑weight family\n\n**Why it’s popular**\n\n- Directly from OpenAI, designed as an “open alternative” with reasoning capabilities similar to their frontier models (per your source).\n- Specifically aimed at organizations that want **self‑hosting** and more control.\n\n**Key points**\n\n- **Developer**: OpenAI.\n- **Use cases**: General GPT‑like assistant on private infrastructure.\n- **License**: Open‑weight; details matter for redistribution and commercial use.\n\n---\n\n## 6. GPT4All – Ecosystem for local LLMs\n\n**Why it’s popular**\n\n- Not a single model but a **tooling ecosystem**: lets you download and run many Llama/Mistral/etc. models locally with a simple UI.\n- Very user‑friendly for non‑experts.\n\n**Key points**\n\n- **Developer**: Nomic AI.\n- **Use cases**: Local ChatGPT‑like experience, experimentation with many open models.\n- **License**: Varies by model; the framework itself is open‑source.\n\n---\n\n## 7. Vicuna\n\n**Why it’s popular**\n\n- Early high‑quality chat fine‑tune of LLaMA; widely cited (“90% of ChatGPT quality”).\n- Still used in research and some legacy systems.\n\n**Key points**\n\n- **Base**: LLaMA / Llama 2.\n- **Use cases**: Conversational agents, research.\n- **License**: Follows base model license; often non‑commercial or restricted.\n\n---\n\n## 8. OpenAssistant\n\n**Why it’s popular**\n\n- Community‑driven attempt to replicate ChatGPT with **fully open data and models**.\n- Emphasis on transparency and RLHF pipeline.\n\n**Key points**\n\n- **Developer**: LAION and community.\n- **Use cases**: Chatbots, research on alignment and RLHF.\n- **License**: Open‑source; good for research and customization.\n\n---\n\n## 9. Falcon\n\n**Why it’s popular**\n\n- One of the first strong, fully open‑weight 40B–180B‑parameter models.\n- Widely available on Hugging Face; still used in many pipelines.\n\n**Key points**\n\n- **Developer**: TII (Technology Innovation Institute).\n- **Use cases**: General‑purpose LLM, multilingual tasks.\n- **License**: Falcon License (permissive but with some constraints).\n\n---\n\n## 10. MPT (MosaicML) – e.g., MPT‑7B\n\n**Why it’s popular**\n\n- Focus on **commercial usability** and efficient deployment.\n- Often used as a base for custom fine‑tunes.\n\n**Key points**\n\n- **Developer**: MosaicML (acquired by Databricks).\n- **Models**: MPT‑7B and derivatives (instruct, story, etc.).\n- **Use cases**: Apps needing permissive licensing and predictable behavior.\n- **License**: Mostly Apache 2.0 / commercially friendly.\n\n---\n\n## 11. Older but still relevant GPT‑like families\n\nThese are less competitive with the newest Llama/Qwen/Mistral generations but still important, especially for research, education, or low‑resource setups:\n\n- **GPT‑J / GPT‑Neo / GPT‑NeoX** (EleutherAI)  \n  Early GPT‑3‑style open models; common in open‑source tools and papers.\n\n- **OPT** (Meta)  \n  175B‑parameter GPT‑3‑scale model; useful for research and benchmarks.\n\n- **BLOOM** (BigScience)  \n  Large multilingual open model; widely used in academia.\n\n- **RWKV / ChatRWKV / Raven RWKV**  \n  RNN‑like architecture as a transformer alternative; efficient and popular among enthusiasts.\n\n---\n\n## 12. Multimodal “GPT‑4‑Vision‑like” open alternatives\n\nFor GPT‑4‑Vision‑style capabilities, these are frequently cited:\n\n- **LLaVA** – LLaMA + vision encoder; question answering about images.\n- **Fuyu** – Multimodal model designed for structured visual inputs.\n- **CogVLM** – Another strong vision‑language model family.\n\nAll are open‑weight and can be hosted privately.\n\n---\n\n## How to pick one\n\nVery roughly:\n\n- **General‑purpose / closest to GPT‑4‑style chat**:  \n  Llama 3, Qwen 2, Mistral/Mixtral, GPT‑OSS.\n- **Best for coding & reasoning**:  \n  DeepSeek, Qwen‑Coder, Llama 3 Instruct/Code variants.\n- **Fully local “ChatGPT on your laptop”**:  \n  Llama 3 via **Ollama**, **GPT4All**, or **LM Studio**.\n- **Research / transparency focus**:  \n  OpenAssistant, Vicuna, BLOOM, GPT‑J/NeoX, Falcon, RWKV.\n\nIf you tell me your main use case (e.g., “small startup, needs on‑prem, heavy coding,” or “university research, must be very open license”), I can narrow this down to a short, concrete recommendation list.",
          "role": "assistant",
          "reasoning_steps": null,
          "tool_call_id": null,
          "tool_calls": null
        },
        "finish_reason": "stop"
      }
    ],
    "created": 1779391627,
    "model": "sonar-pro",
    "citations": [
      "https://neoteric.eu/blog/open-source-vs-openai-8-best-open-source-alternatives-to-gpt",
      "https://www.datacamp.com/blog/12-gpt4-open-source-alternatives",
      "https://bdtechtalks.substack.com/p/what-are-the-open-source-alternatives",
      "https://www.simular.ai/alternatives/top-best-open-source-model-alternatives-to-gpt-5-for-teams",
      "https://www.lindy.ai/blog/chatgpt-alternative",
      "https://github.com/GPT-Alternatives/gpt_alternatives",
      "https://northflank.com/blog/open-source-chatgpt-alternatives-enterprise",
      "https://connect.oeglobal.org/t/tagged-for-oeg-connect-13-best-open-source-chatgpt-alternatives/6303"
    ],
    "object": "chat.completion",
    "search_results": [
      {
        "title": "8 Best Open-Source Alternatives to GPT - Neoteric",
        "url": "https://neoteric.eu/blog/open-source-vs-openai-8-best-open-source-alternatives-to-gpt",
        "date": "2023-06-08",
        "last_updated": "2026-05-21",
        "snippet": "Best alternatives to GPT (open source only) · LLaMA · GPT-J & GPT-NeoX · Dolly · Alpaca · Vicuna · OpenAssistant · ChatGPT alternatives.",
        "source": "web"
      },
      {
        "title": "12 GPT-4 Open-Source Alternatives - DataCamp",
        "url": "https://www.datacamp.com/blog/12-gpt4-open-source-alternatives",
        "date": "2024-08-01",
        "last_updated": "2026-05-18",
        "snippet": "12 GPT-4 Open-Source Alternatives · 1. ColossalChat · 2. Alpaca-LoRA · 3. Vicuna · 4. GPT4ALL · 5. Raven RWKV · 6. OpenChatKit · 7. OPT · 8. Flan-T5-XXL.",
        "source": "web"
      },
      {
        "title": "What are the open-source alternatives to GPT-4 Vision? - TechTalks",
        "url": "https://bdtechtalks.substack.com/p/what-are-the-open-source-alternatives",
        "date": "2024-01-04",
        "last_updated": "2026-02-06",
        "snippet": "There are open-source models that provide similar capabilities. Some of these models include LLaVA, Fuyu, and CogVLM. All these models are available for ...",
        "source": "web"
      },
      {
        "title": "Top Best Open source model alternatives to GPT-5 for teams",
        "url": "https://www.simular.ai/alternatives/top-best-open-source-model-alternatives-to-gpt-5-for-teams",
        "date": "2026-02-28",
        "last_updated": "2026-05-16",
        "snippet": "Comparison Summary · 1. Simular Pro: The \"Hands\" for Your Open-Source Brain · 2. GPT-OSS: OpenAI's Powerful Open Alternative · 3. Llama 3: The Industry Standard.",
        "source": "web"
      },
      {
        "title": "I Tested 20+ ChatGPT Alternatives. These Are The Best in 2026 | Lindy",
        "url": "https://www.lindy.ai/blog/chatgpt-alternative",
        "date": "2026-05-06",
        "last_updated": "2026-05-21",
        "snippet": "DeepSeek: Best ChatGPT alternative for technical reasoning & coding. Why I picked DeepSeek: DeepSeek feels built for thinking things through.",
        "source": "web"
      },
      {
        "title": "GPT-Alternatives/gpt_alternatives - GitHub",
        "url": "https://github.com/GPT-Alternatives/gpt_alternatives",
        "date": "2023-08-02",
        "last_updated": "2025-10-28",
        "snippet": "In this survey paper, we provide an examination of alternative open-sourced models of large GPTs, focusing on user-friendly and relatively small models.",
        "source": "web"
      },
      {
        "title": "Top open-source alternatives to ChatGPT for companies - Northflank",
        "url": "https://northflank.com/blog/open-source-chatgpt-alternatives-enterprise",
        "date": "2025-09-01",
        "last_updated": "2026-05-21",
        "snippet": "1. OpenAI GPT-OSS: OpenAI's first open-weight model release · 2. DeepSeek: Cost-effective reasoning models · 3. Qwen: Alibaba's solution · 4. Meta ...",
        "source": "web"
      },
      {
        "title": "Tagged for OEG Connect: 13 Best Open Source ChatGPT Alternatives",
        "url": "https://connect.oeglobal.org/t/tagged-for-oeg-connect-13-best-open-source-chatgpt-alternatives/6303",
        "date": "2024-01-13",
        "last_updated": "2025-10-10",
        "snippet": "Ollama / Jan.ai can be used as ChatGPT alternatives running on the local computer. I mostly use the text / code generation features but expect ...",
        "source": "web"
      }
    ],
    "status": null,
    "type": null,
    "usage": {
      "completion_tokens": 1664,
      "cost": {
        "input_tokens_cost": 5e-05,
        "output_tokens_cost": 0.02496,
        "total_cost": 0.03101,
        "citation_tokens_cost": null,
        "reasoning_tokens_cost": null,
        "request_cost": 0.006,
        "search_queries_cost": null
      },
      "prompt_tokens": 17,
      "total_tokens": 1681,
      "citation_tokens": null,
      "num_search_queries": null,
      "reasoning_tokens": null,
      "search_context_size": "low"
    }
  }
  ```
</Accordion>

<Info title="Complete Streaming Guide" href="/docs/agent-api/output-control#streaming-responses">
  For a full guide on streaming, including parsing, error handling, citation management, and best practices, see our [Agent API streaming guide](/docs/agent-api/output-control#streaming-responses).
</Info>

## Response Structure

Sonar API responses follow an OpenAI-compatible format:

```json theme={null}
{
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "model": "sonar-pro",
    "created": 1234567890,
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "Recent developments in quantum computing include advances in error correction, new qubit architectures, and progress toward fault-tolerant systems..."
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 14,
        "completion_tokens": 287,
        "total_tokens": 301
    }
}
```

## Next Steps

<CardGroup>
  <Card title="Agent API" icon="code-circle" href="/docs/agent-api/quickstart">
    Need structured outputs or third-party models? Check out the Agent API.
  </Card>

  <Card title="Search API" icon="search" href="/docs/search/quickstart">
    Get raw search results with the Search API.
  </Card>

  <Card title="Sonar API Features" icon="book" href="/docs/sonar/features">
    Complete guide to the Sonar API with advanced features and examples.
  </Card>

  <Card title="Models" icon="brain" href="/docs/sonar/models">
    Explore available Sonar models and their capabilities.
  </Card>

  <Card title="API Reference" icon="code-circle" href="/api-reference/sonar-post">
    View complete endpoint documentation and parameters.
  </Card>

  <Card title="Search Filters" icon="search" href="/docs/sonar/filters#search-control">
    Learn how to control search behavior with filters and parameters.
  </Card>
</CardGroup>

<Info>
  Need help? Check out our [community](https://community.perplexity.ai) for support and discussions with other developers.
</Info>
