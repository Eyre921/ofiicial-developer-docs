---
title: "Zapier and Deepgram"
source: https://developers.deepgram.com/docs/zapier-integration.md
path: docs/zapier-integration
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Zapier and Deepgram

[Zapier](https://zapier.com/) is an online automation tool that allows you to connect your favorite apps, such as Amazon S3, Zoom, Deepgram, and more. It enables you to automate tasks between them, without having to write any code.

## Introduction to Zapier

Zapier workflows are called "Zaps." A Zap is a connection between two apps made up of a trigger and one or more actions.

Here's how it works:

1. Trigger: An event in one app that starts the Zap. For example, receiving a new voicemail, recording a new meeting in a video conference software program, or uploading a video of a lecture.
2. Action: An event that completes the Zap. It's the result or output you want to achieve, such as transcribing a new voicemail to text, converting a recorded meeting to written notes, or generating a summary text document from a spoken lecture.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/0cc416a9fcf9263e94aca8c02e6f0bdd5a409756962f812a5a5607bb2215ba85/images/c9a12a1-trigger_action.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260819T113153Z&X-Amz-Expires=604800&X-Amz-Signature=6835bd533ddd6f2b431e7aeb044c1fbceb3cea22237aff8b2009d1c795a15c89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

An example Zap could be the following:

Add an audio file to a folder in Dropbox (Trigger) -> Transcribe the file with Deepgram (Action) -> Add a text file with the transcription to another folder in Dropbox (Action).

Currently, Deepgram offers these actions in Zapier:

1. Create Transcription (Plain Text)
2. Create Summary
3. Create Deepgram API Request (Speech-To-Text)
4. Create Transcription (Callback)

To use the Create Transcription (Callback) integration, you will need to deploy a server to handle the callback response. This approach is best if you want to automate the transcription of files larger than approximately 200MB. You can find a step-by-step tutorial explaining how to do this in the [Deepgram Blog](https://deepgram.com/learn/no-more-zapier-timeouts-transcribe-large-audio-files-with-deepgram-and-zapier-s-w).

## How to Build a Workflow in Zapier

### Create a Zap

To create a Zap, click on the “Create Zap” button in the left-side navigation bar. This will create a starter zap with a trigger and an action.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/9ed364415a0b2d17c6ecb1603a688031912db19aefbeadddf74c500539187848/images/5a142f0-starter_zap.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260819T113153Z&X-Amz-Expires=604800&X-Amz-Signature=5cc8581212d9f54b4cfbabce947c269ea33e46b4ad77f9d511343792426ee664&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Set up the Trigger

Click into the first box to change the trigger. A Zap must start with a trigger. The trigger starts off the workflow with an initial trigger event.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/e184ada453db58bf60f9557e0914a9df3324ca1c5cbea428ba8067c98f072079/images/20d4e85-change_trigger.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260819T113153Z&X-Amz-Expires=604800&X-Amz-Signature=ae8617bf89419a8bab405ef160c834b019e5f1fde8e478e404398f928a75105d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

The Deepgram integration cannot be used as a trigger event so you should choose a different integration to be the trigger.

Example triggers with Deepgram actions could be:

| Trigger                            | Action                                                                                                                                         |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| New Recording is Completed in Zoom | Deepgram transcribes the recording into a text transcript                                                                                      |
| New Recording in Twilio            | Deepgram summarizes the content of the message                                                                                                 |
| New Audio File in Dropbox          | Deepgram makes an API request and returns a JSON response including the transcription, diarization, or any other features available in the API |

Configure the trigger with your chosen integration (Amazon S3, Dropbox, etc.). Integrations may use OAuth to authenticate automatically, or you may have to enter an API key.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/905817d7b8e99221b25a40eb014c9b9320af10fd078bb38893466caee408e2a8/images/0397791-sign_in.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260819T113153Z&X-Amz-Expires=604800&X-Amz-Signature=e3d0632102513b020c2acdfe3535ef749d09186f684627b51e90b048dfed0015&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Once your trigger has been set up, you can add actions.

### Configure a Deepgram Action

Click into the action box to configure it to use Deepgram.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/9cffae30754481e9be8a0144fd3c4b86edde9c712b0604d29704fe94ac787f8d/images/f8629d3-configure_deepgram.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260819T113153Z&X-Amz-Expires=604800&X-Amz-Signature=49e2cfe4e93212231946484782a2ee33fdcd4e945c64b2148bf4f6e745071cf9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Connect to your Deepgram account by adding your API key.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/4f8a0b7fc477b9f44b047b85918b9d702f4a6687603b4c621a369e432790d444/images/57500c0-add_api_key.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260819T113153Z&X-Amz-Expires=604800&X-Amz-Signature=c65da631f62028ea9e1be52754c106aa6d5332fad773feaf9f45921ef61ee3cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

After successfully connecting your account, you will select your configuration options in the form. Be sure to add a publicly accessible URL as the audio file to transcribe.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/5576112e39dfa2007723b6c4664a0732aef297e9a4bca6abb961091aef3a9f3b/images/09d6f06-config_options.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260819T113153Z&X-Amz-Expires=604800&X-Amz-Signature=18d94bf05ea4ffaa00f7e63b8b4a4666ffca847f88ae10c6817d64f352534bbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Deepgram's Zapier integration only accepts a publicly accessible URL audio file. If you need to convert raw audio to a URL, we recommend using the [Cloud Convert integration](https://zapier.com/apps/cloudconvert/integrations) to convert the audio file to a URL.

You can test the workflow by clicking "Test Step". This will run the workflow, and then you should see a transcription response that looks similar to this:

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/ac7901fad97dfc4fb4a6aa2f8f305377e95dd9fce4e019bad6591a1405042db4/images/ded312a-test_step.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260819T113153Z&X-Amz-Expires=604800&X-Amz-Signature=a16c5f660575fec8470c3fa9cd8fe833d30c83bca23f19192fdee974b60b9570&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

If you add another action after your Deepgram action, you can use the transcript in that following action.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/8d3304dc3ace9e6086cea472f05cb41917b6211235d07d38e92d13cf6c0984d8/images/0b6faab-use_transcript.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260819%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260819T113153Z&X-Amz-Expires=604800&X-Amz-Signature=cccea36fccf0d2840e369b5c35319b38079a7f505ab4f84c519a0690157f74a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Click "Publish" in the final step to publish your zap.

---

What’s Next

* [Deepgram API Overview](/reference/deepgram-api-overview)
