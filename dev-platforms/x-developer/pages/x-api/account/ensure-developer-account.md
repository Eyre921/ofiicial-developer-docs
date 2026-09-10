---
title: "Ensure developer account"
source: https://docs.x.com/x-api/account/ensure-developer-account
path: x-api/account/ensure-developer-account
---

post /2/account
Creates an X Developer Platform account for the authenticated user if they do not already have one, and returns it. Idempotent: when the user already has an account it is returned unchanged with `created` false.
