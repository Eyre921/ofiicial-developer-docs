---
title: "Testing your receptionist"
source: https://elevenlabs.io/docs/reception-ai/receptionist/testing.md
path: docs/reception-ai/receptionist/testing
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Testing your receptionist

Test your receptionist before going live and after every configuration change. Reception.ai supports testing in the browser, by voice or text, and with real phone calls.

## Browser testing

Start a test from the receptionist button in the sidebar, which shows the receptionist's phone number or name. On mobile, select **Test call** on the Receptionists page.

The test dialog lets you:

* **Call**: talk to your receptionist through your microphone.
* **Chat**: type messages to test responses quickly.

If your browser blocks the microphone, allow microphone access for the site and try again.

## Phone call testing

For a full end-to-end test, call your receptionist's phone number from any phone. The test dialog shows the number under **Or call**.

Phone calls are the only way to test [transfers](/docs/reception-ai/receptionist/call-handling#transfer-to-a-human), [staff first answering](/docs/reception-ai/receptionist/call-handling#answering-order), and secure mode for known callers. These features do not work in browser conversations.

## What to test

#### Greeting

Verify the first message sounds natural and includes your business name. If **Always finish the
first message** is on, try interrupting and confirm the greeting continues.

#### Appointment booking

Ask to book an appointment. Verify the receptionist offers the correct services and available
times, and confirms the booking.

#### Procedures

Trigger each procedure with a realistic request and confirm the receptionist follows the steps
in order.

#### Business questions

Ask about hours, location, pricing, or services. Verify answers match your business information.

#### Language switching

Speak a full sentence in one of your additional languages and verify the receptionist switches.
Short phrases do not trigger a switch.

#### Caller verification

With secure mode on, call from a number that is not on file and ask about an existing booking.
Verify the receptionist asks for a verification code before sharing details.

#### Edge cases

Ask something outside your business scope. Verify the receptionist handles it well, for example
by taking a message or offering a transfer.

#### Transfer rules

From a phone, trigger a transfer rule and verify the call reaches the correct number.

> **Tip**
>
> After each test, open **Conversations** to review the transcript and outcome. If the header shows
> a configuration warning, open it to review findings about your instructions.
