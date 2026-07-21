---
title: "What does the status of my Professional Voice Clone mean?"
source: https://elevenlabs.io/docs/help-center/product/voice-customization/voice-cloning/what-does-the-status-of-my-professional-voice-clone-mean.md
path: docs/help-center/product/voice-customization/voice-cloning/what-does-the-status-of-my-professional-voice-clone-mean
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# What does the status of my Professional Voice Clone mean?

Your Professional Voice Clone will go through a few different stages while it is processing. These stages are reflected in the status shown for your Professional Voice Clone in [My Voices](https://elevenlabs.io/app/voice-lab).

To view the current status, find your voice in the list and look at the icons displayed to the right.

 

<strong>Draft:</strong> This status means that your voice is incomplete. Generally this is either
because you haven't completed creating the voice, or you haven't verified the voice yet.

<img src="https://help.elevenlabs.io/hc/article_attachments/35965215258641" alt="" />

To go through the verification process, click the tick icon.

<img src="https://help.elevenlabs.io/hc/article_attachments/35965215262097" alt="" />

To go back to the voice creation process, click <strong>More actions</strong> (three dots) and select <strong>Edit voice</strong>.

 

Once you've verified your voice, it will need to fine-tune on our models before you can use it. You can track this process by hovering over the name of your voice in [My Voices](https://elevenlabs.io/app/voice-lab). You'll see all available models listed here, with an icon to indicate the status for each model. 

<img src="https://help.elevenlabs.io/hc/article_attachments/35965182407569" alt="" />

 

Hover over the name of the model for more information, and you will see one of the following:

<strong>The training run has been scheduled</strong>: This means that your voice is waiting for a
slot to open up so it can be trained. The length of time that your voice will be queued will depend
on how many other voices are also in the queue.

<strong>Creating dataset</strong> and <strong>Running fine-tuning</strong>: Once a slot opens up, it
will begin the fine-tuning process. This can take between 6-24 hours. You'll see how far through
each step in the training process your voice is, indicated by a percentage.

<strong>
  We are sorry the training run experienced issues and has been retried. No further action is
  required
</strong>

: This means that something went wrong. but your voice has been automatically queued to retry the
fine-tuning process. Your voice should successfully complete the fine-tuning process on the next
try, but if you experience multiple failures, please [contact
Support. ](https://help.elevenlabs.io/hc/en-us/requests/new?ticket_form_id=13145996177937)

<strong>Voice is ready to be used with the model</strong>: This means that the fine-tuning process
for this model has been completed, and you can now use your voice with this model.

<strong>Click to start fine-tuning</strong>: Some models do not train automatically, and you will
need to click the model name to begin fine-training. If additional models have become available for
your voice to fine-tune on, you'll see an exclamation icon next to your voice. 

<img src="https://help.elevenlabs.io/hc/article_attachments/35965182410513" alt="" />

To begin the fine-tuning process, just hover over your voice's name and click the name of the model.
