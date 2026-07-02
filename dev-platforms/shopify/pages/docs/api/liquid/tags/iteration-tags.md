---
title: "**Iteration tags**"
source: https://shopify.dev/docs/api/liquid/tags/iteration-tags.md
path: docs/api/liquid/tags/iteration-tags
---

---
title: 'Liquid tags: for'
description: Renders an expression for every item in an array.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/for'
  md: 'https://shopify.dev/docs/api/liquid/tags/for.md'
api_name: liquid
---

# for

Renders an expression for every item in an array.

You can do a maximum of 50 iterations with a `for` loop. If you need to iterate over more than 50 items, then use the [`paginate` tag](https://shopify.dev/docs/api/liquid/tags/paginate) to split the items over multiple pages.

***

**Tip:** Every \<code>for\</code> loop has an associated \<a href="/docs/api/liquid/objects/forloop">\<code>forloop\</code> object\</a> with information about the loop.

***

## Syntax

```oobleckTag
{% for variable in array %}
  expression
{% endfor %}
```

### variable

The current item in the array.

### array

The array to iterate over.

### expression

The expression to render for each iteration.

##### Code

```liquid
{% for product in collection.products -%}
  {{ product.title }}
{%- endfor %}
```

##### Data

```json
{
  "collection": {
    "products": [
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      }
    ]
  }
}
```

##### Output

```html
Draught of Immortality
Glacier ice
Health potion
Invisibility potion
```

## for tag parameters

### limit

## Syntax

```oobleckTag
{% for variable in array limit: number %}
  expression
{% endfor %}
```

You can limit the number of iterations using the `limit` parameter.

***

**Tip:** Limit the amount of data fetched for arrays that can be paginated with the \<code>paginate\</code> tag instead of using the \<code>limit\</code> parameter. Learn more about \<a href="/docs/api/liquid/tags/paginate#paginate-limit-data-fetching">limiting data fetching\</a> for improved server-side performance.

***

##### Code

```liquid
{% for product in collection.products limit: 2 -%}
  {{ product.title }}
{%- endfor %}
```

##### Data

```json
{
  "collection": {
    "products": [
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      }
    ]
  }
}
```

##### Output

```html
Draught of Immortality
Glacier ice
```

### offset

## Syntax

```oobleckTag
{% for variable in array offset: number %}
  expression
{% endfor %}
```

You can specify a 1-based index to start iterating at using the `offset` parameter.

##### Code

```liquid
{% for product in collection.products offset: 2 -%}
  {{ product.title }}
{%- endfor %}
```

##### Data

```json
{
  "collection": {
    "products": [
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      }
    ]
  }
}
```

##### Output

```html
Health potion
Invisibility potion
```

### range

## Syntax

```oobleckTag
{% for variable in (number..number) %}
  expression
{% endfor %}
```

Instead of iterating over specific items in an array, you can specify a numeric range to iterate over.

***

**Note:** You can define the range using both literal and variable values.

***

##### Code

```liquid
{% for i in (1..3) -%}
  {{ i }}
{%- endfor %}

{%- assign lower_limit = 2 -%}
{%- assign upper_limit = 4 -%}

{% for i in (lower_limit..upper_limit) -%}
  {{ i }}
{%- endfor %}
```

##### Output

```html
1
2
3

2
3
4
```

### reversed

## Syntax

```oobleckTag
{% for variable in array reversed %}
  expression
{% endfor %}
```

You can iterate in reverse order using the `reversed` parameter.

##### Code

```liquid
{% for product in collection.products reversed -%}
  {{ product.title }}
{%- endfor %}
```

##### Data

```json
{
  "collection": {
    "products": [
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      }
    ]
  }
}
```

##### Output

```html
Invisibility potion
Health potion
Glacier ice
Draught of Immortality
```

# forloop**object**

Information about a parent [`for` loop](https://shopify.dev/docs/api/liquid/tags/for).

## Properties

* * **first**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the current iteration is the first. Returns `false` if not.

  * **index**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The 1-based index of the current iteration.

  * **index0**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The 0-based index of the current iteration.

  * **last**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the current iteration is the last. Returns `false` if not.

  * **length**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The total number of iterations in the loop.

  * **parentloop**

    [forloop](https://shopify.dev/docs/api/liquid/objects/forloop)

  * The parent `forloop` object.

    If the current `for` loop isn't nested inside another `for` loop, then `nil` is returned.

    ExampleUse the `parentloop` property

    ##### Code

    ```liquid
    {% for i in (1..3) -%}
      {% for j in (1..3) -%}
        {{ forloop.parentloop.index }} - {{ forloop.index }}
      {%- endfor %}
    {%- endfor %}
    ```

    ##### Output

    ```html
    1 - 1
    1 - 2
    1 - 3

    2 - 1
    2 - 2
    2 - 3

    3 - 1
    3 - 2
    3 - 3
    ```

  * **rindex**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The 1-based index of the current iteration, in reverse order.

  * **rindex0**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The 0-based index of the current iteration, in reverse order.

##### Example

```json
{
  "first": true,
  "index": 1,
  "index0": 0,
  "last": false,
  "length": 4,
  "rindex": 3
}
```

### Use the `forloop` object

##### Code

```liquid
{% for page in pages -%}
  {%- if forloop.length > 0 -%}
    {{ page.title }}{% unless forloop.last %}, {% endunless -%}
  {%- endif -%}
{% endfor %}
```

##### Output

```html
About us, Contact, Potion dosages
```

