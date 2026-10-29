---
title: "List the connections an intern can use"
source: https://openrouter.ai/docs/api/api-reference/vault/list-the-connections-an-intern-can-use.md
path: docs/api/api-reference/vault/list-the-connections-an-intern-can-use
---

> ## Documentation Index
> Fetch the complete documentation index at: https://openrouter.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List the connections an intern can use

> Lists the connections in scope for the intern, by the key of their card on the dashboard's Connections tab: `github`, `slack`, `google`, a catalog MCP server such as `linear` or `notion`, or `mcp:<host>` for a custom MCP server. A connection is listed when it is stored, enabled, and not turned off or hidden for this intern, as the Connections tab lists it; whether its last test passed is not part of the rule. `ori features add` checks a feature's `ori.requires.connections` against this list. `routing` is the vault's routing table for the intern: the credentials it holds and what it would inject each for, from the same lookups the egress proxy picks a credential with, GitHub repository coverage read through the installation token and cached. `routing_text` is that table as the lines the intern reads in its instructions. Never credentials. Returns 404 for an intern the key cannot see. The scope is selected by the API key: workspace routes act on the key's active workspace and intern routes act on one intern inside that workspace. There is no default workspace and no fallback to another scope. Every vault route, including reads, requires access to the Intern API programme and returns 404 outside it. An intern's own API key is confined to that intern: it can always read the intern's secrets and effective secrets, writes to them follow the rules above, and every other intern and every workspace route answers 404. Requests on regional hostnames such as `eu.openrouter.ai` are refused. [API key](/docs/api-reference/authentication) required.



## OpenAPI

