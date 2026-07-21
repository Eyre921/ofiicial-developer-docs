---
title: "How do Basic Seat credit limits work?"
source: https://elevenlabs.io/docs/help-center/product/monetization-business/workspaces/how-do-basic-seat-credit-limits-work.md
path: docs/help-center/product/monetization-business/workspaces/how-do-basic-seat-credit-limits-work
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# How do Basic Seat credit limits work?

All workspace members share a single credit pool. Basic Seats do not receive separate credits.

Instead, Basic Seats have a credit ceiling:

* ElevenCreative usage is limited to 50,000 credits per user, per billing cycle
* This limit is drawn from the shared workspace pool
* ElevenAgents and ElevenAPI usage is not capped per user

If the shared credit pool runs out, all generation stops, regardless of individual limits.

If a Basic Seat user reaches their 50,000 credit ceiling, they cannot generate more ElevenCreative content until the next billing cycle. Their access to ElevenAgents and ElevenAPI remains unchanged.
