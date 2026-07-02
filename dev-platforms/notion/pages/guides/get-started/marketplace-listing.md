---
title: "List on the Marketplace"
source: https://developers.notion.com/guides/get-started/marketplace-listing
path: guides/get-started/marketplace-listing
---

Learn how to list your public connection on the Notion Marketplace.

The [Notion Marketplace](https://www.notion.so/integrations/all) is how Notion users discover and connect public connections. Listing your connection there puts it in front of every Notion user — and it's a separate step from building the connection itself, so you can ship whenever you're ready.

This guide assumes you already have a public connection. If you haven't created one yet, see the [Public connections](/guides/get-started/public-connections) guide first.

This guide covers how to:

* Start a new Marketplace listing
* Submit your listing for review
* Understand the review process and timeline

<Note>
  Only public connections with an installation scope of **Any workspace** can be listed on the Marketplace. Internal connections and **Selected workspaces only** public connections are not eligible. Installation scope is set when the connection is created and can't be changed afterward — see [Installation scope](/guides/get-started/public-connections#installation-scope).
</Note>

## Start a new listing

<Steps>
  <Step>
    Navigate to the <a href={marketplaceListingsUrl}>Marketplace listing dashboard</a>.
  </Step>

  <Step>
    In the **Listings** section of the sidebar, select **Connections**.
  </Step>

  <Step>
    Under **Drafts**, click **Start a new connection listing**.
  </Step>

  <Step>
    Fill in the listing details, including:

    * Listing name and description
    * Category and tags
    * Listing images and logo
    * The public connection to associate with this listing
  </Step>

  <Step>
    Save your listing as a draft. You can return to edit it at any time before submitting.
  </Step>
</Steps>

## Submit for review

When your listing is ready, submit it for review from the **Connections** listing page.

<Steps>
  <Step>
    From the **Listings > Connections** page, find your draft listing.
  </Step>

  <Step>
    Review all listing details to ensure they are complete and accurate.
  </Step>

  <Step>
    Submit your listing for review by the Notion team.
  </Step>
</Steps>

After submission, your listing moves to the **Submitted** section where you can track its review status.

## Review process

The Notion team reviews every listing submission. Track the status of your submission from the **Listings > Connections** page in the Marketplace listing dashboard. See the [FAQ](#frequently-asked-questions) below for review timelines.

If approved, the listing appears in the [Notion Marketplace](https://www.notion.so/integrations/all). If changes are required, the Notion team sends feedback and you can resubmit after making updates.

## Connection gallery best practices

For guidance on the review process and best practices to get your connection approved, check out the [Notion Connection Gallery Best Practices](https://www.notion.so/notiondevs/Notion-Integration-Gallery-Best-Practices-997825927fd6473e89617ce0c329145c?pvs=4) guide.

## Frequently asked questions

<AccordionGroup>
  <Accordion title="How long will it take for Notion to publish my submitted connection?">
    After submission, expect to hear back from our team within 5-10 business days via email. Check the status of your connection submission from the **Listings > Connections** page in the Marketplace listing dashboard.
  </Accordion>

  <Accordion title="What if my connection doesn't meet the requirements?">
    The Notion team sends an email explaining why your listing was not approved. Check the status from the **Listings > Connections** page.
  </Accordion>

  <Accordion title="What if my connection is rejected?">
    Connections are rejected for various reasons, from brand/trademark issues to quality concerns to situations where the baseline connection criteria isn't met. We encourage developers to review our feedback, make necessary changes, and resubmit. Our goal is to help you create high-quality and valuable tools for the Notion community.
  </Accordion>

  <Accordion title="Do I need to list my public connection on the Marketplace?">
    No. Public connections work independently of Marketplace listings. Listing on the Marketplace is optional and helps your connection reach a wider audience, but your connection can be used via its OAuth flow without being listed.
  </Accordion>

  <Accordion title="Can you point me to other helpful resources?">
    <CardGroup>
      <Card title="Notion Developers" icon="angles-right" href="/" />

      <Card title="Overview" icon="angles-right" href="/guides/get-started/overview" />

      <Card title="Create connections with the Notion API" icon="angles-right" href="https://www.notion.so/help/create-integrations-with-the-notion-api" />

      <Card title="Authorization guide" icon="angles-right" href="/guides/get-started/authorization" />
    </CardGroup>
  </Accordion>
</AccordionGroup>
