---
title: "Embedded lists"
source: https://docs.x.com/x-for-websites/timelines/guides/list-timeline
path: x-for-websites/timelines/guides/list-timeline
---

Embed a X list timeline showing the latest Posts from a curated public list using an anchor tag with the list URL or the twttr.widgets.createTimeline factory.

A list timeline displays the latest Posts ordered from newest to oldest from a curated public list of X accounts. The timeline includes a header displaying the list’s name, description, and curator. [Read more about X lists](https://support.x.com/articles/76460).

## HTML markup

A responsive timeline backed by a X list can be added to a webpage through a common HTML template.

A template example:

```html theme={null}
<a class="twitter-timeline"
  href="https://x.com/{screen_name}/lists/{slug}">
Posts from https://x.com/{screen_name}/lists/{slug}
</a>
```

```html theme={null}
<a class="twitter-timeline"
  href="https://x.com/x/lists/official-twitter-accts">
Posts from https://x.com/x/lists/official-twitter-accts
</a>
```

## JavaScript factory function

The X for Websites JavaScript library supports dynamic insertion of an embedded list timeline using the `twttr.widgets.createTimeline` function. Pass a data source definition, target container element, and optional options object to insert an embedded timeline into your page.

HTML `data-*` parameters are camelCased when passed as an options object property.

```javascript theme={null}
twttr.widgets.createTimeline(
  {
    sourceType: "list",
    ownerScreenName: "XDevelopers",
    slug: "national-parks"
  },
  document.getElementById("container")
);
```
