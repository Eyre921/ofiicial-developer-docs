---
title: "How much does Dubbing cost?"
source: https://elevenlabs.io/docs/help-center/product/dubbing/how-much-does-dubbing-cost.md
path: docs/help-center/product/dubbing/how-much-does-dubbing-cost
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# How much does Dubbing cost?

Dubbing is charged per minute of source media, for each language you dub into. The exact rate depends on the dubbing model you’re using — see the [pricing page](https://elevenlabs.io/pricing) for details. In the app, the total cost is shown for you to confirm before a dub starts.

A dubbing project created with the [Dubbing API](/docs/eleven-api/guides/cookbooks/dubbing) has a minimum charge of one language. Creating a project charges you for one language’s dub up front, based on the duration of the source, and that charge prepays your first language target:

* The charge is applied when you create the project, while its source is being prepared — not when you add the first language.
* The first language you add (or the one you queue with `target_language` when creating the project) uses this prepaid charge rather than adding to it.
* Each additional language you add is charged separately when you queue it.

## Handling failures

* If a project fails to prepare — for example, its source cannot be transcribed — the creation charge is refunded.
* If an additional language fails to generate, its charge is refunded.
* The first language is prepaid by the project’s creation charge. If it fails to generate, the creation charge is not refunded, but the prepayment is not lost: it stays available, so retrying that language on the same project incurs no additional charge.
* Deleting a project or language does not refund a dub that is already running.
