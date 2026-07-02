---
title: "v1 to v2"
source: https://docs.x.com/enterprise-api/posts/timelines/migrate/standard-to-twitter-api-v2
path: enterprise-api/posts/timelines/migrate/standard-to-twitter-api-v2
---

If you have been working with the v1.1 timelines endpoints (statuses/user\timeline and. Reference for the Enterprise X API tier covering migrate.

## Standard v1.1 timelines to X API v2 timelines

If you have been working with the v1.1 timelines endpoints (statuses/user\_timeline and statuses/mentions\_timeline), the goal of this guide is to help you understand the similarities and differences between the standard and X API v2 timelines endpoints so that you can migrate your current integration to the new version.

* **Similarities:**
  * Authentication:
    * OAuth 1.0a User Context (reverse chronological home timeline, user Post timeline and user mentions timeline)
    * OAuth 2.0 App-Only (user Post timeline)
  * Historical Access limit: User timeline (user Post timeline) provides access to most recent 3200 Posts; mentions timeline (user mention timeline) provides access to most recent 800 mentions.
  * Support for Post edit history and metadata
  * Rate limits (user Post timeline)
  * Refresh polling: Ability to retrieve new results since the since\_id
  * Traversing timelines by Post IDs
  * Results specifications:
    * Results order: Results returned in reverse chronological order
    * Ability to exclude replies (user Post timeline only)
    * Ability to exclude Retweets (user Post timeline only)
* **Differences**
  * New Authentication capability:
    * OAuth 2.0 App-Only (user mention timeline)
    * OAuth 2.0 Authorization Code Flow with PKCE (reverse chronological home timeline, user Post timeline and user mentions timeline)
  * Access requirements: X API v2 App and Project requirements
  * Rate limits (user mention timeline and reverse chronological home timeline)
  * Additional pagination method
    * Different max\_results (count) per response
  * Response data format
  * Request parameters
    * Custom
