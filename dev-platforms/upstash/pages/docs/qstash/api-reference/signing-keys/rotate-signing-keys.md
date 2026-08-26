---
title: "Rotate Signing Keys"
source: https://upstash.com/docs/qstash/api-reference/signing-keys/rotate-signing-keys
path: docs/qstash/api-reference/signing-keys/rotate-signing-keys
---

> Rotate your signing keys

`POST /v2/keys/rotate`

Rotating signing keys lets you switch the keys used to sign messages without causing downtime.
This ensures that signatures remain valid and that the application can continue verifying new messages seamlessly.

During a rotation, the next key becomes the new current key, and a fresh next key is generated.

Make sure to update your application to use the new current and next keys after rotation.
