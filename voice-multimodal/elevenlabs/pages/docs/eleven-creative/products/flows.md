---
title: "ElevenCreative Flows"
source: https://elevenlabs.io/docs/eleven-creative/products/flows.md
path: docs/eleven-creative/products/flows
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# ElevenCreative Flows

![Flows canvas overview](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/476f79826c3bb57f85d46b402ec330dbb8a992fafa9c0a18bc81b9418898fb34/assets/images/product-guides/flows/flows-hero.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T223609Z&X-Amz-Expires=604800&X-Amz-Signature=6d33bca82cb1b90bf89c7421cbd9235cfbd57d8a4b3a4442b0b9740ad69d6c80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Overview

ElevenCreative Flows provides a node-based visual workspace for orchestrating end-to-end creative pipelines. While [ElevenCreative Studio](/docs/eleven-creative/products/studio) uses a linear timeline for precise editing, ElevenCreative Flows allows you to map out production logic on an infinite canvas.

With ElevenCreative Flows, you can chain together over 50 [image and video models](/docs/overview/capabilities/image-video) alongside ElevenLabs' industry-leading [speech](/docs/overview/capabilities/text-to-speech), [music](/docs/overview/capabilities/music), and [sound effects](/docs/overview/capabilities/sound-effects) models. This modular approach enables you to iterate on specific pipeline steps without regenerating the entire project.

ElevenCreative Flows is currently in Alpha. Features are subject to change.

## Key capabilities

* **Visual pipeline builder**: Map complex multi-step workflows on an infinite canvas
* **50+ generative models**: Access image, video, speech, music, and sound effects models in one interface
* **Non-destructive iteration**: Modify individual nodes without regenerating downstream content
* **Modular composition**: Layer and combine outputs from different models
* **Template library**: Start from pre-configured pipelines for common use cases
* **Real-time collaboration**: Work simultaneously with team members on the same flow
* **ElevenCreative Studio integration**: Export finished flows directly to ElevenCreative Studio for timeline editing

## Real-time collaboration

Multiple team members can open the same flow, see each other's cursors, make edits simultaneously, run the pipeline together, and leave comments on nodes. Shared flows appear in each collaborator's flows list automatically.

**Live cursor presence:** See who's working where in the canvas in real time.

**Instant sync:** All edits propagate immediately to every collaborator.

**Shared execution:** Everyone sees pipeline outputs at the same time.

**Basic Seat access:** Reviewers and stakeholders can collaborate at a reduced access tier. Basic Seat members can open shared flows, watch pipelines run, review outputs, and leave comments without needing a full workspace seat.

**Public flows:** External viewers can follow along as anonymous participants on public flows.

## Guide

### Create a new flow

Select **+ New Flow** from the dashboard to open a blank canvas.

![Create a new flow](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/c55e68567471280f6d4e713b2f46a23b0479ef64e4a48144e3876e0330fb3532/assets/images/product-guides/flows/flows-new.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T223609Z&X-Amz-Expires=604800&X-Amz-Signature=5da3764f99a48ab60fea80b2cb902855e5d587e69b16c101692d97d8e781fc02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Add nodes

Right-click anywhere on the canvas or use the toolbar at the bottom to add a node. Nodes represent specific models or utility tools.

![Add nodes](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/3db741756fcf67e9969c2503dbae5bf00fc05103e1c22a2fe3334d962e0654b9/assets/images/product-guides/flows/flows-add-node.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T223609Z&X-Amz-Expires=604800&X-Amz-Signature=c8b9dbb547cf263dda2dbcbe5d13d358004900dc98b3c400c260a9e9c6a47a60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Connect your workflow

Click and drag from an output port of one node to the input port of another to chain them together. For example, connect a generated image to a video generation node.

![Connect workflow](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/ea59847d2a725e920b5a03ecee5cc003f51d7f701c10d2b83c90679a469df685/assets/images/product-guides/flows/flows-connect-workflow.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T223609Z&X-Amz-Expires=604800&X-Amz-Signature=d01903e9404a9c1e81a028126564619c9b21c076c46532b4b83585735c1198f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Execute and iterate

Click the **Run** button on individual nodes to generate content. Re-run a single node to test variations without affecting the rest of the chain.

![Generate and iterate](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/a5055f58da10a7c0ec9f79fb826ed9fd8f5f329e4d6169b58b47608bbdc362eb/assets/images/product-guides/flows/flows-run.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T223609Z&X-Amz-Expires=604800&X-Amz-Signature=d46e926f4f1ce94675987f82be9c105a010f0532e0e7c4f9d9a509c48e437aef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Export or move to ElevenCreative Studio

Once your flow is complete, export the final assets directly or send the project to [ElevenCreative Studio](/docs/eleven-creative/products/studio) for fine-tuned timeline editing.

## Starting options

ElevenCreative Flows is designed for both exploratory creation and structured production pipelines.

### Quick start

#### Start from scratch

#### Start from scratch

Begin with a blank canvas. This is ideal for building custom pipelines from the ground up or experimenting with complex multi-step generation chains.

#### Use a template

#### Use a template

Select from preset shortcuts at the center of the canvas to load pre-configured node structures:

* **Perfume Ad**: A template optimized for luxury product visuals and voiceovers
* **E-commerce Store**: Designed for creating rapid product demos and variations
* **Yacht Promo Shoot**: A multi-modal setup for high-end travel and lifestyle content
* **And more**: Additional templates are continuously being added

## Flows Agent

Flows Agent is a conversational AI co-editor built directly into ElevenCreative Flows. To begin working with the agent, enter a description of what you want to create in the agent chat box. You have the option to upload existing files or start from scratch. The agent may ask clarifying questions, then builds your flow by placing nodes directly onto the canvas. Continue the conversation to keep iterating on your flow by providing feedback and requesting changes.

![Flows Agent creating a new flow](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/ce96a9170d9367e98816346dffbf429eaec694bdffa0eb0134b56b5fee5976b8/assets/images/product-guides/flows/flows-agent-new.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T223609Z&X-Amz-Expires=604800&X-Amz-Signature=2a4da3c9b29e6119e02c3a859d8527482abf2caf9b5737f4e90b8c072c7e37d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Using the agent with existing flows

You can also work with Flows Agent on existing flows. Just enter a description of what you want to do in the agent chat box, and the agent will analyse your existing nodes and carry out your instructions.

![Flows Agent working with existing
flows](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/6e76725a28de83ec701d984fb9620e8fddd22cdbded7858d0f31edd2f0f8d9d8/assets/images/product-guides/flows/flows-agent-existing.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T223609Z&X-Amz-Expires=604800&X-Amz-Signature=1a1bbbf8510bcd234ae69f68fb84df1ff0aa0f76be5704bbf9f80e9ad0ad45e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Agent permissions

You can set permissions for the agent, with the following options:

* **Approve each**: you'll be prompted to review and confirm every action before it executes.
* **Auto-run**: all actions will automatically execute without requiring confirmation.
* **Auto under threshold**: you'll only be asked for confirmation when a single action's cost exceeds your specified threshold.

### Manual control

Flows Agent does not replace manual editing. You can take over at any point to make adjustments, then hand control back to the agent. Manual and agent-assisted editing work side by side throughout your workflow.

![Completed flow with agent
conversation](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/7a394d1cf4a62de6640bb7127063ddb92c733afc234123f9e46b3c7c99797240/assets/images/product-guides/flows/flows-agent-detail.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T223609Z&X-Amz-Expires=604800&X-Amz-Signature=3e01e6f58daffb3f8d1028da8745b0fa26e862d2abccfe612ec0ab283bd5c34e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Pricing

Flows Agent is available on all plans. Chat usage is billed based on the volume and type of tokens processed during your conversation — there is no fixed price per interaction. Speech, image, music, sound effects, and video generation are billed at the standard rates for those capabilities. Commercial usage rights are determined by your subscription plan, consistent with other ElevenLabs products. Standard subscription plans are charged in credits, while Enterprise plans may use fiat billing. [Contact our Enterprise Sales team](https://elevenlabs.io/enterprise) to learn more.

To upgrade your plan, visit your [Subscription page](https://elevenlabs.io/app/subscription).

## The node system

Nodes are the building blocks of a flow. Each node serves a specific purpose, from inputting text to generating high-fidelity video.

#### Generation nodes

#### Generation nodes

These nodes house the generative models that create your assets:

* **Text to Speech**: Generate narration using our latest models, including [v3](/docs/overview/models#eleven-v3)
* **Image Generation**: Choose from 50+ industry-leading models to create visuals
* **Video Generation**: Animate images or generate video clips directly from text
* **Music**: Add atmospheric soundtracks to your project
* **Sound Effects**: Add targeted sound effects to your project

See our [capabilities overview](/docs/overview/intro#capabilities) for detailed information on each model type.

#### Processing & utility nodes

#### Processing & utility nodes

Use these nodes to refine and combine your content:

* **Text**: Add text input to your flow for prompts and instructions
* **Upload Media**: Import your own images, videos, or audio files into the flow
* **Composition**: A centralized preview node where you can layer audio and video to view the final output
* **Lipsync Generation**: Chain a speech node with either a video or image node to create perfectly synced talking heads
* **Upscale**: Increase the resolution and quality of your generated visual assets

#### Contextual navigation

#### Contextual navigation

When you drag a connection from an output port, ElevenCreative Flows automatically suggests compatible next-step nodes to help you build your pipeline faster.

## Execution and iteration

Unlike linear editors, ElevenCreative Flows allows for non-destructive iteration.

![Flow execution](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/fee84dc60f09c24b1ce7b170935640aedf5f158c153fb8a5e1947cf4a1ec0ade/assets/images/product-guides/flows/flows-run-from-here.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T223609Z&X-Amz-Expires=604800&X-Amz-Signature=4e4838bdfd0331467dde116f820d07f1097e951d77c068e96cc55f57aaeb12d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Partial generation:** If you want to change the voiceover but keep the generated video, you only need to re-run the [Text to Speech](/docs/overview/capabilities/text-to-speech) node. Only the subsequent nodes in that specific path will need to be updated.

**Batch variations:** Because the structure is saved as a flow, you can quickly swap out a single prompt or character and re-execute the pipeline to generate dozens of creative variations for A/B testing or multi-language campaigns.

**Credit usage:** Generating content within a node costs credits just like our standalone tools. Re-running a node will trigger a new generation and a new credit charge.

## Export and final production

Once you are satisfied with the output of your flow, you have two primary options:

**Download assets:** Export individual files or the final composition from the result nodes.

**Export to ElevenCreative Studio:** Send your assets directly to [ElevenCreative Studio](/docs/eleven-creative/products/studio) if your project requires precise timeline-based adjustments, captions, or manual track layering.

Programmatic execution via API for mass creative production is planned for a future release.

## Creating a template

You can create a template from an existing flow, allowing you to reuse the same flow with different inputs each time. Templates can be kept for personal use or shared with others.

![Creating a template from a flow](https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/c42cf66b656de0e6764fa615b20986a40cee9f329416b2a80c50a76718c8f795/assets/images/product-guides/flows/flows-create-template.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T223609Z&X-Amz-Expires=604800&X-Amz-Signature=f2dc1847a5b571b5581db6d5b110ae481c9ffc5b0d1a27655ee36ae4338ba34d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### To create a template

### Select your input nodes

These are the values someone provides when they run the template. You can have multiple inputs of different types.

### Select your output nodes

You must select at least one. If you select more than one, all outputs will be bundled into a zip file for download.

### Run the template at least once

This is required before the template can be saved or shared.

### Sharing options

When saving your template, choose who can access it:

* **Just me**: the template can only be used by you.
* **Workspace**: the template can be used by anyone in your workspace.
* **Link only**: the template can be used by anyone with the link.
* **Explore**: the template will be submitted for review. Once approved, it will be visible to everyone in the [Templates](https://elevenlabs.io/app/templates) **Explore** tab.

For more information on using and managing templates, see the [Templates documentation](/docs/eleven-creative/products/templates).

## FAQ

<tbody>
  <tr>
    <td>
      #### What models are available in Flows?

      Flows supports over 50 image and video models alongside ElevenLabs' [Text to Speech](/docs/overview/capabilities/text-to-speech), [Music](/docs/overview/capabilities/music), and [Sound Effects](/docs/overview/capabilities/sound-effects) models.

      See the [Images & Video guide](/docs/eleven-creative/playground/image-video#models) for a complete list of supported models.
    </td>
  </tr>

  <tr>
    <td>
      #### How does Flows differ from Studio?

      [Studio](/docs/eleven-creative/products/studio) uses a linear timeline for precise frame-by-frame editing with tracks for video, audio, music, and captions.

      Flows uses a node-based canvas for building multi-step generative pipelines. Use Flows to orchestrate complex generation chains, then export to Studio for final editing.

      For more details, see the [Flows documentation](/docs/eleven-creative/products/flows).
    </td>
  </tr>

  <tr>
    <td>
      #### Can I save and reuse flows?

      Yes. In Flows, each flow is automatically saved as a project. You can reload a flow, modify prompts or settings, and re-execute to create variations without rebuilding the entire pipeline.

      You can also create a template from any flow, allowing you to reuse the same flow structure with different inputs each time. See [Creating a template](/docs/eleven-creative/products/flows#creating-a-template) and the [Templates documentation](/docs/eleven-creative/products/templates) for more details.
    </td>
  </tr>

  <tr>
    <td>
      #### Do I need to regenerate everything if I change one step?

      No. Flows supports non-destructive iteration. You can re-run a single node, and only downstream nodes connected to that path will need to be updated. Unconnected branches remain unchanged.
    </td>
  </tr>

  <tr>
    <td>
      #### How are credits charged in Flows?

      In Flows, each node generation costs credits based on the model and settings used, identical to standalone tool pricing. Re-running a node triggers a new generation and a new credit charge.

      The number of credits you will be charged is displayed when you hover over the **Run** button.
    </td>
  </tr>

  <tr>
    <td>
      #### Can I export flows to other formats?

      In Flows, you can export individual assets or the final composition as downloadable files.

      To continue working with your outputs in [Studio](/docs/eleven-creative/products/studio), save them to your Files library and import them from there.
    </td>
  </tr>

  <tr>
    <td>
      #### Is there an API for Flows?

      Programmatic execution of Flows via API is planned for a future release. This will enable mass creative production use cases, such as connecting a CMS to a flow for automated content generation.
    </td>
  </tr>

  <tr>
    <td>
      #### What happens if a node fails in Flows?

      If a node fails during execution in Flows, only that node is affected and you are not charged for that execution. You can re-run the failed node without affecting other branches of your flow.
    </td>
  </tr>

  <tr>
    <td>
      #### Can multiple people edit the same flow at the same time?

      Yes. When a flow is shared with your workspace in Flows, any team member can open it and start working. Changes sync instantly. You can see who else is in the flow and work on different parts of the pipeline simultaneously.
    </td>
  </tr>

  <tr>
    <td>
      #### How do I share a flow with my team?

      In Flows, share a flow with anyone in your workspace. Shared flows appear in each collaborator's flows list automatically — no separate link required.
    </td>
  </tr>

  <tr>
    <td>
      #### Can Basic Seat members collaborate in Flows?

      Yes. [Basic Seat](/docs/help-center/account/workspaces/what-are-basic-seats) members can open shared flows, watch pipelines run, review outputs, and leave comments. They do not need a full workspace seat.
    </td>
  </tr>

  <tr>
    <td>
      #### Can people outside my workspace see my flow?

      Yes, if you make the flow public.

      When a flow is public in Flows, people outside your workspace can view it and follow along. They appear as anonymous participants.

      If the flow is not public, only members of your workspace who have access can see it. See [How do I share a flow with my team?](/docs/help-center/product/flows-image-video/flows/how-do-i-share-a-flow-with-my-team).
    </td>
  </tr>

  <tr>
    <td>
      #### Does real-time collaboration cost additional credits in Flows?

      No. Collaboration itself does not consume credits in Flows. Credits are consumed when nodes are executed, as normal.
    </td>
  </tr>
</tbody>
