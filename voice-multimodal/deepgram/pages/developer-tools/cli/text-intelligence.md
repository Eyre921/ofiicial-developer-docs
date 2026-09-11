---
title: "Text Intelligence Commands"
source: https://developers.deepgram.com/developer-tools/cli/text-intelligence.md
path: developer-tools/cli/text-intelligence
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Text Intelligence Commands

## Basic Analysis

```shell
dg read "Customer called about a billing issue."
```

## Analyze a File

```shell
dg read --file document.txt
```

## Piped Input

```shell
cat transcript.txt | dg read
echo "Your text here" | dg read
```

## Available Features

### Sentiment Analysis

```shell
dg read --file document.txt --sentiment
```

Output includes overall document sentiment and its score.

### Topic Detection

```shell
dg read --file document.txt --topics
```

Returns detected topics with confidence scores.

### Summarization

```shell
dg read --file document.txt --summarize
```

Generates a brief summary of the content.

### Intent Recognition

```shell
dg read --file document.txt --intents
```

Detects user intents within the text.

### Full Analysis

```shell
dg read --file document.txt --sentiment --topics --summarize --intents
```

## Output Format

```shell
dg -o json read --file document.txt    # JSON
dg -o yaml read --file document.txt    # YAML
dg -o table read --file document.txt   # Formatted terminal table
dg -o csv read --file document.txt     # CSV
```

`-o` belongs to `dg` itself, so it goes before the subcommand name. Without it, `dg read` prints human-readable output.

## Use Cases

### Summarize Transcripts

```shell
dg listen meeting.mp3 | dg read --summarize
```

### Analyze Customer Feedback

```shell
dg read --file feedback.txt --sentiment --topics
```
