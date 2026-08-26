---
title: "Troubleshooting & FAQ"
source: https://elevenlabs.io/docs/eleven-agents/whatsapp/troubleshooting.md
path: docs/eleven-agents/whatsapp/troubleshooting
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Troubleshooting & FAQ

## Message accepted but not delivered

A `200` response from the outbound message endpoint means ElevenLabs accepted and forwarded the request — delivery is still up to Meta. If the message never arrives, check in order:

1. **Template approval** — the template must have status Approved in [WhatsApp Manager](https://business.facebook.com/latest/whatsapp_manager/message_templates). Pending or rejected templates are not delivered.
2. **Payments** — a missing payment method or unsettled payments on your WhatsApp business account block template delivery (Meta error 131042). Add or update the payment method in WhatsApp Manager.
3. **Parameter shape** — `template_params` entries must be component objects (`{"type": "body", "parameters": [...]}`), every placeholder in the template must be filled, and named templates need a `parameter_name` on each value. See [template parameters](/docs/eleven-agents/whatsapp/outbound#template-parameters).
4. **Recipient format** — `whatsapp_user_id` is digits only with country code, no `+`. See [recipient number format](/docs/eleven-agents/whatsapp/outbound#recipient-number-format).
5. **Marketing limits** — Meta caps how many [marketing templates](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/marketing-templates/per-user-limits) one user can receive in a period (error 131049). Utility templates are not subject to this cap.

## Import problems

* **The number can't be imported** — it is registered with another WhatsApp provider or active in the WhatsApp Business app. A number can only be registered with one provider; see [Limitations](/docs/eleven-agents/whatsapp#limitations).
* **Your WABA doesn't appear in the import flow** — confirm you are logged into a Facebook account with admin access to the business portfolio that owns the WABA, then retry the import.
* **WABAs created under a Meta developer app** cannot be imported through the standard flow.

To check whether another partner already controls your number, open [WhatsApp accounts in Meta
Business settings](https://business.facebook.com/latest/settings/whatsapp_account), select the
WhatsApp account that contains your number, and review its partners. A partner listed there with
control over the number explains both a failed import and a missing WABA — remove the partner or
use a different number.

## The agent doesn't respond to inbound messages

The read receipt and typing indicator narrow the cause down: they are sent the moment a message is accepted for processing, before the agent produces a reply. With **Enable typing indicator** on (the default), send a test message and watch whether your message is marked read and the typing indicator appears.

**The typing indicator appears, but no reply arrives.** The message reached ElevenLabs and the agent started working; the failure happens while producing or delivering the reply:

* The agent requires a [dynamic variable](/docs/eleven-agents/customization/personalization/dynamic-variables) that has no value. Inbound WhatsApp conversations start with no user-provided dynamic variables — only the system variables are populated. The fix is a [conversation initiation webhook](/docs/eleven-agents/customization/personalization#conversation-initiation-webhooks) that returns every variable the agent requires; see [initialization context](/docs/eleven-agents/whatsapp#initialization-context). The values entered under **Dynamic Variables** in the agent editor are test placeholders and are not used in production.
* Meta declined the agent's reply — for example a rate limit for this business–user pair or an account-level payment issue. See the [error reference](#meta-error-reference) below.

The conversation fails if these required dynamic variables are not present.

**No typing indicator appears.** The message was dropped before reaching the agent:

* No agent is assigned to the number, or the **Enable messaging** switch is off — check the account settings on the [WhatsApp page](https://elevenlabs.io/app/agents/whatsapp).
* The account's authorization is no longer valid — the access token expired or was revoked on the Meta side. Re-import the account on the [WhatsApp page](https://elevenlabs.io/app/agents/whatsapp).
* The agent workspace is in [Zero-Retention Mode](/docs/eleven-api/resources/zero-retention-mode), which ignores inbound WhatsApp messages entirely.
* The inbound message is an unsupported type (for example video, or a WhatsApp Flow reply) — see [Limitations](/docs/eleven-agents/whatsapp#limitations).

If **Enable typing indicator** is turned off for the account, this check does not apply — work
through both lists.

## The first reply after a template misbehaves

If your agent has the **First message** override enabled on its **Security** tab, it can conflict with outbound template conversations — the template already served as the first message. If replies to templates behave unexpectedly, remove the first-message override for agents used with WhatsApp outbound messages.

## Meta error reference

Errors Meta returns during delivery are surfaced with remediation advice where possible. The most common:

| Code   | Meaning                                               | What to do                                                                                                                              |
| ------ | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| 131042 | Payment issue on the WhatsApp business account        | Add or fix the payment method in WhatsApp Manager                                                                                       |
| 131056 | Rate limit for this business–user pair                | Slow down messages to this user                                                                                                         |
| 131047 | Re-engagement required                                | The Customer Service Window closed — re-engage with a template                                                                          |
| 130497 | Business restricted from messaging users in a country | Meta has restricted the account's cross-country messaging — resolve with Meta support                                                   |
| 132000 | Parameter count does not match the template           | Send exactly the parameters the template defines — see [template parameters](/docs/eleven-agents/whatsapp/outbound#template-parameters) |
| 132001 | Template does not exist                               | Check the template name and language code, and that the template is approved                                                            |
| 131037 | Phone number display name issue                       | Complete display-name approval in WhatsApp Manager                                                                                      |
| 190    | Access token expired                                  | Re-import the account on the [WhatsApp page](https://elevenlabs.io/app/agents/whatsapp)                                                 |

For the full list, see [Meta's error code reference](https://developers.facebook.com/documentation/business-messaging/whatsapp/support/error-codes).

## FAQ

#### How is WhatsApp usage billed?

Two parties bill you independently.

**ElevenLabs** charges for the agent's usage — conversation time, messages, speech-to-text and
text-to-speech for voice notes, and LLM usage — through your plan's credits, following standard
[ElevenLabs billing](/docs/overview/administration/billing).

**Meta** charges separately for WhatsApp fees such as template messages, outbound calls, and
call permission requests, billed through the payment method in WhatsApp Manager. Rates vary by
message category and country, and Meta has announced pricing updates taking effect on
October 1, 2026 — see [Meta's WhatsApp
pricing](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing) for
the rates that apply to your markets.

#### Can I use ElevenLabs alongside another WhatsApp provider?

A number can currently be registered with only one messaging provider. If a third-party
provider (for example Gupshup) manages your account, it cannot also be imported into
ElevenLabs. We are working with Meta to enable [Multi-Solution
Conversations](https://developers.facebook.com/documentation/business-messaging/whatsapp/solution-providers/multi-solution-conversations),
which allows multiple providers on one number.

**Voice through SIP.** If your goal is to keep messaging with your current provider and use an
ElevenLabs agent for voice, there is a path available today: WhatsApp Business Calling supports
SIP, so a provider that exposes SIP configuration can route your number's WhatsApp calls to an
ElevenLabs [SIP trunk](/docs/eleven-agents/phone-numbers/sip-trunking). Your provider keeps
handling messages on the number; calls are answered by your agent over SIP. Whether this works
depends on your provider supporting SIP call routing — [contact
us](https://elevenlabs.io/contact-sales) and we can evaluate your setup.

If you run your own WhatsApp app on the same account (rather than a third-party provider), you
can already configure ElevenLabs to handle calls only: turn off the ***Enable messaging***
switch in the account settings.

#### How do I hand a conversation off to a human?

Coming soon. We are working with Meta on Coexistence with WhatsApp Business, which will let
your team participate in conversations on the same number the agent uses.

#### Does Zero-Retention Mode work with WhatsApp?

[Zero-Retention Mode](/docs/eleven-api/resources/zero-retention-mode) limits our ability to
provide WhatsApp functionality: inbound messages are ignored and outbound calls are disallowed.

#### Can I personalize based on the WhatsApp ad a user clicked?

Not yet. The agent receives and responds to conversations started from Click-to-WhatsApp ads,
but Meta's ad referral metadata (such as `ctwa_clid` and campaign or creative identifiers) is
not currently exposed to the agent, dynamic variables, or webhooks, so ad-based personalization
and attribution are not natively supported. This is tracked as a feature request — if ad
attribution matters for your use case, [contact us](https://elevenlabs.io/contact-sales).

#### How do I send verification codes (OTP)?

Use a Utility template with the code as a body parameter, sent through the [outbound message
endpoint](/docs/eleven-agents/whatsapp/outbound). Meta's Authentication template category
(with copy-code buttons) is not yet specially supported.

#### Who is the technology provider for my WhatsApp account?

When you import a WhatsApp business account, ElevenLabs acts as the **Tech Provider** for that
account under Meta's partner model. ElevenLabs is a Meta tech partner, not a reseller: Meta
bills you directly for WhatsApp fees via the payment method in WhatsApp Manager.

#### Is EU data residency supported?

EU data residency for ElevenAgents, including WhatsApp conversation data, is available on
Enterprise plans through the isolated EU environment. This covers data handled by ElevenLabs
infrastructure; message transport through WhatsApp itself is governed by your agreement with
Meta.
