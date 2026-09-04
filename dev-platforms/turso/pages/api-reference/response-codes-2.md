---
title: "Errors"
source: https://docs.turso.tech/api-reference/response-codes
path: api-reference/response-codes
---

The Turso API will respond with an HTTP status code, and in the event of an error, return an error message in the response body.

| Code  | Description                                                      |
| ----- | ---------------------------------------------------------------- |
| `200` | `OK` — Successful request                                        |
| `401` | `Unauthorized` — Invalid or expired auth token                   |
| `402` | `Payment required` — Check you have an active subscription       |
| `403` | `Forbidden` — You do not have permission to access this resource |
| `409` | `Conflict` — Resource already exists                             |
