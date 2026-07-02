---
title: "Search Language Filter"
source: https://docs.perplexity.ai/docs/search/filters/language-filter
path: docs/search/filters/language-filter
---

<Note>
  The `search_language_filter` parameter allows you to filter search results by language using ISO 639-1 language codes. Only results in the specified languages will be returned.
</Note>

<Info>
  Language codes must be valid 2-letter ISO 639-1 codes (e.g., "en", "ru", "fr"). You can filter by up to 10 languages per request.
</Info>

## Overview

The language filter for the Search API allows you to control which search results are returned by limiting them to specific languages. This is particularly useful when you need to:

* Search for content in specific languages
* Conduct multilingual research across multiple languages
* Focus on regional content in local languages
* Build language-specific applications or features

The `search_language_filter` parameter accepts an array of ISO 639-1 language codes and returns only results that match those languages.

To filter search results by language:

```bash theme={null}
"search_language_filter": ["en", "fr", "de"]
```

This filter will be applied in addition to any other search parameters.

## Examples

**1. Single Language Filter**

This example limits search results to English language content only.

**Request Example**

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.search.create(
      query="OpenAI API release history and developer features",
      max_results=10,
      search_language_filter=["en"]
  )

  for result in response.results:
      print(f"{result.title}: {result.url}")
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.search.create({
    query: "OpenAI API release history and developer features",
    max_results: 10,
    search_language_filter: ["en"]
  });

  for (const result of response.results) {
    console.log(`${result.title}: ${result.url}`);
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "OpenAI API release history and developer features",
      "max_results": 10,
      "search_language_filter": ["en"]
    }' | jq
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

**2. Multiple Language Filter**

