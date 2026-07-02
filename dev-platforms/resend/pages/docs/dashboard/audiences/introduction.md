---
title: "Your Resend Audience"
source: https://resend.com/docs/dashboard/audiences/introduction
path: docs/dashboard/audiences/introduction
---

Learn how to manage your Contacts and send personalized Broadcasts to them.

The [Audience Page](https://resend.com/audience) is for your marketing Broadcasts and provides tools for managing your Contacts and sending personalized Broadcasts to them. [Broadcasts](/docs/dashboard/broadcasts/introduction) also handle all your unsubscribe flows for you automatically.

The Audience page includes four areas:

* [Contacts](#contacts): individual email addresses
* [Properties](#properties): custom properties for your Contacts
* [Segments](#segments): groups of Contacts for your organization
* [Topics](#topics): user-facing tools for managing email preferences

<img alt="Contacts" />

## Contacts

Contacts in Resend are global entities linked to a specific email address.

<img alt="Properties" />

Each Contact:

* is associated with a single email address
* can have custom properties
* can be in zero, one or multiple Segments
* can be opted in or out of Topics

Each Contact shows a history of all marketing interactions with the Contact.

You can import Contacts in bulk from a CSV (up to 200MB) using either the [dashboard](/docs/dashboard/audiences/contacts) or the [Contacts Import API](/docs/api-reference/contacts/create-contact-import) and SDKs. Both map CSV columns to Contact Properties (the dashboard uses AI to suggest matches and create new properties for you). API and SDK imports let you choose whether to `upsert` or `skip` existing Contacts.

Learn more about [Contacts](/docs/dashboard/audiences/contacts).

## Properties

Contact Properties can be used to store additional information about your Contacts and then personalize your Broadcasts.

<img alt="Properties" />

Resend includes a few default properties:

* `first_name`: The first name of the contact.
* `last_name`: The last name of the contact.
* `unsubscribed`: Whether the contact is unsubscribed from all Broadcasts.
* `email`: The email address of the contact.

You can create additional custom Contact Properties for your Contacts to store additional information. These properties can be used to personalize your Broadcasts across all Segments.

Learn more about [Contact Properties](/docs/dashboard/audiences/properties).

## Segments

Segments are groups of Contacts for your organization. You can use Segments to send emails to a specific group of Contacts using [Broadcasts](/docs/dashboard/broadcasts/introduction).

<img alt="Segment" />

Learn more about [Segments](/docs/dashboard/segments/introduction).

## Topics

Topics are user-facing tools for managing email preferences. You can use them to manage your Contacts' email preferences.

<img alt="Topics" />

When you send [Broadcasts](/docs/dashboard/broadcasts/introduction), you can optionally scope sending to a particular Topic. Not only does scoping your sending help you send more precisely, but it also allows your users to manage their preferences with more control.

<Tip>
  New to Topics? Learn [why and when to use
  them](/docs/knowledge-base/why-use-topics), including how they improve
  deliverability and differ from Segments.
</Tip>
