---
title: "Netlify Forms Notifications"
source: https://docs.netlify.com/manage/forms/notifications.md
path: manage/forms/notifications
---

---
title: "Form notifications"
description: "Set up notifications for form submissions using email, webhooks, or Slack. Use a third-party integration to trigger an action upon form submission."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt). Markdown versions of any documentation page are available by appending `.md` to its docs.netlify.com URL.

Stay updated on the latest form submissions and trigger your own custom workflows with form notifications. Send form notifications to email, webhooks, or a Slack workspace. 

Set up notifications for verified submissions to a specific form or for all verified submissions to any form on your site. 

To send form notifications to email or webhooks: 
- Go to  
### NavigationPath Component:

Project configuration > Notifications > Emails and webhooks > Form submission notifications
. 

To send form notifications to a Slack workspace: 
- Check out our docs on setting up the [Netlify App for Slack](/extend/install-and-use/setup-guides/netlify-app-for-slack).

## Slack notifications 

Surface form submissions in Slack with just a few clicks. Learn more in the [Netlify App for Slack docs](/extend/install-and-use/setup-guides/netlify-app-for-slack).

## Email notifications

By default, form notification emails are sent from formresponses@netlify.com, and any replies to a notification go to that address. To respond to a form submitter, you need to enter their address manually.

We recommend that you add an `<input>` with `name="email"` to your form. This sets the `Reply-to` value on the form notification email, allowing you to reply directly to the form submitter without manually entering their email.

### Customize the email subject line

You can completely customize the email subject line in the email notifications that Netlify sends when someone submits a form from your site.

If you don't customize the email subject line in the Netlify UI or in your Netlify HTML form, then your form will automatically apply a default email subject line.

You can customize the email subject line from the Netlify UI or in the HTML markup for your form. 

We recommend that you choose one way to customize your email subject line since whatever you set in the HTML form overrides the settings in the Netlify UI. 