Search across multiple languages to gather diverse perspectives or multilingual content:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Search for content in English, French, and German
  response = client.search.create(
      query="Système d'échange de quotas d'émission de l'Union européenne: conception du dispositif et historique du prix du carbone",
      max_results=15,
      search_language_filter=["en", "fr", "de"]
  )

  for result in response.results:
      print(f"{result.title}: {result.url}")
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Search for content in English, French, and German
  const response = await client.search.create({
    query: "Système d'échange de quotas d'émission de l'Union européenne: conception du dispositif et historique du prix du carbone",
    max_results: 15,
    search_language_filter: ["en", "fr", "de"]
  });

  for (const result of response.results) {
    console.log(`${result.title}: ${result.url}`);
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "Système d'échange de quotas d'émission de l'Union européenne: conception du dispositif et historique du prix du carbone",
      "max_results": 15,
      "search_language_filter": ["en", "fr", "de"]
    }' | jq
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "fbe2ad33-45df-46bf-953d-ea32cf70ef10",
    "results": [
      {
        "snippet": "",
        "title": "Système d'Echange de Quotas d'Emission",
        "url": "https://www.ecologie.gouv.fr/politiques-publiques/systeme-dechange-quotas-demission",
        "date": "2016-10-12",
        "last_updated": "2026-04-07"
      },
      {
        "snippet": "",
        "title": "Marchés du carbone - SEQE-UE",
        "url": "https://www.ecologie.gouv.fr/politiques-publiques/marches-du-carbone-seqe-ue",
        "date": "2023-10-10",
        "last_updated": "2026-05-04"
      },
      {
        "snippet": "",
        "title": "Marchés du carbone - SEQE-UE 2",
        "url": "https://www.ecologie.gouv.fr/politiques-publiques/marches-du-carbone-seqe-ue-2",
        "date": "2026-02-16",
        "last_updated": "2026-05-22"
      },
      {
        "snippet": "",
        "title": "Système d'échange de quotas d'émission de l'Union européenne — Wikipédia",
        "url": "https://fr.wikipedia.org/wiki/Syst%C3%A8me_d'%C3%A9change_de_quotas_d'%C3%A9mission_de_l'Union_europ%C3%A9enne",
        "date": "2005-12-24",
        "last_updated": "2026-05-22"
      },
      {
        "snippet": "",
        "title": "FR",
        "url": "https://www.europarl.europa.eu/RegData/docs_autres_institutions/commission_europeenne/com/2020/0740/COM_COM(2020)0740_FR.pdf",
        "date": null,
        "last_updated": "2025-09-06"
      },
      {
        "snippet": "",
        "title": "Questions et réponses – Échange de quotas d'émission – Mettre un prix",
        "url": "https://ec.europa.eu/commission/presscorner/api/files/document/print/fr/qanda_21_3542/QANDA_21_3542_FR.pdf",
        "date": null,
        "last_updated": "2025-09-23"
      },
      {
        "snippet": "",
        "title": "Commission européenne - Questions et réponses",
        "url": "https://ec.europa.eu/commission/presscorner/api/files/document/print/fr/qanda_21_3542/QANDA_21_3542_FR.pdf&rut=0b54d265a7ec0a40fb6d973db812b879e90058194a9daf2881bfe68aec33a06b",
        "date": null,
        "last_updated": "2025-06-05"
      },
      {
        "snippet": "",
        "title": "Marché du carbone : quota et bourse, droit à polluer, acteurs",
        "url": "https://www.connaissancedesenergies.org/fiche-pedagogique/marches-du-carbone",
        "date": "2011-09-14",
        "last_updated": "2026-03-04"
      },
      {
        "snippet": "###\nLe marché du carbone est un mécanisme permettant l’**échange de droits d’émission de gaz à effet de serre (GES)**.\nIl s’agit d’une des mesures incitatives prévues par le Protocole de Kyoto signé en 1997 pour encourager les États à réduire leurs émissions polluantes et opter pour de nouvelles technologies à moindre coût.\nCe dispositif doit **faciliter la réalisation des objectifs climatiques** **collectifs**.\nAu sein d'un marché du carbone, un **plafond ** d'émissions est fixé à un niveau plus bas que le niveau d'émission réel.\nDes **quotas ** sont ensuite attribués aux responsables d'émissions de GES (pays, entreprises) :\n- si le pollueur réduit ses émissions en-dessous des quotas dont il dispose, il peut **revendre son droit à émettre non utilisé** ;\n- celui qui, au contraire, a pollué au-delà de son nombre de quotas doit en acheter à d'autres exploitants (ceux qui ne les ont pas tous utilisés).\nPour plus de flexibilité, les quotas peuvent être **empruntés** ou **épargnés**.\nLe système est **incitatif ** car le coût pour réduire les émissions est inférieur au prix du quota sur le marché.\nLe prix du quota dépend du niveau du plafond, qui est fixé en fonction des objectifs à atteindre et **abaissé chaque année**, afin de privilégier les efforts de réduction d'émissions.\n###\nSi plusieurs marchés régionaux s’établissent progressivement, l'un des plus importants est le marché du carbone de l'Union européenne (UE).\nIl couvre les émissions de GES de plusieurs secteurs (énergie, industrie lourde, trafic aérien...).\nMis en place par l’UE en 2005, le **système européen d’échange de quotas d’émissions de gaz à effet de serre (SEQE-UE)** vise à inciter les investissements dans des systèmes plus performants et plus écologiques, afin d'atteindre les objectifs climatiques de l'Union.\nLe marché européen du carbone a connu plusieurs phases, au cours desquelles de nouveaux secteurs ont successivement été intégrés (ex : le secteur de l'aviation, en 2012), tandis que le plafond annuel de quotas diminue chaque année.\nEn 2008, la crise économique a provoqué une chute du prix du carbone du fait de la baisse de l'activité économique, entraînant mécaniquement un surplus de quotas.\nDevenu moins incitatif, le SEQE-UE a fait l’objet de révisions permettant de retirer les quotas excédentaires, jusqu'à l’actuelle **phase 4 (2021-2030)**.\nOutre le système européen, la **Chine**,** premier émetteur mondial de GES**, a également mis en place un marché du carbone en **2021**.",
        "title": "Qu'est-ce que le marché du carbone ou système d'échanges de ...",
        "url": "https://www.vie-publique.fr/fiches/274841-quest-ce-que-le-marche-du-carbone-ou-systeme-dechanges-de-quotas",
        "date": "2020-06-26",
        "last_updated": "2026-05-27"
      },
      {
        "snippet": "",
        "title": "Marché des quotas carbone — Wikipédia",
        "url": "https://fr.wikipedia.org/wiki/March%C3%A9_des_quotas_carbone",
        "date": "2007-08-15",
        "last_updated": "2026-03-14"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

**3. Regional Language Search**

Focus on content from specific regions by using their local languages:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Search for Asian market news in Chinese, Japanese, and Korean
  response = client.search.create(
      query="Apple WWDC 基調講演で発表されたオンデバイスAI機能",
      max_results=10,
      search_language_filter=["zh", "ja", "ko"]
  )

  # Search for European tech news in multiple European languages
  eu_response = client.search.create(
      query="Lo más destacado del programa Y Combinator W26",
      max_results=10,
      search_language_filter=["en", "de", "fr", "es", "it"]
  )
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Search for Asian market news in Chinese, Japanese, and Korean
  const response = await client.search.create({
    query: "Apple WWDC 基調講演で発表されたオンデバイスAI機能",
    max_results: 10,
    search_language_filter: ["zh", "ja", "ko"]
  });

  // Search for European tech news in multiple European languages
  const euResponse = await client.search.create({
    query: "Lo más destacado del programa Y Combinator W26",
    max_results: 10,
    search_language_filter: ["en", "de", "fr", "es", "it"]
  });
  ```

  ```bash cURL theme={null}
  # Search for Asian market news
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "Apple WWDC 基調講演で発表されたオンデバイスAI機能",
      "max_results": 10,
      "search_language_filter": ["zh", "ja", "ko"]
    }' | jq
  ```
</CodeGroup>

<AccordionGroup>
  <Accordion title="Response — Apple WWDC 基調講演で発表されたオンデバイスAI機能">
    ```json theme={null}
    {
      "id": "5e873edb-6a76-4b00-8088-07b7350be1cc",
      "results": [
        {
          "snippet": "今年の基調講演では、iPhone、iPad、Macの中心で生成モデルのパワーとユーザーの個人的な背景を組み合わせて、驚くほど有用で関連性のあるインテリジェンスを提供するパーソナルインテリジェンスシステムであるApple Intelligenceを発表しました。\n...\n**Apple、Apple Intelligenceを発表**\nApple Intelligenceは、Appleシリコンのパワーを活用して、言語や画像を理解して生成したり、複数のアプリにわたってアクションを実行したり、ユーザーの個人的な背景にもとづいて、日々のタスクをシンプルにしてよりすばやくこなせるようにします。\nApple Intelligenceの基礎はデバイス上の処理で、ユーザーのデータを収集することなくパーソナルインテリジェンスを提供します。Private Cloud ComputeはAIにおけるプライバシーの新しい基準を打ち立て、デバイス上の処理から、専用のAppleシリコン搭載のサーバ上で実行する、より大規模なサーバベースのモデルにまで、演算能力を柔軟に拡張できます。\n...\nApple IntelligenceはAppleシリコンとNeural Engineのパワーを最大限に活用し、Mシリーズチップを搭載したすべてのMacで利用できるようになります。",
          "title": "WWDC24のハイライト",
          "url": "https://www.apple.com/jp/newsroom/2024/06/wwdc24-highlights/",
          "date": "2024-03-26",
          "last_updated": "2025-01-20"
        },
        {
          "snippet": "",
          "title": "Apple Intelligence - Apple（日本）",
          "url": "https://www.apple.com/jp/apple-intelligence/",
          "date": null,
          "last_updated": "2026-03-28"
        },
        {
          "snippet": "# Apple製デバイス全体に及ぶ新機能により、Apple Intelligenceがさらにパワフルになります\nデベロッパは、Apple Intelligenceのデバイス上の基盤モデルにアクセスして、プライバシーを保護し、インテリジェントな体験をアプリに組み込めるようになります\n**カリフォルニア州クパティーノ**Appleは本日、iPhone、iPad、Mac、Apple Watch、Apple Vision Proのユーザー体験を向上させるApple Intelligenceの新機能を発表しました。\nApple Intelligenceが実現する新たな方法によって、ユーザーはライブ翻訳のような機能を利用してコミュニケーションをとったり、ビジュアルインテリジェンスのアップデートによって画面上に表示されているものに対してより多くのことをしたり、強化されたImage Playgroundやジェン文字を使用して自分自身を表現したりできるようになります\n1。さらに、ショートカットでApple Intelligenceを直接利用できるようになったほか、デベロッパがApple Intelligenceの中核にあるデバイス上の大規模言語モデルにアクセスできるようになります。そのため、デベロッパは、パワフルかつ高速で、プライバシーが組み込まれ、ユーザーがオフラインの時にも使えるインテリジェンスに、直接アクセスできるようになります。\nこれらのApple Intelligenceの機能は、本日よりテスト用に提供され、対応するデバイスで対応する言語に設定しているユーザーは今秋から利用できるようになります。\n...\nそのため、パワフルかつ高速で、プライバシーが組み込まれ、ユーザーがオフラインの時にも使えるインテリジェンスを活用できるようになります。これにより、ユーザーが日々活用しているアプリでまったく新しいインテリジェントな体験を次々に生み出せるようになると考えています。\n...\nユーザーの前に言語の壁が立ち塞がった時は、ライブ翻訳を利用すれば、メッセージの送信や会話の際に言語をまたいでコミュニケーションをとることができます。この体験は、メッセージ、FaceTime、電話に組み込まれるもので、Appleが構築した完全にデバイス上で動作するモデルによって実現するため、ユーザーの個人的な会話のプライバシーが保たれます。\n...\n2。FaceTimeでは、話し手の声を聞きながら、翻訳されたライブキャプションによって会話についていくことができます。また、電話の通話では、会話の全体を通して、翻訳が音声で読み上げられます 3。\n...\nジェン文字とImage Playgroundは、ユーザーにさらに多くの自己表現の方法を提供します。テキストによる説明をジェン文字に変換するだけでなく、絵文字を取り入れ、それらを説明と組み合わせることによって、新しいものを作り出せるようになります。\n...\nApple Intelligenceを基盤とするビジュアルインテリジェンスがユーザーのiPhoneの画面に拡張され、ユーザーはあらゆるアプリで、画面上に表示しているものを検索し操作できます。\nビジュアルインテリジェンスはすでに、ユーザーがiPhoneのカメラを使用して周囲の対象物や場所について学ぶのに役立っていますが、これからはiPhoneの画面上に表示されているものについて、より多くのことを、より速く実行できるようになります。\n...\nビジュアルインテリジェンスは、イベントが表示されていることを認識してカレンダーへの追加を提案し\n...\nWorkout Buddyは、Apple Intelligenceを利用した、ほかに類を見ないApple Watchのワークアウト体験で、ユーザーのワークアウトのデータとフィットネス履歴を取り込み、パーソナライズされた、モチベーションを高める洞察をセッション中に生成します\n5。\n...\nAppleは、Apple Intelligenceの中核にあるデバイス上の基盤モデルをどのアプリからでも直接利用できるようにしました。\nFoundation Modelフレームワークを利用すれば、アプリのデベロッパはApple Intelligenceをベースに、無料のAI推論を利用して、インテリジェントで、オフラインでも利用でき、プライバシーが保護される新たな体験をユーザーに提供できるようになります。\n...\nショートカットがこれまで以上にパワフルで賢くなります。ユーザーは、Apple Intelligenceによって実現したまったく新しい一連のショートカットであるインテリジェントなアクションを利用することができます。作文ツールによるテキストの要約や、Image Playgroundによる画像の生成などの機能に対応する専用のアクションが提供されます。\nユーザーはデバイス上で、またはプライベートクラウドコンピューティングによって、Apple Intelligenceのモデルを直接利用し、ショートカット内で利用される情報のプライバシーを保ったまま、ほかのショートカットに送るレスポンスを生成できるようになります。\n...\nあらゆる段階でユーザーのプライバシーを保護するように設計されたApple Intelligenceは、デバイス上の処理を使用しているため、それを動かすモデルの多くは完全にデバイス上で実行されます。\n...\nこれらの新機能はすべて、本日よりdeveloper.apple.com/jpでApple Developer Programを通じてテスト用に提供されます。パブリックベータ版は来月、beta.apple.com/jaでApple Beta Software Programを通じて提供されます。対応するデバイスでApple Intelligenceを有効にし、対応言語に設定しているユーザーは、今秋からアクセスできるようになります。\n対応するデバイスにはiPhone 16の全モデル、iPhone 15 Pro、iPhone 15 Pro Max、iPad mini（A17 Pro）、M1以降を搭載したiPadとMacのモデルが含まれます。Siriとデバイスの言語は同じ対応言語に設定する必要があります。\n...\n- 電話とFaceTimeのライブ翻訳は、一対一の通話の場合に、英語（米国、英国）、フランス語（フランス）、ドイツ語、ポルトガル語（ブラジル）、スペイン語（スペイン）に対応しています。\n- ビジュアルインテリジェンスでイベントをカレンダーに追加する機能は、iPhone 16の全モデル、iPhone 15 Pro、iPhone 15 Pro Maxで、英語で利用できます。",
          "title": "Apple製デバイス全体に及ぶ新機能により、Apple Intelligenceが ...",
          "url": "https://www.apple.com/jp/newsroom/2025/06/apple-intelligence-gets-even-more-powerful-with-new-capabilities-across-apple-devices/",
          "date": "2025-09-06",
          "last_updated": "2025-11-28"
        },
        {
          "snippet": "衛星経由でのSMSメッセージにも 対応します 次は、もう一つの通信アプリである メールについてです 受信したEメールを管理するための オンデバイスのカテゴリー分け機能が 年内に登場します メッセージ",
          "title": "基調講演 - WWDC24 - ビデオ - Apple Developer",
          "url": "https://developer.apple.com/jp/videos/play/wwdc2024/101/",
          "date": null,
          "last_updated": "2026-05-12"
        },
        {
          "snippet": "今回のWWDCでは、Apple Intelligenceのアップデートもアナウンスされた。\nWWDC 2025における“目玉”の1つとして、\n**アプリ開発者に対するApple Intelligenceで使っているAIモデルの開放**が挙げられる。\nApple Intelligenceは、複数のAIモデルを組み合わせているが、特に完全オンデバイスのモデルを利用できるようになることで「応答時間の削減」「オフライン動作の保証」「プライバシー保護」を実現できる。\nAIモデルは「Foundation Modelsフレームワーク」を通して利用可能で、開発者は自分のアプリにAI機能を統合しやすくなる。\nWWDC 2024では、Apple Intelligenceの特徴として「\n**プライベートクラウドコンピューティング**」が発表された。これはより大規模なAIモデルが必要とされる場合に使われるもので、「暗号化」「匿名化」そして「一時的な処理」という3つの原則を徹底していることが特徴だ。\n...\nプライベートクラウドによるAI処理は、「Automation（オートメーション）」や新しい「Spotlight（スポットライト：検索機能）」から明示的に利用可能になる。\nWWDC 2025で発表された各OSには、その場で逐次通訳／翻訳を行う「\n**Live Translate（ライブ翻訳）**」という機能が加わる。\nライブ翻訳機能の実装に当たっては「音声認識」「自然言語処理」「音声合成」という複数のAI技術を統合し、各アプリの機能として実装している。\n例えば「Message（メッセージ）アプリ」では、会話スレッド全体の履歴から文脈を考慮した上で適切な翻訳を提供する。「FaceTimeアプリ」のリアルタイム翻訳キャプションは、オンデバイスならではの低レイテンシーを維持しながら、高精度な翻訳を動画コミュニケーションの中で実現する。\nそして「電話アプリ」での音声読み上げは、自分が発話した言葉を相手の言語でリピート発話する機能で（逆方向も可）、相手の話し方のニュアンスを文脈で保持しながら逐次通訳してくれる。",
          "title": "WWDC 2025基調講演から見るAppleの“進む道” 「UIデザイン ...",
          "url": "https://www.itmedia.co.jp/pcuser/articles/2506/10/news090_2.html",
          "date": "2025-06-11",
          "last_updated": "2025-10-21"
        },
        {
          "snippet": "",
          "title": "オンデバイス基盤モデルのためのプロンプトの設計と安全性 ...",
          "url": "https://developer.apple.com/jp/videos/play/wwdc2025/248/",
          "date": "2025-06-09",
          "last_updated": "2026-05-05"
        },
        {
          "snippet": "**Apple Intelligence**（アップル インテリジェンス）は、Appleが独自開発している人工知能プラットフォームである。2024年6月10日にWWDC2024の基調講演で、オンデバイス（小規模言語モデル）をベースとして自社サーバでの処理（Private Cloud Compute、大規模言語モデル）を組み合わせたシステムとして発表された。\n2024年10月28日からアメリカ英語での一部機能のベータテストとして、iOS 18.1, iPadOS 18.1, macOS Sequoia 15.1以降に統合され、アメリカ英語では各OSのバージョン18.2で正式にリリースされた。\n...\nOpenAIとの提携により、iOS 18.2, iPadOS 18.2, macOS Sequoia 15.2からはApple IntelligenceベースのSiriから外部のChatGPTをユーザが任意で呼び出して利用できる機能が実装されている。\n...\n2024年6月11日（日本時間）、WWDC2024にて、プライバシー保護に配慮し、パーソナルコンテキストを理解する、独自開発した生成モデルを据えるパーソナルインテリジェンスシステム（人工知能プラットフォーム）として、iOS 18、iPadOS 18、macOS Sequoiaでの全面採用と応用した多数の機能が発表された。\n...\n|18.1|15.1|2024年10月28日|- 作文ツール（校正、要約、書き換えのみ） - Siri (新しい外観、Siriに入力、文脈の改善) - スマートな返信 - 通知の概要 - 写真のクリーンアップとメモリメーカー - 割り込みを減らすフォーカスモード|\n|18.2|15.2|2024年12月11日|- さらに作文ツール強化（ChatGPTで作成、説明変更） - Image Playground - Image Wand - Siri (ChatGPT統合) - メールの分類(iPhone) - Genmoji (iPhoneとiPadのみ) - Visual Intelligence (iPhone 16/16 Pro/16 Pro Maxに対応)|\n|18.4|15.4|2025年3月31日|- 言語サポート追加（中国語、英語（インド）、英語（シンガポール）、フランス語、ドイツ語、イタリア語、日本語、韓国語、ポルトガル語、スペイン語、ベトナム語） - 優先通知 - メールの分類 (iPadとMac) - Image Playgroundスケッチ - Visual Intelligence (iPhone 15 Pro/Pro MaxとiPhone 16eに対応)|\n|26.1|26.1|2025年11月3日|ライブ翻訳- メッセージː 日本語、中国語（簡体字）、英語（英国、米国）、フランス語（フランス）、ドイツ語、イタリア語、韓国語、ポルトガル語（ブラジル）、スペイン語（スペイン） - 電話とFaceTimeː 英語（英国、米国）、フランス語（フランス）、ドイツ語、ポルトガル語（ブラジル）、スペイン語（スペイン）|\n...\n- これまでの会話内容を理解していることで、代名詞などでも文を理解する事が可能になる。また、画面上の物事についても理解する事が可能となる。個人の機密情報を検索する際であっても、オンデバイス（デバイス内での）処理となるため、機密情報が外に漏れることはなく、外部と共有する際には事前にユーザの同意が必要となる仕組みである。\n...\nApple Intelligenceを活用し、自動でアルバムを生成したり、音楽と共にスライドショーを作成する機能の機能向上とより一層複雑な検索キーワードに対応した検索機能や、意図しない写り込みを除去してくれる機能などが搭載される。\n...\nApple Intelligenceは、ユーザのプライバシーを保護するため基本的にオンデバイスで実行され、個人情報を収集することなく、情報を認識するよう設計されている。\nしかし、オンデバイスでの処理に適さない場合には、Private Cloud Computeと呼ばれるAppleシリコンによるサーバベースのデータセンターを利用し、必要最小限の情報のみを利用し、匿名化と暗号化でプライバシーを保護しながら、ユーザの提供したデータは一時利用のみで保管せず、より複雑なリクエストを処理する。",
          "title": "Apple Intelligence - Wikipedia",
          "url": "https://ja.wikipedia.org/wiki/Apple_Intelligence",
          "date": "2024-06-11",
          "last_updated": "2026-05-22"
        },
        {
          "snippet": "",
          "title": "Platforms State of the Union - WWDC24 - ビデオ - Apple Developer",
          "url": "https://developer.apple.com/jp/videos/play/wwdc2024/102/?time=2408",
          "date": null,
          "last_updated": "2026-04-07"
        },
        {
          "snippet": "# アップルの「Apple Intelligence」で新機能、あらゆるアプリがオンデバイスAIモデルへアクセスできるように\n...\n今回、新機能として、新しいFoundation Modeles frameworkにより、あらゆるアプリが、オンデバイスの大規模言語モデルにアクセスできるようになる。\nこれにより、Apple Intellgenceが利用できるアプリがサードパーティ製アプリにまで、セキュリティを担保した形で大幅に拡充される見込みだ。",
          "title": "あらゆるアプリがオンデバイスAIモデルへアクセスできるように",
          "url": "https://k-tai.watch.impress.co.jp/docs/news/2021215.html",
          "date": "2025-06-10",
          "last_updated": "2026-03-21"
        },
        {
          "snippet": "今回、新機能として、新しいFoundation Modeles frameworkにより、あらゆるアプリが、オンデバイスの大規模言語モデルにアクセスできるようになる。\nこれにより、Apple Intellgenceが利用できるアプリがサードパーティ製アプリにまで、セキュリティを担保した形で大幅に拡充される見込みだ。",
          "title": "アップルの「Apple Intelligence」で新機能、あらゆるアプリがオンデバイスAIモデルへアクセスできるように - ライブドアニュース",
          "url": "https://news.livedoor.com/article/detail/28928262/",
          "date": "2025-06-10",
          "last_updated": "2025-08-16"
        }
      ],
      "server_time": null
    }
    ```
  </Accordion>

  <Accordion title="Response — Lo más destacado del programa Y Combinator W26">
    ```json theme={null}
    {
      "id": "5ba2613b-32d0-4dd0-ac13-b5584566180c",
      "results": [
        {
          "snippet": "Didit entra en YC W26 tras recaudar ~$2M y crecer +20% MoM.\n...\n**Didit forma parte oficialmente del batch Winter 2026 de Y Combinator.**",
          "title": "Didit recauda $2M y entra en Y Combinator (W26)",
          "url": "https://didit.me/es/blog/didit-enters-y-combinator/",
          "date": "2025-12-02",
          "last_updated": "2026-05-21"
        },
        {
          "snippet": "So what have we learned about this batch so far?\n- 64% of the batch are B2B startups, with many building products across productivity, the stack for engineers and infrastructure tools.\n- The consumer category is barely represented in this batch, with only about 5% of startups building within the category.\n- Healthcare is gaining momentum, making up nearly 10% of the batch.\nNotable areas include wearable technologies and drug discovery.\n- The legal tech category is also heating up.\nThis may be driven by the rapid success of platforms like Legora (a YC company) and Harvey, both of which reached unicorn status shortly after founding.\nIt’s therefore not surprising that around 4% of this batch is building in the legal category.\n...\nIn under three weeks, over 180 startups from the latest Y Combinator batch will present to investors at the Winter ‘26 Demo Day, and this may be the strongest batch yet.\n...\nMeet the 180+ startups from YC’s latest batch who are building across the following categories:",
          "title": "Y Combinator W26: The Full Batch - by Ollie Forsyth - New Economies",
          "url": "https://www.neweconomies.co/p/yc-w26-batch",
          "date": "2026-03-05",
          "last_updated": "2026-05-24"
        },
        {
          "snippet": "",
          "title": "Ranking the Best and Worst Y Combinator W26 Companies - YouTube",
          "url": "https://www.youtube.com/watch?v=DtHP5jLgshk",
          "date": "2026-02-02",
          "last_updated": "2026-05-24"
        },
        {
          "snippet": "El **Demo Day Winter 2026 de Y Combinator (YC)** puso en vitrina 16 startups consideradas las más disruptivas de esta edición.\nLos sectores abordados son diversos, desde soluciones de **IA aplicada**, **robótica humana**, hasta plataformas para optimizar experiencias digitales y resolver problemas cotidianos.\nStartups como **LiftAI**, que ayuda a evitar el 'doomscrolling' con IA personalizada, o **NeuroDynamiX**, enfocada en el entrenamiento de robots humanoides, ejemplifican la variedad y profundidad tecnológica que YC fomenta.\n...\nLos proyectos de esta edición señalan una clara aceleración en **aplicaciones prácticas de IA** y una fuerte apuesta por la automatización de procesos empresariales.\n...\nEl Demo Day de YC Winter 2026 muestra que la innovación tecnológica sigue un ritmo acelerado, con soluciones de alto impacto que marcan tendencia para el ecosistema global.",
          "title": "Startups destacadas del YC W'26 Demo Day: análisis y tendencias",
          "url": "https://ecosistemastartup.com/startups-destacadas-del-yc-w26-demo-day-analisis-y-tendencias/",
          "date": "2026-03-26",
          "last_updated": "2026-05-21"
        },
        {
          "snippet": "**Captain** es una startup del batch **Winter 2026 de Y Combinator** que automatiza los pipelines de **Retrieval-Augmented Generation (RAG)** para archivos y datos no estructurados.\nSu propuesta central es sencilla pero poderosa: conectar tus repositorios de archivos y obtener búsquedas de conocimiento con una precisión radicalmente superior a la del RAG tradicional, pasando de un promedio del **78% al 95%** de exactitud, con citas verificables en cada resultado.\n...\nLa diferencia que Captain defiende es su enfoque en la **automatización completa del pipeline** y la mejora medible de precisión (78% → 95%) como métrica central y verificable.\n**Garry Tan**, CEO de **Y Combinator**, calificó públicamente este salto de precisión como un *step function increase* respecto al RAG estándar, lo que da credibilidad institucional al claim técnico.\n...\n**Captain (YC W26)** llega a resolver uno de los problemas más frustrantes del stack de IA moderno: construir sistemas RAG que funcionen bien en producción, no solo en demos.\nSu apuesta por la automatización total del pipeline, la mejora verificable de precisión del **78% al 95%** y una integración simple vía **API REST** lo posicionan como una herramienta relevante para cualquier founder que esté construyendo sobre datos no estructurados.",
          "title": "Captain YC W26: RAG automatizado con 95% de precisión",
          "url": "https://ecosistemastartup.com/captain-yc-w26-rag-automatizado-con-95-de-precision/",
          "date": "2026-03-13",
          "last_updated": "2026-03-26"
        },
        {
          "snippet": "# Las 16 startups más interesantes de YC en el Demo Day W26\nDesde la automatización en la arquitectura hasta la detección de drones, estas 16 startups presentaron propuestas únicas en el reciente Demo Day de Y Combinator, destacando en diversas industrias.\n...\n**AI** fue nuevamente la palabra de moda en esta última edición del **Demo Day** de **Y Combinator** (YC).\n...\nEn lugar de eso, se revisaron las 190 startups que presentaron y se dedicó el día a ver las presentaciones de las más intrigantes, para luego seleccionar las 16 que se destacaron como las más interesantes de esta abarrotada clase de YC.\n**ARC Prize Foundation**\n**Qué hace:** Crea referencias para ayudar a medir el progreso hacia la **AGI**.\n...\nEs un evento donde las startups que participan en el programa de aceleración de Y Combinator presentan sus productos e ideas a inversores y medios.\n...\n**ARC Prize Foundation**, que busca medir el progreso hacia la inteligencia artificial general (AGI).",
          "title": "Las 16 startups más interesantes de YC en el Demo Day W26",
          "url": "https://www.cadena3.com/noticia/tecnologia/las-16-startups-mas-interesantes-de-yc-en-el-demo-day-w26_534171",
          "date": "2026-03-27",
          "last_updated": "2026-05-08"
        },
        {
          "snippet": "La \"Lista de Deseos para Startups\" de Y Combinator para la primavera de 2026 enfatiza el potencial transformador de la IA en diez sectores poco explorados.\nLa incubadora destaca el cambio de la IA como generadora de contenido a una herramienta para resolver problemas complejos y remodelar industrias.\nLas áreas clave de enfoque incluyen fondos de cobertura nativos de IA, que buscan revolucionar las estrategias de inversión aprovechando la IA para un análisis de mercado integral, y empresas de servicios impulsadas por IA que mejoran la eficiencia y la escalabilidad en industrias tradicionalmente intensivas en mano de obra.\nLa lista también subraya el potencial de los servicios financieros derivados de stablecoins, ofreciendo un puente entre las finanzas tradicionales y DeFi, y la modernización de los sistemas industriales mediante la planificación de producción impulsada por IA.\nAdemás, Y Combinator ve oportunidades en mejoras de IA para operaciones gubernamentales, orientación en tiempo real con IA para trabajos físicos y el desarrollo de grandes modelos espaciales para mejorar la comprensión del mundo físico por parte de la IA.\nEstas iniciativas reflejan una tendencia más amplia de integración de la IA en diversos sectores, prometiendo avances y eficiencias significativas.",
          "title": "RFS 2026 de Y Combinator: IA transformará 10 sectores clave",
          "url": "https://phemex.com/es/news/article/y-combinators-spring-2026-rfs-highlights-ais-role-in-transforming-10-key-sectors-59256",
          "date": "2026-02-09",
          "last_updated": "2026-03-11"
        },
        {
          "snippet": "El reciente Demo Day de Y Combinator, correspondiente a la cohorte de invierno del 2026, ha traído consigo una ola de innovaciones tecnológicas, con cerca de 190 startups presentándose ante un público ávido de nuevas ideas.\nEntre ellas, se destacan 16 startups que no solo llamaron la atención, sino que prometen revolucionar diversas industrias como la salud, el transporte y el derecho.\n...\nUna de las temáticas más recurrentes ha sido la inteligencia artificial, que sigue siendo un foco de interés y desarrollo.\nCon proyectos que abarcan desde la formación de humanoides hasta herramientas que optimizan el trabajo en oficinas de arquitectura, estas startups ilustran el potencial transformador de la IA.\n...\nEntre las ofertas innovadoras, Asimov resalta por su enfoque en recopilar datos sobre movimientos humanos que pueden servir para entrenar robots humanoides, una tendencia interesante que va más allá de la simple automatización y busca incorporar elegancia en la manera en que estas máquinas realizan tareas.\n...\nPor último, CodeWisp se diferencia al permitir que cualquiera pueda crear juegos utilizando inteligencia artificial, democratizando así el desarrollo de videojuegos y abriendo las puertas a nuevas formas de expresión creativa.\nEl Demo Day de YC W26 ha demostrado una vez más que la innovación está en constante evolución, ofreciendo un vistazo al futuro donde la tecnología y la creatividad se entrelazan para generar soluciones efectivas y emocionantes.",
          "title": "Innovaciones del Demo Day: 16 Startups Fascinantes de YC",
          "url": "https://www.newstory.tips/es/articles/858/innovaciones-del-demo-day-16-startups-fascinantes-de-yc",
          "date": "2026-03-30",
          "last_updated": "2026-04-20"
        }
      ],
      "server_time": null
    }
    ```
  </Accordion>
</AccordionGroup>

**4. Combining with Other Filters**

Language filters work seamlessly with other search parameters for precise control:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  # Combine language filter with date and domain filters
  response = client.search.create(
      query="IPCC AR6 synthesis report key findings",
      max_results=20,
      search_language_filter=["en", "de"],
      search_domain_filter=["nature.com", "science.org"],
      search_recency_filter="month"
  )

  for result in response.results:
      print(f"{result.title}")
      print(f"URL: {result.url}")
      print(f"Date: {result.date}")
      print("---")
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  // Combine language filter with date and domain filters
  const response = await client.search.create({
    query: "IPCC AR6 synthesis report key findings",
    max_results: 20,
    search_language_filter: ["en", "de"],
    search_domain_filter: ["nature.com", "science.org"],
    search_recency_filter: "month"
  });

  for (const result of response.results) {
    console.log(`${result.title}`);
    console.log(`URL: ${result.url}`);
    console.log(`Date: ${result.date}`);
    console.log("---");
  }
  ```

  ```bash cURL theme={null}
  curl -X POST 'https://api.perplexity.ai/search' \
    -H 'Authorization: Bearer $PERPLEXITY_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "query": "IPCC AR6 synthesis report key findings",
      "max_results": 20,
      "search_language_filter": ["en", "de"],
      "search_domain_filter": ["nature.com", "science.org"],
      "search_recency_filter": "month"
    }' | jq
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "75c39a4e-a46c-4850-bf27-4c061186ece6",
    "results": [
      {
        "snippet": "",
        "title": "10 Big Findings from the 2023 IPCC Report on Climate Change",
        "url": "https://www.wri.org/insights/2023-ipcc-ar6-synthesis-report-climate-change-findings",
        "date": "2023-03-20",
        "last_updated": "2026-05-15"
      },
      {
        "snippet": "",
        "title": "AR6 Synthesis Report",
        "url": "https://www.ipcc.ch/report/ar6/syr/",
        "date": null,
        "last_updated": "2026-05-21"
      },
      {
        "snippet": "",
        "title": "[PDF] Climate Change 2023 Synthesis Report",
        "url": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_LongerReport.pdf",
        "date": null,
        "last_updated": "2026-05-18"
      },
      {
        "snippet": "The Synthesis Report is based on the content of the three Working Groups Assessment Reports:* WGI – The Physical Science Basis, WGII – Impacts, Adaptation and Vulnerability, WGIII – Mitigation of Climate Change*, and the three Special Reports: *Global Warming of 1.5°C*, *Climate Change and Land*, *The Ocean and Cryosphere in a Changing Climate*.\n...\nThe SYR outline agreed at the 52^nd^ Panel Session of the IPCC consists of an introduction and three main sections arranged by timeframes.\nThe first section, ‘Current Status and Trends’, covers the historical and present period.\nThe second section, ‘Long-term Climate and Development Futures’, addresses projected futures up to 2100 and beyond.\nThe final section is ‘Near-term Responses in a Changing Climate’, considers current international policy timeframes, and the time interval between now and 2030-2040.\nThis structure, substantially different to what was adopted for AR5 SYR, enables a holistic framing that integrates across the Working Groups, better enabling the SYR to cover different aspects of climate change.",
        "title": "AR6 Synthesis Report: Climate Change 2023 — IPCC",
        "url": "https://www.ipcc.ch/report/sixth-assessment-report-cycle/",
        "date": null,
        "last_updated": "2026-05-12"
      },
      {
        "snippet": "",
        "title": "[PDF] IPCC_AR6_SYR_FullVolume.pdf",
        "url": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf",
        "date": null,
        "last_updated": "2026-05-20"
      },
      {
        "snippet": "",
        "title": "Summary for Policymakers",
        "url": "https://www.ipcc.ch/report/ar6/syr/summary-for-policymakers/",
        "date": null,
        "last_updated": "2026-05-20"
      },
      {
        "snippet": "",
        "title": "SYR Longer Report - Intergovernmental Panel on Climate Change",
        "url": "https://www.ipcc.ch/report/ar6/syr/longer-report/",
        "date": null,
        "last_updated": "2026-03-21"
      },
      {
        "snippet": "",
        "title": "IPCC Secretariat",
        "url": "https://www.ipcc.ch/site/assets/uploads/2023/03/Doc5_Adopted_AR6_SYR_Longer_Report.pdf",
        "date": null,
        "last_updated": "2024-02-26"
      },
      {
        "snippet": "",
        "title": "IPCC AR6 Working Group 1: Technical Summary",
        "url": "https://www.ipcc.ch/report/ar6/wg1/chapter/technical-summary/",
        "date": null,
        "last_updated": "2026-03-18"
      },
      {
        "snippet": "",
        "title": "IPCC_AR6_SYR_SPM.pdf",
        "url": "https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_SPM.pdf",
        "date": null,
        "last_updated": "2026-05-21"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

## Parameter Reference

### `search_language_filter`

* **Type**: Array of strings
* **Format**: ISO 639-1 language codes (2 lowercase letters)
* **Description**: Filters search results to only include content in the specified languages
* **Optional**: Yes
* **Maximum**: 10 language codes per request
* **Example**: `"search_language_filter": ["en", "fr", "de"]`

## Common Language Codes

Here's a comprehensive list of frequently used ISO 639-1 language codes:

| Language   | Code | Language   | Code |
| ---------- | ---- | ---------- | ---- |
| English    | `en` | Portuguese | `pt` |
| Spanish    | `es` | Dutch      | `nl` |
| French     | `fr` | Polish     | `pl` |
| German     | `de` | Swedish    | `sv` |
| Italian    | `it` | Norwegian  | `no` |
| Russian    | `ru` | Danish     | `da` |
| Chinese    | `zh` | Finnish    | `fi` |
| Japanese   | `ja` | Czech      | `cs` |
| Korean     | `ko` | Hungarian  | `hu` |
| Arabic     | `ar` | Greek      | `el` |
| Hindi      | `hi` | Turkish    | `tr` |
| Bengali    | `bn` | Hebrew     | `he` |
| Indonesian | `id` | Thai       | `th` |
| Vietnamese | `vi` | Ukrainian  | `uk` |

<Tip>
  For a complete list of ISO 639-1 language codes, see the [ISO 639-1 standard](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
</Tip>

## Best Practices

### Language Code Validation

* **Use Valid Codes**: Always use valid 2-letter ISO 639-1 codes. Invalid codes will result in an API error.
* **Lowercase Only**: Language codes must be lowercase (e.g., "en" not "EN").
* **Client-Side Validation**: Validate language codes on the client side using a regex pattern:

<CodeGroup>
  ```python Python theme={null}
  import re

  def validate_language_code(code):
      pattern = r'^[a-z]{2}$'
      return bool(re.match(pattern, code))

  def validate_language_filters(codes):
      if len(codes) > 10:
          raise ValueError("Maximum 10 language codes allowed")
      
      for code in codes:
          if not validate_language_code(code):
              raise ValueError(f"Invalid language code: {code}")
      
      return True

  # Usage
  try:
      codes = ["en", "fr", "de"]
      validate_language_filters(codes)
      
      response = client.search.create(
          query="Apple WWDC 基調講演で発表されたオンデバイスAI機能",
          search_language_filter=codes
      )
  except ValueError as e:
      print(f"Validation error: {e}")
  ```

  ```typescript Typescript theme={null}
  function validateLanguageCode(code: string): boolean {
    const pattern = /^[a-z]{2}$/;
    return pattern.test(code);
  }

  function validateLanguageFilters(codes: string[]): void {
    if (codes.length > 10) {
      throw new Error("Maximum 10 language codes allowed");
    }
    
    for (const code of codes) {
      if (!validateLanguageCode(code)) {
        throw new Error(`Invalid language code: ${code}`);
      }
    }
  }

  // Usage
  try {
    const codes = ["en", "fr", "de"];
    validateLanguageFilters(codes);
    
    const response = await client.search.create({
      query: "Apple WWDC 基調講演で発表されたオンデバイスAI機能",
      search_language_filter: codes
    });
  } catch (error) {
    console.error("Validation error:", error.message);
  }
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "5e873edb-6a76-4b00-8088-07b7350be1cc",
    "results": [
      {
        "snippet": "今年の基調講演では、iPhone、iPad、Macの中心で生成モデルのパワーとユーザーの個人的な背景を組み合わせて、驚くほど有用で関連性のあるインテリジェンスを提供するパーソナルインテリジェンスシステムであるApple Intelligenceを発表しました。\n...\n**Apple、Apple Intelligenceを発表**\nApple Intelligenceは、Appleシリコンのパワーを活用して、言語や画像を理解して生成したり、複数のアプリにわたってアクションを実行したり、ユーザーの個人的な背景にもとづいて、日々のタスクをシンプルにしてよりすばやくこなせるようにします。\nApple Intelligenceの基礎はデバイス上の処理で、ユーザーのデータを収集することなくパーソナルインテリジェンスを提供します。Private Cloud ComputeはAIにおけるプライバシーの新しい基準を打ち立て、デバイス上の処理から、専用のAppleシリコン搭載のサーバ上で実行する、より大規模なサーバベースのモデルにまで、演算能力を柔軟に拡張できます。\n...\nApple IntelligenceはAppleシリコンとNeural Engineのパワーを最大限に活用し、Mシリーズチップを搭載したすべてのMacで利用できるようになります。",
        "title": "WWDC24のハイライト",
        "url": "https://www.apple.com/jp/newsroom/2024/06/wwdc24-highlights/",
        "date": "2024-03-26",
        "last_updated": "2025-01-20"
      },
      {
        "snippet": "",
        "title": "Apple Intelligence - Apple（日本）",
        "url": "https://www.apple.com/jp/apple-intelligence/",
        "date": null,
        "last_updated": "2026-03-28"
      },
      {
        "snippet": "# Apple製デバイス全体に及ぶ新機能により、Apple Intelligenceがさらにパワフルになります\nデベロッパは、Apple Intelligenceのデバイス上の基盤モデルにアクセスして、プライバシーを保護し、インテリジェントな体験をアプリに組み込めるようになります\n**カリフォルニア州クパティーノ**Appleは本日、iPhone、iPad、Mac、Apple Watch、Apple Vision Proのユーザー体験を向上させるApple Intelligenceの新機能を発表しました。\nApple Intelligenceが実現する新たな方法によって、ユーザーはライブ翻訳のような機能を利用してコミュニケーションをとったり、ビジュアルインテリジェンスのアップデートによって画面上に表示されているものに対してより多くのことをしたり、強化されたImage Playgroundやジェン文字を使用して自分自身を表現したりできるようになります\n1。さらに、ショートカットでApple Intelligenceを直接利用できるようになったほか、デベロッパがApple Intelligenceの中核にあるデバイス上の大規模言語モデルにアクセスできるようになります。そのため、デベロッパは、パワフルかつ高速で、プライバシーが組み込まれ、ユーザーがオフラインの時にも使えるインテリジェンスに、直接アクセスできるようになります。\nこれらのApple Intelligenceの機能は、本日よりテスト用に提供され、対応するデバイスで対応する言語に設定しているユーザーは今秋から利用できるようになります。\n...\nそのため、パワフルかつ高速で、プライバシーが組み込まれ、ユーザーがオフラインの時にも使えるインテリジェンスを活用できるようになります。これにより、ユーザーが日々活用しているアプリでまったく新しいインテリジェントな体験を次々に生み出せるようになると考えています。\n...\nユーザーの前に言語の壁が立ち塞がった時は、ライブ翻訳を利用すれば、メッセージの送信や会話の際に言語をまたいでコミュニケーションをとることができます。この体験は、メッセージ、FaceTime、電話に組み込まれるもので、Appleが構築した完全にデバイス上で動作するモデルによって実現するため、ユーザーの個人的な会話のプライバシーが保たれます。\n...\n2。FaceTimeでは、話し手の声を聞きながら、翻訳されたライブキャプションによって会話についていくことができます。また、電話の通話では、会話の全体を通して、翻訳が音声で読み上げられます 3。\n...\nジェン文字とImage Playgroundは、ユーザーにさらに多くの自己表現の方法を提供します。テキストによる説明をジェン文字に変換するだけでなく、絵文字を取り入れ、それらを説明と組み合わせることによって、新しいものを作り出せるようになります。\n...\nApple Intelligenceを基盤とするビジュアルインテリジェンスがユーザーのiPhoneの画面に拡張され、ユーザーはあらゆるアプリで、画面上に表示しているものを検索し操作できます。\nビジュアルインテリジェンスはすでに、ユーザーがiPhoneのカメラを使用して周囲の対象物や場所について学ぶのに役立っていますが、これからはiPhoneの画面上に表示されているものについて、より多くのことを、より速く実行できるようになります。\n...\nビジュアルインテリジェンスは、イベントが表示されていることを認識してカレンダーへの追加を提案し\n...\nWorkout Buddyは、Apple Intelligenceを利用した、ほかに類を見ないApple Watchのワークアウト体験で、ユーザーのワークアウトのデータとフィットネス履歴を取り込み、パーソナライズされた、モチベーションを高める洞察をセッション中に生成します\n5。\n...\nAppleは、Apple Intelligenceの中核にあるデバイス上の基盤モデルをどのアプリからでも直接利用できるようにしました。\nFoundation Modelフレームワークを利用すれば、アプリのデベロッパはApple Intelligenceをベースに、無料のAI推論を利用して、インテリジェントで、オフラインでも利用でき、プライバシーが保護される新たな体験をユーザーに提供できるようになります。\n...\nショートカットがこれまで以上にパワフルで賢くなります。ユーザーは、Apple Intelligenceによって実現したまったく新しい一連のショートカットであるインテリジェントなアクションを利用することができます。作文ツールによるテキストの要約や、Image Playgroundによる画像の生成などの機能に対応する専用のアクションが提供されます。\nユーザーはデバイス上で、またはプライベートクラウドコンピューティングによって、Apple Intelligenceのモデルを直接利用し、ショートカット内で利用される情報のプライバシーを保ったまま、ほかのショートカットに送るレスポンスを生成できるようになります。\n...\nあらゆる段階でユーザーのプライバシーを保護するように設計されたApple Intelligenceは、デバイス上の処理を使用しているため、それを動かすモデルの多くは完全にデバイス上で実行されます。\n...\nこれらの新機能はすべて、本日よりdeveloper.apple.com/jpでApple Developer Programを通じてテスト用に提供されます。パブリックベータ版は来月、beta.apple.com/jaでApple Beta Software Programを通じて提供されます。対応するデバイスでApple Intelligenceを有効にし、対応言語に設定しているユーザーは、今秋からアクセスできるようになります。\n対応するデバイスにはiPhone 16の全モデル、iPhone 15 Pro、iPhone 15 Pro Max、iPad mini（A17 Pro）、M1以降を搭載したiPadとMacのモデルが含まれます。Siriとデバイスの言語は同じ対応言語に設定する必要があります。\n...\n- 電話とFaceTimeのライブ翻訳は、一対一の通話の場合に、英語（米国、英国）、フランス語（フランス）、ドイツ語、ポルトガル語（ブラジル）、スペイン語（スペイン）に対応しています。\n- ビジュアルインテリジェンスでイベントをカレンダーに追加する機能は、iPhone 16の全モデル、iPhone 15 Pro、iPhone 15 Pro Maxで、英語で利用できます。",
        "title": "Apple製デバイス全体に及ぶ新機能により、Apple Intelligenceが ...",
        "url": "https://www.apple.com/jp/newsroom/2025/06/apple-intelligence-gets-even-more-powerful-with-new-capabilities-across-apple-devices/",
        "date": "2025-09-06",
        "last_updated": "2025-11-28"
      },
      {
        "snippet": "衛星経由でのSMSメッセージにも 対応します 次は、もう一つの通信アプリである メールについてです 受信したEメールを管理するための オンデバイスのカテゴリー分け機能が 年内に登場します メッセージ",
        "title": "基調講演 - WWDC24 - ビデオ - Apple Developer",
        "url": "https://developer.apple.com/jp/videos/play/wwdc2024/101/",
        "date": null,
        "last_updated": "2026-05-12"
      },
      {
        "snippet": "今回のWWDCでは、Apple Intelligenceのアップデートもアナウンスされた。\nWWDC 2025における“目玉”の1つとして、\n**アプリ開発者に対するApple Intelligenceで使っているAIモデルの開放**が挙げられる。\nApple Intelligenceは、複数のAIモデルを組み合わせているが、特に完全オンデバイスのモデルを利用できるようになることで「応答時間の削減」「オフライン動作の保証」「プライバシー保護」を実現できる。\nAIモデルは「Foundation Modelsフレームワーク」を通して利用可能で、開発者は自分のアプリにAI機能を統合しやすくなる。\nWWDC 2024では、Apple Intelligenceの特徴として「\n**プライベートクラウドコンピューティング**」が発表された。これはより大規模なAIモデルが必要とされる場合に使われるもので、「暗号化」「匿名化」そして「一時的な処理」という3つの原則を徹底していることが特徴だ。\n...\nプライベートクラウドによるAI処理は、「Automation（オートメーション）」や新しい「Spotlight（スポットライト：検索機能）」から明示的に利用可能になる。\nWWDC 2025で発表された各OSには、その場で逐次通訳／翻訳を行う「\n**Live Translate（ライブ翻訳）**」という機能が加わる。\nライブ翻訳機能の実装に当たっては「音声認識」「自然言語処理」「音声合成」という複数のAI技術を統合し、各アプリの機能として実装している。\n例えば「Message（メッセージ）アプリ」では、会話スレッド全体の履歴から文脈を考慮した上で適切な翻訳を提供する。「FaceTimeアプリ」のリアルタイム翻訳キャプションは、オンデバイスならではの低レイテンシーを維持しながら、高精度な翻訳を動画コミュニケーションの中で実現する。\nそして「電話アプリ」での音声読み上げは、自分が発話した言葉を相手の言語でリピート発話する機能で（逆方向も可）、相手の話し方のニュアンスを文脈で保持しながら逐次通訳してくれる。",
        "title": "WWDC 2025基調講演から見るAppleの“進む道” 「UIデザイン ...",
        "url": "https://www.itmedia.co.jp/pcuser/articles/2506/10/news090_2.html",
        "date": "2025-06-11",
        "last_updated": "2025-10-21"
      },
      {
        "snippet": "",
        "title": "オンデバイス基盤モデルのためのプロンプトの設計と安全性 ...",
        "url": "https://developer.apple.com/jp/videos/play/wwdc2025/248/",
        "date": "2025-06-09",
        "last_updated": "2026-05-05"
      },
      {
        "snippet": "**Apple Intelligence**（アップル インテリジェンス）は、Appleが独自開発している人工知能プラットフォームである。2024年6月10日にWWDC2024の基調講演で、オンデバイス（小規模言語モデル）をベースとして自社サーバでの処理（Private Cloud Compute、大規模言語モデル）を組み合わせたシステムとして発表された。\n2024年10月28日からアメリカ英語での一部機能のベータテストとして、iOS 18.1, iPadOS 18.1, macOS Sequoia 15.1以降に統合され、アメリカ英語では各OSのバージョン18.2で正式にリリースされた。\n...\nOpenAIとの提携により、iOS 18.2, iPadOS 18.2, macOS Sequoia 15.2からはApple IntelligenceベースのSiriから外部のChatGPTをユーザが任意で呼び出して利用できる機能が実装されている。\n...\n2024年6月11日（日本時間）、WWDC2024にて、プライバシー保護に配慮し、パーソナルコンテキストを理解する、独自開発した生成モデルを据えるパーソナルインテリジェンスシステム（人工知能プラットフォーム）として、iOS 18、iPadOS 18、macOS Sequoiaでの全面採用と応用した多数の機能が発表された。\n...\n|18.1|15.1|2024年10月28日|- 作文ツール（校正、要約、書き換えのみ） - Siri (新しい外観、Siriに入力、文脈の改善) - スマートな返信 - 通知の概要 - 写真のクリーンアップとメモリメーカー - 割り込みを減らすフォーカスモード|\n|18.2|15.2|2024年12月11日|- さらに作文ツール強化（ChatGPTで作成、説明変更） - Image Playground - Image Wand - Siri (ChatGPT統合) - メールの分類(iPhone) - Genmoji (iPhoneとiPadのみ) - Visual Intelligence (iPhone 16/16 Pro/16 Pro Maxに対応)|\n|18.4|15.4|2025年3月31日|- 言語サポート追加（中国語、英語（インド）、英語（シンガポール）、フランス語、ドイツ語、イタリア語、日本語、韓国語、ポルトガル語、スペイン語、ベトナム語） - 優先通知 - メールの分類 (iPadとMac) - Image Playgroundスケッチ - Visual Intelligence (iPhone 15 Pro/Pro MaxとiPhone 16eに対応)|\n|26.1|26.1|2025年11月3日|ライブ翻訳- メッセージː 日本語、中国語（簡体字）、英語（英国、米国）、フランス語（フランス）、ドイツ語、イタリア語、韓国語、ポルトガル語（ブラジル）、スペイン語（スペイン） - 電話とFaceTimeː 英語（英国、米国）、フランス語（フランス）、ドイツ語、ポルトガル語（ブラジル）、スペイン語（スペイン）|\n...\n- これまでの会話内容を理解していることで、代名詞などでも文を理解する事が可能になる。また、画面上の物事についても理解する事が可能となる。個人の機密情報を検索する際であっても、オンデバイス（デバイス内での）処理となるため、機密情報が外に漏れることはなく、外部と共有する際には事前にユーザの同意が必要となる仕組みである。\n...\nApple Intelligenceを活用し、自動でアルバムを生成したり、音楽と共にスライドショーを作成する機能の機能向上とより一層複雑な検索キーワードに対応した検索機能や、意図しない写り込みを除去してくれる機能などが搭載される。\n...\nApple Intelligenceは、ユーザのプライバシーを保護するため基本的にオンデバイスで実行され、個人情報を収集することなく、情報を認識するよう設計されている。\nしかし、オンデバイスでの処理に適さない場合には、Private Cloud Computeと呼ばれるAppleシリコンによるサーバベースのデータセンターを利用し、必要最小限の情報のみを利用し、匿名化と暗号化でプライバシーを保護しながら、ユーザの提供したデータは一時利用のみで保管せず、より複雑なリクエストを処理する。",
        "title": "Apple Intelligence - Wikipedia",
        "url": "https://ja.wikipedia.org/wiki/Apple_Intelligence",
        "date": "2024-06-11",
        "last_updated": "2026-05-22"
      },
      {
        "snippet": "",
        "title": "Platforms State of the Union - WWDC24 - ビデオ - Apple Developer",
        "url": "https://developer.apple.com/jp/videos/play/wwdc2024/102/?time=2408",
        "date": null,
        "last_updated": "2026-04-07"
      },
      {
        "snippet": "# アップルの「Apple Intelligence」で新機能、あらゆるアプリがオンデバイスAIモデルへアクセスできるように\n...\n今回、新機能として、新しいFoundation Modeles frameworkにより、あらゆるアプリが、オンデバイスの大規模言語モデルにアクセスできるようになる。\nこれにより、Apple Intellgenceが利用できるアプリがサードパーティ製アプリにまで、セキュリティを担保した形で大幅に拡充される見込みだ。",
        "title": "あらゆるアプリがオンデバイスAIモデルへアクセスできるように",
        "url": "https://k-tai.watch.impress.co.jp/docs/news/2021215.html",
        "date": "2025-06-10",
        "last_updated": "2026-03-21"
      },
      {
        "snippet": "今回、新機能として、新しいFoundation Modeles frameworkにより、あらゆるアプリが、オンデバイスの大規模言語モデルにアクセスできるようになる。\nこれにより、Apple Intellgenceが利用できるアプリがサードパーティ製アプリにまで、セキュリティを担保した形で大幅に拡充される見込みだ。",
        "title": "アップルの「Apple Intelligence」で新機能、あらゆるアプリがオンデバイスAIモデルへアクセスできるように - ライブドアニュース",
        "url": "https://news.livedoor.com/article/detail/28928262/",
        "date": "2025-06-10",
        "last_updated": "2025-08-16"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

### Strategic Language Selection

* **Be Specific**: Choose languages that are most relevant to your research or application needs.
* **Consider Your Audience**: Select languages that match your target audience's preferences.
* **Regional Relevance**: Combine language filters with geographic filters (`country` parameter) for better regional targeting.
* **Content Availability**: Some topics may have limited content in certain languages. Start broad and narrow down as needed.

### Performance Considerations

* **Filter Size**: While you can specify up to 10 languages, using fewer languages may improve response times.
* **Result Quality**: More languages mean a broader search scope, which can dilute result relevance. Be strategic about which languages to include.
* **Combination Effects**: Language filters combined with other restrictive filters (domain, date) may significantly reduce the number of results.

## Advanced Usage Patterns

### Multilingual Research

Conduct comprehensive research by searching across multiple languages:

```python theme={null}
from perplexity import Perplexity

client = Perplexity()

# Research a global topic in multiple languages
languages = [
    ["en"],           # English-speaking countries
    ["zh", "ja"],     # East Asia
    ["es", "pt"],     # Latin America and Iberia
    ["fr", "de", "it"] # Western Europe
]

results_by_region = {}

for lang_group in languages:
    response = client.search.create(
        query="Avances de los Objetivos de Desarrollo Sostenible",
        max_results=10,
        search_language_filter=lang_group
    )
    results_by_region[", ".join(lang_group)] = response.results

# Analyze results by language/region
for region, results in results_by_region.items():
    print(f"Results in {region}: {len(results)} found")
```

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "3271f393-084f-4e71-80de-c6f919001e21",
    "results": [
      {
        "snippet": "Naciones Unidas Informe ODS 2024 Naciones Unidas (en inglés) Informe ODS 2023 Naciones Unidas Informe ODS 2022 Naciones Unidas Informe ODS 2021 Naciones Unidas Europa Informe ODS 2024 en Europa Informe ODS 2023 en Europa Resumen Ejecutivo ODS 2023\nEuropa Informe ODS 2022 Europa Resumen Ejecutivo ODS 2022 Europa Informe ODS 2021 Europa Resumen Ejecutivo ODS 2021 Europa SDS & Me España Examen Nacional Voluntario 2024 Informe de Progreso 2023 España Informe de Progreso 2022 España Informe de Progreso 2021 España",
        "title": "Avance de los ODS en el mundo - Agenda 2030 Castilla-La Mancha",
        "url": "https://agenda2030.castillalamancha.es/avance-de-los-ods-en-el-mundo",
        "date": "2025-01-01",
        "last_updated": "2025-10-19"
      },
      {
        "snippet": "",
        "title": "Agenda 2030 y ODS - ODS UAM - Universidad Autónoma de Madrid",
        "url": "https://ods.uam.es/agenda-2030-y-ods/",
        "date": "2026-04-29",
        "last_updated": "2026-05-25"
      },
      {
        "snippet": "**A falta de seis años para cumplir con la** ** Agenda 2030** **, sólo el 17% de las 169 metas que contienen los ** **17 Objetivos de Desarrollo Sostenible (ODS)** ** de la Agenda 2030 están en camino de conseguirse, ** advierte el Informe sobre ODS 2024 de las Naciones Unidas.\n...\nDesde su lanzamiento, los Objetivos de Desarrollo Sostenible han sido la guía hacia un futuro sostenible y equitativo y un marco de acción prioritario para las empresas y estados.\nSin embargo, **el progreso de estos Objetivos está siendo desigual y enfrenta obstáculos**.\n**El informe de la ONU revela que sólo el 17% de las metas de los ODS están avanzando, la mitad muestra un progreso mínimo o moderado y más de un tercio está estancado o retrocediendo.\n** El aún vigente impacto de la COVID-19, los conflictos y tensiones geopolíticas y el caos climático son algunas de las causas que frenan este progreso.\n...\n- **Aumenta la brecha de financiación de los ODS (** **ODS 17** **): ** la deuda externa de países en desarrollo continúa increíblemente alta y los países desarrollados encaran una brecha de 4 trillones de dólares de inversión para alcanzar los ODS.\n### ODS para mantener la esperanza\nA pesar de los datos abrumadores a nivel global, el informe muestra algunos progresos registrados en ciertos ámbitos de los ODS.\nEn concreto:\n- **Reducción de la pobreza (** **ODS 1** ** y ** **ODS 10** **)**: Asia central y meridional redujeron la pobreza laboral en un 6,9% y la pobreza continua disminuyendo en los países de medianos y altos ingresos.\n- **Mejora de la nutrición (** **ODS 2** **): ** se ha reducido el porcentaje de niños menores de 5 años afectados por el retraso del crecimiento 22,3% y ha aumentado el gasto gubernamental en agricultura.\n- **Avances en salud (** **ODS 3** **): ** se ha reducido a más de la mitad las nuevas infecciones de VIH y ha aumentado al 86% la asistencia de calidad al parto.\n- **Desarrollo en educación (** **ODS 4** **): ** en muchas regiones, las niñas han alcanzado o superado la paridad en la finalización de la escuela y se ha incrementado la tasa de finalización de la educación superior.\n- **Progresos en igualdad de género (** **ODS 5** **): ** desciende a un 20% el porcentaje de niñas que contraen matrimonio en comparación con el 25% de hace 25 años.\n- **Aumenta la producción de energía sostenible (** **ODS 7** **):** la generación de energía renovables ha incrementado un 8,1% anualmente en los pasados cinco años.\n- **Aceleración del empleo (** **ODS 8** **):** el desempleo ha caído a un histórico 5% en 2023.\n- **Aumento de la financiación climática (** **ODS 13** **):** la financiación climática aumentó un 30% desde 2021 desde 2021 alcanzando el objetivo y el 60% se asignó a la mitigación.\n- **Más protección para el océano (** **ODS 14** **):** la cobertura de áreas marinas protegidas se ha multiplicado por diez y la proporción de peces dentro de niveles biológicamente sostenibles aumentó más de una cuarta parte en las principales zonas de pesca.\n- **Progresos en tecnología y datos (** **ODS 17** **):** el acceso a internet ha aumentado un 70% en sólo ocho años y, frente a 2019, 29 nuevos países informaron tener legislación estadística que cumple con los principios.",
        "title": "¿En qué situación se encuentran los ODS de la Agenda 2030?",
        "url": "https://www.pactomundial.org/noticia/en-que-situacion-se-encuentran-los-ods-de-la-agenda-2030/",
        "date": "2025-04-15",
        "last_updated": "2026-05-25"
      },
      {
        "snippet": "> “Como Estados miembros reconocidos en la Cumbre de los ODS celebrada el pasado septiembre, los esfuerzos mundiales llevados a cabo hasta la fecha han sido insuficientes para lograr el cambio que necesitamos, lo que pone en riesgo el compromiso de la Agenda con las generaciones actuales y futuras.\n...\nEn el **Informe de los Objetivos de Desarrollo Sostenible (ODS)**, de periodicidad anual, se proporciona un panorama general de los esfuerzos realizados hasta la fecha para su aplicación en todo el mundo, subrayando las esferas de progreso y las esferas en las que se deben tomar más medidas para garantizar que nadie se quede atrás.\nCuando se cumplen cinco años de la adopción de los Objetivos de Desarrollo Sostenible, el **Informe sobre los Objetivos de Desarrollo Sostenible de 2020** (disponible en inlglés) destaca los progresos que se han logrado en el mundo en algunos ámbitos como la mejora de la salud maternoinfantil, la ampliación del acceso a la electricidad y el aumento de la representación de las mujeres en el Gobierno.\nAun así, estos avances se han visto contrarrestados en todo el mundo por la creciente inseguridad alimentaria, el deterioro del entorno natural y las persistentes desigualdades dominantes.\nAhora, en muy poco tiempo, la pandemia de COVID-19 ha desatado una crisis sin precedentes que obstaculiza aún más el progreso de los ODS, lo que afecta en mayor medida a las personas más pobres y vulnerables del mundo.\nCon base en los datos y las estimaciones más recientes, este informe anual de situación sobre el progreso en los 17 Objetivos revela que las personas más vulnerables (incluidos los niños, ancianos, discapacitados, migrantes y refugiados) son las más gravemente afectadas por la pandemia de COVID-19.\nLas mujeres también están sufriendo las peores consecuencias de la pandemia.\n...\n- Se estima que aproximadamente 71 millones de personas volverán a caer en la extrema pobreza en 2020, lo que supondría el primer aumento de la pobreza mundial desde 1998.\n...\n- Los cierres de las escuelas han afectado al 90 % de los estudiantes de todo el mundo (1.570 millones) y han provocado que más de 370 millones de niños se salten comidas escolares de las que dependen.\n...\n- A medida que más familias caen en la extrema pobreza, los niños de las comunidades pobres y desfavorecidas corren un riesgo mucho mayor de verse involucrados en el trabajo infantil, el matrimonio infantil y el tráfico infantil.\nDe hecho, es probable que los progresos logrados a nivel mundial en la reducción del trabajo infantil se vean invertidos por primera vez en 20 años.\n...\nLos informes anuales ofrecen una descripción general de los esfuerzos mundiales de implementación hasta la fecha, haciendo hincapié en los ámbitos de progreso y aquellos en los que es necesario tomar más medidas.",
        "title": "Informe sobre los progresos en el cumplimiento de los ODS",
        "url": "https://www.un.org/sustainabledevelopment/es/progress-report/",
        "date": "2020-07-15",
        "last_updated": "2026-03-22"
      },
      {
        "snippet": "",
        "title": "Objetivos de Desarrollo Sostenible | Naciones Unidas",
        "url": "https://www.un.org/es/impacto-acad%C3%A9mico/page/objetivos-de-desarrollo-sostenible",
        "date": null,
        "last_updated": "2026-03-26"
      },
      {
        "snippet": "",
        "title": "¿Qué son los Objetivos de Desarrollo Sostenible?",
        "url": "https://www.undp.org/es/sustainable-development-goals",
        "date": null,
        "last_updated": "2026-05-26"
      },
      {
        "snippet": "La **Agenda 2030 para el Desarrollo Sostenible** se compone de 17 objetivos y 169 metas.\nPara su seguimiento, se diseñaron 234 indicadores que pueden medirse a través de los datos estadísticos que aquí se recogen.\nLa actualización de estos indicadores, que constituyen una operación estadística recogida en el Programa anual vigente, es continua e incluye información tanto del INE como de otras fuentes oficiales que se irán incorporando de forma progresiva.",
        "title": "Indicadores de la Agenda 2030 para el Desarrollo Sostenible - INE",
        "url": "https://www.ine.es/dyngs/ODS/es/index.htm",
        "date": null,
        "last_updated": "2026-05-18"
      },
      {
        "snippet": "",
        "title": "Edición especial",
        "url": "https://unstats.un.org/sdgs/report/2023/The-Sustainable-Development-Goals-Report-2023_Spanish.pdf",
        "date": null,
        "last_updated": "2024-07-14"
      },
      {
        "snippet": "",
        "title": "La Agenda para el Desarrollo Sostenible",
        "url": "https://www.un.org/sustainabledevelopment/es/development-agenda/",
        "date": "2023-09-13",
        "last_updated": "2026-03-17"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

### Content Localization Research

Find examples and references in target languages for localization projects:

```python theme={null}
# Find product reviews in target markets
target_languages = ["ja", "ko", "zh"]  # Asian markets

response = client.search.create(
    query="iPhone 17 Pro Testbericht Fazit",
    max_results=15,
    search_language_filter=target_languages,
    search_recency_filter="month"
)
```

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "75adaf83-38af-4111-b4f7-d6462cdf80f9",
    "results": [
      {
        "snippet": "Bei der Ausstattung muss sich das iPhone 17 Pro keinesfalls hinter den Top-Modellen der Android-Sparte verstecken.\nHier bieten sich ein flottes USB-C-3 zur Datenübertragung sowie ein moderner Funkverkehr über Wi-Fi 7, 5G, Bluetooth 6.0 sowie NFC zum kontaktlosen Bezahlen etwa via Apple Pay an.\nMit dem integrierten Ultrabreitband-Chip lassen sich AirTags oder AirPods wie über ein Radar in der Nähe aufspüren.\nFür Sicherheit sorgt wie gewohnt die Gesichtserkennung mittels Face ID.\nAuf einen Fingerabdrucksensor verzichtet Apple weiterhin.\nEbenfalls gerne gesehen sind die Unfallerkennung sowie der Notruf über Satellit, sollte mal kein Handynetz gegeben sein.\nUm dieses zu erreichen, lässt sich anders als beim iPhone Air auch eine physische Nano-SIM im Gehäuse unterbringen.\nEinzeln oder im Dual-SIM-Betrieb können wir aber auch bis zu zwei eSIM-Verträge registrieren.\nObgleich das rund 204 Gramm schwere Aluminiumgehäuse nicht gerade ein Federgewicht ist, liegt das iPhone 17 Pro sehr gut in der Hand.\nDas ist einerseits seinem vergleichsweise handlichen Format, andererseits aber auch den hochwertig verarbeiteten Materialien zu verdanken.\nDie Kamerainsel mag nun deutlich breiter sein, stört uns im Test aber auch nicht mehr als in den Vorjahren oder bei den Modellen anderer Hersteller.\nDas iPhone 17 Pro ist mit den KI-Funktionen der ' Apple Intelligence ' kompatibel.\nDiese berechnet zwar mehr Aufgaben lokal oder auf privaten Servern als die Konkurrenz um Samsung oder Google, doch die Ergebnisse fallen auch meist ernüchternder aus als im Android-Lager.\nDas gilt speziell für den miserablen Objektradierer bei der Fotobearbeitung.\nWer bislang ohnehin nur iPhones kannte, wird die KI aber auch nicht vermissen.\nImmerhin ist Siri dank der Integration von ChatGPT inzwischen deutlich smarter.",
        "title": "Das beste Pro-Smartphone seit Jahren: Apple iPhone 17 Pro im Test",
        "url": "https://www.chip.de/test/Apple-iPhone-17-Pro-im-Test_186266683.html",
        "date": "2025-09-23",
        "last_updated": "2025-09-23"
      },
      {
        "snippet": "",
        "title": "Das habe ich nicht erwartet: Apple iPhone 17 Pro & Pro Max Review (Deutsch) | SwagTab",
        "url": "https://www.youtube.com/watch?v=XJYJxL4zuiA",
        "date": "2025-09-28",
        "last_updated": "2026-05-06"
      },
      {
        "snippet": "## iPhone 17 Pro im Test: Kurzfazit und Wertung\n**hervorragend ausgestattetes Smartphone mit Top-Kamera und ohne größere Schwächen**.\nDieses Jahr gibt es obendrauf ein grundlegend neues iPhone-Design, das mir persönlich sehr gut gefällt, allerdings durchaus polarisiert.\nZwei der größten Verbesserungen fliegen etwas unter dem Radar: die beeindruckende Akkulaufzeit und das schnellere Aufladen.\nInsgesamt fallen die Neuerungen umfangreicher aus als in den meisten Jahren – ein guter Zeitpunkt für ein Upgrade.\n...\nAuch ohne Test war eigentlich klar: Das iPhone 17 Pro besitzt ein **fantastisches 6,3-Zoll-Display**.\n...\nDie **48-MP-Hauptkamera produziert bei unterschiedlichsten Lichtbedingungen tolle Bilder** mit schönen Farben und vielen Details.\n...\nVon 3582 mAh beim bereits wirklich ausdauernder Vorgänger ist die Akkukapazität auf 3988 mAh gestiegen.\nUnd das macht sich bemerkbar: Im Alltagstest konnte ich für das iPhone 17 Pro eine **exzellente Akkulaufzeit von rund 26,5 Stunden** ermitteln.\n...\nFür eine komplette Aufladung benötigte das iPhone 17 Pro im Test knapp 1 Stunde und 20 Minuten.\n...\n### Preise für das iPhone 17 Pro (UVP)\n- **256 GB:** 1299 Euro\n- **512 GB:** 1549 Euro\n- **1 TB:** 1799 Euro\n...\nDas ab 949 Euro (UVP) erhältliche Standardmodell bietet ein deutlich besseres Preis-Leistungs-Verhältnis.\n...\n- Sehr schnell\n- Sehr gute Akkulaufzeit\n- Schnelleres Aufladen\n- Top-Kamera\n- Top-Display\n- Kratzeranfälig\n- Teuer",
        "title": "iPhone 17 Pro im Langzeit-Test: Drei Monate mit dem Apple ...",
        "url": "https://curved.de/reviews/iphone-17-pro-test-783263",
        "date": "2025-12-24",
        "last_updated": "2026-03-05"
      },
      {
        "snippet": "Das iPhone 17 Pro ist kein kleines Upgrade – Apple spricht vom leistungsstärksten iPhone, das sie je gebaut haben.\nMit größeren Kamerasensoren, mehr Zoom, längerer Akkulaufzeit und einem neuen Design will es im Premium-Segment ganz vorne mitspielen.\n...\nHier ist unser ehrliches Fazit nach einem ausgiebigen Test.\n...\n**Vorteile:**\n+ Kraftvoller A19 Pro Chip mit innovativer Dampfkammer\n+ Erstklassige Kamera mit herausragendem Zoom\n+ Center Stage Frontkamera bietet mehr Flexibilität\n+ Super helles Display\n+ Extrem ausdauernder Akku\n**Nachteile:**\n- Sperriges Kameradesign\n- Kleine Farbauswahl\n- Ladevorgang weiterhin nicht so schnell wie bei der Konkurrenz\n...\nApple verspricht beim iPhone 17 Pro eine **spürbar längere Akkulaufzeit**, was wir in unserem Test auch direkt festgestellt haben.\n...\nUnterm Strich liefert das iPhone 17 Pro in Sachen Akkulaufzeit ein zuverlässiges Gesamtpaket – kein Ausdauer-Wunder, aber deutlich alltagstauglicher als viele Vorgängermodelle.\n...\n## Unser Fazit: starkes Upgrade mit Zukunftssicherheit\nDas iPhone 17 Pro **zeigt in unserem Test viele Stärken**: Das neue Design ist erfrischend anders, der A19 Pro Chip sorgt für spürbar mehr Leistung und die Kamera überzeugt mit flexiblem Tele-Zoom sowie Profi-Videofunktionen.\nAuch die längere Akkulaufzeit und der faire Speicher-Einstieg ab 256 GB sind klare Pluspunkte.\n**Natürlich gibt es auch Kritik:** Das Display ist hell und farbstark, erreicht aber nicht ganz die Klasse mancher Android-Flaggschiffe.\nUnd beim Laden bleibt Apple konservativ – schnell, aber kein Spitzenwert.\nUnterm Strich ist das iPhone 17 Pro ein rundes High-End-Smartphone, das **vor allem für Nutzer mit älteren iPhones ein echtes Upgrade** darstellt.\nWer bereits ein 16 Pro besitzt, bekommt keine Revolution, aber ein spürbar besseres Gesamtpaket – und eines der zukunftssichersten Geräte auf dem Markt.",
        "title": "Das iPhone 17 Pro im Test - Apple - Sparhandy",
        "url": "https://www.sparhandy.de/info/test/iphone-17-pro",
        "date": "2025-06-04",
        "last_updated": "2026-05-23"
      },
      {
        "snippet": "",
        "title": "Lohnt sich das iPhone 17 Pro (Max) immer noch? - Langzeittest nach 4 Monaten Nutzung (Deutsch)",
        "url": "https://www.youtube.com/watch?v=HzEl5acsmoY",
        "date": "2026-01-11",
        "last_updated": "2026-05-02"
      },
      {
        "snippet": "Zunächst fallen die geänderte Bauform mit dem Kamerabuckel und die abgerundeten Kanten auf, die zu einer verbesserten Haptik führen.\nDie Handhabung hat sich im Vergleich zum direkten Vorgänger, dem iPhone 16 Pro, allerdings nicht geändert.\nSo lässt sich das iPhone weiterhin gut mit einer Hand bedienen und über den Kamerataster sind Einstellungen wie Blende, Stile und Belichtungskorrektur möglich.\n...\nDas neue Design schafft Platz für eine aktive Kühlung mit Dampfelement sowie für einen größeren Akku.\nDie Sensoren wurden überarbeitet: Alle drei rückseitigen Kameras verfügen jetzt über 48 Megapixel, einschließlich der Telekamera.\nZiel war eine verbesserte Low-Light-Performance.\nStandardmäßig werden die 48 Megapixel mithilfe von Pixel-Binning auf 12 Megapixel reduziert.\nUnterstützt werden die Kameras dabei von der Photonic Engine, die für die Bildverarbeitung verantwortlich ist.\n...\nDie drei sogenannten Fusion-Kameras bestehen aus einer Hauptkamera mit 1,78/24 mm, einem Ultraweitwinkel mit 2,2/13 mm sowie einem neuen Tele mit 2,8/100 mm.\nHaupt- und Telekamera sind zusätzlich mit einer optischen Bildstabilisierung per Sensorverschiebung ausgestattet.\nDank dieser Kombination decken die Kameras kleinbildäqivalente Brennweiten von 13 mm (0,5x), 24 mm (1x), 28 mm (1,2x), 35 mm (1,5x), 48 mm (2x), 100 mm (4x) und 200 mm (8x) sowie Makro-Aufnahmen ab.\n...\nIn den Einstellungen wird dies entsprechend angezeigt.\nApropos Einstellungen: Hier lässt sich das Dateiformat von HEIF auf JPEG umstellen und Raw aktivieren.\nDadurch kann man in der Kamera-App später direkt zwischen zwei Dateiformaten sowie zwischen 24 und 48 Megapixeln wechseln.\nAber auch die Frontkamera wurde überarbeitet: Sie bietet nun 18 Megapixel auf einem quadratischen Sensor und sorgt damit für gleichbleibende Qualität im Hoch- und Querformat.\n...\nDie Kameras des neuen iPhone 17 Pro liefern die erwartete Steigerung der Bildqualität.\nIn der Mehrzahl der Aufnahmen stimmt die Belichtung sehr gut, ebenso die lebhaften, aber nicht übersättigten Farben.\nAuch der Weißabgleich ist überzeugend.\nDas zeigt sich besonders bei Porträtaufnahmen: Hauttöne wirken natürlich, und die Hintergrundtrennung gelingt selbst bei feinen Haarstrukturen präzise.\nHaare und Fell werden detailreich wiedergegeben und wirken nur bei niedriger Auflösung leicht überschärft.\nEin zentrales Kriterium ist das Rauschverhalten, das deutlich verbessert wurde.\nIn den Schattenbereichen sind jetzt mehr Details sichtbar.\n...\nAuch das Ultraweitwinkel wurde verbessert: Es zeigt nun weniger Verzeichnungen und mehr Details bis zum Rand – besonders sichtbar bei Landschafts- und Gruppenaufnahmen.\n...\nDie Pro-iPhones gehören zu den beliebtesten Videokameras – auch, weil sie ProRes im Log-Format aufzeichnen können, auf Wunsch sogar direkt auf externe Laufwerke.\n...\n## Fazit: iPhone 17 Pro – Evolution statt Revolution\nEs sind nicht die großen Sprünge, die Apple Jahr für Jahr mit einer neuen iPhone-Generation vollzieht.\nAuch das iPhone 17 Pro ist ist „nur“ wieder ein Stück besser geworden.\nAm deutlichsten merkt man dies beim Teleobjektiv, das nun eine wesentlich höhere Auflösung liefert und damit nicht mehr gegenüber den beiden anderen Kameras abfällt.\nVerbesserungen zeigen sich auch bei Porträtaufnahmen und beim Einsatz der Blendensteuerung für kreative Fotos.\nDie Bokeh-Übergänge sind so harmonisch, dass sie Aufnahmen einer Kompaktkamera mit größerem Sensor sehr nahekommen.\nAuch das HDR wirkt jetzt deutlich natürlicher.\nSelbst die HEIF-Bilder sind schon sehr überzeugend, doch das Umschalten in den Pro-Modus mit Raw-Format holt das Maximum aus dem iPhone heraus.\nDamit verringert sich der Qualitätsabstand zu einer Kompaktkamera spürbar.\nDas iPhone 17 Pro schließt somit zu den starken Mitbewerbern aus dem Android-Lager auf und gehört erneut zu den Smartphones mit den besten Kamerasystemen.\nSeine großen Pluspunkte bleiben die enge Software-Integration und das professionelle Zubehör.",
        "title": "iPhone 17 Pro im Test – was Fotografen begeistert - fotoMAGAZIN",
        "url": "https://www.fotomagazin.de/smartphone/iphone-17-pro-im-test-gute-wahl-zum-fotografieren/",
        "date": "2025-12-02",
        "last_updated": "2026-05-19"
      },
      {
        "snippet": "",
        "title": "Apple iPhone 17 Pro im Test - Smartzone",
        "url": "https://www.smartzone.de/apple-iphone-17-pro-im-test/",
        "date": "2025-10-19",
        "last_updated": "2026-05-27"
      },
      {
        "snippet": "### Testfazit\nApples iPhone 17 hinterlässt im Test einen starken Eindruck.\nEs hat ein schönes 6,3 Zoll großes OLED-Display mit geschmeidiger Bildwiederholrate und Always-on-Funktion.\nInhalte machen nicht zuletzt dank satter Farben und hoher Schärfe eine gute Figur.\nAuch die Akkulaufzeit des iPhone 17 ist klasse: Mit eingeschaltetem Display hält es in unserem Akkutest über 19 Stunden durch.\nNach 30 Minuten am Stecker lässt es sich schon fast wieder für 13 Stunden verwenden.\nDer A19-Prozessor sorgt nicht nur für eine hohe Energieeffizienz, sondern auch für eine flotte Performance, selbst bei anspruchsvollen Apps.\nDie Dual-Kamera liefert sowohl bei Tageslicht als auch in schwach beleuchteten Umgebungen sehr schöne Fotos und Videos mit vielen Details und realitätsnahen Farben.\nEin Telezoom bleibt dem Standard-iPhone aber weiterhin verwehrt.\nWi-Fi 7, 5G-Mobilfunk, NFC und Dual-eSIM-Funktionalität sind mit dabei.\nDas iPhone 17 unterstützt die „Apple Intelligence“-KI, die zwar durch mehr Privatsphäre, jedoch nicht qualitativ gegenüber Google und Co. punkten kann.\nFace ID, der frei belegbare Actionbutton, die Kamerasteuerung und die Dynamic Island bleiben Teil der iPhone-DNA.\nEbenso wie ein recht hoher Preis.\n...\n### Testfazit\nMit dem iPhone 17 Pro liefert Apple ein fast kompromisslos starkes High-End-Smartphone, das vor allem durch seine enorme Ausdauer überzeugt.\nIn unserem Test erreichte es eine beeindruckende Dauerlaufzeit von über 21 Stunden – so kommen wir problemlos durch einen ganzen Tag.\nBereits 30 Minuten am Kabel reichen für über 13 Stunden Nutzung.\nEiner der Hauptgründe dürfte Apples-Prozessor A19 Pro sein.\nEr arbeitet effizient und bietet jederzeit Leistung auf höchstem Niveau – ohne dabei das Gehäuse bedeutend zu erhitzen.\nDie Triple-Kamera mit drei 48-Megapixel-Sensoren liefert großartige Fotos.\nSie sind gestochen scharf, farbkräftig und kontrastreich.\nEin achtfacher optischer Zoom und 4K-Videos mit 120 Bildern pro Sekunde runden das System ab, während die neue Selfie-Kamera unter anderem mit flexibler Formatwahl und verbesserter Stabilisierung punktet.\nDas 6,3 Zoll große OLED-Display begeistert mit hoher Helligkeit, satten Farben und weicher Bildwiederholrate von 120 Hertz, könnte aber etwas stärker entspiegelt sein.\n...\nDie lokalen KI-Funktionen von Apple bieten mehr Datenschutz, hinken bei der Qualität und Kompetenz jedoch noch hinterher.",
        "title": "iPhone 17 oder iPhone 17 Pro? Für wen sich das Upgrade wirklich ...",
        "url": "https://www.chip.de/test-kaufberatung/iphone-vergleich/iphone-17-oder-iphone-17-pro-fuer-wen-sich-das-upgrade-wirklich-lohnt_fab1a16a-cf5d-4b1d-a167-90a31be5f7aa.html",
        "date": "2026-01-20",
        "last_updated": "2026-05-24"
      },
      {
        "snippet": "Das iPhone 17 Pro präsentiert sich, auch ohne echte Innovationssprünge, als konsequente Weiterentwicklung seines Vorgängers.\nApple hat viele Details verbessert: das neue OLED-Display ist heller und farbtreuer, der Akku größer und ausdauernder, und der A19-Pro-Chip sorgt zusammen mit 12 GB RAM für eine herausragende Systemleistung.\nAuch bei der Kamera gibt es Fortschritte, insbesondere beim Teleobjektiv und bei der Frontkamera, die nun vielseitiger und technisch ausgereifter ist.\nIn der Praxis überzeugt das Smartphone mit starker Performance und einer der besten Akkulaufzeiten seiner Klasse.\n...\nTrotzdem bleibt ein zwiespältiger Eindruck: Der Wechsel von Titan zu Aluminium wirkt wie ein Rückschritt, zumal die Oberfläche laut Nutzerberichten anfälliger für Kratzer ist.\nDie Fotoqualität liegt zwar auf Spitzenniveau, doch der Ultraweitwinkel bleibt schwach und bei schlechtem Licht stößt der Zoom-Sensor an seine Grenzen.\nAuch das Display, so brillant es ist, nutzt weiterhin PWM mit niedriger Frequenz, was empfindliche Nutzer stören kann.\nDazu kommen kleine, aber ärgerliche Einschränkungen: kein High-Res-Audio über Bluetooth, kein Auracast, und einige neue iOS-26-Funktionen sind in der EU noch immer gesperrt.\n### Pro\n+ hohe Performance\n+ gutes Kamera-Setup\n+ sehr gute Akkulaufzeiten\n+ USB 3.2, UWB und Wi-Fi 7\n…\nDas Design wurde beim iPhone 17 Pro sichtbar überarbeitet, der Akku wächst deutlich und es gibt ein neues Zoom-Objektiv sowie eine neue Frontkamera.\nAuch die Ladegeschwindigkeiten ziehen an, das Display leuchtet heller und selbstverständlich hat auch das SoC ein Upgrade erhalten.\n...\nWenn auch diese bei vollflächiger Weißdarstellung unverändert bleibt, klettert sie bei einer verkleinerten Weißfläche auf bis zu 3.044 cd/m² (APL18) und bei der HDR-Wiedergabe sind es 2.997 cd/m².",
        "title": "Test Apple iPhone 17 Pro – Schneller, länger, weiter. Reicht das?",
        "url": "https://www.notebookcheck.com/Test-Apple-iPhone-17-Pro-Schneller-laenger-weiter-Reicht-das.1139984.0.html",
        "date": "2025-10-17",
        "last_updated": "2026-05-23"
      },
      {
        "snippet": "Apple traut sich was.\nAusgerechnet für die umsatzstarken Modelle der Pro-Reihe bietet das Unternehmen die bisher beliebteste Farbe nicht mehr an: Schwarz.\nStattdessen gibt es die Topmodelle jetzt in einem knalligen Orange.\nDer Umstieg auf Aluminium macht es möglich, mit neuen Farben zu spielen.\n...\nEine Neuerung, die alle Modelle betrifft: Sie haben dieselbe 48-Megapixel-Weitwinkelkamera im Rücken.\nAllerdings ist sie beim iPhone Air die einzige Kamera, beim iPhone 17 wird sie von einer Ultraweitwinkelkamera mit ebenfalls 48 Megapixeln begleitet.\nDie beiden Pro-Modelle haben zusätzlich eine Telekamera, auch mit 48 Megapixeln.\n...\nDass die Telekamera beim iPhone 17 Pro und Pro Max dennoch spürbar bessere Aufnahmen macht als die der Vorgänger, liegt daran, dass ihr Fotosensor 56 Prozent größer ist.\nDas erhöht unter anderem die Lichtempfindlichkeit, sorgt vor allem aber für ein natürliches Bokeh, so nennt man den Effekt, wenn Vorder- oder Hintergrund des Motivs unscharf erscheinen.\n...\nEine weitere Neuerung, die alle Modelle betrifft und schon daher viel mehr Menschen berühren wird, ist die neue Selfiekamera.\nSie hat einen Fotosensor mit 24 Megapixeln, der insofern besonders ist, als er quadratisch statt rechteckig ist.\nApple nutzt das ungewohnte Format für eine Funktion, die bisher niemand vermisst hat, von der man sich nach ein paar Tagen aber fragt, warum es sie erst jetzt gibt: Center Stage.\n...\nNur wer solche Funktionen benötigt, hat einen Grund, die neue maximale Speicherausstattung von zwei Terabyte (TB) zu wählen.\n...\nDie für das iPhone 17 wichtigste Neuerung: Erstmals hat auch das Einstiegsmodell einen sogenannten ProMotion-Bildschirm, der seine Bildwiederholrate dynamisch zwischen 1 und 120 Bildern pro Sekunde variieren kann.\n...\n### Fazit\nSelten hat Apple seine iPhones derart stark überarbeitet wie in diesem Jahr.\nStatt einfach Pro- und Nicht-Pro-Modelle mit unterschiedlichen Chips und Bildschirmen anzubieten, hat der Konzern jetzt vier ausgesprochen unterschiedliche iPhone-Varianten im Angebot, die sehr unterschiedliche Stärken und Schwächen haben.\nMit dem iPhone 17 räumt das Unternehmen endlich die beiden großen Makel bisheriger Basismodelle aus dem Weg, bestückt es mit genug Speicher und einem schnellen Bildschirm.\nVollkommen irre: Verglichen mit einem gleich ausgestatteten Google Pixel 10 kostet es 150 Euro weniger.\nDie iPhones 17 Pro und Pro Max hingegen sind mit Preisen ab 1299 Euro alles andere als günstig.\nDafür bieten sie mehr als genug Leistung und sehr gute Kameras, bei denen insbesondere die neue Telekamera glänzt.\nDas neue Design, größere Batterien und die verbesserte Kühlung machen sie stressresistent und ermöglichen stattliche Laufzeiten.\nIm Test musste das Pro Max nur jeden zweiten Tag aufgeladen werden, aber verlässliche Aussagen dazu lassen sich erst nach längeren Tests als dieser knappen Woche machen.\n...\nDas iPhone Air wiederum ist der Anfang einer neuen Ära für Apple.\n...\nDank seines A19 Pro liefert es Leistung satt, aber nicht Ausdauer ohne Ende.\nWer den Look wichtiger findet als mehrere Kameras und lange Laufzeiten, kann sich damit einen Ausblick in die Zukunft sichern, zu Preisen ab 1199 Euro.",
        "title": "Apples Generation 17 im Test: Das können die neuen iPhones",
        "url": "https://www.spiegel.de/netzwelt/gadgets/iphone-air-iphone-17-iphone-17-pro-und-pro-max-im-test-das-koennen-die-neuen-geraete-a-25db6c44-7701-4567-af6a-61e24737e4fc",
        "date": "2025-09-17",
        "last_updated": "2026-05-26"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

### Academic Research Across Languages

Access scholarly content in different languages:

```python theme={null}
# Search for research papers in multiple languages
response = client.search.create(
    query="Algorithmes d'informatique quantique",
    max_results=20,
    search_language_filter=["en", "de", "fr", "ru"],
    search_domain_filter=["arxiv.org", "nature.com", "science.org"]
)
```

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "d98fe101-dee7-4aac-a502-c0b0d5c1b03b",
    "results": [
      {
        "snippet": "",
        "title": "Algorithme quantique — Wikipédia",
        "url": "https://fr.wikipedia.org/wiki/Algorithme_quantique",
        "date": "2025-10-25",
        "last_updated": "2026-04-27"
      },
      {
        "snippet": "La logique quantique permet en principe de réaliser certains calculs de façon plus rapide \nque ne le font les ordinateurs classiques.\nNous en donnons ici trois exemples, correspondant \nà la résolution de problèmes posés sous forme logique simple.\nDe façon générale, on classe les problèmes de calcul en distinguant ceux qui sont\n...\nLa logique quantique, exploitant les superpositions de qubits et leur intrication permet de \ntransformer certains problèmes classiquement difficiles en problèmes quantiquement\nfaciles.\nL’algorithme de Shor décrit par exemple un procédé de factorisation demandant \nun temps croissant de façon polynomiale avec le nombre de bits du nombre à factoriser.\nNous n’aborderons pas dans cette introduction la description de cet algorithme, mais nous \n...\nNous allons montrer que le passage du calcul classique au calcul quantique transforme \ncertains oracles classiques difficiles en oracles quantiques faciles.\nDans d’ autres cas, le \nproblème quantique reste  difficile, mais moins que le problème classique (croissance toujours\nexponentielle du nombre d ’opérations, mais avec un exposant plus petit que classiquement ).\n...\nL ’Algorithme quantique de Deutsch-Josza\nf(x) constante ou \nbalancée ?\nH1.H2….Hn\n| {0} >A\n| 0>B\nN\nH\nLe registre d’entrée A (n qubits) est préparé (par application de la transformation de\nHadamard H sur chaque qubit) dans la superposition symétrique des 2 n états | x > possibles.\nLe registre de sortie B (1 qubit) est inversé par N, puis préparé par H dans (1/21/2) [| 0 > −| 1 >]\n>]\n>]\n>] .\n(1/2n/2) Σx |            x >\n(1/21/2) [| 0 > −| 1 >]\n>]\n...\n>]\n...\nOn applique à nouveau H à tous les qubits.\n...\nsi f(x ) est constante, un état orthogonal si f(x) est balancée →au moins un des qubits\ndoit alors être 1.\nOn le vérifie en mesurant les qubits finals de A.\nLa réponse nécessite au plus 3n+2 opérations à un qubit (2n + 1 opérations H,  une \nopération de bascule (N) et au plus mesure de n qubits (on peut arrêter dès qu’on\n…\n...\nL’ avantage de l’ algorithme quantique n’existe que si on cherche une réponse \ncertaine.\nSi on s’ autorise une probabilité finie ε        d’ erreur, aussi petite soit-elle,\n...\nCeci diminue considérablement l ’intérêt de l ’algorithme \nquantique puisqu’ il faut être sûr de pouvoir l ’effectuer sans aucune décohérence\npour qu ’il soit avantageux par rapport à la version classique.\nAlgorithme de recherche quantique (Grover)\nf (x) = δ (x-x0)\nx0?\n...\nx0?\n...\ndans [ 0, 1] est réalisée par un oracle agissant sur la superposition symétrique des N = 2 n\nqubits de A et sur le qubit B préparé par les opérations N et H dans l ’état (1/21/2) [| 0 > −| 1 >]\n...\nFinalement, l ’algorithme de recherche de Grover \ndemande donc un nombre d ’opérations en √N log2 N , \ninférieur à celui exigé classiquement (en N).\n...\nLes algorithmes de Deutsch et de Grover peuvent se décrire comme des processus\nd’ interférence quantique à 2 n chemins : Les H1.H2….Hn jouent le rôle de « lames \nséparatrices » qui décomposent et recombinent les états du registre  A.\nL ’oracle O est \nl ’analogue d ’une lame déphasante qui modifie les phases relatives des états.\nDans Grover,\nchaque symétrie Us combine «en sandwich» deux lames séparatrices avec une lame \ndéphasante.\nDans les deux «interféromètres», l’effet recherché est de favoriser dans l’état final \nun état ( analogue d’ une «frange brillante» ) dont la mesure finale fournit la réponse voulue.\n...\nUne mesure répétée ~ n fois de A va alors nous permettre de déterminer s\n…\n...\nUne mesure des qubits individuels donne une suite  y1a , y2a , y3a ,…..yna de valeurs 0 et 1\nqui satisfait la condition: \nΣ i si yia = 0 (modulo 2).\nOn recommence n fois l ’opération et on obtient ainsi, en général, n relations \nindépendantes  (si par hasard deux mesures donnent le même vecteur, on recommence \nune fois de plus):\nΣ i si yia = 0\nΣ i si yib = 0\n. . . . . . . . \nΣ i si yin = 0\nLa résolution de ce système d ’équations donne s.\nLe processus requiert  ≅4n2 opérations.\nLe problème est donc quantiquement facile.\nDe plus, il tolère des erreurs puisqu ’on peut \ntoujours vérifier le résultat en comparant f ( x ) et f (x ⊕s) une fois s obtenu.",
        "title": "Les algorithmes quantiques",
        "url": "https://www.college-de-france.fr/media/serge-haroche/UPL55031_SHaroche_260202.pdf",
        "date": null,
        "last_updated": "2025-12-13"
      },
      {
        "snippet": "",
        "title": "Comprendre l'informatique quantique – algorithmes et ...",
        "url": "https://www.oezratty.net/wordpress/2018/comprendre-informatique-quantique-algorithmes-et-applications/",
        "date": "2018-07-20",
        "last_updated": "2025-12-25"
      },
      {
        "snippet": "",
        "title": "Comprendre l'informatique quantique – algorithmes et ...",
        "url": "https://www.frenchweb.fr/comprendre-linformatique-quantique-algorithmes-et-applications/332659",
        "date": "2019-07-05",
        "last_updated": "2025-09-07"
      },
      {
        "snippet": "",
        "title": "Zoo des Algorithmes Quantiques",
        "url": "https://quantumalgorithmzoo.org/FrenchV1_8.html",
        "date": "2024-01-13",
        "last_updated": "2025-08-29"
      },
      {
        "snippet": "Essentiels en informatique, on les retrouve notamment en Data Science et dans le Machine Learning.Un algorithme est en fait une procédure par étapes.\nC’est **un ensemble de règles** à suivre pour accomplir une tâche ou résoudre un problème.\n...\nDans le domaine de la programmation informatique, les algorithmes sont des ensembles de règles qui\n**indiquent à l’ordinateur comment effectuer une tâche**.\nEn réalité, un programme informatique est un algorithme indiquant à l’ordinateur quelles étapes exécuter et dans quel ordre pour accomplir une tâche spécifique.\nIls sont **écrits à l’aide d’un langage de programmation**.\n...\nEn mécanique quantique, la manière de faire change profondément.\nTrois aspects de la mécanique quantique offrent la possibilité de faire de l’informatique quantique :\n**la dualité onde-corpuscule**, ** la superposition d’états **et ** l’intrication**.\nDe par leur nature onde-corpuscule, les particules quantiques sont décrites par des probabilités qui évoluent dans le temps et dans l’espace.\nElles ont aussi la capacité de se trouver dans un état qu’on appelle\n**« superposé » : un peu 0 et un peu 1**.\nAinsi, un qubit, la version quantique du bit traditionnel, possède deux états « d’existence », nommés **|0>** et **|1>**, prononcés : **ket 0** et **ket 1**.\nAlors qu’un bit classique est numérique et a toujours pour valeur soit 0 soit 1, l’état d’un qubit est une superposition quantique linéaire de ses deux états de base, il vaut en même temps |0> et |1>.\nNéanmoins, si on cherche à l’observer, on va alors trouver soit un 0 ou un 1 : **l’observation aura changé l’état de la particule** en choisissant entre les deux.\n...\nAvec un registre de n qubits, on a donc en même temps 2n valeurs, qui peuvent toutes être stockées simultanément (là où l’informatique classique ne peut stocker qu’une valeur à la fois).\nSi on arrive à faire des calculs avec de tels supports, on arrive en quelque sorte à\n**faire tous les calculs en même temps**, comme si on réalisait 2n calculs « en parallèle ».\nPar exemple, si n=3, un ordinateur quantique aura la possibilité de traiter 8 états quantiques différents, et donc 8 calculs en même temps.\nSi chaque calcul durait une seconde, un ordinateur quantique n’aurait donc besoin que de **1 seconde pour les réaliser**, là où un ordinateur classique aurait eu besoin de 8 secondes, puisqu’il aurait dû traiter chaque calcul l’un après l’autre.\nÀ la fin, il se peut qu’il n’y ait qu’un seul de ces calculs qui ait réussi, et c’est son résultat qui nous intéresse.\n**La difficulté, c’est de l’isoler**.\nC’est précisément le rôle des algorithmes quantiques : effacer de façon judicieuse tous les calculs qui n’ont pas abouti.\n...\nComme nous l’avons vu en informatique classique, un algorithme est un programme qui suit une suite logique d’instructions.\nEn informatique quantique,\n**la nature du traitement des instructions est changée**, elle devient aussi quantique.\nComme la lecture du registre ne fournit qu’une valeur 0 ou 1 pour chaque bit (pour rappel, un qubit observé se fige dans un état donné et se comporte comme un bit classique), soit un des états de base du registre, tout l’art de l’algorithmique quantique consiste à concentrer\n**l’évolution vers les états qui donnent la solution au problème étudié**.\nUn ordinateur quantique n’est donc pas une machine qui résoudrait tous les problèmes plus rapidement qu’un ordinateur conventionnel.\nIl s’agit plutôt d’une machine capable de résoudre efficacement certains problèmes hors de portée des machines conventionnelles.\nL’exercice consiste donc à comparer la complexité d’un problème d’un point de vue classique et d’un point de vue quantique.\nSi un algorithme peut être résolu de manière classique avec une complexité bien définie, il peut aussi l’être dans le modèle quantique avec\n**une complexité équivalente ou moindre**.\nLes capacités de l’algorithmique quantique sont reliées au nombre de qubits, mais augmenter leur nombre ne sert que si « l’environnement » quantique est maintenu malgré les inévitables processus de décohérence.\nUne autre particularité du qubit par rapport à un bit classique est qu’\n**il ne peut pas être dupliqué** en raison des lois de la physique quantique.\n...\nLes algorithmes quantiques ont le potentiel de\n**révolutionner de nombreux domaines**, dont la cryptographie, la chimie computationnelle, la recherche opérationnelle et même l’intelligence artificielle.\nL’un des exemples les plus marquants est **l’algorithme de factorisation de Shor**, qui menace les systèmes de cryptographie à base de factorisation et met en lumière la nécessité de développer des méthodes de chiffrement quantique plus robustes.\nEn ce qui concerne la Data Science, les algorithmes quantiques représentent\n**un grand potentiel **dans ce domaine.\nIls pourraient accélérer des tâches complexes telles que l’optimisation, l’apprentissage automatique et la simulation moléculaire.\nDe plus, ils pourraient améliorer la sécurité des données grâce à la cryptographie quantique.\nCependant, leur utilisation en data science est encore en développement en raison des défis technologiques actuels.\nMalgré cela, leur capacité à résoudre des problèmes difficiles rapidement offre des opportunités prometteuses pour l’avenir de l’analyse de données.\n**l’intérêt d’un algorithme quantique**dans notre société et dans le domaine de la data science.\nLes algorithmes quantiques ouvrent la voie à une nouvelle ère de calcul puissant et d’applications révolutionnaires.",
        "title": "Algorithme quantique : qu'est-ce que c'est ? Comment s'en ...",
        "url": "https://datascientest.com/algorithme-quantique-tout-savoir",
        "date": "2023-11-09",
        "last_updated": "2025-10-09"
      },
      {
        "snippet": "Algorithmes simples\n1\nCalcul de fonctions\n`A chaque fonction f : X →Y on peut associer une op´eration unitaire\nF |x⟩|y⟩:= |x⟩|y ⊕f(x)⟩\nclairement F = F †, FF = I et\nF |x⟩|0⟩:= |x⟩|f(x)⟩\nSi f est une fonction binaire, on peut aussi d´efinir\nF ′ |x⟩:= (−1)f(x) |x⟩\nencore une fois F ′ = F ′† et F ′F ′ = I.\n2\nCalcul de fonctions\n`A partir de F, on peut construire F ′ en utilisant un qubit\nsuppl´ementaire dans l’´etat\n1\n√\n2(|0⟩−|1⟩)\nF |x⟩1\n√\n2(|0⟩−|1⟩)\n=\n|x⟩1\n√\n2(|f(x)⟩−\n���f(x)\n�\n)\n=\n|x⟩(−1)f(x) 1\n√\n2(|0⟩−|1⟩)\n=\n(−1)f(x) |x⟩1\n√\n2(|0⟩−|1⟩)\n=\nF ′ |x⟩1\n√\n2(|0⟩−|1⟩)\n3\nAlgorithme de Grover\nSoit f : {0, 1}2 →{0, 1} avec la promesse qu’il existe x0 tel que\nf(x0) = 1 et si x ̸= x0 alors f(x) = 0.\nSoit l’op´eration unitaire U d´efinie par:\nU |00⟩\n=\n1\n2(−|00⟩+ |01⟩+ |10⟩+ |11⟩)\nU |01⟩\n=\n1\n2(+ |00⟩−|01⟩+ |10⟩+ |11⟩)\nU |10⟩\n=\n1\n2(+ |00⟩+ |01⟩−|10⟩+ |11⟩)\nU |11⟩\n=\n1\n2(+ |00⟩+ |01⟩+ |10⟩−|11⟩)\n4\nAlgorithme de Grover\nAlgorithme de Grover(f)\n• |ψ⟩= U†F ′H⊗2 |00⟩\n• m = Mesure(|ψ⟩)\n• retourne m\nClassique: 3 requˆetes `a f.\nQuantique: 1 requˆete `a f.\n5\n...\nAlgorithme de Deutsch\nProbl`eme de Deutsch (version de R.\nCleve et A.\nTapp): ´Etant donn´e\nf : {0, 1} →{0, 1}, d´ecider si f(0) = f(1).\nAlgorithme Deutsch(f)\n• |ψ⟩= HF ′H |0⟩\n• m = Mesure(|ψ⟩)\n• si m = 0 r´epond CONSTANTE sinon ´EQUILIBR´EE\nClassique: deux requˆetes `a f.\nQuantique: une requˆete `a f.\n7\n...\nOn obtient donc f(0) ⊕f(1) avec certitude.\nSi f(0) ⊕f(1) = 0 alors la\nfonction est constante, (f(0) = f(1)) sinon la fonction est ´equilibr´ee\n(f(0) ̸= f(1)).\n...\nAlgorithme de Deutsch-Josza\nProbl`eme de Deutsch-Josza: ´Etant donn´e f : {0, 1}n →{0, 1} d´ecider si\nf est constante (∀x, y, f(x) = f(y)) ou ´equilibr´ee (|f−1(0)| = |f−1(1)|).\nAlgorithme Deutsch-Josza(f)\n• |ψ⟩= H⊗nF ′H⊗n |0⟩\n• m = Mesure(|ψ⟩)\n• si m = 0 r´epond CONSTANTE sinon ´EQUILIBR´EE\nClassique: 2n−1 + 1 requˆetes `a f.\nQuantique: une requˆete `a f.\n10\n...\nAlgorithme de Simon\n´Etant donn´e f : {0, 1}n →{0, 1}n−1 telle qu’il existe s non nul avec la\npropri´et´e que ∀x ̸= y : f(x) = f(y) ⇔x = y ⊕s, trouver s.\nAlgorithme Simon(f)\n• S = {}\n• tant que |S| < n −1\n•\n|ψ⟩= (H⊗n ⊗I2n−1)F(H⊗n ⊗I2n−1) |0⟩|0⟩\n•\n(m, y) = Mesure(|ψ⟩)\n•\nsi m est ind´ependant de S alors S ←S ∪{m}\n• fin du tant que\n• d´eduire s de S.\nClassique: Ω(2(1/2−ϵ)n) requˆetes `a f mˆeme avec probabilit´e de succ`es\nconstante.\nQuantique: Esp´erance de O(n) requˆetes `a f.\n14\n...\n`A chaque it´eration, la probabilit´e de succ`es est donc au moins 1/2, ce\nqui nous donne un nombre d’it´erations esp´er´e dans O(n).\n...\nPour tout ´etat |ψ⟩∈HABC on peut mesurer le sous-espace B.\nPour un sous-espace B de dimension d et un ´etat\n|ψ⟩= �d−1\ni=0 αi |ai⟩|i⟩|ci⟩on obtient le r´esultat classique i avec\nprobabilit´e |αi|2 et l’´etat devient |ai⟩|i⟩|ci⟩.",
        "title": "[PDF] Informatique quantique IFT6155 Algorithmes simples",
        "url": "https://www.iro.umontreal.ca/~tappa/pages/cours/IFT6155/algorithmes1.pdf",
        "date": null,
        "last_updated": "2025-11-28"
      },
      {
        "snippet": "",
        "title": "[PDF] À la découverte des algorithmes quantiques - Ion Nechita",
        "url": "https://ion.nechita.net/wp-content/uploads/2019/06/Projet-S2-Fresse-Colson-Da-Rocha-Balauze.pdf",
        "date": null,
        "last_updated": "2026-02-26"
      },
      {
        "snippet": "",
        "title": "Informatique quantique — Wikipédia",
        "url": "https://fr.wikipedia.org/wiki/Informatique_quantique",
        "date": "2005-09-30",
        "last_updated": "2026-05-22"
      },
      {
        "snippet": "",
        "title": "Informatique quantique : Algorithmes, modèles, défis et applications",
        "url": "https://geekflare.com/fr/ai/guide/quantum-computing/",
        "date": "2024-05-14",
        "last_updated": "2024-10-29"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

### News Monitoring by Language

Track news stories across different language regions:

```python theme={null}
# Monitor breaking news in different languages
news_queries = {
    "English": ["en"],
    "Chinese": ["zh"],
    "Spanish": ["es"],
    "Arabic": ["ar"]
}

for region, langs in news_queries.items():
    response = client.search.create(
        query="Misión y descubrimientos de la sonda Voyager 1",
        max_results=5,
        search_language_filter=langs,
        search_recency_filter="day"
    )
    print(f"{region} News: {len(response.results)} articles")
```

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "6ff356eb-a05a-4d1f-be99-f23b5951266f",
    "results": [
      {
        "snippet": "",
        "title": "Voyager 1 - Wikipedia, la enciclopedia libre",
        "url": "https://es.wikipedia.org/wiki/Voyager_1",
        "date": "2003-09-05",
        "last_updated": "2026-03-21"
      },
      {
        "snippet": "Lanzadas en 1977, las sondas gemelas Voyager son la misión de operación más larga de la NASA y las únicas naves espaciales que ha explorado el espacio interestelar.\n...\nSin embargo, las Voyagers se mantienen a la vanguardia de la exploración espacial.\nAdministradas y operadas por el Laboratorio de Propulsión a Chorro (JPL, por sus siglas en inglés) de la NASA, en el sur de California, son las únicas sondas que han explorado el espacio interestelar, el océano galáctico por el que viajan nuestro Sol y sus planetas.\nEl Sol y los planetas residen en la heliosfera, una burbuja protectora creada por el campo magnético del Sol y el flujo hacia afuera del viento solar (partículas cargadas del Sol).\nLos investigadores, algunos de ellos más jóvenes que las dos naves espaciales distantes, están combinando las observaciones de las Voyagers con datos de misiones más nuevas para obtener una imagen más completa de nuestro Sol y cómo la heliosfera interactúa con el espacio interestelar.\n...\n“Durante los últimos 45 años, las misiones Voyager han sido integrales para proporcionar este conocimiento y han ayudado a cambiar nuestra comprensión del Sol y su influencia de una manera que ninguna otra nave espacial puede”.\n...\nVoyager 2 se lanzó el 20 de agosto de 1977, seguida rápidamente por Voyager 1 el 5 de septiembre.\nAmbas sondas viajaron a Júpiter y Saturno, con Voyager 1 moviéndose más rápido y alcanzándolos primero.\nJuntas, las sondas revelaron mucho sobre los dos planetas más grandes del sistema solar y sus lunas.\nVoyager 2 también se convirtió en la primera y única nave espacial en volar cerca de Urano (en 1986) y Neptuno (en 1989), ofreciendo a la humanidad vistas extraordinarias e información sobre estos mundos distantes.\nMientras Voyager 2 realizaba estos sobrevuelos, Voyager 1 se dirigía hacia el límite de la heliosfera.\nAl salir de ella en 2012, Voyager 1 descubrió que la heliosfera bloquea el 70% de los rayos cósmicos o partículas energéticas creadas por estrellas en explosión.\nVoyager 2, después de completar sus exploraciones planetarias, continuó hasta el límite de la heliosfera y salió en 2018.\nLos datos combinados de las naves espaciales gemelas de esta región han desafiado las teorías anteriores sobre la forma exacta de la heliosfera.\n“Hoy, mientras ambas Voyager exploran el espacio interestelar, están brindando a la humanidad observaciones de un territorio desconocido”, dijo Linda Spilker, científica adjunta del proyecto Voyager en JPL.\n“Esta es la primera vez que hemos podido estudiar directamente cómo una estrella, nuestro Sol, interactúa con las partículas y los campos magnéticos fuera de nuestra heliosfera, ayudando a los científicos a comprender el vecindario local entre las estrellas, cambiando algunas de las teorías sobre esta región y proporcionando información clave para futuras misiones”.\n...\n“Las Voyagers han continuado haciendo descubrimientos sorprendentes, inspirando a una nueva generación de científicos e ingenieros”, dijo Suzanne Dodd, gerente de proyectos de Voyager en JPL.",
        "title": "Voyager, la misión más longeva de la NASA, cumple 45 años en el ...",
        "url": "https://ciencia.nasa.gov/sistema-solar/voyager-cumple-45-en-el-espacio/",
        "date": "2022-08-19",
        "last_updated": "2026-05-23"
      },
      {
        "snippet": "",
        "title": "Lo que descubrió la Voyager 1 en el borde del sistema solar",
        "url": "https://www.youtube.com/watch?v=LQ8SYzg1Rgc",
        "date": "2026-02-07",
        "last_updated": "2026-05-20"
      },
      {
        "snippet": "La **Voyager 1** ye una sonda espacial robótica de 722 kilogramos, llanzada'l 5 de setiembre de 1977, dende Cabu Cañaveral, Florida.\nSigue operativa na actualidá, prosiguiendo la so misión estendida que ye alcontrar y estudiar les llendes del sistema solar, incluyendo'l petrina de Kuiper y más allá, según esplorar l'espaciu interestelar inmediatu, hasta fin de misión.\nEl 25 d'agostu de 2012, a pocu más de 19 000 millones de quilómetros del Sol o 122 UA, la sonda dexó tras la heliopausa, siendo la primera n'algamar l'espaciu interestelar.\nLa so misión orixinal yera visitar Xúpiter y Saturnu.\nFoi la primer sonda n'apurrir imáxenes detallaes de los satélites d'esos planetes.\nA una distancia de 135 AU (2.02×10^10^ km) del Sol, en xunu de 2016, ye la nave espacial más alloñada de la Tierra y la única nel espaciu interestelar, pero entá ensin salir del sistema solar, quedándo-y unos 17 702 años aproximao pa salir a la nube d'Oort.\nVa Entrar nesta nunos 300 años aproximao.\nLa Voyager 1 ye anguaño l'oxetu fechu pol humanu más alloñáu de la Tierra, viaxando a una velocidá relativa de la Tierra y el Sol mayor que la de nenguna otra sonda espacial.\n...\nVoyager 1 tien una trayeutoria hiperbólica, y algamó velocidá d'escape, lo que significa que la so órbita nun va tornar al sistema solar interior.\nXunto cola Pioneer 10, Pioneer 11, Voyager 2 y la New Horizons, Voyager 1 ye una sonda interestelar.\n...\nA pesar de ser llanzada dempués de la so ximielga Voyager 2, la Voyager 1 algamó Jupiter dos meses primero que la so compañera, y, siguiendo una trayeutoria más rápida, llegó nueve meses antes a Saturno.\nVoyager 1 realizó les sos primeres fotografíes de Xúpiter en xineru de 1979 y algamó el so máximu acercamientu'l 5 de marzu de 1979 a una distancia de 278 000 km.\nNa so misión a Xúpiter realizó 19 000 fotografíes, nun periodu que duró hasta abril.\nPor cuenta de el máximu resolución dexáu por tal acercamientu, la mayor parte de les observaciones alrodiu de los satélites, aniellos, campu magnético y condiciones de radiación de Xúpiter fueron tomaes nun periodu de 48 hores alredor de dichu acercamientu.\n...\nAverar a 18 640 km del satélite Io de Xúpiter y pudo reparar per primer vegada actividá volcánica fuera de la Tierra, daqué que pasó inalvertíu pa les Pioneer 10 y 11.\nEl descubrimientu foi realizáu pola inxeniera de navegación Linda A. Morabito mientres un exame d'una fotografía delles hores dempués del sobrevuelu.\nAcelerada pel campu gravitatoriu de Xúpiter, algamó Saturnu el 12 de payares de 1980, averándose a una distancia de 124 200 km.\nNesta ocasión afayó estructures complexes nel sistema d'aniellos del planeta y consiguió datos de l'atmósfera de Saturnu y del so mayor satélite natural, Titán, del que pasó a menos de 6500 km.\nDebíu al descubrimientu d'atmósfera nesti satélite, el controladores de la misión decidieron que la Voyager 1 fixera un mayor aproximamientu a esta lluna, sacrificando asina les siguientes etapes del so viaxe, Uranu y Neptunu, que fueron visitaes pola so ximielga Voyager 2.\nEsti segundu acercamientu a Titan aumentó l'impulsu gravitatoriu de la sonda, alloñar del planu de la eclíptica y poniendo fin a la so misión planetaria.\n...\nD'esta manera, la Voyager 1 convertir nel primer oxetu creáu pol humanu en superar la heliopausa y enfusase nel espaciu interestelar.\n...\nEl 23 de febreru de 2017 a 20 916 millones de quilómetros (137,747 UA, esto ye, 38 h 14 min hores-lluz de la Tierra), la sonda dirixir al centru de la nuesa galaxa, la Vía Láctea, dexando l'espaciu apoderáu pola influencia del nuesu Sol dende'l 25 d'agostu de 2012 y entrando asina nel espaciu ente les estrelles, l'espaciu interestelar.",
        "title": "Voyager 1 - Wikipedia",
        "url": "https://ast.wikipedia.org/wiki/Voyager_1",
        "date": "2018-02-10",
        "last_updated": "2025-10-18"
      },
      {
        "snippet": "",
        "title": "Lo que encontró la Voyager 1 en el borde del sistema solar",
        "url": "https://www.youtube.com/watch?v=1QOXR4UV-_M",
        "date": "2026-01-28",
        "last_updated": "2026-04-20"
      },
      {
        "snippet": "",
        "title": "Voyager 1 - No Sólo Sputnik",
        "url": "https://nosolosputnik.com/el-planeta-jupiter/exploracion-de-jupiter/voyager-1/",
        "date": "2026-05-10",
        "last_updated": "2026-05-10"
      },
      {
        "snippet": "",
        "title": "Viajar 1",
        "url": "https://es.frwiki.wiki/wiki/Voyager_1",
        "date": null,
        "last_updated": "2024-05-04"
      },
      {
        "snippet": "# La Voyager 1, la primera nave en el espacio interestelar, puede haber perdido contacto para siempre con la humanidad\n## La sonda lanzada hace 46 años, que pasó cerca de Júpiter y Saturno em sus primeros años e inspiró a los terrícolas con imágenes del planeta como un “punto azul pálido”, no ha enviado datos en meses\n- 7 minutos de lectura'\nNUEVA YORK.-** Cuando la Voyager 1 se lanzó en 1977, los científicos esperaban que pudiera hacer aquello para lo que fue construida** y tomar imágenes de cerca de Júpiter y Saturno.\n**Hizo eso y mucho más.**\nLa Voyager 1 descubrió volcanes activos, lunas y anillos planetarios, demostrando en el camino que **la Tierra y toda la humanidad podían reducirse a un solo píxel en una fotografía, un “punto azul pálido”**, como lo llamó el astrónomo Carl Sagan.\nAlargó una misión de cuatro años hasta el día de hoy, embarcándose en **el viaje más profundo jamás realizado al espacio.**\n...\nLa Voyager 1, el objeto creado por humanos que llego más lejos en el espacio, **no ha enviado datos coherentes a la Tierra desde noviembre**.\n...\nLa nave espacial encontró una falla en una de sus computadoras que eliminó su capacidad de enviar datos de ingeniería y ciencia a la Tierra.\nLa pérdida de la Voyager 1 pondría** fin a décadas de avances científicos y señalaría el principio del fin de una misión que ha dado forma a la ambición más lejana de la humanidad e inspirado a generaciones a mirar al cielo.**\n...\nLa Voyager 1 es la mitad de la misión Voyager.\n...\nLanzados en 1977, **fueron construidos principalmente para un viaje de cuatro años a Júpiter y Saturno**, ampliando los sobrevuelos anteriores de las sondas Pioneer 10 y 11.\nLa misión Voyager aprovechó una rara alineación de los planetas exteriores (una vez cada 175 años), lo que permitió a las sondas visitar los cuatro.\nUtilizando la gravedad de cada planeta, la nave espacial Voyager podría pasar al siguiente, según la NASA.\n**La misión a Júpiter y Saturno fue un éxito.** Los sobrevuelos de la década de 1980 produjeron varios descubrimientos nuevos, incluidos nuevos conocimientos sobre la llamada gran mancha roja de Júpiter, los anillos alrededor de Saturno y las numerosas lunas de cada planeta.\nLa Voyager 2 también exploró Urano y Neptuno, convirtiéndose en 1989 en la única nave espacial en explorar los cuatro planetas exteriores.\nMientras tanto, **la Voyager 1 había fijado rumbo hacia el espacio profundo**, utilizando su cámara para fotografiar los planetas que iba dejando atrás en el camino.\nLa Voyager 2 comenzaría más tarde su propio viaje al espacio profundo.\n“Cualquiera que esté interesado en el espacio está interesado en las cosas que la Voyager descubrió sobre los planetas exteriores y sus lunas”, dijo Kate Howells, especialista en educación pública de la Planetary Society, una organización cofundada por Sagan para promover la exploración espacial.\n...\nEl día de San Valentín de 1990, la Voyager 1, que se alejaba 6000 millones de kilómetros del Sol hacia los confines exteriores del sistema solar,** se dio la vuelta y tomó una fotografía de la Tierra que Sagan y otros entendieron como un humilde autorretrato de la humanidad.**\n...\nIncluso cuando se lanzaron sondas más avanzadas desde la Tierra, la Voyager 1 continuó enriqueciendo de manera confiable nuestra comprensión del espacio.\nEn 2012, se convirtió en **el primer objeto creado por el hombre en salir de la heliosfera**, el espacio alrededor del sistema solar influenciado directamente por el sol.\nExiste un debate técnico entre los científicos sobre si la Voyager 1 realmente abandonó el sistema solar, pero, aun así, se volvió interestelar, atravesando el espacio entre las estrellas.\nEsto trazó un nuevo camino para la heliofísica, que analiza cómo el Sol influye en el espacio que lo rodea.\nEn 2018, la Voyager 2 siguió a su gemela entre las estrellas.\nAntes de la Voyager 1, los datos científicos sobre los gases y el material del Sol procedían únicamente de los confines de la heliosfera, según Jamie Rankin, científico adjunto del proyecto Voyager.\n...\n**Las Voyager 1 y 2 son las únicas naves espaciales de este tipo.** Antes de desconectarse, la Voyager 1 había estado estudiando una perturbación anómala en el campo magnético y las partículas de plasma en el espacio interestelar.\n...\nIncluso si la misión interestelar Voyager está cerca de su fin,** al viaje aún le queda mucho por recorrer.**\nPodría decirse que la Voyager 1 y su gemela, cada una a 40.000 años de distancia de la siguiente estrella más cercana, permanecerán en una misión indefinida.\n...\nCada nave espacial lleva un disco fonográfico bañado en oro cargado con una variedad de grabaciones de sonido e imágenes que representan la riqueza de la humanidad, sus diversas culturas y la vida en la Tierra.",
        "title": "La Voyager 1, la primera nave en el espacio interestelar ... - La Nación",
        "url": "https://www.lanacion.com.ar/el-mundo/la-voyager-1-la-primera-nave-en-el-espacio-interestelar-puede-haber-perdido-contacto-para-siempre-nid07032024/",
        "date": "2024-03-07",
        "last_updated": "2026-05-20"
      },
      {
        "snippet": "",
        "title": "Voyager 1 - Wikiwand",
        "url": "https://www.wikiwand.com/es/articles/Voyager_1",
        "date": "2023-11-14",
        "last_updated": "2025-08-06"
      },
      {
        "snippet": "",
        "title": "PDF Voyager 1 se acerca al espacio interestelar",
        "url": "https://ia800309.us.archive.org/25/items/Voyager1SeAcercaAlEspacioInterestelar/Voyager%201%20se%20acerca%20al%20espacio%20interestelar.pdf",
        "date": null,
        "last_updated": "2025-11-28"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

## Error Handling

When using language filters, implement proper error handling for validation issues:

<CodeGroup>
  ```python Python theme={null}
  from perplexity import Perplexity, BadRequestError

  client = Perplexity()

  def safe_language_search(query, languages):
      """
      Perform a language-filtered search with error handling.
      """
      try:
          # Validate language codes
          if not isinstance(languages, list):
              raise ValueError("Languages must be provided as a list")
          
          if len(languages) > 10:
              raise ValueError("Maximum 10 language codes allowed")
          
          # Validate each code format
          for lang in languages:
              if not isinstance(lang, str) or len(lang) != 2 or not lang.islower():
                  raise ValueError(f"Invalid language code format: {lang}")
          
          # Perform search
          response = client.search.create(
              query=query,
              search_language_filter=languages,
              max_results=10
          )
          
          return response
          
      except ValueError as e:
          print(f"Validation error: {e}")
          return None
      except BadRequestError as e:
          print(f"API error: {e.message}")
          return None
      except Exception as e:
          print(f"Unexpected error: {e}")
          return None

  # Usage
  results = safe_language_search(
      "artificial intelligence",
      ["en", "fr", "de"]
  )

  if results:
      print(f"Found {len(results.results)} results")
  ```

  ```typescript Typescript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  async function safeLanguageSearch(
    query: string,
    languages: string[]
  ): Promise<any | null> {
    try {
      // Validate language codes
      if (!Array.isArray(languages)) {
        throw new Error("Languages must be provided as an array");
      }
      
      if (languages.length > 10) {
        throw new Error("Maximum 10 language codes allowed");
      }
      
      // Validate each code format
      for (const lang of languages) {
        if (typeof lang !== 'string' || 
            lang.length !== 2 || 
            lang !== lang.toLowerCase()) {
          throw new Error(`Invalid language code format: ${lang}`);
        }
      }
      
      // Perform search
      const response = await client.search.create({
        query,
        search_language_filter: languages,
        max_results: 10
      });
      
      return response;
      
    } catch (error) {
      if (error instanceof Perplexity.BadRequestError) {
        console.error("API error:", error.message);
      } else if (error instanceof Error) {
        console.error("Error:", error.message);
      }
      return null;
    }
  }

  // Usage
  const results = await safeLanguageSearch(
    "artificial intelligence",
    ["en", "fr", "de"]
  );

  if (results) {
    console.log(`Found ${results.results.length} results`);
  }
  ```
</CodeGroup>

<Tip>
  For best results, combine language filtering with other filters like `search_domain_filter` or `search_recency_filter` to narrow down your search to highly relevant, timely content in your target languages.
</Tip>
