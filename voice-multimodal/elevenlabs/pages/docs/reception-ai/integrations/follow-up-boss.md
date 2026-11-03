---
title: "Follow Up Boss"
source: https://elevenlabs.io/docs/reception-ai/integrations/follow-up-boss.md
path: docs/reception-ai/integrations/follow-up-boss
---

> This is a page from the ElevenLabs documentation. For a complete page index, fetch https://elevenlabs.io/docs/llms.txt. For the full documentation in a single file, fetch https://elevenlabs.io/docs/llms-full.txt.

# Follow Up Boss

Your receptionist can check whether a caller is already in Follow Up Boss, and send new callers in as leads. Looking up callers uses a [webhook tool](/docs/reception-ai/integrations/webhooks). Creating leads goes through [Zapier](/docs/reception-ai/integrations/zapier), because Follow Up Boss stores phone numbers and emails as nested lists that webhook tools can't send.

## Look up callers

### Get your API key

In Follow Up Boss, open **Admin** → **API** and copy your API key. The key acts as your user, so it can see the same people you can.

### Build the authorization header

Follow Up Boss uses the API key as a username with an empty password. Encode it in a terminal, replacing `YOUR_API_KEY` with your key and keeping the colon:

```bash
printf 'YOUR_API_KEY:' | base64
```

The header value is `Basic ` followed by the output.

> **Warning**
>
> Don't paste your API key into an online encoder. Anyone with the key or the encoded header can
> read and change your contacts.

### Create the webhook tool

Go to **Integrations**, select **Add integration**, and choose **Webhook Tool**.

| Field                | Value                                                                                                                             |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Name**             | `find_follow_up_boss_person`                                                                                                      |
| **Description**      | "Find the caller in our CRM by phone number. Use it at the start of a call to check whether they are an existing client or lead." |
| **Method**           | GET                                                                                                                               |
| **URL**              | `https://api.followupboss.com/v1/people`                                                                                          |
| **Request Headers**  | `Authorization`: `Basic ` followed by the encoded key                                                                             |
| **Query Parameters** | `phone` (string, required): "The caller's phone number."                                                                          |
| **Assign to agents** | **Receptionist**                                                                                                                  |

Select **Enable**.

> **Note**
>
> Follow Up Boss asks software that uses its API to register and identify itself with `X-System` and
> `X-System-Key` headers. If you've registered a system with Follow Up Boss, add both as request
> headers.

## Send new leads

### Connect Zapier

If you haven't yet, connect [Zapier](/docs/reception-ai/integrations/zapier) in Reception.ai.

### Add the Follow Up Boss action

In your Zapier MCP server, add the Follow Up Boss **New Inquiry or Website Event** action and connect your Follow Up Boss account. Set the source to a fixed value such as `Reception.ai`, and let the AI fill in the caller's name, phone number, email, and message.

Follow Up Boss recommends events like this one for new leads, because they run your lead routing and action plans. To log notes or tasks for existing people, you can also add the **Create Note** or **Create Task** actions.

### Assign the tool

In Reception.ai, open the Zapier integration's **Tools** tab, select **Refresh tools**, and assign the Follow Up Boss action to the **Client** (receptionist).

### Test it

[Test your receptionist](/docs/reception-ai/receptionist/testing) with a call from a new number about buying or selling a home. The lead appears in Follow Up Boss.

## Troubleshooting

| Problem                                  | What to check                                                                                        |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| 401 from Follow Up Boss                  | Encode the key with a colon after it, and start the header value with `Basic ` and a space.          |
| Known callers aren't found               | Follow Up Boss matches phone numbers as stored. Try a test call from a number saved in your account. |
| The receptionist creates duplicate leads | Tell it in the lookup tool's description to send a new lead only when the caller wasn't found.       |
| The Zapier action doesn't appear         | Select **Refresh tools** on the Zapier integration after adding actions in Zapier.                   |
