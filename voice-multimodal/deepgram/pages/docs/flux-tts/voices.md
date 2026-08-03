---
title: "Flux TTS Voices & Languages"
source: https://developers.deepgram.com/docs/flux-tts/voices.md
path: docs/flux-tts/voices
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Flux TTS Voices & Languages

**Early Access.** Flux TTS and the `/v2/speak` API are in Early Access — the API surface and voice catalog may change before general availability.

Flux TTS voices use the model string format `flux-{voice}-{language}` (e.g. `flux-haley-en`). The same voice catalog is served on both `/v2/speak` transports — the [streaming WebSocket](/docs/flux-tts/quickstart) and [batch REST](/docs/flux-tts/batch).

**Launch catalog.** These are the English voices available at launch. The catalog will expand, and multilingual voices (`flux-{voice}-multi`) are planned for a later release.

## Selecting a voice

Pass the model string on connection:

```
wss://api.deepgram.com/v2/speak?model=flux-haley-en
```

Every voice handles general conversational synthesis. Use the character notes below to shortlist, then audition candidates on your own copy.

## Voices

| Voice   | Model             | Accent     | Gender | Age   | Character                                              |
| ------- | ----------------- | ---------- | ------ | ----- | ------------------------------------------------------ |
| Haley   | `flux-haley-en`   | American   | Female | 18–24 | Clear, confident, thoughtful, pleasant, nice           |
| Heather | `flux-heather-en` | American   | Female | 18–24 | Clear, engaging, energetic, friendly, thoughtful       |
| Cole    | `flux-cole-en`    | American   | Male   | 18–24 | Friendly, clear, interesting, energetic, engaging      |
| Alexis  | `flux-alexis-en`  | American   | Female | 18–24 | Friendly, intelligent, fast, confident, energetic      |
| Priya   | `flux-priya-en`   | Indian     | Female | 25–34 | Confident, empathetic, professional, calm, reassuring  |
| Jack    | `flux-jack-en`    | British    | Male   | 25–34 | Confident, thoughtful, friendly, professional, clear   |
| Bruce   | `flux-bruce-en`   | American   | Male   | 25–34 | Friendly, kind, natural, believable, engaged           |
| Rufus   | `flux-rufus-en`   | British    | Male   | 25–34 | Friendly, confident, intelligent, gentle, enthusiastic |
| Drew    | `flux-drew-en`    | American   | Male   | 25–34 | Confident, relaxed, soft, young, calm                  |
| Renee   | `flux-renee-en`   | American   | Female | 55+   | Friendly, bold, warm, professional, kind               |
| Marcus  | `flux-marcus-en`  | American   | Male   | 25–34 | Friendly, helpful, smooth, professional, kind          |
| Sharon  | `flux-sharon-en`  | Australian | Female | 18–24 | Formal, calm, relaxed, stiff, confident                |

## Related resources

* [Getting Started (Streaming)](/docs/flux-tts/quickstart) — connect and synthesize with a voice
* [Getting Started (Batch)](/docs/flux-tts/batch) — one-shot synthesis
* [Feature Overview](/docs/flux-tts/feature-overview)
* [Migrating from Aura to Flux TTS](/docs/flux-tts/migrating)

---
