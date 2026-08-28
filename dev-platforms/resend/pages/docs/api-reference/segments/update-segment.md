---
title: "Update Segment"
source: https://resend.com/docs/api-reference/segments/update-segment
path: docs/api-reference/segments/update-segment
---

PATCH /segments/:segment_id
Update an existing segment.

## Path Parameters

<ResendParamField type="string">
  The Segment ID.
</ResendParamField>

## Body Parameters

<ParamField type="string">
  The name of the segment.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.segments.update(
    '78261eea-8f8b-4381-83c6-79fa7120f1cf',
    {
      name: 'Active Users',
    },
  );
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"vesper"}}
  import resend

  resend.api_key = 're_xxxxxxxxx'

  params: resend.Segments.UpdateParams = {
      "name": "Active Users",
  }

  segment = resend.Segments.update('78261eea-8f8b-4381-83c6-79fa7120f1cf', params)
  ```

  ```ruby Ruby theme={"theme":{"light":"github-light","dark":"vesper"}}
  require "resend"

  Resend.api_key = "re_xxxxxxxxx"

  params = {
    segment_id: "78261eea-8f8b-4381-83c6-79fa7120f1cf",
    name: "Active Users"
  }
  Resend::Segments.update(params)
  ```

  ```go Go theme={"theme":{"light":"github-light","dark":"vesper"}}
  package main

  import (
  	"context"
  	"fmt"

  	"github.com/resend/resend-go/v3"
  )

  func main() {
  	ctx := context.TODO()
  	client := resend.NewClient("re_xxxxxxxxx")

  	params := &resend.UpdateSegmentRequest{
  		Name: "Active Users",
  	}

  	segment, err := client.Segments.UpdateWithContext(ctx, "78261eea-8f8b-4381-83c6-79fa7120f1cf", params)
  	if err != nil {
  		panic(err)
  	}
  	fmt.Println(segment)
  }
  ```

  ```csharp .NET theme={"theme":{"light":"github-light","dark":"vesper"}}
  using Resend;

  IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

  var resp = await resend.SegmentUpdateAsync( new Guid( "78261eea-8f8b-4381-83c6-79fa7120f1cf" ), new SegmentData() {
    Name = "Active Users",
  } );
  Console.WriteLine( "Segment Id={0}", resp.Content.Id );
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X PATCH 'https://api.resend.com/segments/78261eea-8f8b-4381-83c6-79fa7120f1cf' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d $'{
    "name": "Active Users"
  }'
  ```

  ```bash CLI theme={"theme":{"light":"github-light","dark":"vesper"}}
  resend segments update 78261eea-8f8b-4381-83c6-79fa7120f1cf --name "Active Users"
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "segment",
    "id": "78261eea-8f8b-4381-83c6-79fa7120f1cf"
  }
  ```
</ResponseExample>
