---
title: "ApiError"
source: https://docs.x.com/xdks/typescript/reference/classes/ApiError
path: xdks/typescript/reference/classes/apierror
---

Reference for the ApiError class in the X API TypeScript SDK. Properties and methods for inspecting HTTP status, error codes, and X API error responses.

API Error class for handling X API errors

## Hierarchy

* `Error`

  ↳ **`ApiError`**

## Constructors

### constructor

• **new ApiError**(`message`, `status`, `statusText`, `headers`, `data?`): [`ApiError`](/xdks/typescript/reference/classes/ApiError)

#### Parameters

| Name         | Type      |
| :----------- | :-------- |
| `message`    | `string`  |
| `status`     | `number`  |
| `statusText` | `string`  |
| `headers`    | `Headers` |
| `data?`      | `any`     |

#### Returns

[`ApiError`](/xdks/typescript/reference/classes/ApiError)

#### Overrides

Error.constructor

[client.ts:123](https://github.com/xdevplatform/xdk-typescript/blob/81aacb165e0802e188f608bdf462b60fc4e713a2/src/client.ts#L123)

## Properties

<ResponseField name="status" type="number" />

<ResponseField name="statusText" type="string" />

<ResponseField name="headers" type="Headers" />

<ResponseField name="data" type="any" />
