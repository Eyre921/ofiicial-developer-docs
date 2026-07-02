---
title: "Frameworks, guides and examples"
source: https://trigger.dev/docs/guides/introduction
path: docs/guides/introduction
---

A growing list of guides and examples to get the most out of Trigger.dev.

## Frameworks

<CardGroup>
  <Card title="Bun" href="/guides/frameworks/bun" />

  <Card title="Next.js" href="/guides/frameworks/nextjs" />

  <Card title="Node.js" href="/guides/frameworks/nodejs" />

  <Card title="Remix" href="/guides/frameworks/remix" />

  <Card title="SvelteKit" href="/guides/community/sveltekit" />
</CardGroup>

## Guides

Get set up fast using our detailed walk-through guides.

| Guide                                                                                      | Description                                                            |
| :----------------------------------------------------------------------------------------- | :--------------------------------------------------------------------- |
| [AI Agent: Content moderation](/docs/guides/ai-agents/respond-and-check-content)                | Parallel check content while responding to customers                   |
| [AI Agent: Generate and translate copy](/docs/guides/ai-agents/generate-translate-copy)         | Chain prompts to generate and translate content                        |
| [AI Agent: News verification](/docs/guides/ai-agents/verify-news-article)                       | Orchestrate fact checking of news articles                             |
| [AI Agent: Route questions](/docs/guides/ai-agents/route-question)                              | Route questions to different models based on complexity                |
| [AI Agent: Translation refinement](/docs/guides/ai-agents/translate-and-refine)                 | Evaluate and refine translations with feedback                         |
| [Claude Agent SDK](/docs/guides/ai-agents/claude-code-trigger)                                  | Build AI agents that read files, run commands, and edit code           |
| [Cursor rules](/docs/guides/cursor-rules)                                                       | Use Cursor rules to help write Trigger.dev tasks                       |
| [Prisma](/docs/guides/frameworks/prisma)                                                        | How to setup Prisma with Trigger.dev                                   |
| [Python image processing](/docs/guides/python/python-image-processing)                          | Use Python and Pillow to process images                                |
| [Python document to markdown](/docs/guides/python/python-doc-to-markdown)                       | Use Python and MarkItDown to convert documents to markdown             |
| [Python PDF form extractor](/docs/guides/python/python-pdf-form-extractor)                      | Use Python, PyMuPDF and Trigger.dev to extract data from a PDF form    |
| [Python web crawler](/docs/guides/python/python-crawl4ai)                                       | Use Python, Crawl4AI and Playwright to create a headless web crawler   |
| [Sequin database triggers](/docs/guides/frameworks/sequin)                                      | Trigger tasks from database changes using Sequin                       |
| [Stripe webhooks](/docs/guides/examples/stripe-webhook)                                         | Trigger tasks from incoming Stripe webhook events                      |
| [Hookdeck webhooks](/docs/guides/examples/hookdeck-webhook)                                     | Use Hookdeck to receive webhooks and forward them to Trigger.dev tasks |
| [Supabase database webhooks](/docs/guides/frameworks/supabase-edge-functions-database-webhooks) | Trigger tasks using Supabase database webhooks                         |
| [Supabase edge function hello world](/docs/guides/frameworks/supabase-edge-functions-basic)     | Trigger tasks from Supabase edge function                              |
| [Using webhooks in Next.js](/docs/guides/frameworks/nextjs-webhooks)                            | Trigger tasks from a webhook in Next.js                                |
| [Using webhooks in Remix](/docs/guides/frameworks/remix-webhooks)                               | Trigger tasks from a webhook in Remix                                  |

## Featured use cases

<CardGroup>
  <Card title="Data processing & ETL workflows" icon="database" href="/guides/use-cases/data-processing-etl">
    Build complex data pipelines that process large datasets without timeouts.
  </Card>

  <Card title="Media processing workflows" icon="film" href="/guides/use-cases/media-processing">
    Batch process videos, images, audio, and documents with no execution time limits.
  </Card>

  <Card title="AI media generation workflows" icon="wand-magic-sparkles" href="/guides/use-cases/media-generation">
    Generate images, videos, audio, documents and other media using AI models.
  </Card>

  <Card title="Marketing workflows" icon="bullhorn" href="/guides/use-cases/marketing">
    Build drip campaigns, create marketing content, and orchestrate multi-channel campaigns.
  </Card>
</CardGroup>

## Example projects

Example projects are full projects with example repos you can fork and use. These are a great way of learning how to use Trigger.dev in your projects.

