---
title: "Microsoft Teams"
source: https://elevenlabs.io/docs/eleven-agents/phone-numbers/microsoft-teams/overview.md
path: docs/eleven-agents/phone-numbers/microsoft-teams/overview
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Microsoft Teams

## Overview

Microsoft Teams has no built-in ElevenAgents connector. How you make an ElevenLabs agent reachable in Teams depends on how users should reach it and what infrastructure you can run:

* a web widget embedded in a Teams tab,
* a phone number the agent answers (Azure Communication Services),
* a bot users call by name in Teams (Microsoft Graph media bot).

## Choosing an approach

#### [Widget tab](/docs/eleven-agents/phone-numbers/microsoft-teams/widget-tab)

Embed the ElevenLabs agent widget in a Teams tab. Click-to-talk in the Teams client. No
telephony, no phone number.

#### [Phone number (ACS)](/docs/eleven-agents/phone-numbers/microsoft-teams/azure-communication-services)

Users dial a phone number that the agent answers, via Azure Communication Services Call
Automation. PSTN, contact-center style.

#### [Calling bot (call by name)](/docs/eleven-agents/phone-numbers/microsoft-teams/graph-media-bot)

Call or chat with the agent by name in Teams, like a colleague — a Microsoft Graph media bot for
voice plus Bot Framework messaging for text.

## Comparison

|                        | Widget tab                            | Phone number (ACS)            | Calling bot                       |
| ---------------------- | ------------------------------------- | ----------------------------- | --------------------------------- |
| How users reach it     | Open a Teams tab, click to talk       | Dial a phone number           | Search the bot by name → call     |
| Transport              | Web widget (mic in the Teams webview) | PSTN → ACS media streaming    | Teams VoIP → Graph media platform |
| Phone number required  | No                                    | Yes (ACS number)              | No                                |
| Hosting                | Static HTML on any HTTPS host         | Linux bridge (Container Apps) | **Windows** media bot (VM)        |
| Effort                 | Lowest                                | Medium                        | Highest (.NET on Windows)         |
| Warm transfer to human | Not built-in                          | Yes (add participant)         | Yes (invite Teams user)           |
| Text chat in Teams     | No                                    | No                            | Yes (Bot Framework messaging)     |

## At a glance

* **A fast internal demo or self-service assistant** — use the [widget tab](/docs/eleven-agents/phone-numbers/microsoft-teams/widget-tab).
* **Customers calling a number that the agent answers (IVR / contact center)** — use [Azure Communication Services](/docs/eleven-agents/phone-numbers/microsoft-teams/azure-communication-services).
* **Colleagues calling the agent by name inside Teams** — use the [Graph calling bot](/docs/eleven-agents/phone-numbers/microsoft-teams/graph-media-bot).

Each approach has different access requirements — see the **Permissions & roles** section in each
guide. In short: the widget needs Teams custom-app upload; ACS needs a paid subscription +
Contributor; the calling bot needs an Azure Bot, Graph `Calls.AccessMedia.All`, and **admin
consent** (Global Admin / Privileged Role Admin).

## Useful links

* [ElevenLabs widget customization](/docs/eleven-agents/customization/widget)
* [Agent WebSocket protocol](/docs/eleven-agents/libraries/web-sockets)
* [ElevenLabs SIP trunking](/docs/eleven-agents/phone-numbers/sip-trunking)
* [Azure Communication Services Call Automation](https://learn.microsoft.com/en-us/azure/communication-services/concepts/call-automation/call-automation)
* [Microsoft Graph calls & meetings bots](https://learn.microsoft.com/en-us/microsoftteams/platform/bots/calls-and-meetings/calls-meetings-bots-overview)
