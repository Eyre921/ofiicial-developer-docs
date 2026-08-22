---
title: "SDKs"
source: https://modelcontextprotocol.io/docs/2026-07-28/sdk
path: docs/2026-07-28/sdk
---

Official SDKs for building with Model Context Protocol

Build MCP servers and clients using our official SDKs. SDKs are classified into tiers based on feature completeness, protocol support, and maintenance commitment. Learn more about [SDK tiers](/community/sdk-tiers).

## Available SDKs

| SDK                                                                              | Repository                                                                                    |                  Tier |
| :------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------- | --------------------: |
| <Icon icon="square-js" />   [TypeScript](https://ts.sdk.modelcontextprotocol.io) | [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | <Badge>Tier 1</Badge> |
| <Icon icon="python" />   [Python](https://py.sdk.modelcontextprotocol.io)        | [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)         | <Badge>Tier 1</Badge> |
| <Icon icon="square-c" />   [C#](https://csharp.sdk.modelcontextprotocol.io)      | [modelcontextprotocol/csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk)         | <Badge>Tier 1</Badge> |
| <Icon icon="golang" />   [Go](https://go.sdk.modelcontextprotocol.io)            | [modelcontextprotocol/go-sdk](https://github.com/modelcontextprotocol/go-sdk)                 | <Badge>Tier 1</Badge> |
| <Icon icon="rust" />   [Rust](https://rust.sdk.modelcontextprotocol.io)          | [modelcontextprotocol/rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)             | <Badge>Tier 1</Badge> |
| <Icon icon="java" />   [Java](https://java.sdk.modelcontextprotocol.io)          | [modelcontextprotocol/java-sdk](https://github.com/modelcontextprotocol/java-sdk)             | <Badge>Tier 2</Badge> |
| <Icon icon="gem" />   [Ruby](https://ruby.sdk.modelcontextprotocol.io)           | [modelcontextprotocol/ruby-sdk](https://github.com/modelcontextprotocol/ruby-sdk)             | <Badge>Tier 2</Badge> |
| <Icon icon="swift" />   Swift                                                    | [modelcontextprotocol/swift-sdk](https://github.com/modelcontextprotocol/swift-sdk)           | <Badge>Tier 3</Badge> |
| <Icon icon="php" />   [PHP](https://php.sdk.modelcontextprotocol.io)             | [modelcontextprotocol/php-sdk](https://github.com/modelcontextprotocol/php-sdk)               | <Badge>Tier 3</Badge> |
| <Icon icon="square-k" />   [Kotlin](https://kotlin.sdk.modelcontextprotocol.io)  | [modelcontextprotocol/kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk)         | <Badge>Tier 3</Badge> |

See [SDK Tiering System](/community/sdk-tiers) for details on what each tier means.

## Getting Started

Each SDK provides the same functionality but follows the idioms and best practices of its language. All SDKs support:

* Creating MCP servers that expose tools, resources, and prompts
* Building MCP clients that can connect to any MCP server
* Local and remote transport protocols
* Protocol compliance with type safety

Visit the SDK page for your chosen language to find installation instructions, documentation, and examples.

## Next Steps

Ready to start building with MCP? Choose your path:

<CardGroup>
  <Card title="Build a Server" icon="server" href="/docs/2026-07-28/develop/build-server">
    Learn how to create your first MCP server
  </Card>

  <Card title="Build a Client" icon="computer" href="/docs/2026-07-28/develop/build-client">
    Create applications that connect to MCP servers
  </Card>
</CardGroup>
