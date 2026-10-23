---
title: "Flux TTS Voices & Languages"
source: https://developers.deepgram.com/docs/flux-tts/voices.md
path: docs/flux-tts/voices
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Flux TTS Voices & Languages

Flux TTS voices use the model string format `flux-{voice}-{language}` (e.g. `flux-haley-en`). The same voice catalog is served on both `/v2/speak` transports — the [streaming WebSocket](/docs/flux-tts/quickstart) and [batch REST](/docs/flux-tts/batch).

## Selecting a voice

Pass the model string on connection:

```
wss://api.deepgram.com/v2/speak?model=flux-haley-en
```

Every voice handles general conversational synthesis. Use the tables below to shortlist, then hear the voices live at [talk.deepgram.com](https://talk.deepgram.com) before you build.

## Featured voices

Start here. The featured voices are the strongest all-rounders in the catalog — the most versatile across customer service, IVR, narration, and casual chat. Browse [More voices](#more-voices) below for additional accents, ages, and characters when you're matching a specific brand or audience.

| Voice   | Model             | Accent   | Gender | Age         | Character                                             | Use cases                                         |
| ------- | ----------------- | -------- | ------ | ----------- | ----------------------------------------------------- | ------------------------------------------------- |
| Hannah  | `flux-hannah-en`  | American | Female | Young       | Clear, confident, thoughtful, pleasant, nice          | Casual chat, storytelling                         |
| Kit     | `flux-kit-en`     | British  | Male   | Young Adult | Friendly, energetic, thoughtful, calm, helpful        | Customer service, narration, financial services   |
| Alexis  | `flux-alexis-en`  | American | Female | Adult       | Clear, professional, calm, caring, empathetic         | Customer service, IVR, financial services         |
| Cliff   | `flux-cliff-en`   | American | Male   | Mature      | Deep, confident, calm, raspy, clear                   | Financial services, narration, customer service   |
| Sienna  | `flux-sienna-en`  | American | Female | Young Adult | Clear, professional, calm, warm, caring               | Customer service, financial services, narration   |
| Cole    | `flux-cole-en`    | American | Male   | Young       | Friendly, clear, interesting, energetic, engaging     | Customer service, IVR                             |
| Brooke  | `flux-brooke-en`  | American | Female | Young       | Friendly, intelligent, fast, confident, energetic     | Healthcare, financial services, casual chat       |
| Colin   | `flux-colin-en`   | British  | Male   | Adult       | Warm, friendly, trustworthy, confident, authoritative | Customer service, financial services, narration   |
| Gemma   | `flux-gemma-en`   | British  | Female | Young       | Friendly, kind, approachable, caring, happy           | Customer service, IVR                             |
| Haley   | `flux-haley-en`   | American | Female | Young Adult | Clear, professional, caring, calm, empathetic         | Customer service, financial services, IVR         |
| Heather | `flux-heather-en` | American | Female | Young       | Clear, engaging, energetic, friendly, thoughtful      | Customer service, IVR                             |
| Miles   | `flux-miles-en`   | American | Male   | Adult       | Clear, calm, professional, confident, sincere         | Customer service, financial services, informative |
| Sean    | `flux-sean-en`    | British  | Male   | Mature      | Friendly, kind, caring, calming                       | IVR                                               |

## More voices

The rest of the catalog. Every voice here handles general conversational synthesis; the [featured voices](#featured-voices) above are the strongest all-rounders.

| Voice    | Model              | Accent      | Gender | Age         | Character                                              | Use cases                                             |
| -------- | ------------------ | ----------- | ------ | ----------- | ------------------------------------------------------ | ----------------------------------------------------- |
| Bree     | `flux-bree-en`     | American    | Female | Mature      | Friendly, sweet, kind                                  | Customer service, casual chat                         |
| Brittany | `flux-brittany-en` | American    | Female | Mature      | Confident, kind, soft                                  | Casual chat                                           |
| Bruce    | `flux-bruce-en`    | American    | Male   | Adult       | Friendly, kind, natural, believable, engaged           | Customer service, IVR                                 |
| Conor    | `flux-conor-en`    | British     | Male   | Mature      | Confident, deep, friendly, relaxed                     | Customer service, IVR                                 |
| Donovan  | `flux-donovan-en`  | American    | Male   | Adult       | Professional, calm, thoughtful                         | IVR                                                   |
| Drew     | `flux-drew-en`     | American    | Male   | Adult       | Confident, relaxed, soft, young, calm                  | Healthcare, financial services, customer service, IVR |
| Elise    | `flux-elise-en`    | American    | Female | Adult       | Clear, professional, calm, caring, empathetic          | Customer service, financial services, IVR             |
| Jack     | `flux-jack-en`     | British     | Male   | Adult       | Confident, thoughtful, friendly, professional, clear   | Customer service, storytelling                        |
| Kai      | `flux-kai-en`      | Singaporean | Male   | Young Adult | Clear, calm, professional, knowledgeable, caring       | Customer service, informative, IVR                    |
| Kelsey   | `flux-kelsey-en`   | American    | Female | Young Adult | Clear, professional, caring, calm, empathetic          | Customer service, IVR, financial services             |
| Maeve    | `flux-maeve-en`    | Irish       | Female | Adult       | Friendly, energetic, confident, gentle, calm           | Customer service, IVR, narration                      |
| Marcelo  | `flux-marcelo-en`  | Filipino    | Male   | Young Adult | Clear, calm, professional, knowledgeable, caring       | Customer service, informative, IVR                    |
| Marcus   | `flux-marcus-en`   | American    | Male   | Adult       | Friendly, helpful, smooth, professional, kind          | Customer service, casual chat                         |
| Meena    | `flux-meena-en`    | Indian      | Female | Adult       | Empathetic, professional, calm, reassuring, satisfying | Customer service, casual chat                         |
| Meghan   | `flux-meghan-en`   | American    | Female | Adult       | Friendly, nice, energetic, kind, confident             | Healthcare, financial services                        |
| Naveen   | `flux-naveen-en`   | Indian      | Male   | Adult       | Clear, professional, knowledgeable, calm, caring       | Customer service, IVR, informative                    |
| Paige    | `flux-paige-en`    | American    | Female | Young Adult | Clear, professional, calm, comfortable, caring         | Customer service, financial services, IVR             |
| Priya    | `flux-priya-en`    | Indian      | Female | Adult       | Confident, empathetic, professional, calm, reassuring  | IVR                                                   |
| Rufus    | `flux-rufus-en`    | British     | Male   | Adult       | Friendly, confident, intelligent, gentle, enthusiastic | Healthcare, financial services, storytelling          |
| Sharon   | `flux-sharon-en`   | Australian  | Female | Young       | Formal, calm, relaxed, confident                       | Healthcare, financial services                        |
| Tanner   | `flux-tanner-en`   | British     | Male   | Adult       | Professional, calm, confident                          | Customer service                                      |
| Wade     | `flux-wade-en`     | American    | Male   | Adult       | Warm, confident, clear, enthusiastic, friendly         | Customer service, casual chat                         |
| Wes      | `flux-wes-en`      | American    | Male   | Adult       | Thoughtful, friendly, warm, interesting                | Customer service, casual chat                         |

## Dutch

| Voice   | Model             | Gender |
| ------- | ----------------- | ------ |
| Anouk   | `flux-anouk-nl`   | Female |
| Bram    | `flux-bram-nl`    | Male   |
| Fleur   | `flux-fleur-nl`   | Female |
| Irene   | `flux-irene-nl`   | Female |
| Luuk    | `flux-luuk-nl`    | Male   |
| Monique | `flux-monique-nl` | Female |
| Ruben   | `flux-ruben-nl`   | Male   |
| Sanne   | `flux-sanne-nl`   | Female |
| Yvonne  | `flux-yvonne-nl`  | Female |

## Dutch (Flemish)

| Voice  | Model            | Gender |
| ------ | ---------------- | ------ |
| Dirk   | `flux-dirk-nl`   | Male   |
| Lotte  | `flux-lotte-nl`  | Female |
| Niels  | `flux-niels-nl`  | Male   |
| Veerle | `flux-veerle-nl` | Female |

## French

| Voice     | Model               | Gender |
| --------- | ------------------- | ------ |
| Arnaud    | `flux-arnaud-fr`    | Male   |
| Benoit    | `flux-benoit-fr`    | Male   |
| Brigitte  | `flux-brigitte-fr`  | Female |
| Camille   | `flux-camille-fr`   | Female |
| Chloe     | `flux-chloe-fr`     | Female |
| Florian   | `flux-florian-fr`   | Male   |
| Julien    | `flux-julien-fr`    | Male   |
| Mathieu   | `flux-mathieu-fr`   | Male   |
| Pierre    | `flux-pierre-fr`    | Male   |
| Thierry   | `flux-thierry-fr`   | Male   |
| Veronique | `flux-veronique-fr` | Female |
| Yasmine   | `flux-yasmine-fr`   | Female |

## German

| Voice     | Model               | Gender |
| --------- | ------------------- | ------ |
| Benjamin  | `flux-benjamin-de`  | Male   |
| Christian | `flux-christian-de` | Male   |
| Janine    | `flux-janine-de`    | Female |
| Magdalena | `flux-magdalena-de` | Female |
| Moritz    | `flux-moritz-de`    | Male   |
| Nadine    | `flux-nadine-de`    | Female |
| Rolf      | `flux-rolf-de`      | Male   |
| Sonja     | `flux-sonja-de`     | Female |
| Sven      | `flux-sven-de`      | Male   |
| Tobias    | `flux-tobias-de`    | Male   |
| Verena    | `flux-verena-de`    | Female |

## German (Swiss)

| Voice   | Model             | Gender |
| ------- | ----------------- | ------ |
| Leonie  | `flux-leonie-de`  | Female |
| Yannick | `flux-yannick-de` | Male   |

## Hindi

| Voice   | Model             | Gender |
| ------- | ----------------- | ------ |
| Ajay    | `flux-ajay-hi`    | Male   |
| Anjali  | `flux-anjali-hi`  | Female |
| Arjun   | `flux-arjun-hi`   | Male   |
| Divya   | `flux-divya-hi`   | Female |
| Jyoti   | `flux-jyoti-hi`   | Female |
| Nikhil  | `flux-nikhil-hi`  | Male   |
| Pallavi | `flux-pallavi-hi` | Female |
| Prachi  | `flux-prachi-hi`  | Female |
| Rahul   | `flux-rahul-hi`   | Male   |
| Rajesh  | `flux-rajesh-hi`  | Male   |
| Ritu    | `flux-ritu-hi`    | Female |
| Shreya  | `flux-shreya-hi`  | Female |
| Sunita  | `flux-sunita-hi`  | Female |
| Vikram  | `flux-vikram-hi`  | Male   |

## Italian

| Voice    | Model              | Gender |
| -------- | ------------------ | ------ |
| Angela   | `flux-angela-it`   | Female |
| Chiara   | `flux-chiara-it`   | Female |
| Federico | `flux-federico-it` | Male   |
| Giorgio  | `flux-giorgio-it`  | Male   |
| Matteo   | `flux-matteo-it`   | Male   |
| Paola    | `flux-paola-it`    | Female |
| Rocco    | `flux-rocco-it`    | Male   |
| Sofia    | `flux-sofia-it`    | Female |
| Stefano  | `flux-stefano-it`  | Male   |
| Vincenzo | `flux-vincenzo-it` | Male   |
| Vito     | `flux-vito-it`     | Male   |

## Japanese

| Voice  | Model            | Gender |
| ------ | ---------------- | ------ |
| Ayumi  | `flux-ayumi-ja`  | Female |
| Hayato | `flux-hayato-ja` | Male   |
| Nozomi | `flux-nozomi-ja` | Female |
| Sayaka | `flux-sayaka-ja` | Female |

## Portuguese (Brazil)

| Voice   | Model             | Gender |
| ------- | ----------------- | ------ |
| Bianca  | `flux-bianca-pt`  | Female |
| Bruno   | `flux-bruno-pt`   | Male   |
| Claudia | `flux-claudia-pt` | Female |
| Leandro | `flux-leandro-pt` | Male   |
| Marcia  | `flux-marcia-pt`  | Female |
| Mariana | `flux-mariana-pt` | Female |
| Marta   | `flux-marta-pt`   | Female |
| Mateus  | `flux-mateus-pt`  | Male   |
| Miguel  | `flux-miguel-pt`  | Male   |
| Renato  | `flux-renato-pt`  | Male   |
| Roberto | `flux-roberto-pt` | Male   |
| Rodrigo | `flux-rodrigo-pt` | Male   |

## Portuguese (Portugal)

| Voice    | Model              | Gender |
| -------- | ------------------ | ------ |
| Artur    | `flux-artur-pt`    | Male   |
| Benedita | `flux-benedita-pt` | Female |
| Catarina | `flux-catarina-pt` | Female |
| Hugo     | `flux-hugo-pt`     | Male   |
| Pedro    | `flux-pedro-pt`    | Male   |
| Ricardo  | `flux-ricardo-pt`  | Male   |

## Russian

| Voice    | Model              | Gender |
| -------- | ------------------ | ------ |
| Andrei   | `flux-andrei-ru`   | Male   |
| Kirill   | `flux-kirill-ru`   | Male   |
| Maxim    | `flux-maxim-ru`    | Male   |
| Mikhail  | `flux-mikhail-ru`  | Male   |
| Natalia  | `flux-natalia-ru`  | Female |
| Nikolai  | `flux-nikolai-ru`  | Male   |
| Olga     | `flux-olga-ru`     | Female |
| Polina   | `flux-polina-ru`   | Female |
| Vladimir | `flux-vladimir-ru` | Male   |

## Spanish

| Voice     | Model               | Gender |
| --------- | ------------------- | ------ |
| Aina      | `flux-aina-es`      | Female |
| Alfredo   | `flux-alfredo-es`   | Male   |
| Carmen    | `flux-carmen-es`    | Female |
| Cecilia   | `flux-cecilia-es`   | Female |
| Duvan     | `flux-duvan-es`     | Male   |
| Eduardo   | `flux-eduardo-es`   | Male   |
| Ernesto   | `flux-ernesto-es`   | Male   |
| Fernanda  | `flux-fernanda-es`  | Female |
| Fiorella  | `flux-fiorella-es`  | Female |
| Gustavo   | `flux-gustavo-es`   | Male   |
| Jaime     | `flux-jaime-es`     | Male   |
| Martin    | `flux-martin-es`    | Male   |
| Mauricio  | `flux-mauricio-es`  | Male   |
| Patricia  | `flux-patricia-es`  | Female |
| Pilar     | `flux-pilar-es`     | Female |
| Rafael    | `flux-rafael-es`    | Male   |
| Tomas     | `flux-tomas-es`     | Male   |
| Valentina | `flux-valentina-es` | Female |
| Ysabel    | `flux-ysabel-es`    | Female |

## Bengali — Early Access

| Voice   | Model             | Gender |
| ------- | ----------------- | ------ |
| Afsana  | `flux-afsana-bn`  | Female |
| Ishrat  | `flux-ishrat-bn`  | Female |
| Mamun   | `flux-mamun-bn`   | Male   |
| Sabbir  | `flux-sabbir-bn`  | Male   |
| Shuvo   | `flux-shuvo-bn`   | Male   |
| Sumaiya | `flux-sumaiya-bn` | Female |

## Bulgarian — Early Access

| Voice     | Model               | Gender |
| --------- | ------------------- | ------ |
| Desislava | `flux-desislava-bg` | Female |
| Gergana   | `flux-gergana-bg`   | Female |

## Catalan — Early Access

| Voice | Model           | Gender |
| ----- | --------------- | ------ |
| Jordi | `flux-jordi-ca` | Male   |
| Judit | `flux-judit-ca` | Female |

## Chinese (Mandarin) — Early Access

| Voice   | Model             | Gender |
| ------- | ----------------- | ------ |
| Bo      | `flux-bo-zh`      | Male   |
| Haoran  | `flux-haoran-zh`  | Male   |
| Jian    | `flux-jian-zh`    | Male   |
| Jie     | `flux-jie-zh`     | Male   |
| Lijuan  | `flux-lijuan-zh`  | Female |
| Shufen  | `flux-shufen-zh`  | Female |
| Wenbo   | `flux-wenbo-zh`   | Male   |
| Wenjing | `flux-wenjing-zh` | Female |
| Zhen    | `flux-zhen-zh`    | Female |

## Chinese (Taiwanese Mandarin) — Early Access

| Voice    | Model              | Gender |
| -------- | ------------------ | ------ |
| Chiaying | `flux-chiaying-zh` | Female |
| Kuanyu   | `flux-kuanyu-zh`   | Male   |
| Yawen    | `flux-yawen-zh`    | Female |
| Yuting   | `flux-yuting-zh`   | Female |

## Chinese (Cantonese) — Early Access

| Voice  | Model            | Gender |
| ------ | ---------------- | ------ |
| Manlok | `flux-manlok-zh` | Male   |

## Croatian — Early Access

| Voice    | Model              | Gender |
| -------- | ------------------ | ------ |
| Dalibor  | `flux-dalibor-hr`  | Male   |
| Danijela | `flux-danijela-hr` | Female |
| Domagoj  | `flux-domagoj-hr`  | Male   |
| Jasna    | `flux-jasna-hr`    | Female |
| Josipa   | `flux-josipa-hr`   | Female |
| Mihaela  | `flux-mihaela-hr`  | Female |
| Vedran   | `flux-vedran-hr`   | Male   |

## Czech — Early Access

| Voice | Model           | Gender |
| ----- | --------------- | ------ |
| Jakub | `flux-jakub-cs` | Male   |

## Danish — Early Access

| Voice    | Model              | Gender |
| -------- | ------------------ | ------ |
| Pernille | `flux-pernille-da` | Female |
| Rasmus   | `flux-rasmus-da`   | Male   |
| Rikke    | `flux-rikke-da`    | Male   |

## Estonian — Early Access

| Voice | Model           | Gender |
| ----- | --------------- | ------ |
| Triin | `flux-triin-et` | Female |

## Finnish — Early Access

| Voice | Model           | Gender |
| ----- | --------------- | ------ |
| Kirsi | `flux-kirsi-fi` | Female |
| Teemu | `flux-teemu-fi` | Male   |

## Greek — Early Access

| Voice  | Model            | Gender |
| ------ | ---------------- | ------ |
| Kostas | `flux-kostas-el` | Male   |

## Gujarati — Early Access

| Voice   | Model             | Gender |
| ------- | ----------------- | ------ |
| Bhavna  | `flux-bhavna-gu`  | Female |
| Hetal   | `flux-hetal-gu`   | Female |
| Jignesh | `flux-jignesh-gu` | Male   |

## Hungarian — Early Access

| Voice  | Model            | Gender |
| ------ | ---------------- | ------ |
| Bence  | `flux-bence-hu`  | Male   |
| Eszter | `flux-eszter-hu` | Female |
| Kinga  | `flux-kinga-hu`  | Female |
| Tibor  | `flux-tibor-hu`  | Male   |

## Indonesian — Early Access

| Voice | Model           | Gender |
| ----- | --------------- | ------ |
| Dewi  | `flux-dewi-id`  | Female |
| Fajar | `flux-fajar-id` | Male   |
| Fitri | `flux-fitri-id` | Female |
| Rizky | `flux-rizky-id` | Male   |
| Teguh | `flux-teguh-id` | Male   |

## Kannada — Early Access

| Voice     | Model               | Gender |
| --------- | ------------------- | ------ |
| Manjunath | `flux-manjunath-kn` | Male   |

## Korean — Early Access

| Voice   | Model             | Gender |
| ------- | ----------------- | ------ |
| Eunji   | `flux-eunji-ko`   | Female |
| Hyunwoo | `flux-hyunwoo-ko` | Male   |
| Mikyung | `flux-mikyung-ko` | Female |
| Minjun  | `flux-minjun-ko`  | Male   |
| Soojin  | `flux-soojin-ko`  | Female |
| Sungmin | `flux-sungmin-ko` | Male   |

## Latvian — Early Access

| Voice  | Model            | Gender |
| ------ | ---------------- | ------ |
| Agnese | `flux-agnese-lv` | Female |
| Edgars | `flux-edgars-lv` | Male   |

## Lithuanian — Early Access

| Voice   | Model             | Gender |
| ------- | ----------------- | ------ |
| Goda    | `flux-goda-lt`    | Female |
| Neringa | `flux-neringa-lt` | Female |

## Malay — Early Access

| Voice | Model           | Gender |
| ----- | --------------- | ------ |
| Haziq | `flux-haziq-ms` | Male   |
| Izzah | `flux-izzah-ms` | Female |

## Marathi — Early Access

| Voice  | Model            | Gender |
| ------ | ---------------- | ------ |
| Pooja  | `flux-pooja-mr`  | Female |
| Pratik | `flux-pratik-mr` | Male   |
| Sneha  | `flux-sneha-mr`  | Female |

## Norwegian — Early Access

| Voice  | Model            | Gender |
| ------ | ---------------- | ------ |
| Erlend | `flux-erlend-no` | Male   |
| Espen  | `flux-espen-no`  | Male   |
| Ida    | `flux-ida-no`    | Female |
| Signe  | `flux-signe-no`  | Female |
| Silje  | `flux-silje-no`  | Female |
| Vegard | `flux-vegard-no` | Male   |

## Polish — Early Access

| Voice   | Model             | Gender |
| ------- | ----------------- | ------ |
| Bartosz | `flux-bartosz-pl` | Male   |
| Ewa     | `flux-ewa-pl`     | Female |
| Justyna | `flux-justyna-pl` | Female |
| Kacper  | `flux-kacper-pl`  | Male   |
| Konrad  | `flux-konrad-pl`  | Male   |
| Zuzanna | `flux-zuzanna-pl` | Female |

## Romanian — Early Access

| Voice  | Model            | Gender |
| ------ | ---------------- | ------ |
| Cosmin | `flux-cosmin-ro` | Male   |
| Ioana  | `flux-ioana-ro`  | Female |

## Slovak — Early Access

| Voice    | Model              | Gender |
| -------- | ------------------ | ------ |
| Dominika | `flux-dominika-sk` | Female |
| Juraj    | `flux-juraj-sk`    | Male   |

## Slovenian — Early Access

| Voice  | Model            | Gender |
| ------ | ---------------- | ------ |
| Gregor | `flux-gregor-sl` | Male   |
| Katja  | `flux-katja-sl`  | Female |

## Swedish — Early Access

| Voice     | Model               | Gender |
| --------- | ------------------- | ------ |
| Axel      | `flux-axel-sv`      | Male   |
| Charlotta | `flux-charlotta-sv` | Female |
| Frida     | `flux-frida-sv`     | Female |
| Ludvig    | `flux-ludvig-sv`    | Male   |
| Oskar     | `flux-oskar-sv`     | Male   |
| Pontus    | `flux-pontus-sv`    | Male   |
| Wilma     | `flux-wilma-sv`     | Female |

## Tagalog — Early Access

| Voice  | Model            | Gender |
| ------ | ---------------- | ------ |
| Jerome | `flux-jerome-tl` | Male   |
| Jomar  | `flux-jomar-tl`  | Male   |
| Liezel | `flux-liezel-tl` | Female |
| Noel   | `flux-noel-tl`   | Male   |
| Trisha | `flux-trisha-tl` | Female |

## Tamil — Early Access

| Voice  | Model            | Gender |
| ------ | ---------------- | ------ |
| Gokul  | `flux-gokul-ta`  | Male   |
| Kavya  | `flux-kavya-ta`  | Female |
| Sowmya | `flux-sowmya-ta` | Female |
| Vinoth | `flux-vinoth-ta` | Male   |

## Telugu — Early Access

| Voice   | Model             | Gender |
| ------- | ----------------- | ------ |
| Pavan   | `flux-pavan-te`   | Male   |
| Ravi    | `flux-ravi-te`    | Male   |
| Sravani | `flux-sravani-te` | Female |

## Turkish — Early Access

| Voice  | Model            | Gender |
| ------ | ---------------- | ------ |
| Dilek  | `flux-dilek-tr`  | Female |
| Ecem   | `flux-ecem-tr`   | Female |
| Emre   | `flux-emre-tr`   | Male   |
| Gizem  | `flux-gizem-tr`  | Female |
| Mehmet | `flux-mehmet-tr` | Male   |
| Serkan | `flux-serkan-tr` | Male   |
| Zeynep | `flux-zeynep-tr` | Female |

## Ukrainian — Early Access

| Voice    | Model              | Gender |
| -------- | ------------------ | ------ |
| Denys    | `flux-denys-uk`    | Male   |
| Solomiya | `flux-solomiya-uk` | Female |

## Urdu — Early Access

| Voice   | Model             | Gender |
| ------- | ----------------- | ------ |
| Ambreen | `flux-ambreen-ur` | Female |
| Usman   | `flux-usman-ur`   | Male   |

## Vietnamese — Early Access

| Voice | Model          | Gender |
| ----- | -------------- | ------ |
| Hoa   | `flux-hoa-vi`  | Female |
| Minh  | `flux-minh-vi` | Male   |

## Languages

Flux TTS voices speak English — with accents spanning American, British, Irish, Australian, Indian, Singaporean, and Filipino English — and 41 other languages:

Bengali (`bn`), Bulgarian (`bg`), Catalan (`ca`), Chinese (`zh`), Croatian (`hr`), Czech (`cs`), Danish (`da`), Dutch (`nl`), Estonian (`et`), Finnish (`fi`), French (`fr`), German (`de`), Greek (`el`), Gujarati (`gu`), Hindi (`hi`), Hungarian (`hu`), Indonesian (`id`), Italian (`it`), Japanese (`ja`), Kannada (`kn`), Korean (`ko`), Latvian (`lv`), Lithuanian (`lt`), Malay (`ms`), Marathi (`mr`), Norwegian (`no`), Polish (`pl`), Portuguese (`pt`), Romanian (`ro`), Russian (`ru`), Slovak (`sk`), Slovenian (`sl`), Spanish (`es`), Swedish (`sv`), Tagalog (`tl`), Tamil (`ta`), Telugu (`te`), Turkish (`tr`), Ukrainian (`uk`), Urdu (`ur`), Vietnamese (`vi`).

Languages marked Early Access do not have text normalization yet: numbers, dates and abbreviations are read as written, so write them out in words. Text normalization is available for English, German, Dutch, French, Hindi, Italian, Japanese, Portuguese, Russian and Spanish.

The voices in these 41 languages are available on `api.deepgram.com`, `api.eu.deepgram.com` and `api.in.deepgram.com`; they are not yet available on the Australia endpoint (`api.au.deepgram.com`).

## Related resources

* [Getting Started (Streaming)](/docs/flux-tts/quickstart) — connect and synthesize with a voice
* [Getting Started (Batch)](/docs/flux-tts/batch) — one-shot synthesis
* [Feature Overview](/docs/flux-tts/feature-overview)
* [Migrating from Aura to Flux TTS](/docs/flux-tts/migrating)
