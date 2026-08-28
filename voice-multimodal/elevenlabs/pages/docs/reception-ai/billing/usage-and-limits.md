---
title: "Usage and limits"
source: https://elevenlabs.io/docs/reception-ai/billing/usage-and-limits.md
path: docs/reception-ai/billing/usage-and-limits
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Usage and limits

## Credit system

Your plan includes a monthly pool of credits. Credits are consumed by different activities at different rates:

| Activity                         | Credit cost     |
| -------------------------------- | --------------- |
| AI receptionist phone call       | 1.0 per minute  |
| Web chat session                 | 0.5 per minute  |
| Staff-first mode (human answers) | 1.0 per minute  |
| Assistant chat message           | 0.1 per message |

Monthly credit pools vary by plan:

| Plan    | Included credits |
| ------- | ---------------- |
| Trial   | 30               |
| Basic   | 75               |
| Plus    | 275              |
| Premium | 1,000            |

### Checking usage

Go to **Settings** → **Billing** to see:

* Total credits in your pool
* Credits used this billing period
* Credits remaining
* Breakdown by type (phone minutes, web minutes, chat messages)

## Resource limits

Each plan has hard limits on:

| Resource               | Basic | Plus | Premium |
| ---------------------- | ----- | ---- | ------- |
| Phone numbers          | 1     | 3    | 5       |
| Receptionists          | 1     | 1    | 3       |
| Locations              | 1     | 1    | 20      |
| Knowledge sources      | 5     | 10   | 20      |
| Concurrent calls       | 1     | 3    | 10      |
| Assistant messages/day | 150   | 300  | 500     |

## Credit refresh

Credits reset at the start of each billing period. Unused credits do not roll over.

## Overage

On paid plans, exceeding your credit pool triggers overage billing at a rate set by your plan:

| Plan    | Per credit | Phone call/min | Web chat/min | Assistant message |
| ------- | ---------- | -------------- | ------------ | ----------------- |
| Basic   | \$0.45     | \$0.45         | \$0.225      | \$0.045           |
| Plus    | \$0.38     | \$0.38         | \$0.19       | \$0.038           |
| Premium | \$0.30     | \$0.30         | \$0.15       | \$0.03            |

## Assistant daily limit

The business assistant has a separate daily message cap that resets at midnight UTC:

| Plan    | Messages per day |
| ------- | ---------------- |
| Trial   | 150              |
| Basic   | 150              |
| Plus    | 300              |
| Premium | 500              |

When the limit is reached, a banner appears with an option to upgrade.
