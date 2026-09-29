---
title: "Topics"
source: https://resend.com/docs/dashboard/contacts/manage-topics
path: docs/dashboard/contacts/manage-topics
---

Learn how to create, view, delete, and manage Topics.

[Managing subscribers and unsubscribers](/docs/dashboard/contacts/managing-unsubscribe-list) is a critical part of any email implementation. Topics let your Contacts self-manage their marketing email preferences.

Instead of having a single unsubscribe option for all emails, Topics let your Contacts opt in or out of specific types of communications. This keeps them subscribed to the emails they want to receive.

When you send [Broadcasts](/docs/dashboard/broadcasts/introduction), you can optionally scope [sending with a particular Topic](#send-a-broadcast-with-a-topic). Not only do Topics help you send more precisely, but they also give your users more control over which emails they receive.

## Create a Topic

You can create a new Topic in the [Dashboard](https://resend.com/audience/topics) or programmatically from the [Topics API](/docs/api-reference/topics/create-topic), with a [Topics CLI command](/docs/cli#topics), or with [MCP](/docs/mcp-server).

To create a Topic in the Dashboard:

<Steps>
  <Step title="Go to the **Topics** Dashboard view and click **Create Topic**." />

  <Step title="Enter a name for your Topic.">
    Choose something that will help your recipients decide whether they are
    interested in receiving these emails, like "announcements" or "product
    reviews."
  </Step>

  <Step title="Optionally give your Topic a description." />

  <Step title="Select **Opt-in** or **Opt-out** as the default subscription. This value cannot be changed later.">
    <ul>
      <li>
        <b>Opt-in</b>: All Contacts will receive the email unless they have
        explicitly unsubscribed from that Topic.
      </li>

      <li>
        <b>Opt-out</b>: Subscribers will not receive the email unless they have
        explicitly subscribed to that Topic.
      </li>
    </ul>
  </Step>

  <Step title="Select **Public** or **Private** as the visibility.">
    <ul>
      <li>
        <b>Private</b>: Only Contacts who are opted in to the Topic can see it
        on the unsubscribe page.
      </li>

      <li>
        <b>Public</b>: All Contacts can see the Topic on the unsubscribe page.
      </li>
    </ul>
  </Step>
</Steps>

<img alt="Add Topic" />

## View all Topics

The [Topics tab of the Audience Dashboard page](https://resend.com/audience/topics) shows you all the Topics you have created along with their details.

<img alt="View All Topics" />

You can also [retrieve a single Topic](/docs/api-reference/topics/get-topic) or [list all your Topics](/docs/api-reference/topics/list-topics) via the API or [CLI](/docs/cli#topics).

## Edit Topic details

After creating a Topic, you can edit the following details:

* Name
* Description
* Visibility

To edit a Topic, click the **More options** <Icon icon="ellipsis" /> button and then **Edit Topic**.

<img alt="View edit topic" />

You can also [update a Topic](/docs/api-reference/topics/update-topic) via the API.

<Info>
  You cannot edit the default subscription value after it has been created.
</Info>

## Delete a Topic

You can delete a Topic by clicking the **More options** <Icon icon="ellipsis" /> button and then **Remove Topic**.

<img alt="Delete Topic" />

You can also [delete a Topic](/docs/api-reference/topics/delete-topic) via the API.

## Send a Broadcast with a Topic

You can send with a Topic in the Broadcast editor from the Topics dropdown menu.

<img alt="Send emails with a Topic" />

You can also send with a Topic via the [Broadcast API](/docs/api-reference/broadcasts/create-broadcast).

## Topic Subscription Statuses

When you [view a Contact's details](/docs/dashboard/contacts/manage-contacts#view-contacts), you can see the list of Topics that they are subscribed to.

<img alt="Topic Subscription Statuses" />

You can also check a Contact's subscribed Topics [via the API or SDKs](/docs/api-reference/contacts/get-contact-topics) or with a [Contacts CLI command](/docs/cli#contacts).

## Updating a Topic Subscription for a Contact

When you [create new Topics](#create-a-topic), you can update the subscription preferences of your Contacts to include these Topics. A Contact can belong to multiple Topics, and Resend automatically provides an unsubscribe flow for users who decide to opt out of receiving these emails.

You can add a Contact to a Topic via the Dashboard by expanding the **More options** <Icon icon="ellipsis" /> and then **Edit Contact**. Add or remove Topics for a given Contact.

<img alt="Add Contact to Topic" />

You can also update a Topic subscription for a Contact [via the API or SDKs](/docs/api-reference/contacts/update-contact-topics) or with a [Contacts CLI command](/docs/cli#contacts).

## Bulk Subscribe to Topics

You can subscribe multiple Contacts to Topics in the [Dashboard](https://resend.com/audience/) at once:

<Steps>
  <Step title="Go to the **Contacts** Dashboard view." />

  <Step title="Select multiple Contacts by clicking the checkbox next to each Contact." />

  <Step title="Click the **Edit** button in the bulk actions bar." />

  <Step title="Select **Subscribe to Topics**" />

  <Step title="Choose the Topics you want to subscribe the Contacts to." />

  <Step title="Click **Subscribe**" />
</Steps>

Learn more about [bulk actions for Contacts](/docs/dashboard/contacts/manage-contacts#bulk-actions).

## API Reference

For complete API documentation, see the [Topics API reference](/docs/api-reference/topics/create-topic).
