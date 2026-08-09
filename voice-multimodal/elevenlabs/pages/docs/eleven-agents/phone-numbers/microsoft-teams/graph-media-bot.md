---
title: "Graph calling bot"
source: https://elevenlabs.io/docs/eleven-agents/phone-numbers/microsoft-teams/graph-media-bot.md
path: docs/eleven-agents/phone-numbers/microsoft-teams/graph-media-bot
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Graph calling bot

## Overview

This approach makes the agent a **callable Teams identity**. A user searches for it by name and calls it 1:1, and the agent answers in real time — no phone number, PSTN, or Communications Credits. It's the only approach callable by name, and the most involved to run.

It uses a **Microsoft Graph real-time media bot** (the Cloud Communications calling platform). The media SDK (`Microsoft.Skype.Bots.Media`) is **.NET on Windows Server only** — there is no Linux or non-.NET path for raw audio in Teams calls.

This is the only approach that's callable **by name** inside Teams. Prefer the [widget
tab](/docs/eleven-agents/phone-numbers/microsoft-teams/widget-tab) for a lighter setup, or
[ACS](/docs/eleven-agents/phone-numbers/microsoft-teams/azure-communication-services) when you
specifically want a phone number.

## How it works

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/f411ec0b44d4c5ca1a61598fbd1e6162e46a1c74179eebb4b673ee1428823e84/assets/images/conversational-ai/teams-media-bot-architecture.svg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260809%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260809T080735Z&X-Amz-Expires=604800&X-Amz-Signature=66acaac4ede3a238d7e632c8107cab3be887541ce651c540ee93a28758d3c947&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="A Teams user calls the bot by name; Teams routes the call to the media bot on a Windows VM, which bridges raw PCM 16k audio to the ElevenLabs agent over a WebSocket" />

The bot answers with **application-hosted media**, receives 50 audio frames/sec (20 ms PCM 16 kHz), bridges them to the ElevenLabs agent over a WebSocket, and streams the agent's audio back into the call.

## Requirements

1. An **Azure Bot** registration + app (Entra app registration).
2. **Graph application permissions** with admin consent: `Calls.AccessMedia.All` (raw media) plus `Calls.Initiate.All`.
3. A **Windows Server VM** (≥ **2 physical cores** — e.g. `Standard_D4s_v3`) with a public IP and open media ports.
4. A **CA-signed TLS certificate** on a public FQDN for the media/signaling endpoint (the media platform rejects self-signed certs).
5. An [ElevenLabs agent](/docs/eleven-agents/quickstart) set to **PCM 16000 Hz** on both legs: TTS output format on the **Voice** tab, user input audio format on the **Advanced** tab.

A `D2s_v3` (2 vCPU = **1 physical core**) fails with `MediaPlatform needs a system with at least 2
  cores`. Use a size with ≥ 2 physical cores (e.g. `D4s_v3`).

## Permissions & roles

