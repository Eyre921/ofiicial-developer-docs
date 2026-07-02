---
title: "User"
source: https://docs.x.com/xdks/typescript/reference/interfaces/Schemas.User
path: xdks/typescript/reference/interfaces/schemas.user
---

Reference for the Schemas.User TypeScript interface in the X API SDK. Field definitions, types, and properties for X API request or response payloads.

[Schemas](/xdks/typescript/reference/modules/Schemas).User

## Properties

<ResponseField name="affiliation" type="Record<string, any>" />

<ResponseField name="connectionStatus" type="(&#x22;following&#x22; | &#x22;follow_request_received&#x22; | &#x22;follow_request_sent&#x22; | &#x22;blocking&#x22; | &#x22;followed_by&#x22; | &#x22;muting&#x22;)[]" />

<ResponseField name="createdAt" type="string" />

<ResponseField name="description" type="string" />

<ResponseField name="entities" type="Record<string, any>" />

<ResponseField name="id" type="string" />

<ResponseField name="location" type="string" />

<ResponseField name="mostRecentTweetId" type="string" />

<ResponseField name="name" type="string" />

<ResponseField name="pinnedTweetId" type="string" />

<ResponseField name="profileBannerUrl" type="string" />

<ResponseField name="profileImageUrl" type="string" />

<ResponseField name="protected" type="boolean" />

<ResponseField name="publicMetrics" type="Record<string, any>" />

<ResponseField name="receivesYourDm" type="boolean" />

<ResponseField name="subscriptionType" type="&#x22;Basic&#x22; | &#x22;Premium&#x22; | &#x22;PremiumPlus&#x22; | &#x22;None&#x22;" />

<ResponseField name="url" type="string" />

<ResponseField name="username" type="string" />

<ResponseField name="verified" type="boolean" />

<ResponseField name="verifiedType" type="&#x22;blue&#x22; | &#x22;government&#x22; | &#x22;business&#x22; | &#x22;none&#x22;" />

<ResponseField name="withheld" type="UserWithheld" />
