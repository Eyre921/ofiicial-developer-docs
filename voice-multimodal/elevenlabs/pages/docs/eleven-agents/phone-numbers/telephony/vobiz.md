---
title: "Vobiz"
source: https://elevenlabs.io/docs/eleven-agents/phone-numbers/telephony/vobiz.md
path: docs/eleven-agents/phone-numbers/telephony/vobiz
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Vobiz

> **Note**
>
> Before following this guide, consider reading the [SIP trunking guide](/docs/eleven-agents/phone-numbers/sip-trunking) to understand how ElevenLabs supports SIP
> trunks.

## Overview

This guide explains how to connect your Vobiz SIP trunks directly to ElevenAgents. This integration allows you to use your existing Vobiz phone numbers and infrastructure while leveraging ElevenLabs' voice AI capabilities for both inbound and outbound calls.

## How SIP trunking with Vobiz works

SIP trunking establishes a direct connection between your Vobiz telephony infrastructure and the ElevenLabs platform:

1. **Inbound calls**: Calls to your Vobiz phone number are routed from your Vobiz SIP trunk to the ElevenLabs platform using the ElevenLabs origination URI (`sip.rtc.elevenlabs.io:5060`). You configure this in your Vobiz account.
2. **Outbound calls**: Calls initiated by ElevenAgents are routed to your Vobiz SIP trunk using your Vobiz SIP domain (`<your_unique_domain>.sip.vobiz.ai`), enabling your agents to place outgoing calls.
3. **Authentication**: Connection security for signaling is maintained through SIP digest authentication (username and password) or Access Control List (ACL) authentication based on the signaling source IP.
4. **Signaling and media**: The initial call setup (signaling) uses TCP on port 5060. Once the call is established, the audio data (RTP stream) is transmitted over UDP.

## Requirements

Before setting up the Vobiz SIP trunk integration, ensure you have:

