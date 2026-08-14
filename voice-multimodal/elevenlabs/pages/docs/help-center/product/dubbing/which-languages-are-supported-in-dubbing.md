---
title: "Which languages are supported in Dubbing?"
source: https://elevenlabs.io/docs/help-center/product/dubbing/which-languages-are-supported-in-dubbing.md
path: docs/help-center/product/dubbing/which-languages-are-supported-in-dubbing
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Which languages are supported in Dubbing?

Dubbing supports the languages listed below. When using the [Dubbing API](/docs/api-reference/dubbing/create-project), pass the language code as a [BCP-47](https://en.wikipedia.org/wiki/IETF_language_tag) language tag, for example `fr` or `es-MX`.

## Dubbing v2

On Dubbing v2, a region-qualified tag such as `es-MX` must be one of the supported dialects listed below; languages without dialects use the base language tag.

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

## Dubbing v1

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
