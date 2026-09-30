---
title: "Get a server tool"
source: https://openrouter.ai/docs/api/api-reference/tools/get-a-server-tool.md
path: docs/api/api-reference/tools/get-a-server-tool
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a server tool

> One server tool by canonical name or any accepted alias, with the models that run it natively.



## OpenAPI

````yaml /openapi/openapi.yaml get /tools/{name}
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
  - description: End Users endpoints
    name: End Users
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
  - description: Private Endpoints endpoints
    name: Private Endpoints
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
      The catalog of server tools OpenRouter runs on behalf of a model: accepted
      `tools[].type` spellings per API format, engines and pricing, and which
      endpoints run each tool natively. See
      https://openrouter.ai/docs/guides/features/server-tools.
    name: Tools
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
  /tools/{name}:
    get:
      tags:
        - Tools
      summary: Get a server tool
      description: >-
        One server tool by canonical name or any accepted alias, with the models
        that run it natively.
      operationId: getTool
      parameters:
        - description: Canonical `openrouter:*` name or any accepted `tools[].type` alias
          in: path
          name: name
          required: true
          schema:
            description: Canonical `openrouter:*` name or any accepted `tools[].type` alias
            example: openrouter:web_search
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetToolResponse'
          description: The server tool
        '308':
          description: An alias was given; `Location` is the canonical tool URL
          headers:
            Location:
              required: true
              schema:
                example: /api/v1/tools/openrouter:web_search
                type: string
        '401':
          content:
            application/json:
              example:
                error:
                  code: 401
                  message: Missing Authentication header
              schema:
                $ref: '#/components/schemas/UnauthorizedResponse'
          description: Unauthorized - Authentication required or invalid credentials
        '403':
          content:
            application/json:
              example:
                error:
                  code: 403
                  message: Only management keys can perform this operation
              schema:
                $ref: '#/components/schemas/ForbiddenResponse'
          description: Forbidden - Authentication successful but insufficient permissions
        '404':
          content:
            application/json:
              example:
                error:
                  code: 404
                  message: Resource not found
              schema:
                $ref: '#/components/schemas/NotFoundResponse'
          description: Not Found - Resource does not exist
        '500':
          content:
            application/json:
              example:
                error:
                  code: 500
                  message: Internal Server Error
              schema:
                $ref: '#/components/schemas/InternalServerResponse'
          description: Internal Server Error - Unexpected server error
      security:
        - bearer: []
