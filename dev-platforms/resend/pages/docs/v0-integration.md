---
title: "Send emails with v0 and Resend"
source: https://resend.com/docs/v0-integration
path: docs/v0-integration
---

Learn how to add the Resend integration to your v0 project.

[v0](https://v0.dev) by Vercel is a platform for building web sites, tools, apps, and projects via chat. You can add Resend in a v0 project by asking the chat to add email sending with Resend.

## Guide

<Steps>
  <Step title="Add your Resend API key">
    To use Resend with v0, you'll need to add a Resend API key, which you can create in the [Resend Dashboard](https://resend.com/api-keys).

    <Note>
      Do not share your API key with others or expose it in the browser or other
      client-side code.
    </Note>

    <img alt="adding the Resend integration to a v0 chat" />
  </Step>

  <Step title="Add a custom domain to your Resend account">
    By default, you can only send emails to your own email address.

    To send emails to other email addresses:

    1. Add a [custom domain to your Resend account](/docs/add-a-domain).
    2. Add the custom domain to the `from` field in the `resend` function in v0 (or ask the chat to update these fields).

    Get more help adding a custom domain in [Resend's documentation](/docs/dashboard/domains/introduction).
  </Step>
</Steps>
