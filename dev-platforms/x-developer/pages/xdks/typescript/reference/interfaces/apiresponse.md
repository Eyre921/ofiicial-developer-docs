---
title: "ApiResponse"
source: https://docs.x.com/xdks/typescript/reference/interfaces/ApiResponse
path: xdks/typescript/reference/interfaces/apiresponse
---

Reference for the ApiResponse TypeScript interface in the X API SDK. Field definitions, types, and properties for X API request or response payloads.

Response wrapper with metadata

## Type parameters

| Name | Type  |
| :--- | :---- |
| `T`  | `any` |

## Properties

<ResponseField name="body" type="T">
  Response body
</ResponseField>

<ResponseField name="headers" type="Headers">
  Response headers
</ResponseField>

<ResponseField name="status" type="number">
  HTTP status code
</ResponseField>

<ResponseField name="statusText" type="string">
  HTTP status text
</ResponseField>

<ResponseField name="url" type="string">
  Response URL
</ResponseField>
