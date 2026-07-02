---
title: "Audio Preprocessing & Barge-In"
source: https://developers.deepgram.com/guides/deep-dives/audio-preprocessing-barge-in.md
path: guides/deep-dives/audio-preprocessing-barge-in
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Audio Preprocessing & Barge-In

Audio preprocessing — noise suppression, echo cancellation, and related signal processing — is one of the most common questions we hear from customers building with Deepgram. The short answer: **it depends on your use case.** For voice agents, preprocessing can improve conversational flow. For transcription accuracy, it often makes things worse.

This guide explains the tradeoffs and provides concrete recommendations based on real-world experience across hundreds of production deployments.

## The Noise Reduction Paradox

Modern speech-to-text models like Nova and Flux are trained on diverse, real-world audio — including noisy environments, background chatter, and imperfect microphones. These models extract patterns from the full acoustic signal, including parts that humans might consider "noise."

When you apply noise suppression before sending audio to Deepgram:

* The suppression algorithm strips acoustic details that the ASR model relies on to distinguish phonetic elements.
* It inevitably removes some speech components alongside noise, especially for soft or quiet speakers.

**The result:** enterprise customers consistently report lower transcription accuracy after applying noise suppression, particularly in domain-specific use cases where subtle speech cues matter (healthcare, legal, financial services).

