---
title: "Get an intern's daemon access"
source: https://openrouter.ai/docs/api/api-reference/interns/get-an-interns-daemon-access.md
path: docs/api/api-reference/interns/get-an-interns-daemon-access
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get an intern's daemon access

> Returns the origin and daemon token that attach `ori tui --host` to one visible, running intern. The token is a credential: the response is sent with `Cache-Control: no-store`, each reveal is logged by caller and intern, and a caller may make 10 reveals per minute. The API key selects the caller, workspace and visible interns. There is no default workspace fallback. Requests on regional hostnames such as `eu.openrouter.ai` are refused. [API key](/docs/api-reference/authentication) required.



## OpenAPI

````yaml /openapi/openapi.yaml get /interns/{internId}/daemon-access
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
  /interns/{internId}/daemon-access:
    get:
      tags:
        - Interns
      summary: Get an intern's daemon access
      description: >-
        Returns the origin and daemon token that attach `ori tui --host` to one
        visible, running intern. The token is a credential: the response is sent
        with `Cache-Control: no-store`, each reveal is logged by caller and
        intern, and a caller may make 10 reveals per minute. The API key selects
        the caller, workspace and visible interns. There is no default workspace
        fallback. Requests on regional hostnames such as `eu.openrouter.ai` are
        refused. [API key](/docs/api-reference/authentication) required.
      operationId: getInternDaemonAccess
      parameters:
        - description: ID of an intern visible to the authenticated API key.
          in: path
          name: internId
          required: true
          schema:
            description: ID of an intern visible to the authenticated API key.
            example: 7c9e6679-7425-40de-944b-e07fc1f90ae7
            minLength: 1
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/InternDaemonAccess'
          description: Daemon origin and token.
        '401':
          content:
            application/json:
              example:
                error:
                  code: 401
                  message: Invalid or missing API key
              schema:
                $ref: '#/components/schemas/InternLifecycleError'
          description: Missing, unknown or provisioning API key.
        '403':
          content:
            application/json:
              example:
                error:
                  code: 403
                  message: Forbidden
              schema:
                $ref: '#/components/schemas/InternLifecycleError'
          description: >-
            The key owner no longer has access, or the request used a regional
            hostname.
        '404':
          content:
            application/json:
              example:
                error:
                  code: 404
                  message: Intern not found
                  metadata:
                    reason: not_found
                    retryable: false
              schema:
                $ref: '#/components/schemas/InternLifecycleError'
          description: >-
            The caller is outside the Intern API programme, the intern is
            hidden, or lifecycle writes are disabled.
        '408':
          content:
            application/json:
              example:
                error:
                  code: 408
                  message: Operation timed out after 10s. Please try again later.
                  metadata:
                    reason: timeout
                    retryable: true
              schema:
                $ref: '#/components/schemas/InternLifecycleError'
          description: >-
            The request exceeded its route deadline. The deadline quoted in the
            message is the route's own, so it differs between operations.
        '409':
          content:
            application/json:
              example:
                error:
                  code: 409
                  message: This intern is not running.
                  metadata:
                    reason: intern_not_running
                    retryable: false
              schema:
                $ref: '#/components/schemas/InternLifecycleError'
          description: >-
            The intern cannot be attached to. `metadata.reason` is
            `intern_not_running`, `intern_unreachable` when it has no usable
            address yet, or `intern_needs_restart` when it was provisioned
            before daemon access was available.
        '429':
          content:
            application/json:
              example:
                error:
                  code: 429
                  message: Too many token reveals. Please wait a moment.
                  metadata:
                    reason: rate_limited
                    retryable: true
              schema:
                $ref: '#/components/schemas/InternLifecycleError'
          description: >-
            The caller made more than 10 reveals in the last minute. Wait for
            `Retry-After` seconds.
        '500':
          content:
            application/json:
              example:
                error:
                  code: 500
                  message: The request could not be completed
                  metadata:
                    reason: internal_error
                    retryable: true
              schema:
                $ref: '#/components/schemas/InternLifecycleError'
          description: >-
            The request could not be completed. `metadata.reason` says whether
            to try again: `internal_error` is a transient failure and carries
            `metadata.retryable: true`, so the same request may be sent again,
            while `configuration_error` carries `retryable: false` because the
            next attempt reads the same missing binding or unusable stored
            credential.
      security:
        - apiKey: []
components:
  schemas:
    InternDaemonAccess:
      description: >-
        The intern daemon's origin and the bearer `ori tui --host` sends to it
        as `ORI_DAEMON_TOKEN`.
      example:
        origin: https://research-assistant-7c9e6679.or.bot
        token: daemon_token
      properties:
        origin:
          pattern: >-
            ^https?:\/\/([a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?(?:\.[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)*)(?::(\d{1,5}))?$/iu
          type: string
        token:
          pattern: ^[\w-]+$/u
          type: string
      required:
        - origin
        - token
      type: object
    InternLifecycleError:
      additionalProperties: false
      description: Intern lifecycle request failure.
      example:
        error:
          code: 404
          message: Intern not found
          metadata:
            reason: not_found
            retryable: false
      properties:
        error:
          additionalProperties: false
          properties:
            code:
              anyOf:
                - type: string
                - type: integer
            message:
              type: string
            metadata:
              additionalProperties: false
              properties:
                reason:
                  type: string
                retryable:
                  type: boolean
              required:
                - reason
                - retryable
              type: object
          required:
            - code
            - message
          type: object
      required:
        - error
      type: object
  securitySchemes:
    apiKey:
      description: API key as bearer token in Authorization header
      scheme: bearer
      type: http

````