As an overview of these options, consider the following:
  - To reference anything programmatically in the email subject line and keep the subject line version controlled, set the email subject line in your HTML form. Check out [the example HTML forms](/manage/forms/notifications#example-html-forms).
  - To manage your form's email subject line in the Netlify UI, set the email subject line at 
### NavigationPath Component:

Project configuration > Notifications > Emails and webhooks > Form submission notifications
. To change the email subject line, additionally select **Options > Edit notifications**. You many need to remove any email subject line specified in your forms' HTML to keep the email subject line you specify in the Netlify UI.

You can also apply predefined variables to your email subject line, such as `%{formName}` , `%{siteName}`, or `%{submissionId}`. 

For example, your email subject line can be `New lead from %{formName} (%{submissionId})`. Use these variables in the HTML form or in the Netlify UI.

### Example HTML forms

This example sets the email subject line for your form notification to `Sales inquiry from mysitename.netlify.app`:

```html
<form name="contact" method="POST" data-netlify="true">
  <input type="hidden" name="subject" 
  value="Sales inquiry from mysitename.netlify.app" />
  <p>
    <label>Your Name: <input type="text" name="name" /></label>
  </p>
  <p>
    <label>Your Email: <input type="email" name="email" /></label>
  </p>
  <p>
    <label>Message: </label>
  </p>
  <p>
    <button type="submit">Send</button>
  </p>
</form>
```

The `Reply-to` email is whatever value the form submitter entered in the `Your Email:` field.

This example uses [predefined variables](/manage/forms/notifications#customize-the-email-subject-line) to dynamically set your email subject line to `New lead from %{formName} (%{submissionId})`:

```html
<form name="contact" method="POST" data-netlify="true">
  <input type="hidden" name="subject" 
  value="New lead from %{formName} (%{submissionId})" />
  <p>
    <label>Your Name: <input type="text" name="name" /></label>
  </p>
  <p>
    <label>Your Email: <input type="email" name="email" /></label>
  </p>
  <p>
    <label>Message: </label>
  </p>
  <p>
    <button type="submit">Send</button>
  </p>
</form>
```

### Note - Older form or want to remove [Netlify] from subject line?

The example above assumes your form was created after May 5, 2023. Forms created before this date will have an automated `[Netlify]` prefix in your email subject line. 

To remove `[Netlify]` from the subject line of your form submission email notification, check out our [`[Netlify]` prefix removal docs](/manage/forms/notifications/#remove-netlify-prefix-from-your-email-subject-line).

For greater control of form-triggered emails, or to connect other services, you can use the Netlify app on [Zapier](#zapier-integrations) or [n8n](#n8n-integrations).

### Remove `[Netlify]` prefix from your email subject line

Forms created before May 5, 2023 included `[Netlify]` as a default and automated prefix in the email subject line. 

Now you can remove the `[Netlify]` prefix from your email subject line and completely customize your email subject line. 

To remove `[Netlify]` from the email subject line of your form submission notification email:
- If you have an email subject line specified in your HTML form, decide whether to [modify your existing email subject line in the HTML form](/manage/forms/notifications#remove-netlify-prefix-in-the-html-form) or opt to [use the Netlify UI](/manage/forms/notifications#customize-the-email-subject-line) instead.
- If you do not have an email subject line specified in your HTML form, you can just [edit the form notification settings in the Netlify UI](/manage/forms/notifications#customize-the-email-subject-line). All new forms will not include `[Netlify]`.

#### Remove `[Netlify]` prefix in the HTML form

To remove the `[Netlify]` prefix from your subject line and keep using the HTML form to specify the subject line, add the `data-remove-prefix` attribute to your HTML form's email subject input field:

```html
<form name="contact" method="POST" data-netlify="true">
  <input type="hidden" name="subject" data-remove-prefix
  value="Sales inquiry from mysitename.netlify.app" />
  <!-- Add other form fields here -->
</form>
```

In this example, your email subject line is `Sales inquiry from mysitename.netlify.app`. This removes `[Netlify]` from your new form notification emails. Learn more about this update in this [support Forums post](https://answers.netlify.com/t/customize-the-email-subject-line-for-form-submission-notifications/91534).

Note that if you have an HTML form with a different email subject specified, that subject will take precedence over any updates you make to the email subject line in the Netlify UI.

## Zapier integrations

Netlify is available on Zapier, where you can connect Netlify with over 1,000 other applications. You can set up a "Zap" action to be triggered when there is a verified form submission on your website. You can [find out more on our blog](https://www.netlify.com/blog/2018/11/07/automate-your-netlify-sites-with-zapier/), or use one of the templates below to get started:

### Integration: zapier-forms

- **ID**: zapier-forms
- **Description**: Start a deploy of your Netlify site after new Netlify form submissions
- **Subtext**: Netlify
- **Link**: https://zapier.com/webintent/create-zap?template
- **CTA Text**: Use this zap

### Integration: zapier-forms

- **ID**: zapier-forms
- **Description**: Send Gmail emails for new Netlify form submissions
- **Subtext**: Gmail + Netlify
- **Link**: https://zapier.com/webintent/create-zap?template
- **CTA Text**: Use this zap

### Integration: zapier-forms

- **ID**: zapier-forms
- **Description**: Save new Netlify form submissions to rows in Google Sheets
- **Subtext**: Google Sheets + Netlify
- **Link**: https://zapier.com/webintent/create-zap?template
- **CTA Text**: Use this zap

### Integration: zapier-forms

- **ID**: zapier-forms
- **Description**: Create Salesforce leads from new Netlify form submissions
- **Subtext**: Netlify + Salesforce
- **Link**: https://zapier.com/webintent/create-zap?template
- **CTA Text**: Use this zap

### Integration: zapier-forms

- **ID**: zapier-forms
- **Description**: Create Mailchimp subscribers from new Netlify form submissions
- **Subtext**: Mailchimp + Netlify
- **Link**: https://zapier.com/webintent/create-zap?template
- **CTA Text**: Use this zap

### Integration: zapier-forms

- **ID**: zapier-forms
- **Description**: Create Zendesk tickets for new Netlify form submissions
- **Subtext**: Netlify + Zendesk
- **Link**: https://zapier.com/webintent/create-zap?template
- **CTA Text**: Use this zap

## n8n integrations
Netlify is available on <a href="https://n8n.io/" target="_blank">n8n</a>, an open source tool that allows you to connect Netlify with other applications. By using one of n8n's Netlify nodes, you can create your own automated workflow. To get started, you can use the [Netlify node](https://n8n.io/integrations/netlify/), [Netlify Trigger node](https://n8n.io/integrations/netlify-trigger/), or you can use the existing workflow below:

### Integration: n8n-forms

- **ID**: n8n-forms
- **Description**: Add Netlify Form submissions to Airtable
- **Subtext**: Netlify Trigger node
- **Link**: https://n8n.io/workflows/1253-add-netlify-form-submissions-to-airtable/
- **CTA Text**: Use workflow


