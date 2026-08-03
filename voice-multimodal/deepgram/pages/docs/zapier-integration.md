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

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/0cc416a9fcf9263e94aca8c02e6f0bdd5a409756962f812a5a5607bb2215ba85/images/c9a12a1-trigger_action.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260803%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260803T233206Z&X-Amz-Expires=604800&X-Amz-Signature=d41e67e7c1e824d74fbc4e47ea57d2e185b438cea2120daebefba95cc737ec14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/9ed364415a0b2d17c6ecb1603a688031912db19aefbeadddf74c500539187848/images/5a142f0-starter_zap.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260803%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260803T233206Z&X-Amz-Expires=604800&X-Amz-Signature=60af9d56c34d5171191b2fca10501603af9c6c33b46efad2d593c1957e638a97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Set up the Trigger

Click into the first box to change the trigger. A Zap must start with a trigger. The trigger starts off the workflow with an initial trigger event.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/e184ada453db58bf60f9557e0914a9df3324ca1c5cbea428ba8067c98f072079/images/20d4e85-change_trigger.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260803%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260803T233206Z&X-Amz-Expires=604800&X-Amz-Signature=e8b1057cc8874d19b6937b24f4650fb9fd865b8050fa525fd504d3c5beae874c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

The Deepgram integration cannot be used as a trigger event so you should choose a different integration to be the trigger.

Example triggers with Deepgram actions could be:

| Trigger                            | Action                                                                                                                                         |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| New Recording is Completed in Zoom | Deepgram transcribes the recording into a text transcript                                                                                      |
| New Recording in Twilio            | Deepgram summarizes the content of the message                                                                                                 |
| New Audio File in Dropbox          | Deepgram makes an API request and returns a JSON response including the transcription, diarization, or any other features available in the API |

Configure the trigger with your chosen integration (Amazon S3, Dropbox, etc.). Integrations may use OAuth to authenticate automatically, or you may have to enter an API key.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/905817d7b8e99221b25a40eb014c9b9320af10fd078bb38893466caee408e2a8/images/0397791-sign_in.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260803%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260803T233206Z&X-Amz-Expires=604800&X-Amz-Signature=dbc5ad6131b7cbd78143df8fdde4dc9992a7714a1e76dd121a6af3df1f6310c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Once your trigger has been set up, you can add actions.

### Configure a Deepgram Action

Click into the action box to configure it to use Deepgram.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/9cffae30754481e9be8a0144fd3c4b86edde9c712b0604d29704fe94ac787f8d/images/f8629d3-configure_deepgram.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260803%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260803T233206Z&X-Amz-Expires=604800&X-Amz-Signature=b2d523b3b0a2903b1a254062162e8297c6f4177d719b98b5474b24ea860c43ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Connect to your Deepgram account by adding your API key.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/4f8a0b7fc477b9f44b047b85918b9d702f4a6687603b4c621a369e432790d444/images/57500c0-add_api_key.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260803%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260803T233206Z&X-Amz-Expires=604800&X-Amz-Signature=97338af1c9dfbcd3c1e9a0af29b1e6f89ce12a35b3afd4203340bae71386f94b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

After successfully connecting your account, you will select your configuration options in the form. Be sure to add a publicly accessible URL as the audio file to transcribe.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/5576112e39dfa2007723b6c4664a0732aef297e9a4bca6abb961091aef3a9f3b/images/09d6f06-config_options.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260803%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260803T233206Z&X-Amz-Expires=604800&X-Amz-Signature=fe0d0fdfb762adcb8420a0771dd6ff6a66fd8356de18614e4b0b8cd70432da11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Deepgram's Zapier integration only accepts a publicly accessible URL audio file. If you need to convert raw audio to a URL, we recommend using the [Cloud Convert integration](https://www.make.com/en/integrations/cloudconvert) to convert the audio file to a URL.

You can test the workflow by clicking "Test Step". This will run the workflow, and then you should see a transcription response that looks similar to this:

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/ac7901fad97dfc4fb4a6aa2f8f305377e95dd9fce4e019bad6591a1405042db4/images/ded312a-test_step.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260803%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260803T233206Z&X-Amz-Expires=604800&X-Amz-Signature=f2f252b6ed1e249a0ed6471f7300be7e54fa5257b3cf88f6e31479c225a77051&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

If you add another action after your Deepgram action, you can use the transcript in that following action.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/8d3304dc3ace9e6086cea472f05cb41917b6211235d07d38e92d13cf6c0984d8/images/0b6faab-use_transcript.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260803%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260803T233206Z&X-Amz-Expires=604800&X-Amz-Signature=8f1bfcb0e51e316df6612585991f5df0b629327087de1d3782f4c445de8c0f67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Click "Publish" in the final step to publish your zap.

---

What’s Next

* [Deepgram API Overview](/reference/deepgram-api-overview)
