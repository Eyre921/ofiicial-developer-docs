---
title: "Phone numbers"
source: https://elevenlabs.io/docs/reception-ai/phone-numbers/overview.md
path: docs/reception-ai/phone-numbers/overview
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Phone numbers

Your receptionist answers calls on the phone numbers assigned to it. You can get a number in any of these ways:

| Option                                                                                                 | Countries               | Details                                                  |
| ------------------------------------------------------------------------------------------------------ | ----------------------- | -------------------------------------------------------- |
| **Reception.ai number**                                                                                | US and Canada           | A local number, assigned instantly                       |
| [International number](/docs/reception-ai/phone-numbers/international-numbers)                         | About 50 more countries | Requires a regulatory request with your business details |
| [Bring your own number](/docs/reception-ai/phone-numbers/bring-your-own-number)                        | Any                     | Use numbers from your Twilio account or SIP trunk        |
| [Forward an existing number](/docs/reception-ai/receptionist/call-handling#forward-an-existing-number) | Any                     | Keep your current line and forward unanswered calls      |

## Getting your first number

US and Canadian businesses choose a preferred 3-digit area code during onboarding, and Reception.ai assigns an available local number. Toll-free numbers are not available.

## Managing phone numbers

Go to **Receptionists**, select a receptionist, and select the **Phone** tile at the top of the page. The **Phone numbers** dialog lists the receptionist's numbers.

### Getting another number

Enter an optional **Area code** and select **Get a new phone number**. If no numbers are available in that area code, try a nearby one.

### Moving a number

Select **Transfer to another receptionist** on a number to move it.

### Releasing a number

Release a Reception.ai number when you no longer need it.

> **Warning**
>
> Releasing is permanent. The number returns to the shared pool and may be assigned to someone else.
> Numbers from your own Twilio account or SIP trunk are removed from Reception.ai instead.

## Plan limits

| Plan    | Phone numbers |
| ------- | ------------- |
| Trial   | 1             |
| Basic   | 1             |
| Plus    | 3             |
| Premium | 5             |

These limits apply to Reception.ai and international numbers. Numbers you bring from your own Twilio account or SIP trunk don't count toward the limit.

## How inbound calls are routed

When a call arrives, the system processes it in this order:

1. **Held number check**: numbers awaiting regulatory approval reject calls.
2. **Entitlement check**: requires an active subscription or remaining trial credits.
3. **Blocked number check**: blocked callers are rejected.
4. **Answering order**: if staff first is on and within staff answering hours, the staff phone rings first.
5. **AI receptionist**: greets the caller and handles the conversation.

When a trial runs out of credits, callers hear a message that the number's free trial has ended.

## Number deactivation

Numbers stop accepting calls when:

* Your subscription is cancelled or expires. Numbers are kept for a 14-day grace period before release.
* You exceed your plan's phone number limit after a downgrade.

During the grace period, numbers are reserved for you and can be reactivated by upgrading or renewing.
