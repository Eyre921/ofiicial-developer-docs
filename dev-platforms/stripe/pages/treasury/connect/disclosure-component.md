---
title: "Treasury disclosure component"
source: https://docs.stripe.com/treasury/connect/disclosure-component.md
path: treasury/connect/disclosure-component
---

# Treasury disclosure component

Embed a Treasury disclosure component directly onto your website.

You can embed the Treasury disclosure component directly on your website to automatically display currently [compliant](https://docs.stripe.com/treasury/connect/compliance.md) disclosure information without requiring future code changes. Stripe updates the content rendered by the component to reflect legislation and banking partner updates.

> Contact [Treasury support](mailto:treasury-support@stripe.com) to enable the Treasury disclosure component.
![The footer of the furever.dev website with the disclosure component included](https://b.stripecdn.com/docs-statics-srv/assets/disclosure-component.39ddf9371de52e1639f9e72de894f60c.png)

An example of what the disclosure component would look like added to the footer of our furever.dev demo website.

## Create and mount the Treasury disclosure component

#### HTML + JS

To embed the disclosure component, you need to include [Stripe.js](https://docs.stripe.com/js/including) on your website.

1. Add the Stripe.js script onto your page by adding it to the `head` of your HTML file:

   ```html
   <script src="https://js.stripe.com/endive/stripe.js"></script>
   ```

2. Create a placeholder element on your page where you want to mount the Treasury disclosure element:

   ```html
   <div id="treasury-disclosure"></div>
   ```

3. On pages that mention Treasury on your site, include the following code to create an instance of Stripe.js and mount the Treasury disclosure element:

   ```javascript
   const stripe = Stripe('<<YOUR_PUBLISHABLE_KEY>>');
   
   const options = {
     businessName: 'Your Business Name',
     learnMoreLink: 'https://docs.stripe.com/treasury/connect',
   };
   const {htmlElement: treasuryDisclosure, error} =
     await stripe.createTreasuryDisclosure(options);
   
   if (error) {
     // Handle the error in any way you see fit.
     console.error(error);
   } else {
     document
       .getElementById('treasury-disclosure')
       .appendChild(treasuryDisclosure);
   }
   ```

| Parameter       | Description                                                                                                                                                         | Default value                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| `businessName`  | (optional) `string`

     The name of your business as you want it to appear in the disclosure text.                                                                | The name of your business as it appears on Stripe |
| `learnMoreLink` | (optional) `string`

     A supplemental link for your users to learn more about the Treasury product or any other relevant information included in the disclosure. | None                                              |

   **Component styling**

   The HTML element we render contains `<div>`, `<p>`, and `<a>` tags. You can target the `treasury-disclosure` ID attribute to style the inner elements to match the other content on your webpage.

#### React

To embed the disclosure component, you need to include [Stripe.js](https://docs.stripe.com/js/including) on your website.

1. Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry.

   ```bash
   npm install --save @stripe/react-stripe-js @stripe/stripe-js
   ```

2. On pages that mention Treasury on your site, include the `TreasuryDisclosure` component:

   ```jsx
   import {TreasuryDisclosure} from '@stripe/react-stripe-js';
   import {loadStripe} from '@stripe/stripe-js';
   
   const stripe = loadStripe('<<YOUR_PUBLISHABLE_KEY>>');
   {/* ... */}
   <TreasuryDisclosure
     stripe={stripe}
     options={{
       businessName: 'Your Business Name',
       learnMoreLink: 'https://docs.stripe.com/treasury/connect',
     }}
   />
   ```

| Prop            | Description                                                                                                                                                         | Default value                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| `businessName`  | (optional) `string`

     The name of your business as you want it to appear in the disclosure text.                                                                | The name of your business as it appears on Stripe |
| `learnMoreLink` | (optional) `string`

     A supplemental link for your users to learn more about the Treasury product or any other relevant information included in the disclosure. | None                                              |
| `onLoad`        | (optional) `() => void`

     Triggered after the component loads.                                                                                                  | None                                              |
| `onError`       | (optional) `(error: Object) => void`

     Triggered when the component fails to load.                                                                              | None                                              |

   **Component styling**

   The React component we render contains `<div>`, `<p>`, and `<a>` tags. You can wrap the resulting component in a new ID or class attribute and style the inner elements to match the other content on your webpage.

