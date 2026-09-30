---
title: "Usage and limits"
source: https://elevenlabs.io/docs/reception-ai/billing/usage-and-limits.md
path: docs/reception-ai/billing/usage-and-limits
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Usage and limits

## Credit system

Your plan includes a monthly pool of credits shared across all activity:

| Activity                                | Credit cost     |
| --------------------------------------- | --------------- |
| Inbound phone call                      | 1.0 per minute  |
| Web widget or booking page conversation | 0.5 per minute  |
| Staff first call                        | 1.0 per minute  |
| Text message                            | 0.1 per message |

### Checking usage

Go to **Settings** → **Billing** to see your plan, renewal date, and a usage table with rows for **Inbound calls**, **Web widget**, **Human-first calls**, **Text messages**, and **Total usage**. Each row shows usage, the overage rate, and any overage cost.

## Credit refresh

Credits reset at the start of each billing period, and unused credits do not roll over. On annual plans, credits refresh monthly.

When you upgrade mid-cycle, your remaining credits carry over, up to the new plan's pool.

## Overage

On paid plans, usage beyond your credit pool is billed at your plan's overage rate:

| Item               | Basic   | Plus    | Premium |
| ------------------ | ------- | ------- | ------- |
| Per credit         | \$0.45  | \$0.38  | \$0.30  |
| Extra phone minute | \$0.45  | \$0.38  | \$0.30  |
| Extra web minute   | \$0.225 | \$0.19  | \$0.15  |
| Extra text message | \$0.045 | \$0.038 | \$0.03  |

The free trial has no overage. When trial credits run out, your receptionist stops answering until you upgrade.

### Low-credit warnings

During the trial, a warning appears when 25% or less of your credits remain, and again when they run out. Select **View plans** to upgrade.

## Resource limits

| Resource               | Trial | Basic | Plus | Premium |
| ---------------------- | ----- | ----- | ---- | ------- |
| Phone numbers          | 1     | 1     | 3    | 5       |
| Concurrent calls       | 20    | 1     | 3    | 10      |
| Locations              | 20    | 1     | 1    | 20      |
| Knowledge sources      | 5     | 5     | 10   | 20      |
| Assistant messages/day | 150   | 150   | 300  | 500     |

Phone number limits don't include [numbers you bring](/docs/reception-ai/phone-numbers/bring-your-own-number).

Other limits that apply on every plan:

* 50 rules, 20 procedures, and 100 transfer rules per receptionist
* 10 transfer rule changes per day during the free trial

## Assistant daily limit

The business assistant has a daily message limit that resets at midnight UTC. When you reach it, a banner appears with an option to upgrade.