````yaml /openapi/openapi.yaml get /vault/interns/{internId}/connections
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
  - description: External Users endpoints
    name: External Users
  - description: Files endpoints
    name: Files
  - description: Generation history endpoints
    name: Generations
  - description: Guardrails endpoints
    name: Guardrails
  - description: Images endpoints
    name: Images
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
  - description: Private Providers endpoints
    name: Private Providers
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
  /vault/interns/{internId}/connections:
    get:
      tags:
        - Vault
      summary: List the connections an intern can use
      description: >-
        Lists the connections in scope for the intern, by the key of their card
        on the dashboard's Connections tab: `github`, `slack`, `google`, a
        catalog MCP server such as `linear` or `notion`, or `mcp:<host>` for a
        custom MCP server. A connection is listed when it is stored, enabled,
        and not turned off or hidden for this intern, as the Connections tab
        lists it; whether its last test passed is not part of the rule. `ori
        features add` checks a feature's `ori.requires.connections` against this
        list. `routing` is the vault's routing table for the intern: the
        credentials it holds and what it would inject each for, from the same
        lookups the egress proxy picks a credential with, GitHub repository
        coverage read through the installation token and cached. `routing_text`
        is that table as the lines the intern reads in its instructions. Never
        credentials. Returns 404 for an intern the key cannot see. The scope is
        selected by the API key: workspace routes act on the key's active
        workspace and intern routes act on one intern inside that workspace.
        There is no default workspace and no fallback to another scope. Every
        vault route, including reads, requires access to the Intern API
        programme and returns 404 outside it. An intern's own API key is
        confined to that intern: it can always read the intern's secrets and
        effective secrets, writes to them follow the rules above, and every
        other intern and every workspace route answers 404. Requests on regional
        hostnames such as `eu.openrouter.ai` are refused. [API
        key](/docs/api-reference/authentication) required.
      operationId: listInternConnections
      parameters:
        - description: UUID of an intern in the workspace selected by the API key.
          in: path
          name: internId
          required: true
          schema:
            description: UUID of an intern in the workspace selected by the API key.
            example: 7c9e6679-7425-40de-944b-e07fc1f90ae7
            format: uuid
            type: string
      responses:
        '200':
          content:
            application/json:
              example:
                data:
                  - key: github
                  - key: linear
                routing:
                  agent_id: intern_123
                  custom_origins: []
                  github:
                    apps:
                      - app_id: '71000003'
                        app_slug: openrouter-interns
                        installations:
                          - account: OpenRouterTeam
                            account_type: organization
                            coverage:
                              checked_at: '2026-10-27T19:30:00.000Z'
                              repository_count: 42
                              selection: all
                            credential_id: cred_1
                            holds_token: true
                            is_enabled: true
                            is_off_for_intern: false
                        member_links:
                          - holds_token: true
                            login: gfadlallah
                            member_user_id: user_1
                        scope: workspace
                    tokens: []
                  google:
                    accounts: []
                  host_rules:
                    - holds_secret: false
                      host: api.openai.com
                      secret_name: openai_api_key
                  mcp_origins:
                    - account_key: null
                      holds_secret: true
                      host: mcp.linear.app
                      injects: bearer
                      is_personal: false
                      routes:
                        - host: mcp.linear.app
                          path_prefix: null
                  read_at: '2026-10-27T20:00:00.000Z'
                  secrets:
                    - created_at: '2026-09-15T10:00:00.000Z'
                      hosts:
                        - api.linear.app
                      name: linear_api_key
                      scope: workspace
                  slack:
                    member_links: []
                routing_text: |-
                  ## Connections

                  ...
              schema:
                properties:
                  data:
                    items:
                      properties:
                        key:
                          type: string
                      required:
                        - key
                      type: object
                    type: array
                  routing:
                    $ref: '#/components/schemas/VaultRoutingTable'
                  routing_text:
                    description: >-
                      The routing table as the plain lines the intern reads in
                      its instructions' Connections section, or a notice that it
                      could not be read; null for a caller other than the
                      intern.
                    type:
                      - string
                      - 'null'
                required:
                  - data
                  - routing
                  - routing_text
                type: object
          description: The connections the intern can use.
        '400':
          content:
            application/json:
              examples:
                invalid-vault-request:
                  summary: Invalid vault request
                  value:
                    error:
                      code: 400
                      message: Invalid vault request
              schema:
                $ref: '#/components/schemas/BadRequestResponse'
          description: >-
            Bad Request - The secret name, path, query or JSON body failed
            validation. The vault returns 400 for a malformed request as well.
        '401':
          content:
            application/json:
              examples:
                invalid-or-missing-api-key:
                  summary: Invalid or missing API key
                  value:
                    error:
                      code: 401
                      message: Invalid or missing API key
              schema:
                $ref: '#/components/schemas/UnauthorizedResponse'
          description: >-
            Unauthorized - Missing or unknown API key. Provisioning keys cannot
            call vault routes.
        '403':
          content:
            application/json:
              examples:
                regional-hostname:
                  summary: Regional hostname
                  value:
                    error:
                      code: 403
                      message: >-
                        The Intern API does not support regional data residency
                        yet. Please use the global endpoint at openrouter.ai.
                workspace-scope-unavailable:
                  summary: Workspace scope unavailable
                  value:
                    error:
                      code: 403
                      message: Vault scope is unavailable
              schema:
                $ref: '#/components/schemas/ForbiddenResponse'
          description: >-
            Forbidden - The key has no usable workspace scope, or the request
            arrived on a regional hostname.
        '404':
          content:
            application/json:
              examples:
                not-found:
                  summary: Not found
                  value:
                    error:
                      code: 404
                      message: Not found
              schema:
                $ref: '#/components/schemas/NotFoundResponse'
          description: >-
            Not Found - The intern is not in the selected workspace or is not
            visible to the key (a member key without an admin role sees only
            interns its member created or interns in workspaces they
            administer), the secret does not exist in the selected scope, or the
            caller is outside the intern programme.
        '408':
          content:
            application/json:
              examples:
                body-timed-out:
                  summary: Body timed out
                  value:
                    error:
                      code: 408
                      message: Request body timed out
                route-deadline:
                  summary: Route deadline
                  value:
                    error:
                      code: 408
                      message: Vault request timed out
              schema:
                $ref: '#/components/schemas/RequestTimeoutResponse'
          description: >-
            Request Timeout - The route deadline passed before the request
            completed, or the request body stopped arriving.
        '429':
          content:
            application/json:
              examples:
                rate-limited:
                  summary: Rate limited
                  value:
                    error:
                      code: 429
                      message: Too many vault requests
              schema:
                $ref: '#/components/schemas/TooManyRequestsResponse'
          description: Too Many Requests - The vault rate limit was reached.
        '500':
          content:
            application/json:
              examples:
                internal-error:
                  summary: Internal error
                  value:
                    error:
                      code: 500
                      message: Internal Server Error
              schema:
                $ref: '#/components/schemas/InternalServerResponse'
          description: Internal Server Error - Scope lookup failed.
        '502':
          content:
            application/json:
              examples:
                invalid-vault-response:
                  summary: Invalid vault response
                  value:
                    error:
                      code: 502
                      message: Invalid vault response
                vault-request-failed:
                  summary: Vault request failed
                  value:
                    error:
                      code: 502
                      message: Vault request failed
              schema:
                $ref: '#/components/schemas/BadGatewayResponse'
          description: >-
            Bad Gateway - The vault could not be reached or returned an
            unexpected response.
        '503':
          content:
            application/json:
              examples:
                vault-unavailable:
                  summary: Vault unavailable
                  value:
                    error:
                      code: 503
                      message: Vault service is unavailable
                writes-disabled:
                  summary: Writes disabled
                  value:
                    error:
                      code: 503
                      message: Vault writes are not enabled
              schema:
                $ref: '#/components/schemas/ServiceUnavailableResponse'
          description: >-
            Service Unavailable - Vault writes are disabled for the caller, or
            the vault is not configured.
        '504':
          content:
            application/json:
              examples:
                vault-timed-out:
                  summary: Vault timed out
                  value:
                    error:
                      code: 504
                      message: Vault request timed out
              schema:
                $ref: '#/components/schemas/GatewayTimeoutResponse'
          description: Gateway Timeout - The vault did not answer in time.
      security:
        - apiKey: []
