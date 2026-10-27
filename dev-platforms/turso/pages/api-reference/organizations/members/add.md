---
title: "Add Member"
source: https://docs.turso.tech/api-reference/organizations/members/add
path: api-reference/organizations/members/add
---

POST /v1/organizations/{organizationSlug}/members
Add an existing Turso user to an organization.

> [!NOTE]
>
> If you want to add someone who is not a registered Turso user, you can [create an invite](/api-reference/organizations/invites/create) instead.

> [!NOTE]
>
> You must be an `owner` or `admin` to add other members. **You can only add users to a team and not your personal account.**
