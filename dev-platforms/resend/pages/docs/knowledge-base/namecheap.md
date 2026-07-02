---
title: "Namecheap"
source: https://resend.com/docs/knowledge-base/namecheap
path: docs/knowledge-base/namecheap
---

Verify your domain on Namecheap with Resend.

## Add Domain to Resend

First, log in to your [Resend Account](https://resend.com/login) and [add a domain](https://resend.com/domains).

<img alt="Domain Details" />

<Tip>
  It is [best practice to use a
  subdomain](/docs/knowledge-base/is-it-better-to-send-emails-from-a-subdomain-or-the-root-domain)
  (updates.example.com) instead of the root domain (example.com). Using a
  subdomain allows for proper reputation segmentation based on topics or purpose
  (e.g. marketing) and is especially important if receiving emails with Resend.
</Tip>

## Log in to Namecheap

1. Log in to your [Namecheap account](https://ap.www.namecheap.com).

2. Click `Manage` for the domain.

   <img alt="Domain Details" />

   <Info>You may need to expand a dropdown to see the `Manage` button.</Info>

3. Go to the `Advanced DNS` page for the domain you want to verify.

   <img alt="Domain Details" />

## Add MX SPF Record

<Warning>
  If you are changing the MX configuration from `Gmail` to `Custom MX`, you need
  to [setup new MX records for
  Gmail](https://support.google.com/a/answer/174125). If you don't setup new
  records, receiving mail in your gmail inboxes will stop.
</Warning>

Under the `Mail Settings` section, click the dropdown and select `Custom MX`:

1. Type `send` for the `Host` of the record.
2. Copy the MX Value from Resend into the `Value` field.
3. Use the `Automatic` TTL.
4. Select `Save all changes`.

<img alt="Domain Details" />

<br />

<img alt="Domain Details" />

Below is a mapping of the record fields from Resend to Namecheap:

| Namecheap | Resend   | Example Value                           |
| --------- | -------- | --------------------------------------- |
| Type      | Type     | `MX Record`                             |
| Host      | Name     | `send`                                  |
| TTL       | TTL      | `Automatic`                             |
| Value     | Content  | `feedback-smtp.us-east-1.amazonses.com` |
| -         | Priority | `10`                                    |

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

<Info>
  Namecheap does not label the `priority` column. It is the empty column after
  `Value`. Do not use the same priority for multiple records. If Priority `10`
  is already in use, try a higher value `20` or `30`.
</Info>

## Add TXT SPF Record

Under the `Host Records` section, click `Add New Record`:

1. Set the `Type` to `TXT Record`.
2. Enter `send` into the `Host` field.
3. Copy the TXT Value from Resend into the `Value` field.
4. Use the `Automatic` TTL.
5. Select `Save all changes`.

<img alt="Domain Details" />

<br />

<img alt="Domain Details" />

Below is a mapping of the record fields from Resend to Namecheap:

| Namecheap | Resend  | Example Value                         |
| --------- | ------- | ------------------------------------- |
| Type      | Type    | `TXT Record`                          |
| Host      | Name    | `send`                                |
| TTL       | TTL     | `Automatic`                           |
| Value     | Content | `"v=spf1 include:amazonses.com ~all"` |

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

## Add TXT DKIM Records

In that same `Host Records` section, click `Add New Record`.

1. Set the `Type` to `TXT Record`.
2. Enter `resend._domainkey` into the `Host` field.
3. Copy the TXT Value from Resend into the `Value` field.
4. Use the `Automatic` TTL.
5. Select `Save all changes`.

<img alt="Domain Details" />

<br />

<img alt="Domain Details" />

Below is a mapping of the record fields from Resend to Namecheap:

| Namecheap | Resend  | Example Value                |
| --------- | ------- | ---------------------------- |
| Type      | Type    | `TXT Record`                 |
| Host      | Name    | `resend._domainkey`          |
| TTL       | TTL     | `Automatic`                  |
| Value     | Content | `p=example_domain_key_value` |

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `resend._domainkey.example.com`, paste only `resend._domainkey` (or
  `resend._domainkey.subdomain` if you're using a subdomain).
</Info>

## Receiving Emails

If you want to receive emails at your domain, toggle the "Receiving" switch on the domain details page.

<img alt="Enable Receiving Emails for a verified domain" />

<Warning>
  When you enable Inbound on a domain, Resend receives *all emails* sent to that
  specific domain depending on the priority of the MX record. For this reason,
  we strongly recommend verifying a subdomain (`subdomain.example.com`) instead
  of the root domain (`example.com`). Learn more about [avoiding conflicts with
  your existing MX
  records](/docs/knowledge-base/how-do-i-avoid-conflicting-with-my-mx-records).
</Warning>

Under the `Mail Settings` section, click the dropdown and select `Custom MX`:

1. Type `inbound` (or whatever your subdomain is) for the `Host` of the record.
2. Copy the MX Value from Resend into the `Value` field.
3. Use the `Automatic` TTL.
4. Select `Save all changes`.

Below is a mapping of the record fields from Resend to Namecheap:

| Namecheap | Resend   | Example Value                          |
| --------- | -------- | -------------------------------------- |
| Type      | Type     | `MX Record`                            |
| Host      | Name     | `inbound`                              |
| TTL       | TTL      | `Automatic`                            |
| Value     | Content  | `inbound-smtp.us-east-1.amazonaws.com` |
| -         | Priority | `10`                                   |

After verifying your domain, create a webhook to process incoming emails. For help setting up a webhook, how to access email data and attachments, forward emails, and more, see [our guide on receiving emails with Resend](/docs/dashboard/receiving/introduction).

## Complete Verification

Now click [Verify DNS Records](https://resend.com/domains) on your Domain in Resend. It may take up to 72 hours to complete the verification process (often much faster).

## Troubleshooting

If your domain is not successfully verified, these are some common troubleshooting methods.

<AccordionGroup>
  <Accordion title="Resend shows my domain verification failed.">
    Review the records you added to Namecheap to rule out copy and paste errors.
  </Accordion>

  <Accordion title="It has been longer than 72 hours and my domain is still Pending.">
    [Review our guide on a domain not verifying](/docs/knowledge-base/what-if-my-domain-is-not-verifying).
  </Accordion>
</AccordionGroup>
