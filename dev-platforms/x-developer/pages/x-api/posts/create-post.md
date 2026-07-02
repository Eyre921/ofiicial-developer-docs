---
title: "Create or Edit Post"
source: https://docs.x.com/x-api/posts/create-post
path: x-api/posts/create-post
---

post /2/tweets
Creates a new Post for the authenticated user, or edits an existing Post when edit_options are provided. Supports paid partnership disclosure via the paid_partnership field.

<Warning>
  Quote-posting (using the `quote_tweet_id` parameter) requires an [Enterprise plan](/enterprise-api/introduction). It is not available on self-serve (pay-per-use) tiers.
</Warning>
