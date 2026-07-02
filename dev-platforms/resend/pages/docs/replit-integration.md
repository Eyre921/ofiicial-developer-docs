---
title: "Send emails with Replit and Resend"
source: https://resend.com/docs/replit-integration
path: docs/replit-integration
---

Learn how to add the Resend integration to your Replit project.

[Replit](https://replit.com/) is a platform for building sites and apps with AI. You can add Resend in a Replit project by asking the chat to add email sending with Resend.

**Example prompt**

```
When someone fills out the contact form, send an email using Resend.
```

Prefer watching a video? Check out our video walkthrough below.

<YouTube />

## 1. Add a custom domain to your Resend account

By default, you can only send emails to your own email address.

To send emails to other email addresses:

1. Add a [custom domain to your Resend account](https://resend.com/domains).
2. Add the custom domain to the `from` field in the `resend` function in Replit (or ask the chat to update these fields).

Get more help adding a custom domain in [Resend's documentation](/docs/dashboard/domains/introduction).

## 2. Add your Resend API key and from address

To use Resend with Replit, you'll need to add a Resend API key, which you can create in the [Resend Dashboard](https://resend.com/api-keys). Do not share your API key with others or expose it in the browser or other client-side code.

The from address is the email address that will be used to send emails. Use your custom domain you added in step 1 here (e.g., `hello@example.com`).

<img alt="adding the Resend integration to a Replit chat" />

<Note>
  Replit tracks the details of your Resend integration in the [Integrations
  page](https://replit.com/integrations).
</Note>
