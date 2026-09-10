---
title: "Create X activity subscription"
source: https://docs.x.com/x-api/activity/create-x-activity-subscription
path: x-api/activity/create-x-activity-subscription
---

post /2/activity/subscriptions
Creates a subscription for an X activity event. OAuth2 user-context tokens must hold the scope matching the requested event_type: dm.read for chat.* and dm.* events, like.read for like.* events, mute.read for mute.* events, block.read for block.* events, follows.read for subscriptions.* events, and tweet.read for all other event types. Mute and block subscriptions are actor-only: filter.user_id must identify the authenticated user and direction is not supported. subscriptions.* events require a user-context token and filter.user_id must identify the authenticated user. Optional filter.qualifiers further narrow supported chat, follow, unfollow, like, and subscriptions events.
