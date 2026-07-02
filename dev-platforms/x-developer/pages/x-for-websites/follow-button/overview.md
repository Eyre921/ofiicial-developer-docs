---
title: "Follow button"
source: https://docs.x.com/x-for-websites/follow-button/overview
path: x-for-websites/follow-button/overview
---

Add an X Follow button to your website with HTML markup or publish.x.com, customize size and screen name display, and load it with widgets.js.

The Follow button is a small button displayed on your websites to help users easily follow a X account. A Follow button consists of two parts: a link to a [follow web intent](/x-for-websites/follow-button/overview) page on x.com and the X for Websites JavaScript to transform the link into our recognizable Follow button.

## How to add a Follow button to your website

The [publish.x.com](https://publish.x.com) website includes a simple tool to generate the embed for a Follow button to copy-and-paste into your website template. Just enter a @screenName to get started.

### Manually

1. Create an anchor element with a `twitter-follow-button` class name. Set the `href` attribute value pointing to a X profile URL.

```html theme={null}
<a class="twitter-follow-button"
  href="https://x.com/XDevelopers">
Follow @XDevelopers</a>
```

2. Customize Follow button parameters using `data-*` attributes.

```html theme={null}
<a class="twitter-follow-button"
  href="https://x.com/XDevelopers"
  data-size="large">
Follow @XDevelopers</a>
```

3. Asynchronously load the X for Websites JavaScript using our loading snippet. The script will initialize the Follow button after your page content loads.

## Button customization

### Hide username

Hide the username from the displayed Follow button by setting a `data-show-screen-name` attribute value of `false`.

### Large button style

Add a `data-size` attribute value of `large` to display a larger Follow button.
