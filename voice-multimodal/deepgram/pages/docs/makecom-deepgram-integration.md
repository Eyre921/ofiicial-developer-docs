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

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/52523f19884451a64555a5549b2ea4ba5450a60b36b46d3a29f3ac6ba87a046b/images/cc983b5-scenario_example.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T233113Z&X-Amz-Expires=604800&X-Amz-Signature=8139f2b3311b71edd18066a9073fe96a2930771f031c53ea6a1daff80c035a3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

An example workflow could be the following:

Add an audio file to a folder in Dropbox (Trigger) -> Create a shareable URL Link of the file in Dropbox (Action) -> Transcribe the file with Deepgram (Action) -> Add a text file with the transcription to another folder in Dropbox (Action).

Currently, Deepgram offers these actions in Make:

1. Transcribe a Prerecorded Audio File From URL
2. Summarize an Audio File
3. Make an API Call

## How to Build a Workflow in Make

### Create a Scenario

To create a scenario, click on the “Scenarios” section in the left-side navigation bar and then click on “Create a Scenario”. You will be presented with an empty scenario.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/54fa4963b1ec71d073bac87f74a356b4cd42ea50c3ddbc5f76248685bb727b91/images/412813f-make_side_nav.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T233113Z&X-Amz-Expires=604800&X-Amz-Signature=0f1ded83ce71cc2c29dfd8432566abd7e5b1edb43d61f759754f38c6df094248&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Add a Trigger

Click on the plus sign to add a trigger. A scenario must start with a trigger. The trigger starts off the workflow with an initial trigger event.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/42003ffe913f68c15bbf6d4c07f35f1662f3ad63dd9b6f6a9c58308b8a770bc9/images/b86fd4b-new_scenario.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T233113Z&X-Amz-Expires=604800&X-Amz-Signature=bfd80530f395c680fc6b2e64b948c63146ca0f1a937d8ea81c69789ea6d3c9c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Possible triggers with Deepgram actions could be:

| Trigger                                               | Action                                                                            |
| ----------------------------------------------------- | --------------------------------------------------------------------------------- |
| A voicemail message is sent with Telegram or WhatsApp | Deepgram transcribes the audio message into text                                  |
| A new video is added to Vimeo                         | Deepgram summarizes the content of the video                                      |
| A meeting takes place in Zoom                         | Deepgram transcribes the meeting into a text transcript or summarizes the content |

Select your trigger. You will need to connect the integration you’ve chosen. Integrations may use OAuth to authenticate automatically, or you may have to enter an API key.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/fd3015f773a48da0e6b924b1c9ad36c9eb5ed82bd8ada4d2c292d34503f47796/images/acc839f-trigger_example.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T233113Z&X-Amz-Expires=604800&X-Amz-Signature=b22c2f5ac7e45e57d872e7a20cdf10fb97f76cbe130f4c73e80b5754775cb9ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Once your trigger has been set up, you can add actions.

### Add a Deepgram Action

To add a Deepgram action, click on the “Add another module” button. Type Deepgram and then select the appropriate action. This will bring up all the possible Deepgram actions

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/5c86dc127f98611f28999c75e411d77da1501837e536af979f407df9b0def757/images/4b0cbdc-deepgram_actions.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T233113Z&X-Amz-Expires=604800&X-Amz-Signature=829da6676cce38bfc0e11752e3dd4f477071ca09d9ec477cb2fdc08d93f94290&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Next you will be prompted to connect to Deepgram. Enter your API key to connect your account.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/9b6ba844bbee145cfd46ec528a91036e22f0e46f1ecc10e64e97ff67207d290d/images/5100ee2-connect_API.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T233113Z&X-Amz-Expires=604800&X-Amz-Signature=ff914e0778a11223a0df390adac87eedf7e0c8cadf16a9552e3259e31b2d0706&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

After successfully connecting your account, you will select your configuration options in the form. The only required input is the URL; you can leave the rest blank if you do not have a specific configuration in mind. Read more about each of the form options in our [API Reference](/reference/speech-to-text/listen-pre-recorded).

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/e559658a81c4fbc15a79f66d39b74114e828ee0b2fb3e706a41c68a676a7eab1/images/db5acf0-deepgram_action_form.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T233113Z&X-Amz-Expires=604800&X-Amz-Signature=7b353d0fcc228f7ec400821a18f3127cfcb9344e31a8c33cef5775085b04ab94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

For the time being, Deepgram’s Make integration only accepts a URL audio file. If you need to convert raw audio to a URL, we recommend using the [Cloud Convert integration](https://www.make.com/en/integrations/cloudconvert) to convert the audio file.

You can test the workflow by clicking “Run Once”. This will run the workflow one time so you can then check the outputs of each step. Click on the bubble above the Deepgram integration to see the output of the action. By clicking into the form outputs, you can find the transcription within the “Results” section.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/2b23d984469e5b68e4d03b436258c3255b127734fc8ede8d7f663bb6dc8d8171/images/6045d26-output.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T233113Z&X-Amz-Expires=604800&X-Amz-Signature=c93b52e940d3f27b33aed46edee2d1b5b473bfa8245341ca58a9025c34c89c8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

If you add another action after your Deepgram action, you can use the transcript in that following action.

![](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/https%3A//deepgram.docs.buildwithfern.com/069f037ea6feb02cd56d14ffdf9bf1a94e41cb042c4233dda53dc3998dd247af/images/731e9d3-transcript.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260727%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260727T233113Z&X-Amz-Expires=604800&X-Amz-Signature=e106f9909a034954f51934079cabe6a9371c77546c9e3b50793ecda9af91acc9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Choose `Results: Channels[]` to use the transcript output in this following action.

***

What’s Next

* [Deepgram API Overview](/reference/deepgram-api-overview)
