---
title: "Type Safety"
source: https://docs.perplexity.ai/docs/sdk/type-safety
path: docs/sdk/type-safety
---

Learn how to leverage full TypeScript definitions and Python type hints with the Perplexity SDKs for better development experience and code safety.

## Overview

Both Perplexity SDKs provide comprehensive type definitions to help you catch errors at development time and provide better IDE support. This guide covers type annotations, generic types, and advanced typing patterns.

## Basic Type Usage

### Type Imports and Annotations

Use type imports for better IDE support and type checking:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity
  from perplexity.types import (
      SearchCreateResponse,
      ResponseCreateResponse,
      SearchResult
  )

  client = Perplexity()

  # Type hints for better IDE support
  search_response: SearchCreateResponse = client.search.create(
      query="OpenAI API release history and developer features"
  )

  # Access typed properties
  result: SearchResult = search_response.results[0]
  print(f"Title: {result.title}")
  print(f"URL: {result.url}")
  print(f"Snippet: {result.snippet}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // TypeScript provides full intellisense and type checking
  const searchResponse: Perplexity.Search.SearchCreateResponse = await client.search.create({
      query: "OpenAI API release history and developer features"
  });

  // Access typed properties with intellisense
  const result = searchResponse.results[0];
  console.log(`Title: ${result.title}`);
  console.log(`URL: ${result.url}`);
  console.log(`Snippet: ${result.snippet}`);
  ```
</CodeGroup>

<Accordion title="Response">
  ````json theme={null}
  {
    "id": "4a713b10-40e7-4d2a-9e7b-fdd9870702e8",
    "results": [
      {
        "snippet": "",
        "title": "Changelog | OpenAI API",
        "url": "https://developers.openai.com/api/docs/changelog",
        "date": null,
        "last_updated": "2026-05-27"
      },
      {
        "snippet": "All latest OpenAI models support text and image input, text output, multilingual capabilities, and vision.\nModels are available via the Responses API and our Client SDKs.",
        "title": "Models | OpenAI API",
        "url": "https://developers.openai.com/api/docs/models",
        "date": null,
        "last_updated": "2026-05-07"
      },
      {
        "snippet": "June 11, 2020\n...\nWe’re releasing an API for accessing new AI models developed by OpenAI.\nUnlike most AI systems which are designed for one use-case, the API today provides a general-purpose “text in, text out” interface, allowing users to try it on virtually any English language task.\nYou can now request access in order to integrate the API into your product, develop an entirely new application, or help us explore the strengths and limits of this technology.\nGiven any text prompt, the API will return a text completion, attempting to match the pattern you gave it.\nYou can “program” it by showing it just a few examples of what you’d like it to do; its success generally varies depending on how complex the task is.\nThe API also allows you to hone performance on specific tasks by training on a dataset (small or large) of examples you provide, or by learning from human feedback provided by users or labelers.\n...\nToday the API runs models with weights from the GPT‑3⁠(opens in a new window) family with many speed and throughput improvements.",
        "title": "OpenAI API",
        "url": "https://openai.com/index/openai-api/",
        "date": "2020-06-11",
        "last_updated": "2026-03-29"
      },
      {
        "snippet": "",
        "title": "OpenAI Just Changed Everything (Responses API Walkthrough)",
        "url": "https://www.youtube.com/watch?v=0pGxoubWI6s",
        "date": "2025-03-13",
        "last_updated": "2026-03-31"
      },
      {
        "snippet": "",
        "title": "Call to bring back the rigor in API Development and ...",
        "url": "https://community.openai.com/t/call-to-bring-back-the-rigor-in-api-development-and-production-grade-slas-for-api-improvements/1357192",
        "date": "2025-09-09",
        "last_updated": "2026-05-04"
      },
      {
        "snippet": "Announced Open Responses: an open-source spec for building multi-provider, interoperable LLM interfaces built on top of the original OpenAI Responses API.\nJan 14\nFeature\ngpt-5.2-codex\nv1/responses\nReleased\n```\ngpt-5.2-codex\n```\nto the Responses API.\nGPT-5.2-Codex is a version of GPT-5.2 optimized for agentic coding tasks in Codex or similar environments.\nRead more here.\n...\nUpdated the gpt-realtime-mini and gpt-audio-mini slugs to point to the 2025-12-15 snapshots.\n...\nUpdated the sora-2 slug to point to\n```\nsora-2-2025-12-08\n```\n...\ngpt-image-1.5\nchatgpt-image-latest\nAdded\n```\ngpt-image-1.5\n```\nand\n```\nchatgpt-image-latest\n```\nto the Responses API image generation tool.\n...\ngpt-image-1.5\nchatgpt-image-latest\nReleased gpt-image-1.5 and chatgpt-image-latest, our latest and most advanced models for image generation.\nRead more here.\n...\nReleased four new dated audio snapshots.\nThese updates deliver reliability, quality, and voice fidelity improvements for real-time, voice-driven applications.\nRead more here.\n...\nThis launch also includes support for Custom voices for eligible customers.\n...\nReleased GPT-5.2, the newest flagship model in the GPT-5 model family.\nGPT-5.2 shows improvements over the previous GPT-5.1 in:\n- General intelligence\n...\nFor long-running conversations with the Responses API, you can use the\n```\n...\n```\n...\nReleased GPT-5.1, the newest flagship model in the GPT-5 model family.\n...\nReleased enhanced role-based access controls (RBAC).\nRole-based access control (RBAC) lets you decide who can do what across your organization and projects—both through the API and in the Dashboard.\n...\nExtended prompt cache retention keeps cached prefixes active for longer, up to a maximum of 24 hours.\nExtended Prompt Caching works by offloading the key/value tensors to GPU-local storage when memory is full, significantly increasing the storage capacity available for caching.\n...\nReleased gpt-5-pro, a version of GPT-5 that uses more compute to think harder and provide consistently better answers.\nReleased gpt-realtime-mini and gpt-audio-mini for more cost-efficient speech to speech performance.\nReleased gpt-image-1-mini for more cost-efficient image generation and editing.\nLaunched v1/videos for rich, detailed, and dynamic video generation and remixing with our latest Sora 2 and Sora 2 Pro models.\nLaunched Agent Builder for visually creating custom multi-agent workflows.\nLaunched ChatKit, an embeddable chat interface for deploying agents.\n...\n- Released the Responses API, a new API for creating and using agents and tools.\n- Released a set of built-in tools for the Responses API: web search, file search, and computer use.\n...\n- Announced plans to bring all Assistants API features to the easier to use Responses API, with an anticipated sunset date for Assistants in 2026 (after achieving full feature parity).",
        "title": "Changelog | OpenAI API",
        "url": "https://platform.openai.com/docs/changelog",
        "date": "2025-01-31",
        "last_updated": "2026-01-21"
      },
      {
        "snippet": "",
        "title": "API Platform",
        "url": "https://openai.com/api/",
        "date": "2026-04-09",
        "last_updated": "2026-05-27"
      },
      {
        "snippet": "### June, 2025Jun 13featurev1/responses\n- New reusable prompts are now available in the dashboard and Responses API.\nVia API, you can now reference templates created in the dashboard via the\n`prompt`parameter (with a prompt\n`id`, optional\n`version`) and supply dynamic\n`variables`that can include strings, images, or file inputs.\nReusable prompts are not available in Chat Completions.\nLearn more.\n- Released o3-pro, a version of the o3 reasoning model that uses more compute to answer hard problems with better reasoning and consistency.\nPrices for the o3 model have also been reduced for all API requests, including batch and flex processing.\n- Added fine-tuning support with direct preference optimization for the models\n`gpt-4.1-2025-04-14`,\n`gpt-4.1-mini-2025-04-14`, and\n`gpt-4.1-nano-2025-04-14`.\n- New model snapshots available for gpt-4o-audio-preview and gpt-4o-realtime-preview.\nReleased Agents SDK for TypeScript.\n### May, 2025May 20featurev1/responses\n- Added support for new built-in tools in the Responses API, including remote MCP servers and code interpreter.\nLearn more about tools.\n- Added support for using\n`strict`mode for tool schemas when using parallel tool calling with non-fine-tuned models.\n- Added new schema features, including string validation for\n- Launched codex-mini-latest in the API, optimized for use with the Codex CLI.\n...\n- Launched support for reinforcement fine-tuning.\nLearn about available fine-tuning methods.\ngpt-4.1-nano is now available for fine-tuning.\n=======\n...\n### April, 2025Apr 23featurev1/images/generationsv1/images/edits\n- Added a new image generation model,\n`gpt-image-1`.\nThis model sets a new standard for image generation, with improved quality and instruction following.\n- Updated the Image Generation and Edit endpoints to support new parameters specific to the\n`gpt-image-1`model.\n- Added two new o-series reasoning models,\n`o3`and\n`o4-mini`.\nThey set a new standard for math, science, and coding, visual reasoning tasks, and technical writing.\n- Launched Codex, our code generation CLI tool.\n- Added\n`gpt-4.1`,\n`gpt-4.1-mini`, and\n`gpt-4.1-nano`models to the API.\nThese new models feature improved instruction following, coding, and a larger context window (up to 1M tokens).\n`gpt-4.1`and\n`gpt-4.1-mini`are available for supervised fine-tuning.\nAnnounced deprecation of\n`gpt-4.5-preview`.\n### March, 2025Mar 20updatev1/audio\n- Added\n`gpt-4o-mini-tts`,\n`gpt-4o-transcribe`,\n`gpt-4o-mini-transcribe`, and\n`whisper-1`models to the Audio API.\n- Released o1-pro, a version of the o1 reasoning model that uses more compute to answer hard problems with better reasoning and consistency.\nReleased several new models and tools and a new API for agentic workflows:\nReleased the Responses API, a new API for creating and using agents and tools.\nReleased a set of built-in tools for the Responses API: web search, file search, and computer use.\nReleased the Agents SDK, an orchestration framework for designing, building, and deploying agents.\nAnnounced new models:\n`gpt-4o-search-preview`,\n`gpt-4o-mini-search-preview`,\n`computer-use-preview`.\nAnnounced plans to bring all Assistants API features to the easier to use Responses API, with an anticipated sunset date for Assistants in 2026 (after achieving full feature parity).\n- Added\n`metadata`field support to fine-tuning jobs.\n### February, 2025Feb 27featuregpt-4.5v1/chat/completionsv1/assistantsv1/batch\n- Released a research preview of GPT-4.5—our largest and most capable chat model yet.\nGPT-4.5's high \"EQ\" and understanding of user intent make it better at creative tasks and agentic planning.\n### January, 2025Jan 31featureo3-minio3-mini-2025-01-31v1/chat/completions\n- Launched o3-mini, a new small reasoning model that is optimized for science, math, and coding tasks.\n### December, 2024Dec 18feature\nLaunched Admin API Key Rotations, enabling customers to programmatically rotate their admin api keys.\nUpdated Admin API Invites, enabling customers to programmatically invite users to projects at the same time they are invited to organizations.\nAdded new models for o1, gpt-4o-realtime, gpt-4o-audio and more.\nAdded WebRTC connection method for the Realtime API.\nAdded\n...\nAdded\n`developer`message role for o1 model.\nNote that o1-preview and o1-mini do not support system or developer messages.\nLaunched Preference Fine-tuning using Direct Preference Optimization (DPO).\nLaunched beta SDKs for Go and Java.\nLearn more.\nAdded Realtime API support in the Python SDK.\n- Launched Usage API, enabling customers to programmatically query activities and spending across OpenAI APIs.\n### November, 2024Nov 20Updatev1/chat/completions\n- Released gpt-4o-2024-11-20, our newest model in the gpt-4o series.\n- Released Predicted Outputs, which greatly reduces latency for model responses where much of the response is known ahead of time.\nThis is most common when regenerating the content of documents and code files with only minor changes.\n...\n- Released new\n`gpt-4o-audio-preview`model for chat completions, which supports both audio inputs and outputs.\nUses the same underlying model as the Realtime API.\nReleased several new features at OpenAI DevDay in San Francisco:\n...\n- Released\nnew\n`omni-moderation-latest`moderation model, which supports both images and text (for some categories), supports two new text-only harm categories, and has more accurate scores.\n- Released o1-preview and o1-mini, new large language models trained with reinforcement learning to perform complex reasoning tasks.",
        "title": "Changelog - OpenAI API",
        "url": "https://platform.openai.com/docs/changelog/changelog",
        "date": "2025-01-31",
        "last_updated": "2025-06-20"
      },
      {
        "snippet": "",
        "title": "Model Release Notes | OpenAI Help Center",
        "url": "https://help.openai.com/en/articles/9624314-model-release-notes",
        "date": "2025-12-18",
        "last_updated": "2026-04-01"
      },
      {
        "snippet": "### February, 2025Feb 27featuregpt-4.5v1/chat/completionsv1/assistantsv1/batch\n- Released a research preview of GPT-4.5—our largest and most capable chat model yet.\nGPT-4.5's high \"EQ\" and understanding of user intent make it better at creative tasks and agentic planning.\n### January, 2025Jan 31featureo3-minio3-mini-2025-01-31v1/chat/completions\n- Launched o3-mini, a new small reasoning model that is optimized for science, math, and coding tasks.\n### December, 2024Dec 18feature\nLaunched Admin API Key Rotations, enabling customers to programmatically rotate their admin api keys.\nUpdated Admin API Invites, enabling customers to programmatically invite users to projects at the same time they are invited to organizations.\nAdded new models for o1, gpt-4o-realtime, gpt-4o-audio and more.\nAdded WebRTC connection method for the Realtime API.\nAdded\n`reasoning_effort`parameter for o1 models.\nAdded\n`developer`message role for o1 model.\nNote that o1-preview and o1-mini do not support system or developer messages.\nLaunched Preference Fine-tuning using Direct Preference Optimization (DPO).\nLaunched beta SDKs for Go and Java.\nLearn more.\nAdded Realtime API support in the Python SDK.\n- Launched Usage API, enabling customers to programmatically query activities and spending across OpenAI APIs.\n### November, 2024Nov 20Updatev1/chat/completions\n- Released gpt-4o-2024-11-20, our newest model in the gpt-4o series.\n- Released Predicted Outputs, which greatly reduces latency for model responses where much of the response is known ahead of time.\nThis is most common when regenerating the content of documents and code files with only minor changes.\n### October, 2024Oct 30featuregpt-4o-realtime-previewgpt-4o-audio-previewv1/chat/completions\n- Added five new voice types in the Realtime API and Chat Completions API.\n- Released new\n`gpt-4o-audio-preview`model for chat completions, which supports both audio inputs and outputs.\nUses the same underlying model as the Realtime API.\nReleased several new features at OpenAI DevDay in San Francisco:\nRealtime API: Build fast speech-to-speech experiences into your applications using a WebSockets interface.\nModel distillation: Platform for fine-tuning cost-efficient models with your outputs from a large frontier model.\nImage fine-tuning: Fine-tune GPT-4o with images and text to improve vision capabilities.\nEvals: Create and run custom evaluations to measure model performance on specific tasks.\nPrompt caching: Discounts and faster processing times on recently seen input tokens.\nGenerate in playground: Easily generate prompts, function definitions, and structured output schemas in the playground using the Generate button.\n### September, 2024Sep 26featureomni-moderation-latestv1/moderations\n- Released\nnew\n`omni-moderation-latest`moderation model, which supports both images and text (for some categories), supports two new text-only harm categories, and has more accurate scores.\n- Released o1-preview and o1-mini, new large language models trained with reinforcement learning to perform complex reasoning tasks.\n### August, 2024Aug 29featurev1/assistants\n- Assistants API now supports including file search results used by the file search tool, and customizing ranking behavior.\n- GA release for\n`gpt-4o-2024-08-06`fine-tuning—all API users can now fine-tune the latest GPT-4o model.\n- Released dynamic model for\n`chatgpt-4o-latest`—this model will point to the latest GPT-4o model used by ChatGPT.\n- Launched Structured Outputs—model outputs now reliabilty adhere to developer supplied JSON Schemas.\n- Released gpt-4o-2024-08-06, our newest model in the gpt-4o series.\n- Launched Admin and Audit Log APIs, allowing customers to programmatically administer their organization and monitor changes using the audit logs.\nAudit logging must be enabled within settings.\n### July, 2024Jul 24Update\n- Launched self-serve SSO configuration, allowing Enterprise customers on custom and unlimited billing to set up authentication against their desired IDP.\n- Launched fine-tuning for GPT-4o mini, enabling even higher performance for specific use cases.\n- Released GPT-4o mini, our affordable an intelligent small model for fast, lightweight tasks.\n- Released Uploads to upload large files in multiple parts.\n### June, 2024Jun 06Update\n- Parallel function calling\ncan be disabled in Chat Completions and the Assistants API by passing\n`parallel_tool_calls=false`.\n- .NET SDK launched in Beta.\n- Added support for file search customizations .\n### May, 2024May 15Update\n- Added support for archiving projects . Only organization owners can access this functionality.\n- Added support for setting cost limits on a per-project basis for pay as you go customers.\n- Released GPT-4o in the API.\nGPT-4o is our fastest and most affordable flagship model.\n- Added support for image inputs to the Assistants API.\n- Added support for fine-tuned models to the Batch API .\n- Added\n`stream_options: {\"include_usage\": true}`parameter to the Chat Completions and Completions APIs.\nSetting this gives developers access to usage stats when using streaming.\n- Added a new endpoint to delete a message from a thread in the Assistants API.\n### April, 2024Apr 29Update\n- Added a new\nfunction calling option\n`tool_choice: \"required\"`to the Chat Completions and Assistants APIs.\n- Added a guide for the Batch API and Batch API support for embeddings models\n- Introduced a series of updates to the Assistants API , including a new file search tool allowing up to 10,000 files per assistant, new token controls, and support for tool choice.\n- Introduced project based hierarchy for organizing work by projects, including the ability to create API keys and manage rate and cost limits on a per-project basis (cost limits available only for Enterprise customers).\n- Released Batch API\n- Released GPT-4 Turbo with Vision in general availability in the API\n- Added support for seed in the fine-tuning API\n...\n- Added support for temperature and assistant message creation in the Assistants API\n- Added support for streaming in the Assistants API\n...\n- Added\n`timestamp_granularities`parameter to the Audio API\n### January, 2024Jan 25Update\n- Released embedding V3 models and an updated GPT-4 Turbo preview\n- Added\n`dimensions`parameter to the Embeddings API\n...\n### November, 2023Nov 30Update\n- Released OpenAI Deno SDK\n- Released GPT-4 Turbo Preview , updated GPT-3.5 Turbo, GPT-4 Turbo with Vision, Assistants API, DALL·E 3 in the API, and text-to-speech API\n- Deprecated the Chat Completions\n...\n- Released OpenAI Python SDK V1.0\n...\n- Added function calling support to the Fine-tuning API",
        "title": "OpenAI Platform",
        "url": "https://platform.openai.com/docs/changelog/dec-15th-2023",
        "date": "2025-01-31",
        "last_updated": "2025-03-01"
      }
    ],
    "server_time": null
  }
  ````
