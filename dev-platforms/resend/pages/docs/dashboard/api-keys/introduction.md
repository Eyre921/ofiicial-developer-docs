---
title: "Introduction"
source: https://resend.com/docs/dashboard/api-keys/introduction
path: docs/dashboard/api-keys/introduction
---

Visualize all the API Keys on the Resend Dashboard.

## What is an API Key

API Keys are secret tokens used to authenticate your requests. They are unique to your account and must be kept confidential.

You can use multiple keys to isolate different application actions to different API Keys. This allows you to [view logs per key](#view-api-key-logs), detect possible abuse, and control any damage that may be done accidentally or maliciously.

## API key management

You can view and manage your API keys from the [API Key Dashboard](https://resend.com/api-keys). You can also create, list, or delete your API keys using the [API](/docs/api-reference/api-keys/create-api-key), or the [Resend CLI](/docs/cli#api-keys).

## View all API Keys

The [API Dashboard](https://resend.com/api-keys) shows you all the API Keys you have created along with their details, including the **last time you used** an API Key.

Different color indicators let you quickly scan and detect which API Keys are being used and which are not.

<img alt="View All API Keys" />

## Edit API Key details

After [creating an API Key](/docs/create-an-api-key), you can edit the following details:

* [Name](/docs/api-reference/api-keys/create-api-key#param-name)
* [Permission](/docs/api-reference/api-keys/create-api-key#param-permission)
* [Domain](/docs/api-reference/api-keys/create-api-key#domain-id)

<Info>You cannot view or edit an API Key value after it has been created.</Info>

To edit an API key in the Resend Dashboard, click the **More options** <Icon icon="ellipsis" /> button and then **Edit API Key**.

<img alt="View Inactive API Key" />

## Delete inactive API Keys

If an API Key **hasn't been used in the last 30 days**, consider deleting it to keep your account secure.

<img alt="View Inactive API Key" />

You can delete an API Key by clicking the **More options** <Icon icon="ellipsis" /> button and then **Remove API Key**.

<img alt="Delete API Key" />

## View API Key logs

When visualizing an active API Key, you can see the **total number of requests** made to the key. For more detailed logging information, select the underlined number of requests to view all logs for that API Key.

<img alt="View Active API Key" />

## Export your data

Admins can download your data in CSV format for the following resources:

* Emails
* Broadcasts
* Contacts
* Segments
* Domains
* Logs
* API keys

<Info>Currently, exports are limited to admin users of your team.</Info>

To start, apply filters to your data and click on the "Export" button. Confirm your filters before exporting your data.

<video />

If your exported data includes 1,000 items or less, the export will download immediately. For larger exports, you'll receive an email with a link to download your data.

All admins on your team can securely access the export for 7 days. Unavailable exports are marked as "Expired."

<Note>
  All exports your team creates are listed in the
  [Exports](https://resend.com/exports) page under **Settings** > **Team** >
  **Exports**. Select any export to view its details page. All members of your
  team can view your exports, but only admins can download the data.
</Note>
