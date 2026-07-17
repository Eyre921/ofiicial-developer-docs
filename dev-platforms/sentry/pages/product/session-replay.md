---
title: "Session Replay"
source: https://docs.sentry.io/product/session-replay.md
path: product/session-replay
---

---
title: "Session Replay"
description: "Watch video-like reproductions of real user sessions to debug errors, slow transactions, and user frustration without guesswork."
url: https://docs.sentry.io/product/session-replay/
---

# Session Replay

Session Replay gives you video-like reproductions of real user sessions so you can see exactly what a user did before, during, and after a bug or performance issue. Instead of guessing from stack traces and logs alone, you can watch the experience unfold — clicks, navigations, network requests, console output, and errors — all in context and synced to a timeline.

**Why it matters:**

* **Reproduce issues without asking users** — See the exact sequence of actions that led to an error, a rage click, or a slow transaction, without needing to reproduce it locally.
* **Inspect the DOM** — For web replays, click on any element in the replay player to inspect its HTML structure, attributes, and position in the document tree, just like browser DevTools but for a session that already happened in production.
* **Cut debugging time** — Errors, traces, network requests, and console logs are all connected to the replay timeline so you can correlate what happened in the UI with what happened under the hood.
* **Understand real user impact** — Go beyond error counts. See how users actually experienced the problem: did they retry? leave? hit a dead end? You can also customize exactly which sessions to capture based on users, URLs, feature flags, or other application logic.
* **Surface frustration signals** — Rage clicks, dead clicks, and [User Feedback](https://docs.sentry.io/product/user-feedback.md) submissions are all linked to replays, so you can find the moments that matter most.

Session Replay is available for [Web](https://docs.sentry.io/product/session-replay/web.md) (all browser-based applications, including static sites, SPAs, and server-rendered frameworks like Next.js and Remix) and [Mobile](https://docs.sentry.io/product/session-replay/mobile.md) (Android, iOS, React Native, and Flutter). Both are generally available and stable.

Organizations can also [restrict replay access](https://docs.sentry.io/product/session-replay/access-control.md) to specific users, providing granular user-based permissions on top of standard role and team permissions.

* #### [Session Replay for Web](https://docs.sentry.io/product/session-replay/web.md)

  Learn about Session Replay and its video-like reproductions of user interactions, which can help you see when users are frustrated and build a better web experience.

* #### [Session Replay for Mobile](https://docs.sentry.io/product/session-replay/mobile.md)

  Use Session Replay for Mobile to get reproductions of user sessions. You'll be able to repro issues faster and get a better understanding of user impact.

* #### [Replays Page and Filters](https://docs.sentry.io/product/session-replay/replay-page-and-filters.md)

  Learn how to navigate the Replays page and filter user sessions that meet specific conditions.

* #### [Replay Details](https://docs.sentry.io/product/session-replay/replay-details.md)

  Learn more about how information is organized on the Replay Details page and how to share and delete replays.

* #### [Restricting Replay Access](https://docs.sentry.io/product/session-replay/access-control.md)

  Restrict which users can view Session Replays using user-based allowlists.

## Pages in this section

- [Session Replay for Web](https://docs.sentry.io/product/session-replay/web.md)
- [Session Replay for Mobile](https://docs.sentry.io/product/session-replay/mobile.md)
- [Replays Page and Filters](https://docs.sentry.io/product/session-replay/replay-page-and-filters.md)
- [Replay Details](https://docs.sentry.io/product/session-replay/replay-details.md)
- [Restricting Replay Access](https://docs.sentry.io/product/session-replay/access-control.md)

