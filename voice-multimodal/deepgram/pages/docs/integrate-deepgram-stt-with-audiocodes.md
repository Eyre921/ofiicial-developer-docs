---
title: "AudioCodes (LiveHub) and Deepgram STT"
source: https://developers.deepgram.com/docs/integrate-deepgram-stt-with-audiocodes.md
path: docs/integrate-deepgram-stt-with-audiocodes
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# AudioCodes (LiveHub) and Deepgram STT

[AudioCodes VoiceAI Connect](https://voiceaiconnect.audiocodes.com/) is a powerful platform that enables the integration of telephony and contact center platforms with the cloud, thus facilitating the use of Deepgram in your customer journey.

It offers a simple user interface for standing up connections and developer-friendly APIs for advanced integrations.

Note, AudioCodes offers [two versions of this platform](https://techdocs.audiocodes.com/voice-ai-connect/#VAIG_Combined/editions_and_deployment.htm?TocPath=VoiceAI%2520Connect%257C_____1) - LiveHub, which is the self serve version, as well as VoiceAI Connect Enterprise, which is the managed services version.

This guide will focus on LiveHub, as it is accessible to all users. However, if you are using VoiceAI Connect Enterprise, the steps and instructions laid out here will be very similar. In addition, you will have the help of the AudioCodes Professional Services team to help you with the configuration. Refer to this doc for guidance, but note that the steps may vary slightly depending on how your specific version of VoiceAI Connect Enterprise is built.

## Before you Begin

Before you start, you'll need to follow the steps in the [Make Your First API Request](/docs/make-your-first-api-request) guide to obtain a Deepgram API key.

You will need an [AudioCodes LiveHub](https://livehub.audiocodes.io/login) account to connect the two services.

## Add Deepgram as a Speech Service in LiveHub

Follow the steps in the [LiveHub integration guide](https://techdocs.audiocodes.com/livehub/#VAIG_Combined/Creating%20a%20new%20speech%20service.htm?TocPath=Speech%2520service%2520integration%257C_____1) to create a new speech service.

If you want to use Deepgram's Speech-to-Text or Text-to-Speech services, you should choose the [Deepgram specific](https://techdocs.audiocodes.com/livehub/#VAIG_Combined/Creating%20a%20new%20speech%20service.htm#Deepgram) speech provider option.

You can also use the [Custom Integration](https://techdocs.audiocodes.com/livehub/#VAIG_Combined/Creating%20a%20new%20speech%20service.htm#Generic) option and insert the Deepgram API endpoint (example - `wss://api.deepgram.com/v1/listen`).

#### Using the Deepgram specific speech service

Selecting this option automaticaly routes your requests to the default Deepgram STT or TTS endpoints:

* Speech-to-Text [api.deepgram.com/v1/listen](https://developers.deepgram.com/reference/speech-to-text/listen-streaming)
* Text-to-Speech [api.deepgram.com/v1/speak](https://developers.deepgram.com/reference/text-to-speech/speak-streaming)

#### Using the Custom Integration option

Select this option if you wish to pass the Deepgram API endpoint explicitly, or for testing another alternate endpoint.

## Advanced Configuration JSON object

AudioCodes supports Advanced JSON configuration in the Bot Connection. This is how you can pass additional query parameters to Deepgram.

Follow [these instructions](https://techdocs.audiocodes.com/livehub/#LiveHub/Creating%20your%20Bot.htm?TocPath=Bot%2520connectivity%257CDefine%2520your%2520bot%2520connection%257C_____0) if you need to set up a Bot Connection for this first time.

To edit an existing Bot Connection, navigate to **Bot Connections** > **Edit** > **Advanced**

Please see the [AudioCodes documentation](https://techdocs.audiocodes.com/voice-ai-connect/#VAIG_Combined/parameters.htm) for the full list of supported key-value pairs in the Advanced JSON configuration.

Deepgram officially supports the following AudioCodes configuration parameters:

* [sttLanguage](https://techdocs.audiocodes.com/voice-ai-connect/Content/VAIG_Combined/speech-customization.htm#kanchor126) - use this to set the language code for STT. This is the ONLY way to change the language!
* [Other / Misc parameters](https://techdocs.audiocodes.com/voice-ai-connect/#VAIG_Combined/speech-customization.htm#Speech-to-text20detection20features20for20Deepgram) - the following parameters are suppoted by Deepgram. You can set any of these to your desired values. NOTE: requires VoiceAI Connect Enterprise (Version 3.22 and later).
* [sttGenericData](https://techdocs.audiocodes.com/voice-ai-connect/Content/VAIG_Combined/speech-customization.htm#kanchor142) - you can use this object to pass ANY parameter (except language) to Deepgram.

#### Using the sttGenericData object

If you wish to pass ANY supported parameter (other than language) to Deepgram, you can do so using the `sttGenericData` object. For example, [any of the parameters in our API documentation](https://developers.deepgram.com/reference/speech-to-text/listen-streaming#request.query) can be passed through the sttGenericDataobject.

For example, you might configure the sttGenericData object as such:

```JSON
{
  "sttGenericData": {
    "model": "nova-3", // we will default to 'phonecall-enhanced' if not specified here
    "smart_format": true, // str or bool supported
    "profanity_filter": "true" // str or bool supported
  }
}
```

The ONLY way to set the language for your STT service is to use the the `sttLanguage` field. If you try to pass a language code in `sttGenericParams` it will be ignored.

#### Using Keyterm or Keyword boosting

If you wish to use [Keyterms](https://developers.deepgram.com/docs/keyterm) (nova-3) or [Keywords](https://developers.deepgram.com/docs/keywords) (nova-2, nova-1, base, enhanced), you should pass a list through the `sttGenericData` object. See the example below.

[Keyword Intensifiers](https://developers.deepgram.com/docs/keywords#intensifiers) are supported. Simply pass the value immediately after the keyword, separated by a colon, as per our documentation.

```JSON
{
  "sttGenericData": {
    // "model": "nova-3" OR "nova-2"
    "keyterm": ["example", "another example"] // For nova-3
    "keywords": ["snuffleupagus:5"] // For nova-2, nova-1, base, or enhanced models
  }
}
```

### Accessing Deepgram AI Works flows

1. **Configure the Custom Integration Speech Service**
   * Set up a Custom Integration speech service pointing to the Deepgram AudioCodes integration endpoint
   * Use the endpoint: `wss://integrations.deepgram.com/audiocodes/stt`
   * Configure the `sttGenericData` object to pass your parameters

2. **Define and Pass the AI Works Object**
   * Define an `aiworks` object that routes requests to AI Works (instead of the default API endpoint)
   * Include the AI Works endpoint that Deepgram has provided to you
   * Pass any additional query parameters required for your integration

```JSON
{
  "sttGenericData": {
    "aiworks": {
      "repo": "wss://aiworks.deepgram.com/api/repos/<example-repo-id>/flows/<example-flow-id>/execute", // Insert your AI Works URL here!
      "stt_query_params": { // If using AI Works, you must set the STT query parameters here, NOT at the top level. 
        "model": "nova-3",
        "smart_format": true, // str or bool supported
        "mip_opt_out": "true" // str or bool supported
      }
    }
  }
}
```

If using AI Works, do not pass query parameters as "top level" key-value pairs, as these will be ignored if the `aiworks` object is present.

Instead, pass your query parameters in the `aiworks.stt_query_params` object.

Always consult the [AudioCodes API documentation](https://techdocs.audiocodes.com/voice-ai-connect/#VAIG_API/Speech-to-Text.htm?TocPath=AudioCodes%2520API%257C_____4) for the most up to date information.