| Scope                         | Role / permission                                                                                                         | Why                                                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Entra                         | **Application Administrator**                                                                                             | create the app registration + Azure Bot                                                          |
| Entra                         | **Global Administrator / Privileged Role Administrator**                                                                  | grant admin consent for the Graph calling permissions — app permissions cannot be self-consented |
| Microsoft Graph (application) | `Calls.AccessMedia.All`, `Calls.Initiate.All`                                                                             | answer 1:1 calls and access raw media                                                            |
| Azure RBAC                    | **Contributor** on the resource group                                                                                     | create the Windows VM + Azure Bot                                                                |
| Teams admin                   | allow [**custom app upload**](https://admin.teams.microsoft.com/policies/manage-apps); enable the bot **Calling** channel | sideload the app and receive calls                                                               |

## Step 1 — Register the bot + Graph permissions

Create an app registration and an Azure Bot bound to it, then grant + consent the calling permissions (you need Global Admin / Privileged Role Admin to consent):

```bash
APPID=$(az ad app create --display-name "ElevenLabs Teams Agent" \
  --sign-in-audience AzureADMyOrg --query appId -o tsv)
az ad sp create --id "$APPID"
# create a client secret and record it
az ad app credential reset --id "$APPID" --display-name bot --query password -o tsv

# Azure Bot bound to the app
az bot create --resource-group $RG --name el-teams-agent-bot \
  --app-type SingleTenant --appid "$APPID" --tenant-id $TENANT \
  --endpoint "https://YOUR_FQDN/api/messages" --sku S1
```

Grant the two Graph application roles and **admin consent** (needs Global Admin / Privileged Role Admin), then confirm the assignments landed:

```bash
# Graph app roles: Calls.AccessMedia.All, Calls.Initiate.All
az ad app permission add --id "$APPID" --api 00000003-0000-0000-c000-000000000000 \
  --api-permissions a7a681dc-756e-4909-b988-f160edc6655f=Role \
    284383ee-7f6e-4e40-a2a8-e85dcb029101=Role
az ad app permission admin-consent --id "$APPID"

# Verify — should print both role ids
az rest --method GET \
  --url "https://graph.microsoft.com/v1.0/servicePrincipals(appId='$APPID')/appRoleAssignments" \
  --query "value[].appRoleId" -o tsv
```

If `admin-consent` returns `Consent validation failed`, grant the app roles directly on the service principal instead:

```bash
GRAPH_SP=$(az ad sp show --id 00000003-0000-0000-c000-000000000000 --query id -o tsv)
BOT_SP=$(az ad sp show --id "$APPID" --query id -o tsv)
for ROLE in a7a681dc-756e-4909-b988-f160edc6655f 284383ee-7f6e-4e40-a2a8-e85dcb029101; do
  az rest --method POST \
    --url "https://graph.microsoft.com/v1.0/servicePrincipals/$GRAPH_SP/appRoleAssignedTo" \
    --body "{\"principalId\": \"$BOT_SP\", \"resourceId\": \"$GRAPH_SP\", \"appRoleId\": \"$ROLE\"}"
done
```

In the portal, verify in the [Entra admin center](https://entra.microsoft.com/#view/Microsoft_AAD_RegisteredApps/RegisteredAppsListBlade) under **App registrations → your app → API permissions**: both permissions should show **Granted** with green checks.

![The app registration API permissions blade showing Calls.AccessMedia.All and Calls.Initiate.All
granted](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/4abc1e220d3fc03845594aa4f835656425cc1c39448dae30dace98e672fd8fb1/assets/images/conversational-ai/teams-graph-api-permissions.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260809%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260809T080735Z&X-Amz-Expires=604800&X-Amz-Signature=51bfdb6998d678014bd22f40fd32f2478a933094da20e2f4c0c47fb0117525f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Step 2 — Provision the Windows VM, cert and ports

```bash
az vm create -g $RG -n teams-media-bot --image Win2022Datacenter \
  --size Standard_D4s_v3 --admin-username azureuser --admin-password '<strong-pw>' \
  --public-ip-sku Standard --public-ip-address-dns-name elevenmediabot
az vm open-port -g $RG -n teams-media-bot --port 80,443,8445,9441 --priority 300
```

On the VM (the media platform's native code needs these — Windows Server lacks them by default):

```powershell
# VC++ runtime + Media Foundation feature (required by NativeMedia.dll)
choco install -y vcredist140
Install-WindowsFeature Server-Media-Foundation

# CA cert for the VM's FQDN via win-acme (HTTP-01), then import to LocalMachine\My
& wacs.exe --target manual --host <vm-fqdn>.cloudapp.azure.com `
  --validation selfhosting --store pfxfile --pfxfilepath C:\bot\certs --accepttos
```

Open the same ports in the **Windows firewall**, and note the cert **thumbprint** — the bot binds Kestrel (443 + a notifications port) and the media platform (8445) to it.

The VM's own `*.cloudapp.azure.com` FQDN works for a Let's Encrypt cert — no separate domain
needed.

## Step 3 — Build and run the bot

Start from Microsoft's [`microsoft-graph-comms-samples`](https://github.com/microsoftgraph/microsoft-graph-comms-samples) **PublicSamples/EchoBot** — it targets `net6.0` and builds with the .NET SDK (no Visual Studio Build Tools needed):

```powershell
git clone --depth 1 https://github.com/microsoftgraph/microsoft-graph-comms-samples.git C:\bot\samples
cd C:\bot\samples\Samples\PublicSamples\EchoBot\src
dotnet build EchoBot.sln -c Release
```

Configure the `AppSettings` section of `appsettings.json` with your `AadAppId`, `AadAppSecret`, `ServiceDnsName`/`MediaDnsName` (the VM FQDN), `CertificateThumbprint`, and ports (calling `443`, notifications `9441`, media `8445`). Add two settings for the ElevenLabs bridge below: `ElevenLabsAgentId` and `ElevenLabsOrigin` (`wss://api.elevenlabs.io`, or your residency host). Run it as a Windows scheduled task / service so it survives reboots.

Task Scheduler's default **execution time limit (72 hours)** silently kills long-running tasks — a bot started at boot dies three days later and calls fail with "we couldn't connect you". Disable the limit and add restart-on-failure:

```powershell
$s = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Seconds 0) `
  -RestartCount 999 -RestartInterval (New-TimeSpan -Minutes 1) -StartWhenAvailable
Set-ScheduledTask -TaskName EchoBot -Settings $s
```

The stock EchoBot crashes on a call placed to the standard port 443: `HttpHelpers.SetAbsoluteUri`
calls `req.Host.Port.Value`, which is null when the Host header has no explicit port. Patch it to
`req.Host.Port ?? (req.IsHttps ? 443 : 80)`.

### Swap the echo for ElevenLabs

EchoBot's audio seam is clean: `SpeechService.AppendAudioBuffer(in)` and an `OnSendMediaBufferEventArgs(out)` event. Replace its Azure-Speech body with an ElevenLabs agent WebSocket bridge that keeps the same surface:

```csharp title="SpeechService.cs — ElevenLabs bridge (core)"
public class SpeechService
{
    private readonly AppSettings _settings;
    private readonly ILogger _logger;
    private ClientWebSocket _ws;
    private bool _started;
    private bool _connecting;

    public event EventHandler<MediaStreamEventArgs> SendMediaBuffer; // agent audio -> call
    public event EventHandler FlushMedia;                            // barge-in: drop queued audio

    public SpeechService(AppSettings settings, ILogger logger) { _settings = settings; _logger = logger; }

    // Caller audio -> ElevenLabs
    public async Task AppendAudioBuffer(AudioMediaBuffer buffer)
    {
        if (!_started)
        {
            if (_connecting) return;            // a connect attempt is already in flight
            _connecting = true;
            try { await Connect(); _started = true; }
            catch (Exception ex) { _logger.Error(ex, "ElevenLabs connect failed; retry on next frame"); return; }
            finally { _connecting = false; }
        }
        if (_ws?.State != WebSocketState.Open || buffer.Length <= 0) return;
        var pcm = new byte[buffer.Length];
        Marshal.Copy(buffer.Data, pcm, 0, (int)buffer.Length);
        var msg = JsonSerializer.Serialize(new { user_audio_chunk = Convert.ToBase64String(pcm) });
        await _ws.SendAsync(Encoding.UTF8.GetBytes(msg), WebSocketMessageType.Text, true, default);
    }

    private async Task Connect()
    {
        _ws = new ClientWebSocket();
        // ElevenLabsOrigin: wss://api.elevenlabs.io, or a residency host (.eu./.in./.sg.)
        var url = $"{_settings.ElevenLabsOrigin}/v1/convai/conversation?agent_id={_settings.ElevenLabsAgentId}";
        await _ws.ConnectAsync(new Uri(url), default);
        await _ws.SendAsync(Encoding.UTF8.GetBytes(
            JsonSerializer.Serialize(new { type = "conversation_initiation_client_data" })),
            WebSocketMessageType.Text, true, default);
        _ = Task.Run(ReceiveLoop);
    }

    private async Task ReceiveLoop()
    {
        var buf = new byte[32768]; var sb = new StringBuilder();
        while (_ws.State == WebSocketState.Open)
        {
            sb.Clear(); WebSocketReceiveResult r;
            do { r = await _ws.ReceiveAsync(buf, default); sb.Append(Encoding.UTF8.GetString(buf, 0, r.Count)); }
            while (!r.EndOfMessage);

            using var doc = JsonDocument.Parse(sb.ToString());
            var type = doc.RootElement.GetProperty("type").GetString();
            if (type == "audio")            // ElevenLabs audio -> call
                Emit(Convert.FromBase64String(doc.RootElement
                    .GetProperty("audio_event").GetProperty("audio_base_64").GetString()));
            else if (type == "ping")
                await _ws.SendAsync(Encoding.UTF8.GetBytes(JsonSerializer.Serialize(new {
                    type = "pong", event_id = doc.RootElement.GetProperty("ping_event").GetProperty("event_id").GetInt32() })),
                    WebSocketMessageType.Text, true, default);
            else if (type == "interruption")  // barge-in: drop any agent audio still queued
                FlushMedia?.Invoke(this, EventArgs.Empty);
        }
    }

    // slice PCM into 20 ms / 640-byte frames the media platform expects
    private void Emit(byte[] pcm)
    {
        var all = new List<AudioMediaBuffer>(); long tick = DateTime.Now.Ticks;
        for (int off = 0; off < pcm.Length; off += 640)
        {
            var frame = new byte[640];
            Array.Copy(pcm, off, frame, 0, Math.Min(640, pcm.Length - off));
            all.AddRange(Utilities.CreateAudioMediaBuffers(frame, tick, _logger));
            tick += 20 * 10000;
        }
        if (all.Count > 0) SendMediaBuffer?.Invoke(this, new MediaStreamEventArgs { AudioMediaBuffers = all });
    }
}
```

Both sides are PCM 16 kHz mono, so it's a base64 passthrough — set the agent to `pcm_16000`. On an ElevenLabs `interruption` (barge-in), the bridge raises `FlushMedia`; wire that to your media stream so it drops any queued `AudioMediaBuffer`s, otherwise the agent keeps talking over the caller. The full message reference is in the [WebSocket docs](/docs/eleven-agents/libraries/web-sockets). End-of-call hangup and warm transfer are covered in the sections below.

The URL in `Connect()` reaches a **public** agent. For a private agent, request a short-lived
signed URL server-side — `GET /v1/convai/conversation/get-signed-url?agent_id=...` with your API
key — and connect to the returned URL instead. On [data
residency](/docs/overview/administration/data-residency), set `ElevenLabsOrigin` to your residency
host (`wss://api.eu.residency.elevenlabs.io`, `.in.`, or `.sg.`) — signed-URL requests use the
matching `https://` host.

## Step 4 — Make it callable in Teams

1. **Enable Calling** on the Azure Bot's Teams channel and set the **calling webhook** to `https://YOUR_FQDN/api/calling`:

   ```bash
   az bot msteams create -g $RG -n el-teams-agent-bot \
     --enable-calling --calling-web-hook "https://YOUR_FQDN/api/calling"
   ```

   In the portal this lives at your Azure Bot resource → **Channels** → **Microsoft Teams** → **Calling** tab:

   ![The Azure Bot Channels blade listing the Microsoft Teams channel as
   healthy](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/01115d26ab645dd6ec6569a36a918cd4de0214c79dcb0070d7a3c3a5e544c93b/assets/images/conversational-ai/teams-graph-bot-channels.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260809%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260809T080735Z&X-Amz-Expires=604800&X-Amz-Signature=1fe0cb815829a1c16d20c3415634a7c12e702e3c8f27b965288c130e8bc047a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

   ![The Teams channel Calling tab with Enable calling checked and the calling webhook
   set](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/7c4819f64878bfb152661adc948c1170f9efd48ba3d68401c4a4d4ba075951b0/assets/images/conversational-ai/teams-graph-calling-channel.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260809%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260809T080735Z&X-Amz-Expires=604800&X-Amz-Signature=97847944fcff100882d154526c574fbcd598aaca491345b36bc64d2df4585b81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

2. Build a **Teams app manifest** with `bots[0].supportsCalling: true` and the bot's app ID, then sideload it (**Apps → Manage your apps → Upload a custom app**), or publish it org-wide without the UI: `New-TeamsApp -DistributionMethod organization -Path ./bot-app.zip` (MicrosoftTeams PowerShell module).

Search the app by name in Teams and call it — the bot answers and the ElevenLabs agent speaks.

![An active Teams call with the ElevenLabs agent
bot](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/0f1fad08a091bcd20ffbbf5c3949b5503f423d8eb6298f464a870b3a0a254726/assets/images/conversational-ai/teams-graph-call-by-name.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260809%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260809T080735Z&X-Amz-Expires=604800&X-Amz-Signature=e34221a4683b1ac882d5b15ee7c99f8f5484dde2aa1f45b578f1f18fe34fb767&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

No phone number or resource account is needed for 1:1 call-by-name — those are only for PSTN
dial-in. `Calls.AccessMedia.All` is what enables the raw-audio bridge.

## Text chat (same bot)

The same Azure Bot can also answer **text** in Teams — so users can either call the agent or chat with it. Calling and messaging are independent channels on the bot: the calling webhook handles voice, and a Bot Framework **messaging endpoint** (`/api/messages`) handles chat.

![A Teams chat with the ElevenLabs agent bot answering text
messages](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/fb75ae17848916790d29c1c0a703051946902893e46ed62884742db36be453b2/assets/images/conversational-ai/teams-graph-text-chat.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260809%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260809T080735Z&X-Amz-Expires=604800&X-Amz-Signature=87b7db08c09c381941fbf836d31fff95536a40821675643a99f1866e627464d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Point the bot's messaging endpoint at whichever host serves it (the media bot, or any other service — it doesn't have to be the Windows VM):

```bash
az bot update -g $RG -n el-teams-agent-bot --endpoint "https://YOUR_FQDN/api/messages"
```

Implement the endpoint with the Bot Framework SDK and relay each message to the agent in **text mode** over the same conversation WebSocket used for voice — send a [`user_message`](/docs/eleven-agents/customization/events/client-to-server-events) event, read the [`agent_response`](/docs/eleven-agents/customization/events/client-events) event. First enable the **first message** field under the agent's [overrides](/docs/eleven-agents/customization/personalization/overrides) settings — the code below overrides it to empty so the reply is the answer to the user's message rather than the agent's greeting:

```csharp title="ChatBot.cs — Teams text chat -> ElevenLabs (text mode)"
public class ChatBot : ActivityHandler
{
    private readonly AppSettings _settings;
    public ChatBot(AppSettings settings) => _settings = settings;

    protected override async Task OnMessageActivityAsync(
        ITurnContext<IMessageActivity> turn, CancellationToken ct)
    {
        var reply = await AskAgent(turn.Activity.Text, ct);
        await turn.SendActivityAsync(MessageFactory.Text(reply), ct);
    }

    private async Task<string> AskAgent(string text, CancellationToken ct)
    {
        using var ws = new ClientWebSocket();
        var url = $"{_settings.ElevenLabsOrigin}/v1/convai/conversation?agent_id={_settings.ElevenLabsAgentId}";
        await ws.ConnectAsync(new Uri(url), ct);
        // Suppress the agent's greeting: with no override, the first agent_response is the
        // configured first message, not the answer to this user_message.
        await Send(ws, new
        {
            type = "conversation_initiation_client_data",
            conversation_config_override = new { agent = new { first_message = "" } },
        }, ct);
        await Send(ws, new { type = "user_message", text }, ct);

        var buf = new byte[16384]; var sb = new StringBuilder();
        while (ws.State == WebSocketState.Open)
        {
            sb.Clear(); WebSocketReceiveResult r;
            do { r = await ws.ReceiveAsync(buf, ct); sb.Append(Encoding.UTF8.GetString(buf, 0, r.Count)); }
            while (!r.EndOfMessage);

            using var doc = JsonDocument.Parse(sb.ToString());
            switch (doc.RootElement.GetProperty("type").GetString())
            {
                case "agent_response":
                    return doc.RootElement.GetProperty("agent_response_event")
                              .GetProperty("agent_response").GetString();
                case "ping":
                    await Send(ws, new { type = "pong", event_id = doc.RootElement
                        .GetProperty("ping_event").GetProperty("event_id").GetInt32() }, ct);
                    break;
            }
        }
        return "Sorry, I couldn't reach the agent.";
    }

    private static Task Send(ClientWebSocket ws, object msg, CancellationToken ct) =>
        ws.SendAsync(Encoding.UTF8.GetBytes(JsonSerializer.Serialize(msg)),
            WebSocketMessageType.Text, true, ct);
}
```

Register it the standard way (a `CloudAdapter`, the bot via `AddTransient<IBot, ChatBot>()`, and a `/api/messages` controller), and add chat scopes to the manifest's bot entry:

```json
"bots": [
  { "botId": "YOUR_APP_ID", "supportsCalling": true, "scopes": ["personal", "team", "groupChat"] }
]
```

The snippet opens a fresh conversation per message, so each turn is independent. For chat
**memory**, keep one WebSocket open per Teams `conversation.id` (reuse it across turns) and reap
idle sessions — the agent then remembers earlier messages in that chat. The `first_message`
override must be enabled under the agent's
[overrides](/docs/eleven-agents/customization/personalization/overrides) settings — the server
**closes the conversation** if a disallowed override is sent. If you can't enable it, omit the
override and instead discard the first `agent_response` of each session (the greeting) and return
the next one.

If chat replies never arrive, enable the **`agent_response`** [client
event](/docs/eleven-agents/customization/events/client-events) in the agent's **Advanced**
settings — text responses are delivered through that event.

## End of call

When ElevenLabs ends the conversation (its **End Call** tool closes the WebSocket), hang up the Teams leg:

```csharp
await this.Call.DeleteAsync(); // after a short delay so the goodbye audio finishes
```

## Warm transfer to a human

The agent fires a custom `transfer_to_human` client tool; the bot **invites a Teams user** into the live call (consultative add), then steps back:

```csharp
var target = new IdentitySet { User = new Identity { Id = humanObjectId } };
await this.Call.Participants.InviteAsync(target, replacesCallId: null);
// suppress the end-call hangup while transferring, and mute the bot
```

Consultative transfer (`replacesCallId`) requires both parties be Teams users in the **same
tenant**; PSTN transfer targets require an application instance. To brief the human first, pass a
`reason` parameter from the agent and play it to the human before bridging.

## Troubleshooting

#### \`MediaPlatform needs a system with at least 2 cores\`

The VM has only one physical core. Resize to ≥ 2 physical cores (e.g. `D4s_v3`) and restart.

#### \`Unable to load DLL 'NativeMedia'\`

Install the **VC++ Redistributable** (`vcredist140`) and the **Server-Media-Foundation** Windows
feature, then restart the bot.

#### Incoming call returns 500 / call won't connect

The EchoBot port-null bug on 443 — patch `HttpHelpers.SetAbsoluteUri` (see Step 3). Also confirm
the cert is CA-signed and reachable on 443.

#### Calling the bot says 'we couldn't connect you'

Confirm Calling is enabled on the Teams channel with the correct `/api/calling` webhook, the
Graph `Calls.AccessMedia.All` permission is consented, and ports 443/8445/9441 are open on both
the NSG and the Windows firewall. If calling **used to work and stopped**, check the bot process
is still running on the VM — Task Scheduler's default 72-hour execution limit kills it a few
days after boot (see the warning in Step 3).

## Useful links

* [Calls & meetings bots overview](https://learn.microsoft.com/en-us/microsoftteams/platform/bots/calls-and-meetings/calls-meetings-bots-overview)
* [Real-time media concepts](https://learn.microsoft.com/en-us/microsoftteams/platform/bots/calls-and-meetings/real-time-media-concepts)
* [Register a calling bot](https://learn.microsoft.com/en-us/microsoftteams/platform/bots/calls-and-meetings/registering-calling-bot)
* [microsoft-graph-comms-samples (EchoBot)](https://github.com/microsoftgraph/microsoft-graph-comms-samples)
* [call: transfer (consultative)](https://learn.microsoft.com/en-us/graph/api/call-transfer)
* [Agent WebSocket protocol](/docs/eleven-agents/libraries/web-sockets)
