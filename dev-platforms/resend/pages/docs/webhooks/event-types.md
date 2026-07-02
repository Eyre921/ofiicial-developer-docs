---
title: "Event Types"
source: https://resend.com/docs/webhooks/event-types
path: docs/webhooks/event-types
---

List of supported event types and their payload.

## Email Events

<div>
  <div>
    <div>
      <span />

      [`email.bounced`](/docs/webhooks/emails/bounced)
    </div>

    <div>
      Occurs whenever the recipient's mail server **permanently rejected the
      email**.
    </div>
  </div>

  <div>
    <div>
      <span />

      [`email.clicked`](/docs/webhooks/emails/clicked)
    </div>

    <div>
      Occurs whenever the **recipient clicks on an email link**.
    </div>
  </div>

  <div>
    <div>
      <span />

      [`email.complained`](/docs/webhooks/emails/complained)
    </div>

    <div>
      Occurs whenever the email was successfully **delivered, but the recipient
      marked it as spam**.
    </div>
  </div>

  <div>
    <div>
      <span />

      [`email.delivered`](/docs/webhooks/emails/delivered)
    </div>

    <div>
      Occurs whenever Resend **successfully delivered the email** to the
      recipient's mail server.
    </div>
  </div>

  <div>
    <div>
      <span />

      [`email.delivery_delayed`](/docs/webhooks/emails/delivery-delayed)
    </div>

    <div>
      Occurs whenever the **email couldn't be delivered due to a temporary
      issue**. Delivery delays can occur, for example, when the recipient's
      inbox is full, or when the receiving email server experiences a transient
      issue.
    </div>
  </div>

  <div>
    <div>
      <span />

      [`email.failed`](/docs/webhooks/emails/failed)
    </div>

    <div>
      Occurs whenever the **email failed to send due to an error**. This event
      is triggered when there are issues such as invalid recipients, API key
      problems, domain verification issues, email quota limits, or other sending
      failures.
    </div>
  </div>

  <div>
    <div>
      <span />

      [`email.opened`](/docs/webhooks/emails/opened)
    </div>

    <div>
      Occurs whenever the **recipient opened the email**.
    </div>
  </div>

  <div>
    <div>
      <span />

      [`email.received`](/docs/webhooks/emails/received)
    </div>

    <div>
      Occurs whenever Resend **successfully receives an email**.
    </div>
  </div>

  <div>
    <div>
      <span />

      [`email.scheduled`](/docs/webhooks/emails/scheduled)
    </div>

    <div>
      Occurs whenever the **email is scheduled to be sent**.
    </div>
  </div>

  <div>
    <div>
      <span />

      [`email.sent`](/docs/webhooks/emails/sent)
    </div>

    <div>
      Occurs whenever the **API request was successful**. Resend will attempt to
      deliver the message to the recipient's mail server.
    </div>
  </div>

  <div>
    <div>
      <span />

      [`email.suppressed`](/docs/webhooks/emails/suppressed)
    </div>

    <div>
      Occurs whenever the **email is suppressed** by Resend.
    </div>
  </div>
</div>

## Domain Events

<div>
  <div>
    <div>
      <span />

      [`domain.created`](/docs/webhooks/domains/created)
    </div>

    <div>
      Occurs when a **domain was successfully created**.
    </div>
  </div>

  <div>
    <div>
      <span />

      [`domain.updated`](/docs/webhooks/domains/updated)
    </div>

    <div>
      Occurs when a **domain was successfully updated**.
    </div>
  </div>

  <div>
    <div>
      <span />

      [`domain.deleted`](/docs/webhooks/domains/deleted)
    </div>

    <div>
      Occurs when a **domain was successfully deleted**.
    </div>
  </div>
</div>

## Contact Events

<div>
  <div>
    <div>
      <span />

      [`contact.created`](/docs/webhooks/contacts/created)
    </div>

    <div>
      Occurs whenever a **contact was successfully created**.
    </div>

    <div>
      *Note: When importing multiple contacts using CSV, these events won't be
      triggered. [Contact support](https://resend.com/contact) if you have any
      questions.*
    </div>
  </div>

  <div>
    <div>
      <span />

      [`contact.updated`](/docs/webhooks/contacts/updated)
    </div>

    <div>
      Occurs whenever a **contact was successfully updated**.
    </div>
  </div>

  <div>
    <div>
      <span />

      [`contact.deleted`](/docs/webhooks/contacts/deleted)
    </div>

    <div>
      Occurs whenever a **contact was successfully deleted**.
    </div>
  </div>
</div>
