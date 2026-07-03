---
title: "Claiming a domain"
source: https://resend.com/docs/dashboard/domains/claim
path: docs/dashboard/domains/claim
---

Claim a domain that is already verified by another team.

When you try to add a domain that another team has already verified, Resend
blocks the creation and tells you the domain can be claimed. Claiming lets you
prove control of the domain over DNS and transfer it to your team, entirely
over the API.

## How it works

<Steps>
  <Step title="Start a claim">
    Call [Claim Domain](/docs/api-reference/domains/claim-domain) with the domain
    name. Resend creates a placeholder domain on your team and returns a
    `domain_claim` containing a TXT `record` to add to your DNS.
  </Step>

  <Step title="Add the TXT record">
    Add the returned TXT record at your DNS provider. It proves you control the
    domain.
  </Step>

  <Step title="Verify the claim">
    Call [Verify Domain Claim](/docs/api-reference/domains/verify-domain-claim).
    Resend checks the TXT record and runs ownership-safety checks before
    transferring the domain.
  </Step>

  <Step title="Track the status">
    Poll [Get Domain Claim](/docs/api-reference/domains/get-domain-claim) until the
    claim reaches `completed`.
  </Step>
</Steps>

## Claim status

| Status       | Meaning                                                 |
| ------------ | ------------------------------------------------------- |
| `pending`    | Waiting for DNS verification.                           |
| `verified`   | DNS proof accepted. The transfer is in progress.        |
| `completed`  | The domain now belongs to your team.                    |
| `blocked`    | A safety check blocked the claim. See `blocked_reason`. |
| `expired`    | The claim window passed before it completed.            |
| `superseded` | A newer claim replaced this one.                        |
| `canceled`   | The claim was canceled.                                 |
| `failed`     | The claim did not complete.                             |

When a claim is `blocked`, `blocked_reason` explains why: `grace_period`,
`recent_owner_activity`, or `pending_scheduled_emails`.

## Canceling a claim

Cancel a pending claim by deleting its placeholder domain with
[Delete Domain](/docs/api-reference/domains/delete-domain), using the `domain_id`
from the `domain_claim` object.
