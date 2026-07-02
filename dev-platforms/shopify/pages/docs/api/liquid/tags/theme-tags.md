---
title: "**Theme tags**"
source: https://shopify.dev/docs/api/liquid/tags/theme-tags.md
path: docs/api/liquid/tags/theme-tags
---

---
title: 'Liquid tags: content_for'
description: >-
  Creates a designated area in your
  [theme](https://shopify.dev/themes/architecture) where blocks can be rendered.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/content_for'
  md: 'https://shopify.dev/docs/api/liquid/tags/content_for.md'
api_name: liquid
---

# content\_​for

Creates a designated area in your [theme](https://shopify.dev/themes/architecture) where blocks can be rendered.

The `content_for` tag requires a type parameter to differentiate between rendering a number of theme blocks (`'blocks'`) and a single static block (`'block'`).

## Syntax

```oobleckTag
{% content_for 'blocks' %}
{% content_for 'block', type: "slide", id: "slide-1" %}
```

### blocks

## Syntax

```oobleckTag
{% content_for "blocks" %}
```

Creates a designated area that renders theme blocks as configured in the JSON template or section groups, allowing merchants to add, remove, and rearrange blocks using the theme editor. See [theme blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks) for more information.

### block

## Syntax

```oobleckTag
{% content_for "block", type: "button", id: "static-block-1", color: "red" %}
```

Renders a static theme block of the specified type with the provided ID. You can pass additional arbitrary parameters (such as `color`) that will be accessible within the static block using `{{ color }}`. See [static blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks/static-blocks) to learn more.

