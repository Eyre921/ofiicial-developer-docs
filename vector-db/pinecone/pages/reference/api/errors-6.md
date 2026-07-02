---
title: "Errors"
source: https://docs.pinecone.io/reference/api/errors
path: reference/api/errors
---

Pinecone REST API: Pinecone uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the range.

Pinecone uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the `2xx` range indicate success, codes in the `4xx` range indicate an error that failed given the information provided, and codes in the `5xx` range indicate an error with Pinecone's servers.

For guidance on handling errors in production, see [Error handling](/guides/production/error-handling).

## 200 - OK

The request succeeded.

## 201 - CREATED

The request succeeded and a new resource was created.

## 202 - NO CONTENT

The request succeeded, but there is no content to return.

## 400 - INVALID ARGUMENT

The request failed due to an invalid argument.

## 401 - UNAUTHENTICATED

The request failed due to a missing or invalid [API key](/guides/projects/understanding-projects#api-keys).

## 402 - PAYMENT REQUIRED

The request failed due to delinquent payment or account deactivation for non-payment. See [Account deactivation for non-payment](/guides/organizations/manage-billing/non-payment-account-deactivation).

## 403 - FORBIDDEN

The request failed due to an exceeded [quota](/reference/api/database-limits#object-limits) or [index deletion protection](/guides/manage-data/manage-indexes#configure-deletion-protection).

## 404 - NOT FOUND

The request failed because the resource was not found.

## 409 - ALREADY EXISTS

The request failed because the resource already exists.

## 412 - FAILED PRECONDITIONS

The request failed due to preconditions not being met. |

## 422 - UNPROCESSABLE ENTITY

The request failed because the server was unable to process the contained instructions.

## 429 - TOO MANY REQUESTS

The request was [rate-limited](/reference/api/database-limits#rate-limits). [Implement retry logic with exponential backoff](/guides/production/error-handling#handle-rate-limits-429) to handle this error.

## 500 - UNKNOWN

An internal server error occurred. [Implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic) to handle transient errors.

## 502 - BAD GATEWAY

The API gateway received an invalid response from a backend service. This is typically a temporary error. [Implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic) to handle transient errors.

## 503 - UNAVAILABLE

The server is currently unavailable. [Implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic) to handle transient errors.

## 504 - GATEWAY TIMEOUT

The API gateway did not receive a timely response from the backend server. This can occur due to slow requests or backend processing delays. [Implement retry logic with exponential backoff](/guides/production/error-handling#implement-retry-logic) to handle transient errors.