For a deeper dive into the science behind this, read our blog post: [The Noise Reduction Paradox: Why It May Hurt Speech-to-Text Accuracy](https://deepgram.com/learn/the-noise-reduction-paradox-why-it-may-hurt-speech-to-text-accuracy).

## When Preprocessing Helps

Noise suppression and echo cancellation provide the most value in **voice agent** scenarios where audio quality affects conversational flow:

* **Reducing false barge-ins**: Background noise (TV, traffic, other conversations) can be misinterpreted as speech, causing the agent to stop talking or respond prematurely. Noise suppression reduces these false triggers.
* **Echo cancellation**: Prevents the agent's own TTS output from being captured by the microphone and re-transcribed, which causes the agent to respond to itself.
* **Noisy physical environments**: Drive-throughs, retail floors, warehouses, and other high-ambient-noise settings where the signal-to-noise ratio is very low.

## When Preprocessing Can Hurt

Noise suppression doesn't always degrade transcription — but the risk is highest in these scenarios:

* **Pre-recorded audio transcription**: Call center recordings, meeting recordings, podcasts, and media files. Deepgram's models handle background noise natively and often produce better results on unaltered audio. See [The Noise Reduction Paradox](https://deepgram.com/learn/the-noise-reduction-paradox-why-it-may-hurt-speech-to-text-accuracy) for a deeper look at why.
* **Clean or moderate-noise environments**: Office calls, phone conversations, and video meetings where the audio is already good enough for the model. Preprocessing adds risk with little upside.
* **Domain-specific transcription**: Medical dictation, legal proceedings, financial services — where every word matters and suppression artifacts can cause critical errors.
* **Accented or quiet speakers**: Noise suppression disproportionately affects speakers with softer voices or non-standard accents, clipping parts of their speech.
* **Short utterances**: Noise suppression clips the first words of utterances and disproportionately affects short responses — names, "yes," "no," and single-word answers.

In all of these cases, the impact depends on the specific audio, environment, and suppression algorithm. The only way to know for certain is to A/B test with and without preprocessing on representative samples from your production audio.

**Sample rate:** Deepgram models are trained across the full range of audio quality. The sweet spot is **16 kHz** — there is no accuracy gain above this. If your telephony audio is band-limited to 8 kHz, upsampling to a higher rate provides no benefit.

## Recommendations

**Always test without preprocessing first.** Deepgram's models are trained on real-world audio and handle noise natively. Many customers who A/B test find that removing noise suppression improves transcription accuracy. Only add preprocessing if you can measure a clear improvement on your own audio.

Based on extensive testing across voice agent and transcription deployments, here are our recommendations in priority order:

### 1. Start With Platform-Native Echo Cancellation

Use what the operating system or browser gives you. Platform-level echo cancellation has direct access to both the microphone and speaker output, so time alignment is handled automatically. This is the easiest and most effective first step.

| Platform                  | Implementation                                        | Notes                                                |
| ------------------------- | ----------------------------------------------------- | ---------------------------------------------------- |
| **Web (browser)**         | `getUserMedia({ audio: { echoCancellation: true } })` | Enables the browser's WebRTC AEC                     |
| **iOS**                   | `AVAudioSession` with Voice Processing I/O            | Hardware-level echo cancellation                     |
| **Android**               | `VOICE_COMMUNICATION` audio mode                      | Hardware-level echo cancellation                     |
| **Telephony (PSTN/VoIP)** | Built-in                                              | Modern phones handle echo cancellation automatically |

```javascript
// Browser example
navigator.mediaDevices.getUserMedia({
  audio: {
    sampleRate: 16000,
    channelCount: 1,
    echoCancellation: true,
    noiseSuppression: false, // See recommendation #2
  },
});
```

Platform-native echo cancellation isn't perfect, but it's closest to the audio source and essentially free. Start here before adding anything else.

AEC algorithms are dynamic — they "learn" the acoustic environment when audio starts flowing. Having the agent speak an opening greeting helps the AEC calibrate before the customer responds, which reduces echo in the critical first seconds of a conversation.

### 2. Add Noise Suppression for Voice Agents (If Needed)

If you're building a voice agent and experiencing false barge-ins or degraded conversational flow, consider adding noise suppression with a tool like [Krisp](https://krisp.ai/).

What matters most is the **signal-to-noise ratio (SNR)** reaching the microphone — which is affected by background noise, but also by mic distance, placement, room acoustics, and hardware quality. This is why no single suppression level works for every deployment.

**Key guidelines:**

* **Tune suppression for your specific use case.** Higher suppression removes more noise but increases the risk of clipping speech — particularly short utterances, quiet speakers, and the first words of a conversation. The optimal level depends on your environment, hardware, and speaker population — there is no universal "right" setting. Start conservative and increase only if false barge-ins persist.
* **Adjust dynamically if possible.** A quiet office needs less suppression than a drive-through. If your deployment spans multiple environments, consider tuning suppression levels per environment rather than using a single global setting.
* **Test on your own audio.** The impact varies significantly by environment, speaker population, and use case. Always A/B test with and without suppression on representative audio before committing to a setting.

For pure transcription use cases (pre-recorded or streaming), we recommend skipping noise suppression entirely. Send unaltered audio to Deepgram for the best accuracy.

### 3. Use Keyterm Boosting to Handle Echo Bleed

Even with good echo cancellation, some echo will make it through to the speech-to-text engine. Rather than adding more aggressive audio processing, use Deepgram's [Keyterm](/docs/keyterm) feature to handle known patterns.

For example, if the AI agent's greeting bleeds through and gets transcribed, you can map known phrases to empty strings or use keyterm boosting to ensure domain-specific vocabulary is transcribed correctly despite minor echo artifacts.

Another approach: compare STT output against the known TTS text your agent just spoke. If the transcript matches what the agent said, discard it — this is a lightweight, software-level echo cancellation technique that requires no audio pipeline changes.

Both approaches are fast to implement and can be iterated on as you discover patterns in production.

### 4. Server-Side WebRTC AEC (Advanced)

Server-side echo cancellation is powerful but non-trivial. Consider it only if you have:

* **Dual-channel audio access**: A separate microphone stream and speaker reference stream (common with hardware devices like kiosks or drive-through systems).
* **Zero clock skew**: Both streams come from the same audio frame, so time alignment is automatic.

If you're on iOS or web and attempting server-side AEC, you need to capture TTS playback as a reference stream and time-align it with the microphone input — this is significantly more complex.

**If you go this route:**

* Gate the AEC so it only activates when the reference signal is above a threshold. Running AEC on silence introduces artifacts.
* Use a wet/dry blend rather than 100% AEC output so you can dial back suppression without destroying the customer's voice.
* Be aware that aggressive AEC suppression makes barge-in harder — the system may suppress the customer's voice along with the echo.

## Triggering Barge-In

We strongly recommend using Deepgram's built-in speech detection rather than an external Voice Activity Detector (VAD) for triggering barge-in. Client-side VADs are sensitive to any audio energy — background noise, TV speech, door slams — which leads to frequent false positives (unintentional interruptions). Deepgram's approach operates at the model level, so it understands speech content rather than just audio energy, resulting in significantly fewer false triggers.

The tradeoff: Deepgram's model-level detection may have slightly higher latency than a client-side VAD, since it waits for enough audio to confirm real speech. In practice, this produces a better user experience because the agent interrupts less often by mistake.

### Flux (Recommended)

Flux has integrated, semantically-aware turn detection built into the model itself. It produces `StartOfTurn` and `EndOfTurn` events as part of the decode process — not from a separate VAD pipeline.

To trigger barge-in with Flux, listen for a `StartOfTurn` message. Every `StartOfTurn` is guaranteed to contain a non-empty transcript, which means you won't get false triggers from silence or noise. This is the most reliable approach for barge-in, especially in noisy environments.

### Nova-3

For barge-in with Nova-3 streaming, listen for non-empty interim result transcripts. Our recommended approach is to require at least 2 words in an interim result before triggering, or wait for a final result with at least 1 word. This balances responsiveness with accuracy and avoids false triggers from single-word noise artifacts.

If you need more sensitivity, you can trigger on any interim result with at least 1 word — but expect a higher rate of false positives.

### When to Consider an External VAD

Use a standalone VAD (such as [Silero VAD](https://github.com/snakers4/silero-vad)) only if you need the lowest possible barge-in latency and can tolerate a higher rate of false positives. This is a deliberate tradeoff — you gain responsiveness but lose precision. In most voice agent deployments, Deepgram's model-level approach produces a better overall experience.

## Decision Matrix

| Use Case                          |       Echo Cancellation       |       Noise Suppression       | Keyterm Boosting |
| --------------------------------- | :---------------------------: | :---------------------------: | :--------------: |
| Voice agent (browser)             |     Yes (platform-native)     | Test and tune per environment |        Yes       |
| Voice agent (mobile app)          |         Yes (OS-level)        | Test and tune per environment |        Yes       |
| Voice agent (drive-through/kiosk) | Yes (hardware or server-side) |   Yes, tune per environment   |        Yes       |
| Voice agent (telephony)           |            Built-in           |      Usually unnecessary      |     Optional     |
| Pre-recorded transcription        |              N/A              |             **No**            |     Optional     |
| Streaming transcription           |            Optional           |             **No**            |     Optional     |
| Meeting/call recording            |              N/A              |             **No**            |     Optional     |

## Further Reading

* [Voice Agent Echo Cancellation](/docs/voice-agent-echo-cancellation) — browser and telephony echo cancellation specifics for voice agents
* [Voice Agent Audio & Playback](/docs/voice-agent-audio-playback) — troubleshooting audio output issues
* [Keyterm Prompting](/docs/keyterm) — boost domain-specific vocabulary for better accuracy
* [The Noise Reduction Paradox](https://deepgram.com/learn/the-noise-reduction-paradox-why-it-may-hurt-speech-to-text-accuracy) — deep dive into why noise suppression can hurt STT accuracy

For transcription use cases, skip noise suppression and send unaltered audio to Deepgram — the models handle noise natively and preprocessing can degrade accuracy. For voice agents, use platform-native echo cancellation and Deepgram's built-in turn detection (Flux StartOfTurn or Nova-3 interim results) rather than an external VAD — model-level detection has far fewer false positives. Only add noise suppression if A/B testing on your own audio shows improvement, and tune the level for your specific environment.
