---
title: "Genesys and Deepgram"
source: https://developers.deepgram.com/docs/genesys-deepgram.md
path: docs/genesys-deepgram
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Genesys and Deepgram

In this guide, we'll explain how to configure Deepgram as your transcription engine in Genesys.

## Before you begin

Before you can use Deepgram, you'll need to [create a Deepgram account](https://console.deepgram.com/signup?jump=keys). Signup is free and includes **\$200** in free credit and access to all of Deepgram's features!

Before you start, you'll need to follow the steps in the [Make Your First API Request](/guides/fundamentals/make-your-first-api-request) guide to obtain a Deepgram API key, and configure your environment if you are choosing to use a Deepgram SDK.

### Set Up a Genesys Cloud Org

You'll also need a Genesys Cloud org where you have completed the [initial setup tasks](https://help.mypurecloud.com/articles/new-users-home/) so that your call center can receive calls.

## Install Transcription Connector

In your Genesys org, follow [the steps to install Transcription Connector](https://help.mypurecloud.com/articles/install-transcription-connector-from-genesys-appfoundry/). The feature is currently in Limited Availability, so you may need to work with Genesys to give your org access.

## Configure Transcription Connector

Once you've installed Transcription Connector, it will appear under **Admin > Integrations** in the Genesys UI.

1. Click the three dots on the **Transcription Connector** row and choose **Edit Integration**.
2. Under **Configuration > Properties**, set **Channel** to `both` and **Connection URI** to `wss://integrations.deepgram.com/genesys`.
3. Under **Configuration > Credentials**, click **Configure** and paste your Deepgram API key into the **API Key** field. Leave the **Client Secret** field blank. Then click **OK**.

   If you specify an API key and then change it, it can take a long time for the new API key to propagate through the Genesys system. Give it 30 minutes before you assume that Deepgram is receiving the new API key. If you don't want to wait, you can delete Transcription Connector from the **Integrations** page, reinstall it, and provide the new API key to the reinstalled Transcription Connector.

## Set advanced configuration

Under **Configuration > Advanced**, provide a JSON object to customize the Deepgram request. For example:

```json JSON
{
  "model": "nova-3",
  "smart_format": true,
  "endpointing": 500,
  "tag": [
    "sometag1",
    "sometag2"
  ]
}
```

Within this JSON object, you have access to [the full suite of features in Deepgram's streaming API](/reference/speech-to-text/listen-streaming). However, be careful **NOT** to include any of the following, as they would prevent the integration from working correctly:

* `sample_rate`
* `encoding`
* `channels`
* `multichannel`
* `callback`

Setting `endpointing` to a high value like `500` is recommended for best transcript accuracy.

## Activate integration

Back in **Admin > Integrations**, flip the switch to activate the integration. Make sure it goes into the blue **Active** state and no errors are displayed.

## Choose where to use the Transcription Connector

Follow [the Genesys docs](https://help.mypurecloud.com/articles/configure-voice-transcription/) to select where your newly configured transcription engine will be used.

***

What’s Next

* [Deepgram API Overview](/reference/deepgram-api-overview)
