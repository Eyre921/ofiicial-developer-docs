---
title: "Jotform"
source: https://elevenlabs.io/docs/reception-ai/integrations/jotform.md
path: docs/reception-ai/integrations/jotform
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Jotform

Your receptionist can check whether a caller has sent in a form, such as an intake or booking request, and explain what a form asks for.

## Before you start

| Value       | Where to find it                                                                        |
| ----------- | --------------------------------------------------------------------------------------- |
| **API key** | **Settings** → **API** → **Create New Key**, with **Read Access**                       |
| **Form ID** | The number at the end of the form's URL, for example `form.jotform.com/241234567890123` |

Use `https://api.jotform.com` below if your account is in the US. Accounts in the EU use `https://eu-api.jotform.com`, and HIPAA accounts use `https://hipaa-api.jotform.com`.

## Look up submissions

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                          |
| -------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Name**             | `get_form_submissions`                                                                                         |
| **Description**      | "List recent submissions of our intake form. Use it when a caller asks whether we received their form."        |
| **Method**           | GET                                                                                                            |
| **URL**              | `https://api.jotform.com/form/FORM_ID/submissions`                                                             |
| **Request Headers**  | `APIKEY`: your API key                                                                                         |
| **Query Parameters** | `limit` (number, required): "Always 20."  `orderby` (string, required): "Always the exact value `created_at`." |
| **Assign to agents** | **Receptionist**                                                                                               |

Select **Enable**. Your receptionist reads the newest 20 submissions and looks for the caller's name or phone number in the answers.

## Explain the form

Create a second webhook tool with the same header.

| Field           | Value                                                                                  |
| --------------- | -------------------------------------------------------------------------------------- |
| **Name**        | `get_form_questions`                                                                   |
| **Description** | "Get the questions on our intake form. Use it when a caller asks what the form needs." |
| **Method**      | GET                                                                                    |
| **URL**         | `https://api.jotform.com/form/FORM_ID/questions`                                       |

[Test your receptionist](/docs/reception-ai/receptionist/testing) by asking whether a recent submission was received.

## Limitations

Your receptionist can't submit forms. Jotform's API takes submissions as form fields named like `submission[3]`, which webhook tools can't send. To collect details on a call, save them with another tool, such as [Airtable](/docs/reception-ai/integrations/airtable) or a [webhook](/docs/reception-ai/integrations/webhooks) to your own system.

## Troubleshooting

| Problem                   | What to check                                                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `You're not authorized`   | Check the API key, and use the API host for your account's region.                                                              |
| A submission isn't found  | It may be older than the newest 20. Raise the number in the `limit` description, keeping the list short enough to read through. |
| Answers are hard to match | Ask callers for the exact name or email they entered on the form.                                                               |
