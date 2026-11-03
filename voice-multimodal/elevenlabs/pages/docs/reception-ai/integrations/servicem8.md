---
title: "ServiceM8"
source: https://elevenlabs.io/docs/reception-ai/integrations/servicem8.md
path: docs/reception-ai/integrations/servicem8
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# ServiceM8

With the [webhook tools](/docs/reception-ai/integrations/webhooks) below, your receptionist can create a quote or job in ServiceM8 when a caller needs work done, and add new callers as clients.

## Before you start

In ServiceM8, open **Settings** → **API Keys** and create a key. Every tool below sends it in the `X-Api-Key` request header. Anyone with the key can read and change your ServiceM8 data, so keep it out of shared documents.

## Create the tools

For each tool, go to **Integrations**, select **Add integration**, choose **Webhook Tool**, and set **Assign to agents** to **Receptionist**.

### Create a job

| Field               | Value                                                                                                                                                                                                                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**            | `create_servicem8_job`                                                                                                                                                                                                                                                                                  |
| **Description**     | "Create a job when a caller needs work done or wants a quote."                                                                                                                                                                                                                                          |
| **Method**          | POST                                                                                                                                                                                                                                                                                                    |
| **URL**             | `https://api.servicem8.com/api_1.0/job.json`                                                                                                                                                                                                                                                            |
| **Request Headers** | `X-Api-Key`: your API key                                                                                                                                                                                                                                                                               |
| **Body Parameters** | `status` (string, required): "Always the exact value `Quote`."  `job_address` (string, required): "The full address where the work is needed, including the postcode."  `job_description` (string, required): "The caller's name and phone number, then what they need done and any details they gave." |

Use `Work Order` instead of `Quote` if calls should go straight to scheduled work.

### Add a new client

| Field               | Value                                                                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**            | `create_servicem8_client`                                                                                                                         |
| **Description**     | "Add the caller as a new client when they say they haven't used us before."                                                                       |
| **Method**          | POST                                                                                                                                              |
| **URL**             | `https://api.servicem8.com/api_1.0/company.json`                                                                                                  |
| **Request Headers** | `X-Api-Key`: your API key                                                                                                                         |
| **Body Parameters** | `name` (string, required): "The caller's full name, or their business name."  `address` (string): "The client's address, including the postcode." |

Select **Enable** on each tool, then [test your receptionist](/docs/reception-ai/receptionist/testing) by asking for a quote. The new quote appears in ServiceM8.

## Limitations

* ServiceM8 replies to both tools with only `OK`. The new record's ID is in a response header your receptionist can't read, so it can't link the job to the client. Your team links them in ServiceM8.
* ServiceM8 keeps phone numbers and emails on a client's contacts, a separate record the client tool can't create. The job description holds the caller's number instead.
* Searching for an existing client needs a `$filter` parameter, and webhook tool parameter names can't contain `$`, so your receptionist can't look callers up.

To create linked clients and jobs, use ServiceM8's **Create Client** and **Create Job** actions through [Zapier](/docs/reception-ai/integrations/zapier).

## Troubleshooting

| Problem                | What to check                                                                                   |
| ---------------------- | ----------------------------------------------------------------------------------------------- |
| 401 from ServiceM8     | The header must be named `X-Api-Key` and hold a current key.                                    |
| 400 about the status   | `status` must be exactly `Quote`, `Work Order`, `Unsuccessful`, or `Completed`.                 |
| The job has no address | Make the description tell the receptionist to ask for the full address before creating the job. |
| 429 from ServiceM8     | You've hit ServiceM8's request limit. Wait a minute and try again.                              |
