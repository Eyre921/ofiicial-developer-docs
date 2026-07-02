---
title: "Oxygen"
source: https://shopify.dev/docs/storefronts/headless/hydrogen/getting-started.md
path: docs/storefronts/headless/hydrogen/getting-started
---

---
title: Getting started with Hydrogen and Oxygen
description: >-
  Learn how to create a new Hydrogen storefront, run it locally, connect it to a
  Shopify store, and deploy it to Oxygen hosting.
source_url:
  html: 'https://shopify.dev/docs/storefronts/headless/hydrogen/getting-started'
  md: 'https://shopify.dev/docs/storefronts/headless/hydrogen/getting-started.md'
api_name: hydrogen
---

# Getting started with Hydrogen and Oxygen

This tutorial will walk you through the process of creating a new Hydrogen storefront, linking it to your Shopify store, and then deploying it to Oxygen.

#### Requirements

* [Node.js v16.20+](https://nodejs.org/) and [npm v8.19+](https://www.npmjs.com/)
* [Hydrogen channel](https://apps.shopify.com/hydrogen)

***

## Step 1: Create a new Hydrogen storefront

In your terminal, create a new Hydrogen project using example data from [Mock.shop](https://mock.shop):

## Terminal

```text
npm create @shopify/hydrogen@latest -- --quickstart
```

**Note:**

The `--quickstart` flag is shorthand for a set of [recommended options](https://shopify.dev/docs/api/shopify-cli/hydrogen/hydrogen-init#flags-propertydetail-quickstart) for trying Hydrogen. You can drop it to see the available customizations.

You'll see a confirmation message with some details about your new project:

## Output

```text
Shopify:   Mock.shop
Language:  JavaScript
Routes:
  • Home (/ & /:catchAll)
  • Page (/pages/:handle)
  • Cart (/cart/* & /discount/*)
  • Products (/products/:handle)
  • Collections (/collections & /collections/:handle)
  • Policies (/policies & /policies/:handle)
  • Blogs (/blogs/*)
  • Account (/account/*)
  • Search (/api/predictive-search & /search)
  • Robots (/robots.txt)
  • Sitemap (/sitemap.xml)
```

***

## Step 2: Run the dev server

After installation, open your new project and start the dev server:

## Terminal

```text
cd hydrogen-quickstart
shopify hydrogen dev
```

Once the dev server is running, open <http://localhost:3000> in your browser and you'll see [Mock.shop](https://mock.shop) inventory:

![A Hydrogen storefront showing example data from Mock.shop](https://shopify.dev/assets/assets/images/custom-storefronts/hydrogen/mockshop-screenshot-CwtXGip4.png)

***

## Step 3: Link your Hydrogen project to Shopify

By default, your Hydrogen project displays example products from [Mock.shop](https://mock.shop). To show your own products, link your local project to Shopify, create a new storefront, and sync your environment variables.

1. Link your Hydrogen project to Shopify:

   ## Terminal

   ```text
   npx shopify hydrogen link
   ```

   Follow the prompts to log in to your Shopify account and create a new storefront:

   ## Output

   ```text
   ✓  my-shopify-store


       ?  Select a Hydrogen storefront to link:
       ✓  Create a new storefront


       ?  New storefront name:
       >  hydrogen-quickstart
   ```

2. Update your project's environment variables:

   ## Terminal

   ```text
   npx shopify hydrogen env pull
   ```

   Your terminal will show a diff like this:

   ## Output

   ```text
   - SESSION_SECRET="foobar"
       - PUBLIC_STORE_DOMAIN="mock.shop"
       + PUBLIC_STOREFRONT_ID=[ID]
       + PUBLIC_STOREFRONT_API_TOKEN=[TOKEN]
       + PRIVATE_STOREFRONT_API_TOKEN=[TOKEN]
       + PUBLIC_CUSTOMER_ACCOUNT_API_CLIENT_ID=[ID]
       + PUBLIC_CUSTOMER_ACCOUNT_API_URL=https://shopify.com/[ID]
   ```

To confirm that the link works, run `npm run dev` and open <http://localhost:3000>. You'll now see your storefront inventory in your browser:

![A Hydrogen storefront showing data from shopify](https://shopify.dev/assets/assets/images/custom-storefronts/hydrogen/hydrogen-store-screenshot-BXy7MtyH.png)

***

## Step 4: Deploy to Oxygen

After your Hydrogen storefront is linked, you can deploy it to Oxygen hosting to make it publicly accessible:

1. Deploy your project to Oxygen:

   ## Terminal

   ```text
   npx shopify hydrogen deploy
   ```

2. At the prompt to pick which environment to deploy to, select **Preview**.

The Hydrogen CLI builds your storefront, creates a new Oxygen deployment, and returns a preview link in your terminal. Open the preview link in your browser see deployment URL:

![A Hydrogen storefront deployment URL on oxygen](https://shopify.dev/assets/assets/images/custom-storefronts/hydrogen/hydrogen-store-deployment-B5rE-XTf.png)

***

## Next steps

Congratulations! You've created a new Hydrogen storefront, connected it to Shopify, and made your first deployment to Oxygen.

[Hydrogen and Oxygen fundamentals\
\
](https://shopify.dev/docs/storefronts/headless/hydrogen/fundamentals)

[Explore the key components of the Hydrogen and Oxygen stack and how they work together](https://shopify.dev/docs/storefronts/headless/hydrogen/fundamentals)

***

