---
title: "Netlify Forms Troubleshooting"
source: https://docs.netlify.com/manage/forms/troubleshooting-tips.md
path: manage/forms/troubleshooting-tips
---

---
title: "Form troubleshooting tips"
description: "Refer to troubleshooting tips for setting up a form on our platform if things aren't working as expected."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

This document provides troubleshooting tips for setting up a form. If you have questions that aren't answered here, visit our Support Forums to get more advice about [how to debug your form](https://answers.netlify.com/t/common-issue-how-to-debug-your-form/92).

## Custom success page

If you're having trouble using the form `action` to customize the [success page](/manage/forms/setup#success-messages), try linking to your custom success page from somewhere on the same page as the form. Use the same exact path in your test link as you're trying to use for the `action` attribute, and make sure the link works there before digging further into your form.

## Extra spam prevention

If you're adding a [honeypot field](/manage/forms/spam-filters#honeypot-field) or [reCAPTCHA 2 challenge](/manage/forms/spam-filters#recaptcha-2-challenge), you can check the form detail page to confirm whether or not the **Extra spam prevention** has been successfully enabled.

## Missing submissions

Here are some common causes and solutions for missing form submissions.

### Test submissions flagged as spam

If you're sending test [submissions of your form](/manage/forms/submissions) and not finding them in your **Verified submissions** list, it's possible they're getting [flagged as spam by Akismet](/manage/forms/spam-filters). Use the menu above the list to switch to **Spam submissions** and then recheck for your tests.

To avoid having your tests flagged as spam in the first place, we recommend you

- enter a real email address instead of a fake one such as test@test.com.
- write some full sentences in any textareas rather than a few nonsense characters.
- spread out the rate of submissions from a single IP address.

### Form detection disabled

If you're not finding new form submissions in your **Verified submissions** list for updated or newly added forms, ensure that [form detection](/manage/forms/setup#automatic-form-detection) is enabled for your site.

If this is your first time enabling form detection, go to 
### NavigationPath Component:

Forms
 to turn on the setting. If you previously enabled form detection, go to 
### NavigationPath Component:

Forms > Usage and configuration > Form detection
 to review the setting.

Once you [enable](/manage/forms/setup#enable-form-detection) or [re-enable form detection](/manage/forms/setup#re-enable-form-detection), make sure you redeploy your site. Once you redeploy, Netlify will automatically scan your deploys for forms and will accept form submissions.

## Missing data from old submissions

If you recently changed the name or type of a form field, data for that field from old submissions will no longer appear in the Netlify UI. This is because the Netlify UI only shows the form fields and data that correspond to the last deployed version of your form.

Fortunately, all of your previous submission data are still available through the Netlify API. You can request form data with the [listFormSubmissions endpoint](https://open-api.netlify.com/#tag/submission/operation/listFormSubmissions).

If you would like to review the data from both the old and current form fields in the Netlify UI, we recommend that you mark old form fields as "hidden" instead of removing or replacing them entirely.

## Next.js Runtime v5 support

If you're using Netlify Forms with Next.js Runtime v5, you need to extract your form definitions to a dedicated static HTML file and make sure that the form submission uses AJAX rather than full-page navigation. Refer to [the Next.js v5 breaking changes](/build/frameworks/framework-setup-guides/nextjs/overview#v5-breaking-changes) for more information.

