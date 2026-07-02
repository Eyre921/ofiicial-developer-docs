---
title: "Send emails with Resend CLI"
source: https://resend.com/docs/cli-quickstart
path: docs/cli-quickstart
---

Learn how to send your first email using the Resend CLI.

## Prerequisites

Before you start, you'll need:

* A Resend [API key](/docs/create-an-api-key)
* A [verified domain](/docs/add-a-domain)

## 1. Install

<Tabs>
  <Tab title="cURL">
    ```bash theme={"theme":{"light":"github-light","dark":"vesper"}}
    curl -fsSL https://resend.com/install.sh | bash
    ```
  </Tab>

  <Tab title="npm">
    ```bash theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install -g resend-cli
    ```
  </Tab>

  <Tab title="Homebrew">
    ```bash theme={"theme":{"light":"github-light","dark":"vesper"}}
    brew install resend/cli/resend
    ```
  </Tab>

  <Tab title="PowerShell (Windows)">
    ```powershell theme={"theme":{"light":"github-light","dark":"vesper"}}
    irm https://resend.com/install.ps1 | iex
    ```
  </Tab>
</Tabs>

## 2. Authenticate

```bash theme={"theme":{"light":"github-light","dark":"vesper"}}
resend login
```

## 3. Send email

```bash theme={"theme":{"light":"github-light","dark":"vesper"}}
resend emails send \
  --from "Acme <onboarding@resend.dev>" \
  --to delivered@resend.dev \
  --subject "Hello World" \
  --text "Sent from my terminal."
```

## Next steps

<Card title="CLI Reference" icon="terminal" href="/cli">
  Explore the full command reference, authentication options, and CI/CD
  examples.
</Card>
