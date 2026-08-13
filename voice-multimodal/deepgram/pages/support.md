---
title: "Support"
source: https://developers.deepgram.com/support.md
path: support
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Support

## Start here

| What's going on                                     | Where to go                                                                                              |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| I have a quick question while building              | [Ask AI](/ask-ai), or search these docs                                                                  |
| I want to ask other builders                        | [Discord](https://dpgr.am/discord) or [GitHub Discussions](https://github.com/orgs/deepgram/discussions) |
| Is Deepgram down?                                   | [status.deepgram.com](https://status.deepgram.com)                                                       |
| Something looks broken                              | [support@deepgram.com](mailto:support@deepgram.com) with your request ID                                 |
| It's about my account or billing                    | [success@deepgram.com](mailto:success@deepgram.com) or the [help center](https://help.deepgram.com)      |
| I need faster response times or dedicated engineers | [success@deepgram.com](mailto:success@deepgram.com?subject=Support%20plan%20question)                    |

## Instant answers

Ask AI lives right here in the docs. It answers from the pages you're reading and links back to its sources, so you can check its work.

* [Ask AI](/ask-ai)
* Add the Deepgram Slack bot, then mention @Deepgram in any channel: [https://slack.com/oauth/v2/authorize?client\_id=20688005349.8697747146976\&scope=assistant:write,channels:history,channels:read,chat:write,groups:history,groups:read,im:history,im:read,im:write,mpim:history,mpim:read,users:read\&user\_scope=team:read](https://slack.com/oauth/v2/authorize?client_id=20688005349.8697747146976\&scope=assistant:write,channels:history,channels:read,chat:write,groups:history,groups:read,im:history,im:read,im:write,mpim:history,mpim:read,users:read\&user_scope=team:read)

**Prefer Slack?** The Deepgram bot searches our docs and answers right in the thread, with code and links. Add it above, then mention **@Deepgram** in any channel.

## Ask the community

Some of the best debugging help comes from someone who hit the same wall last month.

* [Discord](https://dpgr.am/discord): builders and Deepgram engineers, in real time. Good for a quick gut check or a second pair of eyes.
* [GitHub Discussions](https://github.com/orgs/deepgram/discussions): for questions worth keeping. Threads are searchable, so your answer helps whoever hits this next.

One thing to know: nobody in the community can see your account. Keep billing questions and anything touching your project data to email, where we can pull up your account and help. Both spaces follow our [Code of Conduct](/code-of-conduct).

## Check service status

When something breaks, check [status.deepgram.com](https://status.deepgram.com) first. It's the quickest way to rule out an issue on our end before you go digging through your own. You can subscribe there for incident and maintenance alerts.

During an incident we post updates on the status page as we work, so there's no need to open a ticket to tell us something's down. If your problem outlasts the incident, email us. We want to know.

## Email us

We're always happy to help. Send it to whichever address fits:

* **A technical or API problem:** [support@deepgram.com](mailto:support@deepgram.com), from the address on your Deepgram account so we can find your project.
* **Account or billing:** [success@deepgram.com](mailto:success@deepgram.com), or check the [help center](https://help.deepgram.com) for the common ones.

### When to expect a reply

* **Blocked right now?** Say so in your first line and we'll get to you sooner.
* **We answer on business days.** Weekend and holiday mail is waiting for us the next morning we're in.
* **Mid-incident?** [status.deepgram.com](https://status.deepgram.com) updates fastest.
* **Want a faster turnaround?** Support plans add it. Ask us at [success@deepgram.com](mailto:success@deepgram.com?subject=Support%20plan%20question).

### What to send

The tickets we turn around fastest are the ones we can reproduce. You don't need every item below, but each one you include saves us a round trip:

* **A request ID.** Every API response carries a `dg-request-id` response header. This is the single most useful thing you can send. For a failed WebSocket connection, grab the `dg-error` header too. The [speech-to-text](/docs/stt-troubleshooting-websocket-data-and-net-errors) and [text-to-speech](/docs/tts-troubleshooting-websocket-net-and-data-errors) troubleshooting guides show where to find them.
* **Your project ID**, from the [Console](https://console.deepgram.com).
* **The endpoint and model** you called, for example, `/v1/listen` with `nova-3`.
* **Your SDK and version**, or a note that you called the API directly.
* **When it happened**, in UTC.
* **What you expected, and what you got**: the exact error message or status code.
* **A minimal repro** if you have one: a request, a snippet, or a short audio sample.

## Support plans

Support plans are available on enterprise agreements. Your Deepgram rep can walk you through the options, or email [success@deepgram.com](mailto:success@deepgram.com?subject=Support%20plan%20question) if you don't have a rep yet.
