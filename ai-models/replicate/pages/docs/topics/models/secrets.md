---
title: "Secrets"
source: https://replicate.com/docs/topics/models/secrets.md
path: docs/topics/models/secrets
---

When building models that need to access external services or sensitive configuration, you often need to handle secrets like API keys, authentication tokens, or passwords. For example, some models use a Hugging Face API key to publish trained model weights to the Hugging Face Hub, or a Weights & Biases API key to log training data for later inspection. Cog provides a special `Secret` input type that helps you handle sensitive information securely.

[](#what-are-secrets)What are secrets?
--------------------------------------

Secrets in Cog are input parameters that contain sensitive information that should be handled carefully. When you define an input as a `Secret`, Cog treats it specially:

*   The value is redacted in logs and outputs
*   The default string representation shows `**********` instead of the actual value
*   Model consumers can pass secrets through secure channels

[](#creating-a-model-with-secret-inputs)Creating a model with secret inputs
---------------------------------------------------------------------------

To use secrets in your model, import the `Secret` type from `cog` and use it as a parameter type in your `predict()` method:

```python
from cog import BasePredictor, Secret
class Predictor(BasePredictor):
    def predict(self, 
                prompt: str,
                api_key: Secret
    ) -> str:
        # Access the secret value using get_secret_value()
        token = api_key.get_secret_value()
        
        # Use the token to authenticate with an external service
        response = make_api_call(token, prompt)
        return response
```

### [](#key-points-for-model-authors)Key points for model authors:

*   **Import the `Secret` type**: Import `Secret` from the `cog` package
*   **Use `get_secret_value()`**: Access the actual secret value using the `.get_secret_value()` method
*   **Never log secrets**: The `Secret` type automatically redacts its value when printed, but be careful not to log the result of `get_secret_value()`
*   **Handle securely**: Use secrets only when needed and avoid storing them unnecessarily

[](#example-model-with-external-api-access)Example: Model with external API access
----------------------------------------------------------------------------------

Here’s a complete example of a model that uses a secret to authenticate with an external service:

```python
from cog import BasePredictor, Secret, Input
import requests
class Predictor(BasePredictor):
    def predict(self, 
                text: str = Input(description="Text to process"),
                api_token: Secret = Input(description="API token for the translation service")
    ) -> str:
        # Get the actual secret value
        token = api_token.get_secret_value()
        
        # Use it to authenticate with external service
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(
            "https://api.example.com/translate",
            headers=headers,
            json={"text": text}
        )
        
        return response.json()["translated_text"]
```

[](#security-considerations)Security considerations
---------------------------------------------------

*   **Never expose secrets**: The secret value should only be accessed via `get_secret_value()` and never logged or returned in outputs
*   **Validate before use**: Always validate that a secret was provided before using it
*   **Use HTTPS**: When making external API calls with secrets, always use HTTPS endpoints
*   **Handle errors carefully**: Don’t include secret values in error messages

[](#testing-your-model)Testing your model
-----------------------------------------

When testing locally with `cog predict`, you can pass secrets as regular strings:

```bash
cog predict -i text="Hello world" -i api_token="your-test-token"
```

The secret will be treated as sensitive information when the model runs on Replicate.

[](#next-steps)Next steps
-------------------------

Learn how consumers can provide secrets when running your model by reading the [prediction secrets documentation](/docs/topics/predictions/secrets).
