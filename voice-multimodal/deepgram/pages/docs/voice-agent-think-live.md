---
title: "Think Live"
source: https://developers.deepgram.com/docs/voice-agent-think-live.md
path: docs/voice-agent-think-live
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.

# Think Live

Voice Agent

Today's cascaded voice agents are fast and accurate, but they still struggle with the parts of a conversation that people handle without thinking: knowing when to hold the floor, when to yield it, whether a silence means "I'm thinking" or "I'm done," and when a quick "mhmm" is a better response than a full LLM turn.

Think Live is Deepgram's first step toward closing that gap. It introduces the **Think Live model**, a Deepgram model that runs alongside the reasoning LLM you already configure and participates directly in orchestration. The reasoning LLM keeps doing the deeper thinking (answering the question, calling your functions, working through your prompt). The Think Live model keeps the conversation alive while that happens: acknowledging, holding the floor, checking whether the caller is still there, and reading frustration.

This is also the first customer-visible piece of the architecture Deepgram is building toward, where a conversational model is a first-class stage of the pipeline rather than glue code in your client.

## Key features

* **Backchanneling** – Backchannels are the short active listening noises a person makes while someone else is talking ("mhmm," "yeah," "got it").
  * **User backchannel detection** – The agent understands when a user is backchanneling and continues speaking, not treating it as an interruption.
  * **Agent backchanneling** – The agent provides backchannels to the user to encourage them to continue speaking. Backchannels come from the Think Live model, not from your reasoning LLM, so they land while the user is still speaking instead of after the turn ends.
* **Presence Check** – When the user goes quiet for longer than expected, the agent can prompt rather than leave dead air ("take your time," "are you still there?").
* **Frustration Detection** – The Think Live model monitors user turns for frustration signals (negative valence, high arousal, frustrated intent) and categorizes them accordingly, allowing you to proceed forward with any escalation-dependent workflows.
* **Agent filler** – The Think Live model covers waits on a function call, or any wait your client knows about, with short filler it words itself instead of leaving dead air.
* **Improved End-of-Turn Detection** – With the addition of the Think Live model, you should see improved performance in end-of-turn detection. Semantic end-of-turn and silence handling inherit from your Flux listen settings.

## Recent updates

Think Live changes ship here rather than in the main changelog.

