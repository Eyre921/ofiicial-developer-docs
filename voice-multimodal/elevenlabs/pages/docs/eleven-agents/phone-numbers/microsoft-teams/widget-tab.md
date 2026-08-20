---
title: "Widget tab"
source: https://elevenlabs.io/docs/eleven-agents/phone-numbers/microsoft-teams/widget-tab.md
path: docs/eleven-agents/phone-numbers/microsoft-teams/widget-tab
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Widget tab

## Overview

Host a small HTML page that loads the [agent widget](/docs/eleven-agents/customization/widget) and surface it as a **Teams tab**. Users open the tab and talk to the agent in the Teams client — no phone number or telephony. This is the lightest-weight approach; use it for internal self-service assistants and demos.

![The ElevenLabs agent widget open in a Microsoft Teams
tab](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/8fedd2110258c6751012619128601214cdfcd4a11aaa832f62050c00c52106e7/assets/images/conversational-ai/teams-widget-tab.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260820T100014Z&X-Amz-Expires=604800&X-Amz-Signature=78732daece818a41c3cff9acda05fb091f6402e64a5f4f06c92311a357938382&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## How it works

The widget is a web component. Teams renders a tab's `contentUrl` inside a webview (iframe), so the widget runs exactly as it would on a website — including microphone capture, provided the page is allowed to embed in Teams and is granted media permission.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/c90698c01d5e874b3a3fa8a07af5ef64620e0fe8a602155aed31bd3f1ce06273/assets/images/conversational-ai/teams-widget-architecture.svg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260820T100014Z&X-Amz-Expires=604800&X-Amz-Signature=7a3f9e28b2231a11ec883e5b34ecf6a9f51baf121fb7eaebde90300aeda3fa45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Teams user opens a tab whose webview iframes a hosted page running the ElevenLabs agent widget, which streams audio to ElevenLabs" />

Teams will **not** execute a raw `<script>` pasted into a chat, message, or Loop page. The widget
script must live on a page **you host**, which Teams then embeds as a tab.

## Requirements

1. A **public** [ElevenLabs agent](/docs/eleven-agents/quickstart) with authentication disabled (Advanced tab of the agent settings). Widgets require this.
2. An HTTPS host for a single static HTML file (Vercel, Netlify, Cloudflare Pages, Azure Static Web Apps, etc.).
3. Permission in your tenant to upload a custom Teams app ([Teams admin center → Manage apps](https://admin.teams.microsoft.com/policies/manage-apps) → custom app upload), if you use the custom-tab option.

## Step 1 — Create the widget page

Create `agent-widget.html` with the widget embed and your agent ID:

```html title="agent-widget.html"
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Voice Agent</title>
  </head>
  <body style="margin:0">
    <elevenlabs-convai
      agent-id="<replace-with-agent_7101k5zvyjhmfg983brhmhkd98n6>"
    ></elevenlabs-convai>
    <script
      src="https://unpkg.com/@elevenlabs/convai-widget-embed"
      async
      type="text/javascript"
    ></script>
  </body>
</html>
```

Deploy it to your HTTPS host and confirm it loads and the mic works in a normal browser first.

If your workspace is on a [data residency](/docs/overview/administration/data-residency)
environment, add the widget's `server-location` attribute so it connects to your region — see
[widget customization](/docs/eleven-agents/customization/widget) for the supported values.

Test the page standalone in a browser before touching Teams. If the mic doesn't work there, it
won't work in the Teams webview either.

## Step 2 — Add it to Teams

You have two options, in increasing order of reliability for voice.

### Option A — Website tab (quickest, may be link-only)

In a chat or channel, **+ Add a tab → Website**, paste your HTTPS URL, and save.

The built-in **Website** tab sometimes opens the page as an external link rather than embedding it
— and even when embedded, microphone access in the Teams desktop webview can be blocked. If voice
fails, use Option B.

### Option B — Custom tab app (recommended for voice)

A tiny custom Teams app declares the page as a static tab **and** requests media permission, which is what makes the microphone work reliably inside Teams.

#### Create the manifest

Create `manifest.json`. Replace `your-domain.com` with your host and set a unique GUID for `id`:

```json title="manifest.json"
{
  "$schema": "https://developer.microsoft.com/json-schemas/teams/v1.19/MicrosoftTeams.schema.json",
  "manifestVersion": "1.19",
  "version": "1.0.0",
  "id": "11111111-1111-1111-1111-111111111111",
  "developer": {
    "name": "ElevenLabs",
    "websiteUrl": "https://your-domain.com",
    "privacyUrl": "https://your-domain.com/privacy",
    "termsOfUseUrl": "https://your-domain.com/terms"
  },
  "name": { "short": "Voice Agent", "full": "ElevenLabs Voice Agent" },
  "description": {
    "short": "ElevenLabs voice agent",
    "full": "Embedded ElevenLabs voice agent"
  },
  "icons": { "outline": "outline.png", "color": "color.png" },
  "accentColor": "#000000",
  "staticTabs": [
    {
      "entityId": "voice-agent",
      "name": "Voice Agent",
      "contentUrl": "https://your-domain.com/agent-widget.html",
      "websiteUrl": "https://your-domain.com/agent-widget.html",
      "scopes": ["personal"]
    }
  ],
  "devicePermissions": ["media"],
  "validDomains": ["your-domain.com", "unpkg.com", "elevenlabs.io", "*.elevenlabs.io"]
}
```

The key fields for voice are **`devicePermissions: ["media"]`** (microphone) and listing every domain the page touches in **`validDomains`** (`unpkg.com` for the widget script, `*.elevenlabs.io` for the agent).

#### Package the app

Add a `color.png` (192×192) and `outline.png` (32×32, transparent) next to the manifest, then zip the manifest and the two icons at the **root** of the archive:

```bash
zip -j voice-agent.zip manifest.json color.png outline.png
```

#### Upload and open

In Teams: **Apps → Manage your apps → Upload an app → Upload a custom app**, select `voice-agent.zip`, then open the **Voice Agent** tab and grant microphone access when prompted.

Teams admins can skip the client UI and publish the app to the whole org from PowerShell — it then shows up for everyone under **Apps → Built for your org**:

```powershell
Connect-MicrosoftTeams
New-TeamsApp -DistributionMethod organization -Path ./voice-agent.zip
```

If no prompt appears, open the tab's dropdown and choose **App permissions** to grant microphone access manually:

![The Teams tab dropdown menu with App permissions
highlighted](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/308d95d230864371f4ad2cd8b329c503e672878788a1fdcbc49ab2ce6aa8ce7d/assets/images/conversational-ai/teams-widget-app-permissions.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260820%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260820T100014Z&X-Amz-Expires=604800&X-Amz-Signature=1569529f5bed195596ead973d1b17dbec520a2c7df12e43d577942c75562004e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Step 3 — Allow Teams to embed the page

Your host must permit Teams to iframe the page. If you control response headers, set:

```http
Content-Security-Policy: frame-ancestors 'self' https://teams.microsoft.com https://*.teams.microsoft.com https://*.cloud.microsoft;
```

If Teams keeps opening the page in a browser instead of embedding it, the page is being blocked from iframe embedding — fix the CSP / `X-Frame-Options` on your host.

## Troubleshooting

#### The tab opens the page in a browser instead of embedding it

The page is blocked from being iframed. Remove any `X-Frame-Options: DENY/SAMEORIGIN` and set
the `frame-ancestors` CSP shown above to allow the Teams domains. The custom tab app (Option B)
is also more reliable than the built-in Website tab.

#### The widget loads but the microphone doesn't work

This is the Teams webview permission layer. Use the **custom tab app** with
`"devicePermissions": ["media"]`, and grant the app microphone permission in Teams (tab dropdown
→ **App permissions**). Teams web and Teams desktop behave differently — test both. As a
fallback, offer an "Open in browser" link.

#### The widget never appears

Confirm the agent is **public** with authentication disabled (agent **Advanced** settings), and
that `unpkg.com` and `*.elevenlabs.io` are in the manifest `validDomains`.

## Useful links

* [Widget customization](/docs/eleven-agents/customization/widget)
* [Teams tab requirements](https://learn.microsoft.com/en-us/microsoftteams/platform/tabs/how-to/tab-requirements)
* [Create a personal tab](https://learn.microsoft.com/en-us/microsoftteams/platform/tabs/how-to/create-personal-tab)
* [Teams device permissions](https://learn.microsoft.com/en-us/microsoftteams/platform/concepts/device-capabilities/native-device-permissions)
