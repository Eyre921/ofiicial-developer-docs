---
title: "Voice and personality"
source: https://elevenlabs.io/docs/reception-ai/receptionist/voice-and-personality.md
path: docs/reception-ai/receptionist/voice-and-personality
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Voice and personality

The **Personality** group on the Receptionists page controls how your receptionist sounds and speaks. Languages are set from the **Languages** tile at the top of the page, and free-text instructions from the **Additional instructions** card.

## Voice

Select the **Voice** card to open the voice picker. Click any voice to hear it, then select the one that fits. The change saves immediately.

The picker has search and filters for language, accent, gender, and age, and groups voices into **Current**, **Your favorites**, **Recommended**, and **More voices**. Star a voice to add it to your favorites.

When choosing a voice, consider:

* **Accent match**: a voice that matches your primary language and region sounds most natural.
* **Brand alignment**: preview several voices before choosing.
* **Language coverage**: if you serve multilingual callers, test the voice in each language.

### Create a custom voice

Select **Create voice** in the voice picker to clone a voice, such as your own or a team member's.

### Add samples

Upload or record audio samples. Reception.ai removes background noise by default.

### Preview and name the voice

Listen to the result, give the voice a name, and confirm you have consent to clone it.

### Verify the voice

Read a short prompt aloud to verify the voice. You can select **Skip for now** and verify later.

| Requirement   | Value                                                 |
| ------------- | ----------------------------------------------------- |
| Samples       | Up to 25, each at least 5 seconds                     |
| Total audio   | 10 seconds to 45 minutes. About 3 minutes works best. |
| Custom voices | Basic: 1, Plus: 3, Premium: 5                         |

Custom voices require a paid plan and are not available during the free trial. To free a slot, select the star on a custom voice and confirm **Delete voice**. Deletion is permanent.

## Tone

The **Tone** card sets the receptionist's personality. Choose any combination of **Professional**, **Concise**, **Friendly**, **Warm**, **Formal**, **Empathetic**, **Direct**, and **Upbeat**.

## Greeting

The **Greeting** card sets the first message your receptionist says when it picks up. Keep it short (under 15 words works best):

* "Hello, this is \[Business Name], how can I help you?"
* "Thanks for calling \[Business Name]. What can I do for you today?"

If you leave the greeting empty, the receptionist waits for the caller to speak first.

Turn on **Always finish the first message** to prevent callers from interrupting the greeting. The card then shows an **Uninterrupted** badge. This is useful for greetings that include a required disclosure.

## Languages

Select the **Languages** tile to set:

* **Default language**: the language the receptionist uses when it answers.
* **Additional languages**: languages it can switch to during a conversation.

Reception.ai supports over 70 languages. Language detection is always on. The receptionist switches when the caller speaks a full sentence in one of your additional languages or asks to switch. Short phrases such as "Hello?" do not trigger a switch. It never switches to a language you have not configured.

> **Note**
>
> Choose a voice that sounds natural in your default language. Voices optimized for English may
> sound less natural in French or German.

## Additional instructions

The **Additional instructions** card holds free-text guidance that applies to every conversation, up to 8,000 characters. Use it for:

* How to introduce the business
* What to prioritize, for example "always try to book an appointment before ending the call"
* Topics to avoid or redirect

Select **Generate with AI** to draft instructions from a short description of your business.

For specific, repeatable behavior, use [rules and procedures](/docs/reception-ai/receptionist/rules-and-procedures) instead. They are easier to maintain than one long block of text.
