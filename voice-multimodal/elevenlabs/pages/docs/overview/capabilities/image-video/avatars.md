---
title: "Avatars"
source: https://elevenlabs.io/docs/overview/capabilities/image-video/avatars.md
path: docs/overview/capabilities/image-video/avatars
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Avatars

## Overview

Avatars are persistent visual identities that combine a person, character, or animal with any ElevenLabs voice to generate talking-head videos with synchronized lip movement. Create reusable identities once and pair them with any voice or script to produce consistent video content at scale.

Avatars are available on all paid plans.

Some Avatar models and reference image upload capabilities are restricted in the United States due
to regulatory or provider requirements.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/680e5acbe14121b643cd4f9cb59213707fff145ee66551a2950d3b3523c1b3fa/assets/images/product-guides/images-videos/avatars-overview.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260810%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260810T103257Z&X-Amz-Expires=604800&X-Amz-Signature=ceb8570dda81725c96043aa50e798aafda67823dfdf523752653024daadc572c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Avatar overview" />

## Key capabilities

* **Persistent identities**: Create avatars once and reuse them across unlimited videos
* **Voice flexibility**: Pair any avatar with any voice from your library, including cloned voices
* **Style variations**: Generate multiple styles from a single avatar with different angles, outfits, backgrounds, or lighting
* **Integrated text to speech**: Convert text directly to speech within the avatar interface
* **Flows integration**: Automate avatar video generation at scale using the Avatar node
* **Multiple lip-sync models**: Platform automatically selects the optimal model based on input format and quality requirements

## Creating an avatar

Generate a new avatar from reference images, or a text prompt:

### Navigate to Avatar creation

Go to [Image & Video](https://elevenlabs.io/app/image-video), and in the Avatar section, click **New**.

### Upload reference images or describe your avatar

Upload multiple reference images of the same person or character from different angles. Higher quality reference images with varied perspectives produce better results.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/37d9adbc0f8666e91408180793f2692f51955cfd1b54773cf7c2d38cbec4cb86/assets/images/product-guides/images-videos/avatars-create.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260810%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260810T103257Z&X-Amz-Expires=604800&X-Amz-Signature=723addbebb8f3a76dd339c586e4d7cb1000c0400ba371697b22b3abb0c912dc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Avatar creation interface" />

Upload 3-5 images from different angles for optimal avatar quality.

Alternatively, you can describe your avatar using a text prompt.

### Configure and create

Name your avatar and optionally set a default voice. Click **Create Avatar** to generate the base identity.

Once created, the avatar appears in your library and can be used across projects.

## Styles

Styles are variations of an existing avatar that represent different visual contexts:

* Camera angles and framing
* Outfits and accessories
* Backgrounds and environments
* Lighting conditions

### Creating a style

To create a style for an existing avatar, click **View Avatar**, then click "New Style".

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/98a871e4e3cd60f5bf77ead03246953edfd6a33db778a2e9ef1b36ea8a16923a/assets/images/product-guides/images-videos/avatars-option.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260810%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260810T103257Z&X-Amz-Expires=604800&X-Amz-Signature=6ad2cb205f09214c89c8f334bf6dd5ab23c56c069d7142cc54c84c0b28fdf701&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Style creation options in Avatar interface" />

You can create styles in two ways:

**Prompt it**: Describe the new style using a text prompt.

**Upload**: Upload a reference image to guide the new style while maintaining the core identity.

Styles allow you to maintain brand consistency across different contexts without regenerating the entire avatar.

## Generating videos

Generate talking-head videos by pairing any avatar with a voice and script:

### Select an avatar

Choose an avatar from your library, and select **Create Lip Sync**. Choose the style you want to use.

### Choose a voice

If you set a default voice for your avatar, this will be pre-selected. You can also use any voice from your library, including community voices, cloned voices, or designed voices.

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/d220cca9e55e10964a8611d41f45a0d52e0a54d5071a36a44fcbc5368dfdfc9d/assets/images/product-guides/images-videos/avatars-speech.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260810%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260810T103257Z&X-Amz-Expires=604800&X-Amz-Signature=87e5c2bd8537ce1fccb8bc98d3e2b790a30c43c6a3402b73bfdd0caf9def6ed6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Voice selection and text to speech interface" />

### Add your script

Enter the text you want the avatar to speak, then click **Generate speech.** You can listen to the generated speech before moving onto the next step, and regenerate if needed.

You also have the option of selecting a previous Text to Speech generation from your History.

Once you're happy with your selection, click **Use Speech.**

### Generate

In the next step, you can add an optional prompt to guide the visuals of the lip sync. The platform selects the optimal lip sync model based on your input and quality requirements, but you can also change the model before generating the video. When you're ready, click **Generate** to create your lip sync.

## Flows integration

The Avatar node in [Flows](/docs/eleven-creative/products/flows) enables automated avatar video generation at scale.

Use cases include:

* Personalized video campaigns with dynamic scripts
* Batch video generation with consistent branding
* Automated content pipelines with voice and visual swapping

<img src="https://fdr-prod-docs-files-public.s3.us-east-1.amazonaws.com/elevenlabs.docs.buildwithfern.com/e4cbf4ea8930fdf33e8ae67baab57a2f2e172a300b9d3c1441632ec53ac20407/assets/images/product-guides/images-videos/avatars-flows.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIA6KXJSKKNFOCF7G4B%2F20260810%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260810T103257Z&X-Amz-Expires=604800&X-Amz-Signature=6c4a127cd78347fd3c9ad07de2e23cdbeaf2291727f3bff6cd2b47c8ae82bbea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject" alt="Avatar node in the Flows interface" />

Learn more about [Flows](/docs/eleven-creative/products/flows).

## Credit costs

Avatar generation follows the existing [Image & Video pricing structure](https://elevenlabs.io/pricing). Costs vary by:

* Selected lip-sync model
* Output resolution
* Video duration

Credit usage is deducted per generation. Check your usage in [your usage analytics](https://elevenlabs.io/app/usage).

## Key facts

* **Availability**: All paid plans
* **Lip-sync models**: Platform automatically selects optimal model
* **Voice compatibility**: Works with all ElevenLabs voices, including cloned voices
* **Reusability**: Avatars and styles persist across unlimited generations
* **Flows support**: Available as an Avatar node for automation
* **API access**: Not available at launch; planned for future release
