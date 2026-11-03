---
title: "FreePBX and Asterisk"
source: https://elevenlabs.io/docs/reception-ai/integrations/freepbx.md
path: docs/reception-ai/integrations/freepbx
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# FreePBX and Asterisk

Your PBX keeps its carrier and numbers, and passes the calls you choose to Reception.ai over a [SIP trunk](/docs/reception-ai/phone-numbers/bring-your-own-number#sip-trunk). You add a second trunk on the PBX that points at Reception.ai, then route a DID, a time condition, or an IVR option to it.

## Before you start

* FreePBX 15 or later, or Asterisk with PJSIP, reachable from the internet.
* A static public IP address for the PBX. Reception.ai only accepts calls from addresses you allow.
* Someone comfortable with your PBX's trunks, routes and firewall.

## Setup

### Add the SIP trunk in Reception.ai

Go to **Integrations**, select **Add integration**, and choose **SIP Trunk**. Under **Inbound allowed addresses**, add your PBX's public IP address. If you also set an inbound username and password, use the same pair on the PBX trunk below.

### Add the number

Go to **Receptionists**, select the **Phone** tile, enter the number callers dial, with its country code, and select **Add SIP Trunk number**. Reception.ai shows the SIP server host and the request URI to use.

### Turn on TCP in FreePBX

Reception.ai doesn't accept UDP. In FreePBX, go to **Settings** → **Asterisk SIP Settings** → **SIP Settings \[chan_pjsip]**, set the **tcp** transport to **Yes**, and select **Submit** and **Apply Config**. Restart Asterisk so the new transport loads. TLS also works if you've set up a certificate in **Certificate Management**.

### Create the trunk to Reception.ai

Go to **Connectivity** → **Trunks** → **Add Trunk** → **Add SIP (chan_pjsip) Trunk**. On the **General** tab, enter a **Trunk Name**, such as `reception`. Set **CID Options** to **Allow Any CID**, so the receptionist sees each caller's own number. On the **pjsip Settings** tab:

| Field               | Value                                                                                                     |
| ------------------- | --------------------------------------------------------------------------------------------------------- |
| **Registration**    | **None**                                                                                                  |
| **Authentication**  | **None**, or **Outbound** with **Username** and **Secret** if you set inbound credentials in Reception.ai |
| **SIP Server**      | The Reception.ai SIP server host                                                                          |
| **SIP Server Port** | `5060` for TCP, or `5061` for TLS                                                                         |
| **Transport**       | The TCP (or TLS) transport, for example `0.0.0.0-tcp`                                                     |

### Add an outbound route that sends +E.164

Go to **Connectivity** → **Outbound Routes** and add a route named `Reception` that uses only the `reception` trunk. Add a dial pattern with an unused **prefix**, such as `88`, a **match pattern** of `X.`, and a **prepend** of `+`. A call to `8814155550123` then leaves the trunk as `+14155550123`, which is the format Reception.ai requires.

### Send the DID to Reception.ai

Go to **Applications** → **Misc Destinations** and add one that dials `88` followed by the number in E.164 format without `+`, for example `8814155550123`. Then go to **Connectivity** → **Inbound Routes**, open the route for your DID, and set its destination to that misc destination. You can also use it as the destination of a time condition, ring group failover or IVR option.

### Fix NAT and audio

Go to **Settings** → **Asterisk SIP Settings** → **General SIP Settings**. Set **External Address** to the PBX's public IP and list your private subnets under **Local Networks**. Open the **RTP Port Ranges** shown on that page (UDP, 10000–20000 by default) in your firewall.

### Test it

Call your DID from another phone and check that your receptionist answers.

## Plain Asterisk

On Asterisk without FreePBX, the same setup in `pjsip.conf` looks like this. Replace `SIP_SERVER` with the host Reception.ai shows.

```ini
[transport-tcp]
type=transport
protocol=tcp
bind=0.0.0.0:5060
external_signaling_address=PBX_PUBLIC_IP
external_media_address=PBX_PUBLIC_IP
local_net=192.168.0.0/16

[reception]
type=aor
contact=sip:SIP_SERVER:5060;transport=tcp

[reception]
type=endpoint
transport=transport-tcp
aors=reception
context=from-reception
disallow=all
allow=ulaw,alaw
```

In the dialplan, send the call with the number in E.164 format:

```ini
exten => YOUR_DID,1,Dial(PJSIP/+14155550123@reception)
```

If you set inbound credentials in Reception.ai, add a `type=auth` section with them and reference it with `outbound_auth=` on the endpoint.

## Limitations

* **Transfers.** Your receptionist transfers calls by placing a new call to the **Outbound SIP address**. Point it at your SIP carrier, using a carrier account that accepts a username and password. Routing transfers back into the PBX isn't covered here: Reception.ai calls from a changing pool of addresses, so the PBX can't match those calls to a trunk by IP.
* **Your PBX carries every call twice**, once from the carrier and once to Reception.ai, so it needs a free channel for each leg.

## Troubleshooting

| Problem                                              | What to check                                                                                                                                               |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Calls fail before ringing                            | Check that the trunk uses the TCP or TLS transport, not UDP, and that the port matches it.                                                                  |
| Calls are rejected                                   | Add the PBX's public IP to **Inbound allowed addresses**. Check in the Asterisk console that the INVITE's request URI starts with `+` and the country code. |
| The receptionist sees the PBX's number as the caller | Set **CID Options** on the Reception.ai trunk to **Allow Any CID**.                                                                                         |
| One-way or no audio                                  | Set **External Address** and **Local Networks**, and open the RTP port range in the firewall.                                                               |
| The receptionist doesn't answer                      | Make sure the number is added on the receptionist's **Phone** tile and matches the number the PBX sends.                                                    |
