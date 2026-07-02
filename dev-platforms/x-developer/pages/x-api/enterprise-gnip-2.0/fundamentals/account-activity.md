---
title: "Account Activity API: Enterprise"
source: https://docs.x.com/x-api/enterprise-gnip-2.0/fundamentals/account-activity
path: x-api/enterprise-gnip-2.0/fundamentals/account-activity
---

Manage webhooks and subscriptions with the enterprise Account Activity API to stream realtime Posts, Direct Messages, likes, follows, and edits.

<Note>
  This endpoint has been updated to include Post edit metadata. Learn more about these metadata on the ["Edit Posts" fundamentals page](/x-api/enterprise-gnip-2.0/fundamentals/edit-tweets). 

  This endpoint is often used with the Direct Messages endpoints. We have launched new [v2 Direct Messages endpoints](/x-api/direct-messages/manage/introduction). Note that the Enterprise and Premium Account Activity APIs support v2 one-to-one messages, but do not yet support group conversations.   
</Note>

Overview

`Enterprise`

The Account Activity API provides you the ability to subscribe to realtime activities related to a user account via webhooks. This means that you can receive realtime Posts, Direct Messages, and other account events from one or more of your owned or subscribed accounts through a single connection.

You will receive all related activities below for each user subscription on your webhook registration:

| Activity types                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                               |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \* Posts (by user)  <br />    <br />\* Post deletes (by user)<br />\* @mentions (of user)<br />\* Replies (to or from user)<br />\* Retweets (by user or of user)<br />\* Quote Tweets (by user or of user)<br />\* Retweets of Quoted Tweets (by user or of user)<br />\* Likes (by user or of user)<br />\* Follows (by user or of user)  <br />    <br />\* Unfollows (by user) | \* Blocks (by user)<br />\* Unblocks (by user)<br />\* Mutes (by user)<br />\* Unmutes (by user)<br />\* Direct Messages sent (by user)<br />\* Direct Messages received (by user)<br />\* Typing indicators (to user)<br />\* Read receipts (to user)<br />\* Subscription revokes (by user) |

