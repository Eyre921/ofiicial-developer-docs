---
title: "API Reference (166 pages)"
source: https://openrouter.ai/docs/_llms/api-reference.txt
path: docs/_llms/api-reference.txt
---

# OpenRouter | Documentation: API Reference

## API Reference

### API Guides

- [API Reference](https://openrouter.ai/docs/api_reference/overview.md): An overview of OpenRouter's API
- [Streaming](https://openrouter.ai/docs/api_reference/streaming.md)
- [Embeddings](https://openrouter.ai/docs/api_reference/embeddings.md): Generate vector embeddings from text and images
- [Limits](https://openrouter.ai/docs/api_reference/limits.md): Credit Limits and Rate Limits
- [Authentication](https://openrouter.ai/docs/api_reference/authentication.md): API Authentication
- [Parameters](https://openrouter.ai/docs/api_reference/parameters.md)
- [Errors and Debugging](https://openrouter.ai/docs/api_reference/errors-and-debugging.md): API Errors and Debugging

#### Responses API

- [Responses API](https://openrouter.ai/docs/api_reference/responses/overview.md): OpenAI-compatible Responses API
- [Basic Usage](https://openrouter.ai/docs/api_reference/responses/basic-usage.md): Getting started with the Responses API
- [Reasoning](https://openrouter.ai/docs/api_reference/responses/reasoning.md): Advanced reasoning capabilities with the Responses API
- [Tool Calling](https://openrouter.ai/docs/api_reference/responses/tool-calling.md): Function calling and tool integration with the Responses API
- [Web Search](https://openrouter.ai/docs/api_reference/responses/web-search.md): Real-time web search integration with the Responses API
- [Error Handling](https://openrouter.ai/docs/api_reference/responses/error-handling.md): Understanding and handling errors in the Responses API

### Versioning

- [API Versioning](https://openrouter.ai/docs/api_reference/versioning.md): How the OpenRouter API is versioned, what we consider a breaking change, and how deprecations are communicated.
- [API Changelog](https://openrouter.ai/docs/changelog.md): Changes to the OpenRouter API, generated from the OpenAPI specification on every release.

### API Reference

#### Analytics

- [Get user activity grouped by endpoint](https://openrouter.ai/docs/api/api-reference/analytics/get-user-activity-grouped-by-endpoint.md): Returns user activity data grouped by endpoint for the last 30 (completed) UTC days. Pass `workspace_id` to scope the response to a single workspace. Pass `group_by=workspace` to split each row per workspace and include `workspace_id` on every item; by default rows are aggregated across workspaces a…
- [Get available analytics metrics and dimensions](https://openrouter.ai/docs/api/api-reference/analytics/get-available-analytics-metrics-and-dimensions.md): Returns the available metrics, dimensions, filter operators, and granularities for the analytics query endpoint. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Query analytics data](https://openrouter.ai/docs/api/api-reference/analytics/query-analytics-data.md): Execute an analytics query with specified metrics, dimensions, filters, and time range. [Management key](/docs/guides/overview/auth/management-api-keys) required.

#### alpha.decisions

- [Submit a Decisions request](https://openrouter.ai/docs/api/api-reference/alphadecisions/submit-a-decisions-request.md): Submits a Decisions request to the Decisions router

#### TTS

- [Create speech](https://openrouter.ai/docs/api/api-reference/tts/create-speech.md): Synthesizes audio from the input text. Returns a raw audio bytestream in the requested format (e.g. mp3, pcm, wav).

#### STT

- [Create transcription](https://openrouter.ai/docs/api/api-reference/stt/create-transcription.md): Transcribes audio into text. Accepts base64-encoded audio input as JSON, an OpenAI-style multipart/form-data file upload, or a URL the provider downloads directly, and returns the transcribed text.

#### OAuth

- [Exchange authorization code for API key](https://openrouter.ai/docs/api/api-reference/oauth/exchange-authorization-code-for-api-key.md): Exchange an authorization code from the PKCE flow for a user-controlled API key
- [Create authorization code](https://openrouter.ai/docs/api/api-reference/oauth/create-authorization-code.md): Create an authorization code for the PKCE flow to generate a user-controlled API key
- [OpenRouter access token signing keys](https://openrouter.ai/docs/api/api-reference/oauth/openrouter-access-token-signing-keys.md): RFC 7517 JWK Set containing the public keys OpenRouter signs access tokens with.
- [Exchange a workload identity token](https://openrouter.ai/docs/api/api-reference/oauth/exchange-a-workload-identity-token.md): RFC 8693 token exchange. Presents a JWT from an issuer your organization trusts (Settings → Workload identity) and receives a short-lived OpenRouter access token that acts as the API key the matching federation policy targets.

#### Batch

- [List batches](https://openrouter.ai/docs/api/api-reference/batch/list-batches.md): Lists batches in the workspace of the authenticating API key, newest first. To fetch the next page, pass the previous page's `last_id` as `after`. List items omit `results`. Use `GET /batches/{id}` to get them. See the [Batch API Quickstart](https://openrouter.ai/docs/batch-quickstart).
- [Create a batch](https://openrouter.ai/docs/api/api-reference/batch/create-a-batch.md): Creates a batch of requests that run asynchronously against a single endpoint (`/v1/chat/completions`, `/v1/responses`, `/v1/messages`, `/v1/embeddings`). Returns `202` with `status: "validating"`. Poll `GET /batches/{id}` for progress and results. See the [Batch API Quickstart](https://openrouter.a…
- [Get a batch](https://openrouter.ai/docs/api/api-reference/batch/get-a-batch.md): Returns a batch with its status and request counts. Batches in a terminal status include `results`. Failed batches report the reason in `error.message`. See the [Batch API Quickstart](https://openrouter.ai/docs/batch-quickstart).
- [Delete a batch](https://openrouter.ai/docs/api/api-reference/batch/delete-a-batch.md): Deletes a batch in a terminal status (`completed`, `failed`, `expired`, or `cancelled`) and its stored requests and results. Batches still in progress return `409`. Billing and usage records are kept. See the [Batch API Quickstart](https://openrouter.ai/docs/batch-quickstart).

#### Benchmarks

- [List Benchmarks](https://openrouter.ai/docs/api/api-reference/benchmarks/list-benchmarks.md): Unified benchmark endpoint that aggregates scores from multiple benchmark sources (Artificial Analysis, Design Arena, and OpenRouter's own tau-bench, GPQA, and web-search evals). Filter by source to reproduce the exact shapes from the legacy per-source endpoints, or use task_type to find models suit…

#### BYOK

- [List BYOK provider credentials](https://openrouter.ai/docs/api/api-reference/byok/list-byok-provider-credentials.md): List the bring-your-own-key (BYOK) provider credentials for the authenticated entity's default workspace. Use the `workspace_id` query parameter to scope the result to a different workspace, or the `provider` query parameter to filter by upstream provider. [Management key](/docs/guides/overview/auth…
- [Create a BYOK provider credential](https://openrouter.ai/docs/api/api-reference/byok/create-a-byok-provider-credential.md): Create a new bring-your-own-key (BYOK) provider credential. The raw key is encrypted at rest and never returned in API responses. When `workspace_id` is omitted, the credential is created in the default workspace; if that default has been deleted, the request returns a 400 and you must pass `workspa…
- [Get a BYOK provider credential](https://openrouter.ai/docs/api/api-reference/byok/get-a-byok-provider-credential.md): Get a single bring-your-own-key (BYOK) provider credential by its `id`. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Delete a BYOK provider credential](https://openrouter.ai/docs/api/api-reference/byok/delete-a-byok-provider-credential.md): Delete (soft-delete) a bring-your-own-key (BYOK) provider credential by its `id`. The encrypted key material is wiped and the record is marked as deleted. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Update a BYOK provider credential](https://openrouter.ai/docs/api/api-reference/byok/update-a-byok-provider-credential.md): Update an existing bring-your-own-key (BYOK) provider credential by its `id`. Include the `key` field to rotate the raw provider API key in-place (the previous key material is overwritten). Use `allowed_api_key_hashes` to restrict the credential to specific OpenRouter API keys (`null` clears the res…

#### Chat

- [Create a chat completion](https://openrouter.ai/docs/api/api-reference/chat/create-a-chat-completion.md): Sends a request for a model response for the given chat conversation. Supports both streaming and non-streaming modes.

#### Classifications

- [Task classification market share](https://openrouter.ai/docs/api/api-reference/classifications/task-classification-market-share.md): Returns the market-share breakdown of OpenRouter traffic by task classification (e.g. code generation, web search, summarization) over a trailing time window.

#### Containers

- [List container files](https://openrouter.ai/docs/api/api-reference/containers/list-container-files.md): Lists the files in a container, in lexicographic path order. The container id is the canonical id returned in bash/shell tool results; a restarted session is a separate container with its own id. Paginate with `limit` and `after` (pass the previous page’s `last_id`); `has_more: true` always means th…
- [Retrieve a container file](https://openrouter.ai/docs/api/api-reference/containers/retrieve-a-container-file.md): Returns the metadata of a single file in a container.
- [Download container file content](https://openrouter.ai/docs/api/api-reference/containers/download-container-file-content.md): Streams the raw bytes of a file in a container.
- [Promote a container file into workspace documents](https://openrouter.ai/docs/api/api-reference/containers/promote-a-container-file-into-workspace-documents.md): Copies a file from the container's sandbox prefix into the workspace's durable document storage, so it outlives the container. Returns the new document in the Files API shape, with a durable file id in the documents namespace. The copy counts against the workspace's storage quota. Unlike a direct up…

#### Credits

- [Get remaining credits](https://openrouter.ai/docs/api/api-reference/credits/get-remaining-credits.md): Get total credits purchased and used for the authenticated user. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Deprecated Coinbase Commerce charge endpoint](https://openrouter.ai/docs/api/api-reference/credits/deprecated-coinbase-commerce-charge-endpoint.md): Deprecated. The Coinbase APIs used by this endpoint have been deprecated, so Coinbase Commerce charges have been removed. Use the web credits purchase flow instead.

#### Datasets

- [Top apps by token usage](https://openrouter.ai/docs/api/api-reference/datasets/top-apps-by-token-usage.md): Returns the top public apps on OpenRouter ranked by token usage inside the requested date window, matching the public apps marketplace on openrouter.ai/apps. Token totals are `prompt_tokens + completion_tokens`; hidden and private apps are excluded and traffic from related app aliases is merged into…
- [Daily token totals for top 50 models](https://openrouter.ai/docs/api/api-reference/datasets/daily-token-totals-for-top-50-models.md): Returns the top 50 public models per day by total token usage on OpenRouter, plus a single aggregated `other` row per day that sums every model outside that top 50. Token totals are `prompt_tokens + completion_tokens`, matching the public rankings chart on openrouter.ai/rankings.
- [Cost per session by harness and model](https://openrouter.ai/docs/api/api-reference/datasets/cost-per-session-by-harness-and-model.md): Returns weekly refreshed, aggregated cost-per-session cells for the published harnesses. Sessions are never pooled across apps. Medians are of per-session USD spend, and privacy-preserving aggregation never exposes clerk_user_id values or per-session rows.

#### Embeddings

- [Submit an embedding request](https://openrouter.ai/docs/api/api-reference/embeddings/submit-an-embedding-request.md): Submits an embedding request to the embeddings router
- [List all embeddings models](https://openrouter.ai/docs/api/api-reference/embeddings/list-all-embeddings-models.md): Returns a list of all available embeddings models and their properties

#### End Users

- [List registered end users](https://openrouter.ai/docs/api/api-reference/end-users/list-registered-end-users.md): List registrations belonging to the authenticated organization. Inactive registrations are excluded by default. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Register an end user](https://openrouter.ai/docs/api/api-reference/end-users/register-an-end-user.md): Register a caller-supplied tracking ID under the authenticated organization. No login account, policy, or credentials are created. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Get a registered end user](https://openrouter.ai/docs/api/api-reference/end-users/get-a-registered-end-user.md): Retrieve an active or inactive registration by its URL-encoded, caller-supplied tracking ID. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Deactivate a registered end user](https://openrouter.ai/docs/api/api-reference/end-users/deactivate-a-registered-end-user.md): Soft-deactivate a registration while retaining its tracking ID. Repeat deactivation succeeds. This does not block inference; reactivate through PATCH. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Update a registered end user](https://openrouter.ai/docs/api/api-reference/end-users/update-a-registered-end-user.md): Update registration state without changing identity. State changes do not enforce inference access. [Management key](/docs/guides/overview/auth/management-api-keys) required.

#### Endpoints

- [Preview the impact of ZDR on the available endpoints](https://openrouter.ai/docs/api/api-reference/endpoints/preview-the-impact-of-zdr-on-the-available-endpoints.md)
- [List all endpoints for a model](https://openrouter.ai/docs/api/api-reference/endpoints/list-all-endpoints-for-a-model.md)

#### Files

- [List files](https://openrouter.ai/docs/api/api-reference/files/list-files.md): Lists files belonging to the workspace of the authenticating API key.
- [Upload a file](https://openrouter.ai/docs/api/api-reference/files/upload-a-file.md): Uploads a file to be referenced in future API calls. The file is stored under the workspace of the authenticating API key. Maximum file size: 100 MB; empty files are rejected. The file type is determined from the file contents — not the filename or the declared content type — and must be a PDF, a PN…
- [Get file metadata](https://openrouter.ai/docs/api/api-reference/files/get-file-metadata.md): Retrieves metadata for a single file owned by the requesting workspace.
- [Delete a file](https://openrouter.ai/docs/api/api-reference/files/delete-a-file.md): Deletes a file owned by the requesting workspace. Deletion is irreversible.
- [Download file content](https://openrouter.ai/docs/api/api-reference/files/download-file-content.md): Downloads the raw bytes of a file. Only files created server-side are downloadable; uploaded files return 400.

#### Generations

- [Get request & usage metadata for a generation](https://openrouter.ai/docs/api/api-reference/generations/get-request-&-usage-metadata-for-a-generation.md)
- [Get stored prompt, completion, and error content for a generation](https://openrouter.ai/docs/api/api-reference/generations/get-stored-prompt-completion-and-error-content-for-a-generation.md)
- [Submit feedback for a generation](https://openrouter.ai/docs/api/api-reference/generations/submit-feedback-for-a-generation.md): Submit structured feedback on a generation the authenticated user made. [Management key](/docs/guides/overview/auth/management-api-keys) required.

#### Guardrails

- [List guardrails](https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrails.md): List all guardrails for the authenticated user. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Create a guardrail](https://openrouter.ai/docs/api/api-reference/guardrails/create-a-guardrail.md): Create a new guardrail for the authenticated user. A newly created guardrail enforces nothing until it is assigned to API keys or organization members; `workspace_id` places the guardrail in a workspace but does not apply it to that workspace's traffic. To restrict all traffic in a workspace, update…
- [Get a guardrail](https://openrouter.ai/docs/api/api-reference/guardrails/get-a-guardrail.md): Get a single guardrail by ID. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Delete a guardrail](https://openrouter.ai/docs/api/api-reference/guardrails/delete-a-guardrail.md): Delete an existing guardrail. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Update a guardrail](https://openrouter.ai/docs/api/api-reference/guardrails/update-a-guardrail.md): Update an existing guardrail, or materialize an unconfigured workspace default guardrail. Collection fields use replace semantics: send the full desired set on every update. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [List key assignments for a guardrail](https://openrouter.ai/docs/api/api-reference/guardrails/list-key-assignments-for-a-guardrail.md): List all API key assignments for a specific guardrail. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Bulk assign keys to a guardrail](https://openrouter.ai/docs/api/api-reference/guardrails/bulk-assign-keys-to-a-guardrail.md): Assign multiple API keys to a specific guardrail. A key may hold at most one guardrail; assigning replaces any existing assignment. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Bulk unassign keys from a guardrail](https://openrouter.ai/docs/api/api-reference/guardrails/bulk-unassign-keys-from-a-guardrail.md): Unassign multiple API keys from a specific guardrail. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [List member assignments for a guardrail](https://openrouter.ai/docs/api/api-reference/guardrails/list-member-assignments-for-a-guardrail.md): List all organization member assignments for a specific guardrail. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Bulk assign members to a guardrail](https://openrouter.ai/docs/api/api-reference/guardrails/bulk-assign-members-to-a-guardrail.md): Assign multiple organization members to a specific guardrail. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Bulk unassign members from a guardrail](https://openrouter.ai/docs/api/api-reference/guardrails/bulk-unassign-members-from-a-guardrail.md): Unassign multiple organization members from a specific guardrail. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [List all key assignments](https://openrouter.ai/docs/api/api-reference/guardrails/list-all-key-assignments.md): List all API key guardrail assignments for the authenticated user. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [List all member assignments](https://openrouter.ai/docs/api/api-reference/guardrails/list-all-member-assignments.md): List all organization member guardrail assignments for the authenticated user. [Management key](/docs/guides/overview/auth/management-api-keys) required.

#### Images

- [Generate an image](https://openrouter.ai/docs/api/api-reference/images/generate-an-image.md): Generates an image from a text prompt via the image generation router
- [List image generation models](https://openrouter.ai/docs/api/api-reference/images/list-image-generation-models.md): Lists every image generation model with its top-level supported-parameter superset and a URL to its full per-endpoint records.
- [List endpoints for an image model](https://openrouter.ai/docs/api/api-reference/images/list-endpoints-for-an-image-model.md): Returns the full per-endpoint records for an image model: each endpoint's definitive supported parameters, pricing, and passthrough allowlist.

#### Interns

- [List interns](https://openrouter.ai/docs/api/api-reference/interns/list-interns.md): Lists interns visible to the authenticated key, newest first. Filter by workspace and one or more lifecycle statuses. The API key selects the caller, workspace and visible interns. An intern's own API key sees only that intern: the collection and every other intern answer 404 to it. There is no defa…
- [Create an intern](https://openrouter.ai/docs/api/api-reference/interns/create-an-intern.md): Creates an intern in an explicit workspace. The operation also creates its private vault. It can start provisioning immediately or wait for a later provision call. A retry with the same idempotency key and body resumes unfinished work. The request body is capped at 1048576 bytes and a larger body is…
- [Get an intern](https://openrouter.ai/docs/api/api-reference/interns/get-an-intern.md): Returns the public lifecycle state and settings for one visible intern. The API key selects the caller, workspace and visible interns. An intern's own API key sees only that intern: the collection and every other intern answer 404 to it. There is no default workspace fallback. Requests on regional h…
- [Delete an intern](https://openrouter.ai/docs/api/api-reference/interns/delete-an-intern.md): Starts safe teardown of the intern, its runtime and its private vault. The body is optional. Send `{"acknowledge_workspace_loss": true}` to delete a `destroy_failed` intern whose `last_failure_message` names `workspace_archive_failed`, accepting that its workspace is not backed up. The request body…
- [Update an intern](https://openrouter.ai/docs/api/api-reference/interns/update-an-intern.md): Changes the intern name, description, instructions or model. Omitted fields stay unchanged. The request body is capped at 1048576 bytes and a larger body is refused with 413. A non-empty body must declare `Content-Type: application/json` or it is refused with 415. The API key selects the caller, wor…
- [Stream a chat completion with an intern](https://openrouter.ai/docs/api/api-reference/interns/stream-a-chat-completion-with-an-intern.md): Sends a prompt to one of your interns and streams the reply as OpenAI-compatible server-sent events ending with `[DONE]`. The run executes on the intern, which may pause to ask you something. It then streams one `openrouter.provide_input` tool call and finishes with `finish_reason: "tool_calls"`, an…
- [Get an intern's daemon access](https://openrouter.ai/docs/api/api-reference/interns/get-an-interns-daemon-access.md): Returns the origin and daemon token that attach `ori tui --host` to one visible, running intern. The token is a credential: the response is sent with `Cache-Control: no-store`, and each reveal is logged by caller and intern. The API key selects the caller, workspace and visible interns. An intern's…
- [Get an intern's daemon access (deprecated alias)](https://openrouter.ai/docs/api/api-reference/interns/get-an-interns-daemon-access-deprecated-alias.md): Deprecated alias of `GET /interns/{internId}/daemon` with the same request, response, and errors. The API key selects the caller, workspace and visible interns. An intern's own API key sees only that intern: the collection and every other intern answer 404 to it. There is no default workspace fallba…
- [Sign a daemon request with the caller's identity (deprecated alias)](https://openrouter.ai/docs/api/api-reference/interns/sign-a-daemon-request-with-the-callers-identity-deprecated-alias.md): Deprecated alias of `POST /interns/{internId}/daemon/sign` with the same request, response, and errors. The API key selects the caller, workspace and visible interns. An intern's own API key sees only that intern: the collection and every other intern answer 404 to it. There is no default workspace…
- [Sign a daemon request with the caller's identity](https://openrouter.ai/docs/api/api-reference/interns/sign-a-daemon-request-with-the-callers-identity.md): Signs the SHA-256 digest of one request the CLI is about to send to the intern daemon, binding it to the intern and to the signed-in member so personal connections resolve. Only an OAuth session from `ori login --oidc` whose grant carries `vault:read` can sign: an API key is refused with 403 because…
- [Start an intern run without waiting for it](https://openrouter.ai/docs/api/api-reference/interns/start-an-intern-run-without-waiting-for-it.md): Starts a run on one of your interns and answers `202` with the `session_id` as soon as the intern accepts it. The run keeps going on the intern after the response. Nothing about its progress comes back on this request; the intern reports through its own tools, such as Slack.
- [Provision an intern](https://openrouter.ai/docs/api/api-reference/interns/provision-an-intern.md): Starts the first boot, or resumes an intern after suspension. This operation takes no request body. A body carrying any field is refused with 400 rather than ignored. The API key selects the caller, workspace and visible interns. An intern's own API key sees only that intern: the collection and ever…
- [Suspend an intern](https://openrouter.ai/docs/api/api-reference/interns/suspend-an-intern.md): Stops the intern runtime while keeping its disk and configuration for a later provision call. This operation takes no request body. A body carrying any field is refused with 400 rather than ignored. The API key selects the caller, workspace and visible interns. An intern's own API key sees only that…

#### API Keys

- [Get current API key](https://openrouter.ai/docs/api/api-reference/api-keys/get-current-api-key.md): Get information on the API key associated with the current authentication session
- [List API keys](https://openrouter.ai/docs/api/api-reference/api-keys/list-api-keys.md): List all API keys for the authenticated user. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Create a new API key](https://openrouter.ai/docs/api/api-reference/api-keys/create-a-new-api-key.md): Create a new API key for the authenticated user. The plaintext `key` is returned only in this response. Treat it as a write-only, sensitive value; it cannot be retrieved later. Authenticate with a [management key](/docs/guides/overview/auth/management-api-keys). The optional `external` object associ…
- [Get a single API key](https://openrouter.ai/docs/api/api-reference/api-keys/get-a-single-api-key.md): Get a single API key by hash. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Delete an API key](https://openrouter.ai/docs/api/api-reference/api-keys/delete-an-api-key.md): Delete an existing API key. Authenticate with a [management key](/docs/guides/overview/auth/management-api-keys).
- [Update an API key](https://openrouter.ai/docs/api/api-reference/api-keys/update-an-api-key.md): Update an existing API key. Authenticate with a [management key](/docs/guides/overview/auth/management-api-keys).

#### Anthropic Messages

- [Create a message](https://openrouter.ai/docs/api/api-reference/anthropic-messages/create-a-message.md): Creates a message using the Anthropic Messages API format. Supports text, images, PDFs, tools, and extended thinking.

#### Models

- [Get a model by its slug](https://openrouter.ai/docs/api/api-reference/models/get-a-model-by-its-slug.md): Returns full details for a single model identified by its author and slug (e.g. openai/gpt-4). Supports variant suffixes (e.g. openai/gpt-4:free) and resolves known slug aliases.
- [List all models and their properties](https://openrouter.ai/docs/api/api-reference/models/list-all-models-and-their-properties.md)
- [Get total count of available models](https://openrouter.ai/docs/api/api-reference/models/get-total-count-of-available-models.md)
- [List models filtered by user provider preferences, privacy settings, and guardrails](https://openrouter.ai/docs/api/api-reference/models/list-models-filtered-by-user-provider-preferences-privacy-settings-and-guardrails.md): List models filtered by user provider preferences, [privacy settings](https://openrouter.ai/docs/guides/privacy/provider-logging), and [guardrails](https://openrouter.ai/docs/guides/features/guardrails). Returns text-output models by default; pass `output_modalities` (a comma-separated list of `text…

#### Observability

- [List observability destinations](https://openrouter.ai/docs/api/api-reference/observability/list-observability-destinations.md): List the observability destinations configured for the authenticated entity's default workspace. Use the `workspace_id` query parameter to scope the result to a different workspace. Only destinations with stable release status are surfaced — destinations of other types are excluded. [Management key]…
- [Create an observability destination](https://openrouter.ai/docs/api/api-reference/observability/create-an-observability-destination.md): Create a new observability destination. A maximum of 5 destinations per type is allowed. Defaults to the authenticated entity's default workspace; use the `workspace_id` body field to scope to a different workspace. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Get an observability destination](https://openrouter.ai/docs/api/api-reference/observability/get-an-observability-destination.md): Fetch a single observability destination by its UUID. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Delete an observability destination](https://openrouter.ai/docs/api/api-reference/observability/delete-an-observability-destination.md): Delete an existing observability destination. This performs a soft delete. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Update an observability destination](https://openrouter.ai/docs/api/api-reference/observability/update-an-observability-destination.md): Update an existing observability destination. Only the fields provided in the request body are updated. [Management key](/docs/guides/overview/auth/management-api-keys) required.

#### Organization

- [List organization members](https://openrouter.ai/docs/api/api-reference/organization/list-organization-members.md): List all members of the organization associated with the authenticated management key. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Get organization settings](https://openrouter.ai/docs/api/api-reference/organization/get-organization-settings.md): Get the settings of the organization associated with the authenticated management key. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Update organization settings](https://openrouter.ai/docs/api/api-reference/organization/update-organization-settings.md): Update the settings of the organization associated with the authenticated management key. [Management key](/docs/guides/overview/auth/management-api-keys) required.

#### Presets

- [List presets](https://openrouter.ai/docs/api/api-reference/presets/list-presets.md): Lists all presets for the authenticated user, ordered by most recently updated first.
- [Get a preset](https://openrouter.ai/docs/api/api-reference/presets/get-a-preset.md): Retrieves a preset by its slug with its currently designated version inline.
- [Create a preset from a chat-completions request body](https://openrouter.ai/docs/api/api-reference/presets/create-a-preset-from-a-chat-completions-request-body.md): Creates a preset (or a new version of an existing one) from an inference request body. Only fields that overlap with the preset config are persisted; other fields (e.g. `messages`, `stream`, `prompt`) are silently ignored.
- [Create a preset from a messages request body](https://openrouter.ai/docs/api/api-reference/presets/create-a-preset-from-a-messages-request-body.md): Creates a preset (or a new version of an existing one) from an inference request body. Only fields that overlap with the preset config are persisted; other fields (e.g. `messages`, `stream`, `prompt`) are silently ignored.
- [Create a preset from a responses request body](https://openrouter.ai/docs/api/api-reference/presets/create-a-preset-from-a-responses-request-body.md): Creates a preset (or a new version of an existing one) from an inference request body. Only fields that overlap with the preset config are persisted; other fields (e.g. `messages`, `stream`, `prompt`) are silently ignored.
- [List versions of a preset](https://openrouter.ai/docs/api/api-reference/presets/list-versions-of-a-preset.md): Lists all versions of a preset, ordered by version number ascending (oldest first).
- [Get a specific version of a preset](https://openrouter.ai/docs/api/api-reference/presets/get-a-specific-version-of-a-preset.md): Retrieves a specific version of a preset by its slug and version number.

#### Private Endpoints

- [List private endpoints](https://openrouter.ai/docs/api/api-reference/private-endpoints/list-private-endpoints.md): List the organization's private endpoints, including drafts. Requires the private endpoints entitlement. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Create a private endpoint](https://openrouter.ai/docs/api/api-reference/private-endpoints/create-a-private-endpoint.md): Create a private endpoint as a draft. Drafts are not routable: validate one with `POST /private-endpoints/{id}/validate`, then activate it with `POST /private-endpoints/{id}/activate`. Pass `activate` to do all three in one call; if validation fails the draft is kept and returned with the failed che…
- [Get a private endpoint](https://openrouter.ai/docs/api/api-reference/private-endpoints/get-a-private-endpoint.md): Get one private endpoint with its upstream configuration and current pricing. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Delete a private endpoint](https://openrouter.ai/docs/api/api-reference/private-endpoints/delete-a-private-endpoint.md): Delete a private endpoint and stop routing to it. Pass `draft_only=true` to refuse (409) when the endpoint has been activated. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Update a draft private endpoint](https://openrouter.ai/docs/api/api-reference/private-endpoints/update-a-draft-private-endpoint.md): Replace a draft endpoint's upstream configuration: send `upstream_model_id`, and `base_url` to change it (an omitted `base_url` keeps the stored one). Omitted data-policy declarations are kept while the upstream is unchanged and cleared when it changes. Any change clears earlier validation. Active e…
- [Activate a validated private endpoint](https://openrouter.ai/docs/api/api-reference/private-endpoints/activate-a-validated-private-endpoint.md): Make a validated draft routable. Returns 409 when the endpoint was never validated, the validation is stale, or it is already active. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Disable a private endpoint](https://openrouter.ai/docs/api/api-reference/private-endpoints/disable-a-private-endpoint.md): Stop routing to an active endpoint without deleting it. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Enable a private endpoint](https://openrouter.ai/docs/api/api-reference/private-endpoints/enable-a-private-endpoint.md): Resume routing to a disabled endpoint. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Set private endpoint pricing](https://openrouter.ai/docs/api/api-reference/private-endpoints/set-private-endpoint-pricing.md): Set the negotiated per-token rates reported for requests routed to this endpoint. Applies to drafts and active endpoints; new rates take effect for subsequent requests. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Validate a draft private endpoint](https://openrouter.ai/docs/api/api-reference/private-endpoints/validate-a-draft-private-endpoint.md): Send a live test request to the draft endpoint using the given workspace's BYOK credential for its provider. A passing validation is required before activation. Failed checks return 200 with `passed: false`. [Management key](/docs/guides/overview/auth/management-api-keys) required.

#### Providers

- [List all providers](https://openrouter.ai/docs/api/api-reference/providers/list-all-providers.md)

#### Rerank

- [Submit a rerank request](https://openrouter.ai/docs/api/api-reference/rerank/submit-a-rerank-request.md): Submits a rerank request to the rerank router

#### Responses

- [Create a response](https://openrouter.ai/docs/api/api-reference/responses/create-a-response.md): Creates a streaming or non-streaming response using OpenResponses API format

#### SCIM

- [List SCIM group mappings](https://openrouter.ai/docs/api/api-reference/scim/list-scim-group-mappings.md): List SCIM group-to-workspace mappings for the organization. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Create a SCIM group mapping](https://openrouter.ai/docs/api/api-reference/scim/create-a-scim-group-mapping.md): Create a SCIM group-to-workspace role mapping. Creating a mapping that already exists with the same role succeeds and re-applies the mapping to the group members. Requesting a different role for an existing mapping returns 409. [Management key](/docs/guides/overview/auth/management-api-keys) require…
- [Get a SCIM group mapping](https://openrouter.ai/docs/api/api-reference/scim/get-a-scim-group-mapping.md): Get a SCIM group-to-workspace mapping. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Delete a SCIM group mapping](https://openrouter.ai/docs/api/api-reference/scim/delete-a-scim-group-mapping.md): Delete a SCIM group-to-workspace mapping. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Update a SCIM group mapping](https://openrouter.ai/docs/api/api-reference/scim/update-a-scim-group-mapping.md): Update a SCIM group mapping role. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [List SCIM groups](https://openrouter.ai/docs/api/api-reference/scim/list-scim-groups.md): List SCIM groups for the organization. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Start a SCIM directory sync](https://openrouter.ai/docs/api/api-reference/scim/start-a-scim-directory-sync.md): Start a SCIM directory sync. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Get SCIM directory sync status](https://openrouter.ai/docs/api/api-reference/scim/get-scim-directory-sync-status.md): Get SCIM directory sync status. [Management key](/docs/guides/overview/auth/management-api-keys) required.

#### SystemOne

- [Submit a System One request](https://openrouter.ai/docs/api/api-reference/systemone/submit-a-system-one-request.md): Sends state and typed questions to a System One model such as Jev and returns its answers. Compatible with the TypeSafe SDKs. Bare System One model IDs such as `jev-1.13` and `jev-latest` are mapped onto the `typesafe/` namespace.

#### Tools

- [List server tools](https://openrouter.ai/docs/api/api-reference/tools/list-server-tools.md): Lists every server tool OpenRouter can run on behalf of a model: accepted `tools[].type` spellings per API format, the engines behind it with their pricing, and how many endpoints run it natively.
- [Get a server tool](https://openrouter.ai/docs/api/api-reference/tools/get-a-server-tool.md): One server tool by canonical name or any accepted alias, with the models that run it natively.

#### Vault

- [List the secrets an intern receives](https://openrouter.ai/docs/api/api-reference/vault/list-the-secrets-an-intern-receives.md): Lists, one entry per name, the secret the intern's outbound requests receive: its own secrets, secrets from an attached vault, and workspace secrets, including ones stored before workspace-scoped storage. Where several vaults hold a name, the entry is the one that wins, in the order intern, attached…
- [List intern secrets](https://openrouter.ai/docs/api/api-reference/vault/list-intern-secrets.md): Lists secret metadata stored for one intern. The list includes secrets stored from the dashboard or at provisioning before workspace-scoped storage; where both exist under one name, the one stored through this API is listed. Those older secrets cannot be deleted or copied through this API, and stori…
- [Store an intern secret](https://openrouter.ai/docs/api/api-reference/vault/store-an-intern-secret.md): Creates or replaces a secret stored for one intern. The value is encrypted at rest and released only to the exact hostnames in `hosts`. The response carries metadata only. Writes return 503 while vault writes are disabled for the caller. The scope is selected by the API key: workspace routes act on…
- [Delete an intern secret](https://openrouter.ai/docs/api/api-reference/vault/delete-an-intern-secret.md): Deletes a secret stored for one intern. Returns 204 with no body on success and 404 when the secret does not exist in the selected scope. Writes return 503 while vault writes are disabled for the caller. The scope is selected by the API key: workspace routes act on the key's active workspace and int…
- [Copy workspace secrets to an intern](https://openrouter.ai/docs/api/api-reference/vault/copy-workspace-secrets-to-an-intern.md): Copies the named workspace secrets into one intern's scope, replacing any intern secret with the same name. Each copy keeps the source value and host bindings. Every name must exist in the workspace scope or the request fails with 404 and nothing is copied. A workspace secret whose `hosts` is `null`…
- [List workspace secrets](https://openrouter.ai/docs/api/api-reference/vault/list-workspace-secrets.md): Lists secret metadata for the workspace of the authenticated API key. The list includes secrets stored from the dashboard or at provisioning before workspace-scoped storage; where both exist under one name, the one stored through this API is listed. Those older secrets cannot be deleted or copied th…
- [Store a workspace secret](https://openrouter.ai/docs/api/api-reference/vault/store-a-workspace-secret.md): Creates or replaces a secret in the workspace of the authenticated API key. The value is encrypted at rest and released only to the exact hostnames in `hosts`. The response carries metadata only. Writes return 503 while vault writes are disabled for the caller. The scope is selected by the API key:…
- [Delete a workspace secret](https://openrouter.ai/docs/api/api-reference/vault/delete-a-workspace-secret.md): Deletes a secret from the workspace of the authenticated API key. Returns 204 with no body on success and 404 when the secret does not exist in the selected scope. Writes return 503 while vault writes are disabled for the caller. The scope is selected by the API key: workspace routes act on the key'…

#### Video Generation

- [Submit a video generation request](https://openrouter.ai/docs/api/api-reference/video-generation/submit-a-video-generation-request.md): Submits a video generation request and returns a polling URL to check status
- [Poll video generation status](https://openrouter.ai/docs/api/api-reference/video-generation/poll-video-generation-status.md): Returns job status and content URLs when completed
- [Download generated video content](https://openrouter.ai/docs/api/api-reference/video-generation/download-generated-video-content.md): Streams the generated video content from the upstream provider
- [List all video generation models](https://openrouter.ai/docs/api/api-reference/video-generation/list-all-video-generation-models.md): Returns a list of all available video generation models and their properties

#### Workspaces

- [List workspaces](https://openrouter.ai/docs/api/api-reference/workspaces/list-workspaces.md): List all workspaces for the authenticated user. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Create a workspace](https://openrouter.ai/docs/api/api-reference/workspaces/create-a-workspace.md): Create a new workspace for the authenticated user. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Get a workspace](https://openrouter.ai/docs/api/api-reference/workspaces/get-a-workspace.md): Get a single workspace by ID or slug. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Delete a workspace](https://openrouter.ai/docs/api/api-reference/workspaces/delete-a-workspace.md): Delete an existing workspace. Workspaces with active API keys cannot be deleted; remove the keys first. Deleting the default workspace requires confirm_default_workspace_deletion=true. Deleting any workspace permanently deletes its budgets and guardrails and disables its classifiers and broadcast de…
- [Update a workspace](https://openrouter.ai/docs/api/api-reference/workspaces/update-a-workspace.md): Update an existing workspace by ID or slug. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [List workspace members](https://openrouter.ai/docs/api/api-reference/workspaces/list-workspace-members.md): List all members of a workspace. Returns paginated results. For the default workspace, returns all organization members (implicit membership). [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Bulk add members to a workspace](https://openrouter.ai/docs/api/api-reference/workspaces/bulk-add-members-to-a-workspace.md): Add multiple organization members to a workspace. Members are assigned the same role they hold in the organization. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Bulk remove members from a workspace](https://openrouter.ai/docs/api/api-reference/workspaces/bulk-remove-members-from-a-workspace.md): Remove multiple members from a workspace. Members with active API keys in the workspace cannot be removed. SCIM-managed members cannot be removed; changes must be made in your identity provider. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [List workspace budgets](https://openrouter.ai/docs/api/api-reference/workspaces/list-workspace-budgets.md): List all budgets configured for a workspace. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Get a workspace budget](https://openrouter.ai/docs/api/api-reference/workspaces/get-a-workspace-budget.md): Retrieve the budget for a given interval. [Management key](/docs/guides/overview/auth/management-api-keys) required.
- [Create or update a workspace budget](https://openrouter.ai/docs/api/api-reference/workspaces/create-or-update-a-workspace-budget.md): Create or update the budget for a given interval. Budget limits must strictly decrease as the interval narrows (lifetime > monthly > weekly > daily). The optional `include_byok_in_budgets` flag is a workspace-wide setting: when provided it applies to every budget interval for the workspace, not just…
- [Delete a workspace budget](https://openrouter.ai/docs/api/api-reference/workspaces/delete-a-workspace-budget.md): Remove the budget for a given interval. [Management key](/docs/guides/overview/auth/management-api-keys) required.

## OpenAPI Specs

- [openapi](/docs/openapi/openapi.yaml)

