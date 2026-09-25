---
title: "Start an intern run without waiting for it"
source: https://openrouter.ai/docs/api/api-reference/interns/start-an-intern-run-without-waiting-for-it.md
path: docs/api/api-reference/interns/start-an-intern-run-without-waiting-for-it
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Start an intern run without waiting for it

> Starts a run on one of your interns and answers `202` with the `session_id` as soon as the intern accepts it. The run keeps going on the intern after the response. Nothing about its progress comes back on this request; the intern reports through its own tools, such as Slack.

Send the same `session_id` later to continue the conversation, for example to hand the intern a decision on work it started. If that session already has a run going, the prompt is delivered into it and the status is `steered`. A `session_id` is accepted only from the caller it was issued to, on the same intern; any other, including sessions started from Slack or the chat endpoint, is refused with `404`.

Runs started here self-drive: the intern consents to its own tool approvals, and a question it asks is answered by its own fallback. A run ends when the intern finishes it or after its execution deadline (1 hour by default).

Available to interns programme members. Callers outside the programme receive `404` for every path under `/api/v1/interns`.



## OpenAPI

````yaml /openapi/openapi.yaml post /interns/{internId}/invoke
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
  /interns/{internId}/invoke:
    post:
      tags:
        - Interns
      summary: Start an intern run without waiting for it
      description: >-
        Starts a run on one of your interns and answers `202` with the
        `session_id` as soon as the intern accepts it. The run keeps going on
        the intern after the response. Nothing about its progress comes back on
        this request; the intern reports through its own tools, such as Slack.


        Send the same `session_id` later to continue the conversation, for
        example to hand the intern a decision on work it started. If that
        session already has a run going, the prompt is delivered into it and the
        status is `steered`. A `session_id` is accepted only from the caller it
        was issued to, on the same intern; any other, including sessions started
        from Slack or the chat endpoint, is refused with `404`.


        Runs started here self-drive: the intern consents to its own tool
        approvals, and a question it asks is answered by its own fallback. A run
        ends when the intern finishes it or after its execution deadline (1 hour
        by default).


        Available to interns programme members. Callers outside the programme
        receive `404` for every path under `/api/v1/interns`.
      operationId: invokeIntern
      parameters:
        - description: The intern to run.
          in: path
          name: internId
          required: true
          schema:
            description: The intern to run.
            example: a11e0000-0000-4000-8000-000000000005
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/InternInvokeRequest'
        required: true
      responses:
        '202':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/InternInvokeAcceptedResponse'
          description: The intern accepted the prompt. The run continues on the intern.
        '400':
          content:
            application/json:
              example:
                error:
                  code: 400
                  message: >-
                    Invalid invoke request (input: Too small: expected string to
                    have >=1 characters).
                  metadata:
                    reason: bad_request
                    retryable: false
              schema:
                $ref: '#/components/schemas/InternChatErrorResponse'
          description: The body is not a valid request (`bad_request`).
        '401':
          content:
            application/json:
              example:
                error:
                  code: 401
                  message: Invalid or missing API key
              schema:
                $ref: '#/components/schemas/InternChatErrorResponse'
          description: No valid API key.
        '403':
          content:
            application/json:
              example:
                error:
                  code: 403
                  message: >-
                    This API key's creator is no longer a member of the
                    organization. Ask an organization admin to reassign the key
                    to an active member.
              schema:
                $ref: '#/components/schemas/InternChatErrorResponse'
          description: >-
            The key belongs to a member who has left the organization and holds
            no grant.
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
                $ref: '#/components/schemas/InternChatErrorResponse'
          description: >-
            The caller is outside the interns programme, the intern does not
            exist for this key, or the `session_id` was not issued to this
            caller on this intern (`not_found`).
        '408':
          content:
            application/json:
              example:
                error:
                  code: 408
                  message: Operation timed out after 60s. Please try again later.
                  metadata:
                    reason: timeout
                    retryable: true
              schema:
                $ref: '#/components/schemas/InternChatErrorResponse'
          description: >-
            The request exceeded the route's own deadline before the handler
            answered (`timeout`).
        '409':
          content:
            application/json:
              example:
                error:
                  code: 409
                  message: This intern is not running.
                  metadata:
                    reason: intern_not_ready
                    retryable: true
              schema:
                $ref: '#/components/schemas/InternChatErrorResponse'
          description: >-
            The intern is not running or its runtime is too old to keep a run
            going without a connection (`intern_not_ready`), or the session
            already has a run that did not take the prompt (`busy`). A `busy`
            refusal carries `Retry-After`.
          headers:
            Retry-After:
              description: >-
                Seconds to wait before retrying this request. Present only on a
                `busy` refusal.
              required: false
              schema:
                description: >-
                  Seconds to wait before retrying this request. Present only on
                  a `busy` refusal.
                example: '5'
                type: string
        '413':
          content:
            application/json:
              example:
                error:
                  code: 413
                  message: Request body exceeds 1048576 bytes
                  metadata:
                    reason: payload_too_large
                    retryable: false
              schema:
                $ref: '#/components/schemas/InternChatErrorResponse'
          description: The body exceeds 1 MiB (`payload_too_large`).
        '429':
          content:
            application/json:
              example:
                error:
                  code: 429
                  message: Too many intern turns. Please wait a moment.
                  metadata:
                    reason: rate_limited
                    retryable: true
              schema:
                $ref: '#/components/schemas/InternChatErrorResponse'
          description: >-
            Too many turns for the user or organization this key acts as
            (`rate_limited`). It carries `Retry-After`.
          headers:
            Retry-After:
              description: Seconds to wait before retrying this request.
              required: true
              schema:
                description: Seconds to wait before retrying this request.
                example: '60'
                type: string
        '500':
          content:
            application/json:
              example:
                error:
                  code: 500
                  message: Could not look up the intern
                  metadata:
                    reason: intern_unreachable
                    retryable: true
              schema:
                $ref: '#/components/schemas/InternChatErrorResponse'
          description: The intern could not be looked up, or authenticating the key failed.
        '502':
          content:
            application/json:
              example:
                error:
                  code: 502
                  message: The intern could not be reached.
                  metadata:
                    reason: intern_unreachable
                    retryable: true
              schema:
                $ref: '#/components/schemas/InternChatErrorResponse'
          description: >-
            The intern could not be reached, rejected the request, or refused
            the turn before it started.
        '503':
          content:
            application/json:
              example:
                error:
                  code: 503
                  message: >-
                    The intern cannot hold another run open across a question
                    right now. Retry later.
                  metadata:
                    reason: busy
                    retryable: true
              schema:
                $ref: '#/components/schemas/InternChatErrorResponse'
          description: >-
            The intern cannot take another run right now (`busy`). It reports
            `retryable: true` and carries `Retry-After`.
          headers:
            Retry-After:
              description: Seconds to wait before retrying this request.
              required: true
              schema:
                description: Seconds to wait before retrying this request.
                example: '5'
                type: string
        '504':
          content:
            application/json:
              example:
                error:
                  code: 504
                  message: The intern did not answer in time.
                  metadata:
                    reason: timeout
                    retryable: true
              schema:
                $ref: '#/components/schemas/InternChatErrorResponse'
          description: The intern did not accept the turn in time (`timeout`).
      security:
        - apiKey: []