**Please note** - We do not deliver home timeline data via the Account Activity API. Please use the [GET statuses/home\_timeline](https://developer.x.com/en/docs/x-api/v1/tweets/timelines/overview) to pull this data.
 

#### Video series

Check out our [four-part video series](https://www.youtube.com/watch?v=otPxejFhyy8\&index=0\&list=PLFKjcMIU2WshGG6Yj940XM7Z6BFs1zfBg) on the Account Activity API to get up to speed!

<iframe />

### Feature summary

| Tier       | Pricing                                                     | Number of unique subscriptions | Number of webhooks | Reliability and Activity Recovery                                                                                                                                              |
| :--------- | :---------------------------------------------------------- | :----------------------------- | :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enterprise | [Contact sales](/x-api/enterprise-gnip-2.0/enterprise-gnip) | Up to 500+                     | 3+                 | [Retries](/x-api/enterprise-gnip-2.0/fundamentals/account-activity#retries) and [Replay](/x-api/enterprise-gnip-2.0/fundamentals/account-activity#account-activity-replay-api) |

* Have questions? Running into errors?
  * Read our [Frequently asked questions](/x-api/enterprise-gnip-2.0/fundamentals/account-activity#frequently-asked-questions) or [Error Troubleshooting guide](/x-api/enterprise-gnip-2.0/fundamentals/account-activity#frequently-asked-questions).

* Explore our sample code:
  * [Enterprise Account Activity API dashboard](https://github.com/xdevplatform/account-activity-dashboard-enterprise), a node web app that displays webhook events using the enterprise tier of the Account Activity API and includes [Replay](/x-api/enterprise-gnip-2.0/fundamentals/account-activity#account-activity-replay-api) functionality.
  * The [SnowBot chatbot](https://github.com/xdevplatform/SnowBotDev), a Ruby web app built on the enterprise Account Activity and Direct Message APIs.

## Manage webhooks and subscribed users

**⏱ 10 min read**

The enterprise Account Activity API provides you webhook-based JSON messages any time there are events associated with X accounts subscribed to your service. X delivers those activities to your registered webhook. In the following steps, you will learn how to manage webhooks and subscribed users.

You will learn how to register, view, and remove, both webhooks and subscribed users. We'll be using simple cURL commands to make requests to the various API endpoints. cURL is a command-line tool for getting or sending requests using the URL syntax.

You will need:

* A registered X app - *[register here](https://developer.x.com/content/developer-twitter/en/apps)*
* A bearer token - *[learn more](/resources/fundamentals/authentication#using-and-generating-an-app-only-bearer-token)*
* A webhook that passes a Challenge-Response Check (CRC) - *[learn more](/x-api/enterprise-gnip-2.0/fundamentals/account-activity#securing-webhooks)*
* An enterprise account - *\[apply here][https://developer.x.com/en/products/x-api/enterprise](https://developer.x.com/en/products/x-api/enterprise)*

*Before you get started, we recommend you check out our [Github repo here](https://github.com/xdevplatform/account-activity-dashboard) that provides a sample web app and helper scripts to get started with X's Account Activity API*

#### Managing a webhook:

Using a webhook provides you the ability to subscribe to realtime activities related to a user account through a single connection. 

<Tabs>
  <Tab title="Adding a webhook">
    Let’s begin with registering a new webhook URL for the given application context.

    The URL will be validated via a CRC request before saving. Once you've registered a webhook, make sure to document the webhook ID as you will need it later on.

    Copy the following cURL request into your command line after making changes to the following:

    * **URL** `<URL>` e.g. `https://yourdomain.com/webhooks/twitter/`

    * **Consumer key** `<CONSUMER_KEY>` e.g. `xvz1evFS4wEEPTGEFPHBog`

    * **Access token** `<ACCESS_TOKEN>` e.g.  `370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb`

      ```
      curl --request POST --url 'https://api.x.com/1.1/account_activity/webhooks.json?url=<URL>' --header 'authorization: OAuth oauth_consumer_key="<CONSUMER_KEY>", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="<ACCESS_TOKEN>", oauth_version="1.0"'
      ```
  </Tab>

  <Tab title="Viewing a webhook">
    We will run the following command to returns all registered webhook URLs and their statuses for the given application.

    Copy the following cURL request into your command line after making changes to the following:

    * **Bearer token** `<BEARER_TOKEN>` e.g. `AAAAAAAAAAAA0%2EUifi76ZC9Ub0wn...`

      ```curl --request GET --url https://api.x.com/1.1/account_activity/webhooks.json --header 'authorization: Bearer <BEARER_TOKEN>' theme={null}
      ```
  </Tab>

  <Tab title="Removing a webhook">
    To remove a webhook from the provided application's configuration, copy the following cURL request into your command line after making changes to the following:

    * **Webhook ID** `<:WEBHOOK_ID>` e.g. `1234567890`

    * **Consumer key** `<CONSUMER_KEY>` e.g. `xvz1evFS4wEEPTGEFPHBog`

    * **Access token** `<ACCESS_TOKEN>` e.g.  `370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb`

      ```curl --request DELETE --url https://api.x.com/1.1/account_activity/webhooks/<:WEBHOOK_ID>.json --header 'authorization: OAuth oauth_consumer_key="<CONSUMER_KEY>", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="<ACCESS_TOKEN>", oauth_version="1.0"' theme={null}
      ```
  </Tab>
</Tabs>

#### Managing subscribed users:

Once you've registered a Webhook, you can add a subscribed user to the Account Activity API to begin receiving their account activities.

<Tabs>
  <Tab title="Adding a subscription">
    We'll begin with subscribing a user so you receive all event types.

    Copy the following cURL request into your command line after making changes to the following:

    * **Webhook ID** `<:WEBHOOK_ID>` e.g. `1234567890`

    * **Consumer key name** `<CONSUMER_KEY>` e.g. `xvz1evFS4wEEPTGEFPHBog`

    * **Subscribing user's access token** `<SUBSCRIBING_USER'S_ACCESS_TOKEN>` e.g. `370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb`

      ```
      curl --request POST --url https://api.x.com/1.1/account_activity/webhooks/<:WEBHOOK_ID>/subscriptions/all.json --header 'authorization: OAuth oauth_consumer_key="<CONSUMER_KEY>", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="<SUBSCRIBING_USER'S_ACCESS_TOKEN>", oauth_version="1.0"'
      ```
  </Tab>

  <Tab title="Viewing subscriptions">
    To view a list of all activity type subscriptions for a specified webhook, copy the following cURL request into your command line after making changes to the following:

    * **Webhook ID** `<:WEBHOOK_ID>` e.g. `1234567890`

    * **Bearer token** `<BEARER_TOKEN>` e.g. `AAAAAAAAAAAA0%2EUifi76ZC9Ub0wn...`

      ```
      curl --request GET --url https://api.x.com/1.1/account_activity/webhooks/<:WEBHOOK_ID>/subscriptions/all/list.json --header 'authorization: Bearer <BEARER_TOKEN>'
      ```
  </Tab>

  <Tab title="Removing a subscription">
    After deactivation, all events for the requesting user will no longer be sent to the webhook URL.

    To deactivate a subscription from the provided user context and application, copy the following cURL request into your command line after making changes to the following:

    * **Webhook ID** `<:WEBHOOK_ID>` e.g. `1234567890`

    * **Consumer key** `<CONSUMER_KEY>` e.g. `xvz1evFS4wEEPTGEFPHBog`

    * **Subscribing user's access token** `<SUBSCRIBING_USER'S_ACCESS_TOKEN>` e.g. `370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb`

      ```
      curl --request DELETE --url https://api.x.com/1.1/account_activity/webhooks/:WEBHOOK_ID/subscriptions/all.json --header 'authorization: OAuth oauth_consumer_key="CONSUMER_KEY", oauth_nonce="GENERATED", oauth_signature="GENERATED", oauth_signature_method="HMAC-SHA1", oauth_timestamp="GENERATED", oauth_token="SUBSCRIBED_USER'S_ACCESS_TOKEN", oauth_version="1.0"'
      ```
  </Tab>
</Tabs>

Great job! You should now able to manage your webhooks and subscribed users.

#### Referenced articles

* [Overview of Challenge-Response Check (CRC)](/x-api/enterprise-gnip-2.0/fundamentals/account-activity#securing-webhooks)
* [Account Activity Data Types](/x-api/enterprise-gnip-2.0/fundamentals/account-activity#account-activity-data-object-structure)
* [Managing Webhooks and Subscriptions](/x-api/enterprise-gnip-2.0/fundamentals/account-activity#managing-webhooks-and-subscriptions)

## A video walkthrough of the Account Activity API

In this video walkthrough, you will learn about the capabilities of the premium and enterprise tiers of the Account Activity API.

By the end of this video, you will learn abo
