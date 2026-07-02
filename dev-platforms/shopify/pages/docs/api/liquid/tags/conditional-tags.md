---
title: "**Conditional tags**"
source: https://shopify.dev/docs/api/liquid/tags/conditional-tags.md
path: docs/api/liquid/tags/conditional-tags
---

---
title: 'Liquid tags: if'
description: Renders an expression if a specific condition is `true`.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/if'
  md: 'https://shopify.dev/docs/api/liquid/tags/if.md'
api_name: liquid
---

# if

Renders an expression if a specific condition is `true`.

## Syntax

```oobleckTag
{% if condition %}
  expression
{% endif %}
```

### condition

The condition to evaluate.

### expression

The expression to render if the condition is met.

##### Code

```liquid
{% if product.compare_at_price > product.price %}
  This product is on sale!
{% endif %}
```

##### Data

```json
{
  "product": {
    "compare_at_price": "10.00",
    "price": "0.00"
  }
}
```

##### Output

```html
This product is on sale!
```

### elsif

You can use the `elsif` tag to check for multiple conditions.

##### Code

```liquid
{% if product.type == 'Love' %}
  This is a love potion!
{% elsif product.type == 'Health' %}
  This is a health potion!
{% endif %}
```

##### Data

```json
{
  "product": {
    "type": null
  }
}
```

##### Output

```html
This is a health potion!
```

