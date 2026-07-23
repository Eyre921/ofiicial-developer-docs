---
title: "Ingress Authentication"
source: https://developers.deepgram.com/docs/self-hosted-ingress-auth.md
path: docs/self-hosted-ingress-auth
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Ingress Authentication

However, you may have a use case where you wish to expose your Deepgram services directly to the public internet. In this case, you will need to implement additional authentication measures to secure ingress traffic to your environment.

While Deepgram's self-hosted containers do not include built-in authentication, you can implement your own authentication system, such as using API keys. This guide describes on how to set up API key authentication for your self-hosted Deepgram instance. We will focus on AWS deployments, but the general principles can be applied to other cloud providers, as well as on-premises setups.

## Why Use API Keys?

API keys provide a simple and effective way to control access to your API. They allow you to:

1. Authenticate requests
2. Track and monitor API usage
3. Revoke access when necessary

## Implementing API Key Authentication

There are several ways to implement API key authentication for your self-hosted Deepgram instance. This API key setup will be entirely separate from the Deepgram API keys [you generate in the Deepgram Console](/docs/create-additional-api-keys).

You should not expose your Deepgram API keys to a third-party. Your Deepgram API keys are a critical security component of your product's integration with Deepgram, and no other parties should have access to your Deepgram API keys.

Always use a separate set of API keys for authenticating ingress requests versus the Deepgram self-hosted API keys you use to license your Deepgram containers.

One straightforward method to implement API key authentication for your server is to use [AWS API Gateway](https://aws.amazon.com/api-gateway/).

1. Set up AWS API Gateway:

   1. Create a new API in AWS API Gateway
   2. Configure it to forward requests to your self-hosted deployment, typically either an EC2 instance or EKS cluster

2. Enable API Key Authentication:

   1. In the API Gateway settings, enable API key authentication
   2. Generate and manage API keys through the AWS console

3. Secure Your EC2 Instance:

   1. Configure your EC2 instance's security group to only allow traffic from the API Gateway
   2. This ensures that all requests must pass through the authenticated API Gateway

4. Client Usage:

   1. Provide API keys to your clients
   2. Instruct clients to include the API key in their requests to the API Gateway endpoint

If you're not using AWS, see your cloud provider's documentation for their equivalent authentication offering.

### Alternative Implementation Methods

If you prefer a different approach, you can implement API key authentication directly on your server.

Consult your internal security team before implementing your own authentication solution.

1. Modify your server configuration to check for an API key in incoming request headers
   1. Web server software, such as `nginx`, typically include request verification features
2. Store valid API keys securely, and distribute as needed
3. Verify the API key before processing the request

## Best Practices

* Regularly rotate API keys
* Use HTTPS to encrypt all API traffic
* Implement rate limiting to prevent abuse
* Monitor API usage for suspicious activity

Remember, implementing authentication is crucial for securing your self-hosted Deepgram instance. Choose a method that best fits your infrastructure and security requirements. In many cases, your security posture will be improved by designing your architecture to only access your Deepgram self-hosted services from within your private network, instead of from the public internet.

For more detailed information on AWS API Gateway and API key implementation, refer to the [AWS documentation](https://aws.amazon.com/api-gateway/).

This article provides general guidance. For specific implementation details or if you encounter issues, please consult your IT team or a cloud security professional.
