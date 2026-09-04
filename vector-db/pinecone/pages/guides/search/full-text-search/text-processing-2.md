---
title: "Full-text search text processing"
source: https://docs.pinecone.io/guides/search/full-text-search/text-processing
path: guides/search/full-text-search/text-processing
---

Control how Pinecone full-text search tokenizes and analyzes text, including tokens and analyzers, stemming, language options, and substring (n-gram) matching.

Configure how Pinecone indexes and matches text in your full-text-search fields. These options are set per field at index creation.

## Tokens and analyzers

The word "token" appears in every scoring method, but it means different things in each. Knowing what counts as a token in your chosen method is essential to writing queries that match what you expect.

### FTS tokens (`type: "text"`, `type: "query_string"`, and `$match_*` filters)

When you declare a field with `full_text_search: { ... }`, Pinecone runs the field's text through an **analyzer pipeline** at index time and at query time. Both `type: "text"` and `type: "query_string"` use the same pipeline, and the text-match filter operators ([`$match_phrase`, `$match_all`, `$match_any`](/guides/search/filter-by-metadata#text-match-filters)) reuse it as well, so a token that scores in BM25 will match in a filter on the same field.

The pipeline (in order):

1. **Split** the text on whitespace and punctuation. Hyphenated words become multiple tokens (`state-of-the-art` → `state`, `of`, `the`, `art`).
2. **Lowercase** every token. Lowercasing is server-applied and cannot be overridden.
3. **Stem** each token to its root form, if [`stemming`](#stemming) is enabled on the field. The stemmer is selected by the field's [`language`](#language) setting (`models` → `model`, `running` → `run`).
4. **Drop stop words** (common words like `the`, `and`), if `stop_words: true` is set on the field. Not all languages have built-in stop word lists; see the [Language](#language) table for details.
5. **Cap** each token at 40 characters. A raw token value can be up to 256 bytes at ingest; the analyzer then truncates it to this 40-character cap. This cap is server-applied and cannot be overridden.

For example, with the `english` analyzer, `stemming: true`, and `stop_words: false`, the input `"State-of-the-Art Models"` becomes the tokens `state`, `of`, `the`, `art`, `model`. Those are the tokens BM25 scores against, and the tokens a `$match_phrase: "art models"` filter will look for.

Fields configured for [substring search](#substring-search-with-n-grams) replace this whole-token pipeline with character n-gram tokenization, so a token is further split into overlapping character sequences.

### Dense-vector tokens (`type: "dense_vector"`)

Dense embedding models have their own internal tokenizer, usually a subword scheme like BPE, WordPiece, or SentencePiece, that breaks text into pieces the model was trained on. Those tokens are **private to the model**. You never query them directly: a dense search compares the full embedding of a query against the full embedding of a document. The same string can therefore behave very differently in `type: "text"` (which sees the FTS analyzer tokens above) and `type: "dense_vector"` (which sees a single high-dimensional vector). The `$match_*` filter operators do not apply to dense-vector fields.

### Sparse-vector tokens (`type: "sparse_vector"`)

Sparse encoders also tokenize internally, and the tokenization depends on the encoder. Pinecone's hosted [`pinecone-sparse-english-v0`](/models/pinecone-sparse-english-v0) produces learned per-token weights and **expands to related terms** that don't appear in the source text. Encoder tokens are not interchangeable with FTS analyzer tokens, and `$match_*` filters do not apply to sparse-vector fields.

### Practical implication

If your application stores the same source text in an FTS-enabled `string` field and also encodes it into a `dense_vector` or `sparse_vector` field, the three representations are tokenized **independently**: the FTS analyzer for the `string` field, and each model's internal tokenizer for the vector fields. Identical query strings will therefore retrieve different documents under different `score_by` types, and `$match_*` filters can only narrow on the FTS-analyzer tokens of FTS-enabled `string` fields.

## Stemming

Stemming reduces words to their root form so that morphological variants match each other. For example, with stemming enabled, a query for "run" also matches documents containing "running" or "runs".

Stemming is **opt-in** and disabled by default. To enable it, set `stemming: true` on a text-searchable field when creating the index. The stemming algorithm is determined by the field's [`language`](#language) setting. Stemming applies to both `type: "text"` and `type: "query_string"` queries on the field.

<Note>
  Stemming is set at index creation and cannot be changed afterward.
</Note>

### Enable stemming with French

```json theme={null}
{
  "schema": {
    "fields": {
      "body": {
        "type": "string",
        "full_text_search": {
          "stemming": true,
          "language": "french"
        }
      }
    }
  }
}
```

## Language

The `language` parameter controls tokenization and stemming behavior for a text-searchable field. It determines how text is analyzed during indexing and search: how words are split into tokens and, when [stemming](#stemming) is enabled, which language-specific rules are used to reduce words to their root forms.

The default language is `"en"` (English). You can specify a language using either its short code or full name (e.g., `"fr"` or `"french"`).

<Note>
  Language is set at index creation and cannot be changed afterward.
</Note>

### Supported languages

| Code | Full name    | Stop words |
| ---- | ------------ | ---------- |
| `ar` | `arabic`     | No         |
| `da` | `danish`     | Yes        |
| `de` | `german`     | Yes        |
| `el` | `greek`      | No         |
| `en` | `english`    | Yes        |
| `es` | `spanish`    | Yes        |
| `fi` | `finnish`    | Yes        |
| `fr` | `french`     | Yes        |
| `hu` | `hungarian`  | Yes        |
| `it` | `italian`    | Yes        |
| `nl` | `dutch`      | Yes        |
| `no` | `norwegian`  | Yes        |
| `pt` | `portuguese` | Yes        |
| `ro` | `romanian`   | No         |
| `ru` | `russian`    | Yes        |
| `sv` | `swedish`    | Yes        |
| `ta` | `tamil`      | No         |
| `tr` | `turkish`    | No         |

## Substring search with n-grams

By default, full-text search matches whole tokens: a query for `comp` does not match a document containing `computer`. To match substrings (for example, to find `computer` from `comp`, `mput`, or `uter`), configure a text field for **character n-gram** tokenization.

With n-gram tokenization, each token is broken into overlapping character sequences (n-grams) at index time, and query text is broken the same way at search time, so a substring of an indexed word matches. This is useful for partial-word matching, autocomplete, and searching identifiers or codes where users type only a fragment.

To enable it, set an `ngram` object on a text field's `full_text_search` config at index creation:

```json theme={null}
{
  "schema": {
    "fields": {
      "product_name": {
        "type": "string",
        "full_text_search": {
          "ngram": {
            "min_gram": 3,
            "max_gram": 4,
            "prefix_only": false
          }
        }
      }
    }
  }
}
```

`ngram` parameters:

| Parameter     | Type    | Required             | Description                                                                                                                                                                                                         |
| ------------- | ------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `min_gram`    | integer | Yes                  | Shortest n-gram to generate. Must be at least `1`.                                                                                                                                                                  |
| `max_gram`    | integer | Yes                  | Longest n-gram to generate. Must be at least `min_gram` and at most `10`.                                                                                                                                           |
| `prefix_only` | boolean | No (default `false`) | When `true`, generate only n-grams anchored to the start of each token (edge n-grams). Use this for prefix and autocomplete matching. When `false`, generate n-grams at every position for full substring matching. |

For example, with `min_gram: 3`, `max_gram: 4`, and `prefix_only: false`, the token `search` is indexed as `sea`, `ear`, `arc`, `rch`, `sear`, `earc`, `arch`. A shorter or longer window changes the tradeoff: smaller n-grams match more loosely and grow the index more; larger n-grams are more precise but require longer matching substrings.

Querying an n-gram field needs no special syntax. Once a field is configured for n-grams, ordinary `type: "text"` and `query_string` queries against it match on substrings automatically, because the query text is tokenized into the same n-grams as the indexed text:

```python Python theme={null}
response = index.documents.search(
    namespace="example-namespace",
    top_k=10,
    score_by=[
        {
            "type": "text",
            "fields": ["product_name"],
            "query": "sear",
        }
    ],
    include_fields=["product_name"],
)
```

<Note>
  N-gram tokenization cannot be combined with [`stemming`](#stemming) or `stop_words` on the same field — an index-creation request that sets `ngram` alongside either is rejected with a `400` error. Tokens are always lowercased. Because every position emits a token for each gram length, an n-gram field is larger on disk than a plain text field; keep `min_gram`/`max_gram` as narrow as your matching needs allow.
</Note>

<Note>
  N-gram configuration is set at index creation and cannot be changed afterward.
</Note>
