---
title: "Bandwidth SIP trunking"
source: https://elevenlabs.io/docs/eleven-agents/phone-numbers/telephony/bandwidth.md
path: docs/eleven-agents/phone-numbers/telephony/bandwidth
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Bandwidth SIP trunking

Before following this guide, consider reading the [SIP trunking guide](/docs/eleven-agents/phone-numbers/sip-trunking) to understand how ElevenLabs supports SIP
trunks.

## Overview

This guide explains how to connect your Bandwidth SIP trunks directly to ElevenLabs Agents. This integration allows you to use your existing Bandwidth phone numbers and infrastructure while leveraging ElevenLabs' advanced voice AI capabilities, for both inbound and outbound calls.

## How SIP trunking with Bandwidth works

SIP trunking establishes a direct connection between your Bandwidth telephony infrastructure and the ElevenLabs platform:

1. **Inbound calls**: Calls from Bandwidth are routed to the ElevenLabs platform using our origination URI. You configure this in the Bandwidth App using a Voice Configuration Package (VCP).
2. **Outbound calls**: Calls initiated by ElevenLabs are routed to your Bandwidth SIP trunk using your realm FQDN or termination SBC addresses, enabling your agents to make outgoing calls.
3. **Authentication**: Bandwidth provides SIP-based authentication for Unified Communications (UC) trunks, leveraging digest authentication through SIP credentials (network bridge). This method is essential for facilitating outbound calls from ElevenLabs and ensuring secure communication.
4. **Signaling and media**: The initial call setup (signaling) uses UDP/TLS. Once the call is established, the actual audio data (RTP stream) is transmitted over UDP.

## Requirements

Before setting up the Bandwidth SIP trunk integration, ensure you have:

1. An active ElevenLabs account
2. An active Bandwidth Universal Platform account with SIP trunking enabled (with sip-auth enabled)
3. At least one phone number purchased or ported into your Bandwidth account
4. Administrator access on your account in the [Bandwidth App](https://app.bandwidth.com/)

## Configuring inbound calls (Bandwidth to ElevenLabs)

Configure Bandwidth origination settings to route inbound calls to ElevenLabs.

#### Sign in to the Bandwidth App

Log in to the [Bandwidth App](https://app.bandwidth.com/).

#### Create Voice Configuration Package

1. Navigate to the **Service Management** tab and select **Voice Configuration**.
2. Click **Create New** to start creation of a new Voice Configuration Package.
3. Enter a unique Package Name.
4. Click **Add Route**.
5. Choose **Route to Domain Name**.
6. Enter the FQDN provided by ElevenLabs in the field provided. This is typically `sip.rtc.elevenlabs.io`. If your ElevenLabs account uses an isolated data residency region or uses the static SIP infrastructure, use the corresponding SIP endpoint instead. See [data residency](/docs/overview/administration/data-residency) for available regions.
7. Click **Save** to finish creating the Voice Configuration Package.

Please refer to the [Bandwidth VCP documentation](https://dev.bandwidth.com/docs/universal-platform/create-a-vcp) for additional
details.

#### Verify E.164 formatting

Bandwidth sends inbound calls in E.164 format. When importing the phone number in ElevenLabs, use the same format with a leading `+` (for example, `+15551234567`).

## Configuring outbound calls (ElevenLabs to Bandwidth)

For outbound calls, ElevenLabs must authenticate with Bandwidth. The recommended approach is SIP digest authentication using a realm and credentials.

#### Create a realm

1. In the Bandwidth App, select **Account** and click **SIP Credentials**.
2. Scroll to **Manage Realms** and click **Add**.
3. Enter a realm name and optional description, then click **Add**.

Bandwidth creates a realm FQDN in the format `{realmname}.{hash}.auth.bandwidth.com`. Note this FQDN — you will use it as the outbound address in ElevenLabs.

If you do not see the **SIP Credentials** tab, contact your Bandwidth Account Manager or open a
ticket with Bandwidth Support to enable SIP authentication on your account.

#### Create SIP credentials

1. In the **SIP Credentials** section, click **Add**.
2. Enter a **Username** and **Password**.
3. Select the realm you created in the previous step.
4. Click **Add SIP Credentials**.

Store the username and password securely. You will enter them in the ElevenLabs SIP trunk configuration.

#### Note your realm FQDN

Your outbound termination address is the realm FQDN displayed after creation (for example, `myrealm-a1b2c3.auth.bandwidth.com`). Enter this hostname in the **Address** field when configuring outbound settings in ElevenLabs.

To verify the SBC IP addresses associated with your realm, run an SRV lookup:

```bash
nslookup -type=SRV _sip._{udp/tls}.{realm_FQDN}
```

Bandwidth provides a mated pair of SBC IPs for redundancy. Both must be reachable for outbound traffic.

## Complete setup in ElevenLabs

After configuring these settings in the Bandwidth App, import your phone number in ElevenLabs:

#### Import the SIP trunk phone number

Follow the [SIP trunking guide](/docs/eleven-agents/phone-numbers/sip-trunking) to import your Bandwidth phone number. Use the following settings:

* **Transport type**: UDP (or TLS if your Bandwidth trunk uses encrypted signaling)
* **Media encryption**: Match your Bandwidth trunk configuration
* **Outbound address**: Your realm FQDN (for example, `myrealm-a1b2c3.auth.bandwidth.com`)
* **SIP trunk username and password**: The credentials created in the Bandwidth App

#### Assign an agent

After importing, assign an agent to the phone number in the [Phone Numbers dashboard](https://elevenlabs.io/app/agents/phone-numbers).

After setting up your Bandwidth SIP trunk, follow the [SIP trunking guide](/docs/eleven-agents/phone-numbers/sip-trunking) to complete the configuration in
ElevenLabs.

## Troubleshooting

#### Inbound calls fail to connect

* Verify that `sip.rtc.elevenlabs.io` is entered as the route destination in your Bandwidth VCP origination settings.
* Confirm the phone number is assigned to the VCP with the correct origination settings.
* Ensure the phone number format in ElevenLabs matches the E.164 format Bandwidth sends (with a leading `+`).
* Check that your firewall allows SIP signaling traffic on the configured transport protocol and port (5060 for UDP, 5061 for TLS) and that RTP ports are not blocked.

#### Outbound calls receive 407 or authentication errors

* Confirm the **SIP trunk username**, **password**, and **realm** in ElevenLabs match the credentials created in the Bandwidth App.
* Verify the **Address** field contains only the realm FQDN hostname, without the `sip:` prefix.
* Ensure the transport type in ElevenLabs outbound settings matches your Bandwidth trunk configuration (UDP or TLS).

#### One-way audio or no audio

* Confirm RTP ports are open for media traffic and not blocked by your firewall.
* Verify G711ulaw codec compatibility. Bandwidth and ElevenLabs both support G711.

## FAQ

#### What signaling transport and ports does Bandwidth require?

Bandwidth and ElevenLabs use UDP on port 5060 for SIP signaling. If your Bandwidth trunk is configured for encrypted transport, use TLS on port 5061 instead.

#### What phone number format should I use?

Use E.164 format with a leading `+` (for example, `+19192971100`). Bandwidth sends and expects numbers in this format.

#### Which audio codecs are compatible?

ElevenLabs supports G711 and G722. Bandwidth supports G711ulaw and G729a. G711ulaw is the recommended codec for compatibility between both platforms.

## Useful links

* [SIP trunking guide](/docs/eleven-agents/phone-numbers/sip-trunking)
* [SIP reference](/docs/eleven-agents/phone-numbers/sip-reference)
* [Bandwidth UC trunking integration guide](https://www.bandwidth.com/support/en/articles/12822954-uc-trunking-integration-guide)
* [Bandwidth SIP authentication setup](https://www.bandwidth.com/support/en/articles/12823069-sip-authentication-network-bridge-setup-and-configuration)
* [Managing Bandwidth Voice Configuration Packages](https://www.bandwidth.com/support/en/articles/12823404-managing-voice-configuration-packages-on-the-universal-platform)
* [Universal Platform Guide](https://www.bandwidth.com/support/en/collections/12889706-universal-platform)
