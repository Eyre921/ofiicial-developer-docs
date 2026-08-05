---
title: "Profanity Filtering"
source: https://developers.deepgram.com/docs/profanity-filter.md
path: docs/profanity-filter
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Profanity Filtering

* [Try Profanity Filter in the Playground](https://playground.deepgram.com/?endpoint=listen\&profanity_filter=true\&language=en\&model=base)

`profanity_filter` *boolean* Default: `false`

&#x20;Pre-recorded

&#x20;Streaming:Nova

Streaming:Flux

&#x20;Specific languages only

Deepgram’s profanity filtering feature masks offensive language in transcripts using asterisks. Profanity filtering is available for the following languages:

* **Arabic**: `ar`, `ar-AE`, `ar-SA`, `ar-QA`, `ar-KW`, `ar-SY`, `ar-LB`, `ar-PS`, `ar-JO`, `ar-EG`, `ar-SD`, `ar-TD`, `ar-MA`, `ar-DZ`, `ar-TN`, `ar-IQ`, `ar-IR`
* **Belarusian**: `be`
* **Bengali**: `bn`
* **Bosnian**: `bs`
* **Bulgarian**: `bg`
* **Catalan**: `ca`
* **Chinese**: `zh`, `zh-CN`, `zh-TW`
* **Chinese (Cantonese, Traditional)**: `zh-HK`
* **Chinese (Mandarin, Simplified)**: `zh`, `zh-CN`, `zh-Hans`
* **Chinese (Mandarin, Traditional)**: `zh-TW`, `zh-Hant`
* **Croatian**: `hr`
* **Czech**: `cs`
* **Danish**: `da`, `da-DK`
* **Dutch**: `nl`
* **English**: `en`, `en-US`, `en-AU`, `en-CA`, `en-GB`, `en-IE`, `en-IN`, `en-NZ`
* **Estonian**: `et`
* **Finnish**: `fi`
* **Flemish**: `nl-BE`
* **French**: `fr`, `fr-CA`
* **German**: `de`
* **German (Switzerland)**: `de-CH`
* **Greek**: `el`
* **Gujarati**: `gu`, `gu-IN`
* **Hebrew**: `he`
* **Hindi**: `hi`, `hi-Latn`
* **Hungarian**: `hu`
* **Indonesian**: `id`
* **Italian**: `it`
* **Japanese**: `ja`
* **Kannada**: `kn`
* **Korean**: `ko`, `ko-KR`
* **Latvian**: `lv`
* **Lithuanian**: `lt`
* **Macedonian**: `mk`
* **Malay**: `ms`
* **Marathi**: `mr`
* **Norwegian**: `no`
* **Persian**: `fa`
* **Polish**: `pl`
* **Portuguese**: `pt`, `pt-BR`, `pt-PT`
* **Romanian**: `ro`
* **Russian**: `ru`
* **Serbian**: `sr`
* **Slovak**: `sk`
* **Slovenian**: `sl`
* **Spanish**: `es`, `es-419`, `es-LATAM`
* **Swedish**: `sv`, `sv-SE`
* **Tagalog**: `tl`
* **Tamasheq**: `taq`
* **Tamil**: `ta`
* **Telugu**: `te`
* **Thai**: `th`, `th-TH`
* **Turkish**: `tr`
* **Ukrainian**: `uk`
* **Urdu**: `ur`
* **Vietnamese**: `vi`

Profanity filtering is supported for all multilingual models: Nova-2 multi, Nova-3 multi, and Flux multi (`language=multi`).

## Enable Feature

To enable Profanity Filtering, use the following parameter in the query string when you call Deepgram’s `/listen` endpoint :

`profanity_filter=true`

To transcribe audio from a file on your computer, run the following cURL command in a terminal or your favorite API client.

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?profanity_filter=true'
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

## Results

Filtered results will appear in the transcript as \*\*\*\*

```json JSON
{
    "metadata": {
        "transaction_key": "deprecated",
        "request_id": "9d5be02c-85a6-4e88-839e-474507583c70",
        "sha256": "36ee5ac2e476126b4a50bc192239ab73e5f9cdd496b0f27c516162447631a105",
        "created": "2024-12-14T00:07:25.012Z",
        "duration": 22.013313,
        "channels": 1,
        "models": [
            "1abfe86b-e047-4eed-858a-35e5625b41ee"
        ],
        "model_info": {
            "1abfe86b-e047-4eed-858a-35e5625b41ee": {
                "name": "2-general-nova",
                "version": "2024-01-06.5664",
                "arch": "nova-2"
            }
        }
    },
    "results": {
        "channels": [
            {
                "alternatives": [
                    {
                        "transcript": "it's a test of profanity filtering **** **** ******* **** you ******* **** *** **** you that's the end of the test",
                        "confidence": 0.9854036,
                        "words": [
                            {
                                "word": "it's",
                                "start": 1.92,
                                "end": 2.1599998,
                                "confidence": 0.94446576
                            },
                            {
                                "word": "a",
                                "start": 2.1599998,
                                "end": 2.32,
                                "confidence": 0.6431149
                            },
                            {
                                "word": "test",
                                "start": 2.32,
                                "end": 2.72,
                                "confidence": 0.9996898
                            },
                            {
                                "word": "of",
                                "start": 2.72,
                                "end": 2.96,
                                "confidence": 0.9829601
                            },
                            {
                                "word": "profanity",
                                "start": 2.96,
                                "end": 3.46,
                                "confidence": 0.99511766
                            },
                            {
                                "word": "filtering",
                                "start": 3.6799998,
                                "end": 4.18,
                                "confidence": 0.9920975
                            },
                            {
                                "word": "****",
                                "start": 5.12,
                                "end": 5.62,
                                "confidence": 0.9255334
                            },
                            {
                                "word": "****",
                                "start": 6.08,
                                "end": 6.58,
                                "confidence": 0.99655294
                            },
                            {
                                "word": "*******",
                                "start": 7.2,
                                "end": 7.7,
                                "confidence": 0.9951559
                            },
                            {
                                "word": "****",
                                "start": 8.32,
                                "end": 8.82,
                                "confidence": 0.627333
                            },
                            {
                                "word": "you",
                                "start": 9.5199995,
                                "end": 10.0199995,
                                "confidence": 0.67789125
                            },
                            {
                                "word": "*******",
                                "start": 11.068313,
                                "end": 11.568313,
                                "confidence": 0.96285325
                            },
                            {
                                "word": "****",
                                "start": 12.428312,
                                "end": 12.928312,
                                "confidence": 0.97373027
                            },
                            {
                                "word": "***",
                                "start": 18.028313,
                                "end": 18.348312,
                                "confidence": 0.8841204
                            },
                            {
                                "word": "****",
                                "start": 18.348312,
                                "end": 18.668312,
                                "confidence": 0.9854036
                            },
                            {
                                "word": "you",
                                "start": 18.668312,
                                "end": 19.168312,
                                "confidence": 0.9957408
                            },
                            {
                                "word": "that's",
                                "start": 19.94831,
                                "end": 20.268312,
                                "confidence": 0.9990535
                            },
                            {
                                "word": "the",
                                "start": 20.268312,
                                "end": 20.348312,
                                "confidence": 0.94378966
                            },
                            {
                                "word": "end",
                                "start": 20.348312,
                                "end": 20.508312,
                                "confidence": 0.9983961
                            },
                            {
                                "word": "of",
                                "start": 20.508312,
                                "end": 20.668312,
                                "confidence": 0.9802233
                            },
                            {
                                "word": "the",
                                "start": 20.668312,
                                "end": 20.748312,
                                "confidence": 0.9961033
                            },
                            {
                                "word": "test",
                                "start": 20.748312,
                                "end": 21.248312,
                                "confidence": 0.9991727
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```

***