| Date         | Update                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| October 2026 | **Agent filler.** The Think Live model can now cover waits with short filler it words itself ("Let me pull that up for you"). Turn it on per function with [`initial_agent_filler`, `agent_filler_max_count`, and `agent_filler_interval_ms`](#filler-during-function-calls), or request it on demand with [`InjectAgentMessage`](#filler-on-demand) and `is_dynamic: true`. Filler is tagged `conversational_behavior: "filler"` in [`ConversationText`](#conversationtext). |

## The API surface

The Voice Agent API today configures one provider per stage:

* `agent.listen.provider` (STT)
* `agent.think.provider` (LLM)
* `agent.speak.provider` (TTS)

Think Live splits `think` into two providers, because there are now two models thinking:

* `agent.listen.provider` (STT)
* `agent.think.provider` (your reasoning LLM)
* `agent.think_live.provider` (Deepgram's Think Live model)
* `agent.speak.provider` (TTS)

Existing configurations keep working: `agent.think.provider` is the reasoning LLM in both modes. The server also accepts `agent.think_reasoning.provider` as an alias, but sending both is an error, so prefer `agent.think`. Think Live is off until you provide the `think_live.provider`.

`agent.think_live.provider` is a Deepgram provider - you cannot specify another `provider.type`. Set `type` to `deepgram` and `version` to `v1`.

### Configuration parameters

| Parameter                                                     | Type    | Description                                                                                                                                                                                                                                            |
| ------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `agent.think_live.provider.`  `agent_backchannel_sensitivity` | Number  | Probability of the agent producing backchannel responses to the user (such as "mhmm"). Valid range `0` to `1`. Higher values produce more backchanneling. `0` disables the feature. Defaults to `0.73`.                                                |
| `agent.think_live.provider.`  `presence_check_max_count`      | Integer | Maximum number of times the agent will probe the user for a response after extended silence. Once the maximum is reached, the agent stays silent. `0` disables the feature. Defaults to `3`.                                                           |
| `agent.think_live.provider.`  `presence_check_interval_ms`    | Integer | Time in milliseconds the agent waits between presence-check utterances. Valid range `1` to `60000`, though the first check is floored at `3000`, so lower values behave as `3000`. Ignored when `presence_check_max_count` is `0`. Defaults to `4500`. |
| `agent.think_live.provider.`  `frustration_max_count`         | Integer | Maximum number of [`FrustrationDetected`](#frustrationdetected) events the agent will try to resolve before setting the `escalated` flag. `0` stops `FrustrationDetected` from being sent at all. Omit it to use the server default.                   |
| `agent.think_live.provider.`  `restricted_terms`              | Array   | Terms the Think Live model will not say. Each entry is a plain string; pass a multi-word phrase as a single array element. Defaults to `["human", "transfer"]`.                                                                                        |

#### `agent.think_live.provider.agent_backchannel_sensitivity`

Raise the value for agents that should sound attentive during long user turns, such as an agent taking an order number or an address. Lower it for agents that read as more formal, or where the caller is likely to be on a noisy line.

#### `agent.think_live.provider.presence_check_max_count` and `presence_check_interval_ms`

`presence_check_max_count` caps how many times the agent will prompt the user to respond in a single silence; `presence_check_interval_ms` sets the gap between attempts. After the cap is reached the agent stays silent and leaves the next move to you.

#### `agent.think_live.provider.restricted_terms`

`restricted_terms` constrains the Think Live model's own text generation. The model is trained on roughly 200,000 curated Deepgram conversations.

The default list exists because the Think Live model speaks without your prompt in front of it: an agent with no escalation path should not volunteer "let me get you a human."

This is a constraint on the Think Live model only. Your reasoning LLM can still produce these words, depending on your prompt and your functions.

### Turn-taking and silence

See [Configure the Voice Agent](/docs/configure-voice-agent#agent---listen-settings-stt) for detailed EOT settings.

### Example Settings message

**`JSON`**

```json JSON
{
  "type": "Settings",
  "audio": {
    "input": { "encoding": "linear16", "sample_rate": 16000 },
    "output": { "encoding": "linear16", "sample_rate": 16000 }
  },
  "agent": {
    "listen": {
      "provider": { "type": "deepgram", "model": "flux-general-en", "version": "v2" }
    },
    "think": {
      "provider": { "type": "open_ai", "model": "gpt-5.4-mini" },
      "prompt": "You are Stella, a customer support agent for an online retailer."
    },
    "think_live": {
      "provider": {
        "type": "deepgram",
        "version": "v1",
        "agent_backchannel_sensitivity": 0.2,
        "presence_check_max_count": 2,
        "presence_check_interval_ms": 5000,
        "frustration_max_count": 2,
        "restricted_terms": ["human", "transfer"]
      }
    },
    "speak": {
      "provider": { "type": "deepgram", "model": "flux-kit-en", "version": "v2" }
    },
    "greeting": "Hi, thanks for calling. How can I help?"
  }
}
```

Note: The released SDKs do not yet expose `think_live` as a typed field. It passes through unchanged: build the Settings object from a dict in Python, or cast the object in TypeScript before calling `sendSettings`. The same applies to the agent filler fields on functions. Dynamic `InjectAgentMessage` has its own method in the next SDK release; until then, send it as a raw JSON message.

## Agent filler

A function call that takes a few seconds leaves the caller in silence unless your prompt tells the reasoning LLM to announce it, and even then the announcement comes once. Agent filler hands that job to the Think Live model. It words a short line that fits the conversation ("Let me check the available slots for you"), and if the wait keeps going, follows up with a different line ("Still looking, thanks for bearing with me") rather than repeating itself.

Unlike an `agent_filler` function your server implements, where your code supplies the words, here the Think Live model writes and speaks the line itself, with no round trip to your client.

Agent filler requires `agent.think_live`. Filler is spoken through your `speak` provider, enters the conversation history, and is reported in [`ConversationText`](#conversationtext) with `conversational_behavior: "filler"`.

### Filler during function calls

Three optional fields on each function definition (`agent.think.functions`) control filler for that function.

| Field                      | Type    | Default | Description                                                                                                                                                                                          |
| -------------------------- | ------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `initial_agent_filler`     | Boolean | `false` | Speak one filler once the call is dispatched and the user's turn is confirmed, if the `FunctionCallResponse` has not arrived yet.                                                                    |
| `agent_filler_max_count`   | Integer | `0`     | Maximum number of additional fillers while the call is still outstanding. `0` disables additional filler.                                                                                            |
| `agent_filler_interval_ms` | Integer | `5000`  | Silence, in milliseconds, before each additional filler. Ignored when `agent_filler_max_count` is `0`, which is also the only case in which a value outside the `1000` to `60000` range is accepted. |

**`JSON`**

```json JSON
{
  "name": "get_available_slots",
  "description": "Look up open appointment slots for a given date",
  "parameters": {
    "type": "object",
    "properties": {
      "date": { "type": "string", "description": "Date in YYYY-MM-DD format" }
    },
    "required": ["date"]
  },
  "initial_agent_filler": true,
  "agent_filler_max_count": 2,
  "agent_filler_interval_ms": 7000
}
```

With these settings, the agent speaks one filler when the call goes out, then up to two more, each after 7 seconds of silence, until your `FunctionCallResponse` arrives. If the response arrives first, no filler is spoken.

How filler timing works:

* **Confirmed turns only.** If a call is dispatched early (for example, from an eager end-of-turn), the initial filler waits until the user's turn is confirmed. If the user keeps talking and the turn is not confirmed, no filler is spoken.
* **No double announcements.** If the reasoning LLM already said something in the same response that made the call ("Let me look that up"), the initial filler is skipped because that line already covers the moment.
* **One schedule per turn.** When a turn makes several calls, they share one filler schedule, taken from the first call that asked for filler.
* **Silence-based spacing.** `agent_filler_interval_ms` counts from when the agent last stopped speaking, not from when the call started.
* **Additional filler without an initial one.** You can set `initial_agent_filler` to `false` and `agent_filler_max_count` above `0` to stay quiet for short calls and only fill long ones.

> **Note**
>
> If any function sets `initial_agent_filler` or a nonzero `agent_filler_max_count` and `agent.think_live` is not configured, the `Settings` message is rejected with an `Error` (code `INVALID_SETTINGS`) naming the function, and the session closes. An `agent_filler_interval_ms` outside `1000` to `60000` is rejected the same way when `agent_filler_max_count` is above `0`.

### Filler on demand

Your client sometimes knows about a wait the agent does not: a slow lookup outside a function call, a handoff, or reasoning LLM latency you are tracking yourself. Send [`InjectAgentMessage`](/docs/voice-agent-inject-agent-message) with `is_dynamic: true` and the Think Live model words a filler for you.

| Field        | Type    | Required    | Description                                                                                               |
| ------------ | ------- | ----------- | --------------------------------------------------------------------------------------------------------- |
| `type`       | String  | Yes         | `"InjectAgentMessage"`                                                                                    |
| `behavior`   | String  | No          | `"default"`, `"queue"`, or `"interrupt"`. Defaults to `"default"`. Same behavior as a standard injection. |
| `is_dynamic` | Boolean | No          | When `true`, the agent generates the filler. Defaults to `false`.                                         |
| `message`    | String  | Conditional | The text to speak. Required when `is_dynamic` is `false`. Must be omitted when `is_dynamic` is `true`.    |

**`JSON`**

```json JSON
{
  "type": "InjectAgentMessage",
  "behavior": "default",
  "is_dynamic": true
}
```

Each message requests one filler. Once the previous filler has been spoken, a further request in the same wait escalates the wording rather than repeating it.

| Situation                                                        | Result                                                                                |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `is_dynamic: true` with a `message`                              | Rejected with an `Error` (code `UNPARSABLE_CLIENT_MESSAGE`), and the session closes.  |
| `is_dynamic` omitted or `false` without a `message`              | Rejected with an `Error` (code `UNPARSABLE_CLIENT_MESSAGE`), and the session closes.  |
| `is_dynamic: true` without `agent.think_live`                    | Ignored, with a `Warning` (code `DYNAMIC_FILLER_UNAVAILABLE`).                        |
| Filler could not be generated                                    | Nothing is spoken, with a `Warning` (code `DYNAMIC_FILLER_UNAVAILABLE`).              |
| A second `is_dynamic` request arrives before the first is worded | The earlier request is dropped, with a `Warning` (code `DYNAMIC_FILLER_UNAVAILABLE`). |
| User starts speaking before the filler is worded                 | Nothing is spoken, with a `Warning` (code `DYNAMIC_FILLER_UNAVAILABLE`).              |
| User is speaking and `behavior` is `default` or `queue`          | Ignored, with the standard `INJECT_AGENT_MESSAGE_DURING_USER_SPEECH` warning.         |
| Agent is speaking and `behavior` is `default`                    | Ignored, with the standard `INJECT_AGENT_MESSAGE_DURING_AGENT_SPEECH` warning.        |

## Server events

Think Live adds one server event, one field to an existing one, and an acknowledgement for mid-session updates, described below.

### FrustrationDetected

The Think Live model monitors user turns for frustration signals (negative valence, high arousal, frustrated intent). When it detects frustration, the server sends a `FrustrationDetected` event.

**`JSON`**

```json JSON
{
  "type": "FrustrationDetected",
  "count": 1,         // Cumulative count of FrustrationDetected events in this session, starting at 1
  "escalated": false  // True once count reaches frustration_max_count
}
```

`escalated` stays `false` until `count` reaches [`agent.think_live.provider.frustration_max_count`](#configuration-parameters). Treat `escalated: true` as the signal to run your escalation workflow: transfer to a human, alert a supervisor, or whatever your product requires. Deepgram does not transfer the call for you.

Set `frustration_max_count` to `0` to stop `FrustrationDetected` from being sent.

### ConversationText

[`ConversationText`](/docs/voice-agent-conversation-text) gains a `conversational_behavior` field, which annotates what kind of utterance the message represents. Existing messages are reported as `default`, so a client that ignores the field behaves as it does today.

**`JSON`**

```json JSON
{
  "type": "ConversationText",
  "role": "",                    // The speaker of this statement, either "user" or "assistant"
  "conversational_behavior": "", // "default", "backchannel", "presence_check", or "filler"
  "content": ""                  // The statement that was spoken
}
```

| Value            | Meaning                                                                            |
| ---------------- | ---------------------------------------------------------------------------------- |
| `default`        | A standard turn, the same content `ConversationText` carries today.                |
| `backchannel`    | A short acknowledgement produced while the user held the floor.                    |
| `presence_check` | A prompt produced after extended silence.                                          |
| `filler`         | A short line covering a wait on a function call or a dynamic `InjectAgentMessage`. |

Use the field to keep transcripts and UI readable. Backchannels, presence checks, and filler are conversational scaffolding rather than substance, so most clients render them differently from a `default` turn, or suppress them entirely.

## Mid-session updates

You can change the Think Live model configuration in the middle of a session by sending an `UpdateThink_Live` message. It replaces the entire `agent.think_live.provider` block, so include every parameter you want in effect, not only the ones you are changing. Parameters you omit fall back to their defaults.

**`JSON`**

```json JSON
{
  "type": "UpdateThink_Live",
  "think_live": {
    "provider": {
      "type": "deepgram",
      "version": "v1",
      "agent_backchannel_sensitivity": 0.5,
      "presence_check_max_count": 3,
      "presence_check_interval_ms": 4500,
      "frustration_max_count": 2,
      "restricted_terms": ["human", "transfer"]
    }
  }
}
```

Once the server has applied the new configuration, it acknowledges with a `ThinkLiveUpdated` message. Wait for this acknowledgement before assuming the new parameters are in effect.

**`JSON`**

```json JSON
{
  "type": "ThinkLiveUpdated"
}
```

`UpdateThink_Live` changes the Think Live model only. To change your reasoning LLM mid-session, use [`UpdateThink`](/docs/voice-agent-update-think).

## Feedback

The Think Live defaults are a hypothesis, not a finished answer. The feedback that helps most is specific: which parameter you wanted to turn up or down, in what kind of conversation, and what the agent did instead. Rough timestamps or session IDs let us line your observation up with the model signals on our side.

Reach out in your Deepgram shared Slack channel to provide feedback, and feel free to tag Theresa Foy with any questions or comments.
