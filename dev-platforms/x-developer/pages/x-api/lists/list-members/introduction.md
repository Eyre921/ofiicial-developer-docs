---
title: "List Members"
source: https://docs.x.com/x-api/lists/list-members/introduction
path: x-api/lists/list-members/introduction
---

The List Members endpoints let you view List members, add members to your Lists, and remove. Reference for the X API v2 standard tier covering list members.

The List Members endpoints let you view List members, add members to your Lists, and remove them. You can also see which Lists a user is a member of.

## Overview

<CardGroup>
  <Card title="View members" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-people.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=9d5f3f82edcd2a4070364193436e7980">
    Get all members of a List
  </Card>

  <Card title="Add member" icon="user-plus">
    Add a user to your List
  </Card>

  <Card title="Remove member" icon="user-minus">
    Remove a user from your List
  </Card>

  <Card title="Memberships" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-bulleted-list.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=b9bf8323233df59c682b0fec8e3f88d5">
    See Lists a user is on
  </Card>
</CardGroup>

***

## Endpoints

### List members lookup

| Method | Endpoint                                                             | Description            |
| :----- | :------------------------------------------------------------------- | :--------------------- |
| GET    | [`/2/lists/:id/members`](/x-api/lists/get-list-members)              | Get members of a List  |
| GET    | [`/2/users/:id/list_memberships`](/x-api/users/get-list-memberships) | Get Lists a user is on |

### Manage List members

| Method | Endpoint                                                           | Description     |
| :----- | :----------------------------------------------------------------- | :-------------- |
| POST   | [`/2/lists/:id/members`](/x-api/lists/add-list-member)             | Add a member    |
| DELETE | [`/2/lists/:id/members/:user_id`](/x-api/lists/remove-list-member) | Remove a member |

***

## Example: Get List members

```bash theme={null}
curl "https://api.x.com/2/lists/1234567890/members?\
user.fields=username,verified" \
  -H "Authorization: Bearer $BEARER_TOKEN"
```

## Example: Add a member

```bash theme={null}
curl -X POST "https://api.x.com/2/lists/1234567890/members" \
  -H "Authorization: Bearer $USER_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "9876543210"}'
```

***

## Getting started

<Note>
  **Prerequisites**

  * An approved [developer account](https://developer.x.com/en/portal/petition/essential/basic-info)
  * A [Project and App](/resources/fundamentals/developer-apps) in the Developer Console
  * Your App's [keys and tokens](/resources/fundamentals/authentication)
</Note>

<CardGroup>
  <Card title="Lookup quickstart" icon="https://mintcdn.com/x-preview/SxzTbJaLjs3MidH1/icons/xds/icon-people.svg?fit=max&auto=format&n=SxzTbJaLjs3MidH1&q=85&s=9d5f3f82edcd2a4070364193436e7980" href="/x-api/lists/list-members/quickstart/list-members-lookup">
    Get members of a List
  </Card>

  <Card title="Manage quickstart" icon="user-plus" href="/x-api/lists/list-members/quickstart/manage-list-members">
    Add and remove members
  </Card>

  <Card title="Integration guide" icon="https://mintcdn.com/x-preview/Vn2KEkZaPF9LiPi3/icons/xds/icon-book.svg?fit=max&auto=format&n=Vn2KEkZaPF9LiPi3&q=85&s=22ac564792481d14ae36a941546039c8" href="/x-api/lists/list-members/integrate">
    Key concepts and best practices
  </Card>

  <Card title="API Reference" icon="https://mintcdn.com/x-preview/ygI6sSJPehlc0qNT/icons/xds/icon-code.svg?fit=max&auto=format&n=ygI6sSJPehlc0qNT&q=85&s=488e23401b19225b89acc0136d242219" href="/x-api/lists/get-list-members">
    Full endpoint documentation
  </Card>
</CardGroup>
