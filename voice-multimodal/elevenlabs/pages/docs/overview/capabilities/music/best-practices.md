---
title: "Best practices"
source: https://elevenlabs.io/docs/overview/capabilities/music/best-practices.md
path: docs/overview/capabilities/music/best-practices
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Best practices

This guide summarizes the most effective techniques for prompting Music in ElevenCreative. It covers how the model reads a prompt, production vocabulary, musical control, arrangement, vocals, loops, sound design, and structural timing & lyrics.

The model is designed to understand intent and generate complete, context-aware audio based on your goals. High-level prompts like *"ad for a sneaker brand"* or *"peaceful meditation with voiceover"* are often enough to guide the model toward tone, structure, and content that match your use case.

## How the Model Reads a Prompt

A prompt answers five questions, whether you intend it to or not: genre, mood, instrumentation, tempo, and production era. Any question you leave open, the model answers with the most statistically likely choice — which is to say, the most average one.

A prompt that leaves all five open:

```text
upbeat electronic track
```

The same request with all five answered:

```text
French house, 122 BPM, filtered disco sample chops, sidechained bass, tight
four-on-the-floor kick, rooftop-at-sunset mood, warm analog glue
```

The second prompt contains no special technique — every decision in the output is one a person made. Decide genre, mood, instruments, tempo, and era before the model decides for you.

## Genre & Creativity

The model demonstrates strong adherence to genre conventions and emotional tone. It responds effectively to both:

* Abstract mood descriptors (e.g., "eerie," "foreboding")
* Detailed musical language (e.g., "dissonant violin screeches over a pulsing sub-bass")

Prompt length and detail do not always correlate with better quality outputs. For more creative and unexpected results, try using simple, evocative keywords to let the model interpret and compose freely.

## Production Vocabulary

The model understands music the way it's discussed in studios. Studio language moves real levers: *sidechained*, *close-mic'd*, *bone-dry*, *tape saturation*, *plate reverb* each audibly change the mix.

The same ballad in three rooms — only the production words change:

```text
slow soul ballad, 68 BPM, female vocal — bone-dry drums, close-mic'd vocal, dead room
```

```text
slow soul ballad, 68 BPM, female vocal — cavernous plate reverb, tape echo throws, gospel room
```

```text
slow soul ballad, 68 BPM, female vocal — tape saturation, wow and flutter, dusty vinyl crackle
```

If you don't have the vocabulary, describe the space: "sounds like it was recorded in a stairwell" will get you a stairwell.

Production era is a dial like tempo, and the model can turn it mid-song. Naming an era ("1950s rock and roll with slapback echo," "1990s jungle") sets the entire production character, and narrating era changes over time produces coherent transitions within a single track.

## Musical Control

The model accurately follows BPM and often captures the intended musical key. To gain more control over timing and harmony, include tempo cues like "130 BPM" and key signatures like "in A minor" in your prompt. The model holds a stated BPM and key precisely enough to layer the output with other material — a vocal take, a sample, a second generation.

To influence vocal delivery and tone, use expressive descriptors such as "raw," "live," "glitching," "breathy," or "aggressive." Delivery notes work the same way: *whispered*, *belted*, *conversational*, *deadpan*, *stacked harmonies*. The same lyric under opposite instructions:

```text
whispered indie folk, close and intimate, fingerpicked acoustic guitar
```

```text
stadium rock, belted powerhouse vocal, huge drums, wall of guitars
```

The model can effectively render multiple vocalists — use prompts like "two singers harmonizing in C" to direct vocal arrangement.

In general, more detailed prompts lead to greater control and expressiveness in the output.

## Arrangement

The model follows instructions about time. Narrate the arrangement in order, the way you'd brief a band:

```text
UK garage, 132 BPM — start with just a shuffled drum loop, add a warm sub bassline
after four bars, then bring in chopped vocal stabs for the drop
```

The load-bearing words are small: *start with*, *just*, *then*, *bring in*. Without the *just*, the model fills the silence — mark the silences explicitly.

## Loops

A loop prompt is an exercise in exclusion. State the bars, the BPM, the key — and state what's banned:

```text
boom bap drum break, 90 BPM, dusty and swung, four bars, no melody — just drums
```

```text
dreamy guitar loop, 140 BPM, F sharp minor, emo trap, four bars, instrumental
```

"No melody, just drums" is the entire reason the drum break stays a drum break. For loops, the negative space is the prompt.

