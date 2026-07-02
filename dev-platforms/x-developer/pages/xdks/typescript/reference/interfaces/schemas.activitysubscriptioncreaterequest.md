---
title: "ActivitySubscriptionCreateRequest"
source: https://docs.x.com/xdks/typescript/reference/interfaces/Schemas.ActivitySubscriptionCreateRequest
path: xdks/typescript/reference/interfaces/schemas.activitysubscriptioncreaterequest
---

TypeScript XDK `ActivitySubscriptionCreateRequest` interface reference — request schema with fields, types, and required flags for the X API v2 SDK.

[Schemas](/xdks/typescript/reference/modules/Schemas).ActivitySubscriptionCreateRequest

## Properties

<ResponseField name="eventType" type="&#x22;profile.update.bio&#x22; | &#x22;profile.update.profile_picture&#x22; | &#x22;profile.update.banner_picture&#x22; | &#x22;profile.update.screenname&#x22; | &#x22;profile.update.geo&#x22; | &#x22;profile.update.url&#x22; | &#x22;profile.update.verified_badge&#x22; | &#x22;news.new&#x22; | &#x22;follow.follow&#x22; | &#x22;follow.unfollow&#x22; | &#x22;ProfileBioUpdate&#x22; | &#x22;ProfilePictureUpdate&#x22; | &#x22;ProfileBannerPictureUpdate&#x22; | &#x22;ProfileScreennameUpdate&#x22; | &#x22;ProfileGeoUpdate&#x22; | &#x22;ProfileUrlUpdate&#x22; | &#x22;ProfileVerifiedBadgeUpdate&#x22; | &#x22;NewsNew&#x22; | &#x22;FollowFollow&#x22; | &#x22;FollowUnfollow&#x22;" />

<ResponseField name="filter" type="ActivitySubscriptionFilter" />

<ResponseField name="tag" type="string" />

<ResponseField name="webhookId" type="string" />
