---
title: "**Variable tags**"
source: https://shopify.dev/docs/api/liquid/tags/variable-tags.md
path: docs/api/liquid/tags/variable-tags
---

---
title: 'Liquid tags: assign'
description: Creates a new variable.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/assign'
  md: 'https://shopify.dev/docs/api/liquid/tags/assign.md'
api_name: liquid
---

# assign

Creates a new variable.

You can create variables of any [basic type](https://shopify.dev/docs/api/liquid/basics#types), [object](https://shopify.dev/docs/api/liquid/objects), or object property.

***

**Caution:** Predefined Liquid objects can be overridden by variables with the same name. To make sure that you can access all Liquid objects, make sure that your variable name doesn\&#39;t match a predefined object\&#39;s name.

***

## Syntax

```oobleckTag
{% assign variable_name = value %}
```

### variable\_name

The name of the variable being created.

### value

The value you want to assign to the variable.

##### Code

```liquid
{%- assign product_title = product.title | upcase -%}

{{ product_title }}
```

##### Data

```json
{
  "product": {
    "title": "Health potion"
  }
}
```

##### Output

```html
HEALTH POTION
```