components:
  schemas:
    GetToolResponse:
      properties:
        data:
          $ref: '#/components/schemas/ServerToolDetails'
      required:
        - data
      type: object
    UnauthorizedResponse:
      description: Unauthorized - Authentication required or invalid credentials
      example:
        error:
          code: 401
          message: Missing Authentication header
      properties:
        error:
          $ref: '#/components/schemas/UnauthorizedResponseErrorData'
        openrouter_metadata:
          additionalProperties: {}
          type:
            - object
            - 'null'
        user_id:
          type:
            - string
            - 'null'
      required:
        - error
      type: object
    ForbiddenResponse:
      description: Forbidden - Authentication successful but insufficient permissions
      example:
        error:
          code: 403
          message: Only management keys can perform this operation
      properties:
        error:
          $ref: '#/components/schemas/ForbiddenResponseErrorData'
        openrouter_metadata:
          additionalProperties: {}
          type:
            - object
            - 'null'
        user_id:
          type:
            - string
            - 'null'
      required:
        - error
      type: object
    NotFoundResponse:
      description: Not Found - Resource does not exist
      example:
        error:
          code: 404
          message: Resource not found
      properties:
        error:
          $ref: '#/components/schemas/NotFoundResponseErrorData'
        openrouter_metadata:
          additionalProperties: {}
          type:
            - object
            - 'null'
        user_id:
          type:
            - string
            - 'null'
      required:
        - error
      type: object
    InternalServerResponse:
      description: Internal Server Error - Unexpected server error
      example:
        error:
          code: 500
          message: Internal Server Error
      properties:
        error:
          $ref: '#/components/schemas/InternalServerResponseErrorData'
        openrouter_metadata:
          additionalProperties: {}
          type:
            - object
            - 'null'
        user_id:
          type:
            - string
            - 'null'
      required:
        - error
      type: object
    ServerToolDetails:
      allOf:
        - $ref: '#/components/schemas/ServerTool'
        - properties:
            native_support:
              allOf:
                - $ref: '#/components/schemas/ServerToolNativeSupport'
                - properties:
                    models:
                      items:
                        $ref: '#/components/schemas/ServerToolNativeModel'
                      type: array
                  required:
                    - models
                  type: object
              description: >-
                Endpoints whose provider runs this tool itself during inference.
                Zero for tools no provider runs natively.
              example:
                endpoint_count: 18
                model_count: 12
          type: object
    UnauthorizedResponseErrorData:
      description: Error data for UnauthorizedResponse
      example:
        code: 401
        message: Missing Authentication header
      properties:
        code:
          type: integer
        message:
          type: string
        metadata:
          additionalProperties: {}
          type:
            - object
            - 'null'
      required:
        - code
        - message
      type: object
    ForbiddenResponseErrorData:
      description: Error data for ForbiddenResponse
      example:
        code: 403
        message: Only management keys can perform this operation
      properties:
        code:
          type: integer
        message:
          type: string
        metadata:
          additionalProperties: {}
          type:
            - object
            - 'null'
      required:
        - code
        - message
      type: object
    NotFoundResponseErrorData:
      description: Error data for NotFoundResponse
      example:
        code: 404
        message: Resource not found
      properties:
        code:
          type: integer
        message:
          type: string
        metadata:
          additionalProperties: {}
          type:
            - object
            - 'null'
      required:
        - code
        - message
      type: object
    InternalServerResponseErrorData:
      description: Error data for InternalServerResponse
      example:
        code: 500
        message: Internal Server Error
      properties:
        code:
          type: integer
        message:
          type: string
        metadata:
          additionalProperties: {}
          type:
            - object
            - 'null'
      required:
        - code
        - message
      type: object
    ServerTool:
      properties:
        aliases:
          description: >-
            Every spelling accepted in `tools[].type` for this tool, including
            the canonical `id`, and what the call surfaces as under each
          items:
            $ref: '#/components/schemas/ServerToolInputName'
          type: array
        default_engine:
          description: >-
            The engine a request without `parameters.engine` (or with `engine:
            "auto"`) runs on; `native` applies where the endpoint runs the tool
            itself, otherwise `fallback_engine`. A request pinned to a data
            region skips either engine when its `data_regions` does not list
            that region. Null for a tool without an engine parameter
          example: native
          type:
            - string
            - 'null'
        docs_url:
          format: uri
          type: string
        engines:
          items:
            $ref: '#/components/schemas/ServerToolEngine'
          type: array
        fallback_engine:
          description: >-
            The engine an unpinned request runs on when `default_engine` is
            `native` and the endpoint does not run the tool itself; null when
            there is no fallback
          example: exa
          type:
            - string
            - 'null'
        id:
          description: >-
            Canonical `openrouter:*` name; the stable `tools[].type` on every
            API format in `supported_api_formats`
          example: openrouter:web_search
          type: string
        input_schema:
          additionalProperties: {}
          description: JSON Schema of the arguments the model emits when calling the tool
          example:
            properties: {}
            type: object
          type: object
        name:
          example: Web search
          type: string
        native_support:
          $ref: '#/components/schemas/ServerToolNativeSupport'
        output_schema:
          additionalProperties: {}
          description: >-
            JSON Schema of the result returned to the model; null when
            undeclared
          example:
            properties: {}
            type: object
          type:
            - object
            - 'null'
        parameters_schema:
          additionalProperties: {}
          description: JSON Schema for the caller-side `tools[].parameters` object
          example:
            properties: {}
            type: object
          type: object
        status:
          enum:
            - active
            - deprecated
          example: active
          type: string
        summary:
          description: One sentence for cards and search results; never sent to a model
          type: string
        supported_api_formats:
          items:
            enum:
              - responses
              - chat-completions
              - anthropic-messages
            type: string
          type: array
        tool_description:
          description: The description sent upstream as the function tool description
          type: string
      required:
        - id
        - name
        - summary
        - tool_description
        - status
        - docs_url
        - aliases
        - supported_api_formats
        - default_engine
        - fallback_engine
        - parameters_schema
        - input_schema
        - output_schema
        - engines
        - native_support
      type: object
    ServerToolNativeSupport:
      description: >-
        Endpoints whose provider runs this tool itself during inference. Zero
        for tools no provider runs natively.
      example:
        endpoint_count: 18
        model_count: 12
      properties:
        endpoint_count:
          example: 18
          type: integer
        model_count:
          example: 12
          type: integer
      required:
        - endpoint_count
        - model_count
      type: object
    ServerToolNativeModel:
      properties:
        providers:
          example:
            - Anthropic
            - Google
          items:
            type: string
          type: array
        slug:
          example: anthropic/claude-4.5-sonnet
          type: string
      required:
        - slug
        - providers
      type: object
    ServerToolInputName:
      properties:
        api_formats:
          description: API formats that accept this spelling in `tools[].type`
          items:
            enum:
              - responses
              - chat-completions
              - anthropic-messages
            type: string
          type: array
        output_names:
          description: >-
            What the call surfaces as on each accepting API format when
            requested under this spelling; a format is absent when the call is
            not visible to the caller
          items:
            $ref: '#/components/schemas/ServerToolOutputName'
          type: array
        type:
          example: web_search_20250305
          type: string
      required:
        - type
        - api_formats
        - output_names
      type: object
    ServerToolEngine:
      properties:
        byok:
          description: >-
            Whether the engine needs the caller's own key, saved in plugin
            settings: `required` (OpenRouter holds none), `optional`
            (OpenRouter's key is used unless the caller saved one), or `none`
          enum:
            - required
            - optional
            - none
          example: none
          type: string
        data_regions:
          description: >-
            The data regions whose requests this engine serves without leaving
            the region. A request pinned to a region can only use engines that
            list it; `global` is always listed.
          example:
            - global
            - us
          items:
            enum:
              - global
              - europe
              - us
            type: string
          type: array
        default_mode:
          description: >-
            The `parameters.mode` a request without one runs and bills as; null
            for engines without modes. The `pricing[]` row with this `mode` is
            what an unmoded request bills
          example: auto
          type:
            - string
            - 'null'
        executed_by:
          $ref: '#/components/schemas/ServerToolExecutedBy'
        id:
          description: >-
            The `parameters.engine` value that selects this engine; null for the
            single engine of a tool without an engine parameter
          example: exa
          type:
            - string
            - 'null'
        name:
          example: Exa
          type: string
        pricing:
          description: >-
            The rows OpenRouter bills; non-empty exactly when `pricing_source`
            is `openrouter`
          items:
            $ref: '#/components/schemas/ServerToolPrice'
          type: array
        pricing_doc_url:
          description: >-
            Where the rates are documented when `pricing_source` is `provider`
            or `byok`; null otherwise
          example: null
          type:
            - string
            - 'null'
        pricing_source:
          description: >-
            Who bills the engine's calls beyond the model's tokens: `openrouter`
            (the `pricing` rows, from the caller's credits), `provider` (a
            per-call tool fee from the model's provider on the inference call,
            at its own rates), `byok` (the engine's vendor, against the caller's
            own key), or `none` (no charge)
          enum:
            - openrouter
            - provider
            - byok
            - none
          example: openrouter
          type: string
      required:
        - id
        - name
        - executed_by
        - data_regions
        - byok
        - default_mode
        - pricing_source
        - pricing_doc_url
        - pricing
      type: object
    ServerToolOutputName:
      properties:
        api_format:
          enum:
            - responses
            - chat-completions
            - anthropic-messages
          type: string
        name:
          description: >-
            Anthropic Messages `server_tool_use` block `name`, when the call
            surfaces as one
          example: web_search
          type: string
        type:
          description: >-
            Output item `type` on Responses, content block `type` on Anthropic
            Messages, `reasoning_details[].type` on Chat Completions
          example: web_search_call
          type: string
      required:
        - api_format
        - type
      type: object
    ServerToolExecutedBy:
      description: >-
        Who runs the tool call: the model provider during inference
        (`provider`), OpenRouter (`openrouter`), or the caller's application
        after the call is returned (`client`).
      enum:
        - provider
        - openrouter
        - client
      example: openrouter
      type: string
    ServerToolPrice:
      properties:
        max_units_per_call:
          type: integer
        mode:
          description: >-
            The `parameters.mode` this price applies to; null for prices that do
            not depend on the mode. A request bills exactly one `request` row
          example: auto
          type:
            - string
            - 'null'
        price:
          description: USD per unit, as a decimal string
          example: '0.007'
          type: string
        unit:
          example: request
          type: string
      required:
        - mode
        - unit
        - price
        - max_units_per_call
      type: object
  securitySchemes:
    apiKey:
      description: API key as bearer token in Authorization header
      scheme: bearer
      type: http
    bearer:
      description: API key as bearer token in Authorization header
      scheme: bearer
      type: http

````
