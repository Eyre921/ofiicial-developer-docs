---
title: "Build a Voice Agent"
source: https://developers.deepgram.com/reference/voice-agent/voice-agent.md
path: reference/voice-agent/voice-agent
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Build a Voice Agent

GET /v1/agent/converse

Build a conversational voice agent using Deepgram's Voice Agent WebSocket

Reference: https://developers.deepgram.com/reference/voice-agent/voice-agent

## AsyncAPI Specification

```yaml
asyncapi: 2.6.0
info:
  title: agent.v1
  version: subpackage_agent/v1.agent.v1
  description: Build a conversational voice agent using Deepgram's Voice Agent WebSocket
channels:
  /v1/agent/converse:
    description: Build a conversational voice agent using Deepgram's Voice Agent WebSocket
    bindings:
      ws:
        headers:
          type: object
          properties:
            Authorization:
              type: string
    publish:
      operationId: subpackage_agent/v1.agent.v1-publish
      summary: Server messages
      message:
        oneOf:
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-0-AgentV1ListenUpdated
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-1-AgentV1ThinkUpdated
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-2-AgentV1ThinkLiveUpdated
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-3-AgentV1FrustrationDetected
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-4-AgentV1ReceiveFunctionCallResponse
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-5-AgentV1PromptUpdated
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-6-AgentV1SpeakUpdated
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-7-AgentV1InjectionRefused
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-8-AgentV1Welcome
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-9-AgentV1SettingsApplied
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-10-AgentV1ConversationText
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-11-AgentV1UserStartedSpeaking
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-12-AgentV1AgentThinking
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-13-AgentV1LatencyReport
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-14-AgentV1FunctionCallRequest
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-15-AgentV1FunctionCallCancelled
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-16-AgentV1AgentStartedSpeaking
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-17-AgentV1AgentAudioDone
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-18-AgentV1CustomFromThinkProvider
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-19-AgentV1Error
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-20-AgentV1Warning
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-21-AgentV1History
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-server-22-AgentV1Audio
    subscribe:
      operationId: subpackage_agent/v1.agent.v1-subscribe
      summary: Client messages
      message:
        oneOf:
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-client-0-AgentV1Settings
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-client-1-AgentV1UpdateListen
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-client-2-AgentV1UpdateThink
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-client-3-AgentV1UpdateThinkLive
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-client-4-AgentV1UpdateSpeak
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-client-5-AgentV1InjectUserMessage
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-client-6-AgentV1InjectAgentMessage
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-client-7-AgentV1InjectDynamicAgentMessage
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-client-8-AgentV1SendFunctionCallResponse
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-client-9-AgentV1KeepAlive
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-client-10-AgentV1UpdatePrompt
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-client-11-AgentV1ForceEndTurn
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-client-12-AgentV1CustomToThinkProvider
          - $ref: >-
              #/components/messages/subpackage_agent/v1.agent.v1-client-13-AgentV1Media
servers:
  Production:
    url: wss://agent.deepgram.com/
    protocol: wss
    x-default: true
components:
  messages:
    subpackage_agent/v1.agent.v1-server-0-AgentV1ListenUpdated:
      name: AgentV1ListenUpdated
      title: AgentV1ListenUpdated
      description: Confirms that an UpdateListen message from the client has been applied
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1ListenUpdated'
    subpackage_agent/v1.agent.v1-server-1-AgentV1ThinkUpdated:
      name: AgentV1ThinkUpdated
      title: AgentV1ThinkUpdated
      description: Confirms that an UpdateThink message from the client has been applied
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1ThinkUpdated'
    subpackage_agent/v1.agent.v1-server-2-AgentV1ThinkLiveUpdated:
      name: AgentV1ThinkLiveUpdated
      title: AgentV1ThinkLiveUpdated
      description: >-
        Confirms that an UpdateThink_Live message from the client has been
        applied
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1ThinkLiveUpdated'
    subpackage_agent/v1.agent.v1-server-3-AgentV1FrustrationDetected:
      name: AgentV1FrustrationDetected
      title: AgentV1FrustrationDetected
      description: >-
        Sent when the Think Live model detects frustration in a user turn
        (negative valence, high arousal, or frustrated intent). Treat
        `escalated: true` as the trigger for your own escalation workflow;
        Deepgram does not transfer the call. Not sent when
        `agent.think_live.provider.frustration_max_count` is 0
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1FrustrationDetected'
    subpackage_agent/v1.agent.v1-server-4-AgentV1ReceiveFunctionCallResponse:
      name: AgentV1ReceiveFunctionCallResponse
      title: AgentV1ReceiveFunctionCallResponse
      description: |
        Receive a function call response from the server after the server
        has executed a server-side function call internally. This occurs
        when functions are marked with `client_side: false`.
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1ReceiveFunctionCallResponse'
    subpackage_agent/v1.agent.v1-server-5-AgentV1PromptUpdated:
      name: AgentV1PromptUpdated
      title: AgentV1PromptUpdated
      description: Confirms that an UpdatePrompt message from the client has been applied
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1PromptUpdated'
    subpackage_agent/v1.agent.v1-server-6-AgentV1SpeakUpdated:
      name: AgentV1SpeakUpdated
      title: AgentV1SpeakUpdated
      description: Confirms that an UpdateSpeak message from the client has been applied
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1SpeakUpdated'
    subpackage_agent/v1.agent.v1-server-7-AgentV1InjectionRefused:
      name: AgentV1InjectionRefused
      title: AgentV1InjectionRefused
      description: Receive injection refused message
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1InjectionRefused'
    subpackage_agent/v1.agent.v1-server-8-AgentV1Welcome:
      name: AgentV1Welcome
      title: AgentV1Welcome
      description: Confirms that the WebSocket connection has been successfully opened
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1Welcome'
    subpackage_agent/v1.agent.v1-server-9-AgentV1SettingsApplied:
      name: AgentV1SettingsApplied
      title: AgentV1SettingsApplied
      description: >-
        Confirm the server has successfully received and applied the Settings
        message
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1SettingsApplied'
    subpackage_agent/v1.agent.v1-server-10-AgentV1ConversationText:
      name: AgentV1ConversationText
      title: AgentV1ConversationText
      description: >-
        Facilitate real-time communication by relaying spoken statements from
        both the user and the assistant
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1ConversationText'
    subpackage_agent/v1.agent.v1-server-11-AgentV1UserStartedSpeaking:
      name: AgentV1UserStartedSpeaking
      title: AgentV1UserStartedSpeaking
      description: Notify the client that the user has begun speaking
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1UserStartedSpeaking'
    subpackage_agent/v1.agent.v1-server-12-AgentV1AgentThinking:
      name: AgentV1AgentThinking
      title: AgentV1AgentThinking
      description: Inform the client when the agent is processing information
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1AgentThinking'
    subpackage_agent/v1.agent.v1-server-13-AgentV1LatencyReport:
      name: AgentV1LatencyReport
      title: AgentV1LatencyReport
      description: >-
        Detailed latency breakdown across the STT, LLM, and TTS pipeline,
        emitted by the server after a turn. All latency fields are floats in
        seconds and are optional, so they are omitted when not applicable to
        that turn.
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1LatencyReport'
    subpackage_agent/v1.agent.v1-server-14-AgentV1FunctionCallRequest:
      name: AgentV1FunctionCallRequest
      title: AgentV1FunctionCallRequest
      description: Client-side or server-side function call request sent by the server
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1FunctionCallRequest'
    subpackage_agent/v1.agent.v1-server-15-AgentV1FunctionCallCancelled:
      name: AgentV1FunctionCallCancelled
      title: AgentV1FunctionCallCancelled
      description: >-
        Sent when a client-side function call the server already sent you is
        cancelled because the user started speaking again, either inside the
        speculative window (the turn resumed) or after the turn was confirmed
        (barge-in). Only calls the client already received are announced
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1FunctionCallCancelled'
    subpackage_agent/v1.agent.v1-server-16-AgentV1AgentStartedSpeaking:
      name: AgentV1AgentStartedSpeaking
      title: AgentV1AgentStartedSpeaking
      description: >-
        Get notified when the server begins streaming an agent's audio response
        for playback. This message is only sent when the experimental flag is
        enabled
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1AgentStartedSpeaking'
    subpackage_agent/v1.agent.v1-server-17-AgentV1AgentAudioDone:
      name: AgentV1AgentAudioDone
      title: AgentV1AgentAudioDone
      description: >-
        Get signals that the server has finished sending the final audio segment
        to the client
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1AgentAudioDone'
    subpackage_agent/v1.agent.v1-server-18-AgentV1CustomFromThinkProvider:
      name: AgentV1CustomFromThinkProvider
      title: AgentV1CustomFromThinkProvider
      description: >-
        Experimental. Receive the response body from your custom think provider
        after sending a __customToThinkProvider message. Deepgram passes the
        response through unchanged. Requires a `wss://` custom Think endpoint in
        `agent.think.endpoint.url`.
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1CustomFromThinkProvider'
    subpackage_agent/v1.agent.v1-server-19-AgentV1Error:
      name: AgentV1Error
      title: AgentV1Error
      description: Receive an error message from the server when an error occurs
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1Error'
    subpackage_agent/v1.agent.v1-server-20-AgentV1Warning:
      name: AgentV1Warning
      title: AgentV1Warning
      description: Notifies the client of non-fatal errors or warnings
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1Warning'
    subpackage_agent/v1.agent.v1-server-21-AgentV1History:
      name: AgentV1History
      title: AgentV1History
      description: >-
        Conversation history message emitted by the server during a session.
        Each message is either a conversation text message or a function call
        message. These messages can be supplied in settings of a subsequent
        Voice Agent session (via the agent.context.messages field) to allow the
        agent to maintain awareness of prior interactions.
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1History'
    subpackage_agent/v1.agent.v1-server-22-AgentV1Audio:
      name: AgentV1Audio
      title: AgentV1Audio
      description: >-
        Raw binary audio data generated by the Voice Agent and sent to the
        client
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1Audio'
    subpackage_agent/v1.agent.v1-client-0-AgentV1Settings:
      name: AgentV1Settings
      title: AgentV1Settings
      description: Configure the voice agent and sets the input and output audio formats
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1Settings'
    subpackage_agent/v1.agent.v1-client-1-AgentV1UpdateListen:
      name: AgentV1UpdateListen
      title: AgentV1UpdateListen
      description: >-
        Send a message to update the Listen configuration on the fly during a
        conversation. The payload uses the same shape as agent.listen in the
        Settings message — model, language, and the other tunable fields live
        under listen.provider.
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1UpdateListen'
    subpackage_agent/v1.agent.v1-client-2-AgentV1UpdateThink:
      name: AgentV1UpdateThink
      title: AgentV1UpdateThink
      description: Send a message to change the Think model in the middle of a conversation
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1UpdateThink'
    subpackage_agent/v1.agent.v1-client-3-AgentV1UpdateThinkLive:
      name: AgentV1UpdateThinkLive
      title: AgentV1UpdateThinkLive
      description: >-
        Change the Think Live model configuration in the middle of a
        conversation. Replaces the entire `think_live.provider` block, so
        include every parameter you want in effect; omitted parameters revert to
        their defaults. Does not affect the reasoning LLM (use UpdateThink for
        that). The server confirms with ThinkLiveUpdated
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1UpdateThinkLive'
    subpackage_agent/v1.agent.v1-client-4-AgentV1UpdateSpeak:
      name: AgentV1UpdateSpeak
      title: AgentV1UpdateSpeak
      description: Send a message to change the Speak model in the middle of a conversation
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1UpdateSpeak'
    subpackage_agent/v1.agent.v1-client-5-AgentV1InjectUserMessage:
      name: AgentV1InjectUserMessage
      title: AgentV1InjectUserMessage
      description: Send a text based message to the agent
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1InjectUserMessage'
    subpackage_agent/v1.agent.v1-client-6-AgentV1InjectAgentMessage:
      name: AgentV1InjectAgentMessage
      title: AgentV1InjectAgentMessage
      description: Immediately trigger an agent response during a conversation
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1InjectAgentMessage'
    subpackage_agent/v1.agent.v1-client-7-AgentV1InjectDynamicAgentMessage:
      name: AgentV1InjectDynamicAgentMessage
      title: AgentV1InjectDynamicAgentMessage
      description: >-
        Requires `agent.think_live`. Ask the Think Live model to generate a
        short filler line instead of speaking a fixed message. Each request
        produces one filler; another request during the same wait escalates the
        wording. If filler cannot be generated, nothing is spoken and the server
        sends a `DYNAMIC_FILLER_UNAVAILABLE` warning
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1InjectDynamicAgentMessage'
    subpackage_agent/v1.agent.v1-client-8-AgentV1SendFunctionCallResponse:
      name: AgentV1SendFunctionCallResponse
      title: AgentV1SendFunctionCallResponse
      description: |
        Send a function call response from the client to the server after
        executing a client-side function call. This is used when the server
        requests execution of a function marked with `client_side: true`.
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1SendFunctionCallResponse'
    subpackage_agent/v1.agent.v1-client-9-AgentV1KeepAlive:
      name: AgentV1KeepAlive
      title: AgentV1KeepAlive
      description: Send a control message to the agent
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1KeepAlive'
    subpackage_agent/v1.agent.v1-client-10-AgentV1UpdatePrompt:
      name: AgentV1UpdatePrompt
      title: AgentV1UpdatePrompt
      description: Send a message to update the system prompt of the agent
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1UpdatePrompt'
    subpackage_agent/v1.agent.v1-client-11-AgentV1ForceEndTurn:
      name: AgentV1ForceEndTurn
      title: AgentV1ForceEndTurn
      description: >-
        End the current user turn immediately, without waiting for end-of-turn
        detection. Requires a Deepgram V2 (Flux) listen provider; with any other
        listen provider the server sends a FORCE_END_TURN_UNSUPPORTED warning
        and the turn does not end.
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1ForceEndTurn'
    subpackage_agent/v1.agent.v1-client-12-AgentV1CustomToThinkProvider:
      name: AgentV1CustomToThinkProvider
      title: AgentV1CustomToThinkProvider
      description: >-
        Experimental. Send an arbitrary JSON payload to your custom think
        provider. Deepgram does not validate the content and forwards it to the
        provider unchanged. Requires a `wss://` custom Think endpoint in
        `agent.think.endpoint.url`. The provider's response arrives as a
        __customFromThinkProvider message.
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1CustomToThinkProvider'
    subpackage_agent/v1.agent.v1-client-13-AgentV1Media:
      name: AgentV1Media
      title: AgentV1Media
      description: Raw binary audio data sent to the Voice Agent for processing
      payload:
        $ref: '#/components/schemas/AgentV1_AgentV1Media'
  schemas:
    AgentV1_AgentV1ListenUpdated:
      type: object
      properties:
        type:
          type: string
          enum:
            - ListenUpdated
          description: Message type identifier for listen update confirmation
      required:
        - type
      title: AgentV1_AgentV1ListenUpdated
    AgentV1_AgentV1ThinkUpdated:
      type: object
      properties:
        type:
          type: string
          enum:
            - ThinkUpdated
          description: Message type identifier for think update confirmation
      required:
        - type
      title: AgentV1_AgentV1ThinkUpdated
    AgentV1_AgentV1ThinkLiveUpdated:
      type: object
      properties:
        type:
          type: string
          enum:
            - ThinkLiveUpdated
          description: Message type identifier for Think Live model update confirmation
      required:
        - type
      title: AgentV1_AgentV1ThinkLiveUpdated
    AgentV1_AgentV1FrustrationDetected:
      type: object
      properties:
        type:
          type: string
          enum:
            - FrustrationDetected
          description: Message type identifier for frustration detection
        count:
          type: integer
          minimum: 1
          description: >-
            Cumulative number of FrustrationDetected events in this session,
            starting at 1
        escalated:
          type: boolean
          description: >-
            True once `count` reaches
            `agent.think_live.provider.frustration_max_count`
      required:
        - type
        - count
        - escalated
      title: AgentV1_AgentV1FrustrationDetected
    AgentV1_AgentV1ReceiveFunctionCallResponse:
      type: object
      properties:
        type:
          type: string
          enum:
            - FunctionCallResponse
          description: Message type identifier for function call responses
        id:
          type: string
          description: |
            The unique identifier for the function call.

            • **Required for client responses**: Should match the id from
              the corresponding `FunctionCallRequest`
            • **Optional for server responses**: Server may omit when responding
              to internal function executions
        name:
          type: string
          description: The name of the function being called
        content:
          type: string
          description: The content or result of the function call
      required:
        - type
        - name
        - content
      description: |
        Function call response message used bidirectionally:

        • **Client → Server**: Response after client executes a function
          marked as client_side: true
        • **Server → Client**: Response after server executes a function
          marked as client_side: false

        The same message structure serves both directions, enabling a unified
        interface for function call responses regardless of execution location.
      title: AgentV1_AgentV1ReceiveFunctionCallResponse
    AgentV1_AgentV1PromptUpdated:
      type: object
      properties:
        type:
          type: string
          enum:
            - PromptUpdated
          description: Message type identifier for prompt update confirmation
      required:
        - type
      title: AgentV1_AgentV1PromptUpdated
    AgentV1_AgentV1SpeakUpdated:
      type: object
      properties:
        type:
          type: string
          enum:
            - SpeakUpdated
          description: Message type identifier for speak update confirmation
      required:
        - type
      title: AgentV1_AgentV1SpeakUpdated
    AgentV1_AgentV1InjectionRefused:
      type: object
      properties:
        type:
          type: string
          enum:
            - InjectionRefused
          description: Message type identifier for injection refused
        message:
          type: string
          description: Details about why the injection was refused
      required:
        - type
        - message
      title: AgentV1_AgentV1InjectionRefused
    AgentV1_AgentV1Welcome:
      type: object
      properties:
        type:
          type: string
          enum:
            - Welcome
          description: Message type identifier for welcome message
        request_id:
          type: string
          description: Unique identifier for the request
      required:
        - type
        - request_id
      title: AgentV1_AgentV1Welcome
    AgentV1_AgentV1SettingsApplied:
      type: object
      properties:
        type:
          type: string
          enum:
            - SettingsApplied
          description: Message type identifier for settings applied confirmation
      required:
        - type
      title: AgentV1_AgentV1SettingsApplied
    ChannelsAgentV1MessagesAgentV1ConversationTextRole:
      type: string
      enum:
        - user
        - assistant
      description: Identifies who spoke the statement
      title: ChannelsAgentV1MessagesAgentV1ConversationTextRole
    ChannelsAgentV1MessagesAgentV1ConversationTextConversationalBehavior:
      type: string
      enum:
        - default
        - backchannel
        - presence_check
        - filler
      description: >-
        Annotates what kind of utterance the message represents: `default` (a
        standard turn), `backchannel` (a short acknowledgement while the user
        held the floor), `presence_check` (a prompt after extended silence), or
        `filler` (a line covering a wait on a function call or a dynamic
        InjectAgentMessage). Always sent; it is `default` for every message
        while Think Live is off
      title: ChannelsAgentV1MessagesAgentV1ConversationTextConversationalBehavior
    AgentV1_AgentV1ConversationText:
      type: object
      properties:
        type:
          type: string
          enum:
            - ConversationText
          description: Message type identifier for conversation text
        role:
          $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1ConversationTextRole
          description: Identifies who spoke the statement
        content:
          type: string
          description: The actual statement that was spoken
        conversational_behavior:
          $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1ConversationTextConversationalBehavior
          description: >-
            Annotates what kind of utterance the message represents: `default`
            (a standard turn), `backchannel` (a short acknowledgement while the
            user held the floor), `presence_check` (a prompt after extended
            silence), or `filler` (a line covering a wait on a function call or
            a dynamic InjectAgentMessage). Always sent; it is `default` for
            every message while Think Live is off
        languages_hinted:
          type: array
          items:
            type: string
          description: >-
            The language hints that were active at the time of the turn. Only
            present on user-role messages when the listen model is
            flux-general-multi.
        languages:
          type: array
          items:
            type: string
          description: >-
            Languages detected in the user's speech, sorted by word count
            (descending). Only present on user-role messages when the listen
            model is flux-general-multi.
      required:
        - type
        - role
        - content
        - conversational_behavior
      title: AgentV1_AgentV1ConversationText
    AgentV1_AgentV1UserStartedSpeaking:
      type: object
      properties:
        type:
          type: string
          enum:
            - UserStartedSpeaking
          description: Message type identifier indicating that the user has begun speaking
      required:
        - type
      title: AgentV1_AgentV1UserStartedSpeaking
    AgentV1_AgentV1AgentThinking:
      type: object
      properties:
        type:
          type: string
          enum:
            - AgentThinking
          description: Message type identifier for agent thinking
        content:
          type: string
          description: The text of the agent's thought process
      required:
        - type
        - content
      title: AgentV1_AgentV1AgentThinking
    AgentV1_AgentV1LatencyReport:
      type: object
      properties:
        type:
          type: string
          enum:
            - LatencyReport
          description: Message type identifier for the latency report
        stt_latency:
          type: string
          title: float
          description: >-
            Speech-to-text: time from audio received to transcript produced, in
            seconds
        ttt_token_latency:
          type: string
          title: float
          description: >-
            Time to first token of any type (text, tool call, or thinking), in
            seconds
        ttt_text_latency:
          type: string
          title: float
          description: Time to first text token from the LLM, in seconds
        ttt_tool_latency:
          type: string
          title: float
          description: Time to first tool-call token from the LLM, in seconds
        ttt_thinking_latency:
          type: string
          title: float
          description: Time to first thinking token from the LLM, in seconds
        tts_latency:
          type: string
          title: float
          description: >-
            Text-to-speech: time from first text token to first audio byte, in
            seconds
        total_latency:
          type: string
          title: float
          description: >-
            End-to-end: time from user utterance end to first audio byte, in
            seconds
      required:
        - type
      title: AgentV1_AgentV1LatencyReport
    ChannelsAgentV1MessagesAgentV1FunctionCallRequestFunctionsItems:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the function call
        name:
          type: string
          description: The name of the function to call
        arguments:
          type: string
          description: JSON string containing the function arguments
        client_side:
          type: boolean
          description: Whether the function should be executed client-side
        thought_signature:
          type: string
          description: >-
            Some Gemini models require this as an additional function call
            identifier
      required:
        - id
        - name
        - arguments
        - client_side
      title: ChannelsAgentV1MessagesAgentV1FunctionCallRequestFunctionsItems
    AgentV1_AgentV1FunctionCallRequest:
      type: object
      properties:
        type:
          type: string
          enum:
            - FunctionCallRequest
          description: Message type identifier for function call requests
        functions:
          type: array
          items:
            $ref: >-
              #/components/schemas/ChannelsAgentV1MessagesAgentV1FunctionCallRequestFunctionsItems
          description: Array of functions to be called
      required:
        - type
        - functions
      title: AgentV1_AgentV1FunctionCallRequest
    ChannelsAgentV1MessagesAgentV1FunctionCallCancelledFunctionsItems:
      type: object
      properties:
        id:
          type: string
          description: >-
            The id from the FunctionCallRequest that is now cancelled. Send no
            FunctionCallResponse for this id
        name:
          type: string
          description: The name of the cancelled function
      required:
        - id
        - name
      title: ChannelsAgentV1MessagesAgentV1FunctionCallCancelledFunctionsItems
    AgentV1_AgentV1FunctionCallCancelled:
      type: object
      properties:
        type:
          type: string
          enum:
            - FunctionCallCancelled
          description: Message type identifier for cancelled function calls
        functions:
          type: array
          items:
            $ref: >-
              #/components/schemas/ChannelsAgentV1MessagesAgentV1FunctionCallCancelledFunctionsItems
          description: The function calls that are no longer valid
      required:
        - type
        - functions
      title: AgentV1_AgentV1FunctionCallCancelled
    AgentV1_AgentV1AgentStartedSpeaking:
      type: object
      properties:
        type:
          type: string
          enum:
            - AgentStartedSpeaking
          description: Message type identifier for agent started speaking
        total_latency:
          type: string
          title: float
          description: >-
            Seconds from receiving the user's utterance to producing the agent's
            reply
        tts_latency:
          type: string
          title: float
          description: The portion of total latency attributable to text-to-speech
        ttt_latency:
          type: string
          title: float
          description: >-
            The portion of total latency attributable to text-to-text (usually
            an LLM)
      required:
        - type
        - total_latency
        - tts_latency
        - ttt_latency
      title: AgentV1_AgentV1AgentStartedSpeaking
    AgentV1_AgentV1AgentAudioDone:
      type: object
      properties:
        type:
          type: string
          enum:
            - AgentAudioDone
          description: >-
            Message type identifier indicating the agent has finished sending
            audio
      required:
        - type
      title: AgentV1_AgentV1AgentAudioDone
    AgentV1_AgentV1CustomFromThinkProvider:
      type: object
      properties:
        type:
          type: string
          enum:
            - __customFromThinkProvider
          description: >-
            Message type identifier for a custom payload returned by the think
            provider
        content:
          description: >-
            The think provider's response body, passed through unchanged. If the
            provider's response is not valid JSON, it arrives as a JSON string
      required:
        - type
        - content
      title: AgentV1_AgentV1CustomFromThinkProvider
    ChannelsAgentV1MessagesAgentV1ErrorType:
      type: string
      enum:
        - Error
      description: Message type identifier for error responses
      title: ChannelsAgentV1MessagesAgentV1ErrorType
    AgentV1_AgentV1Error:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ChannelsAgentV1MessagesAgentV1ErrorType'
          description: Message type identifier for error responses
        description:
          type: string
          description: A description of what went wrong
        code:
          type: string
          description: Error code identifying the type of error
      required:
        - type
        - description
        - code
      title: AgentV1_AgentV1Error
    ChannelsAgentV1MessagesAgentV1WarningType:
      type: string
      enum:
        - Warning
      description: Message type identifier for warnings
      title: ChannelsAgentV1MessagesAgentV1WarningType
    AgentV1_AgentV1Warning:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ChannelsAgentV1MessagesAgentV1WarningType'
          description: Message type identifier for warnings
        description:
          type: string
          description: Description of the warning
        code:
          type: string
          description: Warning code identifier
      required:
        - type
        - description
        - code
      description: Notifies the client of non-fatal errors or warnings
      title: AgentV1_AgentV1Warning
    ChannelsAgentV1MessagesAgentV1HistoryOneOf0Role:
      type: string
      enum:
        - user
        - assistant
      description: Identifies who spoke the statement
      title: ChannelsAgentV1MessagesAgentV1HistoryOneOf0Role
    AgentV1AgentV1History0:
      type: object
      properties:
        type:
          type: string
          enum:
            - History
          description: Message type identifier for conversation text
        role:
          $ref: '#/components/schemas/ChannelsAgentV1MessagesAgentV1HistoryOneOf0Role'
          description: Identifies who spoke the statement
        content:
          type: string
          description: The actual statement that was spoken
      required:
        - type
        - role
        - content
      description: Conversation text as part of the conversation history
      title: AgentV1AgentV1History0
    ChannelsAgentV1MessagesAgentV1HistoryOneOf1FunctionCallsItems:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the function call
        name:
          type: string
          description: Name of the function called
        client_side:
          type: boolean
          description: Indicates if the call was client-side or server-side
        arguments:
          type: string
          description: Arguments passed to the function
        response:
          type: string
          description: Response from the function call
        thought_signature:
          type: string
          description: >-
            Some Gemini models require this as an additional function call
            identifier
      required:
        - id
        - name
        - client_side
        - arguments
        - response
      title: ChannelsAgentV1MessagesAgentV1HistoryOneOf1FunctionCallsItems
    AgentV1AgentV1History1:
      type: object
      properties:
        type:
          type: string
          enum:
            - History
        function_calls:
          type: array
          items:
            $ref: >-
              #/components/schemas/ChannelsAgentV1MessagesAgentV1HistoryOneOf1FunctionCallsItems
          description: List of function call objects
      required:
        - type
        - function_calls
      description: >-
        Client-side or server-side function call request and response as part of
        the conversation history
      title: AgentV1AgentV1History1
    AgentV1_AgentV1History:
      oneOf:
        - $ref: '#/components/schemas/AgentV1AgentV1History0'
        - $ref: '#/components/schemas/AgentV1AgentV1History1'
      description: A history message is either a conversational message or a function call
      title: AgentV1_AgentV1History
    AgentV1_AgentV1Audio:
      type: string
      format: binary
      title: AgentV1_AgentV1Audio
    ChannelsAgentV1MessagesAgentV1SettingsFlags:
      type: object
      properties:
        history:
          type: boolean
          default: true
          description: Enable or disable history message reporting
      title: ChannelsAgentV1MessagesAgentV1SettingsFlags
    ChannelsAgentV1MessagesAgentV1SettingsAudioInputEncoding:
      type: string
      enum:
        - linear16
        - linear32
        - flac
        - alaw
        - mulaw
        - amr-nb
        - amr-wb
        - opus
        - ogg-opus
        - speex
        - g729
      default: linear16
      description: Audio encoding format
      title: ChannelsAgentV1MessagesAgentV1SettingsAudioInputEncoding
    ChannelsAgentV1MessagesAgentV1SettingsAudioInput:
      type: object
      properties:
        encoding:
          $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAudioInputEncoding
          description: Audio encoding format
        sample_rate:
          type: integer
          default: 24000
          description: Sample rate in Hz. Common values are 16000, 24000, 44100, 48000
      required:
        - encoding
        - sample_rate
      description: >-
        Audio input configuration settings. If omitted, defaults to
        encoding=linear16 and sample_rate=24000. Higher sample rates like 44100
        Hz provide better audio quality.
      title: ChannelsAgentV1MessagesAgentV1SettingsAudioInput
    ChannelsAgentV1MessagesAgentV1SettingsAudioOutputEncoding:
      type: string
      enum:
        - linear16
        - mulaw
        - alaw
        - mp3
        - opus
        - flac
        - aac
      default: linear16
      description: Audio encoding format for streaming TTS output
      title: ChannelsAgentV1MessagesAgentV1SettingsAudioOutputEncoding
    ChannelsAgentV1MessagesAgentV1SettingsAudioOutputContainer:
      type: string
      enum:
        - none
        - wav
        - ogg
      default: none
      description: Audio container format.
      title: ChannelsAgentV1MessagesAgentV1SettingsAudioOutputContainer
    ChannelsAgentV1MessagesAgentV1SettingsAudioOutput:
      type: object
      properties:
        encoding:
          $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAudioOutputEncoding
          default: linear16
          description: Audio encoding format for streaming TTS output
        sample_rate:
          type: integer
          description: Sample rate in Hz
        bitrate:
          type: integer
          description: Audio bitrate in bits per second
        container:
          $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAudioOutputContainer
          default: none
          description: Audio container format.
      description: Audio output configuration settings
      title: ChannelsAgentV1MessagesAgentV1SettingsAudioOutput
    ChannelsAgentV1MessagesAgentV1SettingsAudio:
      type: object
      properties:
        input:
          $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAudioInput
          description: >-
            Audio input configuration settings. If omitted, defaults to
            encoding=linear16 and sample_rate=24000. Higher sample rates like
            44100 Hz provide better audio quality.
        output:
          $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAudioOutput
          description: Audio output configuration settings
      title: ChannelsAgentV1MessagesAgentV1SettingsAudio
    ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0ContextMessagesItemsOneOf0Role:
      type: string
      enum:
        - user
        - assistant
      description: Identifies who spoke the statement
      title: >-
        ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0ContextMessagesItemsOneOf0Role
    ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0ContextMessagesItems0:
      type: object
      properties:
        type:
          type: string
          enum:
            - History
          description: Message type identifier for conversation text
        role:
          $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0ContextMessagesItemsOneOf0Role
          description: Identifies who spoke the statement
        content:
          type: string
          description: The actual statement that was spoken
      required:
        - type
        - role
        - content
      description: Conversation text as part of the conversation history
      title: ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0ContextMessagesItems0
    ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0ContextMessagesItemsOneOf1FunctionCallsItems:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the function call
        name:
          type: string
          description: Name of the function called
        client_side:
          type: boolean
          description: Indicates if the call was client-side or server-side
        arguments:
          type: string
          description: Arguments passed to the function
        response:
          type: string
          description: Response from the function call
        thought_signature:
          type: string
          description: >-
            Some Gemini models require this as an additional function call
            identifier
      required:
        - id
        - name
        - client_side
        - arguments
        - response
      title: >-
        ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0ContextMessagesItemsOneOf1FunctionCallsItems
    ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0ContextMessagesItems1:
      type: object
      properties:
        type:
          type: string
          enum:
            - History
        function_calls:
          type: array
          items:
            $ref: >-
              #/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0ContextMessagesItemsOneOf1FunctionCallsItems
          description: List of function call objects
      required:
        - type
        - function_calls
      description: >-
        Client-side or server-side function call request and response as part of
        the conversation history
      title: ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0ContextMessagesItems1
    ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0ContextMessagesItems:
      oneOf:
        - $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0ContextMessagesItems0
        - $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0ContextMessagesItems1
      description: A history message is either a conversational message or a function call
      title: ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0ContextMessagesItems
    ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0Context:
      type: object
      properties:
        messages:
          type: array
          items:
            $ref: >-
              #/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0ContextMessagesItems
          description: Conversation history as a list of messages and function calls
      description: >-
        Conversation context including the history of messages and function
        calls
      title: ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0Context
    DeepgramListenProviderV1:
      type: object
      properties:
        type:
          type: string
          enum:
            - deepgram
          description: Provider type for speech-to-text
        version:
          type: string
          enum:
            - v1
          description: Specifies usage of the V1 Deepgram speech-to-text API
        model:
          type: string
          description: >-
            Model to use for speech to text using the V1 API (e.g. Nova-3,
            Nova-2)
        language:
          type: string
          default: en-US
          description: >-
            Language code to use for speech-to-text. Can be a BCP-47 language
            tag (e.g. `en`), or `multi` for code-switching transcription
        keyterms:
          type: array
          items:
            type: string
          description: Prompt keyterm recognition to improve Keyword Recall Rate
        smart_format:
          type: boolean
          default: false
          description: Applies smart formatting to improve transcript readability
      required:
        - type
      title: DeepgramListenProviderV1
    DeepgramListenProviderV2:
      type: object
      properties:
        type:
          type: string
          enum:
            - deepgram
          description: Provider type for speech-to-text
        version:
          type: string
          enum:
            - v2
          description: Specifies usage of the V2 Deepgram speech-to-text API (e.g. Flux)
        model:
          type: string
          description: >-
            Model to use for speech to text using the V2 API (e.g.
            flux-general-en, flux-general-multi)
        language_hints:
          type: array
          items:
            type: string
          description: >-
            An array of one or more BCP-47 language codes to bias the model
            toward specific languages. Only supported when model is
            flux-general-multi. Without hints, the model auto-detects the spoken
            language. See the Language Prompting guide for details.
        eot_threshold:
          type: number
          format: double
          description: >-
            End-of-turn confidence required to finish a turn. Valid range: 0.5 -
            1.0. Defaults to 0.7. Set to 1.0 to fully suppress confidence-based
            end-of-turn detection. `eot_timeout_ms` still ends idle turns;
            increase it when using ForceEndTurn for full manual turn control.
        eager_eot_threshold:
          type: number
          format: double
          description: >-
            End-of-turn confidence required to fire an eager end-of-turn event.
            When set, enables EagerEndOfTurn and TurnResumed events. Valid
            range: 0.3 - 0.9.
        eot_timeout_ms:
          type: integer
          description: >-
            A turn will be finished when this much time in milliseconds has
            passed after speech, regardless of EOT confidence. Defaults to 5000.
        keyterms:
          type: array
          items:
            type: string
          description: Prompt keyterm recognition to improve Keyword Recall Rate
      required:
        - type
        - model
      title: DeepgramListenProviderV2
    ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0ListenProvider:
      oneOf:
        - $ref: '#/components/schemas/DeepgramListenProviderV1'
        - $ref: '#/components/schemas/DeepgramListenProviderV2'
      title: ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0ListenProvider
    ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0Listen:
      type: object
      properties:
        provider:
          $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0ListenProvider
      title: ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0Listen
    OpenAiThinkProviderVersion:
      type: string
      enum:
        - v1
      description: The REST API version for the OpenAI chat completions API
      title: OpenAiThinkProviderVersion
    OpenAiThinkProviderModel:
      type: string
      enum:
        - gpt-5
        - gpt-5-mini
        - gpt-5-nano
        - gpt-4.1
        - gpt-4.1-mini
        - gpt-4.1-nano
        - gpt-4o
        - gpt-4o-mini
      description: OpenAI model to use
      title: OpenAiThinkProviderModel
    OpenAiThinkProviderReasoningMode:
      type: string
      enum:
        - none
        - minimal
        - low
        - medium
        - high
      description: OpenAI reasoning_effort
      title: OpenAiThinkProviderReasoningMode
    OpenAiThinkProvider:
      type: object
      properties:
        type:
          type: string
          enum:
            - open_ai
        version:
          $ref: '#/components/schemas/OpenAiThinkProviderVersion'
          description: The REST API version for the OpenAI chat completions API
        model:
          $ref: '#/components/schemas/OpenAiThinkProviderModel'
          description: OpenAI model to use
        temperature:
          type: number
          format: double
          minimum: 0
          maximum: 2
          description: OpenAI temperature (0-2)
        reasoning_mode:
          $ref: '#/components/schemas/OpenAiThinkProviderReasoningMode'
          description: OpenAI reasoning_effort
      required:
        - type
        - model
      title: OpenAiThinkProvider
    AwsBedrockThinkProviderModel:
      type: string
      enum:
        - anthropic/claude-3-5-sonnet-20240620-v1:0
        - anthropic/claude-3-5-haiku-20240307-v1:0
      description: AWS Bedrock model to use
      title: AwsBedrockThinkProviderModel
    AwsBedrockThinkProviderCredentialsType:
      type: string
      enum:
        - sts
        - iam
      description: AWS credentials type (STS short-lived or IAM long-lived)
      title: AwsBedrockThinkProviderCredentialsType
    AwsBedrockThinkProviderCredentials:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/AwsBedrockThinkProviderCredentialsType'
          description: AWS credentials type (STS short-lived or IAM long-lived)
        region:
          type: string
          description: AWS region
        access_key_id:
          type: string
          description: AWS access key
        secret_access_key:
          type: string
          description: AWS secret access key
        session_token:
          type: string
          description: AWS session token (required for STS only)
      description: AWS credentials type (STS short-lived or IAM long-lived)
      title: AwsBedrockThinkProviderCredentials
    AwsBedrockThinkProvider:
      type: object
      properties:
        type:
          type: string
          enum:
            - aws_bedrock
        model:
          $ref: '#/components/schemas/AwsBedrockThinkProviderModel'
          description: AWS Bedrock model to use
        temperature:
          type: number
          format: double
          minimum: 0
          maximum: 2
          description: AWS Bedrock temperature (0-2)
        credentials:
          $ref: '#/components/schemas/AwsBedrockThinkProviderCredentials'
          description: AWS credentials type (STS short-lived or IAM long-lived)
      required:
        - type
        - model
      title: AwsBedrockThinkProvider
    AnthropicThinkProviderVersion:
      type: string
      enum:
        - v1
      description: The REST API version for the Anthropic Messages API
      title: AnthropicThinkProviderVersion
    AnthropicThinkProviderModel:
      type: string
      enum:
        - claude-3-5-haiku-latest
        - claude-sonnet-4-20250514
      description: Anthropic model to use
      title: AnthropicThinkProviderModel
    AnthropicThinkProvider:
      type: object
      properties:
        type:
          type: string
          enum:
            - anthropic
        version:
          $ref: '#/components/schemas/AnthropicThinkProviderVersion'
          description: The REST API version for the Anthropic Messages API
        model:
          $ref: '#/components/schemas/AnthropicThinkProviderModel'
          description: Anthropic model to use
        temperature:
          type: number
          format: double
          minimum: 0
          maximum: 1
          description: Anthropic temperature (0-1)
      required:
        - type
        - model
      title: AnthropicThinkProvider
    GoogleThinkProviderVersion:
      type: string
      enum:
        - ai-studio-v1beta
        - gemini-enterprise-agent-v1
        - v1beta
      description: >-
        The Google API used for the request: ai-studio-v1beta for the AI Studio
        API, or gemini-enterprise-agent-v1 for the Gemini Enterprise Agent (GEA)
        API. v1beta is accepted as an alias for ai-studio-v1beta. Defaults based
        on the Deepgram Voice Agent endpoint you connect to.
      title: GoogleThinkProviderVersion
    GoogleThinkProviderModel:
      type: string
      enum:
        - gemini-2.0-flash
        - gemini-2.0-flash-lite
        - gemini-2.5-flash
      description: Google model to use
      title: GoogleThinkProviderModel
    GoogleThinkProvider:
      type: object
      properties:
        type:
          type: string
          enum:
            - google
        version:
          $ref: '#/components/schemas/GoogleThinkProviderVersion'
          description: >-
            The Google API used for the request: ai-studio-v1beta for the AI
            Studio API, or gemini-enterprise-agent-v1 for the Gemini Enterprise
            Agent (GEA) API. v1beta is accepted as an alias for
            ai-studio-v1beta. Defaults based on the Deepgram Voice Agent
            endpoint you connect to.
        model:
          $ref: '#/components/schemas/GoogleThinkProviderModel'
          description: Google model to use
        temperature:
          type: number
          format: double
          minimum: 0
          maximum: 2
          description: Google temperature (0-2)
      required:
        - type
        - model
      title: GoogleThinkProvider
    GroqThinkProviderVersion:
      type: string
      enum:
        - v1
      description: >-
        The REST API version for the Groq's chat completions API (mostly
        OpenAI-compatible)
      title: GroqThinkProviderVersion
    GroqThinkProviderModel:
      type: string
      enum:
        - openai/gpt-oss-20b
      description: Groq model to use
      title: GroqThinkProviderModel
    GroqThinkProviderReasoningMode:
      type: string
      enum:
        - none
        - minimal
        - low
        - medium
        - high
      description: OpenAI reasoning_effort
      title: GroqThinkProviderReasoningMode
    GroqThinkProvider:
      type: object
      properties:
        type:
          type: string
          enum:
            - groq
        version:
          $ref: '#/components/schemas/GroqThinkProviderVersion'
          description: >-
            The REST API version for the Groq's chat completions API (mostly
            OpenAI-compatible)
        model:
          $ref: '#/components/schemas/GroqThinkProviderModel'
          description: Groq model to use
        temperature:
          type: number
          format: double
          minimum: 0
          maximum: 2
          description: Groq temperature (0-2)
        reasoning_mode:
          $ref: '#/components/schemas/GroqThinkProviderReasoningMode'
          description: OpenAI reasoning_effort
      required:
        - type
        - model
      title: GroqThinkProvider
    DeepgramThinkProviderModel:
      type: string
      enum:
        - think-fast
        - phonellm-mini-alpha-2-fp8
      description: >-
        Deepgram language model to use. Early Access. think-fast requires the
        Model Improvement Program: a session with mip_opt_out set to true is
        rejected with INVALID_SETTINGS. Use phonellm-mini-alpha-2-fp8 for
        sessions that opt out.
      title: DeepgramThinkProviderModel
    DeepgramThinkProviderVersion:
      type: string
      enum:
        - v1
      default: v1
      description: API version for the Deepgram think provider. Defaults to `v1`.
      title: DeepgramThinkProviderVersion
    DeepgramThinkProviderReasoningMode:
      type: string
      enum:
        - none
        - minimal
        - low
        - medium
        - high
      description: >-
        Reasoning effort. For phonellm-mini-alpha-2-fp8, use none or omit it;
        other values put reasoning text in the reply, which the agent speaks.
      title: DeepgramThinkProviderReasoningMode
    DeepgramThinkProvider:
      type: object
      properties:
        type:
          type: string
          enum:
            - deepgram
          description: >-
            Provider type for Deepgram-hosted language models. Must be
            `deepgram`.
        model:
          $ref: '#/components/schemas/DeepgramThinkProviderModel'
          description: >-
            Deepgram language model to use. Early Access. think-fast requires
            the Model Improvement Program: a session with mip_opt_out set to
            true is rejected with INVALID_SETTINGS. Use
            phonellm-mini-alpha-2-fp8 for sessions that opt out.
        version:
          $ref: '#/components/schemas/DeepgramThinkProviderVersion'
          default: v1
          description: API version for the Deepgram think provider. Defaults to `v1`.
        temperature:
          type: number
          format: double
          minimum: 0
          maximum: 2
          description: Deepgram temperature (0-2).
        reasoning_mode:
          $ref: '#/components/schemas/DeepgramThinkProviderReasoningMode'
          description: >-
            Reasoning effort. For phonellm-mini-alpha-2-fp8, use none or omit
            it; other values put reasoning text in the reply, which the agent
            speaks.
        voice_prompt_opt_out:
          type: boolean
          default: false
          description: >-
            With think-fast, Deepgram places spoken-style instructions ahead of
            your prompt and sends a VOICE_PROMPT_ADDED warning. Set to true to
            send your prompt unchanged.
      required:
        - type
        - model
      description: Deepgram-hosted language models for the Voice Agent think stage.
      title: DeepgramThinkProvider
    ThinkSettingsV1Provider:
      oneOf:
        - $ref: '#/components/schemas/OpenAiThinkProvider'
        - $ref: '#/components/schemas/AwsBedrockThinkProvider'
        - $ref: '#/components/schemas/AnthropicThinkProvider'
        - $ref: '#/components/schemas/GoogleThinkProvider'
        - $ref: '#/components/schemas/GroqThinkProvider'
        - $ref: '#/components/schemas/DeepgramThinkProvider'
      title: ThinkSettingsV1Provider
    ThinkSettingsV1Endpoint:
      type: object
      properties:
        url:
          type: string
          description: Custom LLM endpoint URL
        headers:
          type: object
          additionalProperties:
            type: string
          description: Custom headers for the endpoint
      description: >
        Optional for non-Deepgram LLM providers. When present, must include url
        field and headers object
      title: ThinkSettingsV1Endpoint
    ThinkSettingsV1FunctionsItemsParameters:
      type: object
      properties: {}
      description: Function parameters
      title: ThinkSettingsV1FunctionsItemsParameters
    ThinkSettingsV1FunctionsItemsEndpoint:
      type: object
      properties:
        url:
          type: string
          description: Endpoint URL
        method:
          type: string
          description: HTTP method
        headers:
          type: object
          additionalProperties:
            type: string
      description: >-
        The Function endpoint to call. if not passed, function is called
        client-side
      title: ThinkSettingsV1FunctionsItemsEndpoint
    ThinkSettingsV1FunctionsItems:
      type: object
      properties:
        name:
          type: string
          description: Function name
        description:
          type: string
          description: Function description
        parameters:
          $ref: '#/components/schemas/ThinkSettingsV1FunctionsItemsParameters'
          description: Function parameters
        defer_until_eot:
          type: boolean
          default: false
          description: >-
            Hold this function call until the user's turn is confirmed instead
            of dispatching it speculatively. Set it to true for actions that
            cannot be undone. If the turn resumes, a deferred call is discarded
            before it runs. Defaults to false
        initial_agent_filler:
          type: boolean
          default: false
          description: >-
            Requires `agent.think_live`. Speak one short filler line after the
            function is dispatched and the user's turn is confirmed, if the
            function response has not yet arrived. Skipped when the reasoning
            LLM already announced the call in the same response
        agent_filler_max_count:
          type: integer
          minimum: 0
          default: 0
          description: >-
            Requires `agent.think_live`. Number of additional filler lines the
            agent may speak while this function call is outstanding. Set to 0 to
            disable additional filler
        agent_filler_interval_ms:
          type: integer
          minimum: 1000
          maximum: 60000
          default: 5000
          description: >-
            Requires `agent.think_live`. Silence in milliseconds, counted from
            when the agent last stopped speaking, before each additional filler
            line. Ignored when `agent_filler_max_count` is 0, which is also the
            only case in which a value outside the 1000 to 60000 range is
            accepted. Setting any filler field without `agent.think_live`, or an
            out-of-range interval while `agent_filler_max_count` is greater than
            0, returns an `INVALID_SETTINGS` error and closes the session
        endpoint:
          $ref: '#/components/schemas/ThinkSettingsV1FunctionsItemsEndpoint'
          description: >-
            The Function endpoint to call. if not passed, function is called
            client-side
      title: ThinkSettingsV1FunctionsItems
    ThinkSettingsV1ContextLength0:
      type: string
      enum:
        - max
      description: Agent will not discard context regardless of length
      title: ThinkSettingsV1ContextLength0
    ThinkSettingsV1ContextLength:
      oneOf:
        - $ref: '#/components/schemas/ThinkSettingsV1ContextLength0'
        - type: number
          format: double
          minimum: 2
      description: >
        Specifies the number of characters retained in context between user
        messages, agent responses, and function calls. This setting is only
        configurable when a custom think endpoint is used
      title: ThinkSettingsV1ContextLength
    ThinkSettingsV1:
      type: object
      properties:
        provider:
          $ref: '#/components/schemas/ThinkSettingsV1Provider'
        endpoint:
          $ref: '#/components/schemas/ThinkSettingsV1Endpoint'
          description: >
            Optional for non-Deepgram LLM providers. When present, must include
            url field and headers object
        functions:
          type: array
          items:
            $ref: '#/components/schemas/ThinkSettingsV1FunctionsItems'
        prompt:
          type: string
        context_length:
          $ref: '#/components/schemas/ThinkSettingsV1ContextLength'
          description: >
            Specifies the number of characters retained in context between user
            messages, agent responses, and function calls. This setting is only
            configurable when a custom think endpoint is used
      required:
        - provider
      title: ThinkSettingsV1
    ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0Think1:
      type: array
      items:
        $ref: '#/components/schemas/ThinkSettingsV1'
      title: ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0Think1
    ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0Think:
      oneOf:
        - $ref: '#/components/schemas/ThinkSettingsV1'
        - $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0Think1
      description: >-
        Your reasoning LLM. With Think Live on, this is the reasoning half of
        the pair, running alongside the Think Live model configured in
        `think_live`
      title: ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0Think
    DeepgramThinkLiveProviderV1:
      type: object
      properties:
        type:
          type: string
          enum:
            - deepgram
          description: Provider type for the Think Live model. Must be `deepgram`
        version:
          type: string
          enum:
            - v1
          description: Version of the Deepgram Think Live model. Must be `v1`
        agent_backchannel_sensitivity:
          type: number
          format: double
          minimum: 0
          maximum: 1
          default: 0.73
          description: >-
            Probability of the agent producing backchannel responses (such as
            "mhmm") while the user is speaking. Higher values produce more
            backchanneling. Set to 0 to disable agent backchannels
        presence_check_max_count:
          type: integer
          minimum: 0
          default: 3
          description: >-
            Maximum number of times the agent prompts the user after extended
            silence. Once reached, the agent stays silent. Set to 0 to disable
            presence checks
        presence_check_interval_ms:
          type: integer
          minimum: 1
          maximum: 60000
          default: 4500
          description: >-
            Time in milliseconds the agent waits between presence-check prompts.
            The first prompt is floored at 3000, so values below that behave as
            3000. Ignored when `presence_check_max_count` is 0
        frustration_max_count:
          type: integer
          minimum: 0
          description: >-
            Number of `FrustrationDetected` events sent before `escalated`
            becomes true. Set to 0 to stop `FrustrationDetected` events from
            being sent. Omit it to use the server default
        restricted_terms:
          type: array
          items:
            type: string
          default:
            - human
            - transfer
          description: >-
            Terms the Think Live model will not say. Pass a multi-word phrase as
            a single array element. Applies to the Think Live model only, not to
            your reasoning LLM
      required:
        - type
        - version
      description: >-
        Deepgram's Think Live model, which runs alongside your reasoning LLM to
        handle backchanneling, presence checks, and frustration detection. Only
        the Deepgram provider is supported.
      title: DeepgramThinkLiveProviderV1
    ThinkLiveSettingsV1:
      type: object
      properties:
        provider:
          $ref: '#/components/schemas/DeepgramThinkLiveProviderV1'
      required:
        - provider
      description: >-
        Configures Deepgram's Think Live model. Think Live is off until this
        object is provided
      title: ThinkLiveSettingsV1
    DeepgramSpeakProviderModel:
      type: string
      enum:
        - aura-asteria-en
        - aura-luna-en
        - aura-stella-en
        - aura-athena-en
        - aura-hera-en
        - aura-orion-en
        - aura-arcas-en
        - aura-perseus-en
        - aura-angus-en
        - aura-orpheus-en
        - aura-helios-en
        - aura-zeus-en
        - aura-2-amalthea-en
        - aura-2-andromeda-en
        - aura-2-apollo-en
        - aura-2-arcas-en
        - aura-2-aries-en
        - aura-2-asteria-en
        - aura-2-athena-en
        - aura-2-atlas-en
        - aura-2-aurora-en
        - aura-2-callista-en
        - aura-2-cora-en
        - aura-2-cordelia-en
        - aura-2-delia-en
        - aura-2-draco-en
        - aura-2-electra-en
        - aura-2-harmonia-en
        - aura-2-helena-en
        - aura-2-hera-en
        - aura-2-hermes-en
        - aura-2-hyperion-en
        - aura-2-iris-en
        - aura-2-janus-en
        - aura-2-juno-en
        - aura-2-jupiter-en
        - aura-2-luna-en
        - aura-2-mars-en
        - aura-2-minerva-en
        - aura-2-neptune-en
        - aura-2-odysseus-en
        - aura-2-ophelia-en
        - aura-2-orion-en
        - aura-2-orpheus-en
        - aura-2-pandora-en
        - aura-2-phoebe-en
        - aura-2-pluto-en
        - aura-2-saturn-en
        - aura-2-selene-en
        - aura-2-thalia-en
        - aura-2-theia-en
        - aura-2-vesta-en
        - aura-2-zeus-en
        - aura-2-sirio-es
        - aura-2-nestor-es
        - aura-2-carina-es
        - aura-2-celeste-es
        - aura-2-alvaro-es
        - aura-2-diana-es
        - aura-2-aquila-es
        - aura-2-selena-es
        - aura-2-estrella-es
        - aura-2-javier-es
        - flux-alexis-en
        - flux-bree-en
        - flux-brittany-en
        - flux-brooke-en
        - flux-bruce-en
        - flux-cliff-en
        - flux-cole-en
        - flux-colin-en
        - flux-conor-en
        - flux-donovan-en
        - flux-drew-en
        - flux-elise-en
        - flux-gemma-en
        - flux-haley-en
        - flux-hannah-en
        - flux-heather-en
        - flux-jack-en
        - flux-kai-en
        - flux-kelsey-en
        - flux-kit-en
        - flux-maeve-en
        - flux-marcelo-en
        - flux-marcus-en
        - flux-meena-en
        - flux-meghan-en
        - flux-miles-en
        - flux-naveen-en
        - flux-paige-en
        - flux-priya-en
        - flux-rufus-en
        - flux-sean-en
        - flux-sharon-en
        - flux-sienna-en
        - flux-tanner-en
        - flux-wade-en
        - flux-wes-en
        - flux-anouk-nl
        - flux-bram-nl
        - flux-fleur-nl
        - flux-irene-nl
        - flux-luuk-nl
        - flux-monique-nl
        - flux-ruben-nl
        - flux-sanne-nl
        - flux-yvonne-nl
        - flux-dirk-nl
        - flux-lotte-nl
        - flux-niels-nl
        - flux-veerle-nl
        - flux-arnaud-fr
        - flux-benoit-fr
        - flux-brigitte-fr
        - flux-camille-fr
        - flux-chloe-fr
        - flux-florian-fr
        - flux-julien-fr
        - flux-mathieu-fr
        - flux-pierre-fr
        - flux-thierry-fr
        - flux-veronique-fr
        - flux-yasmine-fr
        - flux-benjamin-de
        - flux-christian-de
        - flux-janine-de
        - flux-magdalena-de
        - flux-moritz-de
        - flux-nadine-de
        - flux-rolf-de
        - flux-sonja-de
        - flux-sven-de
        - flux-tobias-de
        - flux-verena-de
        - flux-leonie-de
        - flux-yannick-de
        - flux-ajay-hi
        - flux-anjali-hi
        - flux-arjun-hi
        - flux-divya-hi
        - flux-jyoti-hi
        - flux-nikhil-hi
        - flux-pallavi-hi
        - flux-prachi-hi
        - flux-rahul-hi
        - flux-rajesh-hi
        - flux-ritu-hi
        - flux-shreya-hi
        - flux-sunita-hi
        - flux-vikram-hi
        - flux-angela-it
        - flux-chiara-it
        - flux-federico-it
        - flux-giorgio-it
        - flux-matteo-it
        - flux-paola-it
        - flux-rocco-it
        - flux-sofia-it
        - flux-stefano-it
        - flux-vincenzo-it
        - flux-vito-it
        - flux-ayumi-ja
        - flux-hayato-ja
        - flux-nozomi-ja
        - flux-sayaka-ja
        - flux-bianca-pt
        - flux-bruno-pt
        - flux-claudia-pt
        - flux-leandro-pt
        - flux-marcia-pt
        - flux-mariana-pt
        - flux-marta-pt
        - flux-mateus-pt
        - flux-miguel-pt
        - flux-renato-pt
        - flux-roberto-pt
        - flux-rodrigo-pt
        - flux-artur-pt
        - flux-benedita-pt
        - flux-catarina-pt
        - flux-hugo-pt
        - flux-pedro-pt
        - flux-ricardo-pt
        - flux-andrei-ru
        - flux-kirill-ru
        - flux-maxim-ru
        - flux-mikhail-ru
        - flux-natalia-ru
        - flux-nikolai-ru
        - flux-olga-ru
        - flux-polina-ru
        - flux-vladimir-ru
        - flux-aina-es
        - flux-alfredo-es
        - flux-carmen-es
        - flux-cecilia-es
        - flux-duvan-es
        - flux-eduardo-es
        - flux-ernesto-es
        - flux-fernanda-es
        - flux-fiorella-es
        - flux-gustavo-es
        - flux-jaime-es
        - flux-martin-es
        - flux-mauricio-es
        - flux-patricia-es
        - flux-pilar-es
        - flux-rafael-es
        - flux-tomas-es
        - flux-valentina-es
        - flux-ysabel-es
        - flux-afsana-bn
        - flux-ishrat-bn
        - flux-mamun-bn
        - flux-sabbir-bn
        - flux-shuvo-bn
        - flux-sumaiya-bn
        - flux-desislava-bg
        - flux-gergana-bg
        - flux-jordi-ca
        - flux-judit-ca
        - flux-bo-zh
        - flux-haoran-zh
        - flux-jian-zh
        - flux-jie-zh
        - flux-lijuan-zh
        - flux-shufen-zh
        - flux-wenbo-zh
        - flux-wenjing-zh
        - flux-zhen-zh
        - flux-chiaying-zh
        - flux-kuanyu-zh
        - flux-yawen-zh
        - flux-yuting-zh
        - flux-manlok-zh
        - flux-dalibor-hr
        - flux-danijela-hr
        - flux-domagoj-hr
        - flux-jasna-hr
        - flux-josipa-hr
        - flux-mihaela-hr
        - flux-vedran-hr
        - flux-jakub-cs
        - flux-pernille-da
        - flux-rasmus-da
        - flux-rikke-da
        - flux-triin-et
        - flux-kirsi-fi
        - flux-teemu-fi
        - flux-kostas-el
        - flux-bhavna-gu
        - flux-hetal-gu
        - flux-jignesh-gu
        - flux-bence-hu
        - flux-eszter-hu
        - flux-kinga-hu
        - flux-tibor-hu
        - flux-dewi-id
        - flux-fajar-id
        - flux-fitri-id
        - flux-rizky-id
        - flux-teguh-id
        - flux-manjunath-kn
        - flux-eunji-ko
        - flux-hyunwoo-ko
        - flux-mikyung-ko
        - flux-minjun-ko
        - flux-soojin-ko
        - flux-sungmin-ko
        - flux-agnese-lv
        - flux-edgars-lv
        - flux-goda-lt
        - flux-neringa-lt
        - flux-haziq-ms
        - flux-izzah-ms
        - flux-pooja-mr
        - flux-pratik-mr
        - flux-sneha-mr
        - flux-erlend-no
        - flux-espen-no
        - flux-ida-no
        - flux-signe-no
        - flux-silje-no
        - flux-vegard-no
        - flux-bartosz-pl
        - flux-ewa-pl
        - flux-justyna-pl
        - flux-kacper-pl
        - flux-konrad-pl
        - flux-zuzanna-pl
        - flux-cosmin-ro
        - flux-ioana-ro
        - flux-dominika-sk
        - flux-juraj-sk
        - flux-gregor-sl
        - flux-katja-sl
        - flux-axel-sv
        - flux-charlotta-sv
        - flux-frida-sv
        - flux-ludvig-sv
        - flux-oskar-sv
        - flux-pontus-sv
        - flux-wilma-sv
        - flux-jerome-tl
        - flux-jomar-tl
        - flux-liezel-tl
        - flux-noel-tl
        - flux-trisha-tl
        - flux-gokul-ta
        - flux-kavya-ta
        - flux-sowmya-ta
        - flux-vinoth-ta
        - flux-pavan-te
        - flux-ravi-te
        - flux-sravani-te
        - flux-dilek-tr
        - flux-ecem-tr
        - flux-emre-tr
        - flux-gizem-tr
        - flux-mehmet-tr
        - flux-serkan-tr
        - flux-zeynep-tr
        - flux-denys-uk
        - flux-solomiya-uk
        - flux-ambreen-ur
        - flux-usman-ur
        - flux-hoa-vi
        - flux-minh-vi
      description: >-
        Deepgram TTS model. Aura models (version v1) use the aura-* voices; Flux
        TTS (version v2) uses the flux-{voice}-{language} voices (e.g.
        flux-alexis-en). Defaults to flux-kit-en when agent.speak is omitted.
      title: DeepgramSpeakProviderModel
    DeepgramSpeakProviderExpressivity:
      type: string
      enum:
        - '-2'
        - '-1'
        - '0'
        - '1'
        - '2'
      description: >-
        Delivery register of the generated speech, on a calm-to-animated axis.
        Flux TTS (version v2) only, on every Flux voice. Accepts the whole
        numbers -2 to 2, where 0 (the default) is the voice's tuned delivery and
        the only value validated for production, -2 the calm end of the range
        and 2 the animated end. Fixed for the session. Beta: behavior may change
        in future model versions, and non-default values increase the risk of
        hallucinations and pronunciation errors. See
        [Expressivity](/docs/tts-expressivity).
      title: DeepgramSpeakProviderExpressivity
    DeepgramSpeakProvider:
      type: object
      properties:
        type:
          type: string
          enum:
            - deepgram
        version:
          type: string
          default: v1
          description: >-
            The Deepgram text-to-speech model family. Accepted values: `v1`
            (Aura, the default) and `v2` (Flux TTS). Use `v1` with an aura-*
            model and `v2` with a flux-* model. Defaults to `v1` when omitted.
        model:
          $ref: '#/components/schemas/DeepgramSpeakProviderModel'
          description: >-
            Deepgram TTS model. Aura models (version v1) use the aura-* voices;
            Flux TTS (version v2) uses the flux-{voice}-{language} voices (e.g.
            flux-alexis-en). Defaults to flux-kit-en when agent.speak is
            omitted.
        speed:
          type: number
          format: double
          minimum: 0.5
          maximum: 1.5
          default: 1
          description: >-
            Speaking rate multiplier that adjusts the pace of generated speech
            while preserving natural prosody and voice quality. Aura (version
            v1) accepts any value from 0.7 to 1.5. Flux TTS (version v2) accepts
            values from 0.5 to 1.5 in 0.05 increments; a value the family does
            not accept ends the session with FAILED_TO_SPEAK. Not yet supported
            in all languages.
        expressivity:
          $ref: '#/components/schemas/DeepgramSpeakProviderExpressivity'
          default: 0
          description: >-
            Delivery register of the generated speech, on a calm-to-animated
            axis. Flux TTS (version v2) only, on every Flux voice. Accepts the
            whole numbers -2 to 2, where 0 (the default) is the voice's tuned
            delivery and the only value validated for production, -2 the calm
            end of the range and 2 the animated end. Fixed for the session.
            Beta: behavior may change in future model versions, and non-default
            values increase the risk of hallucinations and pronunciation errors.
            See [Expressivity](/docs/tts-expressivity).
      required:
        - type
        - model
      description: >-
        Deepgram text-to-speech provider. Aura models use version v1 (default);
        Flux TTS uses version v2 and a flux-* model. Flux TTS is the default
        when agent.speak is omitted, using the flux-kit-en voice.
      title: DeepgramSpeakProvider
    ElevenLabsSpeakProviderVersion:
      type: string
      enum:
        - v1
      description: The REST API version for the ElevenLabs text-to-speech API
      title: ElevenLabsSpeakProviderVersion
    ElevenLabsSpeakProviderModelId:
      type: string
      enum:
        - eleven_turbo_v2_5
        - eleven_monolingual_v1
        - eleven_multilingual_v2
      description: Eleven Labs model ID
      title: ElevenLabsSpeakProviderModelId
    ElevenLabsSpeakProvider:
      type: object
      properties:
        type:
          type: string
          enum:
            - eleven_labs
        version:
          $ref: '#/components/schemas/ElevenLabsSpeakProviderVersion'
          description: The REST API version for the ElevenLabs text-to-speech API
        model_id:
          $ref: '#/components/schemas/ElevenLabsSpeakProviderModelId'
          description: Eleven Labs model ID
        language:
          type: string
          description: >-
            Optional language to use, e.g. 'en-US'. Corresponds to the
            `language_code` parameter in the ElevenLabs API
        language_code:
          type: string
          description: Use the `language` field instead.
          deprecated: true
      required:
        - type
        - model_id
      title: ElevenLabsSpeakProvider
    CartesiaSpeakProviderVersion:
      type: string
      enum:
        - '2025-03-17'
      description: The API version header for the Cartesia text-to-speech API
      title: CartesiaSpeakProviderVersion
    CartesiaSpeakProviderModelId:
      type: string
      enum:
        - sonic-2
        - sonic-multilingual
      description: Cartesia model ID
      title: CartesiaSpeakProviderModelId
    CartesiaSpeakProviderVoice:
      type: object
      properties:
        mode:
          type: string
          description: Cartesia voice mode
        id:
          type: string
          description: Cartesia voice ID
      required:
        - mode
        - id
      title: CartesiaSpeakProviderVoice
    CartesiaSpeakProvider:
      type: object
      properties:
        type:
          type: string
          enum:
            - cartesia
        version:
          $ref: '#/components/schemas/CartesiaSpeakProviderVersion'
          description: The API version header for the Cartesia text-to-speech API
        model_id:
          $ref: '#/components/schemas/CartesiaSpeakProviderModelId'
          description: Cartesia model ID
        voice:
          $ref: '#/components/schemas/CartesiaSpeakProviderVoice'
        language:
          type: string
          description: Cartesia language code
        volume:
          type: number
          format: double
          minimum: 0.5
          maximum: 2
          description: >
            Volume level for Cartesia TTS output. Valid range: 0.5 to 2.0. See
            [Cartesia
            documentation](https://docs.cartesia.ai/build-with-cartesia/sonic-3/volume-speed-emotion#volume-speed-and-emotion).
      required:
        - type
        - model_id
        - voice
      title: CartesiaSpeakProvider
    OpenAiSpeakProviderVersion:
      type: string
      enum:
        - v1
      description: The REST API version for the OpenAI text-to-speech API
      title: OpenAiSpeakProviderVersion
    OpenAiSpeakProviderModel:
      type: string
      enum:
        - tts-1
        - tts-1-hd
      description: OpenAI TTS model
      title: OpenAiSpeakProviderModel
    OpenAiSpeakProviderVoice:
      type: string
      enum:
        - alloy
        - echo
        - fable
        - onyx
        - nova
        - shimmer
      description: OpenAI voice
      title: OpenAiSpeakProviderVoice
    OpenAiSpeakProvider:
      type: object
      properties:
        type:
          type: string
          enum:
            - open_ai
        version:
          $ref: '#/components/schemas/OpenAiSpeakProviderVersion'
          description: The REST API version for the OpenAI text-to-speech API
        model:
          $ref: '#/components/schemas/OpenAiSpeakProviderModel'
          description: OpenAI TTS model
        voice:
          $ref: '#/components/schemas/OpenAiSpeakProviderVoice'
          description: OpenAI voice
      required:
        - type
        - model
        - voice
      title: OpenAiSpeakProvider
    AwsPollySpeakProviderVoice:
      type: string
      enum:
        - Matthew
        - Joanna
        - Amy
        - Emma
        - Brian
        - Arthur
        - Aria
        - Ayanda
      description: AWS Polly voice name
      title: AwsPollySpeakProviderVoice
    AwsPollySpeakProviderEngine:
      type: string
      enum:
        - generative
        - long-form
        - standard
        - neural
      title: AwsPollySpeakProviderEngine
    AwsPollySpeakProviderCredentialsType:
      type: string
      enum:
        - sts
        - iam
      title: AwsPollySpeakProviderCredentialsType
    AwsPollySpeakProviderCredentials:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/AwsPollySpeakProviderCredentialsType'
        region:
          type: string
        access_key_id:
          type: string
        secret_access_key:
          type: string
        session_token:
          type: string
          description: Required for STS only
      required:
        - type
        - region
        - access_key_id
        - secret_access_key
      title: AwsPollySpeakProviderCredentials
    AwsPollySpeakProvider:
      type: object
      properties:
        type:
          type: string
          enum:
            - aws_polly
        voice:
          $ref: '#/components/schemas/AwsPollySpeakProviderVoice'
          description: AWS Polly voice name
        language:
          type: string
          description: >-
            Language code to use, e.g. 'en-US'. Corresponds to the
            `language_code` parameter in the AWS Polly API
        language_code:
          type: string
          description: Use the `language` field instead.
          deprecated: true
        engine:
          $ref: '#/components/schemas/AwsPollySpeakProviderEngine'
        credentials:
          $ref: '#/components/schemas/AwsPollySpeakProviderCredentials'
      required:
        - type
        - voice
        - language
        - engine
        - credentials
      title: AwsPollySpeakProvider
    SpeakSettingsV1Provider:
      oneOf:
        - $ref: '#/components/schemas/DeepgramSpeakProvider'
        - $ref: '#/components/schemas/ElevenLabsSpeakProvider'
        - $ref: '#/components/schemas/CartesiaSpeakProvider'
        - $ref: '#/components/schemas/OpenAiSpeakProvider'
        - $ref: '#/components/schemas/AwsPollySpeakProvider'
      title: SpeakSettingsV1Provider
    SpeakSettingsV1Endpoint:
      type: object
      properties:
        url:
          type: string
          description: >
            Custom TTS endpoint URL. Cannot contain `output_format` or
            `model_id` query parameters when the provider is Eleven Labs.
        headers:
          type: object
          additionalProperties:
            type: string
      description: >
        Optional if provider is Deepgram. Required for non-Deepgram TTS
        providers.

        When present, must include url field and headers object. Valid schemes
        are https and wss with wss only supported for Eleven Labs.
      title: SpeakSettingsV1Endpoint
    SpeakSettingsV1:
      type: object
      properties:
        provider:
          $ref: '#/components/schemas/SpeakSettingsV1Provider'
        endpoint:
          $ref: '#/components/schemas/SpeakSettingsV1Endpoint'
          description: >
            Optional if provider is Deepgram. Required for non-Deepgram TTS
            providers.

            When present, must include url field and headers object. Valid
            schemes are https and wss with wss only supported for Eleven Labs.
      required:
        - provider
      title: SpeakSettingsV1
    ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0Speak1:
      type: array
      items:
        $ref: '#/components/schemas/SpeakSettingsV1'
      title: ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0Speak1
    ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0Speak:
      oneOf:
        - $ref: '#/components/schemas/SpeakSettingsV1'
        - $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0Speak1
      title: ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0Speak
    ChannelsAgentV1MessagesAgentV1SettingsAgent0:
      type: object
      properties:
        language:
          type: string
          default: en
          description: >-
            Deprecated. Use `listen.provider.language` and
            `speak.provider.language` fields instead.
          deprecated: true
        context:
          $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0Context
          description: >-
            Conversation context including the history of messages and function
            calls
        listen:
          $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0Listen
        think:
          $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0Think
          description: >-
            Your reasoning LLM. With Think Live on, this is the reasoning half
            of the pair, running alongside the Think Live model configured in
            `think_live`
        think_live:
          $ref: '#/components/schemas/ThinkLiveSettingsV1'
        speak:
          $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAgentOneOf0Speak
        greeting:
          type: string
          description: Optional message that agent will speak at the start
      title: ChannelsAgentV1MessagesAgentV1SettingsAgent0
    ChannelsAgentV1MessagesAgentV1SettingsAgent:
      oneOf:
        - $ref: '#/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAgent0'
        - type: string
          format: uuid
      title: ChannelsAgentV1MessagesAgentV1SettingsAgent
    AgentV1_AgentV1Settings:
      type: object
      properties:
        type:
          type: string
          enum:
            - Settings
        tags:
          type: array
          items:
            type: string
          description: Tags to associate with the request
        experimental:
          type: boolean
          default: false
          description: To enable experimental features
        flags:
          $ref: '#/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsFlags'
        mip_opt_out:
          type: boolean
          default: false
          description: To opt out of Deepgram Model Improvement Program
        audio:
          $ref: '#/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAudio'
        agent:
          $ref: '#/components/schemas/ChannelsAgentV1MessagesAgentV1SettingsAgent'
      required:
        - type
        - audio
        - agent
      title: AgentV1_AgentV1Settings
    ChannelsAgentV1MessagesAgentV1UpdateListenListenProvider:
      oneOf:
        - $ref: '#/components/schemas/DeepgramListenProviderV1'
        - $ref: '#/components/schemas/DeepgramListenProviderV2'
      title: ChannelsAgentV1MessagesAgentV1UpdateListenListenProvider
    ChannelsAgentV1MessagesAgentV1UpdateListenListen:
      type: object
      properties:
        provider:
          $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1UpdateListenListenProvider
      required:
        - provider
      description: >-
        Listen configuration to update. Contains a provider object with the same
        schema as Settings. The model and language can be changed mid-session.
        Keyterms can only be updated mid-session for Flux models.
      title: ChannelsAgentV1MessagesAgentV1UpdateListenListen
    AgentV1_AgentV1UpdateListen:
      type: object
      properties:
        type:
          type: string
          enum:
            - UpdateListen
          description: Message type identifier for updating the listen configuration
        listen:
          $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1UpdateListenListen
          description: >-
            Listen configuration to update. Contains a provider object with the
            same schema as Settings. The model and language can be changed
            mid-session. Keyterms can only be updated mid-session for Flux
            models.
      required:
        - type
        - listen
      title: AgentV1_AgentV1UpdateListen
    ChannelsAgentV1MessagesAgentV1UpdateThinkThink1:
      type: array
      items:
        $ref: '#/components/schemas/ThinkSettingsV1'
      title: ChannelsAgentV1MessagesAgentV1UpdateThinkThink1
    ChannelsAgentV1MessagesAgentV1UpdateThinkThink:
      oneOf:
        - $ref: '#/components/schemas/ThinkSettingsV1'
        - $ref: '#/components/schemas/ChannelsAgentV1MessagesAgentV1UpdateThinkThink1'
      title: ChannelsAgentV1MessagesAgentV1UpdateThinkThink
    AgentV1_AgentV1UpdateThink:
      type: object
      properties:
        type:
          type: string
          enum:
            - UpdateThink
          description: Message type identifier for updating the think model
        think:
          $ref: '#/components/schemas/ChannelsAgentV1MessagesAgentV1UpdateThinkThink'
      required:
        - type
        - think
      title: AgentV1_AgentV1UpdateThink
    AgentV1_AgentV1UpdateThinkLive:
      type: object
      properties:
        type:
          type: string
          enum:
            - UpdateThink_Live
          description: >-
            Message type identifier for updating the Think Live model
            configuration
        think_live:
          $ref: '#/components/schemas/ThinkLiveSettingsV1'
      required:
        - type
        - think_live
      title: AgentV1_AgentV1UpdateThinkLive
    ChannelsAgentV1MessagesAgentV1UpdateSpeakSpeak1:
      type: array
      items:
        $ref: '#/components/schemas/SpeakSettingsV1'
      title: ChannelsAgentV1MessagesAgentV1UpdateSpeakSpeak1
    ChannelsAgentV1MessagesAgentV1UpdateSpeakSpeak:
      oneOf:
        - $ref: '#/components/schemas/SpeakSettingsV1'
        - $ref: '#/components/schemas/ChannelsAgentV1MessagesAgentV1UpdateSpeakSpeak1'
      title: ChannelsAgentV1MessagesAgentV1UpdateSpeakSpeak
    AgentV1_AgentV1UpdateSpeak:
      type: object
      properties:
        type:
          type: string
          enum:
            - UpdateSpeak
          description: Message type identifier for updating the speak model
        speak:
          $ref: '#/components/schemas/ChannelsAgentV1MessagesAgentV1UpdateSpeakSpeak'
      required:
        - type
        - speak
      title: AgentV1_AgentV1UpdateSpeak
    AgentV1_AgentV1InjectUserMessage:
      type: object
      properties:
        type:
          type: string
          enum:
            - InjectUserMessage
          description: Message type identifier for injecting a user message
        content:
          type: string
          description: The specific phrase or statement the agent should respond to
      required:
        - type
        - content
      title: AgentV1_AgentV1InjectUserMessage
    ChannelsAgentV1MessagesAgentV1InjectAgentMessageBehavior:
      type: string
      enum:
        - default
        - queue
        - interrupt
      default: default
      description: >
        Controls how the injection interacts with any in-progress user or agent
        turn.


        * `default` — The agent speaks only if neither the user nor the agent is
        mid-turn. If a turn is in progress, the server replies with
        `InjectionRefused`.

        * `queue` — The message is appended after any already-queued
        `ConversationText` without interrupting the current agent turn or think
        response. If nothing is queued, the message plays immediately.

        * `interrupt` — The agent immediately speaks. If the agent was already
        speaking, it interrupts the current speech and replaces it with the new
        message. If the user is speaking, the agent interrupts with the new
        message, but the user's continued speech triggers `UserStartedSpeaking`,
        which quickly interrupts the agent.
      title: ChannelsAgentV1MessagesAgentV1InjectAgentMessageBehavior
    AgentV1_AgentV1InjectAgentMessage:
      type: object
      properties:
        type:
          type: string
          enum:
            - InjectAgentMessage
          description: Message type identifier for injecting an agent message
        message:
          type: string
          description: The statement that the agent should say
        behavior:
          $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1InjectAgentMessageBehavior
          default: default
          description: >
            Controls how the injection interacts with any in-progress user or
            agent turn.


            * `default` — The agent speaks only if neither the user nor the
            agent is mid-turn. If a turn is in progress, the server replies with
            `InjectionRefused`.

            * `queue` — The message is appended after any already-queued
            `ConversationText` without interrupting the current agent turn or
            think response. If nothing is queued, the message plays immediately.

            * `interrupt` — The agent immediately speaks. If the agent was
            already speaking, it interrupts the current speech and replaces it
            with the new message. If the user is speaking, the agent interrupts
            with the new message, but the user's continued speech triggers
            `UserStartedSpeaking`, which quickly interrupts the agent.
      required:
        - type
        - message
      title: AgentV1_AgentV1InjectAgentMessage
    ChannelsAgentV1MessagesAgentV1InjectDynamicAgentMessageBehavior:
      type: string
      enum:
        - default
        - queue
        - interrupt
      default: default
      description: >
        Controls how the injection interacts with any in-progress user or agent
        turn.


        * `default` — The agent speaks only if neither the user nor the agent is
        mid-turn. If a turn is in progress, the server replies with
        `InjectionRefused`.

        * `queue` — The message is appended after any already-queued
        `ConversationText` without interrupting the current agent turn or think
        response. If nothing is queued, the message plays immediately.

        * `interrupt` — The agent immediately speaks. If the agent was already
        speaking, it interrupts the current speech and replaces it with the new
        message. If the user is speaking, the agent interrupts with the new
        message, but the user's continued speech triggers `UserStartedSpeaking`,
        which quickly interrupts the agent.
      title: ChannelsAgentV1MessagesAgentV1InjectDynamicAgentMessageBehavior
    AgentV1_AgentV1InjectDynamicAgentMessage:
      type: object
      properties:
        type:
          type: string
          enum:
            - InjectAgentMessage
          description: Message type identifier for injecting an agent message
        is_dynamic:
          type: boolean
          enum:
            - true
          description: >-
            Must be `true`. The Think Live model generates the line, so no
            `message` is sent
        behavior:
          $ref: >-
            #/components/schemas/ChannelsAgentV1MessagesAgentV1InjectDynamicAgentMessageBehavior
          default: default
          description: >
            Controls how the injection interacts with any in-progress user or
            agent turn.


            * `default` — The agent speaks only if neither the user nor the
            agent is mid-turn. If a turn is in progress, the server replies with
            `InjectionRefused`.

            * `queue` — The message is appended after any already-queued
            `ConversationText` without interrupting the current agent turn or
            think response. If nothing is queued, the message plays immediately.

            * `interrupt` — The agent immediately speaks. If the agent was
            already speaking, it interrupts the current speech and replaces it
            with the new message. If the user is speaking, the agent interrupts
            with the new message, but the user's continued speech triggers
            `UserStartedSpeaking`, which quickly interrupts the agent.
      required:
        - type
        - is_dynamic
      title: AgentV1_AgentV1InjectDynamicAgentMessage
    AgentV1_AgentV1SendFunctionCallResponse:
      type: object
      properties:
        type:
          type: string
          enum:
            - FunctionCallResponse
          description: Message type identifier for function call responses
        id:
          type: string
          description: |
            The unique identifier for the function call.

            • **Required for client responses**: Should match the id from
              the corresponding `FunctionCallRequest`
            • **Optional for server responses**: Server may omit when responding
              to internal function executions
        name:
          type: string
          description: The name of the function being called
        content:
          type: string
          description: The content or result of the function call
      required:
        - type
        - name
        - content
      description: |
        Function call response message used bidirectionally:

        • **Client → Server**: Response after client executes a function
          marked as client_side: true
        • **Server → Client**: Response after server executes a function
          marked as client_side: false

        The same message structure serves both directions, enabling a unified
        interface for function call responses regardless of execution location.
      title: AgentV1_AgentV1SendFunctionCallResponse
    ChannelsAgentV1MessagesAgentV1KeepAliveType:
      type: string
      enum:
        - KeepAlive
      description: Message type identifier
      title: ChannelsAgentV1MessagesAgentV1KeepAliveType
    AgentV1_AgentV1KeepAlive:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ChannelsAgentV1MessagesAgentV1KeepAliveType'
          description: Message type identifier
      required:
        - type
      description: Send a control message to the agent
      title: AgentV1_AgentV1KeepAlive
    AgentV1_AgentV1UpdatePrompt:
      type: object
      properties:
        type:
          type: string
          enum:
            - UpdatePrompt
          description: Message type identifier for prompt update request
        prompt:
          type: string
          description: The new system prompt to be used by the agent
      required:
        - type
        - prompt
      title: AgentV1_AgentV1UpdatePrompt
    AgentV1_AgentV1ForceEndTurn:
      type: object
      properties:
        type:
          type: string
          enum:
            - ForceEndTurn
          description: Message type identifier for forcing the end of the current turn
      required:
        - type
      title: AgentV1_AgentV1ForceEndTurn
    AgentV1_AgentV1CustomToThinkProvider:
      type: object
      properties:
        type:
          type: string
          enum:
            - __customToThinkProvider
          description: >-
            Message type identifier for sending a custom payload to the think
            provider
        content:
          description: >-
            Any valid JSON value (object, array, string, number, boolean, or
            null). Deepgram forwards it to the think provider without validation
      required:
        - type
        - content
      title: AgentV1_AgentV1CustomToThinkProvider
    AgentV1_AgentV1Media:
      type: string
      format: binary
      title: AgentV1_AgentV1Media

```
