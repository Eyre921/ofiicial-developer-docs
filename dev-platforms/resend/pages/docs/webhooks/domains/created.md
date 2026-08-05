---
title: "domain.created"
source: https://resend.com/docs/webhooks/domains/created
path: docs/webhooks/domains/created
---

Received when a domain is created.

Event triggered when a **domain was successfully created**.

<Info>
  If you're having issues verifying your domain, [review our guide on a domain
  not verifying](/docs/knowledge-base/what-if-my-domain-is-not-verifying) for
  troubleshooting steps.
</Info>

<ResponseBodyParameters type="domain.created">
  <ParamField type="string">
    Unique identifier for the domain
  </ParamField>

  <ParamField type="string">
    Domain name (e.g., `example.com`)
  </ParamField>

  <ParamField type="verified | partially_verified | partially_failed | failed | pending | not_started">
    Current verification status of the domain:

    * `verified`: The domain is verified and can be used to send or receive emails.
    * `partially_verified`: One capability (send or receive) is verified while the other is still pending verification.
    * `partially_failed`: The domain is verified but one of the features (send or receive) is not verified.
    * `pending`: The domain is pending verification and cannot be used to send or receive emails.
    * `not_started`: Verification has not started yet, so the domain cannot be used to send or receive emails.
    * `failed`: The domain failed verification.

    <Note>
      The `data.status` field represents an aggregated status of the domain. For
      domains that can both [send](/docs/dashboard/emails/introduction) and
      [receive](/docs/dashboard/receiving/introduction) emails, the status may be
      `partially_verified` (one capability verified, the other pending) or
      `partially_failed` (one capability verified, the other failed).
    </Note>
  </ParamField>

  <ParamField type="string">
    ISO 8601 timestamp when the domain was created
  </ParamField>

  <ParamField type="us-east-1 | eu-west-1 | sa-east-1 | ap-northeast-1">
    AWS region where the domain is configured.
  </ParamField>

  <ParamField type="object">
    Domain capabilities for sending and receiving emails.

    <Expandable title="properties">
      <ParamField type="enabled | disabled">
        Whether the domain can be used to send emails.
      </ParamField>

      <ParamField type="enabled | disabled">
        Whether the domain can be used to receive emails.
      </ParamField>
    </Expandable>
  </ParamField>

  <ParamField type="array">
    Array of DNS record objects required for domain verification

    <Expandable title="record object">
      <ParamField type="SPF | DKIM | Receiving MX | Tracking">
        Record type purpose. Learn more about [domain verification records](/docs/dashboard/domains/introduction).
      </ParamField>

      <ParamField type="string">
        DNS record name/subdomain
      </ParamField>

      <ParamField type="MX | TXT | CNAME">
        DNS record type
      </ParamField>

      <ParamField type="string">
        DNS record value to be set
      </ParamField>

      <ParamField type="string">
        Time to live for the DNS record
      </ParamField>

      <ParamField type="string">
        Verification status of this specific record
      </ParamField>

      <ParamField type="number">
        Priority value for MX records (optional)
      </ParamField>
    </Expandable>
  </ParamField>
</ResponseBodyParameters>

<ResponseExample>
  ```json theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "type": "domain.created",
    "created_at": "2026-11-17T19:32:22.980Z",
    "data": {
      "id": "d91cd9bd-1176-453e-8fc1-35364d380206",
      "name": "example.com",
      "status": "not_started",
      "created_at": "2026-04-26T20:21:26.347Z",
      "region": "us-east-1",
      "capabilities": {
        "sending": "enabled",
        "receiving": "disabled"
      },
      "records": [
        {
          "record": "SPF",
          "name": "send",
          "type": "MX",
          "ttl": "Auto",
          "status": "not_started",
          "value": "feedback-smtp.us-east-1.amazonses.com",
          "priority": 10
        },
        {
          "record": "SPF",
          "name": "send",
          "value": "\"v=spf1 include:amazonses.com ~all\"",
          "type": "TXT",
          "ttl": "Auto",
          "status": "not_started"
        },
        {
          "record": "DKIM",
          "name": "resend._domainkey",
          "value": "p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDsc4Lh8xilsngyKEgN2S84+21gn+x6SEXtjWvPiAAmnmggr5FWG42WnqczpzQ/mNblqHz4CDwUum6LtY6SdoOlDmrhvp5khA3cd661W9FlK3yp7+jVACQElS7d9O6jv8VsBbVg4COess3gyLE5RyxqF1vYsrEXqyM8TBz1n5AGkQIDAQA2",
          "type": "TXT",
          "status": "not_started",
          "ttl": "Auto"
        }
      ]
    }
  }
  ```
</ResponseExample>