</Accordion>

### Runtime Type Validation

Python SDK uses Pydantic for runtime type validation:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity
  from perplexity.types import SearchCreateResponse

  client = Perplexity()

  # Runtime validation ensures type safety
  try:
      search_response = client.search.create(
          query="OpenAI o-series reasoning model benchmarks",
          max_results=10
      )
      
      # Pydantic model methods for serialization
      json_data = search_response.to_json()
      dict_data = search_response.to_dict()
      
      # Type validation on field access
      first_result = search_response.results[0]
      print(f"Result type: {type(first_result)}")
      
  except ValueError as e:
      print(f"Type validation error: {e}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // TypeScript compile-time type checking
  const searchResponse: Perplexity.Search.SearchCreateResponse = await client.search.create({
      query: "OpenAI o-series reasoning model benchmarks",
      max_results: 10  // TypeScript ensures correct property names
  });

  // Serialization (already plain objects)
  const jsonData = JSON.stringify(searchResponse);
  const objectData = searchResponse; // Already a plain object

  // Type safety at compile time
  const firstResult = searchResponse.results[0];
  console.log(`Result type available in IDE: ${typeof firstResult}`);
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "169d5d3b-272a-46ca-a59d-7c218f9d5ce2",
    "results": [
      {
        "snippet": "",
        "title": "Reasoning best practices | OpenAI API",
        "url": "https://developers.openai.com/api/docs/guides/reasoning-best-practices",
        "date": null,
        "last_updated": "2026-05-21"
      },
      {
        "snippet": "",
        "title": "A Comparative Study on Reasoning Patterns of OpenAI's o1 Model",
        "url": "https://arxiv.org/html/2410.13639v1",
        "date": "2024-10-17",
        "last_updated": "2026-03-22"
      },
      {
        "snippet": "**OpenAI o1** is a generative pre-trained transformer (GPT), the first in OpenAI's \"o\" series of reasoning models.\nA preview of o1 was released by OpenAI on September 12, 2024.\no1 spends time \"thinking\" before it answers, making it better at complex reasoning tasks, science and programming than GPT-4o.\nThe full version was released to ChatGPT users on December 5, 2024.\n...\nOpenAI noted that o1 is the first of a series of \"reasoning\" models.\nOpenAI shared in December 2024 benchmark results for its successor, o3 (the name o2 was skipped to avoid trademark conflict with the mobile carrier brand named O2).\n...\no1 spends additional time thinking (generating a chain of thought) before generating an answer, which makes it better for complex reasoning tasks, particularly in science and mathematics.\n...\nOpenAI's test results suggest a correlation between accuracy and the logarithm of the amount of compute spent thinking before answering.\no1-preview performed approximately at a PhD level on benchmark tests related to physics, chemistry, and biology.\nOn the American Invitational Mathematics Examination, it solved 83% (12.5/15) of the problems, compared to 13% (1.8/15) for GPT-4o.\nIt also ranked in the 89th percentile in Codeforces coding competitions.\no1-mini is faster and 80% cheaper than o1-preview.\nIt is particularly suitable for programming and STEM-related tasks, but does not have the same \"broad world knowledge\" as o1-preview.\nOpenAI noted that o1's reasoning capabilities make it better at adhering to safety rules provided in the prompt's context window.\n...\nAccording to OpenAI's assessments, o1-preview and o1-mini crossed into \"medium risk\" in CBRN (biological, chemical, radiological, and nuclear) weapons.\nDan Hendrycks wrote that \"The model already outperforms PhD scientists most of the time on answering questions related to bioweapons.\"\n...\nAccording to OpenAI, o1 may \"fake alignment\", that is, generate a response that is contrary to accuracy and its own chain of thought, in about 0.38% of cases.\n...\nBy changing the numbers and names used in a math problem or simply running the same problem again, LLMs would perform somewhat worse than their best benchmark results.\nAdding extraneous but logically inconsequential information to the problems caused a much greater drop in performance, from −17.5% for o1-preview and −29.1% for o1-mini, to −65.7% for the worst model tested.",
        "title": "OpenAI o1 - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/OpenAI_o1",
        "date": "2024-09-12",
        "last_updated": "2026-03-31"
      },
      {
        "snippet": "",
        "title": "OpenAI O3 & O4 Mini: The First True Reasoning Agents? - YouTube",
        "url": "https://www.youtube.com/watch?v=TGnPcObHdLY",
        "date": "2025-04-16",
        "last_updated": "2026-04-08"
      },
      {
        "snippet": "",
        "title": "Safety",
        "url": "https://openai.com/index/learning-to-reason-with-llms/",
        "date": "2024-09-12",
        "last_updated": "2026-03-29"
      },
      {
        "snippet": "",
        "title": "Introducing OpenAI o3 and o4-mini",
        "url": "https://openai.com/index/introducing-o3-and-o4-mini/",
        "date": "2025-04-16",
        "last_updated": "2026-05-16"
      },
      {
        "snippet": "",
        "title": "OpenAI's o3 model scores 3% on the ARC-AGI-2 benchmark ...",
        "url": "https://forum.effectivealtruism.org/posts/CoPNbwNqDai6orZhv/openai-s-o3-model-scores-3-on-the-arc-agi-2-benchmark",
        "date": "2025-05-01",
        "last_updated": "2026-05-17"
      },
      {
        "snippet": "Built to handle hard problems — they take more time to think before responding, similar to how a person would approach a difficult task.\nThe “ OpenAI o1 preview ” model, specifically, shows incredible results for various hard problems: math, coding, and reasoning.\n...\nToday, OpenAI released the full version of the o1 model, making it production-ready for a wide range of use cases.\nIn this article, we’ll compare its capabilities with GPT-4o and Claude 3.5 Sonnet to see if it lives up to the claim.\n...\nWe compared these models across three key tasks:\nReasoning riddles, Math Problems, and Classifying customer tickets\nAlong the way, we explored the latest benchmarks, evaluated input and output token costs, assessed latency and throughput, and shared guidance on choosing the best model for your needs.\nFor up-to-date rankings, check our leaderboard , or keep reading to see the results of our evaluation.\nFrom this analysis we learn that:\nProduction apps: For apps in productions, we still recommend sing GPT-4o over o1, at least for one-off tasks like the ones we tested here.\nReasoning riddles: OpenAI o1 showed some inconsistency, refusing to answer one question and scoring 60% accuracy, similar to GPT-4o, though the difference isn’t major.\nGPT-4o is a great model for this task.\nClaude 3.5 Sonnet scored a lower accuracy of 56%.\n- Math equations: GPT-4o and the o1 model performed equally well on this task, raising questions about whether the higher cost of o1 is justified.\n- Surprisingly, the latest Claude 3.5 Sonnet lagged significantly behind, achieving only 39% accuracy on these examples.\n- Classification : All models performed similarly: GPT-4o (74%), O1 (73%), and Model 3.5 Sonnet (76%), with GPT-4o improving by 12% since September.\n- GPT-4o had the highest precision (86%) making it ideal for tasks where correct possitive predictions matter most.\nThe o1 model led in recall (82%) making it suitable when you need to capture as many TRUE cases as possible.\nThe Claude 3.5 Sonnet had best F1 score (77%) indicating robust overall classification performance.\n- Speed &amp; Cost: Given that we saw similar results across the three tasks we evaluated, we still can’t justify the cost of o1, and we recommend going with GPT-4o for most use-cases.\n- Complex Problems: Use OpenAI o1 when you need top-tier reasoning and latency isn’t a concern.\nIt’s ideal for agentic workflows with a “planning” stage, where the model creates a detailed plan that smaller, cheaper models can follow\n...\nAs expected, the new o1 models are slower due to their “reasoning” process.\nThis isn’t a drawback necessarily—it just makes them better suited for tasks where thoughtful problem-solving is essential.\nOpenAI o1 is approximately 30 times slower than GPT-4o.\nSimilarly, the o1 mini version is around 16 times slower than GPT-4o mini.\n## Cost comparison\nIt's evident that using OpenAI o1 will cost roughly 6x more than GPT-4o and Claude 3.5 Sonnet for input tokens, and about 5x more for output tokens.\n## Throughput (Output speed)\nOpenAI o1 stands out with the fastest throughput, generating 143 tokens per second.\nHowever, take this throughput data with a grain of salt — while its output speed is significantly higher than the other models, its latency, or time-to-think, is about 30x longer than GPT-4o and Claude 3.5 Sonnet.\n...\nWhen new models are released, we learn about their capabilities from benchmark data reported in the technical reports.\nThe new OpenAI o1 model improves on the most complex reasoning benchmarks:\nExceeds human PhD-level accuracy on challenging benchmark tasks in physics, chemistry, and biology on the GPQA benchmark Coding is easier — It ranks in the 89th percentile on competitive programming questions (Codeforces) It’s also very good at math — In a qualifying exam for the International Mathematics Olympiad (IMO), GPT-4o correctly solved only 13% of problems, while the reasoning model scored 83%.\nNow, this is next level.\nOn the standard ML benchmarks , it has huge improvements across the board:\n...\nThey’ve gathered over 6,000 votes, and the results show that the OpenAI o1 model is consistently ranked #1 across all categories, with Math being the most notable area of impact.\nThe o1-mini model is #1 in technical areas, #2 overall.\nCheck out the full results on this link.\n...\nThe results show that the newest model is great at complex tasks, but not preferred for some natural language tasks — suggesting that maybe the model is not the best for every use-case.\n...\nGPT-4o and the o1 model performed equally well on this task, raising questions about whether the higher cost of o1 is justified.\nSurprisingly, the latest Claude 3.5 Sonnet lagged significantly behind, achieving only 39% accuracy on these examples.\n...\nOpenAI o1 showed some inconsistency, refusing to answer one question and scoring 60% accuracy, similar to GPT-4o, though the difference isn’t major.\nGPT-4o is a great model for this task.\nClaude 3.5 Sonnet scored a lower accuracy of 56%.\n...\nWe ran the evaluation to test if the models' outputs matched our ground truth data for 100 labeled test cases, and we can see that they all got similar accuracies.\nGPT-4o got 74, O1 got 73, Claude 3.5 Sonnet got 76 answers right from total of 100.\nThis reinforces the idea that smarter, more cost-effective models without a \"reasoning module\" like o1 can perform just as well as o1, but without the added expense.\nIn a similar evaluation in September of 2024, we evaluated that GPT-4o had lower accuracy, and classified only 62 of the 100 examples correctly.\nToday, we’re seeing at a 12% improvement on this task!\n...\nToday, O1 has more production-ready properties and is starting to becomemore valuable for production use cases—though it’s best suited for those who can tolerate higher latency and need to tackle the toughest challenges.\nGPT-4O, however, remains the go-to model for many of the production use cases we see in the market.",
        "title": "Analysis: OpenAI o1 vs GPT-4o vs Claude 3.5 Sonnet - Vellum",
        "url": "https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o",
        "date": "2024-12-17",
        "last_updated": "2026-05-21"
      },
      {
        "snippet": "",
        "title": "THE RELATIONSHIP BETWEEN REASONING AND PERFORMANCE",
        "url": "http://arxiv.org/pdf/2502.15631.pdf",
        "date": null,
        "last_updated": "2025-02-25"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

## Advanced Type Patterns

### Generic Type Helpers

Create reusable typed functions:

<CodeGroup>
  ```python Python theme={null}
  from typing import TypeVar, Generic, List, Optional, Callable
  from perplexity import Perplexity
  from perplexity.types import SearchCreateResponse, ResponseCreateResponse

  T = TypeVar('T')
  R = TypeVar('R')

  class TypedPerplexityClient:
      def __init__(self, client: Perplexity):
          self.client = client
      
      def search_with_transform(
          self, 
          query: str, 
          transform: Callable[[SearchCreateResponse], T]
      ) -> T:
          """Perform search and transform the result with type safety"""
          response = self.client.search.create(query=query)
          return transform(response)
      
      def batch_search(
          self, 
          queries: List[str]
      ) -> List[SearchCreateResponse]:
          """Perform multiple searches with proper typing"""
          results = []
          for query in queries:
              response = self.client.search.create(query=query)
              results.append(response)
          return results

  # Usage with type safety
  client = TypedPerplexityClient(Perplexity())

  def extract_titles(response: SearchCreateResponse) -> List[str]:
      return [result.title for result in response.results]

  # Typed function call
  titles: List[str] = client.search_with_transform("AI research", extract_titles)
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class TypedPerplexityClient {
      constructor(private client: Perplexity) {}
      
      async searchWithTransform<T>(
          query: string,
          transform: (response: Perplexity.Search.SearchCreateResponse) => T
      ): Promise<T> {
          const response = await this.client.search.create({ query });
          return transform(response);
      }
      
      async batchSearch(queries: string[]): Promise<Perplexity.Search.SearchCreateResponse[]> {
          const tasks = queries.map(query => 
              this.client.search.create({ query })
          );
          return Promise.all(tasks);
      }
  }

  // Usage with type safety
  const client = new TypedPerplexityClient(new Perplexity());

  function extractTitles(response: Perplexity.Search.SearchCreateResponse): string[] {
      return response.results.map(result => result.title);
  }

  // Typed function call with full intellisense
  const titles: string[] = await client.searchWithTransform("AI research", extractTitles);
  ```
</CodeGroup>

### Custom Type Guards

Create type guards for safer type checking:

<CodeGroup>
  ```python Python theme={null}
  from typing import Union, TypeGuard
  from perplexity.types import (
      SearchCreateResponse,
      ResponseCreateResponse,
      SearchResult
  )

  def is_search_response(
      response: Union[SearchCreateResponse, ResponseCreateResponse]
  ) -> TypeGuard[SearchCreateResponse]:
      """Type guard to check if response is a search response"""
      return hasattr(response, 'results')

  def is_valid_search_result(result: SearchResult) -> TypeGuard[SearchResult]:
      """Type guard to validate search result structure"""
      return (
          hasattr(result, 'title') and 
          hasattr(result, 'url') and 
          hasattr(result, 'snippet') and
          result.title is not None and
          result.url is not None
      )

  # Usage
  def process_response(
      response: Union[SearchCreateResponse, ResponseCreateResponse]
  ) -> None:
      if is_search_response(response):
          # Python type checker now knows this is SearchCreateResponse
          for result in response.results:
              if is_valid_search_result(result):
                  print(f"Valid result: {result.title}")
              else:
                  print("Invalid result format")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  function isSearchResponse(
      response: Perplexity.Search.SearchCreateResponse | Perplexity.StreamChunk
  ): response is Perplexity.Search.SearchCreateResponse {
      return 'results' in response;
  }

  function isValidSearchResult(result: { title: string; url: string; snippet: string }): boolean {
      return (
          typeof result.title === 'string' &&
          typeof result.url === 'string' &&
          typeof result.snippet === 'string' &&
          result.title.length > 0 &&
          result.url.length > 0
      );
  }

  // Usage
  function processResponse(
      response: Perplexity.Search.SearchCreateResponse | Perplexity.StreamChunk
  ): void {
      if (isSearchResponse(response)) {
          // TypeScript now knows this is SearchCreateResponse
          response.results.forEach(result => {
              if (isValidSearchResult(result)) {
                  console.log(`Valid result: ${result.title}`);
              } else {
                  console.log("Invalid result format");
              }
          });
      }
  }
  ```
</CodeGroup>

## Response Type Utilities

### Extracting Nested Types

Work with nested response structures safely:

<CodeGroup>
  ```python Python theme={null}
  from typing import List, Optional
  from perplexity import Perplexity
  from perplexity.types import (
      SearchCreateResponse,
      SearchResult,
      ResponseCreateResponse
  )

  class ResponseUtils:
      @staticmethod
      def extract_search_titles(response: SearchCreateResponse) -> List[str]:
          """Extract all search result titles with type safety"""
          return [result.title for result in response.results if result.title]
      
      @staticmethod
      def extract_search_urls(response: SearchCreateResponse) -> List[str]:
          """Extract all search result URLs with type safety"""
          return [result.url for result in response.results if result.url]
      
      @staticmethod
      def get_first_search_result(
          response: SearchCreateResponse
      ) -> Optional[SearchResult]:
          """Get first search result safely"""
          return response.results[0] if response.results else None
      
      @staticmethod
      def extract_response_output(
          response: ResponseCreateResponse
      ) -> Optional[str]:
          """Extract response output safely"""
          if response.output:
              return response.output
          return None

  # Usage
  client = Perplexity()
  search_response = client.search.create(query="Python 3.13 free-threaded GIL changes")

  titles = ResponseUtils.extract_search_titles(search_response)
  urls = ResponseUtils.extract_search_urls(search_response)
  first_result = ResponseUtils.get_first_search_result(search_response)

  print(f"Found {len(titles)} results")
  if first_result:
      print(f"First result: {first_result.title}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class ResponseUtils {
      static extractSearchTitles(response: Perplexity.Search.SearchCreateResponse): string[] {
          return response.results
              .filter(result => result.title)
              .map(result => result.title);
      }
      
      static extractSearchUrls(response: Perplexity.Search.SearchCreateResponse): string[] {
          return response.results
              .filter(result => result.url)
              .map(result => result.url);
      }
      
      static getFirstSearchResult(
          response: Perplexity.Search.SearchCreateResponse
      ) {
          return response.results[0];
      }
      
      static extractChatContent(
          response: Perplexity.StreamChunk
      ): string | undefined {
          const content = response.choices[0]?.message?.content;
          // Handle content which can be string, array of chunks, or null
          if (typeof content === 'string') {
              return content;
          }
          if (Array.isArray(content)) {
              // Extract text from content chunks
              return content
                  .filter(chunk => chunk.type === 'text' && 'text' in chunk)
                  .map(chunk => (chunk as { text: string }).text)
                  .join('');
          }
          return undefined;
      }
  }

  // Usage
  const client = new Perplexity();
  const searchResponse: Perplexity.Search.SearchCreateResponse = await client.search.create({ 
      query: "Python 3.13 free-threaded GIL changes" 
  });

  const titles = ResponseUtils.extractSearchTitles(searchResponse);
  const urls = ResponseUtils.extractSearchUrls(searchResponse);
  const firstResult = ResponseUtils.getFirstSearchResult(searchResponse);

  console.log(`Found ${titles.length} results`);
  if (firstResult) {
      console.log(`First result: ${firstResult.title}`);
  }
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "915ddb6e-c856-4856-a036-330e8e021895",
    "results": [
      {
        "snippet": "Starting with the 3.13 release, CPython has support for a build of\nPython called where the\n(GIL) is disabled.\nFree-threaded execution allows for full utilization of the\navailable processing power by running threads in parallel on available CPU cores.\nWhile not all software will benefit from this automatically, programs\ndesigned with threading in mind will run faster on multi-core hardware.\nSome third-party packages, in particular ones\n...\nStarting with Python 3.13, the official macOS and Windows installers\noptionally support installing free-threaded Python binaries.\n...\nWhen building CPython from source, the configure option\nshould be used to build a free-threaded Python interpreter.\n...\nTo check if the current interpreter supports free-threading,\nand contain “free-threading build”.\nThe new function can be used to check whether\nthe GIL is actually disabled in the running process.\nThe `sysconfig.get_config_var(\"Py_GIL_DISABLED\")` configuration variable can\nbe used to determine whether the build supports free threading.\nIf the variable\nis set to `1`, then the build supports free threading.\nThis is the recommended\nmechanism for decisions related to the build configuration.\n## The global interpreter lock in free-threaded Python ¶\nFree-threaded builds of CPython support optionally running with the GIL enabled\nat runtime using the environment variable or\nthe command-line option .\nThe GIL may also automatically be enabled when importing a C-API extension\nmodule that is not explicitly marked as supporting free threading.\nA warning\nwill be printed in this case.\n...\n## Thread safety ¶\nThe free-threaded build of CPython aims to provide similar thread-safety\nbehavior at the Python level to the default GIL-enabled build.\nBuilt-in\ntypes like , , and use internal locks\nto protect against concurrent modifications in ways that behave similarly to\nthe GIL.\nHowever, Python has not historically guaranteed specific behavior for\nconcurrent modifications to these built-in types, so this should be treated\nas a description of the current implementation, not a guarantee of current or\nfuture behavior.\nNote\nIt’s recommended to use the or other synchronization\nprimitives instead of relying on the internal locks of built-in types, when\npossible.\n...\nIn the free-threaded build, some objects are .\nImmortal objects are not deallocated and have reference counts that are\nnever modified.\nThis is done to avoid reference count contention that would\nprevent efficient multi-threaded scaling.\nAs of the 3.14 release, immortalization is limited to:\n- Code constants: numeric literals, string literals, and tuple literals\ncomposed of other constants.\n- Strings interned by .\n### Frame objects ¶\nIt is not safe to access from a\nobject if that frame is currently executing in another thread, and doing so may\ncrash the interpreter.\n### Iterators ¶\nIt is generally not thread-safe to access the same iterator object from\nmultiple threads concurrently, and threads may see duplicate or missing\nelements.\n### Single-threaded performance ¶\nThe free-threaded build has additional overhead when executing Python code\ncompared to the default GIL-enabled build.\nThe amount of overhead depends\non the workload and hardware.\nOn the pyperformance benchmark suite, the\naverage overhead ranges from about 1% on macOS aarch64 to 8% on x86-64 Linux\nsystems.\n## Behavioral changes ¶\nThis section describes CPython behavioural changes with the free-threaded\nbuild.\n### Context variables ¶\nIn the free-threaded build, the flag\nis set to true by default which causes threads created with\nto start with a copy of the\nof the caller of\n. In the default GIL-enabled build, the flag\ndefaults to false so threads start with an\nempty `Context()`.\n### Warning filters ¶\nIn the free-threaded build, the flag\nis set to true by default. In the default GIL-enabled build, the flag defaults\nto false. If the flag is true then the\ncontext manager uses a context variable for warning filters. If the flag is\nfalse then `catch_warnings` modifies the global filters list,\nwhich is not thread-safe. See the module for more details.",
        "title": "Python support for free threading — Python 3.14.5 documentation",
        "url": "https://docs.python.org/3/howto/free-threading-python.html",
        "date": null,
        "last_updated": "2026-05-18"
      },
      {
        "snippet": "CPython 3.13 was released two weeks ago and this release is the most\nperformance-oriented in some time.\nAfter a quick read of the release notes, a\nfew things stand out for the impact they can have on the performance:\n- CPython can now run in **free-threaded mode**, with the global interpreter lock (GIL) disabled\n- a brand new **just-in-time** (JIT) compiler has been added\n- CPython now bundles the `mimalloc` allocator out of the box\n...\n## Free-threaded CPython\nFree-threading is an experimental feature in Python 3.13 that allows CPython to\nrun without the Global Interpreter Lock (GIL).\nThe GIL is a mutex preventing\nmultiple threads from executing Python bytecode simultaneously.\nThis design\nchoice has simplified CPython's memory management and made the C API easier to\nwork with.\nHowever, it has also been one of the most significant barriers to\nutilizing modern multi-core processors effectively.\n...\n- As expected the `threading` based implementation is the fastest when running\n**3.13t with no GIL** and the GIL is effectively not limiting the parallel execution of the threads anymore.\n- Still, when running with the free threaded build both **with** and **without** the GIL, we see a significant slowdown for all other implementations.\nThis is mostly because the free-threaded build requires the specializing adaptive interpreter to be disabled, thus clearly decreasing the performance of the other implementations.\nThis overhead should be reduced in the 3.14 release where the specializing adaptive interpreter will be thread-safe and thus will be re-enabled.\n...\nthe same.\nFrom this measurement, we can see that the new free-threaded build of\nCPython 3.13 can have a significant impact on the performance of parallel\napplications, bringing a very relevant alternative to `multiprocessing`.\nStill\nit's experimental and not yet ready for production use because of the overall\nslowdown it introduces, but it's a very promising step in the right direction!",
        "title": "State of Python 3.13 Performance: Free-Threading - CodSpeed",
        "url": "https://codspeed.io/blog/state-of-python-3-13-performance-free-threading",
        "date": "2024-11-05",
        "last_updated": "2026-05-14"
      },
      {
        "snippet": "In this video, I'll discuss how Python 3.13 is revolutionizing performance by making the Global Interpreter Lock (GIL) optional!\nLearn what the GIL is, why it exists, and the potential impacts of its removal on your Python projects.\n...\n{ts:0} the global interpreter log has been holding python back for years that's\n{ts:4} about to change with python 3.30 but there are dangers that you need to be aware of the aim of the global\n{ts:11} interpreter lock or the Gill is to protect python object access by letting only one thread at a time execute python\n{ts:19} bite code with python 3.13 the Gill can be made optional it's an experimental feature and requires a bit of work to\n{ts:27} actually remove the lock I had to download the source code compile it build it from scratch almost seems like\n{ts:34} hio doesn't want me to do this video in any case it's a big change for python but what does it actually mean will it\n{ts:41} have any effect on you I'll show you some examples where it's going to give you a massive performance boost however\n...\n{ts:56} the first place so what is the Gill the Gill was introduced used in Python 1.5 in essence this is a mutex a lock in\n{ts:64} cpython that allows only one thread at a time to execute python bite code and since cpython is an open source project\n...\n{ts:77} course this is all written in C and the interesting thing is that you can also see the actual commit that added the\n...\n{ts:102} code depending on whether the Gill is disabled or not now though cpython the default python interpreter has the Gill\n{ts:109} currently in Python 3.12 there are interpreters like jython that don't the Gill ensures threat safety in Python's\n{ts:117} memory management unfortunately that means that you can't effectively use multiple CPU cores in a multi-threaded\n{ts:124} program for heavy computations that has an effect on performance so why does the default interpreter have this look in\n{ts:132} the early days multi-threaded programs were less common than they are now and single threaded performance was the main\n{ts:138} concern locking The Interpreter was a mechanism to improve the execution time of single threaded code mainly because\n...\n{ts:239} Prim competitions what you can clearly see is that the difference between single-threaded and multi-thread is\n{ts:245} actually pretty minimal and that's because of course the Gill is there so you can't really benefit from the\n...\n{ts:283} faster but it does have some overhead and unfortunately we can't really use multi-threaded programs here because the\n{ts:290} Gill prevents us from doing that so why is the Gill becoming optional now well it's been requested for a long time and\n{ts:300} it's become even more requested with the hype of AI the python Community has been advocating for a solution to the gills\n...\n{ts:333} go over the plan in the short term python version 3.13 or possibly 3.14 which by the way should definitely\n{ts:341} be called piy th the no Gill build is most likely to be in experimental mode meaning that it's going to be on you\n{ts:350} will still have the Gill by default and the main idea is that the developers just want to gain insights into how it's\n{ts:357} being used it's kind of like a trial so really don't rely on that feature in production just yet in the midterm once\n{ts:364} the core team is confident that no Guild builds are more stable it's going to become a supported option but still not\n{ts:370} the default the estimation is that this may take a year or two but of course that could be longer now in the long\n{ts:376} term the goal is for the no Gill build to become the default eliminating the Gill without disrupting backwards\n{ts:383} compatibility the team estimates that this could take up to 5 years to reach this stage throughout this Pro process\n{ts:389} they'll evaluate regularly to ensure that it's moving along while avoiding backward compatibility struggles by the\n...\n{ts:401} Loop the link is down below so what are some of the dangers of disabling the Gill or first many packages rely on it\n{ts:409} being present or at least not having to De manually with memory safety if that goes away those packages might break and\n{ts:416} I can imagine Frameworks like Fast API SE Alchemy Jango are going to be affected by this for example fast API\n...\n{ts:442} the Gill will impact the most let me know in the comments down below another danger of removing the Gill is that it\n{ts:449} can increase increase the complexity of python I mean in the long term it's going to make python more parallel\n{ts:455} friendly however without the Gill you need to be more cautious about threat safety in your programs now I did not\n...\n{ts:483} threaded version is much faster than the single thread version but there's also another interesting thing going on here\n{ts:489} which is that the multiprocessing version is actually slower than in Python 3.12 and single thread is also\n...\n{ts:576} it's going to remove a major limitation which is great however disabling the Gill in Python is an experimental\n{ts:583} feature don't rely on it just yet there are other ways you can optimize the performance of your python code one way\n{ts:589} is to use concurrent programming with the async iio package if you want to learn more about that check out this",
        "title": "How Much FASTER Is Python 3.13 Without the GIL? - YouTube",
        "url": "https://www.youtube.com/watch?v=zWPe_CUR4yU",
        "date": "2024-08-02",
        "last_updated": "2026-03-17"
      },
      {
        "snippet": "",
        "title": "What's New In Python 3.13 — Python 3.14.5 documentation",
        "url": "https://docs.python.org/3/whatsnew/3.13.html",
        "date": null,
        "last_updated": "2026-05-19"
      },
      {
        "snippet": "In Python, the Global Interpreter Lock (GIL) has been a major hurdle in achieving true concurrency.\nHowever, with the upcoming release of Python 3.13, the GIL becomes optional!\nThis experimental feature marks a significant milestone in the evolution of Python’s multithreading capabilities.\n...\n**What’s New in Python 3.13?**\n**Python 3.13** introduces an experimental feature that allows you to disable the GIL altogether!\nThis means that threads can run more concurrently, which can lead to significant performance improvements for certain types of workloads.\nTo take advantage of this new feature, you’ll need to download and install the beta version(rc1) of Python 3.13, which includes a free-threaded build configuration.\nFrom there, you can enable or disable the GIL using environment variables or command-line options.\n...\n**How to Detect and Disable GIL in Python 3.13**\nFree-threaded CPython refers to an experimental feature that allows for full utilization of available processing power by running threads in parallel on available CPU cores.\nThis means that programs designed with threading in mind will run faster on multicore hardware.\n> To enable the free-threaded build, you would need to either compile your own interpreter using the --disable-gil option or install an experimental build that is marked as free-threaded.\nNote that this feature is still under development and may have some bugs and a substantial single-threaded performance hit.\nAdditionally, users can optionally run with the GIL enabled at runtime using the environment variable **PYTHON_GIL** or the command line option **-X gil**.\n...\nWhen we disable the Global Interpreter Lock (GIL), our multi-threaded task finishes remarkably fast — just **1.36 seconds!** This is about **six** times faster than when the GIL is active.\nInterestingly, with Python 3.13 and an active GIL, the results are very similar to those of Python 3.12, which doesn’t support disabling the GIL.",
        "title": "GIL Becomes Optional in Python 3.13: A Game-Changer ...",
        "url": "https://medium.com/@mitesh.singh.jat/gil-becomes-optional-in-python-3-13-a-game-changer-for-multithreading-4c5d28856803",
        "date": "2024-08-14",
        "last_updated": "2025-10-16"
      },
      {
        "snippet": "",
        "title": "Python 3.13: Free Threading and a JIT Compiler",
        "url": "https://realpython.com/python313-free-threading-jit/",
        "date": "2024-09-18",
        "last_updated": "2026-05-18"
      },
      {
        "snippet": "The documentation states:\n> `--disable-gil` enables experimental support for running Python without the Global Interpreter Lock (GIL): free-threading build.\n> (Source: Python 3.13 Configuration)\nIt also mentions that free-threaded execution:\n> allows for full utilization of available CPU cores by running threads in parallel.\nThe mode is experimental, with some expected bugs and a substantial single-threaded performance hit.\nFree-threaded builds support optionally running with the GIL enabled at runtime using the environment variable `PYTHON_GIL` or the command-line option `-X gil`.\n> (Source: What's New in Python 3.13)\n...\nYes, the free-threaded build is experimental including enabling the GIL at runtime.\nThe most important limitation is that you still need to compile C extensions specifically for the free-threaded build.\nLooking at https://peps.python.org/pep-0703/#backwards-compatibility:\n- Refcounting always uses biased refcounting in the free-threaded build, with the potentital associated changes in lifetimes.\n(Some objects may live longer than they would normally. I don't think this is likely to come up very often)\n- Mimalloc is always used so there are still the limitations on the memory allocator mentioned in the PEP\nMember\n...\nTo make an addition to Sam's comment,\nIMO, everything under the `--disable-gil ` build should be considered experimental.\nEvery implementation detail can be changed in a future version, and even behavior details can be changed.",
        "title": "Request for Clarification on Experimental Status of Free-Threaded Builds with GIL in CPython 3.13 · Issue #124287 · python/cpython",
        "url": "https://github.com/python/cpython/issues/124287",
        "date": "2024-09-20",
        "last_updated": "2026-04-16"
      },
      {
        "snippet": "##### Feb 05, 2026 (0:08:53)\nPython 3.13 just made history by making the Global Interpreter Lock (GIL) optional for the first time in 30+ years!\nIn this video, I'll explain what the GIL is, why it existed, and how Python finally removed it through PEP 703.\n...\n- Why Python 3.13's free-threading changes everything\n...\nPEP 703: https://peps.python.org/pep-0703/\nPython 3.13 Docs: https://docs.python.org/3.13/\nFree-Threading Build Guide: https://github.com/roshandec29/PythonGIL/tree/main?tab=readme-ov-file#part-2-python-313-revolution\n...\nAfter that, we'll explore how Python is removing the lock,\n{ts:30} including free threading, sub interpreters, and the real meaning of PEP 703.\n...\nThe\n{ts:148} GIL is a mutex, a single global lock.\nIts only job is to make absolutely sure that only one thread is executing Python\n{ts:157} bite code at any given moment inside a single process.\n...\nThe GL makes this entire process thread safe by default.\nIt prevents two threads from,\n{ts:197} say, trying to change the same reference count at the exact same time and completely corrupting memory.\n...\nThe official proposal to remove the GIL, that's PEP 703, says it right there.\n...\nWhich brings us to today and the absolutely monumental engineering effort to finally make the\n{ts:308} Jill optional.\nAnd let me tell you, this is so much more than just deleting a few lines of code.\nOkay, first things first,\n{ts:315} and this is a really important detail.\nThe Jill isn't just gone.\nIt's optional.\nYou now have to compile a special\n{ts:322} freethreaded version of Python by adding a flag- disable Jill.\nThis is huge for backward compatibility with the entire\n{ts:329} existing Python world.\nSo instead of that one big lock, the new system uses what are called thread states.\nA thread\n{ts:336} has to be in the attached state before it can touch any Python objects.\nBut and this is the whole point now multiple\n{ts:342} threads can be in that attached state at the exact same time.\nThat's the key that unlocks true parallelism.\n...\nTo make any of this possible, the core of\n{ts:355} the interpreter had to be completely rearchitected.\nThat simple reference counting, it's been replaced by much\n{ts:360} more complex systems.\nThere's a whole new stop the world garbage collector that has to pause everything to clean up\n...\nAll of that new machinery\n{ts:391} for thread safety, the new reference counting, the fine grained locks, it all adds overhead.\nRight now, the estimate\n{ts:398} is that it slows down normal singlethreaded code by around 9%.\n...\nThe other massive cost isn't in performance, it's in the ecosystem.\n...\n{ts:416} protect them.\nEvery single one now needs to be checked and likely updated to be safe in this new free threaded world.\n...\nNow that the lock is\n{ts:510} optional, Python is more powerful.\nYes, but it's also more dangerous.",
        "title": "Python's GIL is FINALLY Gone! 🔥 Python 3.13 Free-Threading Explained",
        "url": "https://www.youtube.com/watch?v=fXJ1oveqsR8",
        "date": "2026-02-05",
        "last_updated": "2026-05-15"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

### Custom Response Mappers

Create typed mappers for domain-specific data structures:

<CodeGroup>
  ```python Python theme={null}
  from typing import List, Optional, Dict, Any
  from dataclasses import dataclass
  from perplexity import Perplexity
  from perplexity.types import SearchCreateResponse, SearchResult

  @dataclass
  class SimplifiedSearchResult:
      title: str
      url: str
      snippet: str
      domain: str

  @dataclass
  class SearchSummary:
      query: str
      total_results: int
      results: List[SimplifiedSearchResult]
      domains: List[str]

  class SearchResponseMapper:
      @staticmethod
      def to_simplified(response: SearchCreateResponse, query: str) -> SearchSummary:
          """Convert API response to simplified domain model"""
          simplified_results = []
          domains = set()
          
          for result in response.results:
              if result.title and result.url and result.snippet:
                  # Extract domain from URL
                  try:
                      from urllib.parse import urlparse
                      domain = urlparse(result.url).netloc
                      domains.add(domain)
                      
                      simplified_results.append(SimplifiedSearchResult(
                          title=result.title,
                          url=result.url,
                          snippet=result.snippet,
                          domain=domain
                      ))
                  except Exception:
                      # Skip invalid URLs
                      continue
          
          return SearchSummary(
              query=query,
              total_results=len(simplified_results),
              results=simplified_results,
              domains=list(domains)
          )

  # Usage with type safety
  client = Perplexity()
  query = "PyTorch versus JAX performance benchmarks for large language model training"
  api_response = client.search.create(query=query)
  summary: SearchSummary = SearchResponseMapper.to_simplified(api_response, query)

  print(f"Query: {summary.query}")
  print(f"Results: {summary.total_results}")
  print(f"Unique domains: {len(summary.domains)}")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  interface SimplifiedSearchResult {
      title: string;
      url: string;
      snippet: string;
      domain: string;
  }

  interface SearchSummary {
      query: string;
      totalResults: number;
      results: SimplifiedSearchResult[];
      domains: string[];
  }

  class SearchResponseMapper {
      static toSimplified(response: Perplexity.Search.SearchCreateResponse): SearchSummary {
          const simplifiedResults: SimplifiedSearchResult[] = [];
          const domains = new Set<string>();
          
          for (const result of response.results) {
              if (result.title && result.url && result.snippet) {
                  try {
                      const domain = new URL(result.url).hostname;
                      domains.add(domain);
                      
                      simplifiedResults.push({
                          title: result.title,
                          url: result.url,
                          snippet: result.snippet,
                          domain
                      });
                  } catch {
                      // Skip invalid URLs
                      continue;
                  }
              }
          }
          
          return {
              query: '',
              totalResults: simplifiedResults.length,
              results: simplifiedResults,
              domains: Array.from(domains)
          };
      }
  }

  // Usage with type safety
  const client = new Perplexity();
  const apiResponse: Perplexity.Search.SearchCreateResponse = await client.search.create({ 
      query: "PyTorch versus JAX performance benchmarks for large language model training" 
  });
  const summary: SearchSummary = SearchResponseMapper.toSimplified(apiResponse);

  console.log(`Query: ${summary.query}`);
  console.log(`Results: ${summary.totalResults}`);
  console.log(`Unique domains: ${summary.domains.length}`);
  ```
</CodeGroup>

<Accordion title="Response">
  ````json theme={null}
  {
    "id": "e48a6f66-7d8a-4dfd-aa79-342ae22199b6",
    "results": [
      {
        "snippet": "### Performance\n*In this section, we will explore two main implementations in Machine Learning, one suitable for large datasets, working in a streaming fashion, and another ideal for smaller datasets, which can fully fit in the memory of GPU.*\n**Out-of-the-box implementation (stream-based)**\n|Pytorch|Pytorch lightning|Tensorflow + Keras|JAX|\n|--|--|--|--|\n|232s (180s with native loader)|180s|64s|84s|\nIn this setup, we load data in a streaming fashion, so each image is loaded via a data loader when needed.\nPlenty of ways to tune each setup further, but here, we aim for simple, out-of-the-box implementation.\nOur results show that Tesorflow and JAX are faster, while Pytroch and Pytorch lightning are slower.\nThe reason behind it is straightforward: Pytorch and Pytorch lightning use PIL-based image loading, while Tensorflow and FLAX use TF native implementation.\nWhen experimenting with a custom-defined Dataloader for Pytorch (via torchvision.io.read_image()), it was possible to reduce the processing time by 22% (down to 180s).\nThis is still significantly slower than TF processing (under the hood using highly optimised tf.io.read_file()).\n**All in-memory implementation (memory-based)**\nIn contrast to the previous setup, in this one, we tried a subset of 3/10 classes due to memory limitations) and placed the whole dataset on the GPU (limiting the effect of slower DataLoaders).\nIn this setup, Pytorch seems significantly faster than other solutions, PyTorch Lightning and JAX have similar times, and Tensorflow is the slowest.\nThis might indicate that Pytorch Lightning and Keras might have certain extra overhead due to their additional features.",
        "title": "ML Engineer comparison of Pytorch, TensorFlow, JAX, and ...",
        "url": "https://softwaremill.com/ml-engineer-comparison-of-pytorch-tensorflow-jax-and-flax/",
        "date": "2024-09-24",
        "last_updated": "2026-05-27"
      },
      {
        "snippet": "The predictability of pure functions and functional programming unlocks many benefits in JAX, such as Just-In-Time (JIT) compilation, where the XLA compiler can significantly optimize code on GPUs or TPUs, for major speed-ups.\n...\nWith PyTorch, you calculate the gradients with `loss.backward()`, triggering AutoGrad to follow the computation graph from `loss` to compute the gradients.\n...\nThe key takeaway is that the training loops are very similar between PyTorch and JAX/Flax NNX, with most of the differences boiling down to object-oriented versus functional programming.\nAlthough there’s a slight learning curve to functional programming and thinking about gradients of functions, it enables many of the aforementioned benefits in JAX, e.g., JIT compilation and automatic parallelization.\nFor example, just adding the `@nnx.jit` annotations to the above functions speeds up training the model for 500 epochs from 6.25 minutes to just 1.8 minutes with a P100 GPU on Kaggle!\nYou’ll see similar speedups with the same code across CPUs, TPUs, and even non-NVIDIA GPUs.",
        "title": "A guide to JAX for PyTorch developers",
        "url": "https://cloud.google.com/blog/products/ai-machine-learning/guide-to-jax-for-pytorch-developers",
        "date": "2025-01-07",
        "last_updated": "2026-05-22"
      },
      {
        "snippet": "",
        "title": "TensorFlow vs PyTorch vs JAX: Performance Benchmark",
        "url": "https://apxml.com/posts/tensorflow-vs-pytorch-vs-jax-performance-benchmark",
        "date": "2025-03-24",
        "last_updated": "2026-03-18"
      },
      {
        "snippet": "Built on functional programming principles and composable transformations, JAX offers automatic differentiation, just-in-time compilation, and parallel execution, making it particularly well-suited for scalable and efficient model training on modern hardware accelerators.\n...\nJAX, a newer framework, at a high -level is simpler and more flexible than PyTorch for creating high-performance machine learning code.\n...\nComparing the performance and speed of JAX and PyTorch, JAX works well on hardware accelerators such as GPUs and TPUs, leading to potentially faster performance in specific scenarios.\nHowever, PyTorch’s longer tenure and larger community translate to more available resources for optimizing performance.\nFurthermore, automatic differentiation stands as a significant feature in effectively training deep learning models.\nPyTorch’s autograd package offers a straightforward method for computing gradients and adjusting model parameters.\nMeanwhile, JAX builds upon Autograd and elevates automatic differentiation by integrating its XLA (Accelerated Linear Algebra) backend.\n...\n## Critical Points for Pytorch and JAX\n- JAX performance increases when using GPUs to run the code and further the performance increases when using JIT compilation.\nThis provides a greater advantage as GPUs utilize parallelization, which provides faster performance than CPUs.\n- JAX has excellent built-in support for parallelism across multiple devices, surpassing other frameworks commonly utilized for machine learning tasks like PyTorch and TensorFlow.\n- JAX provides Auto differentiation with the grad() function, this function comes in handy while training a deep neural network.\nAs DNN requires backpropagation, JAX utilizes an analytical gradient solver instead of using other sophisticated techniques.\nIt essentially breaks down the function’s structure and applies the chain rule to compute gradients.\n- Pytorch combines Torch’s efficient and adaptable GPU-accelerated backend libraries with a user-friendly Python frontend.\nIt provides prototyping, clear code readability, and extensive support for diverse deep-learning models.\n-\n...\nThey share similarities with NumPy’s ndarrays, with the added capability of GPU acceleration for faster computation.\n...\nThe code below compares the execution time of matrix multiplication using JAX and PyTorch.\nIt generates large matrices of 1000x1000 and measures the time taken to perform the multiplication operation using both libraries.\n...\nstart_time = time.time()\n...\ntorch_execution_time = time.time() - start_time\nprint(\"JAX execution time:\", jax_execution_time, \"seconds\")\nprint(\"PyTorch execution time:\", torch_execution_time, \"seconds\")\n```\nJAX execution time: 0.00592041015625 seconds\nPyTorch execution time: 0.017140865325927734 seconds\n...\nIn conclusion, both PyTorch and JAX offer powerful frameworks for machine learning and developing deep neural networks.\nEach framework comes with its strengths and areas of expertise.\nPyTorch excels in its ease of use, extensive community support, and flexibility for rapid prototyping and experimentation, making it an ideal choice for many deep-learning projects.\nOn the other hand, JAX shines in its performance optimization, functional programming paradigm, and seamless integration with hardware accelerators, making it a preferred framework for high-performance computing and research at scale.\nUltimately, the choice between PyTorch and JAX depends on the project’s specific requirements, balancing ease of development against performance and scalability needs.",
        "title": "Comparing PyTorch and JAX",
        "url": "https://www.digitalocean.com/community/tutorials/pytorch-vs-jax",
        "date": "2024-12-20",
        "last_updated": "2026-05-16"
      },
      {
        "snippet": "",
        "title": "Deep Learning in Practice: A Technical Comparison of ...",
        "url": "https://medium.com/@nijesh-kanjinghat/deep-learning-in-practice-a-technical-comparison-of-pytorch-and-jax-6458a115dcde",
        "date": "2025-09-25",
        "last_updated": "2025-10-22"
      },
      {
        "snippet": "",
        "title": "JAX vs PyTorch 2.0 vs TensorFlow 3.0: Comparison 2026 - Index.dev",
        "url": "https://www.index.dev/skill-vs-skill/ai-pytorch2-vs-tensorflow3-vs-jax",
        "date": null,
        "last_updated": "2026-03-27"
      },
      {
        "snippet": "This blog uses the ViT classification models of varying sizes to benchmark the training performance of PyTorch and JAX versions on the Vertex AI Platform under different machine configurations.\nThe goal is to:\n- Benchmark OSS ViT training for both PyTorch and JAX frameworks.\n- Benchmark OSS ViT L16, H14, g14, and G14 models.\n- Benchmark OSS ViT PyTorch training with A100 GPUs.\n- Benchmark OSS ViT JAX training with A100 GPUs and TPU V3 accelerators.\n...\nFor both the PyTorch and JAX experiments, the following evaluation metrics are\ncollected:\n- Throughput: Images-per-second observed for training.\n- Cost: The training-cost-per-epoch (USD).\n...\nThe following section provides observations and conclusions for these results.\n## Observation and Conclusions\n- Training with JAX TPU V3 POD with 32 cores costs 33% less than the PyTorch GPU\n8 A100-40GBs runs.\n- Training with JAX GPU 8 A100-40GBs costs 23% less than the PyTorch GPU 8\nA100-40GBs runs.\n- JAX TPU V3 POD with 32 cores was 4x faster and slightly more cost-effective\nthan the JAX TPU V3 8 core run for the ViT-large model.\nThis indicates that it\nmight be better to use more cores.\nThe JAX TPU V3 speed scales very well with\nthe number of cores.\n- Cloud TPU VM training speed numbers were the same as the Vertex AI for\nTPU V3 8 cores.\nThe dataset was copied to the docker in both the cases.\n- The training-cost-per-epoch increases with the model size irrespective of the\nframework.",
        "title": "vertex-ai-samples/community-content/vertex_model_garden/benchmarking_reports/jax_vit_benchmarking_report.md at main · GoogleCloudPlatform/vertex-ai-samples",
        "url": "https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/community-content/vertex_model_garden/benchmarking_reports/jax_vit_benchmarking_report.md",
        "date": "2021-05-27",
        "last_updated": "2025-06-05"
      },
      {
        "snippet": "Benchmark scripts for comparing the UvA Deep Learning Tutorials in PyTorch and JAX.\nThe scripts are reduced versions of the tutorials, and save the runtimes of each model in a logging file in the `logs/` directory.\n...\nThe scripts have been executed with PyTorch v1.11 and JAX v0.3.13.\n...\nTo run all benchmarks, simply run `bash eval_all.sh`.\nAfterwards, you can find the evaluated runtimes in the `logs/` folder.\n## Benchmark times\nWe report the runtimes for all models on an NVIDIA RTX3090 GPU with 24-core CPU.\nThe times are averaged over two runs, which commonly have a standard deviation of <5%.\n### Tutorial 5: Inception, ResNet and DenseNet\n|Models|PyTorch|JAX|\n|--|--|--|\n|GoogleNet|53min 50sec|16min 10sec|\n|ResNet|20min 47sec|7min 51sec|\n|Pre-Activation ResNet|20min 57sec|8min 25sec|\n|DenseNet|49min 23sec|20min 1sec|\n### Tutorial 6: Transformers and Multi-Head Attention\n|Models|PyTorch|JAX|\n|--|--|--|\n|Reverse Sequence|0min 26sec|0min 7sec|\n|Anomaly Detection|16min 34sec|3min 45sec|\n### Tutorial 9: Deep Autoencoders\n|Models|PyTorch|JAX|\n|--|--|--|\n|AE - 64 latents|13min 10sec|7min 10sec|\n|AE - 128 latents|13min 11sec|7min 10sec|\n|AE - 256 latents|13min 11sec|7min 11sec|\n|AE - 384 latents|13min 12sec|7min 14sec|\n### Tutorial 11: Normalizing Flows\n|Models|PyTorch|JAX|\n|--|--|--|\n|MNIST Flow - Simple|2hrs 37min 29sec|1hrs 17min 59sec|\n|MNIST Flow - VarDeq|3hrs 25min 10sec|1hrs 36min 56sec|\n|MNIST Flow - Multiscale|2hrs 17min 10sec|57min 57sec|\n### Tutorial 15: Vision Transformer\n|Models|PyTorch|JAX|\n|--|--|--|\n|Vision Transformer|28min 40sec|27min 10sec|",
        "title": "GitHub - phlippe/uvadlc_notebooks_benchmarking: Benchmark scripts for comparing tutorials in PyTorch and JAX",
        "url": "https://github.com/phlippe/uvadlc_notebooks_benchmarking",
        "date": "2022-07-03",
        "last_updated": "2026-04-16"
      },
      {
        "snippet": "So I decided to implement the same model in both and compare.\nHere’s the top level summary:\n**PyTorch gets 1.11 iterations per second and JAX gets 1.24it/s (12% better)** on a Google Colab notebook with a P100.\nIn addition, **JAX is more memory efficient, the PyTorch model OOMs with more than 62 examples at a time and JAX can get up to 79** (at 1.01it/s, or 79.79 examples per second vs PyTorch’s 68.82 with the smaller batch size).\nMeanwhile TPUs are kind of absurd.\nTorch on XLA theoretically exists, but I don’t know of anyone who’s actually gotten it to work.\nWhen I was testing it my code\n*segfaulted*.\nTPUs work very smoothing with JAX though.\nI was accepted in the TPU Research Cloud (formerly TFRC), and a TPUv3-8 can run through 2,591 examples per second with a batch size of 3,032.\n...\nThe model is a simple, byte-level, autoregressive transformer language model trained on enwik9.\n...\nI let the model train for around four days on a TPUv3-8.\nI was surprised by how well it works.",
        "title": "JAX vs PyTorch: A simple transformer benchmark - Echo Nolan's Blog",
        "url": "https://www.echonolan.net/posts/2021-09-06-JAX-vs-PyTorch-A-Transformer-Benchmark.html",
        "date": "2021-09-06",
        "last_updated": "2025-11-03"
      }
    ],
    "server_time": null
  }
  ````
</Accordion>

## IDE Integration

### Enhanced Development Experience

Maximize IDE support with proper type usage:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity
  from perplexity.types import SearchCreateResponse
  from typing import TYPE_CHECKING

  if TYPE_CHECKING:
      # Import types only for type checking (no runtime cost)
      from perplexity.types import ResponseCreateResponse as ChatResponse

  class EnhancedClient:
      def __init__(self):
          self.client = Perplexity()
      
      def search(self, query: str, **kwargs) -> SearchCreateResponse:
          """
          Perform search with full type hints
          
          Args:
              query: Search query string
              **kwargs: Additional search parameters
              
          Returns:
              SearchCreateResponse: Typed search results
          """
          return self.client.search.create(query=query, **kwargs)
      
      def chat(self, message: str, model: str = "sonar") -> "ChatResponse":
          """
          Chat completion with type hints

          Args:
              message: User message
              model: Model to use for completion

          Returns:
              ChatResponse: Typed chat response
          """
          return self.client.chat.completions.create(
              model=model,
              messages=[{"role": "user", "content": message}]
          )

  # Usage with full IDE support
  enhanced_client = EnhancedClient()

  # IDE provides full autocomplete and type checking
  search_result = enhanced_client.search("Python tutorials")
  print(search_result.results[0].title)  # Full intellisense available

  chat_result = enhanced_client.chat("Explain decorators")
  # Access content safely with type checking
  if hasattr(chat_result, 'output') and chat_result.output:
      print(chat_result.output)  # Type-safe access
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class EnhancedClient {
      private client: Perplexity;
      
      constructor() {
          this.client = new Perplexity();
      }
      
      /**
       * Perform search with full type hints
       */
      async search(
          query: string, 
          options?: Partial<Perplexity.Search.SearchCreateParams>
      ): Promise<Perplexity.Search.SearchCreateResponse> {
          return this.client.search.create({ 
              query, 
              ...options 
          });
      }
      
      /**
       * Chat completion with type hints
       */
      async chat(
          message: string, 
          model: string = "sonar"
      ): Promise<Perplexity.StreamChunk> {
          return this.client.chat.completions.create({
              model,
              messages: [{ role: "user", content: message }]
          });
      }
  }

  // Usage with full IDE support
  const enhancedClient = new EnhancedClient();

  // IDE provides full autocomplete and type checking
  const searchResult = await enhancedClient.search("Python tutorials");
  console.log(searchResult.results[0].title); // Full intellisense available

  const chatResult = await enhancedClient.chat("Explain decorators");
  // Content can be string, array of chunks, or null - handle appropriately
  const content = chatResult.choices[0]?.message?.content;
  if (typeof content === 'string') {
      console.log(content); // Type-safe access
  }
  ```
</CodeGroup>

## Type Safety Best Practices

<Steps>
  <Step title="Always use type imports">
    Import and use specific types for better IDE support and error catching.

    <CodeGroup>
      ```python Python theme={null}
      # Good: Specific type imports
      from typing import List
      from perplexity.types import SearchCreateResponse, SearchResult

      def process_search(response: SearchCreateResponse) -> List[str]:
          return [result.title for result in response.results]
      ```

      ```typescript TypeScript theme={null}
      // Good: Use namespace types for type safety
      import Perplexity from '@perplexity-ai/perplexity_ai';

      function processSearch(response: Perplexity.Search.SearchCreateResponse): string[] {
          return response.results.map(result => result.title);
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Use type guards for runtime safety">
    Implement proper type checking for dynamic data.

    <Warning>
      TypeScript types are compile-time only. Use type guards for runtime validation.
    </Warning>
  </Step>

  <Step title="Leverage generic types">
    Create reusable typed functions and classes for common patterns.

    <Tip>
      Generic types help maintain type safety while providing flexibility.
    </Tip>
  </Step>

  <Step title="Document with types">
    Use type annotations as documentation for better code maintainability.

    <CodeGroup>
      ```python Python theme={null}
      def analyze_search_results(
          response: SearchCreateResponse,
          min_score: float = 0.5
      ) -> Dict[str, Any]:
          """
          Analyze search results with scoring
          
          Args:
              response: Search API response
              min_score: Minimum quality score threshold
              
          Returns:
              Analysis results with scores and recommendations
          """
          # Implementation with type safety
      ```

      ```typescript TypeScript theme={null}
      /**
       * Analyze search results with scoring
       */
      function analyzeSearchResults(
          response: Perplexity.Search.SearchCreateResponse,
          minScore: number = 0.5
      ): { scores: number[]; recommendations: string[] } {
          // Implementation with type safety
      }
      ```
    </CodeGroup>
  </Step>
</Steps>

## Related Resources

<CardGroup>
  <Card title="Error Handling" icon="alert-triangle" href="/docs/sdk/error-handling">
    Type-safe error handling patterns
  </Card>

  <Card title="Best Practices" icon="star" href="/docs/sdk/best-practices">
    Type safety in production code
  </Card>
</CardGroup>
