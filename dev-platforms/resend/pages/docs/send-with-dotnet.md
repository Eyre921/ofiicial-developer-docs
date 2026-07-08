---
title: "Send emails with .NET"
source: https://resend.com/docs/send-with-dotnet
path: docs/send-with-dotnet
---

Learn how to send your first email using the Resend .NET SDK.

## Prerequisites

Before you start, you'll need:

* A Resend [API key](/docs/create-an-api-key)
* A [verified domain](/docs/add-a-domain)

Prefer watching a video? Check out our video walkthrough below.

<YouTube />

## Guide

<Steps>
  <Step title="Install">
    <CodeGroup>
      ```bash dotnet CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
      dotnet add package Resend
      ```

      ```bash Visual Studio (Package Manager Console) theme={"theme":{"light":"github-light","dark":"vesper"}}
      PM> Install-Package Resend
      ```
    </CodeGroup>
  </Step>

  <Step title="Send emails using HTML">
    In the startup of your application, configure the DI container as follows:

    ```csharp theme={"theme":{"light":"github-light","dark":"vesper"}}
    using Resend;

    builder.Services.AddOptions();
    builder.Services.AddHttpClient<ResendClient>();
    builder.Services.Configure<ResendClientOptions>( o =>
    {
        o.ApiToken = Environment.GetEnvironmentVariable( "RESEND_APITOKEN" )!;
    } );
    builder.Services.AddTransient<IResend, ResendClient>();
    ```

    Send an email using the injected `IResend` instance:

    ```csharp theme={"theme":{"light":"github-light","dark":"vesper"}}
    using Resend;

    public class FeatureImplementation
    {
        private readonly IResend _resend;


        public FeatureImplementation( IResend resend )
        {
            _resend = resend;
        }


        public Task Execute()
        {
            var message = new EmailMessage();
            message.From = "Acme <onboarding@resend.dev>";
            message.To.Add( "delivered@resend.dev" );
            message.Subject = "hello world";
            message.HtmlBody = "<strong>it works!</strong>";

            await _resend.EmailSendAsync( message );
        }
    }
    ```
  </Step>
</Steps>

## Examples

<CardGroup>
  <Card title="Basic Send" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/blob/main/dotnet-resend-examples/Examples/BasicSend.cs">
    Basic email sending
  </Card>

  <Card title="Attachments" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/blob/main/dotnet-resend-examples/Examples/WithAttachments.cs">
    Send emails with file attachments
  </Card>

  <Card title="Templates" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/blob/main/dotnet-resend-examples/Examples/WithTemplate.cs">
    Send emails using Resend hosted templates
  </Card>

  <Card title="Scheduling" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/blob/main/dotnet-resend-examples/Examples/ScheduledSend.cs">
    Schedule emails for future delivery
  </Card>

  <Card title="Audiences" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/blob/main/dotnet-resend-examples/Examples/Audiences.cs">
    Manage contacts and audiences
  </Card>

  <Card title="Domains" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/blob/main/dotnet-resend-examples/Examples/Domains.cs">
    Create and manage sending domains
  </Card>

  <Card title="Inbound Webhooks" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/blob/main/dotnet-resend-examples/Examples/Inbound.cs">
    Receive and process inbound emails
  </Card>

  <Card title="Double Opt-in" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/blob/main/dotnet-resend-examples/Examples/DoubleOptinSubscribe.cs">
    Double opt-in subscription flow
  </Card>

  <Card title="Minimal API App" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/tree/main/dotnet-resend-examples/MinimalApiApp">
    ASP.NET Minimal API application
  </Card>

  <Card title="MVC App" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-examples/tree/main/dotnet-resend-examples/MvcApp">
    ASP.NET MVC application
  </Card>
</CardGroup>
