---
title: "NFS Server Access"
source: https://docs.turso.tech/agentfs/guides/nfs
path: agentfs/guides/nfs
---

Export AgentFS over the network via NFS

AgentFS can expose filesystems over NFS, enabling remote access from other machines, containers, or virtual machines.

## Starting the NFS Server

```bash theme={null}
agentfs serve nfs my-agent
```

By default, this listens on `127.0.0.1:11111`.

### Binding to All Interfaces

To allow remote access:

```bash theme={null}
agentfs serve nfs my-agent --bind 0.0.0.0 --port 2049
```

<Warning>
  Exposing NFS on `0.0.0.0` makes the filesystem accessible to anyone who can reach your machine. Use firewall rules or a VPN for production deployments.
</Warning>

## Mounting the Filesystem

### From the Same Machine

```bash theme={null}
mkdir /mnt/agentfs
mount -t nfs -o vers=3,tcp,port=11111,mountport=11111,nolock 127.0.0.1:/ /mnt/agentfs
```

### From a Remote Machine

```bash theme={null}
mount -t nfs -o vers=3,tcp,port=2049,mountport=2049,nolock server-ip:/ /mnt/agentfs
```

### Mount Options Explained

| Option            | Description                        |
| ----------------- | ---------------------------------- |
| `vers=3`          | Use NFSv3 protocol                 |
| `tcp`             | Use TCP transport                  |
| `port=11111`      | NFS server port                    |
| `mountport=11111` | Mount protocol port                |
| `nolock`          | Disable file locking (single-user) |

## Unmounting

```bash theme={null}
umount /mnt/agentfs
```

If the mount is busy:

```bash theme={null}
umount -f /mnt/agentfs  # Force unmount
# or
umount -l /mnt/agentfs  # Lazy unmount
```

## Next Steps

<CardGroup>
  <Card title="MCP Server" icon="plug" href="/agentfs/guides/mcp">
    Expose AgentFS via MCP
  </Card>

  <Card title="Sync with Turso Cloud" icon="cloud" href="/agentfs/guides/sync">
    Back up and share agent state
  </Card>
</CardGroup>
