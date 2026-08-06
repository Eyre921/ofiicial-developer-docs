---
title: "Model Options"
source: https://developers.deepgram.com/docs/model.md
path: docs/model
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Model Options

`model` *string* Default: `base-general`

&#x20;Pre-recorded

&#x20;Streaming:Nova

Streaming:Flux

Deepgram’s Model feature allows you to supply a model to use when processing submitted audio. To learn more about the pricing for our different models, see [Deepgram Pricing & Plans](https://deepgram.com/pricing/).

## Models & Model Options

Below are a list of all model and model options that can be used with the Deepgram API.

### Flux

**Examples**

```
https://api.deepgram.com/v2/listen?model=flux-general-en
```

```
https://api.deepgram.com/v2/listen?model=flux-general-multi&language_hint=es
```

Flux is the first conversational speech recognition model built specifically for voice agents. Unlike traditional STT that just transcribes words, Flux understands conversational flow and automatically handles turn-taking. Flux tackles the most critical challenges for voice agents today: knowing when to listen, when to think, and when to speak. The model features first-of-its-kind model-integrated end-of-turn detection, configurable turn-taking dynamics, and ultra-low latency optimized for voice agent pipelines, all with Nova-3 level accuracy.

Flux Multilingual (`flux-general-multi`) extends Flux to 10 languages with an optional `language_hint` parameter that biases output toward specified languages. See [Language Prompting](/docs/flux/language-prompting) for details.

### Nova-3

**Examples**

```
https://api.deepgram.com/v1/listen?model=nova-3
```

Nova-3 represents a significant leap forward in speech AI technology, featuring substantial improvements in accuracy and real-world application capabilities. The model delivers industry-leading performance with a 53.4% reduction in word error rate (WER) for streaming and 47.4% for batch processing compared to competitors. Nova-3 introduces groundbreaking features including real-time multilingual conversation transcription, enhanced comprehension of domain-specific terminology, and optional personal information redaction. Notably, it's the first voice AI model to offer self-serve customization, enabling instant vocabulary adaptation without model retraining. In multilingual testing, Nova-3 demonstrated superior performance across all seven tested languages, with particularly strong results showing up to 8:1 preference ratios in certain languages.

Nova-3 has the following model options which can be called by using the following syntax: `model=nova-3-{option}`

* `general`: Optimized for everyday audio processing.
* `medical`: Optimized for audio with medical oriented vocabulary.

### Nova-2

**Examples**

```text Text
https://api.deepgram.com/v1/listen?model=nova-2
```

```text Text
https://api.deepgram.com/v1/listen?model=nova-2-phonecall
```

Nova-2 expands on Nova-1's advancements with speech-specific optimizations to the underlying Transformer architecture, advanced data curation techniques, and a multi-stage training methodology. These changes yield reduced word error rate (WER) and enhancements to entity recognition (i.e. proper nouns, alphanumerics, etc.), punctuation, and capitalization.

Nova-2 has the following model options which can be called by using the following syntax: `model=nova-2-{option}`

* `general`: Optimized for everyday audio processing.
* `meeting`: Optimized for conference room settings, which include multiple speakers with a single microphone.
* `phonecall`: Optimized for low-bandwidth audio phone calls.
* `voicemail`: Optimized for low-bandwidth audio clips with a single speaker. Derived from the phonecall model.
* `finance`: Optimized for multiple speakers with varying audio quality, such as might be found on a typical earnings call. Vocabulary is heavily finance oriented.
* `conversationalai`: Optimized for use cases in which a human is talking to an automated bot, such as IVR, a voice assistant, or an automated kiosk.
* `video`: Optimized for audio sourced from videos.
* `medical`: Optimized for audio with medical oriented vocabulary.
* `drivethru`: Optimized for audio sources from drivethrus.
* `automotive`: Optimized for audio with automative oriented vocabulary.
* `atc`: Optimized for audio from air traffic control.

### Nova

**Examples**

```text Text
https://api.deepgram.com/v1/listen?model=nova
```

```text Text
https://api.deepgram.com/v1/listen?model=nova-phonecall
```

Nova is the predecessor to Nova-2. Training on this model spans over 100 domains and 47 billion tokens, making it the deepest-trained automatic speech recognition (ASR) model to date. Nova doesn't just excel in one specific domain — it is ideal for a wide array of voice applications that require high accuracy in diverse contexts.

Nova has the following model options which can be called by using the following syntax: `model=nova-{option}`

* `general`: Optimized for everyday audio processing. Likely to be more accurate than any region-specific Base model for the language for which it is enabled. If you aren't sure which model to select, start here.

* `phonecall`: Optimized for low-bandwidth audio phone calls.

### Enhanced

**Examples**

```text Text
https://api.deepgram.com/v1/listen?model=enhanced
```

```text Text
https://api.deepgram.com/v1/listen?model=enhanced-phonecall
```

Enhanced models are still some of our most powerful speech-to-text models; they generally have higher accuracy and better word recognition than our base models, and they handle uncommon words significantly better.

Enhanced has the following model options which can be called by using the following syntax: `model=enhanced-{option}`

* `general`: Optimized for everyday audio processing. Likely to be more accurate than any region-specific Base model for the language for which it is enabled. If you aren't sure which model to select, start here.

* `meeting` *beta*: Optimized for conference room settings, which include multiple speakers with a single microphone.

* `phonecall`: Optimized for low-bandwidth audio phone calls.

* `finance` *beta*: Optimized for multiple speakers with varying audio quality, such as might be found on a typical earnings call. Vocabulary is heavily finance oriented.

The Enhanced models can be called with the following syntax:

### Base

**Examples**

```text Text
https://api.deepgram.com/v1/listen?model=base
```

```text Text
https://api.deepgram.com/v1/listen?model=base-phonecall
```

Base models are built on our signature end-to-end deep learning speech-to-text model architecture. They offer a solid combination of accuracy and cost effectiveness in some cases.

Base has the following model options which can be called by using the following syntax: `model=base-{option}`

* `general`: (Default) Optimized for everyday audio processing.
* `meeting`: Optimized for conference room settings, which include multiple speakers with a single microphone.
* `phonecall`: Optimized for low-bandwidth audio phone calls.
* `voicemail`: Optimized for low-bandwidth audio clips with a single speaker. Derived from the phonecall model.
* `finance`: Optimized for multiple speakers with varying audio quality, such as might be found on a typical earnings call. Vocabulary is heavily finance oriented.
* `conversationalai`: Optimized for use cases in which a human is talking to an automated bot, such as IVR, a voice assistant, or an automated kiosk.
* `video`: Optimized for audio sourced from videos.

### Custom

You may also use a custom, trained model associated with your account by including its `custom_id`.

Custom models are only available to Enterprise customers. See [Deepgram Pricing & Plans](https://deepgram.com/pricing/) for more details.

### Whisper

**Examples**

```text Text
https://api.deepgram.com/v1/listen?model=whisper
```

```text Text
https://api.deepgram.com/v1/listen?model=whisper-SIZE
```

Whisper models are less scalable than all other Deepgram models due to their inherent model architecture. All non-Whisper models will return results faster and scale to higher load.

Deepgram's Whisper Cloud is a fully managed API that gives you access to Deepgram's version of OpenAI’s Whisper model. Read our guide [Deepgram Whisper Cloud](/docs/deepgram-whisper-cloud) for a deeper dive into this offering.

Deepgram's Whisper models have the following size options:

* `tiny`: Contains 39 M parameters. The smallest model available.
* `base`: Contains 74 M parameters.
* `small`: Contains 244 M parameters.
* `medium`: Contains 769 M parameters. The default model if you don't specify a size.
* `large`: Contains 1550 M parameters. The largest model available. Defaults to OpenAI’s Whisper large-v2.

Additional rate limits apply to Whisper due to poor scalability. Requests to Whisper are limited to 15 concurrent requests with a paid plan and 5 concurrent requests with the pay-as-you-go plan. Long audio files are supported up to a maximum of 20 minutes of processing time (the maximum length of the audio depends on the size of the Whisper model).

## Try it out

To transcribe audio from a file on your computer using a particular model, run the following curl command in a terminal or your favorite API client.

```bash CURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?model=OPTION'
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](https://console.deepgram.com/signup?jump=keys).

---