## Structural Timing & Lyrics

You can specify the length of the song (e.g., "60 seconds") or use auto mode to let the model determine the duration. If lyrics are not provided, the model will generate structured lyrics that match the chosen or auto-detected length.

By default, most music prompts will include lyrics. To generate music without vocals, add "instrumental only" to your prompt. You can also write your own lyrics for more creative control. The model uses your lyrics in combination with the prompt length to determine vocal structure and placement.

To manage when vocals begin or end, include clear timing cues like:

* "lyrics begin at 15 seconds"
* "instrumental only after 1:45"

The model supports multilingual lyric generation. To change the language of a generated song in our UI, use follow-ups like "make it Japanese" or "translate to Spanish."

## Instrument & Vocal Isolation

To create stems with greater control, use targeted prompts and structure:

* Use the word "solo" before instruments (e.g., "solo electric guitar," "solo piano in C minor").
* For vocals, use "a cappella" before the vocal description (e.g., "a cappella female vocals," "a cappella male chorus").

To improve stem quality and control:

* Include key, tempo (BPM), and musical tone (e.g., "a cappella vocals in A major, 90 BPM, soulful and raw").
* Be as musically descriptive as possible to guide the model's output.

## Sound Design

The model renders sound itself, and it holds no opinion on whether the sound you're describing could physically occur. Non-musical audio — sound effects, ambience, textures — can be prompted directly or incorporated within a track:

```text
a thunderstorm in 6/8 — thunder lands on the downbeat, rain fills the offbeats,
distant lightning as crash cymbals
```

```text
one enormous cathedral bell that, as it decays, slowly turns out to have been
a choir all along
```

```text
an orchestra tuning up that accidentally becomes techno — the A gets a kick drum,
chaos becomes a groove
```

The method: take a sound that exists, give it one property it has no business having, and describe the result with a straight face. Every technique in this guide — keys, BPM, sidechaining, narrated arrangement — works on these sounds as raw material.

## Audio Reference

Some ideas resist description — a melody you hummed into your phone, the swing of one specific bassline, a texture you can only point at. Upload a track (a voice memo qualifies) as an [Audio Reference](https://elevenlabs.io/blog/introducing-references-sound-control-for-music-v2), and the model matches its feel, groove, and palette without copying the notes.

The prompt still steers everything the reference leaves open. The pairing that works: a reference that carries the feel, and a prompt that says what should be different — "same energy, half-time drums, female vocal."

Uploads can be \~30 seconds. Every reference track passes a copyright check before generation — Audio Reference is designed for music you've made yourself.

## Sample Prompts

The model allows you to move beyond song descriptors and into intent for maximum creativity.

#### Mascara Ad

```text
Track for a high-end mascara commercial. Upbeat and polished. Voiceover only.
The script begins: "We bring you the most volumizing mascara yet." Mention the brand
name "X" at the end.
```

#### Synthwave Anthem

```text
synthwave arpeggio anthem, F minor, 128 BPM, neon nostalgia, analog polysynth pads
```

#### Experimental

```text
a dial-up modem handshake harmonised by a gospel choir, in E flat
```

#### Century of Recording

```text
one melody carried through a century of recording, without stopping — it starts on a
crackling 1920s gramophone as hot jazz, turns into 1950s rock and roll with slapback
echo, blooms into 1970s disco, gets swallowed by a 1990s jungle rave, and lands in
the present as glossy hyperpop. The same tune the whole way.
```

#### Bedroom Pop

```text
Bedroom pop about a city at 5am, 96 BPM, A minor — muted guitar chops, soft breakbeat,
tape-warm bass. Verse close and conversational, chorus opens wide with stacked harmonies.
```

## Summary

Three habits cover most of this guide:

1. **Be specific.** Genre, mood, instruments, tempo, era — decide all five, or the model decides for you.
2. **Speak production.** Studio vocabulary moves real levers, and the model holds numbers exactly.
3. **Constrain what matters, leave space everywhere else.** Narrated arrangements, explicit exclusions, direction for the voice.

## Advanced: Composition plans

For precise control over section structure, lyrics placement, and multi-vocalist arrangements, use composition plans instead of simple text prompts.

#### [Composition plans guide](/docs/eleven-api/guides/how-to/music/composition-plans)

Learn how to structure songs with sections, global/local styles, and proper lyrics formatting for
maximum control.
