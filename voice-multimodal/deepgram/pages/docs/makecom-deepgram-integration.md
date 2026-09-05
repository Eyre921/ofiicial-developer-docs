---
title: "Make.com and Deepgram"
source: https://developers.deepgram.com/docs/makecom-deepgram-integration.md
path: docs/makecom-deepgram-integration
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Make.com and Deepgram

[Make](https://www.make.com/en) is a visual platform for automating tasks, workflows, and apps without the need for coding.

## Introduction to Make

Make workflows are called scenarios. Scenarios are automated tasks that start with a trigger (an event which sets off the workflow), and then continue on with actions, the other steps of the workflow.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/52523f19884451a64555a5549b2ea4ba5450a60b36b46d3a29f3ac6ba87a046b/images/cc983b5-scenario_example.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260905T113127Z&X-Amz-Expires=604800&X-Amz-Signature=59ae3d21dadb2e0866c726b673e7f8532e1bff2fd17c5ca709414363ff1ce914&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

An example workflow could be the following:

Add an audio file to a folder in Dropbox (Trigger) -> Create a shareable URL Link of the file in Dropbox (Action) -> Transcribe the file with Deepgram (Action) -> Add a text file with the transcription to another folder in Dropbox (Action).

Currently, Deepgram offers these actions in Make:

1. Transcribe a Prerecorded Audio File From URL
2. Summarize an Audio File
3. Make an API Call

## How to Build a Workflow in Make

### Create a Scenario

To create a scenario, click on the “Scenarios” section in the left-side navigation bar and then click on “Create a Scenario”. You will be presented with an empty scenario.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/54fa4963b1ec71d073bac87f74a356b4cd42ea50c3ddbc5f76248685bb727b91/images/412813f-make_side_nav.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260905T113127Z&X-Amz-Expires=604800&X-Amz-Signature=046170e697f33dc4cf15c9a3eaa1d384783e858c422ec1bb8c3f5727e2f106d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Add a Trigger

Click on the plus sign to add a trigger. A scenario must start with a trigger. The trigger starts off the workflow with an initial trigger event.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/42003ffe913f68c15bbf6d4c07f35f1662f3ad63dd9b6f6a9c58308b8a770bc9/images/b86fd4b-new_scenario.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260905T113127Z&X-Amz-Expires=604800&X-Amz-Signature=5238f57a742fb3579c2c00409e0df3858756b450e7b236cf871b368fb49d262b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Possible triggers with Deepgram actions could be:

| Trigger                                               | Action                                                                            |
| ----------------------------------------------------- | --------------------------------------------------------------------------------- |
| A voicemail message is sent with Telegram or WhatsApp | Deepgram transcribes the audio message into text                                  |
| A new video is added to Vimeo                         | Deepgram summarizes the content of the video                                      |
| A meeting takes place in Zoom                         | Deepgram transcribes the meeting into a text transcript or summarizes the content |

Select your trigger. You will need to connect the integration you’ve chosen. Integrations may use OAuth to authenticate automatically, or you may have to enter an API key.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/fd3015f773a48da0e6b924b1c9ad36c9eb5ed82bd8ada4d2c292d34503f47796/images/acc839f-trigger_example.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260905T113127Z&X-Amz-Expires=604800&X-Amz-Signature=89f0a37d0d719f397c4b7be9805028d11bf254bf3b4f34d74b17dbbc7e295b4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Once your trigger has been set up, you can add actions.

### Add a Deepgram Action

To add a Deepgram action, click on the “Add another module” button. Type Deepgram and then select the appropriate action. This will bring up all the possible Deepgram actions

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/5c86dc127f98611f28999c75e411d77da1501837e536af979f407df9b0def757/images/4b0cbdc-deepgram_actions.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260905T113127Z&X-Amz-Expires=604800&X-Amz-Signature=5fc7325b20de99125686d7ee72b82209c06313d155eeffc99760e2aa6d2d794c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Next you will be prompted to connect to Deepgram. Enter your API key to connect your account.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/9b6ba844bbee145cfd46ec528a91036e22f0e46f1ecc10e64e97ff67207d290d/images/5100ee2-connect_API.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260905T113127Z&X-Amz-Expires=604800&X-Amz-Signature=85c80ee951ab2fdbb269ac71f825f63336b97de27e125635034d33187175f5e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

After successfully connecting your account, you will select your configuration options in the form. The only required input is the URL; you can leave the rest blank if you do not have a specific configuration in mind. Read more about each of the form options in our [API Reference](/reference/speech-to-text/listen-pre-recorded).

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/e559658a81c4fbc15a79f66d39b74114e828ee0b2fb3e706a41c68a676a7eab1/images/db5acf0-deepgram_action_form.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260905T113127Z&X-Amz-Expires=604800&X-Amz-Signature=f7d9e7085a96e0e25a70489f57b7bdd73ce454c9660796618bd6b4c8c3bf3f82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

For the time being, Deepgram’s Make integration only accepts a URL audio file. If you need to convert raw audio to a URL, we recommend using the [Cloud Convert integration](https://www.make.com/en/integrations/cloudconvert) to convert the audio file.

You can test the workflow by clicking “Run Once”. This will run the workflow one time so you can then check the outputs of each step. Click on the bubble above the Deepgram integration to see the output of the action. By clicking into the form outputs, you can find the transcription within the “Results” section.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/2b23d984469e5b68e4d03b436258c3255b127734fc8ede8d7f663bb6dc8d8171/images/6045d26-output.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260905T113127Z&X-Amz-Expires=604800&X-Amz-Signature=b21af377d8554c2921cc6d1b03f13a77fe36a497bba94c665404a4e74725bcc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

If you add another action after your Deepgram action, you can use the transcript in that following action.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/069f037ea6feb02cd56d14ffdf9bf1a94e41cb042c4233dda53dc3998dd247af/images/731e9d3-transcript.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260905%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260905T113127Z&X-Amz-Expires=604800&X-Amz-Signature=96d9685092bec17d05da10f98b8168328043986f475010853f19af805cdde8cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Choose `Results: Channels[]` to use the transcript output in this following action.

---

What’s Next

* [Deepgram API Overview](/reference/deepgram-api-overview)
