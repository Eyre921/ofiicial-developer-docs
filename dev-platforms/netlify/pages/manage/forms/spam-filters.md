---
title: "Netlify Form Spam Filters"
source: https://docs.netlify.com/manage/forms/spam-filters.md
path: manage/forms/spam-filters
---

---
title: "Spam filters"
description: "Rely on built-in spam protection for forms, or set up extra spam protection using a honeypot field or reCAPTCHA."
---

> For the complete documentation index for AI agents, see [llms.txt](https://docs.netlify.com/llms.txt).

All form submissions are filtered for spam [using Akismet](https://www.netlify.com/blog/2019/02/12/improved-netlify-forms-spam-filtering-using-akismet/), an industry leader in spam detection. Only submissions that pass the filter are included in your form's **Verified submissions** list in the [form submissions UI](/manage/forms/submissions#form-submissions-ui). Submissions flagged as spam by Akismet can be found by switching to your form's **Spam submissions** list.

### Tip - Tip

You can [change the state of a submission](/manage/forms/submissions#change-a-form-submission-s-state) from spam to verified or vice versa.

## Extra spam prevention
For additional protection to help prevent abuse of your forms, you can add a [honeypot field](/manage/forms/spam-filters#honeypot-field), a [reCAPTCHA 2](/manage/forms/spam-filters#recaptcha-2-challenge), or both. We automatically reject submissions that do not pass these challenges. Junk submissions caught by a honeypot field or reCAPTCHA 2 won't even be included in your form's spam submissions. The **Submissions** page for a form will indicate if it has any extra spam prevention enabled.

### Honeypot field

"Honeypot" fields are hidden form fields that lure bot users into completing a field that human users can't detect. A form submitted with a completed honeypot field can be safely rejected because only a bot would detect and complete the field. You can alert Netlify to a hidden honeypot field by adding a `netlify-honeypot` attribute to your `<form>` with the name of your hidden field. Then make sure that field is present in the form, but hidden via CSS or JavaScript.

Here's an example:

```html
<form
  name="contact"
  method="POST"
  netlify-honeypot="bot-field"
  data-netlify="true"
>
  <p class="hidden">
    <label>
      Don't fill this out if you're human: <input name="bot-field" type="text" />
    </label>
  </p>
  <p>
    <label>
      Email: <input type="text" name="email" />
    </label>
  </p>
  <p>
    <label>
      Message: 
    </label>
  </p>
  <p>
    <button type="submit">Send</button>
  </p>
</form>
```

When Netlify parses the static HTML during post-processing, the build system automatically strips the `netlify-honeypot` attribute from the `<form>` tag, leaving the honeypot input field in place. In the example above, if a spambot enters any value in `bot-field`, Netlify will quietly reject the form submission.

If you [submit your form with AJAX](/manage/forms/setup#submit-javascript-rendered-forms-with-ajax), make sure that the honeypot field name is included in the body of the POST request. This happens automatically if you use `FormData()` to encode the body of the request.

### reCAPTCHA 2 challenge

If you would like to add a [reCAPTCHA 2 challenge](https://developers.google.com/recaptcha/) to a form, Netlify can include one for you, or you can [add your own](/manage/forms/spam-filters#custom-recaptcha-2).

#### Netlify-provided reCAPTCHA 2

To have Netlify provide the CAPTCHA:

1. Add a `data-netlify-recaptcha="true"` attribute to your `<form>` tag.
2. In the place where you'd like the CAPTCHA to appear, add an empty `<div>` element inside your form with the same `data-netlify-recaptcha="true"` attribute.

When your site is published, the form will include the necessary HTML to render the CAPTCHA.

Here's an example:

```html
<form
  name="contact"
  method="POST"
  data-netlify-recaptcha="true"
  data-netlify="true"
>
  <p>
    <label>
      Email: <input type="text" name="name" />
    </label>
  </p>
  <p>
    <label>
      Message: 
    </label>
  </p>
  
  <p>
    <button type="submit">Send</button>
  </p>
</form>
```

When a visitor submits the form, our servers will validate the CAPTCHA server-side. If the validation fails, we'll redirect the visitor back to the same page and reject the form submission.

You can include one Netlify-provided reCAPTCHA 2 challenge per page. To use multiple challenges on one page, add [custom reCAPTCHA 2](#custom-recaptcha-2).

#### Custom reCAPTCHA 2

You can also add your own reCAPTCHA 2 code in your site and let Netlify validate that form submissions come from a human. This is useful if you want to have more control over your validations, if you use a JavaScript library to inject a CAPTCHA in your forms, or if you need more than one CAPTCHA on a page.

In this case, Netlify needs your reCAPTCHA 2 site key and secret for validating that the captcha response is correct. You can provide these values with [environment variables](/build/environment-variables/overview) in your site configuration. Use `SITE_RECAPTCHA_KEY` to set your site key, and use `SITE_RECAPTCHA_SECRET` to set the secret provided by reCAPTCHA 2.

To set up a custom reCAPTCHA:

1. [Sign up for a reCAPTCHA API key pair](http://www.google.com/recaptcha/admin) and follow the instructions for adding reCAPTCHA to your site. This typically involves adding a script before the closing `</head>` of your HTML template, and a snippet at the end of the `<form>` where you want the reCAPTCHA widget to appear.
2. Create the following environment variables for your site [using the Netlify UI, CLI, or API](/build/environment-variables/get-started/#create-variables-with-the-netlify-ui-cli-or-api):
   * A variable with the key name of `SITE_RECAPTCHA_KEY` and a value set to your reCAPTCHA API site key. If you have the option to set specific [scopes](/build/environment-variables/overview#scopes) for your environment variables, the scope must include both **Builds** and **Runtime**.
   * A variable with the key name of `SITE_RECAPTCHA_SECRET` and a value set to your reCAPTCHA API secret key. If you have the option to set specific [scopes](/build/environment-variables/overview#scopes) for your environment variables, the scope must include **Runtime**.
3. Add a `data-netlify-recaptcha="true"` attribute to the HTML form that has the custom reCAPTCHA widget.

   ```html
   <form 
     name="contact" 
     method="POST" 
     data-netlify-recaptcha="true" 
     data-netlify="true"
   >
     <!-- input fields and custom reCAPTCHA snippet -->
   </form>
   ```

The Netlify servers will check the submissions from that form, and accept them only if they include a valid `g-recaptcha-response` value.

If you [submit your form with AJAX](/manage/forms/setup#submit-javascript-rendered-forms-with-ajax), make sure the `g-recaptcha-response` field is included in the body of the POST request.  This happens automatically if you use `FormData()` to encode the body of the request.

