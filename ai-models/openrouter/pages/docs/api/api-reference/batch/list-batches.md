---
title: "List batches"
source: https://openrouter.ai/docs/api/api-reference/batch/list-batches.md
path: docs/api/api-reference/batch/list-batches
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List batches

> Lists batches in the workspace of the authenticating API key, newest first. To fetch the next page, pass the previous page's `last_id` as `after`. List items omit `results`. Use `GET /batches/{id}` to get them. See the [Batch API Quickstart](https://openrouter.ai/docs/batch-quickstart).



## OpenAPI

````yaml /openapi/openapi.yaml get /batches
openapi: 3.1.0
info:
  contact:
    email: support@openrouter.ai
    name: OpenRouter Support
    url: https://openrouter.ai/docs
  description: OpenAI-compatible API with additional OpenRouter features
  license:
    name: MIT
    url: https://opensource.org/licenses/MIT
  title: OpenRouter API
  version: 1.0.0
servers:
  - description: Production server
    url: https://openrouter.ai/api/v1
    x-speakeasy-server-id: production
security:
  - apiKey: []
tags:
  - description: API key management endpoints
    name: API Keys
  - description: Analytics and usage endpoints
    name: Analytics
  - description: Anthropic Messages endpoints
    name: Anthropic Messages
  - description: BYOK endpoints
    name: BYOK
  - description: >-
      Submit, list, poll, and delete asynchronous batches of inference requests.
      See https://openrouter.ai/docs/batch-quickstart.
    name: Batch
  - description: Benchmarks endpoints
    name: Benchmarks
  - description: Chat completion endpoints
    name: Chat
  - description: Task classification market-share endpoints
    name: Classifications
  - description: Containers endpoints
    name: Containers
  - description: Credit management endpoints
    name: Credits
  - description: >-
      Public OpenRouter usage datasets. Data returned by these endpoints is
      licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/):
      reuse and republish it, including commercially, with attribution to
      OpenRouter.
    name: Datasets
  - description: Text embedding endpoints
    name: Embeddings
  - description: Endpoint information
    name: Endpoints
  - description: Files endpoints
    name: Files
  - description: Generation history endpoints
    name: Generations
  - description: Guardrails endpoints
    name: Guardrails
  - description: Images endpoints
    name: Images
  - description: >-
      Create, inspect, update, provision, suspend and delete OpenRouter interns
      through an API key, and talk to them: the chat route streams
      OpenAI-compatible completions from one intern, pausing as an
      `openrouter.provide_input` tool call when the intern needs your permission
      or an answer. Available to interns programme members; other callers
      receive 404. See https://openrouter.ai/docs/guides/ori/intern-chat.
    name: Interns
  - description: Model information endpoints
    name: Models
  - description: OAuth authentication endpoints
    name: OAuth
  - description: Observability endpoints
    name: Observability
  - description: Organization endpoints
    name: Organization
  - description: Presets endpoints
    name: Presets
  - description: Provider information endpoints
    name: Providers
  - description: Rerank endpoints
    name: Rerank
  - description: OpenAI-compatible Responses API endpoints
    name: Responses
  - description: >-
      Management endpoints for SCIM group-to-workspace mappings, authenticated
      with a management key. These are not the SCIM 2.0 connector endpoints for
      your identity provider. In your identity provider, enter the SCIM endpoint
      URL shown when you enable provisioning under Settings > Members > SCIM
      Mappings. See
      https://openrouter.ai/docs/guides/features/scim-mappings#set-up-provisioning.
    name: SCIM
  - description: Speech-to-text endpoints
    name: STT
    x-displayName: Transcriptions
  - description: >-
      System One endpoints for models such as Jev, compatible with the TypeSafe
      SDKs. See https://openrouter.ai/docs/guides/community/typesafe-sdk.
    name: SystemOne
    x-displayName: System One
  - description: Text-to-speech endpoints
    name: TTS
    x-displayName: Speech
  - description: >-
      Store host-bound secrets for a workspace or for one intern. Scope is
      selected by the API key. Responses return metadata only, never secret
      values. See https://openrouter.ai/docs/guides/ori/vault.
    name: Vault
  - description: Video Generation endpoints
    name: Video Generation
  - description: Workspaces endpoints
    name: Workspaces
  - description: Alpha feature endpoints for Decisions requests
    name: alpha.decisions
