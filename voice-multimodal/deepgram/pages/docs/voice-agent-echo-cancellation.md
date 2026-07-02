---
title: "Voice Agent Adaptive Echo Cancellation"
source: https://developers.deepgram.com/docs/voice-agent-echo-cancellation.md
path: docs/voice-agent-echo-cancellation
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Voice Agent Adaptive Echo Cancellation

Adaptive echo cancellation reduces or eliminates audio feedback that occurs when a microphone picks up audio from speakers in the same environment, dynamically adjusting based on the audio conditions.

## Purpose

Echo cancellation addresses audio feedback issues in real-time communication applications. Many modern browsers and telephony systems have built-in echo cancellation, so you may not need additional configuration depending on your Voice Agent implementation.

## Browser Implementation

Chrome implements adaptive echo cancellation effectively through its built-in WebRTC capabilities for real-time communication. Most browsers and communication apps enable adaptive echo cancellation by default.

References for browser-based echo cancellation:

* [Native echo cancellation in Chrome](https://developer.chrome.com/blog/more-native-echo-cancellation/?utm_source=chatgpt.com)
* [MediaTrackSettings: echoCancellation property](https://developer.mozilla.org/en-US/docs/Web/API/MediaTrackSettings/echoCancellation?)
* [MediaTrackConstraints: echoCancellation property](https://developer.mozilla.org/en-US/docs/Web/API/MediaTrackConstraints/echoCancellation?)

## Telephony Systems

Modern phones have hardware-level and software-level echo cancellation built in, ensuring users don't hear their own voice echoed back during calls. When integrating with telephony services (PSTN or VoIP), the built-in echo cancellation handles audio issues automatically without requiring additional configuration.

**Examples:**

* VoIP apps integrated with a phone's native dialer benefit from built-in echo cancellation
* No extra code or custom echo management is needed

## What Echo Cancellation Addresses

Echo cancellation is most effective for:

* **Acoustic Echo**: When microphones capture sound from nearby speakers during video calls
* **Audio Feedback**: Preventing repeated amplification of sound in communication systems

Common scenarios where echo cancellation applies:

* Video/audio calls with active speakers and microphones
* Conferencing systems with multiple participants and devices
* Real-time media apps like video chat or gaming applications

## When Echo Cancellation Doesn't Apply

If you're experiencing playback issues unrelated to feedback loops (stuttering, latency, or low volume), the root cause is likely:

* Poor internet connection in streaming applications
* Hardware limitations (faulty speakers or headphones)
* Incorrect audio configurations or codecs
* Incorrect parameters in your Deepgram API request

In Voice Agent workflows, echo cancellation might not be the core issue if you're experiencing other audio problems.

## Noise Suppression, Barge-In & Broader Audio Preprocessing

Echo cancellation is one part of the audio preprocessing picture. For full recommendations on when to use noise suppression, echo cancellation, barge-in strategies, and other preprocessing techniques (including when they can hurt transcription accuracy), see [Audio Preprocessing & Barge-In](/guides/deep-dives/audio-preprocessing-barge-in).
