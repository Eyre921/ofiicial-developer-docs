---
title: "Models & Languages Overview"
source: https://developers.deepgram.com/docs/tts-models-languages-overview.md
path: docs/tts-models-languages-overview
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Models & Languages Overview

## Models

| Model                                                    | Description & Use                                                                                                                                                                                                                               |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Flux TTS](/docs/tts-models-languages-overview#flux-tts) | Our latest-generation, conversation-native voice model — streaming-first, turn-based, and expressive by default. **Recommended for all new builds**: voice agents, customer service, IVR, and general-purpose synthesis. Served on `/v2/speak`. |
| [Aura-2](/docs/tts-models-languages-overview#aura-2)     | Our previous-generation model, with voices across seven languages. Served on `/v1/speak`.                                                                                                                                                       |
| [Aura](/docs/tts-models-languages-overview#aura)         | Our first-generation text-to-speech model. English voices only. Served on `/v1/speak`.                                                                                                                                                          |

**Start with Flux TTS.** It's our best-sounding, most accurate model and the default recommendation for every use case it serves.

> **Info**
>
> The language comes from the voice's model string — the language code at the end selects it (`flux-desislava-bg` is Bulgarian, `flux-haley-en` is English). A `model` is required on every request — Flux TTS on `/v2/speak`, Aura-2 and Aura on `/v1/speak`.

### Example

To request a voice, set the `model` to the voice you want. Aura-2 and Aura use `/v1/speak`:

**`cURL (Aura-2, /v1/speak)`**

```bash cURL (Aura-2, /v1/speak)
curl "https://api.deepgram.com/v1/speak?model=aura-2-thalia-en" \
  -H "Authorization: Token YOUR_DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "text": "Hello, how are you?" }' \
  --output audio.mp3
```

Flux TTS uses `/v2/speak` (streaming WebSocket and batch REST). See [Getting Started with Flux TTS](/docs/flux-tts/quickstart).

> **Warning**
>
> Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys).

## Flux TTS

Flux TTS is Deepgram's best text-to-speech model and the recommended choice for every use case — real-time voice agents, customer service, IVR, and pre-rendered audio alike. It's conversation-native: streaming-first, turn-based, expressive by default, and consistent across turns, with native interruption handling and strong accuracy on the strings that trip up agents in production (alphanumerics, drug names, and other hard-to-say entities). Model strings follow the format `flux-{voice}-{language}` (e.g. `flux-alexis-en`), and `model` is required on every `/v2/speak` connection.

| Model Option      | Language                                                                            |
| ----------------- | ----------------------------------------------------------------------------------- |
| `flux-{voice}-en` | English (American, British, Irish, Australian, Indian, Singaporean, Filipino): `en` |
| `flux-{voice}-bn` | Bengali: `bn`                                                                       |
| `flux-{voice}-bg` | Bulgarian: `bg`                                                                     |
| `flux-{voice}-ca` | Catalan: `ca`                                                                       |
| `flux-{voice}-zh` | Chinese (Mandarin, Taiwanese Mandarin, Cantonese): `zh`                             |
| `flux-{voice}-hr` | Croatian: `hr`                                                                      |
| `flux-{voice}-cs` | Czech: `cs`                                                                         |
| `flux-{voice}-da` | Danish: `da`                                                                        |
| `flux-{voice}-nl` | Dutch (Dutch, Flemish): `nl`                                                        |
| `flux-{voice}-et` | Estonian: `et`                                                                      |
| `flux-{voice}-fi` | Finnish: `fi`                                                                       |
| `flux-{voice}-fr` | French: `fr`                                                                        |
| `flux-{voice}-de` | German (German, Swiss German): `de`                                                 |
| `flux-{voice}-el` | Greek: `el`                                                                         |
| `flux-{voice}-gu` | Gujarati: `gu`                                                                      |
| `flux-{voice}-hi` | Hindi: `hi`                                                                         |
| `flux-{voice}-hu` | Hungarian: `hu`                                                                     |
| `flux-{voice}-id` | Indonesian: `id`                                                                    |
| `flux-{voice}-it` | Italian: `it`                                                                       |
| `flux-{voice}-ja` | Japanese: `ja`                                                                      |
| `flux-{voice}-kn` | Kannada: `kn`                                                                       |
| `flux-{voice}-ko` | Korean: `ko`                                                                        |
| `flux-{voice}-lv` | Latvian: `lv`                                                                       |
| `flux-{voice}-lt` | Lithuanian: `lt`                                                                    |
| `flux-{voice}-ms` | Malay: `ms`                                                                         |
| `flux-{voice}-mr` | Marathi: `mr`                                                                       |
| `flux-{voice}-no` | Norwegian: `no`                                                                     |
| `flux-{voice}-pl` | Polish: `pl`                                                                        |
| `flux-{voice}-pt` | Portuguese (Brazil, Portugal): `pt`                                                 |
| `flux-{voice}-ro` | Romanian: `ro`                                                                      |
| `flux-{voice}-ru` | Russian: `ru`                                                                       |
| `flux-{voice}-sk` | Slovak: `sk`                                                                        |
| `flux-{voice}-sl` | Slovenian: `sl`                                                                     |
| `flux-{voice}-es` | Spanish: `es`                                                                       |
| `flux-{voice}-sv` | Swedish: `sv`                                                                       |
| `flux-{voice}-tl` | Tagalog: `tl`                                                                       |
| `flux-{voice}-ta` | Tamil: `ta`                                                                         |
| `flux-{voice}-te` | Telugu: `te`                                                                        |
| `flux-{voice}-tr` | Turkish: `tr`                                                                       |
| `flux-{voice}-uk` | Ukrainian: `uk`                                                                     |
| `flux-{voice}-ur` | Urdu: `ur`                                                                          |
| `flux-{voice}-vi` | Vietnamese: `vi`                                                                    |

Text normalization (numbers, dates and abbreviations read out) is available for English, German, Dutch, French, Hindi, Italian, Japanese, Portuguese, Russian and Spanish; the other 32 languages are in Early Access without it — write numbers and dates out in words.

See the full [Flux TTS Voices & Languages](/docs/flux-tts/voices) catalog for every voice and its characteristics.

## Aura-2

Aura-2 is Deepgram's previous-generation text-to-speech model, with voices across seven languages. For new work, build on [Flux TTS](#flux-tts). Model strings follow the format `aura-2-{voice}-{language}` (e.g. `aura-2-thalia-en`).

| Model Option        | Language                                                                  |
| ------------------- | ------------------------------------------------------------------------- |
| `aura-2-{voice}-en` | English (American, British, Australian, Filipino): `en`                   |
| `aura-2-{voice}-es` | Spanish (Mexican, Peninsular, Colombian, Argentine, Latin American): `es` |
| `aura-2-{voice}-de` | German: `de`                                                              |
| `aura-2-{voice}-fr` | French: `fr`                                                              |
| `aura-2-{voice}-nl` | Dutch: `nl`                                                               |
| `aura-2-{voice}-it` | Italian: `it`                                                             |
| `aura-2-{voice}-ja` | Japanese: `ja`                                                            |

See the full [Aura Voices & Languages](/docs/tts-models) catalog for every voice, accent, and audio sample. Select Spanish voices (Aquila, Carina, Diana, Javier, Selena) support English–Spanish codeswitching.

## Aura

Aura is Deepgram's first-generation text-to-speech model. English voices only, served on `/v1/speak`.

| Model Option      | Language                                 |
| ----------------- | ---------------------------------------- |
| `aura-{voice}-en` | English (American, British, Irish): `en` |

See the [Aura Voices & Languages](/docs/tts-models#aura-1-all-available-english-voices) catalog for the full list.

---