externalDocs:
  description: OpenRouter Documentation
  url: https://openrouter.ai/docs
paths:
  /batches:
    get:
      tags:
        - Batch
      summary: List batches
      description: >-
        Lists batches in the workspace of the authenticating API key, newest
        first. To fetch the next page, pass the previous page's `last_id` as
        `after`. List items omit `results`. Use `GET /batches/{id}` to get them.
        See the [Batch API
        Quickstart](https://openrouter.ai/docs/batch-quickstart).
      operationId: listBatches
      parameters:
        - description: Maximum number of batches to return, from 1 through 100.
          in: query
          name: limit
          required: false
          schema:
            description: Maximum number of batches to return, from 1 through 100.
            example: 20
            type: integer
        - description: Batch id from the previous page's `last_id`.
          in: query
          name: after
          required: false
          schema:
            description: Batch id from the previous page's `last_id`.
            example: batch_7a4b02
            minLength: 1
            type: string
        - description: Repeat this parameter to include more than one status.
          explode: true
          in: query
          name: status
          required: false
          schema:
            description: Repeat this parameter to include more than one status.
            example:
              - completed
              - failed
            items:
              $ref: '#/components/schemas/BatchListStatus'
            type: array
          style: form
        - description: Only include batches created strictly after this timestamp.
          in: query
          name: created_after
          required: false
          schema:
            $ref: '#/components/schemas/BatchListTimestamp'
        - description: Only include batches created strictly before this timestamp.
          in: query
          name: created_before
          required: false
          schema:
            allOf:
              - $ref: '#/components/schemas/BatchListTimestamp'
              - description: Only include batches created strictly before this timestamp.
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchListResponse'
          description: A newest-first page of batches.
        '400':
          content:
            application/json:
              example:
                error:
                  code: 400
                  message: Invalid batch list query.
              schema:
                $ref: '#/components/schemas/BatchErrorResponse'
          description: Malformed or unsupported batch list query parameters.
        '401':
          content:
            application/json:
              example:
                error:
                  code: 401
                  message: No auth credentials found.
              schema:
                $ref: '#/components/schemas/BatchErrorResponse'
          description: Missing or invalid API key.
        '429':
          content:
            application/json:
              example:
                error:
                  code: 429
                  message: Rate limit exceeded.
              schema:
                $ref: '#/components/schemas/BatchErrorResponse'
          description: Batch API rate limit exceeded for the billable entity.
        '500':
          content:
            application/json:
              example:
                error:
                  code: 500
                  message: Internal server error.
              schema:
                $ref: '#/components/schemas/BatchErrorResponse'
          description: Unexpected error in the ingress or upstream batch-api.
        '502':
          content:
            application/json:
              example:
                error:
                  code: 502
                  message: Upstream batch-api is unavailable.
              schema:
                $ref: '#/components/schemas/BatchErrorResponse'
          description: >-
            The batch service is unavailable, or an upstream provider operation
            failed, including batch or file cleanup.
components:
  schemas:
    BatchListStatus:
      description: >-
        A batch status that is durably represented by the list data source.
        `finalizing` and `cancelling` are not accepted because stored jobs
        collapse those phases into `in_progress`.
      enum:
        - validating
        - in_progress
        - completed
        - failed
        - expired
        - cancelled
      example: completed
      type: string
    BatchListTimestamp:
      anyOf:
        - pattern: ^\d+$
          type: string
        - anyOf:
            - format: date
              type: string
            - format: date-time
              type: string
      description: Only include batches created strictly after this timestamp.
      example: '2026-08-20T00:00:00Z'
    BatchListResponse:
      description: A newest-first page of metadata-only batch objects.
      example:
        data: []
        first_id: null
        has_more: false
        last_id: null
        object: list
      properties:
        data:
          items:
            $ref: '#/components/schemas/BatchListItem'
          type: array
        first_id:
          type:
            - string
            - 'null'
        has_more:
          type: boolean
        last_id:
          type:
            - string
            - 'null'
        object:
          enum:
            - list
          type: string
      required:
        - object
        - data
        - first_id
        - last_id
        - has_more
      type: object
    BatchErrorResponse:
      example:
        error:
          code: 400
          message: custom_id is required on requests[0].
      properties:
        error:
          properties:
            code:
              type: integer
            message:
              type: string
          required:
            - code
            - message
          type: object
      required:
        - error
      type: object
    BatchListItem:
      description: >-
        Metadata-only batch object. `results` is always `null` in list
        responses.
      properties:
        completion_window:
          enum:
            - 24h
          type: string
        created_at:
          type: integer
        endpoint:
          type: string
        error:
          properties:
            message:
              type: string
          required:
            - message
          type:
            - object
            - 'null'
        finalized_at:
          type:
            - integer
            - 'null'
        id:
          type: string
        model:
          type: string
        object:
          enum:
            - batch
          type: string
        request_counts:
          properties:
            completed:
              type: integer
            failed:
              type: integer
            total:
              type: integer
          required:
            - total
            - completed
            - failed
          type: object
        results:
          description: >-
            Always null: retrieve the batch with `GET /batches/{id}` to access
            its results.
          type: 'null'
        status:
          enum:
            - validating
            - in_progress
            - finalizing
            - completed
            - failed
            - expired
            - cancelling
            - cancelled
          type: string
        usage:
          properties:
            cache_creation:
              $ref: '#/components/schemas/AnthropicCacheCreation'
            completion_tokens:
              description: The tokens generated
              type: integer
            completion_tokens_details:
              properties:
                audio_tokens:
                  description: Tokens generated by the model for audio output.
                  type:
                    - integer
                    - 'null'
                image_tokens:
                  description: Tokens generated by the model for image output.
                  type:
                    - integer
                    - 'null'
                reasoning_tokens:
                  description: Tokens generated by the model for reasoning.
                  type:
                    - integer
                    - 'null'
              type:
                - object
                - 'null'
            cost:
              description: Cost of the completion
              format: double
              type:
                - number
                - 'null'
            cost_details:
              $ref: '#/components/schemas/CostDetails'
            is_byok:
              description: >-
                Whether a request was made using a Bring Your Own Key
                configuration
              type: boolean
            iterations:
              items:
                $ref: '#/components/schemas/AnthropicUsageIteration'
              type:
                - array
                - 'null'
            prompt_tokens:
              description: Including images, input audio, and tools if any
              type: integer
            prompt_tokens_details:
              description: Breakdown of tokens used in the prompt.
              properties:
                audio_tokens:
                  description: Tokens used for input audio.
                  type:
                    - integer
                    - 'null'
                cache_write_tokens:
                  description: >-
                    Tokens written to cache. Only returned for models with
                    explicit caching and cache write pricing.
                  type:
                    - integer
                    - 'null'
                cached_tokens:
                  description: Tokens cached by the endpoint.
                  type:
                    - integer
                    - 'null'
                file_tokens:
                  description: Tokens used for input files/documents.
                  type:
                    - integer
                    - 'null'
                video_tokens:
                  description: Tokens used for input video.
                  type:
                    - integer
                    - 'null'
              type:
                - object
                - 'null'
            server_tool_use:
              description: Usage for server-side tool execution (e.g., web search)
              properties:
                tool_calls_executed:
                  description: >-
                    Number of OpenRouter server tool calls that executed and
                    produced a result.
                  type:
                    - integer
                    - 'null'
                tool_calls_requested:
                  description: >-
                    Total number of OpenRouter server-orchestrated tool calls
                    the model requested, across all tool types. Provider-native
                    tools (e.g. native web search) are not counted here.
                  type:
                    - integer
                    - 'null'
                web_search_requests:
                  description: >-
                    Number of web searches performed by server-side tools. For
                    server-orchestrated tool calls a web search is also counted
                    in tool_calls_requested; provider-native web search may
                    report web_search_requests only. Do not sum the two.
                  type:
                    - integer
                    - 'null'
              type:
                - object
                - 'null'
            service_tier:
              description: The service tier used by the upstream provider for this request
              type:
                - string
                - 'null'
            speed:
              $ref: '#/components/schemas/AnthropicSpeed'
            total_tokens:
              description: Sum of the above two fields
              type: integer
          required:
            - prompt_tokens
            - completion_tokens
            - total_tokens
          type:
            - object
            - 'null'
      required:
        - id
        - object
        - endpoint
        - model
        - completion_window
        - status
        - created_at
        - finalized_at
        - request_counts
        - usage
        - error
        - results
      type: object
    AnthropicCacheCreation:
      example:
        ephemeral_1h_input_tokens: 0
        ephemeral_5m_input_tokens: 100
      properties:
        ephemeral_1h_input_tokens:
          type: integer
        ephemeral_5m_input_tokens:
          type: integer
      required:
        - ephemeral_5m_input_tokens
        - ephemeral_1h_input_tokens
      type:
        - object
        - 'null'
    CostDetails:
      description: Breakdown of upstream inference costs
      example:
        upstream_inference_completions_cost: 0.0004
        upstream_inference_cost: null
        upstream_inference_prompt_cost: 0.0008
      properties:
        server_tool_cost:
          description: >-
            Metered server-tool execution cost (for example, shell sandbox time)
            billed for this request, in USD. Matches the billed checkpoint and
            settlement amounts exactly. 0 when a metered server tool ran but
            settled at zero dollars; absent when no metered server tool ran.
          format: double
          type:
            - number
            - 'null'
        upstream_inference_completions_cost:
          format: double
          type: number
        upstream_inference_cost:
          format: double
          type:
            - number
            - 'null'
        upstream_inference_prompt_cost:
          format: double
          type: number
      required:
        - upstream_inference_prompt_cost
        - upstream_inference_completions_cost
      type:
        - object
        - 'null'
    AnthropicUsageIteration:
      anyOf:
        - $ref: '#/components/schemas/AnthropicCompactionUsageIteration'
        - $ref: '#/components/schemas/AnthropicMessageUsageIteration'
        - $ref: '#/components/schemas/AnthropicAdvisorMessageUsageIteration'
        - $ref: '#/components/schemas/AnthropicUnknownUsageIteration'
      example:
        cache_creation: null
        cache_creation_input_tokens: 0
        cache_read_input_tokens: 0
        input_tokens: 100
        output_tokens: 50
        type: message
    AnthropicSpeed:
      enum:
        - fast
        - standard
        - null
      example: standard
      type:
        - string
        - 'null'
    AnthropicCompactionUsageIteration:
      allOf:
        - $ref: '#/components/schemas/AnthropicBaseUsageIteration'
        - properties:
            type:
              enum:
                - compaction
              type: string
          required:
            - type
          type: object
      example:
        cache_creation: null
        cache_creation_input_tokens: 0
        cache_read_input_tokens: 0
        input_tokens: 50
        output_tokens: 25
        type: compaction
    AnthropicMessageUsageIteration:
      allOf:
        - $ref: '#/components/schemas/AnthropicBaseUsageIteration'
        - properties:
            model:
              type: string
            type:
              enum:
                - message
              type: string
          required:
            - type
          type: object
      example:
        cache_creation: null
        cache_creation_input_tokens: 0
        cache_read_input_tokens: 0
        input_tokens: 100
        output_tokens: 50
        type: message
    AnthropicAdvisorMessageUsageIteration:
      allOf:
        - $ref: '#/components/schemas/AnthropicBaseUsageIteration'
        - properties:
            model:
              type: string
            type:
              enum:
                - advisor_message
              type: string
          required:
            - type
            - model
          type: object
      example:
        cache_creation: null
        cache_creation_input_tokens: 0
        cache_read_input_tokens: 0
        input_tokens: 823
        model: claude-opus-4-6
        output_tokens: 1612
        type: advisor_message
    AnthropicUnknownUsageIteration:
      allOf:
        - $ref: '#/components/schemas/AnthropicBaseUsageIteration'
        - properties:
            type:
              type: string
          required:
            - type
          type: object
      example:
        cache_creation: null
        cache_creation_input_tokens: 0
        cache_read_input_tokens: 0
        input_tokens: 100
        output_tokens: 50
        type: unknown
    AnthropicBaseUsageIteration:
      example:
        cache_creation: null
        cache_creation_input_tokens: 0
        cache_read_input_tokens: 0
        input_tokens: 100
        output_tokens: 50
      properties:
        cache_creation:
          $ref: '#/components/schemas/AnthropicIterationCacheCreation'
        cache_creation_input_tokens:
          type: integer
        cache_read_input_tokens:
          type: integer
        input_tokens:
          type: integer
        output_tokens:
          type: integer
      type: object
    AnthropicIterationCacheCreation:
      default: null
      example:
        ephemeral_1h_input_tokens: 0
        ephemeral_5m_input_tokens: 0
      properties:
        ephemeral_1h_input_tokens:
          type: integer
        ephemeral_5m_input_tokens:
          type: integer
      type:
        - object
        - 'null'
  securitySchemes:
    apiKey:
      description: API key as bearer token in Authorization header
      scheme: bearer
      type: http

````
