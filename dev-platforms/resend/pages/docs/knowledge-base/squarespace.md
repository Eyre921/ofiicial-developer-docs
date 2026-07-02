---
title: "Squarespace"
source: https://resend.com/docs/knowledge-base/squarespace
path: docs/knowledge-base/squarespace
---

Verify your domain on Squarespace with Resend.

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

## Log in to Squarespace

Log in to your [Squarespace domains page](https://account.squarespace.com/domains) and click on your domain.

<img alt="Domain Details" />

## Add MX SPF Record

Scroll down to the **Custom records** section and select `Add record` on Squarespace.

1. Type `send` for the `Host` of the record.
2. Set the `Type` to `MX`.
3. Set the `Priority` to `10`.
4. Use the Default 4 hours for `TTL`.
5. Copy the MX Value from Resend into the `Mail Server` field
6. Select `Save`.

<img alt="Domain Details" />

<img alt="Domain Details" />

Below is a mapping of the record fields from Resend to Squarespace:

| Squarespace | Resend   | Example Value                           |
| ----------- | -------- | --------------------------------------- |
| Type        | Type     | `MX`                                    |
| Host        | Name     | `send`                                  |
| TTL         | TTL      | `4 hrs` (default)                       |
| Mail Server | Content  | `feedback-smtp.us-east-1.amazonses.com` |
| Priority    | Priority | `10`                                    |

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

<Info>
  Do not use the same priority for multiple records. If Priority `10` is already
  in use, try a higher value `20` or `30`.
</Info>

## Add TXT SPF Record

In the same **Custom records** section, select `Add Record` on Squarespace.

1. Type `send` for the `Host` of the record.
2. Set the `Type` to `TXT`.
3. Use the Default 4 hours for `TTL`.
4. Copy the TXT Value from Resend into the `Text` field
5. Select `Save`.

Add the **TXT Record** from your domain in Resend to Squarespace and click "Save".

<img alt="Domain Details" />

<br />

<img alt="Domain Details" />

Below is a mapping of the record fields from Resend to Squarespace:

| Squarespace | Resend  | Example Value                         |
| ----------- | ------- | ------------------------------------- |
| Type        | Type    | `TXT`                                 |
| Host        | Name    | `send`                                |
| TTL         | TTL     | `4 hrs` (default)                     |
| Text        | Content | `"v=spf1 include:amazonses.com ~all"` |

<Info>
  Omit your domain from the record values in Resend when you paste. Instead of
  `send.example.com`, paste only `send` (or `send.subdomain` if you're using a
  subdomain).
</Info>

## Add TXT DKIM Records

In the same **Custom records** section, select `Add Record` on Squarespace.

1. Type `resend._domainkey` for the `Host` of the record.
2. Set the `Type` to `TXT`.
3. Use the Default 4 hours for `TTL`.
4. Copy the TXT Value from Resend into the `Text` field
5. Select `Save`.

<img alt="Domain Details" />

<img alt="Domain Details" />

Below is a mapping of the record fields from Resend to Squarespace:

| Squarespace | Resend  | Example Value                |
| ----------- | ------- | ---------------------------- |
| Type        | Type    | `TXT`                        |
| Host        | Name    | `resend._domainkey`          |
| TTL         | TTL     | `4 hrs` (default)            |
| Text        | Content | `p=example_domain_key_value` |

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

Scroll down to the **Custom records** section and select `Add record` on Squarespace:

1. Type `inbound` (or whatever your subdomain is) for the `Host` of the record.
2. Set the `Type` to `MX`.
3. Set the `Priority` to `10`.
4. Use the Default 4 hours for `TTL`.
5. Copy the MX Value from Resend into the `Mail Server` field.
6. Select `Save`.

Below is a mapping of the record fields from Resend to Squarespace:

| Squarespace | Resend   | Example Value                          |
| ----------- | -------- | -------------------------------------- |
| Type        | Type     | `MX`                                   |
| Host        | Name     | `inbound`                              |
| TTL         | TTL      | `4 hrs` (default)                      |
| Mail Server | Content  | `inbound-smtp.us-east-1.amazonaws.com` |
| Priority    | Priority | `10`                                   |

After verifying your domain, create a webhook to process incoming emails. For help setting up a webhook, how to access email data and attachments, forward emails, and more, see [our guide on receiving emails with Resend](/docs/dashboard/receiving/introduction).

## Complete Verification

Now click [Verify DNS Records](https://resend.com/domains) on your Domain in Resend. It may take up to 72 hours to complete the verification process (often much faster).

## Troubleshooting

If your domain is not successfully verified, these are some common troubleshooting methods.

<AccordionGroup>
  <Accordion title="Resend shows my domain verification failed.">
    Review the records you added to Squarespace to rule out copy and paste errors.
  </Accordion>

  <Accordion title="It has been longer than 72 hours and my domain is still Pending.">
    [Review our guide on a domain not verifying](/docs/knowledge-base/what-if-my-domain-is-not-verifying).
  </Accordion>
</AccordionGroup>
