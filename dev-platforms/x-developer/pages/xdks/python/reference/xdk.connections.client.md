---
title: "ConnectionsClient"
source: https://docs.x.com/xdks/python/reference/xdk.connections.client
path: xdks/python/reference/xdk.connections.client
---

Reference for the connections.client Python module in the X API SDK. Client class and methods for calling the connections endpoints of the X API v2.

## ConnectionsClient

<Badge>Class</Badge>

<Badge>Bases: object</Badge>

Client for connections operations

## Constructors

### `__init__`

#### Parameters

<ParamField type="Client" />

### `delete_all`

Terminate all connections
Terminates all active streaming connections for the authenticated application.
:returns: Response data
:rtype: DeleteAllResponse

#### Returns

`DeleteAllResponse`
