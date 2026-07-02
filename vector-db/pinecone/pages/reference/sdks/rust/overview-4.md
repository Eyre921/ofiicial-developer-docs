---
title: "Pinecone Rust SDK"
source: https://docs.pinecone.io/reference/sdks/rust/overview
path: reference/sdks/rust/overview
---

Install and use the Pinecone SDK for Pinecone Rust SDK: auth, typed clients, and API operations. The Rust SDK is in alpha and under active development. It.

<Warning>
  The Rust SDK is in alpha and under active development. It should be considered unstable and not used in production. Before a 1.0 release, there are no guarantees of backward compatibility between minor versions.
</Warning>

<Tip>
  For installation instructions and usage examples, see the [Rust SDK README](https://github.com/pinecone-io/pinecone-rust-client). To report an issue or request a feature, [file an issue on GitHub](https://github.com/pinecone-io/pinecone-rust-client/issues).
</Tip>

## Install

To install the latest version of the [Rust SDK](https://github.com/pinecone-io/pinecone-rust-client), add a dependency to the current project:

```shell theme={null}
cargo add pinecone-sdk
```

## Initialize

Once installed, you can import the SDK and then use an [API key](/guides/production/security-overview#api-keys) to initialize a client instance:

```rust Rust theme={null}
use pinecone_sdk::pinecone::PineconeClientConfig;   
use pinecone_sdk::utils::errors::PineconeError;
	
#[tokio::main]
async fn main() -> Result<(), PineconeError> {
    let config = PineconeClientConfig {
        api_key: Some("YOUR_API_KEY".to_string()),
        ..Default::default()
    };

    let pinecone = config.client()?;
    let indexes = pinecone.list_indexes().await?;

    println!("Indexes: {:?}", indexes);

    Ok(())
}
```
