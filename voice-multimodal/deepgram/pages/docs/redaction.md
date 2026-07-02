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

&#x20;Pre-recorded

&#x20;Streaming:Nova

Streaming: Flux

&#x20;Specific languages only

## Language Support

Redaction language support varies by deployment type and processing method:

| Deployment Type               | Processing Method    | Language Support        |
| ----------------------------- | -------------------- | ----------------------- |
| Hosted API (api.deepgram.com) | Pre-recorded (batch) | All available languages |
| Hosted API (api.deepgram.com) | Streaming            | English only            |
| Self-hosted                   | Pre-recorded (batch) | English only            |
| Self-hosted                   | Streaming            | English only            |

## Enable Feature

To enable redaction, use the following parameter in the query string when you call Deepgram's `/listen` endpoint:

`redact=OPTION`

### Redacting Common Entities

Deepgram provides the following options to redact common groups of entities:

* `pci`: Redacts credit card information, including credit card number, expiration date, and CVV.
* `pii`: Redacts a broad range of personally identifiable information, including names, locations, and identifying numbers.
* `phi`: Redacts protected health information, including medical conditions, drugs, injuries, blood types, medical processes, and statistics.
* `numbers` (or `true`): Redacts any sequence of three or more consecutive numerals, plus the entity types in the `numbers` redaction group (dates, account numbers, credit cards, SSNs, and more).
* `aggressive_numbers`: Redacts every numeral (including single- and two-digit numbers), plus the entity types in the `numbers` redaction group.
* Multiple redaction values can be sent: `redact=pci&redact=numbers`

To see exactly which entity types are included in each group, refer to the Redaction Groups column in the [Supported Entity Types](/docs/supported-entity-types) table.

Digit-sequence redaction is independent of entity recognition. Numerals that match an entity type in the `numbers` group are tagged with the specific entity (`[CREDIT_CARD_1]`, `[SSN_1]`, etc.). Sequences caught only by the digit-length rule — three or more for `numbers`/`true`, one or more for `aggressive_numbers` — are replaced with a generic `[REDACTED]` placeholder.

### Redacting Specific Entities

You may select the types of entities you wish to redact from [over 50 supported entity types](/docs/supported-entity-types). This powerful functionality allows you total control over what is redacted in your transcript.

Some options include `credit_card`, `credit_card_expiration`, `cvv`, and `email_address`.

View all options here: [Supported Entity Types](/docs/supported-entity-types)

### Pre-Recorded Examples

You can enable redaction by adding `redact=OPTION` as a query parameter.

To transcribe audio and remove `PCI` data from an audio file run the following cURL command:

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?redact=pci'
```

Multiple types of entities can be redacted with the syntax `redact=option_1&redact=option_2`. To transcribe audio and remove `PCI` and `PII` data from an audio file run the following cURL command:

```bash cURL
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @youraudio.wav \
  --url 'https://api.deepgram.com/v1/listen?redact=pci&redact=pii'
```

Replace `YOUR_DEEPGRAM_API_KEY` with your [Deepgram API Key](/docs/create-additional-api-keys).

### Streaming Examples

To ensure redaction operates with the highest accuracy, set `no_delay=false` or avoid including `no_delay` altogether. If `no_delay=true` is set, our system will opt for low latency at the risk of redaction performance.

In streaming redaction, Deepgram follows a two-phase approach. During interim results, the system returns a generic `[REDACTED]` placeholder for a redacted entity while it continues evaluating the spoken content. Once a segment is considered complete and Deepgram has high confidence in the detected entity, the placeholder is replaced with a specific entity tag (for example, `[CREDIT_CARD_1]`, `[SSN_1]`, or `[PHONE_NUMBER_1]`). This replacement may occur in a later interim result or in the final result. This approach enables real-time transcription with both low latency and accurate, contextual redaction.

## Results

For both Live-streaming and Pre-recorded audio, Redaction replaces redacted content with the type of entity redacted and the number of times that entity has been detected in the transcript. For example, if you choose to redact social security numbers, the phrase "My social security number is five five five two two one one one one and his is six six six two two one three three three" would appear in your transcript as "My social security number is \[SSN\_1] and his is \[SSN\_2]".

Example with `redact=pci&redact=pii`:

| Source                                                                                                                                                                                                                                                                                                                                                                                   | Before redact                                                                                                                                                                                                                                                                                                                                                                            | After redact                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| my credit card number is four four four four nine nine nine nine three three three three two two two two with an expiration date of one twenty three and the cvv code is one one one i live at one two three main street dallas texas seven five two zero one my phone number is five five five two one two nine three three three my date of birth is july twelfth nineteen seventy six | my credit card number is four four four four nine nine nine nine three three three three two two two two with an expiration date of one twenty three and the cvv code is one one one i live at one two three main street dallas texas seven five two zero one my phone number is five five five two one two nine three three three my date of birth is july twelfth nineteen seventy six | my credit card number is \[CREDIT\_CARD\_1] with an expiration date of \[CREDIT\_CARD\_EXPIRATION\_1] and the cv code is \[CVV\_1] i live at \[LOCATION\_ADDRESS\_1] my phone number is \[PHONE\_NUMBER\_1] my date of birth is \[DOB\_1] |
