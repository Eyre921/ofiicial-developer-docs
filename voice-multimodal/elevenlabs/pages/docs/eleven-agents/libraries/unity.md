---
title: "Unity SDK"
source: https://elevenlabs.io/docs/eleven-agents/libraries/unity.md
path: docs/eleven-agents/libraries/unity
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Unity SDK

> **Info**
>
> Refer to the [ElevenAgents overview](/docs/eleven-agents/overview) for an explanation of how
> ElevenAgents works.

The [ElevenAgents Unity SDK](https://github.com/elevenlabs/unity) connects a Unity scene to an ElevenLabs agent. It captures the player's microphone, streams the agent's voice back through an `AudioSource`, and exposes the session through a single `Conversation` API that behaves the same in the Editor, desktop standalone players, and WebGL builds.

## Requirements

* Unity 6.3 LTS (`6000.3.0f1`) or later. The SDK uses scriptable-audio APIs introduced in Unity 6.3.
* [`ApiCompatibilityLevel`](https://docs.unity3d.com/6000.3/Documentation/ScriptReference/ApiCompatibilityLevel.html) set to **.NET Standard 2.1** (`ApiCompatibilityLevel.NET_Standard`), the default for Unity 2023.1 and later. In the Editor, find it under **Edit** > **Project Settings** > **Player** > **Other Settings** > **Api Compatibility Level**.
* An ElevenLabs account and an agent. Create one in the [dashboard](https://elevenlabs.io/app/agents) or follow the [quickstart](/docs/eleven-agents/quickstart).

### Platform support

| Target                                                         | Transport                                | Status                           |
| -------------------------------------------------------------- | ---------------------------------------- | -------------------------------- |
| Editor (Play Mode), desktop standalone (macOS, Windows, Linux) | Native WebSocket                         | Supported                        |
| WebGL                                                          | `@elevenlabs/client` through a JS bridge | Supported (WebSocket and WebRTC) |
| iOS, Android, XR                                               | Native WebSocket                         | Beta                             |

The SDK selects the transport for the active build target automatically. WebRTC is only available on WebGL; on every other target `ConnectionType.WebRTC` throws a `NotSupportedException`.

Beta targets use the same native transport as desktop but are not yet covered by the SDK's test suite. Report issues on [GitHub](https://github.com/elevenlabs/unity/issues).

> **Warning**
>
> The SDK does not request microphone permission. On iOS and Android, request it yourself before
> starting a session. Without it, `StartSessionAsync` throws.

## Installation

In Unity, open **Window** > **Package Manager**, select **+** > **Install package from git URL**, and paste the repository URL:

```text
https://github.com/elevenlabs/unity.git
```

The Package Manager installs the package as **ElevenAgents** (`io.elevenlabs.agents`), together with its dependencies: Input System and Newtonsoft Json.

> **Note**
>
> The URL without a version installs the latest commit on the default branch. To pin a release, find
> the latest tag on the [releases page](https://github.com/elevenlabs/unity/releases) and append it
> to the URL after `#`, in the form `https://github.com/elevenlabs/unity.git#vX.Y.Z`. To upgrade
> later, change the tag in `Packages/manifest.json`.

> **Tip**
>
> The package ships two samples. Import them from **Package Manager** > **ElevenAgents** >
> **Samples**. **QuickStart** is a single MonoBehaviour that renders the live transcript.
> **GettingStarted** is a walk-up-and-talk scene with spatial audio and dynamic variables. See the
> [Getting started walkthrough](https://github.com/elevenlabs/unity/blob/main/Docs~/GETTING_STARTED.md) for a
> step-by-step guide.

## Quickstart

This section adds a voice agent to an empty scene. The agent starts talking when you enter Play Mode and the session ends when you leave it.

#### Create a public agent

Create an agent in the [ElevenLabs dashboard](https://elevenlabs.io/app/agents). In the agent's **Security** settings, turn **Authentication** off so the game can connect with the agent ID alone. Copy the agent ID.

For agents that require authentication, see [Public and private agents](#public-and-private-agents).

#### Install the SDK

Install the package from the git URL as described in [Installation](#installation).

#### Add a conversation script

Create `Assets/Scripts/AgentConversation.cs`:

**`AgentConversation.cs`**

```csharp title="AgentConversation.cs"
using System;
using ElevenLabs.Agents;
using ElevenLabs.Protocol;
using UnityEngine;

public sealed class AgentConversation : MonoBehaviour
{
    [SerializeField]
    private string agentId = "agent_7101k5zvyjhmfg983brhmhkd98n6";

    private Conversation conversation;

    private async void Start()
    {
        try
        {
            conversation = await Conversation.StartSessionAsync(
                new ConversationOptions { AgentId = agentId }
            );
        }
        catch (Exception ex)
        {
            Debug.LogError($"Failed to start session: {ex.Message}");
            return;
        }

        Debug.Log($"Connected: {conversation.ConversationId}");

        conversation.UserTranscriptReceived += OnUserTranscript;
        conversation.AgentResponded += OnAgentResponse;
        conversation.ErrorOccurred += message => Debug.LogError(message);
        conversation.Disconnected += details => Debug.Log($"Disconnected: {details.Reason}");
    }

    private void OnUserTranscript(UserTranscriptArgs args) =>
        Debug.Log($"User: {args.UserTranscript}");

    private void OnAgentResponse(AgentResponseArgs args) =>
        Debug.Log($"Agent: {args.AgentResponse}");

    private void OnDestroy()
    {
        _ = conversation?.EndSession();
    }
}
```

`Conversation.StartSessionAsync` returns once the connection is open and the audio devices are ready. `EndSession` is idempotent, so calling it from `OnDestroy` is safe even if the session has already ended.

#### Run the scene

Create an empty GameObject, add the `AgentConversation` component, and paste your agent ID into the **Agent Id** field. Enter Play Mode and allow microphone access if your operating system prompts for it. The agent speaks its first message and the transcript appears in the Console.

## Public and private agents

#### Public agents

Pass the agent ID directly. Anyone with the ID can start a conversation with the agent.

```csharp
var conversation = await Conversation.StartSessionAsync(
    new ConversationOptions { AgentId = "agent_7101k5zvyjhmfg983brhmhkd98n6" }
);
```

#### Private agents

Agents with authentication enabled need a short-lived credential issued by your own server. Request a [signed URL](/docs/eleven-agents/customization/authentication) from your backend and pass it as `SignedUrl`:

```csharp
using UnityEngine.Networking;

private static async Awaitable<string> FetchSignedUrlAsync()
{
    using var request = UnityWebRequest.Get("https://api.example-game.com/agent/signed-url");
    await request.SendWebRequest();
    if (request.result != UnityWebRequest.Result.Success)
        throw new InvalidOperationException(request.error);
    return request.downloadHandler.text;
}

var conversation = await Conversation.StartSessionAsync(
    new ConversationOptions { SignedUrl = await FetchSignedUrlAsync() }
);
```

For WebRTC sessions on WebGL, pass a conversation token as `ConversationToken` and set `ConnectionType = ConnectionType.WebRTC`.

> **Warning**
>
> Never ship your ElevenLabs API key in a game build. Generate signed URLs and conversation tokens on a server you control.

Set exactly one of `AgentId`, `SignedUrl`, or `ConversationToken`. Set `UserId` to associate the conversation with a player in your own systems.

## Spatial audio

By default the SDK plays the agent's voice through a hidden `AudioSource` it creates. To place the voice in the scene, pass your own `AudioSource` as `OutputAudioSource`:

```csharp
[SerializeField]
private AudioSource voiceSource; // Spatial Blend = 1 for 3D audio

var conversation = await Conversation.StartSessionAsync(
    new ConversationOptions
    {
        AgentId = "agent_7101k5zvyjhmfg983brhmhkd98n6",
        OutputAudioSource = voiceSource,
    }
);
```

The SDK keeps the source's spatial blend, rolloff, mixer routing, and position. It restores the source's clip, loop, and volume settings when the session ends.

To drive a visual effect from the agent's voice, such as a mouth animation, read `conversation.GetOutputVolume()` each frame. It returns a value between 0 and 1 on every platform.

## Personalization

Use [dynamic variables](/docs/eleven-agents/customization/personalization/dynamic-variables) to fill placeholders in the agent's prompt and first message, and [overrides](/docs/eleven-agents/customization/personalization/overrides) to replace parts of the agent configuration for one session:

```csharp
using System.Collections.Generic;
using ElevenLabs.Protocol;

var options = new ConversationOptions
{
    AgentId = "agent_7101k5zvyjhmfg983brhmhkd98n6",
    DynamicVariables = new Dictionary<string, object>
    {
        ["player_name"] = "Ada",
        ["quest_stage"] = 3,
    },
    Overrides = new ConversationConfigOverride
    {
        Agent = new ConversationConfigOverrideAgent
        {
            FirstMessage = "Welcome back, {{player_name}}.",
        },
        Tts = new ConversationConfigOverrideTts { VoiceId = "JBFqnCBsd6RMkjVDRZzb" },
    },
};
```

Dynamic variable values must be strings, numbers, or booleans. Each override must be enabled in the agent's **Security** settings before the server accepts it.

## Client tools

[Client tools](/docs/eleven-agents/customization/tools/client-tools) let the agent trigger actions in your game. Define the tool in the agent's settings, then register a handler with the same name:

```csharp
using Newtonsoft.Json;

public sealed class OpenDoorParams
{
    [JsonProperty("door_id")]
    public string DoorId { get; set; }
}

conversation.RegisterTool<OpenDoorParams, string>("open_door", parameters =>
{
    DoorRegistry.Open(parameters.DoorId);
    return $"Door {parameters.DoorId} is open.";
});
```

The SDK deserializes the tool parameters into `TParams` with Newtonsoft Json, so use `[JsonProperty]` when a parameter name differs from the property name. The return value is serialized as the tool result. Return an `Awaitable<TResult>` for asynchronous handlers. Throw `ClientToolException` with an `errorType` to report a specific failure to the agent; any other exception is reported as a generic error.

Calls to tools without a registered handler raise `ErrorOccurred`, or `UnhandledClientToolCall` if you subscribe to it.

## Events

Subscribe to events on the `Conversation` returned by `StartSessionAsync`. The SDK raises them on Unity's main thread.

| Event                     | Payload                | Description                                                              |
| ------------------------- | ---------------------- | ------------------------------------------------------------------------ |
| `Disconnected`            | `DisconnectionDetails` | The session ended. `Reason` is `User`, `Agent`, or `Error`.              |
| `ErrorOccurred`           | `string`               | An error occurred after the session started.                             |
| `StatusChanged`           | `Status`               | The connection status changed.                                           |
| `ModeChanged`             | `Mode`                 | The agent switched between `Speaking` and `Listening`.                   |
| `UserTranscriptReceived`  | `UserTranscriptArgs`   | A finalized transcript of the player's speech.                           |
| `AgentResponded`          | `AgentResponseArgs`    | The text of the agent's response.                                        |
| `Interrupted`             | `InterruptionArgs`     | The player interrupted the agent.                                        |
| `AgentToolRequested`      | `AgentToolRequestArgs` | The agent started a tool call. `AgentToolResponded` fires on completion. |
| `UnhandledClientToolCall` | `ClientToolCallArgs`   | The agent called a client tool with no registered handler.               |
| `CanSendFeedbackChanged`  | `bool`                 | Feedback became available or unavailable for the latest agent response.  |

The `Connected` event fires before `StartSessionAsync` returns, so read `ConversationId` and `Status` directly once the call completes. The [package changelog](https://github.com/elevenlabs/unity/blob/main/CHANGELOG.md) lists the full event surface.

## Methods

| Method                                                        | Description                                                            |
| ------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `EndSession()`                                                | Close the connection and release the audio devices.                    |
| `SendUserMessage(string text)`                                | Send a text message as if the player had spoken it.                    |
| `SendContextualUpdate(string text)`                           | Share game state with the agent without interrupting the conversation. |
| `SendUserActivity()`                                          | Signal that the player is active so the agent holds its turn.          |
| `SendFeedback(bool like)`                                     | Rate the latest agent response when `CanSendFeedback` is `true`.       |
| `SetMicMuted(bool isMuted)`                                   | Mute or unmute the microphone.                                         |
| `SetVolume(float volume)`                                     | Set the agent's playback volume between 0 and 1.                       |
| `GetInputVolume()`, `GetOutputVolume()`                       | Read the current microphone or agent audio level between 0 and 1.      |
| `GetInputByteFrequencyData()`, `GetOutputByteFrequencyData()` | Fill a byte buffer with frequency data for audio visualizers.          |
| `UploadFileAsync()`, `SendMultimodalMessage()`                | Upload a file and attach it to a user message.                         |
| `ChangeInputDevice()`, `ChangeOutputDevice()`                 | Switch the microphone or output device during a session.               |

For example, send the player's current location to the agent when they enter a new area:

```csharp
conversation.SendContextualUpdate("The player entered the abandoned lighthouse.");
```

## WebGL builds

WebGL builds need one additional Player Setting.

> **Warning**
>
> In **Player Settings** > **WebGL** > **Publishing Settings**, turn **Use WebAssembly.Table** on.
> The SDK fails the build with instructions if this setting is off.

> **Warning**
>
> Play Mode in the Editor is not yet supported while the active build target is WebGL, and
> `StartSessionAsync` throws. Switch to a desktop build target to test in the Editor.

Unity has no scriptable audio pipeline on WebGL, so the SDK plays the agent's voice through the browser's Web Audio API and mirrors the volume, position, and spatial settings of your `OutputAudioSource`. As a result, `AudioSource.GetOutputData` and `OnAudioFilterRead` return silence on WebGL. Use `GetOutputVolume()` and `GetOutputByteFrequencyData()` instead.

See [`COMPATIBILITY.md`](https://github.com/elevenlabs/unity/blob/main/COMPATIBILITY.md) for the full WebGL compatibility matrix.

## Troubleshooting

* **`StartSessionAsync` throws `ArgumentException`.** Set exactly one of `AgentId`, `SignedUrl`, or `ConversationToken`.
* **The session fails to connect for a valid agent ID.** The agent requires authentication. Turn authentication off or connect with a signed URL.
* **An override has no effect.** Enable the matching override in the agent's **Security** settings.
* **The player hears nothing on WebGL.** Browsers keep audio suspended until the player interacts with the page. Start the session after a click or key press.
* **The microphone is unavailable on WebGL.** Browsers only grant microphone access to pages served over HTTPS or from `localhost`.

Report bugs and request features on [GitHub](https://github.com/elevenlabs/unity/issues).