1. An active [Vobiz account](https://console.vobiz.ai/auth/signup) with SIP trunking enabled.
2. At least one Vobiz [phone number](https://www.vobiz.ai/docs/account-phone-number/list-inventory-numbers) to connect to ElevenLabs.
3. An ElevenLabs account with an [agent](/docs/eleven-agents/quickstart) configured in ElevenAgents.
4. Administrator access to the [Vobiz Console](https://console.vobiz.ai) and your SIP trunk configuration.
5. Appropriate firewall settings to allow SIP and RTP traffic between ElevenLabs and Vobiz.

## Configuring Vobiz SIP trunks

This section provides instructions for configuring inbound and outbound SIP trunks in Vobiz before connecting them to ElevenLabs.

### Setting up inbound trunks (calls from Vobiz to ElevenLabs)

#### Access Vobiz Console

Sign in to the [Vobiz Console](https://console.vobiz.ai).

#### Navigate to Inbound Trunks

In the sidebar, navigate to **SIP Trunk** > **Inbound Trunks** > **Trunks**.

#### Configure inbound SIP URI

In your Vobiz inbound SIP trunk configuration (or Application Answer URL), point incoming calls to the ElevenLabs SIP URI:

| Setting   | Value                        |
| --------- | ---------------------------- |
| SIP URI   | `sip.rtc.elevenlabs.io:5060` |
| Transport | `TCP`                        |

Set `sip.rtc.elevenlabs.io:5060` as the trunk's **Primary URI** and save the trunk configuration.

> **Note**
>
> `sip.rtc.elevenlabs.io:5060` is the default global (non-static) endpoint. If your workspace uses an isolated [data residency](/docs/overview/administration/data-residency) deployment (India, Singapore, or Europe) or has [static IP SIP servers](/docs/eleven-agents/phone-numbers/sip-trunking) enabled, use the corresponding SIP URI instead:
>
> * **Data residency (non-static)**: `sip.rtc.in.residency.elevenlabs.io:5060` (India), `sip.rtc.sg.residency.elevenlabs.io:5060` (Singapore), or `sip.rtc.eu.residency.elevenlabs.io:5060` (Europe)
> * **Global (static)**: `sip-static.rtc.elevenlabs.io:5060`
> * **Data residency (static)**: `sip-static.rtc.in.residency.elevenlabs.io:5060` (India), `sip-static.rtc.sg.residency.elevenlabs.io:5060` (Singapore), or `sip-static.rtc.eu.residency.elevenlabs.io:5060` (Europe)

#### Assign phone number to trunk

Link the Vobiz phone number you want to route to your inbound trunk and save the configuration.

### Setting up outbound trunks (calls from ElevenLabs to Vobiz)

#### Access Vobiz Console

Sign in to the [Vobiz Console](https://console.vobiz.ai).

#### Navigate to Outbound Trunks

In the sidebar, navigate to **SIP Trunk** > **Outbound Trunks** > **Trunks**.

#### Configure outbound SIP trunk

1. Select your outbound trunk (or create a new outbound trunk and provide a descriptive name).
2. Scroll to the **Authentication & Linking** section.
3. Configure your SIP trunk username and password for outbound digest authentication, and link your Vobiz phone number.

#### Note your trunk credentials

From the **Authentication & Linking** section of your trunk, record the following details. You will need them when importing the number in ElevenLabs:

* **SIP Trunk Address**: `<your_unique_domain>.sip.vobiz.ai`
* **SIP Trunk Username**: `<your_username>`
* **SIP Trunk Password**: `<your_password>`

## Complete setup in ElevenLabs

Follow the [SIP trunking guide](/docs/eleven-agents/phone-numbers/sip-trunking#setting-up-sip-trunking) to import your Vobiz phone number in the [Phone Numbers dashboard](https://elevenlabs.io/app/agents/phone-numbers) using the Vobiz-specific inbound and outbound settings below.

### Inbound configuration (calls from Vobiz to ElevenLabs)

In the basic and **Inbound Configuration** sections of the **Import SIP Trunk** dialog:

| Field                | Value                                                                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Label**            | A descriptive name for the phone number (for example, `Vobiz Main Line`)                                                                         |
| **Phone Number**     | Your Vobiz number in E.164 format with `+` (for example, `+911234567890`) or local format (`01234567890`), matching what your Vobiz trunk sends  |
| **Media Encryption** | `Allowed` (or `Disabled` if your Vobiz trunk uses unencrypted RTP)                                                                               |
| **Authentication**   | Leave disabled (off) unless you have configured digest authentication on your Vobiz inbound trunk. Use outbound authentication for Vobiz trunks. |

Leave the optional **Allowed Numbers**, **Allowed Source IP Addresses**, and **Remote Domains** settings disabled unless your deployment requires inbound filtering or TLS domain validation.

![Import SIP Trunk dialog showing basic phone number details and Inbound Configuration
settings](/docs/_fern-files/_img/80bfa38758a57755fa5cf4ac55c7fb6eb42f4bb59520c416462a8390b2101a89.webp)

### Outbound configuration (calls from ElevenLabs to Vobiz)

In the **Outbound Configuration** section of the **Import SIP Trunk** dialog, enter your Vobiz outbound trunk credentials:

| Field                  | Value                                                                           |
| ---------------------- | ------------------------------------------------------------------------------- |
| **Address**            | `<your_unique_domain>.sip.vobiz.ai` (hostname only, without the `sip:` prefix)  |
| **Transport Type**     | `TCP`                                                                           |
| **Media Encryption**   | `Allowed` (or `Disabled` to match your Vobiz trunk configuration)               |
| **Enabled Codecs**     | `G.722`, `PCMU`, `PCMA`                                                         |
| **Authentication**     | Enabled                                                                         |
| **SIP Trunk Username** | `<your_username>` (from your Vobiz outbound trunk **Authentication & Linking**) |
| **SIP Trunk Password** | `<your_password>` (from your Vobiz outbound trunk **Authentication & Linking**) |

![Outbound Configuration section with Vobiz SIP trunk address, TCP transport, and authentication
fields](/docs/_fern-files/_img/935e119e68aea8279285b8d7404440e62e93956c8285fd704327cdb49a80b936.webp)

After importing the number, see [Assigning agents to phone numbers](/docs/eleven-agents/phone-numbers/sip-trunking#assigning-agents-to-phone-numbers) in the SIP trunking guide to assign your agent.

> **Warning**
>
> Once you have set up your Vobiz SIP trunk, see the [SIP trunking guide](/docs/eleven-agents/phone-numbers/sip-trunking) for advanced configuration options such as
> media encryption, custom SIP headers, and static IP allowlisting.

## Troubleshooting

#### SIP 408 request timeout

The Vobiz trunk cannot reach ElevenLabs SIP servers:

* Verify the SIP trunk address is formatted as `<your_unique_domain>.sip.vobiz.ai` without a `sip:` prefix.
* Check that the transport type is set to `TCP`.
* Confirm your Vobiz trunk status is `active` in the [Vobiz Console](https://console.vobiz.ai).

#### SIP authentication failed

The SIP trunk username or password does not match:

* Verify the username and password in the [Vobiz Console](https://console.vobiz.ai) under **Trunks** > **Authentication & Linking**.
* Ensure the credentials match case-sensitively.
* Re-enter the credentials in the ElevenAgents phone number configuration.

#### Call connects but is silent

The agent configuration or voice setting is incomplete:

* Verify the agent has a **First message** configured.
* Confirm the agent has a valid voice selected and test the voice in the ElevenAgents dashboard.
* Check the conversation logs in **Call History** for errors.

#### Call does not connect

The phone number format or trunk status is invalid:

* Use E.164 format with a leading `+` (for example, `+919988776655`) or local format without `+` (for example, `09988776655`).
* Verify your Vobiz trunk is active and has sufficient account balance.

## Useful links

* [SIP trunking guide](/docs/eleven-agents/phone-numbers/sip-trunking)
* [SIP reference](/docs/eleven-agents/phone-numbers/sip-reference)
* [Vobiz ElevenLabs integration overview](https://www.vobiz.ai/docs/integrations/elevenlabs)
* [Vobiz ElevenLabs API setup guide](https://www.vobiz.ai/docs/integrations/elevenlabs-api)
* [Vobiz phone numbers documentation](https://www.vobiz.ai/docs/account-phone-number/list-inventory-numbers)
