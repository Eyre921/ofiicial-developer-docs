---
title: "Docs (148 pages)"
source: https://openrouter.ai/docs/_llms/docs.md
path: docs/_llms/docs
---

# OpenRouter | Documentation: Docs

## Docs

### Overview

- [Quickstart](https://openrouter.ai/docs/quickstart.md): Get started with OpenRouter
- [Principles](https://openrouter.ai/docs/guides/overview/principles.md): Core principles and values of OpenRouter
- [Models](https://openrouter.ai/docs/guides/overview/models.md): One API for hundreds of models
- [Frequently Asked Questions](https://openrouter.ai/docs/faq.md): Common questions about OpenRouter
- [Report Feedback](https://openrouter.ai/docs/guides/overview/report-feedback.md)

#### Multimodal

- [Multimodal Capabilities](https://openrouter.ai/docs/guides/overview/multimodal/overview.md): Send images, PDFs, audio, and video to OpenRouter models, generate speech from text, or transcribe audio to text
- [Image Generation](https://openrouter.ai/docs/guides/overview/multimodal/image-generation.md): How to generate images with OpenRouter's dedicated Image API
- [Video Generation](https://openrouter.ai/docs/guides/overview/multimodal/video-generation.md): How to generate videos with OpenRouter models
- [Text-to-Speech](https://openrouter.ai/docs/guides/overview/multimodal/tts.md): How to generate speech audio from text with OpenRouter models
- [Speech-to-Text](https://openrouter.ai/docs/guides/overview/multimodal/stt.md): How to transcribe audio into text with OpenRouter models
- [Audio](https://openrouter.ai/docs/guides/overview/multimodal/audio.md): How to send and receive audio with OpenRouter models
- [PDF Inputs](https://openrouter.ai/docs/guides/overview/multimodal/pdfs.md): How to send PDFs to OpenRouter models
- [Image Inputs](https://openrouter.ai/docs/guides/overview/multimodal/image-understanding.md): How to send images to OpenRouter models
- [Video Inputs](https://openrouter.ai/docs/guides/overview/multimodal/videos.md): How to send video files to OpenRouter models

### Models & Routing

- [Model Fallbacks](https://openrouter.ai/docs/guides/routing/model-fallbacks.md): Automatic failover between models
- [Provider Routing](https://openrouter.ai/docs/guides/routing/provider-selection.md): Route requests to the best provider
- [Auto Exacto](https://openrouter.ai/docs/guides/routing/auto-exacto.md): Automatic tool-calling provider optimization
- [Private Models](https://openrouter.ai/docs/guides/routing/private-models.md): Bring your own model to OpenRouter, scoped to approved users and organizations

#### Model Variants

- [Model Variants](https://openrouter.ai/docs/guides/routing/model-variants/overview.md): How variant suffixes relate to the models catalog and how clients should resolve them
- [Free Variant](https://openrouter.ai/docs/guides/routing/model-variants/free.md): Access free models with the :free variant
- [Extended Variant](https://openrouter.ai/docs/guides/routing/model-variants/extended.md): Extended context windows with :extended
- [Exacto Variant](https://openrouter.ai/docs/guides/routing/model-variants/exacto.md): Route requests with quality-first provider sorting
- [Thinking Variant](https://openrouter.ai/docs/guides/routing/model-variants/thinking.md): Enable extended reasoning with :thinking
- [Online Variant](https://openrouter.ai/docs/guides/routing/model-variants/online.md): Real-time web search with :online
- [Nitro Variant](https://openrouter.ai/docs/guides/routing/model-variants/nitro.md): High-speed model inference with :nitro
- [Floor Variant](https://openrouter.ai/docs/guides/routing/model-variants/floor.md): Lowest-cost model inference with :floor

#### Routers

- [Auto Router](https://openrouter.ai/docs/guides/routing/routers/auto-router.md): Automatically select the best model for your prompt
- [Body Builder](https://openrouter.ai/docs/guides/routing/routers/body-builder.md): Generate multiple parallel API requests from natural language
- [Free Models Router](https://openrouter.ai/docs/guides/routing/routers/free-router.md): Get free AI inference by routing to available free models
- [Latest Model Resolution](https://openrouter.ai/docs/guides/routing/routers/latest-resolution.md): Always target the newest version of a model family with a single slug
- [Pareto Router](https://openrouter.ai/docs/guides/routing/routers/pareto-router.md): Pick a coding model by minimum coding score without choosing a specific model
- [Fusion Router](https://openrouter.ai/docs/guides/routing/routers/fusion-router.md): Multi-model deliberation as a model slug
- [Jev Router](https://openrouter.ai/docs/guides/routing/routers/jev-router.md): Let Jev pick the model and reasoning effort for each request, within model lists you control
- [Switchyard Router](https://openrouter.ai/docs/guides/routing/routers/switchyard-router.md): Switch between multiple models of your choice to optimize the cost of the request

### Tool Calling

- [Client Tools](https://openrouter.ai/docs/guides/features/tool-calling.md): Use client tools in your prompts

#### Server Tools

- [Server Tools](https://openrouter.ai/docs/guides/features/server-tools.md): Tools operated by OpenRouter that models can call during request
- [Web Search](https://openrouter.ai/docs/guides/features/server-tools/web-search.md): Give any model access to real-time web information
- [Web Fetch](https://openrouter.ai/docs/guides/features/server-tools/web-fetch.md): Give any model the ability to fetch content from URLs
- [Datetime](https://openrouter.ai/docs/guides/features/server-tools/datetime.md): Give any model access to the current date and time
- [Image Generation](https://openrouter.ai/docs/guides/features/server-tools/image-generation.md): Generate images from text prompts with any model
- [Apply Patch](https://openrouter.ai/docs/guides/features/server-tools/apply-patch.md): Let models propose file changes via V4A diffs
- [Shell](https://openrouter.ai/docs/guides/features/server-tools/shell.md): Give any model a sandboxed hosted shell on the Responses and Messages APIs
- [Bash](https://openrouter.ai/docs/guides/features/server-tools/bash.md): Give any model a sandboxed shell to run commands server-side
- [Search Models](https://openrouter.ai/docs/guides/features/server-tools/search-models.md): Let any model search the OpenRouter model catalog
- [Tool Search](https://openrouter.ai/docs/guides/features/server-tools/tool-search.md): Let the model discover tools on demand instead of loading every definition up front
- [Fusion](https://openrouter.ai/docs/guides/features/server-tools/fusion.md): Multi-model deliberation as a server tool
- [Advisor](https://openrouter.ai/docs/guides/features/server-tools/advisor.md): Consult a stronger model mid-generation as a server tool
- [Subagent](https://openrouter.ai/docs/guides/features/server-tools/subagent.md): Delegate tasks to a smaller, faster model as a server tool

#### Plugins

- [Plugins](https://openrouter.ai/docs/guides/features/plugins.md): Extend model capabilities with OpenRouter plugins
- [Web Search](https://openrouter.ai/docs/guides/features/plugins/web-search.md): Model-agnostic grounding
- [Response Healing](https://openrouter.ai/docs/guides/features/plugins/response-healing.md): Automatically fix malformed JSON responses

### Features

- [Notifications](https://openrouter.ai/docs/guides/features/notifications.md): Choose which OpenRouter alerts you receive and where they are delivered
- [Files API](https://openrouter.ai/docs/guides/features/files-api.md): Upload files to your workspace and use them in requests
- [Containers](https://openrouter.ai/docs/guides/features/containers.md): How sandbox containers work for the shell and bash server tools
- [Presets](https://openrouter.ai/docs/guides/features/presets.md): Manage your LLM configurations
- [Custom Classifiers](https://openrouter.ai/docs/guides/features/classifiers.md): Automatically categorize LLM generations in your workspace
- [Response Caching](https://openrouter.ai/docs/guides/features/response-caching.md): Cache responses for identical API requests to save time and money
- [Structured Outputs](https://openrouter.ai/docs/guides/features/structured-outputs.md): Return structured data from your models
- [Message Transforms](https://openrouter.ai/docs/guides/features/message-transforms.md): Transform prompt messages
- [Zero Completion Insurance](https://openrouter.ai/docs/guides/features/zero-completion-insurance.md): OpenRouter will not charge you for zero token responses
- [App Attribution](https://openrouter.ai/docs/app-attribution.md): Get your app featured in OpenRouter rankings and analytics
- [Batch API Quickstart](https://openrouter.ai/docs/batch-quickstart.md): Submit and retrieve asynchronous batches of inference requests
- [Service Tiers](https://openrouter.ai/docs/guides/features/service-tiers.md): Control cost and latency tradeoffs with service tier selection
- [Router Metadata](https://openrouter.ai/docs/guides/features/router-metadata.md): Surface routing decisions on every response with a single opt-in header

#### Workspaces

- [Workspaces](https://openrouter.ai/docs/guides/features/workspaces.md): Organize your projects, teams, and agents into separate environments
- [Workspace Budgets](https://openrouter.ai/docs/guides/features/workspaces/workspace-budgets.md): Set spending limits per workspace with automatic enforcement
- [Switching Workspaces](https://openrouter.ai/docs/guides/features/workspaces/switching.md): Change which workspace your Chat and Fusion requests run in.

#### Guardrails

- [Guardrails](https://openrouter.ai/docs/guides/features/guardrails.md): Control spending and model access for your organization
- [Sensitive Info Guardrail](https://openrouter.ai/docs/guides/features/guardrails/sensitive-info.md): Automatically detect and handle sensitive information in API requests
- [Detected Secret Formats](https://openrouter.ai/docs/guides/features/guardrails/secret-formats.md): Full list of API key and credential formats detected by the Secrets guardrail preset

##### Prompt Injection Detection

- [Prompt Injection Detection](https://openrouter.ai/docs/guides/features/guardrails/prompt-injection.md): Regex-based prompt injection guardrail patterns
- [Allowlist](https://openrouter.ai/docs/guides/features/guardrails/prompt-injection/allowlist.md): Exclude known-safe phrases from prompt injection detection

### Observability

- [Logs](https://openrouter.ai/docs/guides/features/logs.md): Inspect individual generations, upstream requests, sessions, and async jobs from your OpenRouter dashboard
- [Activity](https://openrouter.ai/docs/guides/features/activity.md): Analyze spend, request volume, tokens, and trends across your OpenRouter usage from the Activity dashboard
- [Input & Output Logging](https://openrouter.ai/docs/guides/features/input-output-logging.md): Privately store and review your prompts and completions

#### Broadcast

- [Broadcast](https://openrouter.ai/docs/guides/features/broadcast.md): Send traces from your OpenRouter requests to external observability platforms
- [Arize AX](https://openrouter.ai/docs/guides/features/broadcast/arize.md): Send traces to Arize AX
- [Braintrust](https://openrouter.ai/docs/guides/features/broadcast/braintrust.md): Send traces to Braintrust
- [ClickHouse](https://openrouter.ai/docs/guides/features/broadcast/clickhouse.md): Send traces to ClickHouse
- [Comet Opik](https://openrouter.ai/docs/guides/features/broadcast/opik.md): Send traces to Comet Opik
- [Datadog](https://openrouter.ai/docs/guides/features/broadcast/datadog.md): Send traces to Datadog
- [Elastic Observability](https://openrouter.ai/docs/guides/features/broadcast/elastic.md): Send traces to Elastic Observability
- [Google BigQuery](https://openrouter.ai/docs/guides/features/broadcast/bigquery.md): Send traces to Google BigQuery
- [Grafana Cloud](https://openrouter.ai/docs/guides/features/broadcast/grafana.md): Send traces to Grafana Cloud
- [Langfuse](https://openrouter.ai/docs/guides/features/broadcast/langfuse.md): Send traces to Langfuse
- [LangSmith](https://openrouter.ai/docs/guides/features/broadcast/langsmith.md): Send traces to LangSmith
- [New Relic](https://openrouter.ai/docs/guides/features/broadcast/newrelic.md): Send traces to New Relic
- [OpenTelemetry Collector](https://openrouter.ai/docs/guides/features/broadcast/otel-collector.md): Send traces to any OpenTelemetry-compatible backend
- [PostHog](https://openrouter.ai/docs/guides/features/broadcast/posthog.md): Send traces to PostHog
- [Raindrop](https://openrouter.ai/docs/guides/features/broadcast/raindrop.md): Send traces to Raindrop
- [Ramp](https://openrouter.ai/docs/guides/features/broadcast/ramp.md): Send traces to Ramp
- [S3 / S3-Compatible](https://openrouter.ai/docs/guides/features/broadcast/s3.md): Send traces to Amazon S3 or S3-compatible storage
- [Sentry](https://openrouter.ai/docs/guides/features/broadcast/sentry.md): Send traces to Sentry
- [Snowflake](https://openrouter.ai/docs/guides/features/broadcast/snowflake.md): Send traces to Snowflake
- [W&B Weave](https://openrouter.ai/docs/guides/features/broadcast/weave.md): Send traces to W&B Weave
- [Webhook](https://openrouter.ai/docs/guides/features/broadcast/webhook.md): Send traces to any HTTP endpoint

### Authentication

- [OAuth PKCE](https://openrouter.ai/docs/guides/overview/auth/oauth.md): Connect your users to OpenRouter
- [Workload Identity Federation](https://openrouter.ai/docs/guides/overview/auth/workload-identity-federation.md): Call OpenRouter from workloads signed in with your own identity provider, without long-lived API keys
- [Management API Keys](https://openrouter.ai/docs/guides/overview/auth/management-api-keys.md): Manage API keys programmatically
- [Security settings](https://openrouter.ai/docs/guides/overview/auth/security-settings.md): Review and manage API key security settings
- [BYOK](https://openrouter.ai/docs/guides/overview/auth/byok.md): Bring your own provider API keys
- [Single Sign-On (SSO)](https://openrouter.ai/docs/guides/features/sso.md): Let your team sign in to OpenRouter through your identity provider
- [SCIM Group Mappings](https://openrouter.ai/docs/guides/features/scim-mappings.md): Automatically provision workspace access from your identity provider groups

### Ori

- [Ori](https://openrouter.ai/docs/guides/ori/overview.md): Ori is OpenRouter's family of tools for putting agents to work with any model, in your terminal, in Slack, and on your desktop
- [Ori Eval](https://openrouter.ai/docs/guides/ori/eval.md): Find the best model for your project by testing your agent on real prompts, with one harness and one model for each run
- [Ori Harness](https://openrouter.ai/docs/guides/ori/harness.md): Run your existing agent CLI on OpenRouter with any model, organization guardrails, and one bill
- [Ori Codex](https://openrouter.ai/docs/guides/ori/codex.md): Run the Codex CLI and Codex Desktop on OpenRouter with one setup command, and go back with one reset
- [File Writing](https://openrouter.ai/docs/guides/ori/files.md): Find the files and directories that Ori creates during a run
- [Ori Configuration](https://openrouter.ai/docs/guides/ori/configuration.md): How to configure Ori, from a single shell to a managed fleet, plus every setting it reads
- [Chatting with Interns](https://openrouter.ai/docs/guides/ori/intern-chat.md): Stream a chat completion from one of your interns with an API key, and answer its questions and permission requests in a second request
- [Vault Secrets for Interns](https://openrouter.ai/docs/guides/ori/vault.md): Store host-bound secrets for a workspace or an intern with the Vault API
- [Changelog](https://openrouter.ai/docs/guides/ori/changelog.md): Curated release notes for the Ori CLI, with version history and changes across releases.

### Developer Tools

- [MCP](https://openrouter.ai/docs/guides/overview/mcp-server.md): Connect your AI coding tools to OpenRouter over MCP
- [Terraform Provider](https://openrouter.ai/docs/guides/overview/terraform.md): Manage OpenRouter resources as infrastructure-as-code with Terraform
- [Stripe Projects](https://openrouter.ai/docs/guides/overview/stripe-projects.md): Add OpenRouter to your app with the Stripe Projects CLI

### Privacy

- [Data Collection](https://openrouter.ai/docs/guides/privacy/data-collection.md): What data OpenRouter collects
- [Provider Logging](https://openrouter.ai/docs/guides/privacy/provider-logging.md): Provider logging and data retention policies
- [Zero Data Retention](https://openrouter.ai/docs/guides/features/zdr.md): How OpenRouter gives you control over your data
- [In-Region Routing](https://openrouter.ai/docs/guides/features/in-region-routing.md): Keep prompts and completions inside the EU or the US
- [Sovereign AI](https://openrouter.ai/docs/guides/features/sovereign-ai.md): Keep AI workloads within national and regional boundaries

### Best Practices

- [Latency and Performance](https://openrouter.ai/docs/guides/best-practices/latency-and-performance.md): Understanding OpenRouter's performance characteristics and practical DX optimization recipes
- [Prompt Caching](https://openrouter.ai/docs/guides/best-practices/prompt-caching.md): Cache prompt messages
- [Spend Controls](https://openrouter.ai/docs/guides/best-practices/spend-controls.md): How to structure workspace budgets, guardrails, and access controls for your organization
- [Uptime Optimization](https://openrouter.ai/docs/guides/best-practices/uptime-optimization.md): OpenRouter tracks provider availability
- [Reasoning Tokens](https://openrouter.ai/docs/guides/best-practices/reasoning-tokens.md)

### Community

- [Provider Integration](https://openrouter.ai/docs/guides/community/for-providers.md)
- [Frameworks and Integrations Overview](https://openrouter.ai/docs/guides/community/frameworks-and-integrations-overview.md): Using OpenRouter with Popular Frameworks and Integrations
- [Awesome OpenRouter](https://openrouter.ai/docs/guides/community/awesome-openrouter.md): Community-curated list of projects built with OpenRouter
- [Effect AI SDK](https://openrouter.ai/docs/guides/community/effect-ai-sdk.md): Integrate OpenRouter using the Effect AI SDK
- [Arize AX](https://openrouter.ai/docs/guides/community/arize.md): Using OpenRouter with Arize AX
- [LangChain](https://openrouter.ai/docs/guides/community/langchain.md): Using OpenRouter with LangChain
- [LiveKit](https://openrouter.ai/docs/guides/community/livekit.md): Using OpenRouter with LiveKit Agents
- [Langfuse](https://openrouter.ai/docs/guides/community/langfuse.md): Using OpenRouter with Langfuse
- [Mastra](https://openrouter.ai/docs/guides/community/mastra.md): Using OpenRouter with Mastra
- [OpenAI SDK](https://openrouter.ai/docs/guides/community/openai-sdk.md): Using OpenRouter with OpenAI SDK
- [Anthropic Agent SDK](https://openrouter.ai/docs/guides/community/anthropic-agent-sdk.md): Using OpenRouter with the Anthropic Agent SDK
- [PydanticAI](https://openrouter.ai/docs/guides/community/pydantic-ai.md): Using OpenRouter with PydanticAI
- [Render](https://openrouter.ai/docs/guides/community/render.md): Using OpenRouter with Render Workflows
- [Replit](https://openrouter.ai/docs/guides/community/replit.md): Using OpenRouter with Replit Agent and Replit Apps
- [TanStack AI](https://openrouter.ai/docs/guides/community/tanstack-ai.md): Using OpenRouter with TanStack AI
- [Jev Documentation: Using the TypeSafe Decision Model on OpenRouter](https://openrouter.ai/docs/guides/community/jev.md): The OpenRouter hub for Jev, the TypeSafe decision model. What Jev is, how to get access, the Decisions API, TypeScript and Python SDKs, cookbooks, pricing, and demos
- [Jev Tutorial: Make Your First Decision Call on OpenRouter](https://openrouter.ai/docs/guides/community/jev-tutorial.md): Step-by-step Jev tutorial. Send a typed decision request to the TypeSafe model on OpenRouter with curl, TypeScript, or Python and read the probabilities it returns
- [Multimodal Decisions: Images in the Decisions API](https://openrouter.ai/docs/guides/community/multimodal-decisions.md): Send images to Decisions models on OpenRouter. Quickstart, the image part format, supported models, and size limits.
- [Jev SDK for TypeScript and Python (TypeSafe SDK)](https://openrouter.ai/docs/guides/community/typesafe-sdk.md): Point the official TypeSafe JavaScript or Python SDK at OpenRouter to call Jev with your OpenRouter API key
- [Vercel AI SDK](https://openrouter.ai/docs/guides/community/vercel-ai-sdk.md): Using OpenRouter with Vercel AI SDK
- [Xcode](https://openrouter.ai/docs/guides/community/xcode.md): Using OpenRouter with Apple Intelligence in Xcode
- [Zapier](https://openrouter.ai/docs/guides/community/zapier.md): Build AI automations with OpenRouter & Zapier
- [Infisical](https://openrouter.ai/docs/guides/community/infisical.md): Automatic API Key Rotation with Infisical

