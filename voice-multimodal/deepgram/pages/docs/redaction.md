---
title: "Redaction"
source: https://developers.deepgram.com/docs/redaction.md
path: docs/redaction
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Redaction

* [Try Redaction in the Playground](https://playground.deepgram.com/?endpoint=listen\&redact=pci\&language=en\&model=nova-3)

`redact` *string* Default: `False`

Pre-recorded  Streaming:Nova Streaming:Flux  Specific languages only

## Redaction options

Redaction has two kinds:

* **Number redaction** (`numbers`, `true`, `aggressive_numbers`) — redacts numeric sequences such as account and card numbers.
* **Entity redaction** (`pci`, `pii`, `phi`, and specific entity types) — redacts recognized entities such as names, addresses, and PHI. Available for English only.

### Redaction groups

Deepgram provides the following options to redact common groups of entities:

* `pci`: Redacts credit card information, including credit card number, expiration date, and CVV.
* `pii`: Redacts a broad range of personally identifiable information, including names, locations, and identifying numbers.
* `phi`: Redacts protected health information, including medical conditions, drugs, injuries, blood types, medical processes, and statistics.
* `numbers` (or `true`): Redacts any sequence of three or more consecutive numerals, plus the entity types in the `numbers` redaction group (dates, account numbers, credit cards, SSNs, and more).
* `aggressive_numbers`: Redacts every numeral (including single- and two-digit numbers), plus the entity types in the `numbers` redaction group.

To see exactly which entity types are included in each group, refer to the Redaction Groups column in the [Supported Entity Types](/docs/supported-entity-types) table.

### Specific entity types

You may select the types of entities you wish to redact from [over 50 supported entity types](/docs/supported-entity-types). Some options include `credit_card`, `credit_card_expiration`, `cvv`, and `email_address`.

Specific entity types rely on entity recognition and are available for English only.

## Enable redaction

To enable redaction, add the `redact` parameter to the query string when you call Deepgram's `/listen` endpoint:

`redact=OPTION`

Send multiple redaction values by repeating the parameter: `redact=pci&redact=numbers`.

## Examples

To transcribe pre-recorded audio and remove `PCI` data from a file, run:

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?redact=pci'
```

To remove both `PCI` and `PII` data, repeat the parameter:

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?redact=pci&redact=pii'
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys).

## How redacted output looks

Redaction replaces redacted content with the type of entity redacted and the number of times that entity has been detected in the transcript. For example, if you redact social security numbers, the phrase "My social security number is five five five two two one one one one and his is six six six two two one three three three" appears in your transcript as "My social security number is \[SSN\_1] and his is \[SSN\_2]".

Numerals that match an entity type in the `numbers` group are tagged with the specific entity (`[CREDIT_CARD_1]`, `[SSN_1]`, etc.). Sequences caught only by the digit-length rule — three or more numerals for `numbers`/`true`, one or more for `aggressive_numbers` — are replaced with a generic `[REDACTED]` placeholder.

On Nova streaming (`/v1/listen`), Deepgram follows a two-phase approach. During interim results, the system returns a generic `[REDACTED]` placeholder while it continues evaluating the spoken content. Once a segment is complete and Deepgram has high confidence in the detected entity, the placeholder is replaced with a specific entity tag. This replacement may occur in a later interim result or in the final result.

For the highest streaming redaction accuracy, set `no_delay=false` or omit `no_delay` entirely. Setting `no_delay=true` opts for low latency at the risk of redaction performance.

Flux (`/v2/listen`) uses a different output format — see [Redaction on Flux](#redaction-on-flux).

Example with `redact=pci&redact=pii`:

| Source                                                                                                                                                                                                                                                                                                                                                                                   | Before redact                                                                                                                                                                                                                                                                                                                                                                            | After redact                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| my credit card number is four four four four nine nine nine nine three three three three two two two two with an expiration date of one twenty three and the cvv code is one one one i live at one two three main street dallas texas seven five two zero one my phone number is five five five two one two nine three three three my date of birth is july twelfth nineteen seventy six | my credit card number is four four four four nine nine nine nine three three three three two two two two with an expiration date of one twenty three and the cvv code is one one one i live at one two three main street dallas texas seven five two zero one my phone number is five five five two one two nine three three three my date of birth is july twelfth nineteen seventy six | my credit card number is \[CREDIT\_CARD\_1] with an expiration date of \[CREDIT\_CARD\_EXPIRATION\_1] and the cv code is \[CVV\_1] i live at \[LOCATION\_ADDRESS\_1] my phone number is \[PHONE\_NUMBER\_1] my date of birth is \[DOB\_1] |

## Language support

Redaction language coverage differs by kind and deployment:

| Environment                                | Number redaction                     | Entity redaction |
| ------------------------------------------ | ------------------------------------ | ---------------- |
| Hosted API — pre-recorded                  | All available languages              | English only     |
| Hosted API — Nova streaming (`/v1/listen`) | 12 languages (see below)             | English only     |
| Hosted API — Flux streaming (`/v2/listen`) | `numbers`, `aggressive_numbers` only | Not supported    |
| Self-hosted — pre-recorded and streaming   | English only                         | English only     |

Pre-recorded (batch) number redaction is available for all supported languages. In streaming, it is limited to:

Danish, Dutch, English, French, German, German (Swiss), Italian, Norwegian, Polish, Portuguese, Spanish, and Swedish.

On multilingual models (`language=multi`), each word is redacted using its detected language's number rules, so a single transcript can mix languages. In streaming, detected languages outside the set above fall back to English number rules.

For non-English audio, only numbers are redacted. Entity redaction — names, addresses, PHI, and other `pii`/`phi` entities — is applied for English only, even when you request `true`.

## Redaction on Flux

Flux (`/v2/listen`) supports **number redaction only**. `redact` accepts `numbers` and `aggressive_numbers`; any other value — including `true`, `pci`, `pii`, `phi`, and specific entity types such as `ssn` or `credit_card` — is rejected: the WebSocket connection fails to open with an HTTP `400` at connection time rather than being silently ignored. Use Nova streaming or pre-recorded for entity redaction.

Number redaction works on both `flux-general-en` and `flux-general-multi`. Because Flux does not produce word-level language tags, number redaction is applied across every language detected in the transcript.

Currently, Flux replaces each redacted span with a single `*` (for example, `my phone number is *`) rather than the `[REDACTED]` placeholder or specific entity tags (such as `[CREDIT_CARD_1]`) used by Nova — Flux performs digit redaction only, without entity recognition. Treat the redacted text as removed rather than depending on this exact placeholder format, which may change.
