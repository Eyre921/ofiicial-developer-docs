---
title: "Secrets"
source: https://replicate.com/docs/topics/predictions/secrets.md
path: docs/topics/predictions/secrets
---

Some models require sensitive information like API keys, authentication tokens, or passwords to function properly. For example, some models need a Hugging Face API key to publish trained model weights to the Hugging Face Hub, or a Weights & Biases API key to log training data for later inspection. When a model has secret inputs, you can provide them securely through Replicate’s web interface or API.

[](#what-are-secret-inputs)What are secret inputs?
--------------------------------------------------

Secret inputs are model parameters marked with the `Secret` type that contain sensitive information. These inputs are handled specially by Replicate:

*   Values are redacted in logs and prediction metadata after being sent to the model
*   The web interface shows password-style input fields for secrets
*   API responses never include the secret values

[](#providing-secrets-via-the-web-interface)Providing secrets via the web interface
-----------------------------------------------------------------------------------

When you run a model with secret inputs on replicate.com:

1.  Navigate to the model page
2.  Secret inputs will appear as password fields (showing dots instead of characters as you type)
3.  Enter your secret values and run the prediction
4.  The secret values will be redacted from the prediction details after the model receives them

[](#providing-secrets-via-the-api)Providing secrets via the API
---------------------------------------------------------------

When using the Replicate API, you should provide secrets using environment variables rather than hardcoding them. Here’s how:

```bash
# Use your secret from an environment variable
curl -X POST \
  -H "Authorization: Token $REPLICATE_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
      "prompt": "Hello world",
      "api_key": "'$MODEL_API_KEY'"
    }
  }' \
  https://api.replicate.com/v1/models/owner/model-name/predictions
```

### [](#using-client-libraries)Using client libraries

**Python:**

```python
import replicate
import os
output = replicate.run(
    "owner/model-name",
    input={
        "prompt": "Hello world",
        "api_key": os.environ["MODEL_API_KEY"]
    }
)
```

**Node.js:**

```javascript
const replicate = new Replicate();
const output = await replicate.run(
    "owner/model-name",
    {
        input: {
            prompt: "Hello world",
            api_key: process.env.MODEL_API_KEY
        }
    }
);
```

[](#identifying-secret-inputs)Identifying secret inputs
-------------------------------------------------------

You can identify which inputs are secrets by looking at the model’s schema:

*   In the web interface, secret inputs appear as password fields
*   In the API, secret inputs have `"x-cog-secret": true` in their OpenAPI schema
*   The input type will be `"string"` with `"format": "password"`

[](#security-considerations)Security considerations
---------------------------------------------------

*   **Never hardcode secrets**: Always store secrets in environment variables, never commit them to version control
*   **Secrets are redacted after use**: Once the model receives your secret, it’s removed from Replicate’s systems
*   **Rotate secrets regularly**: If you suspect a secret has been compromised, rotate it immediately
*   **Trust model authors**: Only provide secrets to models from authors you trust, as they could potentially misuse them

[](#best-practices)Best practices
---------------------------------

### [](#store-secrets-securely)Store secrets securely

Instead of hardcoding secrets in your code:

```python
# Don't do this
output = replicate.run("model", input={"api_key": "sk-abc123..."})
# Do this instead
import os
output = replicate.run("model", input={"api_key": os.environ["API_KEY"]})
```

### [](#validate-secret-requirements)Validate secret requirements

Before running a model, check if it requires secrets and ensure you have them available:

```python
import replicate
# Get model information
model = replicate.models.get("owner/model-name")
schema = model.latest_version.openapi_schema
# Check for secret inputs
secret_inputs = []
for param, details in schema["components"]["schemas"]["Input"]["properties"].items():
    if details.get("x-cog-secret"):
        secret_inputs.append(param)
if secret_inputs:
    print(f"This model requires these secrets: {secret_inputs}")
```

### [](#handle-errors-gracefully)Handle errors gracefully

Models may fail if required secrets are missing or invalid:

```python
import os
try:
    output = replicate.run("model", input={"api_key": os.environ["MODEL_API_KEY"]})
except Exception as e:
    if "authentication" in str(e).lower():
        print("Invalid API key provided")
    else:
        print(f"Error: {e}")
```

[](#next-steps)Next steps
-------------------------

*   Learn how model authors implement secret inputs in the [model secrets documentation](/docs/topics/models/secrets)
*   Read about [input files](/docs/topics/predictions/input-files) for handling file uploads
*   Explore [prediction lifecycle](/docs/topics/predictions/lifecycle) to understand how predictions work
