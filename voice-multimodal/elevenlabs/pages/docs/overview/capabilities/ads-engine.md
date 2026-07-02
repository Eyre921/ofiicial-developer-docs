---
title: "Ads Engine"
source: https://elevenlabs.io/docs/overview/capabilities/ads-engine.md
path: docs/overview/capabilities/ads-engine
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Ads Engine

## Overview

Ads Engine is a product area within ElevenCreative that connects to your advertising platforms to help you localize, generate, and manage ads at scale. Connect your Google, Meta, and LinkedIn ad accounts and the platform pulls your existing ads, localizes them across languages and markets — translating copy, adapting image overlays, and dubbing video with Dubbing v2 — then pushes the finished ads back to your ad platform.

Ads Engine is in alpha. This feature is under active development and subject to change.

Ads Engine can be used to:

* Localize existing ads across 50+ languages in a single workflow
* Translate text, adapt image overlays and composition, and dub video while preserving the original speaker's voice
* Pull ads and performance data from connected ad platforms, then push localized variants back
* Save reusable templates so any team member can rerun the same localization pipeline for new campaigns
* Review localized assets through an optional approval workflow before they go live

## Supported ad platforms

Connect an integration from the Settings tab to begin syncing campaigns and ads.

| Platform     | Supported content                               |
| ------------ | ----------------------------------------------- |
| Google Ads   | Search campaigns (text)                         |
| Meta Ads     | Facebook and Instagram (text, image, and video) |
| LinkedIn Ads | Performance insights                            |

## Supported languages

Ads Engine localizes ads across 50+ languages. Video dubbing is powered by Dubbing v2, which reproduces the original speaker's tone, emotion, and pacing in each target language rather than replacing the voice with a generic voiceover.

## Actions

Once an ad is loaded in Ads Engine, the following actions are available from the creative detail view:

* **Translate**: Generate localized versions across one or more target languages, including text, image overlays, and dubbed audio for video
* **Create new variants**: Produce four new visual variants while preserving brand, copy, and intent
* **Make a video**: Turn a static image into an image-to-video ad
* **Change copy**: Edit text fields (brand text, headlines, supporting copy) and regenerate
* **Run template**: Apply a saved template, including languages, approval steps, and image-adaptation preferences, or pick one from the Explore library
* **Launch ad**: Push the finished ad back to the connected ad platform

## Features

* **Localization engine**: One workflow to localize text, image, and dubbed video across 50+ languages
* **Ad platform connections**: Pulls existing ads and performance data from Google Ads, Meta Ads, and LinkedIn Ads, then pushes localized assets back
* **Image adaptation**: Translates text overlays and adapts image composition for culturally distinct markets
* **Dubbing v2 for video**: Reproduces the original speaker's voice, tone, and pacing in each target language
* **Reusable templates**: Save a pipeline — languages, approval steps, image-adaptation preferences — and rerun it for any campaign
* **Approval workflow**: Optional human review step before localized assets are pushed to the ad platform

## Availability

Ads Engine is available on the Pro plan and above.

## FAQ

Ads Engine is a product area within ElevenCreative that connects directly to your advertising
platforms to help you localize, generate, and manage ads at scale.

It takes your existing ads and localizes them across languages and markets — translating text,
adapting images, and dubbing video — then pushes the localized ads back to your ad platform.

Google Ads (Search — text) and Meta Ads (text, image, and video). LinkedIn Ads is supported for
performance insights only.

Ads Engine uses Dubbing v2 to reproduce the original speaker's tone, emotion, and pacing in the
target language. The original voice is preserved, not replaced with a generic voiceover.

Yes. Text overlays are translated and image composition can be adapted per market.

Yes. An optional approval workflow lets your team review localized assets before they are pushed
to the ad platform.

Yes. The platform pulls existing ads from Google, Meta, and LinkedIn regardless of where they
were originally created.

No, Ads Engine is not currently available via API.
