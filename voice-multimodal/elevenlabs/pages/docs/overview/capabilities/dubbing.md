---
title: "Dubbing"
source: https://elevenlabs.io/docs/overview/capabilities/dubbing.md
path: docs/overview/capabilities/dubbing
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Dubbing

## Overview

ElevenLabs [dubbing](/docs/eleven-creative/products/dubbing) translates audio and video across 90+ languages while preserving the emotion, timing, tone and unique characteristics of each speaker. The original background audio is retained, so you can recreate each speaker's delivery in another language without re-mixing the soundtrack. It can be used to:

* Grow your addressable audience by 4x to reach international audiences
* Adapt existing material for new markets while preserving emotional nuance
* Offer content in multiple languages without re-recording voice talent

We also offer a [fully managed dubbing service](https://elevenlabs.io/elevenstudios) for video and podcast creators.

## Usage

* **[Automatic Dubbing](https://elevenlabs.io/app/dubbing)** — Dub content from one language into another with a few clicks, powered by the latest Dubbing v2 Alpha model.
  * **Upload limits:** Up to 1 GB and 180 minutes in the app, or 3 GB per source file via the API
* **[Dubbing Studio](/docs/eleven-creative/products/dubbing/dubbing-studio)** — Granular control over your dubs, including transcript editing, speaker reassignment, and per-clip regeneration. Only available via the v1 model.
  * **Upload limits:** Up to 1 GB and 45 minutes
  * **Note:** Dubbing Studio is in maintenance mode and receives critical bug fixes only
* **Human-verified dubs via ElevenLabs Productions** — For more information, reach out to [productions@elevenlabs.io](mailto:productions@elevenlabs.io).

#### [Products](/docs/eleven-creative/products/dubbing/dubbing-studio)

Edit transcripts and translate videos step by step in Dubbing Studio.

#### [Developers](/docs/eleven-api/guides/cookbooks/dubbing)

Learn how to integrate dubbing into your application.

### Cloning strength

Cloning strength is the configurable setting in Automatic Dubbing on the Dubbing v2 Alpha model, on a scale of 0 to 10. In the app it appears as **Speaker similarity** under **Advanced**. The default value of 7 works well for most content. Higher values prioritize voice similarity to the original speaker, which can sound less natural across languages with very different phonetic characteristics. A higher setting can also carry over more of the original accent into the dubbed output. Lower values give the model more freedom for natural delivery in the target language at the cost of resemblance to the original voice.

### Key features

* **Multiple speakers:** Automatically detect multiple speakers, even with overlapping speech.
* **Multi-language output:** Generate localized tracks in 90+ languages.
* **Preserve original voices:** Retain the speaker's identity and emotional tone.
* **Keep background audio:** Avoid re-mixing music, effects, or ambient sounds.
* **Supported file types:** Videos and audio can be dubbed from various sources, including YouTube, TikTok, direct URLs, or file uploads.

Dubbing v2 does not include a watermark toggle. Free-tier dubs are watermarked automatically;
paid-tier dubs are not. There is no watermark-for-credit-discount option on Dubbing v2. The legacy
v1 dubbing flow and Dubbing Studio were the only places where the watermark discount existed.

### Cost

Refer to our [pricing page](https://elevenlabs.io/pricing) for detailed credit costs.

## Supported languages

Dubbing supports 90+ languages including English, Spanish, French, German, Japanese, Chinese, Arabic, and more. The API accepts a [BCP-47](https://en.wikipedia.org/wiki/IETF_language_tag) language tag in the `source_language` and `target_language` parameters, for example `fr` or `es-MX`. On Dubbing v2, a region-qualified tag such as `es-MX` must be one of the supported dialects listed below; all other languages use the base language tag. Dubbing v1 does not support dialects.

#### Dubbing v2 languages and dialects

| Language           | Code  | Dialects                           |
| ------------------ | ----- | ---------------------------------- |
| Afrikaans          | `af`  | —                                  |
| Akan               | `ak`  | —                                  |
| Albanian           | `sq`  | —                                  |
| Amharic            | `am`  | —                                  |
| Arabic             | `ar`  | `ar-EG`                            |
| Armenian           | `hy`  | —                                  |
| Assamese           | `as`  | —                                  |
| Azerbaijani        | `az`  | —                                  |
| Basque             | `eu`  | —                                  |
| Belarusian         | `be`  | —                                  |
| Bosnian            | `bs`  | —                                  |
| Bulgarian          | `bg`  | —                                  |
| Burmese            | `my`  | —                                  |
| Cantonese          | `yue` | —                                  |
| Catalan            | `ca`  | —                                  |
| Cebuano            | `ceb` | —                                  |
| Chinese            | `zh`  | `zh-TW`                            |
| Croatian           | `hr`  | —                                  |
| Czech              | `cs`  | —                                  |
| Danish             | `da`  | —                                  |
| Dogri              | `dgo` | —                                  |
| Dutch              | `nl`  | —                                  |
| English            | `en`  | `en-AU`, `en-CA`, `en-GB`, `en-US` |
| Estonian           | `et`  | —                                  |
| Filipino (Tagalog) | `fil` | —                                  |
| Finnish            | `fi`  | —                                  |
| French             | `fr`  | `fr-CA`, `fr-FR`                   |
| Galician           | `gl`  | —                                  |
| Georgian           | `ka`  | —                                  |
| German             | `de`  | —                                  |
| Greek              | `el`  | —                                  |
| Gujarati           | `gu`  | —                                  |
| Hausa              | `ha`  | —                                  |
| Hebrew             | `he`  | —                                  |
| Hindi              | `hi`  | —                                  |
| Hungarian          | `hu`  | —                                  |
| Icelandic          | `is`  | —                                  |
| Indonesian         | `id`  | —                                  |
| Italian            | `it`  | —                                  |
| Japanese           | `ja`  | —                                  |
| Javanese           | `jv`  | —                                  |
| Kannada            | `kn`  | —                                  |
| Kazakh             | `kk`  | —                                  |
| Kikuyu             | `ki`  | —                                  |
| Kinyarwanda        | `rw`  | —                                  |
| Kirundi            | `rn`  | —                                  |
| Korean             | `ko`  | —                                  |
| Kyrgyz             | `ky`  | —                                  |
| Latvian            | `lv`  | —                                  |
| Lithuanian         | `lt`  | —                                  |
| Luganda            | `lg`  | —                                  |
| Macedonian         | `mk`  | —                                  |
| Malay              | `ms`  | —                                  |
| Malayalam          | `ml`  | —                                  |
| Mandarin Chinese   | `cmn` | —                                  |
| Marathi            | `mr`  | —                                  |
| Mongolian          | `mn`  | —                                  |
| Nepali             | `ne`  | —                                  |
| Norwegian          | `no`  | —                                  |
| Persian            | `fa`  | —                                  |
| Polish             | `pl`  | —                                  |
| Portuguese         | `pt`  | `pt-BR`, `pt-PT`                   |
| Punjabi            | `pa`  | —                                  |
| Romanian           | `ro`  | —                                  |
| Russian            | `ru`  | —                                  |
| Sepedi             | `nso` | —                                  |
| Sesotho            | `st`  | —                                  |
| Sindhi             | `sd`  | —                                  |
| Slovak             | `sk`  | —                                  |
| Slovenian          | `sl`  | —                                  |
| Spanish            | `es`  | `es-AR`, `es-CL`, `es-ES`, `es-MX` |
| Sundanese          | `su`  | —                                  |
| Swahili            | `sw`  | —                                  |
| Swati              | `ss`  | —                                  |
| Swedish            | `sv`  | —                                  |
| Tajik              | `tg`  | —                                  |
| Tamil              | `ta`  | —                                  |
| Telugu             | `te`  | —                                  |
| Thai               | `th`  | —                                  |
| Tibetan            | `bo`  | —                                  |
| Tsonga             | `ts`  | —                                  |
| Tswana             | `tn`  | —                                  |
| Turkish            | `tr`  | —                                  |
| Ukrainian          | `uk`  | —                                  |
| Urdu               | `ur`  | —                                  |
| Uyghur             | `ug`  | —                                  |
| Uzbek              | `uz`  | —                                  |
| Venda              | `ve`  | —                                  |
| Vietnamese         | `vi`  | —                                  |
| Waray              | `war` | —                                  |
| Welsh              | `cy`  | —                                  |
| Wolof              | `wo`  | —                                  |
| Yoruba             | `yo`  | —                                  |
| Zulu               | `zu`  | —                                  |

#### Dubbing v1 languages

Dubbing v1 supports the same languages as the Eleven v3 model. Region-qualified dialect tags are not supported; use the base language tag.

| Language      | Code  |
| ------------- | ----- |
| Afrikaans     | `af`  |
| Arabic        | `ar`  |
| Armenian      | `hy`  |
| Assamese      | `as`  |
| Asturian      | `ast` |
| Azerbaijani   | `az`  |
| Belarusian    | `be`  |
| Bengali       | `bn`  |
| Bosnian       | `bs`  |
| Bulgarian     | `bg`  |
| Burmese       | `my`  |
| Cantonese     | `yue` |
| Catalan       | `ca`  |
| Cebuano       | `ceb` |
| Chichewa      | `ny`  |
| Chinese       | `zh`  |
| Croatian      | `hr`  |
| Czech         | `cs`  |
| Danish        | `da`  |
| Dutch         | `nl`  |
| English       | `en`  |
| Estonian      | `et`  |
| Filipino      | `fil` |
| Finnish       | `fi`  |
| French        | `fr`  |
| Galician      | `gl`  |
| Georgian      | `ka`  |
| German        | `de`  |
| Greek         | `el`  |
| Gujarati      | `gu`  |
| Hausa         | `ha`  |
| Hebrew        | `he`  |
| Hindi         | `hi`  |
| Hungarian     | `hu`  |
| Icelandic     | `is`  |
| Indonesian    | `id`  |
| Irish         | `ga`  |
| Italian       | `it`  |
| Japanese      | `ja`  |
| Javanese      | `jv`  |
| Kannada       | `kn`  |
| Kazakh        | `kk`  |
| Korean        | `ko`  |
| Kyrgyz        | `ky`  |
| Latvian       | `lv`  |
| Lingala       | `ln`  |
| Lithuanian    | `lt`  |
| Luxembourgish | `lb`  |
| Macedonian    | `mk`  |
| Malay         | `ms`  |
| Malayalam     | `ml`  |
| Maltese       | `mt`  |
| Maori         | `mi`  |
| Marathi       | `mr`  |
| Mongolian     | `mn`  |
| Nepali        | `ne`  |
| Norwegian     | `no`  |
| Occitan       | `oc`  |
| Odia          | `or`  |
| Pashto        | `ps`  |
| Persian       | `fa`  |
| Polish        | `pl`  |
| Portuguese    | `pt`  |
| Punjabi       | `pa`  |
| Romanian      | `ro`  |
| Russian       | `ru`  |
| Serbian       | `sr`  |
| Sindhi        | `sd`  |
| Slovak        | `sk`  |
| Slovenian     | `sl`  |
| Somali        | `so`  |
| Spanish       | `es`  |
| Swahili       | `sw`  |
| Swedish       | `sv`  |
| Tagalog       | `tl`  |
| Tajik         | `tg`  |
| Tamil         | `ta`  |
| Telugu        | `te`  |
| Thai          | `th`  |
| Turkish       | `tr`  |
| Ukrainian     | `uk`  |
| Urdu          | `ur`  |
| Uzbek         | `uz`  |
| Vietnamese    | `vi`  |
| Welsh         | `cy`  |
| Yoruba        | `yo`  |

## Key facts

* **Dubbing v2** Alpha — Dubbing v2 is currently in alpha. You may encounter occasional rough edges as we continue to improve the model.
* **Content types:** All audio and video content types are supported, with up to 32 unique speakers per file.
* **Speaker preservation:** Each speaker's tone, pace, and style is preserved in the target language.
* **Concurrency:** All self-serve plans (Free, Starter, Creator, Pro, Scale, Business) allow up to 3 concurrent dubbing jobs, and Enterprise plans default to 10. Limits are applied per workspace and counted per model, so v1 and v2 jobs do not share a pool. If you hit a limit, you will receive a `too_many_concurrent_requests` error and should wait for existing jobs to complete before starting new ones.

## FAQ

#### Is realtime or live dubbing available?

Realtime or live dubbing is not currently available.

#### What happens if my dub fails or gets stuck?

If a Dubbing Studio job fails or you cancel it, the credits are automatically refunded to your
account. Dubbing v2 (priced per minute in US dollars on Automatic Dubbing) is not charged for
failed jobs. If a dub is stuck in Queued or Loading for an extended period, cancel and resubmit
it. You will not lose credits by doing so.

#### Is Dubbing v2 available via API?

Yes. See the [Dubbing quickstart](/docs/eleven-api/guides/cookbooks/dubbing) to create your
first dub with the API.

#### How do I use the legacy v1 dubbing model?

Automatic Dubbing on the main [Dubbing](https://elevenlabs.io/app/dubbing) page uses Dubbing v2
by default. To use the legacy v1 dubbing model and the original dubbing dialog, click
**Advanced** and then **Use legacy V1 dubbing model**. The legacy dialog includes the v1
watermark-for-credit-discount option and is the only way to reach Dubbing Studio from this page.
