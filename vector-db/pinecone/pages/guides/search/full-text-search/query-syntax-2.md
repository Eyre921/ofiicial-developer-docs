---
title: "Full-text search query syntax"
source: https://docs.pinecone.io/guides/search/full-text-search/query-syntax
path: guides/search/full-text-search/query-syntax
---

Write Pinecone full-text search queries with Lucene query_string syntax, including boolean, phrase, prefix, boosting, and fuzzy operators.

Full-text search offers two text-based query types: `type: "text"` for BM25 token search over one or more named fields, and `type: "query_string"` for the full Lucene grammar, with boolean operators, phrases, boosting, fuzzy matching, and more.

## Choosing a query type

The two types differ in the capabilities they support:

| Feature                          | `type: "text"`                                                                       | `type: "query_string"`                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| **Purpose**                      | Token search on one or more fields                                                   | Lucene query syntax                                                                  |
| **Field targeting**              | Required `fields`, one or more text fields (scores against all)                      | No `field`/`fields` param; use Lucene field qualifiers (`title:(...)`) in the query  |
| **Multi-word behavior**          | Token match, OR across terms (BM25)                                                  | OR by default; use `AND`, quotes, etc. for other logic                               |
| **Boolean operators**            | Not supported (treated as words)                                                     | `AND`, `OR`, `NOT`, `+`, `-`                                                         |
| **Phrase prefix**                | Not supported                                                                        | `"phrase pre"*` (last term as prefix)                                                |
| **Single-term prefix** (`auto*`) | Not supported                                                                        | Not supported. Use [phrase prefix](#phrase-prefix)                                   |
| **Phrase matching**              | Not supported in `score_by` (use `query_string` or `$match_phrase` filter)           | Wrap in quotes: `"exact phrase"`                                                     |
| **Phrase slop**                  | Not supported                                                                        | `"phrase"~N`                                                                         |
| **Boosting**                     | Not supported                                                                        | `term^N`                                                                             |
| **Regex**                        | Not supported                                                                        | `field:/pattern.*/`                                                                  |
| **Fuzzy matching**               | Not supported                                                                        | `term~`, `term~N` (typo tolerance)                                                   |
| **Stemming**                     | Supported ([when enabled](/guides/search/full-text-search/text-processing#stemming)) | Supported ([when enabled](/guides/search/full-text-search/text-processing#stemming)) |
| **Case sensitivity**             | Case-insensitive                                                                     | Case-insensitive                                                                     |

## Token matching (`type: "text"`)

With `type: "text"`, the query string is run through the field's analyzer pipeline (see [Tokens and analyzers](/guides/search/full-text-search/text-processing#tokens-and-analyzers)) and each resulting term contributes to the BM25 score. Multiple terms use **OR** semantics: documents can match if they contain **any** of the terms; documents that match more terms or stronger term statistics typically rank higher. Matching is case-insensitive. Exact **phrase** constraints (adjacent words in order) belong in `type: "query_string"` using quotes, or in a `$match_phrase` filter.

| Query              | Matches                                                               | Does not match                         |
| ------------------ | --------------------------------------------------------------------- | -------------------------------------- |
| `machine learning` | "**Machine** learning is great" (has "machine")                       | "Vector databases only" (neither term) |
| `machine learning` | "We use **learning** and **machine**" (both terms present, any order) | "Vector databases only" (neither term) |
| `machine`          | "**Machine** learning is great"                                       | "Vector databases only" (no "machine") |

### Key behaviors

* **Single term** (`machine`): Matches documents containing that term. Case-insensitive.
* **Multiple terms** (`machine learning`): Each term is searched independently with OR-style matching and combined BM25 scoring, not as a single adjacent phrase.
* **No operator support**: Characters like `AND`, `OR`, `NOT`, `*`, `~`, `^`, `+`, `-`, and quotes are treated as literal text.

## Lucene query syntax (`type: "query_string"`)

With `type: "query_string"`, you write Lucene query syntax, with operator support. Field names are embedded in the query itself (e.g., `content:(term)`) and can combine multiple fields with boolean operators.

| Operator       | Syntax                     | Example                             | Description                                                                   |
| -------------- | -------------------------- | ----------------------------------- | ----------------------------------------------------------------------------- |
| Term           | `field:(word)`             | `body:(computers)`                  | Match documents containing term                                               |
| Multiple terms | `field:(a b)`              | `body:(machine learning)`           | OR by default, matches either term                                            |
| Phrase         | `field:("words")`          | `body:("machine learning")`         | Exact phrase match (adjacent, in order)                                       |
| AND            | `AND`                      | `body:(a AND b)`                    | Both terms required                                                           |
| OR             | `OR`                       | `body:(a OR b)`                     | Either term matches (same as default)                                         |
| NOT            | `NOT`                      | `body:(a NOT b)`                    | Exclude second term                                                           |
| Required       | `+term`                    | `body:(+database search)`           | Term must be present                                                          |
| Excluded       | `-term`                    | `body:(database -deprecated)`       | Term must not be present                                                      |
| Grouping       | `(expr)`                   | `body:((a OR b) AND c)`             | Control precedence                                                            |
| Phrase slop    | `"phrase"~N`               | `body:("fast search"~2)`            | Allow up to N words between phrase terms                                      |
| Boost          | `term^N`                   | `body:(machine^3 learning)`         | Multiply the clause's relevance score by N (`0` or greater, decimals allowed) |
| Phrase prefix  | `"phrase pre"*`            | `body:("james w"*)`                 | Last term in phrase matched as prefix                                         |
| Regex          | `field:/pattern.*/`        | `body:/comput.*/`                   | Match documents by regular expression on a field                              |
| Fuzzy          | `term~` or `term~N`        | `body:(compxter~1)`                 | Match terms within edit distance N (0–2) for typo tolerance                   |
| Cross-field    | `fieldA:(…) OR fieldB:(…)` | `title:(quantum) OR body:(machine)` | Combine clauses across text-searchable fields                                 |

### Terms and default OR behavior

A **term** is a single word. Multiple space-separated terms use **OR logic** by default.

```
body:(machine learning)
```

Matches documents containing "machine" OR "learning" (or both). Documents with both terms rank higher.

### Phrases

Wrap multiple words in quotes to match them as an exact sequence.

```
body:("machine learning")
```

Matches only documents containing the exact phrase "machine learning" with the words adjacent. That is different from `type: "text"` with `query: "machine learning"`, which uses **token OR** matching on the field. For phrase matching as a **filter** (e.g., composed with dense-vector ranking), use `{"body": {"$match_phrase": "machine learning"}}` in the `filter` block.

*Phrase terms are matched against the field's analyzed tokens. If [stemming](/guides/search/full-text-search/text-processing#stemming) is enabled on the field, the phrase terms stem too, e.g., `"running fast"` matches `running fast` and `runs fast`.*

### Boolean operators (AND, OR, NOT)

Use `AND`, `OR`, and `NOT` for explicit boolean logic.

```
body:(machine AND learning)        # Both terms required (any order)
body:(machine OR learning)         # Either term (same as default)
body:(machine NOT learning)        # "machine" but not "learning"
```

AND binds tighter than OR, so use parentheses to control order:

```
body:((database OR storage) AND distributed)
```

### Required and excluded terms (+, -)

Use `+` to require a term and `-` to exclude a term.

```
body:(+database distributed)       # MUST contain "database", "distributed" optional
body:(database -deprecated)        # Contains "database", must NOT contain "deprecated"
body:(+vector +search -legacy)     # MUST have "vector" AND "search", must NOT have "legacy"
```

### Phrase proximity (slop)

Allow words in a phrase to appear within N positions of each other.

```
body:("machine learning"~3)
```

Matches "machine learning", "machine deep learning", or "machine-assisted learning" (words within 3 positions).

*The phrase terms are matched against analyzed tokens, so [stemming](/guides/search/full-text-search/text-processing#stemming) (when enabled on the field) applies here too.*

### Boosting

Use `^N` to multiply a clause's contribution to the relevance score, where `N` is `0` or greater. The default is `1`, so `^2` doubles the contribution and `^0.5` halves it. Scaling is linear.

```
body:(machine^3 learning)           # "machine" weighted 3x more than "learning"
body:(machine^0.5 learning)         # "machine" weighted half as much as "learning"
body:("neural network"^2 deep)      # Phrase boosted 2x
body:((machine OR neural)^2 deep)   # Whole group boosted 2x
```

Attach `^N` directly to a term, a quoted phrase, or a parenthesized group. A space on either side of `^`, as in `body:(machine ^2 learning)`, is a query error (`400`).

* **`N` is a literal number**, whole or decimal, with digits on both sides of the decimal point, such as `2`, `1.5`, or `0.75`.
* **Values below `1`** reduce the clause's weight, and `^1` leaves scoring unchanged.
* **`^0`** drops the clause's contribution to zero, though documents matching it are still returned. If every clause in the query is boosted to `0`, all matches score `0` and their order isn't meaningful.
* **Anything else is a query error (`400`)**: Arithmetic (`^(2*3)`), negatives (`^-2`), scientific notation (`^1e3`), a bare leading decimal point (`^.5`), and chained boosts (`^2^3`).

There's no function- or field-based scoring, so weight by a stored field value or a formula in your application after the search returns.

Boosting is available only with `type: "query_string"`. With `type: "text"` and in the [text-match filters](/guides/search/filter-by-metadata#text-match-filters), `^` is treated as a literal character.

### Phrase prefix

Append `*` to a quoted phrase to treat the last term as a prefix. The phrase must contain at least two terms.

```
body:("james w"*)                  # Matches "james webb", "james watson", "james wilde"
body:("machine lea"*)              # Matches "machine learning", "machine learns"
```

A single-term prefix wildcard, such as `auto*`, isn't supported. It returns no matches rather than an error. Use a phrase prefix instead, or configure the field for [substring search](/guides/search/full-text-search/text-processing#substring-search-with-n-grams).

Both the literal terms and the prefix are matched against the field's analyzed tokens. If [stemming](/guides/search/full-text-search/text-processing#stemming) is enabled on the field, stemming applies to the completed terms in the phrase, while the final prefix is expanded against analyzed tokens.

Phrase prefix is optimized for autocomplete-style queries where the final word prefix is reasonably specific. To keep latency low, Pinecone expands the final prefix to the first 50 matching terms in lexicographic order. For example, `"new yor"*` can match `new york`, but `"new yo"*` might not if `york` is not among the first 50 expanded terms for `yo`.

### Regex

Wrap a pattern in forward slashes to match documents by regular expression on a field.

```
body:/comput.*/
```

Matches documents whose `body` field contains a token matching the regex `comput.*` (e.g., "computer", "computing", "computation"). Regex patterns are matched against individual analyzed tokens, not the raw field text.

```
body:/machin[ei].*/
```

Matches tokens like "machine" or "machene". Standard Lucene regex syntax is supported.

Regex is only available with `type: "query_string"`. It is not supported with `type: "text"`.

### Fuzzy matching (typo tolerance)

Append `~` to a bare term to match indexed terms within a small edit distance, so a misspelled query term still matches the intended word.

```
body:(compxter~1)                  # Matches "computer" (1 edit away)
body:(machine~ learning~)          # Auto distance per term, based on term length
title:(pinecone~2)                 # Explicit distance 2
```

* **`term~`** — automatic distance based on the term's length: terms shorter than 4 characters must match exactly, terms of 4–7 characters allow 1 edit, and terms of 8 or more characters allow 2 edits.
* **`term~N`** — fixed edit distance `N`, where `N` is `0`, `1`, or `2`. `~0` is an exact match. A distance greater than 2 is a query error (`400`).

An "edit" is an inserted, deleted, or substituted character (plain Levenshtein distance). Swapping two adjacent characters counts as 2 edits. Matching is case-insensitive, as with all text queries.

Fuzzy matches are scored as a constant; exact matches still contribute their full BM25 score, so an exact hit ranks above a fuzzy hit for the same term. Fuzzy composes with the rest of the query syntax, boolean operators, required/excluded terms, boosts, field qualifiers, and metadata filters.

<Note>
  The `~` operator is fuzzy only when it follows a **bare term**. After a quoted phrase, `~N` keeps its [phrase slop](#phrase-proximity-slop) meaning, for example, `body:("machine learning"~2)` is slop, while `body:(learning~2)` is fuzzy. There is no fuzzy phrase matching.
</Note>

<Note>
  On [stemmed](/guides/search/full-text-search/text-processing#stemming) fields, fuzzy matching runs against the stemmed terms and is best-effort: a typo that changes how a word stems may not match. Fuzzy matching is most effective on fields without stemming (the default). Fuzzy is available only with `type: "query_string"`. With `type: "text"`, `~` is treated as a literal character. Fuzzy also doesn't apply in the `$match_phrase`, `$match_all`, and `$match_any` [text-match filters](/guides/search/filter-by-metadata#text-match-filters), where a `~` operator is matched literally and the filter finds nothing.
</Note>

### Cross-field queries

`query_string` can target multiple fields in the same expression. Use Lucene field qualifiers (`field:(clause)`) directly in the query string; omit them to run against all text-searchable fields:

```
title:(quantum) OR body:(machine learning)
```

Matches documents whose `title` contains "quantum", documents whose `body` contains "machine" or "learning", or both, with BM25 scoring combining across fields.
