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

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/52523f19884451a64555a5549b2ea4ba5450a60b36b46d3a29f3ac6ba87a046b/images/cc983b5-scenario_example.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T113200Z&X-Amz-Expires=604800&X-Amz-Signature=b8c8e33ab5845f016f665559118d60aa0bbd3448cf2c95f41e88793b8f8b914f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

An example workflow could be the following:

Add an audio file to a folder in Dropbox (Trigger) -> Create a shareable URL Link of the file in Dropbox (Action) -> Transcribe the file with Deepgram (Action) -> Add a text file with the transcription to another folder in Dropbox (Action).

Currently, Deepgram offers these actions in Make:

1. Transcribe a Prerecorded Audio File From URL
2. Summarize an Audio File
3. Make an API Call

## How to Build a Workflow in Make

### Create a Scenario

To create a scenario, click on the “Scenarios” section in the left-side navigation bar and then click on “Create a Scenario”. You will be presented with an empty scenario.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/54fa4963b1ec71d073bac87f74a356b4cd42ea50c3ddbc5f76248685bb727b91/images/412813f-make_side_nav.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T113200Z&X-Amz-Expires=604800&X-Amz-Signature=f68bdc477fdcdbf7614540e8044baaf0878a0eb09207fc8d370a6f7d27b61a52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Add a Trigger

Click on the plus sign to add a trigger. A scenario must start with a trigger. The trigger starts off the workflow with an initial trigger event.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/42003ffe913f68c15bbf6d4c07f35f1662f3ad63dd9b6f6a9c58308b8a770bc9/images/b86fd4b-new_scenario.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T113200Z&X-Amz-Expires=604800&X-Amz-Signature=5f96aa9095448ee168d76c39f0b5d7ea1c200d3abc1d6075b5d7f6f4e72d67b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Possible triggers with Deepgram actions could be:

| Trigger                                               | Action                                                                            |
| ----------------------------------------------------- | --------------------------------------------------------------------------------- |
| A voicemail message is sent with Telegram or WhatsApp | Deepgram transcribes the audio message into text                                  |
| A new video is added to Vimeo                         | Deepgram summarizes the content of the video                                      |
| A meeting takes place in Zoom                         | Deepgram transcribes the meeting into a text transcript or summarizes the content |

Select your trigger. You will need to connect the integration you’ve chosen. Integrations may use OAuth to authenticate automatically, or you may have to enter an API key.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/fd3015f773a48da0e6b924b1c9ad36c9eb5ed82bd8ada4d2c292d34503f47796/images/acc839f-trigger_example.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T113200Z&X-Amz-Expires=604800&X-Amz-Signature=e7940a2d0bebfa85e6ee5de4dd30eed5526577928dde9b2515a9a5d17c3edbb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Once your trigger has been set up, you can add actions.

### Add a Deepgram Action

To add a Deepgram action, click on the “Add another module” button. Type Deepgram and then select the appropriate action. This will bring up all the possible Deepgram actions

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/5c86dc127f98611f28999c75e411d77da1501837e536af979f407df9b0def757/images/4b0cbdc-deepgram_actions.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T113200Z&X-Amz-Expires=604800&X-Amz-Signature=fb8738096b6843f0257b563b8186b7231e40421e382802e1cc144fc105a759fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Next you will be prompted to connect to Deepgram. Enter your API key to connect your account.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/9b6ba844bbee145cfd46ec528a91036e22f0e46f1ecc10e64e97ff67207d290d/images/5100ee2-connect_API.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T113200Z&X-Amz-Expires=604800&X-Amz-Signature=605ce6f51ff0a230cfcc59045a01147f39f3aae32d294aca1253b201f1dd6368&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

After successfully connecting your account, you will select your configuration options in the form. The only required input is the URL; you can leave the rest blank if you do not have a specific configuration in mind. Read more about each of the form options in our [API Reference](/reference/speech-to-text/listen-pre-recorded).

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/e559658a81c4fbc15a79f66d39b74114e828ee0b2fb3e706a41c68a676a7eab1/images/db5acf0-deepgram_action_form.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T113200Z&X-Amz-Expires=604800&X-Amz-Signature=7c69ee6922dc30f5272dc953938a6dbe21b1c6a724c465d73978a59232da4d61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

For the time being, Deepgram’s Make integration only accepts a URL audio file. If you need to convert raw audio to a URL, we recommend using the [Cloud Convert integration](https://www.make.com/en/integrations/cloudconvert) to convert the audio file.

You can test the workflow by clicking “Run Once”. This will run the workflow one time so you can then check the outputs of each step. Click on the bubble above the Deepgram integration to see the output of the action. By clicking into the form outputs, you can find the transcription within the “Results” section.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/2b23d984469e5b68e4d03b436258c3255b127734fc8ede8d7f663bb6dc8d8171/images/6045d26-output.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T113200Z&X-Amz-Expires=604800&X-Amz-Signature=d2b23a9e9c7b85007daf23c6716f6a330cb010ab0c79013a903807204d704d15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

If you add another action after your Deepgram action, you can use the transcript in that following action.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/069f037ea6feb02cd56d14ffdf9bf1a94e41cb042c4233dda53dc3998dd247af/images/731e9d3-transcript.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260808T113200Z&X-Amz-Expires=604800&X-Amz-Signature=b830993816949a11c09230c0796a923113ee839a3aa867e1bcb3f9d784174159&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Choose `Results: Channels[]` to use the transcript output in this following action.

---

What’s Next

* [Deepgram API Overview](/reference/deepgram-api-overview)