| Example project                                                                                                 | Description                                                                                                                            | Framework | GitHub                                                                                                         |
| :-------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- | :-------- | :------------------------------------------------------------------------------------------------------------- |
| [Anchor Browser web scraper](/docs/guides/example-projects/anchor-browser-web-scraper)                               | Monitor a website and find the cheapest tickets for a show.                                                                            | —         | [View the repo](https://github.com/triggerdotdev/examples/tree/main/anchor-browser-web-scraper)                |
| [Batch LLM Evaluator](/docs/guides/example-projects/batch-llm-evaluator)                                             | Evaluate multiple LLM models and stream the results to the frontend.                                                                   | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/batch-llm-evaluator)                       |
| [Claude changelog generator](/docs/guides/example-projects/claude-changelog-generator)                               | Automatically generate professional changelogs from git commits using Claude.                                                          | —         | [View the repo](https://github.com/triggerdotdev/examples/tree/main/changelog-generator)                       |
| [Claude GitHub wiki agent](/docs/guides/example-projects/claude-github-wiki)                                         | Generate and maintain GitHub wiki documentation with Claude-powered analysis.                                                          | —         | [View the repo](https://github.com/triggerdotdev/examples/tree/main/claude-agent-github-wiki)                  |
| [Claude thinking chatbot](/docs/guides/example-projects/claude-thinking-chatbot)                                     | Use Vercel's AI SDK and Anthropic's Claude 3.7 model to create a thinking chatbot.                                                     | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/claude-thinking-chatbot)                   |
| [Cursor background agent](/docs/guides/example-projects/cursor-background-agent)                                     | Run Cursor's headless CLI agent as a background task, streaming live output to the browser.                                            | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/cursor-cli-demo)                           |
| [Human-in-the-loop workflow](/docs/guides/example-projects/human-in-the-loop-workflow)                               | Create audio summaries of newspaper articles using a human-in-the-loop workflow built with ReactFlow and Trigger.dev waitpoint tokens. | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/article-summary-workflow)                  |
| [Mastra agents with memory](/docs/guides/example-projects/mastra-agents-with-memory)                                 | Use Mastra to create a weather agent that can collect live weather data and generate clothing recommendations.                         | —         | [View the repo](https://github.com/triggerdotdev/examples/tree/main/mastra-agents)                             |
| [OpenAI Agents SDK for Python guardrails](/docs/guides/example-projects/openai-agent-sdk-guardrails)                 | Use the OpenAI Agents SDK for Python to create a guardrails system for your AI agents.                                                 | —         | [View the repo](https://github.com/triggerdotdev/examples/tree/main/openai-agent-sdk-guardrails-examples)      |
| [OpenAI Agents SDK for TypeScript playground](/docs/guides/example-projects/openai-agents-sdk-typescript-playground) | A playground containing 7 AI agents using the OpenAI Agents SDK for TypeScript with Trigger.dev.                                       | —         | [View the repo](https://github.com/triggerdotdev/examples/tree/main/openai-agents-sdk-with-trigger-playground) |
| [Product image generator](/docs/guides/example-projects/product-image-generator)                                     | Transform basic product photos into professional marketing shots using Replicate's image generation models.                            | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/product-image-generator)                   |
| [Python web crawler](/docs/guides/python/python-crawl4ai)                                                            | Use Python, Crawl4AI and Playwright to create a headless web crawler with Trigger.dev.                                                 | —         | [View the repo](https://github.com/triggerdotdev/examples/tree/main/python-crawl4ai)                           |
| [Realtime CSV Importer](/docs/guides/example-projects/realtime-csv-importer)                                         | Upload a CSV file and see the progress of the task streamed to the frontend.                                                           | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/realtime-csv-importer)                     |
| [Realtime Fal.ai image generation](/docs/guides/example-projects/realtime-fal-ai)                                    | Generate an image from a prompt using Fal.ai and show the progress of the task on the frontend using Realtime.                         | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/realtime-fal-ai-image-generation)          |
| [Smart Spreadsheet](/docs/guides/example-projects/smart-spreadsheet)                                                 | Enrich company data using Exa search and Claude with real-time streaming results.                                                      | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/smart-spreadsheet)                         |
| [Turborepo monorepo with Prisma](/docs/guides/example-projects/turborepo-monorepo-prisma)                            | Use Prisma in a Turborepo monorepo with Trigger.dev.                                                                                   | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/monorepos/turborepo-prisma-tasks-package)  |
| [Vercel AI SDK image generator](/docs/guides/example-projects/vercel-ai-sdk-image-generator)                         | Use the Vercel AI SDK to generate images from a prompt.                                                                                | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/vercel-ai-sdk-image-generator)             |
| [Vercel AI SDK deep research agent](/docs/guides/example-projects/vercel-ai-sdk-deep-research)                       | Use the Vercel AI SDK to generate comprehensive PDF reports using a deep research agent.                                               | Next.js   | [View the repo](https://github.com/triggerdotdev/examples/tree/main/vercel-ai-sdk-deep-research-agent)         |

## Example tasks

Task code you can copy and paste to use in your project. They can all be extended and customized to fit your needs.

| Example task                                                                  | Description                                                                                                                                          |
| :---------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| [DALL·E 3 image generation](/docs/guides/examples/dall-e3-generate-image)          | Use OpenAI's GPT-4o and DALL·E 3 to generate an image and text.                                                                                      |
| [Deepgram audio transcription](/docs/guides/examples/deepgram-transcribe-audio)    | Transcribe audio using Deepgram's speech recognition API.                                                                                            |
| [Fal.ai image to cartoon](/docs/guides/examples/fal-ai-image-to-cartoon)           | Convert an image to a cartoon using Fal.ai, and upload the result to Cloudflare R2.                                                                  |
| [Fal.ai with Realtime](/docs/guides/examples/fal-ai-realtime)                      | Generate an image from a prompt using Fal.ai and show the progress of the task on the frontend using Realtime.                                       |
| [FFmpeg video processing](/docs/guides/examples/ffmpeg-video-processing)           | Use FFmpeg to process a video in various ways and save it to Cloudflare R2.                                                                          |
| [Firecrawl URL crawl](/docs/guides/examples/firecrawl-url-crawl)                   | Learn how to use Firecrawl to crawl a URL and return LLM-ready markdown.                                                                             |
| [LibreOffice PDF conversion](/docs/guides/examples/libreoffice-pdf-conversion)     | Convert a document to PDF using LibreOffice.                                                                                                         |
| [Lightpanda](/docs/guides/examples/lightpanda)                                     | Use Lightpanda browser (or cloud version) to get a webpage's content.                                                                                |
| [OpenAI with retrying](/docs/guides/examples/open-ai-with-retrying)                | Create a reusable OpenAI task with custom retry options.                                                                                             |
| [PDF to image](/docs/guides/examples/pdf-to-image)                                 | Use `MuPDF` to turn a PDF into images and save them to Cloudflare R2.                                                                                |
| [Puppeteer](/docs/guides/examples/puppeteer)                                       | Use Puppeteer to generate a PDF or scrape a webpage.                                                                                                 |
| [React email](/docs/guides/examples/react-email)                                   | Send an email using React Email.                                                                                                                     |
| [React to PDF](/docs/guides/examples/react-pdf)                                    | Use `react-pdf` to generate a PDF and save it to Cloudflare R2.                                                                                      |
| [Resend email sequence](/docs/guides/examples/resend-email-sequence)               | Send a sequence of emails over several days using Resend with Trigger.dev.                                                                           |
| [Replicate image generation](/docs/guides/examples/replicate-image-generation)     | Learn how to generate images from source image URLs using Replicate and Trigger.dev.                                                                 |
| [Satori](/docs/guides/examples/satori)                                             | Generate OG images using React Satori.                                                                                                               |
| [Scrape Hacker News](/docs/guides/examples/scrape-hacker-news)                     | Scrape Hacker News using BrowserBase and Puppeteer, summarize the articles with ChatGPT and send an email of the summary every weekday using Resend. |
| [Sentry error tracking](/docs/guides/examples/sentry-error-tracking)               | Automatically send errors to Sentry from your tasks.                                                                                                 |
| [Sharp image processing](/docs/guides/examples/sharp-image-processing)             | Use Sharp to process an image and save it to Cloudflare R2.                                                                                          |
| [Supabase database operations](/docs/guides/examples/supabase-database-operations) | Run basic CRUD operations on a table in a Supabase database using Trigger.dev.                                                                       |
| [Supabase Storage upload](/docs/guides/examples/supabase-storage-upload)           | Download a video from a URL and upload it to Supabase Storage using S3.                                                                              |
| [Vercel AI SDK](/docs/guides/examples/vercel-ai-sdk)                               | Use Vercel AI SDK to generate text using OpenAI.                                                                                                     |
| [Vercel sync environment variables](/docs/guides/examples/vercel-sync-env-vars)    | Automatically sync environment variables from your Vercel projects to Trigger.dev.                                                                   |

<Note>
  If you would like to see a guide for your framework, or an example task for your use case, please
  request it in our [Discord server](https://trigger.dev/discord) and we'll add it to the list.
</Note>
