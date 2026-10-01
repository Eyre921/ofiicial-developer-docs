---
title: "Eleven v4"
source: https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4.md
path: docs/overview/capabilities/text-to-speech/eleven-v4
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Eleven v4

Eleven v4 is our latest and most advanced Text to Speech model, and the first in a new generation of models. It improves output quality, voice accuracy, consistency, emotion, delivery, audio tags, and language coverage compared with Eleven v3.

In general, Eleven v4 is a net upgrade over Eleven v3, delivering better results in almost every case. We strongly recommend switching to v4 and testing it with your own voices and content to see the difference for yourself. While a few edge cases may call for a different fit, most users should find v4 the better choice.

For tags, punctuation, and dialogue prompting, see [Prompting Eleven v4](/docs/overview/capabilities/text-to-speech/best-practices#prompting-eleven-v4).

## Voice cloning

Voice cloning accuracy takes a major step forward with Eleven v4. Cloned voices capture the source voice's characteristics — timbre, cadence, and delivery — more faithfully than any previous model.

Instant Voice Clones (IVCs) are more accurate than ever in Eleven v4. They capture the defining characteristics of a source voice more faithfully, making it easier to create a convincing clone quickly from a short audio sample.

> **Tip**
>
> Instant Voice Cloning has received a significant upgrade in Eleven v4, delivering noticeably
> better accuracy overall. If you haven't tried it yet, now is a good time to test it with your own
> audio.

Professional Voice Clones (PVCs) are fully supported in Eleven v4. They build on the same advances in voice accuracy, offering a more faithful reproduction of the source voice for workflows that require the highest level of consistency and control.

> **Warning**
>
> Professional Voice Clone support for Eleven v4 is currently rolling out to everyone and should be
> available within the next few days.

Because of this significant leap in accuracy, Eleven v4 may sound substantially different from Eleven v3. Eleven v3 laid the foundation for Eleven v4, with a strong emphasis on delivery and accuracy, while Eleven v4 builds on that foundation with substantially improved voice accuracy. As a result, Eleven v4 is designed to capture the source voice more faithfully, though you may still prefer how a voice sounded in Eleven v3. Accuracy and personal preference are not always the same, so we recommend comparing both versions with your own content to choose the best fit for your use case.

Considering that Eleven v4 more faithfully reproduces the source voice's characteristics, including its accent, delivery, loudness, and other distinctive qualities, the quality of the source recording matters more than ever. Clear, clean training audio helps Eleven v4 capture the voice accurately, without introducing unwanted sounds or characteristics. Background noise, distortion, or other recording issues can affect the result.

We're still experimenting with Eleven v4 to understand how best to use it. So far, it seems much better at capturing nuanced audio, particularly when there's a lot of training audio, as with Professional Voice Clones. Our guidance on using varied training data may change as we continue testing how to control the model with a more versatile dataset. For now, we recommend sticking to a single speaking style in your training audio, which Eleven v4 should capture better than earlier models.

## Native accent handling

This is one of the biggest changes in Eleven v4 compared to any of the older models, and it's worth understanding clearly.

When the language you're generating matches the language of your reference voice, the original accent is preserved exactly as before.

When the language you're generating is different from the reference voice's language, Eleven v4 generates fluent, natural-sounding speech in the target language — rather than carrying over the reference voice's accent from its original language.

In practice: if you clone a voice from a Korean speaker and generate English, Eleven v4 will produce natural, fluent English rather than English spoken with a Korean accent. This makes every voice usable across every supported language, and is especially useful for dubbing, multilingual content, and voice agents that need to serve users in different languages from a single voice.

If your workflow depends on a voice carrying its native accent into other languages, test this behavior directly with Eleven v4 before migrating — it's a deliberate change in how cross-language generation works, not a bug.

However, this new functionality is still being fine-tuned, and we are exploring ways to make it a toggle instead of having it always on. That is still a research project, so we do not have a timeline or any further information about it at this point.

## Model variants

Eleven v4 comes in two variants, so you can choose the right balance of quality and speed for your use case:

* **Eleven v4** (`eleven_v4`) — our highest-quality model, ideal for content creation, audiobooks, character voiceovers, and any use case where quality is the top priority.
* **Eleven v4 Turbo** (`eleven_v4_turbo`) — extremely high quality while retaining impressively low latency, purpose-built for real-time use cases like conversational agents and interactive voice experiences.

Both variants use two voice settings: Stability and Similarity.

Stability controls how consistent the delivery stays across generations. Lower values allow more expressive, varied delivery; higher values keep the performance closer to a fixed baseline.

Similarity controls how closely the output adheres to the reference voice. Higher values enforce closer adherence to the reference, which can come at the cost of some naturalness.

Style and Speed sliders are not available in Eleven v4, and SSML is not supported.

Audio tags (e.g. `[whispering]`, `[shouting]`, `[laughing]`) let you direct delivery with fine-grained control, and Eleven v4 handles them with a level of nuance beyond previous models. They're not perfect yet, and we're continuing to iterate and improve how reliably the model follows tag instructions — this is an active area of ongoing investment, and it will keep getting better.

## Showcase

> **Warning**
>
> These examples are raw. Nothing has been heavily post-processed: no EQ, compression,
> normalization, de-essing, plosive removal, or similar. If you hear any recurring issues, such as
> clipping, plosives, uneven EQ, or jumps in volume, they are very likely in the training data for
> that voice. The Eleven v4 model just captured them, since it is very accurate, even when capturing
> flaws. We left the audio untouched so you can hear what the model produced.

### Voice cloning accuracy

Each example starts with a Voice Library preview. We then took some text and generated it using an Instant Voice Clone of that voice on both Eleven v3 and Eleven v4.

This isn’t a perfect comparison. Eleven v4 also works with Professional Voice Clones, which can take the match further. However, to keep things fairer, we used Instant Voice Clones for both Eleven v3 and Eleven v4.

These examples show how much of the original voice the model picks up. It’s important to note that this also includes EQ, quality, volume, and any other minor details and imperfections in the audio, such as plosives, harsh sibilance, and volume fluctuation.

Listen to the preview, then Eleven v3, then Eleven v4.

<elevenlabs-audio-player audio-title="Preview" audio-src="https://storage.googleapis.com/eleven-public-cdn/documentation_assets/audio/eleven-v4-accuracy-01-reference.mp3" />

<elevenlabs-audio-player audio-title="Eleven v3" audio-src="https://storage.googleapis.com/eleven-public-cdn/documentation_assets/audio/eleven-v4-accuracy-01-v3.mp3" />

<elevenlabs-audio-player audio-title="Eleven v4" audio-src="https://storage.googleapis.com/eleven-public-cdn/documentation_assets/audio/eleven-v4-accuracy-01-v4.mp3" />

Voice `NfUrCNRReUL9RXS9upG1`.

```text
"Brother... I must cross the sea, though I'd rather stay beside you. If the gods will it, we'll see each other again. Until then, when the sun sinks beyond the waves, know that I'll be looking toward home."

He clasped my forearm beneath the pale morning sky. I held on a moment longer, then watched him turn toward the waiting ship.
```

<elevenlabs-audio-player audio-title="Preview" audio-src="https://storage.googleapis.com/eleven-public-cdn/documentation_assets/audio/eleven-v4-accuracy-02-reference.mp3" />

<elevenlabs-audio-player audio-title="Eleven v3" audio-src="https://storage.googleapis.com/eleven-public-cdn/documentation_assets/audio/eleven-v4-accuracy-02-v3.mp3" />

<elevenlabs-audio-player audio-title="Eleven v4" audio-src="https://storage.googleapis.com/eleven-public-cdn/documentation_assets/audio/eleven-v4-accuracy-02-v4.mp3" />

Voice `HBDoL4wkcalemIO0nUAu`.

```text
"When I was young, I thought the mountain stood because it was strong. Then winter came, and the mountain wore its crown of snow without complaint. Spring followed, and it let every stream run free.

"So remember, traveler: strength is not always holding fast. Sometimes it is knowing what to carry, and what the season asks you to release."
```

### Voice acting

These are Eleven v4 generations. The audio tags in the text direct the delivery.

<elevenlabs-audio-player audio-title="Voice acting 1" audio-src="https://storage.googleapis.com/eleven-public-cdn/documentation_assets/audio/eleven-v4-voice-acting-01.mp3" />

Voice `EkK5I93UQWFDigLMpZcX`.

```text
[casual] "You're looking for work, eh? Hmm, I might have something for you. Just outside the valley, there's a group of wild horned boars I need you to take care of - nasty little beasts. The village would be grateful if you could get that done, and I'll make it worth your while."
------------
[annoyed] [under his breath] "Oh, you again... [sigh] Did you take care of that little problem I mentioned earlier? No, not yet? All right, off you go. I don't have time to chitchat. I'm busy standing here... handing out quests."
------------
[ecstatic] "You did it, you crazy bastard! [dismissive] Not that I didn't have any faith in you, but you wouldn't be the first one to fail. Yes, yes, I know. One of them might have been a little bigger than the others. But hey, you survived. You got it done. You helped the village."
```

<elevenlabs-audio-player audio-title="Voice acting 2" audio-src="https://storage.googleapis.com/eleven-public-cdn/documentation_assets/audio/eleven-v4-voice-acting-02.mp3" />

Voice `t7VaN65ClS2VrEUwk1nR`.

```text
[quietly curious] "Hmm… that mark. I haven't seen one like it in years. Where did you get it? Oh, you gonna make me guess? [giggle]"
------------
[measured] "No need to explain, if you'd rather not. This town has a way of leaving its mark on people. [soft chuckle] Usually not quite so literally."
------------
[lower, thoughtful] "Keep it covered when you can. There are still a few who remember what it means, and they may not ask as politely as I have."
```

### Audiobook

This is an Eleven v4 narration. The tags set the pace and the tone of the scene.

<elevenlabs-audio-player audio-title="Audiobook" audio-src="https://storage.googleapis.com/eleven-public-cdn/documentation_assets/audio/eleven-v4-audiobook-01.mp3" />

Voice `KHRvDizAHFVPzoSehNY6`.

```text
[Quiet, measured narration] The moonlit training court lay beneath the keep, its stone walls silvered with frost. Beyond the battlements, a dragon's distant call rolled over the mountains.

Sir Alden lifted his blunted practice sword. "Ready?"

Bram, his broad shoulders wrapped in a travel-worn cloak, studied the wooden shield strapped to his arm. "I've faced worse odds."

[Pause, dry amusement] "You lost to a turnip cart yesterday," Sir Alden said.

"It was a very determined cart," Bran muttered

[Gradually building energy] They circled across the frost-dusted stones. One step. Another. Alden watched Bram's hands; Bram watched the faint blue glow gathering along Alden's blade. The air between them prickled with harmless magic.

[Quick, light, playful pace] Bram charged. Alden slipped aside. Clack! Wood met steel. Bram turned, his cloak flaring, and swung wide. Alden ducked beneath it. Bram's boot skidded on the frost; he windmilled, caught himself, and bowed as if he'd meant to do that all along.

"Magnificent," Alden said.

"I was giving you time to admire the cloak," Bran retorted.
```

## The model will keep evolving

Eleven v4 is under active, continuous development. As we keep training and improving the model after launch, its behavior may shift over time as quality improves. We recommend periodically re-testing your use case as the model evolves, and we'll share meaningful updates as they roll out.

## FAQ

#### Which languages does Eleven v4 support?

Eleven v4 supports Afrikaans, Amharic, Arabic, Armenian, Assamese, Asturian, Azerbaijani,
Belarusian, Bengali, Bosnian, Bulgarian, Burmese, Cantonese, Catalan, Cebuano, Croatian, Czech,
Danish, Dutch, English, Estonian, Filipino, Finnish, French, Fula (Pulaar), Galician, Georgian,
German, Greek, Gujarati, Hausa, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian,
Japanese, Kannada, Kazakh, Korean, Kyrgyz, Lao, Lingala, Lithuanian, Luganda, Luxembourgish,
Macedonian, Malay, Malayalam, Maltese, Mandarin Chinese, Māori, Marathi, Mongolian, Nepali,
Norwegian Bokmål, Occitan, Odia, Pashto, Persian, Polish, Portuguese (Brazil), Punjabi, Romanian,
Russian, Serbian, Shona, Sindhi, Slovak, Slovenian, Somali, Sorani Kurdish, Spanish (LatAm),
Swahili, Swedish, Tajik, Tamil, Telugu, Thai, Turkish, Ukrainian, Urdu, Uzbek, Vietnamese, Welsh,
and Wolof.

Some languages are handled more fluently than others, but in general Eleven v4 handles the large
majority of these very well.

#### Will a cloned voice retain its accent?

When the reference voice and generated speech are in the same language, the voice's accent is
preserved. For example, if you clone someone speaking English with a particular English accent
and generate English speech, that accent will be retained.

#### Can I make a voice speak another language with its original accent?

By default, when the generated language differs from the reference voice's language, Eleven v4
aims for fluent, natural-sounding speech in the target language rather than carrying over the
reference accent. You can try using audio tags to guide an accent or delivery style, but results
may vary, so test your specific voice and use case.

#### Will an Eleven v4 clone sound like its Eleven v3 version?

In general, Eleven v4 reproduces the source voice's characteristics much more accurately than
Eleven v3, including its timbre, cadence, delivery, and other mannerisms. As a result, an Eleven
v4 clone will generally sound more like the source voice, and may sound quite different from its
Eleven v3 version.

#### Do I need to train Eleven v4?

Eleven v4 works with both [Instant Voice Cloning](/docs/eleven-creative/voices/voice-cloning/instant-voice-cloning) and [Professional Voice Cloning](/docs/eleven-creative/voices/voice-cloning/professional-voice-cloning).

With Instant Voice Cloning, you create a voice without a separate training step. Upload a short sample, generally one to two minutes, and within seconds you have a voice you can use.

[Professional Voice Cloning](/docs/eleven-creative/voices/voice-cloning/professional-voice-cloning) works the same way it does for earlier models. It trains a dedicated model on a longer set of recordings.

If you already have a Professional Voice Clone and want to train it on Eleven v4, open [My Voices](https://elevenlabs.io/app/voice-lab), find the voice in the list, and hover over it. You will see the models available for that voice. Click the plus button next to Eleven v4 to start fine-tuning.

#### Should I use Voice Design with Eleven v4?

Voice Design voices work with Eleven v4, but they may not be as performative or sound as good as
with earlier models.