components:
  schemas:
    InternInvokeRequest:
      description: A prompt to run on the intern without holding a connection open.
      example:
        input: 'New support ticket 48213. Case token: ct_9f2c. Investigate and reply.'
      properties:
        input:
          description: The prompt for the run, at most 32000 characters.
          example: >-
            New support ticket 48213. Case token: ct_9f2c. Investigate and
            reply.
          maxLength: 32000
          minLength: 1
          type: string
        session_id:
          description: >-
            The session to run in. Send the `session_id` from an earlier `202`
            to continue that conversation, for example to hand the intern a
            decision on a case it is working. Omit it to start a new session.
            Only a `session_id` this endpoint issued to the same caller on the
            same intern is accepted; any other is refused with `404`.
          example: b51a0e21-368b-4780-a220-14655bf28c55
          maxLength: 256
          minLength: 1
          type: string
      required:
        - input
      type: object
    InternInvokeAcceptedResponse:
      description: The intern admitted the prompt. The run continues on the intern.
      example:
        session_id: b51a0e21-368b-4780-a220-14655bf28c55
        status: started
      properties:
        session_id:
          description: >-
            The session the run belongs to. Send it back to continue the
            conversation.
          example: b51a0e21-368b-4780-a220-14655bf28c55
          type: string
        status:
          description: >-
            `started` when a new run began. `steered` when the session already
            had a run going and the prompt was delivered into it instead.
          enum:
            - started
            - steered
          example: started
          type: string
      required:
        - session_id
        - status
      type: object
    InternChatErrorResponse:
      description: >-
        A refusal before the stream opens. Once the response is `200` and
        streaming, failures arrive as a chunk with `finish_reason: "error"`
        instead.
      example:
        error:
          code: 409
          message: That question is no longer waiting for an answer.
          metadata:
            reason: interaction_not_pending
            retryable: false
      properties:
        error:
          $ref: '#/components/schemas/InternChatError'
      required:
        - error
      type: object
    InternChatError:
      description: >-
        The OpenAI-compatible error object. `metadata` is present on refusals
        from the chat route. Authentication refusals (`401`), the
        departed-creator `403` and the programme `404` carry only `code` and
        `message`.
      example:
        code: 409
        message: That question is no longer waiting for an answer.
        metadata:
          reason: interaction_not_pending
          retryable: false
      properties:
        code:
          description: The HTTP status of the response.
          type: integer
        message:
          type: string
        metadata:
          $ref: '#/components/schemas/InternChatErrorMetadata'
      required:
        - code
        - message
      type: object
    InternChatErrorMetadata:
      description: Machine-readable detail for the failure.
      example:
        reason: interaction_not_pending
        retryable: false
      properties:
        reason:
          description: A stable reason a client can branch on.
          enum:
            - attachment_failed
            - bad_request
            - busy
            - client_closed_request
            - interaction_not_pending
            - interaction_unknown
            - intern_not_ready
            - intern_rejected
            - intern_unreachable
            - not_found
            - payload_too_large
            - rate_limited
            - run_ended
            - stream_severed
            - timeout
            - turn_failed
          type: string
        retryable:
          description: >-
            Whether the same request may be sent again unchanged. Always `true`
            for the transient refusals — `busy`, `intern_not_ready`,
            `intern_unreachable`, `rate_limited`, `stream_severed` and `timeout`
            — and always `false` for the ones a retry cannot fix. For
            `turn_failed` it varies by failure and is the intern's own
            classification of what went wrong: `true` for an upstream overload,
            rate limit, timeout or transport fault, `false` for an
            authentication or bad-request failure that would be rejected the
            same way again. Branch on this field rather than on `reason` when
            deciding whether to retry. A `429`, and a `409` or `503` with reason
            `busy`, also carry a `Retry-After` header saying how long to wait.
          type: boolean
      required:
        - reason
        - retryable
      type: object
  securitySchemes:
    apiKey:
      description: API key as bearer token in Authorization header
      scheme: bearer
      type: http

````
