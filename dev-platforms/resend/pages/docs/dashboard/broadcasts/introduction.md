---
title: "Managing Broadcasts"
source: https://resend.com/docs/dashboard/broadcasts/introduction
path: docs/dashboard/broadcasts/introduction
---

Send marketing emails efficiently without code.

Broadcasts allow you to send email blasts to your customers using a no-code editor on Resend, or from our [Broadcast API](/docs/api-reference/broadcasts/create-broadcast).

You can use this to send email blasts such as:

* Newsletters
* Product Launches
* Investor Updates
* Promotions
* Changelogs

## Sending a Broadcast from Resend

Our Broadcasts feature was made to enable your entire team to send email campaigns without having to ask for help from developers.

### No-Code Editor

<video />

### Markdown Support

You can also write your emails using Markdown. This works with headings, lists, and quotes. It also works with italic, bold, and links.

If you copy and paste content from applications like Notion, Google Docs, or iA Writer, the editor maintains formatting consistency.

<video />

### Custom Styling

You can customize the look and feel of your email by changing **global styles** such as the background color, link color, and container size, allowing you to create emails aligned with your brand identity.

To do this, click on **Styles** at the top left of the Broadcast editor. You can edit specific images or lines of texts by selecting or highlighting them prior to clicking on **Styles**.

<video />

You can also edit individual styles for each component. These include the font size, font weight, letter spacing, line height, and text alignment. You can also set custom properties for each component, such as image alt, button links, and social links.

<video />

### Personalize your content

When creating broadcasts, you can include dynamic audience data to personalize the email content.

* `{{{contact.first_name|fallback}}}`
* `{{{contact.last_name|fallback}}}`
* `{{{contact.email}}}`
* `{{{RESEND_UNSUBSCRIBE_URL}}}`

When you include the `{{{RESEND_UNSUBSCRIBE_URL}}}` placeholder in the call, Resend includes an unsubscribe link in the email to automatically handle unsubscribe requests.

<Note>
  Learn how to create a [custom Unsubscribe
  Page](/docs/dashboard/settings/unsubscribe-page).
</Note>

### Testing & Sending

Once you're finished writing your email, you can preview it in your personal inbox or send it to your team for feedback.

To do this, click on **Test Email** on the top right of your screen. Enter in the email address you'd like to send your email to, and then click on **Send Test Email** to complete.

Once you're ready to send your email to your Audience, click on **Send**, and slide to confirm.

<video />

**Note**: Test emails do not include any custom Reply-To address that may have been configured. This behavior is limited to test mode and does not affect actual email sends.

## Managing Multiple Broadcasts

You can perform bulk actions on multiple broadcasts at once to efficiently manage your campaigns.

### Bulk Delete Drafts

To delete multiple draft broadcasts:

1. Select the broadcasts you want to delete by clicking the checkboxes next to each broadcast
2. Click **Delete** in the bottom action bar
3. Type the broadcast name (for single selection) or `DELETE N BROADCASTS` (for multiple) to confirm
4. Press **Cmd+Enter** or click **Delete broadcasts** to complete

You can also use keyboard shortcuts:

* **Cmd+A** to select all broadcasts on the current page
* **Backspace** to open the delete confirmation modal

<Note>
  Only draft broadcasts can be deleted. Sent or queued broadcasts cannot be
  removed.
</Note>

### Bulk Cancel Schedules

To cancel the schedule for multiple scheduled broadcasts:

1. Select the scheduled broadcasts you want to cancel
2. Click **Cancel schedule** in the bottom action bar
3. Type `CANCEL` to confirm
4. Press **Cmd+Enter** or click **Cancel schedules** to complete

When you cancel a scheduled broadcast, it returns to draft status and won't be sent at the scheduled time.

<Note>
  Canceling a broadcast only stops emails that haven't been sent yet. Any emails
  already delivered cannot be recalled. If a broadcast is mid-send (`queued`),
  canceling halts delivery to the remaining recipients.
</Note>

### Using Command Palette

You can also access bulk actions through the command palette (Cmd+K):

* **Select all** - Select all broadcasts on the current page
* **Delete selected** - Delete selected draft broadcasts
* **Cancel schedule** - Cancel schedules for selected broadcasts

## Clone as Template

You can turn any sent Broadcast into a [reusable Template](/docs/dashboard/templates/introduction) by clicking the more options button <span><Icon icon="ellipsis" /></span> next to a Broadcast and choosing **Clone as template**.

Cloning reuses a Broadcast's design and content as a starting point for transactional emails.

## Sending a Broadcast from the Broadcast API

You can also send your Broadcasts from the [Broadcast API](/docs/api-reference/broadcasts/create-broadcast).

The Broadcast API offers 6 endpoints for programmatically creating, updating, and sending broadcasts.

## Understand broadcast statuses

Here are all the statuses that can be associated with a broadcast:

* `draft`: The broadcast is a draft. Drafts can be edited, deleted, or scheduled for sending.
* `scheduled`: The broadcast is scheduled to be sent at a specific time. Scheduled broadcasts can have their schedule canceled, which returns them to draft status and prevents any emails from being sent.
* `sent`: The broadcast was sent.
* `queued`: The broadcast is queued for delivery. Canceling a queued broadcast stops delivery to the remaining recipients only. Emails already sent cannot be recalled.

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
