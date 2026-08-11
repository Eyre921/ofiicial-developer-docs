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

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/52523f19884451a64555a5549b2ea4ba5450a60b36b46d3a29f3ac6ba87a046b/images/cc983b5-scenario_example.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260811%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260811T113147Z&X-Amz-Expires=604800&X-Amz-Signature=d30406fed5fa3aba2d46db1111069dc5f85bec281d199694d512187fd84ce4fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

An example workflow could be the following:

Add an audio file to a folder in Dropbox (Trigger) -> Create a shareable URL Link of the file in Dropbox (Action) -> Transcribe the file with Deepgram (Action) -> Add a text file with the transcription to another folder in Dropbox (Action).

Currently, Deepgram offers these actions in Make:

1. Transcribe a Prerecorded Audio File From URL
2. Summarize an Audio File
3. Make an API Call

## How to Build a Workflow in Make

### Create a Scenario

To create a scenario, click on the “Scenarios” section in the left-side navigation bar and then click on “Create a Scenario”. You will be presented with an empty scenario.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/54fa4963b1ec71d073bac87f74a356b4cd42ea50c3ddbc5f76248685bb727b91/images/412813f-make_side_nav.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260811%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260811T113147Z&X-Amz-Expires=604800&X-Amz-Signature=14992e054463bee41129a07cfc819109a6607c7ba5f3d1c53d12be18dcb980a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Add a Trigger

Click on the plus sign to add a trigger. A scenario must start with a trigger. The trigger starts off the workflow with an initial trigger event.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/42003ffe913f68c15bbf6d4c07f35f1662f3ad63dd9b6f6a9c58308b8a770bc9/images/b86fd4b-new_scenario.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260811%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260811T113147Z&X-Amz-Expires=604800&X-Amz-Signature=7741bc2641de14868020c0042cee9d3583d2620d7fbe1e19eaa76c9c20b2a7b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Possible triggers with Deepgram actions could be:

| Trigger                                               | Action                                                                            |
| ----------------------------------------------------- | --------------------------------------------------------------------------------- |
| A voicemail message is sent with Telegram or WhatsApp | Deepgram transcribes the audio message into text                                  |
| A new video is added to Vimeo                         | Deepgram summarizes the content of the video                                      |
| A meeting takes place in Zoom                         | Deepgram transcribes the meeting into a text transcript or summarizes the content |

Select your trigger. You will need to connect the integration you’ve chosen. Integrations may use OAuth to authenticate automatically, or you may have to enter an API key.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/fd3015f773a48da0e6b924b1c9ad36c9eb5ed82bd8ada4d2c292d34503f47796/images/acc839f-trigger_example.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260811%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260811T113147Z&X-Amz-Expires=604800&X-Amz-Signature=85bfbd1f009ca83fb2ccffba7ea78daa7a86d99a66e9fc47a8d175e1ad084b3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Once your trigger has been set up, you can add actions.

### Add a Deepgram Action

To add a Deepgram action, click on the “Add another module” button. Type Deepgram and then select the appropriate action. This will bring up all the possible Deepgram actions

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/5c86dc127f98611f28999c75e411d77da1501837e536af979f407df9b0def757/images/4b0cbdc-deepgram_actions.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260811%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260811T113147Z&X-Amz-Expires=604800&X-Amz-Signature=866cb0d2b709355bb3a7946ffdc7f967a6c0a54d133928ad10eda6bc229f3bc9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Next you will be prompted to connect to Deepgram. Enter your API key to connect your account.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/9b6ba844bbee145cfd46ec528a91036e22f0e46f1ecc10e64e97ff67207d290d/images/5100ee2-connect_API.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260811%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260811T113147Z&X-Amz-Expires=604800&X-Amz-Signature=16c6bc4a0c7a5c17cf4ff9483da2e8d913fb48eb234e7850982fa865acf0931c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

After successfully connecting your account, you will select your configuration options in the form. The only required input is the URL; you can leave the rest blank if you do not have a specific configuration in mind. Read more about each of the form options in our [API Reference](/reference/speech-to-text/listen-pre-recorded).

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/e559658a81c4fbc15a79f66d39b74114e828ee0b2fb3e706a41c68a676a7eab1/images/db5acf0-deepgram_action_form.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260811%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260811T113147Z&X-Amz-Expires=604800&X-Amz-Signature=9495bdbe732c80eac11dd8a693a8d4800f83c56a0ef91218c7fc261b30c755f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

For the time being, Deepgram’s Make integration only accepts a URL audio file. If you need to convert raw audio to a URL, we recommend using the [Cloud Convert integration](https://www.make.com/en/integrations/cloudconvert) to convert the audio file.

You can test the workflow by clicking “Run Once”. This will run the workflow one time so you can then check the outputs of each step. Click on the bubble above the Deepgram integration to see the output of the action. By clicking into the form outputs, you can find the transcription within the “Results” section.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/2b23d984469e5b68e4d03b436258c3255b127734fc8ede8d7f663bb6dc8d8171/images/6045d26-output.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260811%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260811T113147Z&X-Amz-Expires=604800&X-Amz-Signature=dfd85ae2ad72031be351ec288c1d8743b9b753de63444680cb831a69311e8074&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

If you add another action after your Deepgram action, you can use the transcript in that following action.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/deepgram.docs.buildwithfern.com/069f037ea6feb02cd56d14ffdf9bf1a94e41cb042c4233dda53dc3998dd247af/images/731e9d3-transcript.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260811%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260811T113147Z&X-Amz-Expires=604800&X-Amz-Signature=fb89a1445f6fcf780b646049485f1482fea1e82e96f757dc757a8df730f9d11a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Choose `Results: Channels[]` to use the transcript output in this following action.

---

What’s Next

* [Deepgram API Overview](/reference/deepgram-api-overview)
