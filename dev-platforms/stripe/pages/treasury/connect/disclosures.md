---
title: "Compliance disclosures"
source: https://docs.stripe.com/treasury/connect/disclosures.md
path: treasury/connect/disclosures
---

# Compliance disclosures

Embed Treasury and Issuing disclosure components directly on your website.

Use Stripe’s disclosure components to display current compliance information for your Treasury and Issuing programs.

## Treasury disclosure component

You can embed the Treasury disclosure component directly on your website to automatically display currently [compliant](https://docs.stripe.com/treasury/connect/compliance.md) disclosure information without requiring future code changes. Stripe updates the content rendered by the component to reflect legislation and banking partner updates.
![The footer of the furever.dev website with the disclosure component included](https://b.stripecdn.com/docs-statics-srv/assets/disclosure-component.39ddf9371de52e1639f9e72de894f60c.png)

An example of what the disclosure component would look like added to the footer of our furever.dev demo website.

### Create and mount the Treasury disclosure component

#### HTML + JS

To embed the disclosure component, you need to include [Stripe.js](https://docs.stripe.com/js/including) on your website.

1. Add the Stripe.js script onto your page by adding it to the `head` of your HTML file:

   ```html
   <script src="https://js.stripe.com/dahlia/stripe.js"></script>
   ```

2. Create a placeholder element on your page where you want to mount the Treasury disclosure element:

   ```html
   <div id="financial-account-disclosure"></div>
   ```

3. On pages that mention Treasury on your site, include the following code to create an instance of Stripe.js and mount the Treasury disclosure element:

   ```javascript
   const stripe = Stripe('<<YOUR_PUBLISHABLE_KEY>>');
   
   const options = {
     businessName: 'Your Business Name',
     learnMoreLink: 'https://docs.stripe.com/financial-accounts/connect',
   };
   const {htmlElement: financialAccountDisclosure, error} =
     await stripe.createFinancialAccountDisclosure(options);
   
   if (error) {
     // Handle the error in any way you see fit.
     console.error(error);
   } else {
     document
       .getElementById('financial-account-disclosure')
       .appendChild(financialAccountDisclosure);
   }
   ```

| Parameter       | Description                                                                                                                                                                  | Default value                                     |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| `businessName`  | (optional) `string`

     The name of your business as you want it to appear in the disclosure text.                                                                         | The name of your business as it appears on Stripe |
| `learnMoreLink` | (optional) `string`

     A supplemental link for your users to learn more about the Financial Account product or any other relevant information included in the disclosure. | None                                              |

   **Component styling**

   The HTML element we render contains `<div>`, `<p>`, and `<a>` tags. You can target the `financial-account-disclosure` ID attribute to style the inner elements to match the other content on your webpage.

#### React

To embed the disclosure component, you need to include [Stripe.js](https://docs.stripe.com/js/including) on your website.

1. Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry.

   ```bash
   npm install --save @stripe/react-stripe-js @stripe/stripe-js
   ```

2. On pages that mention Treasury on your site, include the `FinancialAccountDisclosure` component:

   ```jsx
   import {FinancialAccountDisclosure} from '@stripe/react-stripe-js';
   import {loadStripe} from '@stripe/stripe-js';
   
   const stripe = loadStripe('<<YOUR_PUBLISHABLE_KEY>>');
   {/* ... */}
   <FinancialAccountDisclosure
     stripe={stripe}
     options={{
       businessName: 'Your Business Name',
       learnMoreLink: 'https://docs.stripe.com/treasury/connect',
     }}
   />
   ```

| Prop            | Description                                                                                                                                                                  | Default value                                     |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| `businessName`  | (optional) `string`

     The name of your business as you want it to appear in the disclosure text.                                                                         | The name of your business as it appears on Stripe |
| `learnMoreLink` | (optional) `string`

     A supplemental link for your users to learn more about the Financial Account product or any other relevant information included in the disclosure. | None                                              |
| `onLoad`        | (optional) `() => void`

     Triggered after the component loads.                                                                                                           | None                                              |
| `onError`       | (optional) `(error: Object) => void`

     Triggered when the component fails to load.                                                                                       | None                                              |

   **Component styling**

   The React component we render contains `<div>`, `<p>`, and `<a>` tags. You can wrap the resulting component in a new ID or class attribute and style the inner elements to match the other content on your webpage.

## Issuing disclosure component

To meet compliance regulations and provide transparency to your cardholders, you must disclose information about the Stripe Issuing product on your website to any current or potential cardholders. The disclosure must include information about the product, the issuing bank partner, and the card network.

Because the disclosure information can change, we provide you with a UI element that you can embed directly on your website using Stripe.js (instead of giving you static text). If bank partners or card program details change in the future, this component automatically updates to reflect the latest disclosure information without requiring future code changes.
![The footer of the furever.dev website with the disclosure component included](https://b.stripecdn.com/docs-statics-srv/assets/disclosure-component.9483c39f893105543aeb62f6339352a1.png)

An example of what the disclosure component would look like added to the footer of our furever.dev demo website.

### Create and mount the Issuing disclosure component

#### HTML + JS

To embed the disclosure component, you need to include [Stripe.js](https://docs.stripe.com/js/including) on your website.

1. Add the Stripe.js script onto your page by adding it to the `head` of your HTML file:

   ```html
   <script src="https://js.stripe.com/dahlia/stripe.js"></script>
   ```

2. Create a placeholder element on your page where you want to mount the Issuing disclosure element:

   ```html
   <div id="issuing-disclosure"></div>
   ```

3. On pages that mention Issuing on your site, include the following code to create an instance of Stripe.js and mount the Issuing disclosure element:

   ```javascript
   const stripe = Stripe('<<YOUR_PUBLISHABLE_KEY>>');
   
   const options = {
     issuingProgramID: 'iprg_123',
     publicCardProgramName: 'Your Card Program Name',
     learnMoreLink: 'https://docs.stripe.com/issuing',
   };
   const {htmlElement: issuingDisclosure, error} =
     await stripe.createIssuingDisclosure(options);
   
   if (error) {
     // Handle the error in any way you see fit.
     console.error(error);
   } else {
     document
       .getElementById('issuing-disclosure')
       .appendChild(issuingDisclosure);
   }
   ```

| Parameter               | Description                                                                                                                                                                                                                                                                    | Default value                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| `issuingProgramID`      | `string`

     The ID of the [Issuing card program](https://docs.stripe.com/api/issuing/programs/object.md) you want to display the disclosure for. You must provide it if you want to display the disclosure for a card program other than your default Issuing card program. | Your default Issuing card program                 |
| `publicCardProgramName` | `string`

     The public name of the Issuing card program as you want it to appear in the disclosure text. If you haven’t set a business name within Stripe, you need to provide a value for `publicCardProgramName`.                                                         | The name of your business as it appears on Stripe |
| `learnMoreLink`         | (optional) `string`

     A supplemental link for your cardholders to learn more about the Issuing product or any other relevant information included in the disclosure.                                                                                                       | None                                              |

   **Component styling**

   The HTML element we render contains `<div>`, `<p>`, and `<a>` tags. You can target the `issuing-disclosure` ID attribute to style the inner elements to match the other content on your webpage.

#### React

To embed the disclosure component, you need to include [Stripe.js](https://docs.stripe.com/js/including) on your website.

1. Install [React Stripe.js](https://www.npmjs.com/package/@stripe/react-stripe-js) and the [Stripe.js loader](https://www.npmjs.com/package/@stripe/stripe-js) from the npm public registry.

   ```bash
   npm install --save @stripe/react-stripe-js @stripe/stripe-js
   ```

2. On pages that mention Issuing on your site, include the `IssuingDisclosure` component:

   ```jsx
   import {IssuingDisclosure} from '@stripe/react-stripe-js';
   import {loadStripe} from '@stripe/stripe-js';
   
   const stripe = loadStripe('<<YOUR_PUBLISHABLE_KEY>>');
   {/* ... */}
   <IssuingDisclosure
     stripe={stripe}
     options={{
       issuingProgramID: 'icp_1234567890',
       publicCardProgramName: 'Your Card Program Name',
       learnMoreLink: 'https://docs.stripe.com/issuing',
     }}
   />
   ```

| Prop                    | Description                                                                                                                                                                                                                                                                    | Default value                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| `issuingProgramID`      | `string`

     The ID of the [Issuing card program](https://docs.stripe.com/api/issuing/programs/object.md) you want to display the disclosure for. You must provide it if you want to display the disclosure for a card program other than your default Issuing card program. | Your default Issuing card program                 |
| `publicCardProgramName` | `string`

     The public name of the Issuing card program as you want it to appear in the disclosure text. If you haven’t set a business name within Stripe, you need to provide a value for `publicCardProgramName`.                                                         | The name of your business as it appears on Stripe |
| `learnMoreLink`         | (optional) `string`

     A supplemental link for your cardholders to learn more about the Issuing product or any other relevant information included in the disclosure.                                                                                                       | None                                              |
| `onLoad`                | (optional) `() => void`

     Triggered after the component loads.                                                                                                                                                                                                             | None                                              |
| `onError`               | (optional) `(error: Object) => void`

     Triggered when the component fails to load.                                                                                                                                                                                         | None                                              |

   **Component styling**

   The React component we render contains `<div>`, `<p>`, and `<a>` tags. You can wrap the resulting component in a new ID or class attribute and style the inner elements to match the other content on your webpage.