components:
  schemas:
    VaultRoutingTable:
      description: >-
        The intern's routing table, for the intern's own key only; null for any
        other caller or when the vault could not build it in time. The keys
        still list.
      properties:
        agent_id:
          type: string
        custom_origins:
          items:
            properties:
              host:
                type: string
              path_prefix:
                type:
                  - string
                  - 'null'
              status:
                description: >-
                  The vault injection decision for this destination, at
                  `read_at`.
                properties:
                  failure:
                    description: >-
                      The credential failure code when `state` is `failing`;
                      null otherwise.
                    type:
                      - string
                      - 'null'
                  state:
                    enum:
                      - usable
                      - no_credential
                      - failing
                    type: string
                required:
                  - state
                  - failure
                type: object
            required:
              - host
              - path_prefix
              - status
            type: object
          type: array
        github:
          properties:
            apps:
              items:
                properties:
                  app_id:
                    type:
                      - string
                      - 'null'
                  app_slug:
                    type:
                      - string
                      - 'null'
                  installations:
                    items:
                      properties:
                        account:
                          description: >-
                            The account the App is installed on, as GitHub
                            spells it.
                          type: string
                        account_type:
                          enum:
                            - organization
                            - user
                            - null
                          type:
                            - string
                            - 'null'
                        coverage:
                          description: >-
                            What GitHub says the installation covers; null until
                            read.
                          properties:
                            checked_at:
                              description: >-
                                When GitHub answered, through the installation
                                token the vault holds.
                              format: date-time
                              type: string
                            repository_count:
                              description: >-
                                Repositories the installation covers; null when
                                GitHub did not count them.
                              type:
                                - integer
                                - 'null'
                            selection:
                              enum:
                                - all
                                - selected
                              type: string
                          required:
                            - selection
                            - repository_count
                            - checked_at
                          type:
                            - object
                            - 'null'
                        credential_id:
                          type: string
                        holds_token:
                          description: >-
                            Whether the vault holds a current installation token
                            to inject.
                          type: boolean
                        is_enabled:
                          type: boolean
                        is_off_for_intern:
                          description: >-
                            The workspace turned this shared installation off or
                            hid it for this intern.
                          type: boolean
                        shadowed_by:
                          description: >-
                            What egress uses instead of this installation for a
                            request to its account: an earlier installation on
                            the same account, or a token pinned to the account.
                            Null when this installation answers.
                          enum:
                            - installation
                            - token
                            - null
                          type:
                            - string
                            - 'null'
                      required:
                        - credential_id
                        - account
                        - account_type
                        - is_enabled
                        - is_off_for_intern
                        - holds_token
                        - coverage
                        - shadowed_by
                      type: object
                    type: array
                  member_links:
                    description: >-
                      Members whose own account the vault would act as on this
                      App's accounts; GitHub still limits a member's token to
                      what that member can reach.
                    items:
                      properties:
                        holds_token:
                          type: boolean
                        login:
                          type: string
                        via:
                          description: >-
                            How the vault picks this link for the App, by the
                            same selection egress uses.
                          enum:
                            - app_link
                            - token
                            - any_link
                          type: string
                      required:
                        - login
                        - via
                        - holds_token
                      type: object
                    type: array
                  scope:
                    description: >-
                      `workspace` applies to every intern of the workspace;
                      `intern` to this intern alone.
                    enum:
                      - workspace
                      - intern
                    type: string
                required:
                  - app_id
                  - app_slug
                  - scope
                  - installations
                  - member_links
                type: object
              type: array
            tokens:
              items:
                properties:
                  holds_token:
                    type: boolean
                  login:
                    type: string
                  owner:
                    type:
                      - string
                      - 'null'
                  repository_count:
                    type:
                      - integer
                      - 'null'
                  scope:
                    description: >-
                      `workspace` applies to every intern of the workspace;
                      `intern` to this intern alone.
                    enum:
                      - workspace
                      - intern
                    type: string
                required:
                  - login
                  - owner
                  - repository_count
                  - scope
                  - holds_token
                type: object
              type: array
          required:
            - apps
            - tokens
          type: object
        google:
          properties:
            accounts:
              items:
                properties:
                  delegated_capabilities:
                    items:
                      type: string
                    type: array
                  email:
                    type: string
                  holds_grant:
                    type: boolean
                  is_delegated_to_intern:
                    type: boolean
                  scope:
                    description: >-
                      `workspace` applies to every intern of the workspace;
                      `intern` to this intern alone.
                    enum:
                      - workspace
                      - intern
                    type: string
                required:
                  - email
                  - scope
                  - is_delegated_to_intern
                  - delegated_capabilities
                  - holds_grant
                type: object
              type: array
          required:
            - accounts
          type: object
        host_rules:
          description: >-
            Built-in hosts the vault injects a named secret for, and whether
            that secret is stored.
          items:
            properties:
              holds_secret:
                type: boolean
              host:
                type: string
              secret_name:
                type: string
            required:
              - host
              - secret_name
              - holds_secret
            type: object
          type: array
        mcp_origins:
          items:
            properties:
              account_key:
                type:
                  - string
                  - 'null'
              host:
                type: string
              is_personal:
                description: Members' own accounts, matched to the acting member per turn.
                type: boolean
              routes:
                items:
                  properties:
                    host:
                      type: string
                    path_prefix:
                      type:
                        - string
                        - 'null'
                  required:
                    - host
                    - path_prefix
                  type: object
                type: array
              status:
                description: >-
                  The vault's decision for a request to this server; null for
                  members' own accounts, decided per acting member.
                properties:
                  failure:
                    description: >-
                      The credential failure code when `state` is `failing`;
                      null otherwise.
                    type:
                      - string
                      - 'null'
                  state:
                    enum:
                      - usable
                      - no_credential
                      - failing
                    type: string
                required:
                  - state
                  - failure
                type:
                  - object
                  - 'null'
            required:
              - host
              - account_key
              - is_personal
              - routes
              - status
            type: object
          type: array
        read_at:
          format: date-time
          type: string
        secrets:
          items:
            properties:
              created_at:
                type: string
              hosts:
                items:
                  type: string
                type:
                  - array
                  - 'null'
              name:
                type: string
              scope:
                enum:
                  - intern
                  - attached
                  - workspace
                type: string
            required:
              - name
              - hosts
              - scope
              - created_at
            type: object
          type: array
        slack:
          properties:
            member_links:
              description: >-
                Members whose own Slack account the vault can act as; whether
                the intern's own Slack app runs is a runtime fact the
                `connections` tool reports.
              items:
                properties:
                  holds_token:
                    type: boolean
                  slack_user_id:
                    type: string
                required:
                  - slack_user_id
                  - holds_token
                type: object
              type: array
          required:
            - member_links
          type: object
      required:
        - agent_id
        - read_at
        - github
        - google
        - slack
        - mcp_origins
        - host_rules
        - custom_origins
        - secrets
      type:
        - object
        - 'null'
    BadRequestResponse:
      description: Bad Request - Invalid request parameters or malformed input
      example:
        error:
          code: 400
          message: Invalid request parameters
      properties:
        error:
          $ref: '#/components/schemas/BadRequestResponseErrorData'
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
    RequestTimeoutResponse:
      description: Request Timeout - Operation exceeded time limit
      example:
        error:
          code: 408
          message: Operation timed out. Please try again later.
      properties:
        error:
          $ref: '#/components/schemas/RequestTimeoutResponseErrorData'
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
    TooManyRequestsResponse:
      description: Too Many Requests - Rate limit exceeded
      example:
        error:
          code: 429
          message: Rate limit exceeded
      properties:
        error:
          $ref: '#/components/schemas/TooManyRequestsResponseErrorData'
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
    BadGatewayResponse:
      description: Bad Gateway - Provider/upstream API failure
      example:
        error:
          code: 502
          message: Provider returned error
      properties:
        error:
          $ref: '#/components/schemas/BadGatewayResponseErrorData'
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
    ServiceUnavailableResponse:
      description: Service Unavailable - Service temporarily unavailable
      example:
        error:
          code: 503
          message: Service temporarily unavailable
      properties:
        error:
          $ref: '#/components/schemas/ServiceUnavailableResponseErrorData'
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
    GatewayTimeoutResponse:
      description: Gateway Timeout - Provider did not respond before the upstream deadline
      example:
        error:
          code: 504
          message: The operation was aborted due to timeout
      properties:
        error:
          $ref: '#/components/schemas/GatewayTimeoutResponseErrorData'
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
    BadRequestResponseErrorData:
      description: Error data for BadRequestResponse
      example:
        code: 400
        message: Invalid request parameters
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
    RequestTimeoutResponseErrorData:
      description: Error data for RequestTimeoutResponse
      example:
        code: 408
        message: Operation timed out. Please try again later.
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
    TooManyRequestsResponseErrorData:
      description: Error data for TooManyRequestsResponse
      example:
        code: 429
        message: Rate limit exceeded
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
    BadGatewayResponseErrorData:
      description: Error data for BadGatewayResponse
      example:
        code: 502
        message: Provider returned error
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
    ServiceUnavailableResponseErrorData:
      description: Error data for ServiceUnavailableResponse
      example:
        code: 503
        message: Service temporarily unavailable
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
    GatewayTimeoutResponseErrorData:
      description: Error data for GatewayTimeoutResponse
      example:
        code: 504
        message: The operation was aborted due to timeout
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
  securitySchemes:
    apiKey:
      description: API key as bearer token in Authorization header
      scheme: bearer
      type: http

````
