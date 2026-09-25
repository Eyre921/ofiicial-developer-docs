---
title: "Delete a batch"
source: https://openrouter.ai/docs/api/api-reference/batch/delete-a-batch.md
path: docs/api/api-reference/batch/delete-a-batch
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a batch

> Deletes a batch in a terminal status (`completed`, `failed`, `expired`, or `cancelled`) and its stored requests and results. Batches still in progress return `409`. Billing and usage records are kept. See the [Batch API Quickstart](https://openrouter.ai/docs/batch-quickstart).



## OpenAPI

````yaml /openapi/openapi.yaml delete /batches/{id}
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
  /batches/{id}:
    delete:
      tags:
        - Batch
      summary: Delete a batch
      description: >-
        Deletes a batch in a terminal status (`completed`, `failed`, `expired`,
        or `cancelled`) and its stored requests and results. Batches still in
        progress return `409`. Billing and usage records are kept. See the
        [Batch API Quickstart](https://openrouter.ai/docs/batch-quickstart).
      operationId: deleteBatch
      parameters:
        - description: The batch job id returned from submit.
          in: path
          name: id
          required: true
          schema:
            description: The batch job id returned from submit.
            example: batch_abc123
            minLength: 1
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchDeletedObject'
          description: >-
            The batch was deleted; per-target outcomes are reported under
            `deletion`.
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
        '404':
          content:
            application/json:
              example:
                error:
                  code: 404
                  message: Batch not found.
              schema:
                $ref: '#/components/schemas/BatchErrorResponse'
          description: No batch exists for the given id.
        '409':
          content:
            application/json:
              example:
                error:
                  code: 409
                  message: >-
                    Only completed, failed, expired, or cancelled batches can be
                    deleted. Wait for the batch to finish and try again.
              schema:
                $ref: '#/components/schemas/BatchErrorResponse'
          description: >-
            The batch is still processing, its required provider key is
            unavailable, or its state changed during deletion.
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
    BatchDeletedObject:
      description: >-
        Confirms a terminal batch was removed from the API and its
        OpenRouter-held artifacts purged. Deletion is not cancellation and does
        not erase billing or audit records.
      example:
        deletion:
          openrouter: deleted
          upstream:
            provider: OpenAI
            status: unsupported
        id: batch_abc123
        object: batch
      properties:
        deletion:
          $ref: '#/components/schemas/BatchDeletionTargets'
        id:
          example: batch_abc123
          type: string
        object:
          enum:
            - batch
          type: string
      required:
        - id
        - object
        - deletion
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
    BatchDeletionTargets:
      additionalProperties: false
      description: >-
        OpenRouter cleanup and, when a provider was assigned, the upstream batch
        deletion outcome.
      example:
        openrouter: deleted
        upstream:
          provider: Anthropic
          status: deleted
      properties:
        openrouter:
          description: OpenRouter-held request and result artifacts were purged.
          enum:
            - deleted
          type: string
        upstream:
          additionalProperties: false
          description: >-
            The upstream batch deletion outcome; omitted when no provider was
            assigned.
          properties:
            provider:
              description: The provider name stored on the batch.
              example: OpenAI
              minLength: 1
              type: string
            status:
              $ref: '#/components/schemas/BatchDeletionOutcome'
          required:
            - provider
            - status
          type: object
      required:
        - openrouter
      type: object
    BatchDeletionOutcome:
      description: >-
        Outcome for one deletion target: `deleted` (removed), `unsupported` (the
        provider has no batch-delete API; supported file cleanup still runs), or
        `not_applicable` (the batch never reached that target).
      enum:
        - deleted
        - unsupported
        - not_applicable
      example: deleted
      type: string
  securitySchemes:
    apiKey:
      description: API key as bearer token in Authorization header
      scheme: bearer
      type: http

````
