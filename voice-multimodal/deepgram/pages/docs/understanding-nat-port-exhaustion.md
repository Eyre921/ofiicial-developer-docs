---
title: "Understanding NAT Port Exhaustion"
source: https://developers.deepgram.com/docs/understanding-nat-port-exhaustion.md
path: docs/understanding-nat-port-exhaustion
---

> For clean Markdown of any page, append .md to the page URL.
> For a complete documentation index, see https://developers.deepgram.com/llms.txt.
> For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://developers.deepgram.com/_mcp/server.

# Understanding NAT Port Exhaustion

When applications connect to Deepgram from a cloud or on-premises environment that sits behind a Network Address Translation (NAT) device, misconfigured or undersized NAT can cause intermittent connection timeouts and WebSocket handshake failures. These problems typically arise before traffic ever reaches Deepgram's infrastructure.

This document explains:

* What NAT port exhaustion is
* Why it tends to surface with real-time speech workloads
* How to identify and troubleshoot the issue (including AWS, GCP, and Azure specifics)
* What changes to consider in your environment to eliminate these failures

***

## What is NAT Port Exhaustion?

### How NAT works

A NAT gateway lets many private hosts share a smaller pool of public IP addresses by rewriting outbound connections:

* Each outbound connection is represented as:

  `(public IP, ephemeral source port) → (destination IP, destination port)`

Managed NAT solutions (GCP Cloud NAT, Azure SNAT/NAT Gateway, AWS NAT Gateway, firewalls, etc.) have:

* A finite number of ports per public IP
* Idle / TIME\_WAIT timers that keep ports reserved for some time after a connection closes
* Often, per-destination and per-IP limits, which can be hit even if overall utilization looks low

### What "NAT port exhaustion" means

NAT port exhaustion / aggressive port reuse occurs when the NAT device:

* Has too few ports and/or too few public IPs for the actual connection pattern, and/or
* Holds ports in TIME\_WAIT for a long time, and/or
* Is asked to handle many short-lived connections opened and closed in quick succession (for example, frequent WebSocket opens/closes, or very bursty HTTP traffic)

Once the NAT runs out of usable (public IP, port) combinations to a destination:

* New connections may never leave your network
* You may see:
  * TCP SYN retransmits
  * Delayed or missing SYN-ACKs from the remote side
  * Application-level "connect timed out" / handshake failures
* On the Deepgram side, we often see no corresponding HTTP/WebSocket requests at all for the failing attempts, because they never reach our edge

In other words: the symptoms appear as connectivity problems *with* Deepgram, but the failure point is actually within the NAT layer that sits in front of your workloads.

***

## Why Real-Time Speech Workloads Stress NAT

Real-time speech applications (voice agents, contact centers, streaming STT/TTS) often:

* Open many concurrent WebSocket or HTTPS connections
* Use short-lived sessions (for example, a new WebSocket per call, or even per interaction)
* Implement immediate retries on failure

This pattern can be NAT-intensive:

* Each new connection consumes an ephemeral port on the NAT
* Short idle timers on the application side don't necessarily align with NAT TIME\_WAIT behavior
* Aggressive retry loops can repeatedly hit the same ports/IPs

When combined with a small NAT IP/port pool or long TCP idle timers, this creates a situation where NAT ports are frequently re-used for new connections *before* the previous flows are fully torn down at the network layer.

That's the essence of NAT port exhaustion.

***

## How to Recognize NAT Port Exhaustion

### Common application-level symptoms

If you see some or all of the following, NAT port exhaustion is a strong suspect:

* Intermittent connection failures during:
  * WebSocket handshake / upgrade
  * Initial HTTP(S) connection to Deepgram endpoints
* "Connect timed out" or similar errors while attempting to establish the connection
* Failures that:
  * Are more frequent under higher load or during spikes
  * Sometimes appear to affect only some of the Deepgram IPs/regions

From Deepgram's perspective, typical signs include:

* No logged requests for many of the failing attempts (they never reached our edge)
* Healthy behavior for other customers and traffic during the same time window

### Network-level symptoms

On the network side (in pcaps and NAT logs), you may observe:

* TCP SYN retransmits from your hosts, with no timely SYN-ACK response
* Delayed SYN-ACKs that arrive after the client has already given up on the connection
* Repeated reuse of the same NAT source port (same public IP + port) to the same Deepgram destination across overlapping time windows
* NAT logs reporting:
  * Port allocation failures (for example, "out of ports", "NatAllocationFailed")
  * High port utilization for a small subset of IPs

These are exactly the patterns cloud NAT troubleshooting guides call out as red flags.

***

## Provider-Specific Considerations

### Google Cloud Platform (GCP)

#### Architectures to clarify

When troubleshooting on GCP, it's important to answer:

* Are workloads running:
  * Behind Cloud NAT for GCE/GKE?
  * Behind GKE default NAT?
  * On Cloud Run with default/shared NAT, or behind a dedicated Cloud NAT gateway?
* How many public IPs does the NAT gateway have?
* What is the configured minimum ports per VM/instance?

Environments that rely on shared NAT (e.g., default Cloud Run NAT) and have no visibility into port allocation or TIME\_WAIT behavior are much harder to tune.

#### What to check

In Cloud NAT / GKE scenarios, we recommend:

1. **Enable Cloud NAT logging** (if not already enabled)
   * Look for:
     * `NatAllocationFailed` or similar events
     * Spikes in NAT allocation failures around the times you see connection issues
2. **Review Cloud NAT configuration**
   * Min ports per VM / instance:
     * Is this large enough for your worst-case concurrency and retry behavior?
   * Number of NAT IPs:
     * A single NAT IP can become a bottleneck, even when aggregate utilization seems low
   * TCP idle / TIME\_WAIT settings:
     * Longer TIME\_WAIT → ports held longer → higher chance of collisions under churn
3. **Look for forced / narrow source port ranges**
   * Make sure applications or load-testing tools are not forcing a tiny local port range (e.g., `-local-port 7000-7000`)
   * Allowing the OS to choose from the full ephemeral port range spreads load much more safely
4. **Comparative testing**
   * Run simple HTTPS/WebSocket connectivity tests:
     * Once from a VM that has a dedicated external IP (bypassing Cloud NAT as much as possible)
     * Once through the existing Cloud NAT / firewall path
   * If direct traffic is consistently healthy and NAT-routed traffic is not, that strongly points at a NAT configuration or capacity issue.

#### Google Cloud Run specifics

For Cloud Run:

* The default model uses a shared, provider-managed NAT where:
  * Port allocation and TIME\_WAIT behavior are opaque
  * You cannot easily tune NAT settings
* For latency-sensitive, high-throughput workloads, we recommend:
  * Running Cloud Run with VPC egress and
  * Using a dedicated Cloud NAT gateway with:
    * Sufficient IPs
    * Adequate min-ports per instance
    * Appropriate TCP idle timers

***

### Microsoft Azure

#### SNAT vs. NAT Gateway

Azure environments can use:

* Implicit SNAT via load balancers/firewalls, or
* The more modern Azure NAT Gateway

From a reliability perspective:

* NAT Gateway generally offers greater capacity, more predictable behavior, and clearer metrics.
* Legacy/implicit SNAT configurations are more likely to suffer from localized exhaustion that's hard to see from aggregate dashboards.

#### What to check

On Azure, we recommend:

1. **Determine the egress path**
   * Are you relying on SNAT via a firewall/load balancer?
   * Have you deployed Azure NAT Gateway with explicit outbound IP ranges?
2. **Inspect SNAT utilization in context**
   * Aggregate SNAT charts (e.g., "never above 7% utilized") can be misleading.
   * Focus on:
     * Specific outbound IPs used to reach Deepgram
     * Per-destination behavior (Deepgram IP ranges)
     * Short spikes and uneven distribution across IPs
3. **Capture and analyze traffic**
   * Capture packets from the outbound IP ranges used to reach Deepgram.
   * In Wireshark/tshark, filter to Deepgram IPs and check for:
     * Source port reuse on still-active connections or within TIME\_WAIT
     * SYN retransmits with delayed or missing SYN-ACKs
4. **Consider Azure NAT Gateway**
   * For more predictable behavior, we recommend:
     * Migrating outbound egress to Azure NAT Gateway
     * Assigning multiple NAT IPs scaled for peak concurrency
     * Verifying:
       * Balanced distribution across IPs
       * Healthy port utilization without rapid reuse for the same destination

***

### Amazon Web Services (AWS)

On AWS, workloads on ECS/Fargate or EC2 usually reach Deepgram through a NAT Gateway, commonly deployed as one gateway per Availability Zone and shared across many tasks. Because a single NAT Gateway's source ports are shared across every resource routed through it, a high-concurrency streaming workload can exhaust ports and produce the intermittent `/listen` WebSocket handshake timeouts described above.

#### Diagnosing NAT port exhaustion on AWS

Two AWS-native data sources let you self-diagnose this quickly: use CloudWatch NAT Gateway metrics to confirm exhaustion, and VPC Flow Logs to trace the failing connections.

##### CloudWatch NAT Gateway metrics

Pull the following metrics from the `AWS/NATGateway` namespace, filtered to the affected `NatGatewayId` dimension, at 1-minute granularity around the failure timestamps:

* **`ErrorPortAllocation`** — the number of times the NAT Gateway could not allocate a source port. Any non-zero value is a direct signal of port exhaustion at that moment.
* **`PacketsDropCount`** — the total packets the NAT Gateway dropped. This is a broader drop count that corroborates `ErrorPortAllocation`.
* **`ActiveConnectionCount`** — the number of concurrent active connections. Each NAT Gateway supports up to 55,000 concurrent connections per unique destination — that is, per unique combination of protocol, destination IP, and destination port — and this quota is shared across every resource routed through that gateway. Many tasks connecting to the same Deepgram endpoint on port 443 draw from the same 55,000-connection budget.
* **`ConnectionAttemptCount`** vs **`ConnectionEstablishedCount`** — compare these two. A gap, where attempts exceed established connections, indicates attempts that never completed the handshake, which is consistent with port allocation failure.

##### VPC Flow Logs

VPC Flow Logs record the actual packet flows and let you confirm that failing connections never complete a handshake:

* **Enable flow logs on the NAT Gateway resource directly**, not only on the subnet or VPC. A flow log attached to the NAT Gateway captures both the pre-translation and post-translation addresses, so you can correlate a task's private source address with the public source port the gateway assigned.
* **Use the custom flow log format with all fields** — including `tcp-flags`, `flow-direction`, `pkt-srcaddr`, `pkt-dstaddr`, and `log-status` — and set the maximum aggregation interval to 1 minute instead of the 10-minute default. The finer interval and richer fields make short exhaustion spikes visible.
* **Filter on the affected source IPs and destination port 443** around known failure timestamps. Look for SYN packets with no corresponding response, which is consistent with port allocation failure.
* **Treat a missing flow log entry at a failure timestamp as corroborating, not contradictory.** A port allocation failure can drop the connection before it is ever logged, so the absence of a record at the exact moment of a reported failure is itself expected and consistent with exhaustion.

***

## Why This Typically Lives in the Customer Network, Not Deepgram

It's natural to suspect a remote service when you see connection timeouts. However, in NAT-related cases we consistently observe that:

* Failing connections never appear in Deepgram's edge or application logs:
  * There is no HTTP request, no WebSocket upgrade, and no request ID for the failing attempts.
  * This means the connection failed before it reached our infrastructure.
* When we compare:
  * Tests that bypass the NAT/firewall layer (for example, direct from a VM/static IP), and
  * Tests that go through the existing NAT/firewall,
  * We typically see that:
    * Direct tests are reliable, and
    * NAT-routed tests show timeouts and SYN retransmits under the same external conditions.
* NAT logs and packet captures taken on the customer side show:
  * Port allocation failures or heavy reuse
  * SYN retransmits and delayed SYN-ACKs
  * Behavior that matches the provider's own documented NAT exhaustion patterns

These signals together indicate that the failure domain is the egress path between your workloads and the public internet (NAT/SNAT, firewall, or similar), rather than Deepgram's edge.

That said, we take these reports seriously. We can:

* Verify that our own edge, firewalls, and upstream ISPs are healthy
* Adjust our side (for example, TCP session handling and firewall tuning) when we see opportunities to make the system more robust to external behavior

But the core controls that eliminate NAT port exhaustion (ports, IP pool size, NAT timers, retry patterns) are within your control and located in your environment.

***

## Recommended Mitigations

### General best practices (all providers)

We recommend the following for any environment using NAT to reach Deepgram:

1. **Avoid unnecessary WebSocket churn**
   * Prefer one WebSocket per call/session, rather than per utterance or sub-task.
   * Implement graceful close logic; avoid tight reconnect loops on transient failures.
   * Use exponential backoff for reconnects instead of immediate rapid retries.
2. **Increase NAT capacity and spread**
   * Add more public IPs behind the NAT gateway if concurrency is high.
   * Increase minimum ports per VM/instance (or equivalent setting) so each host has enough ephemeral ports.
   * Ensure traffic is not funneled through a single outbound IP when overall load grows.
3. **Tune NAT TCP timeouts** (within provider guidelines)
   * Shorter idle / TIME\_WAIT values (relative to your traffic pattern) help free ports more quickly.
   * The goal is to avoid long-lived reservations of ports that are no longer in active use, without being so aggressive that you prematurely kill legitimate long-lived connections.
4. **Avoid narrow source port ranges**
   * Do not pin traffic to a very narrow local port range except in controlled experiments.
   * Allow the OS to select from the full ephemeral port range to minimize the chance of conflicting reuse.
5. **Log enough information for diagnosis**
   * On your side, log at least:
     * `source_ip`, `source_port`, `destination_ip`, `destination_port`
     * Connection timestamp
     * Error code or message on failure
   * These fields make it much easier for your cloud provider and Deepgram to collaborate on root cause.

### GCP-specific recommendations

* Use a dedicated Cloud NAT gateway for speech workloads rather than shared/default NAT where feasible.
* Follow GCP's Cloud NAT best practices and troubleshooting guides, especially around:
  * Sizing the IP pool
  * Setting an appropriate minimum ports per instance
  * Enabling NAT logging and log-based metrics
* For Cloud Run:
  * Prefer Cloud Run → VPC egress → dedicated Cloud NAT for production traffic.

### Azure-specific recommendations

* Prefer Azure NAT Gateway as the primary outbound egress mechanism for latency-sensitive workloads.
* Ensure:
  * Adequate NAT IPs for your peak concurrency and connection patterns
  * Reasonable SNAT idle / timeout settings, in line with Azure guidance
  * Balanced port and IP usage across the configured NAT IPs
* Confirm that your application:
  * Explicitly closes WebSocket/TCP connections when calls end or retries occur
  * Uses backoff strategies instead of immediate infinite retry loops

***

## How Deepgram Can Help

While NAT configuration is under your control, we're happy to collaborate. In practice, the most effective joint workflow looks like:

1. **Share context and logs**
   * Provide:
     * A small bundle of failing connection timestamps (with time zones)
     * Any error messages or stack traces
     * Your NAT/log excerpts and pcaps
2. **Deepgram verification**
   * We check:
     * Whether we see any corresponding requests at our edge
     * Whether there were capacity issues, maintenance, or known ISP events in that window
3. **Targeted tests**
   * Optionally, coordinate:
     * Short, controlled tests from your environment
     * Comparative tests from a VM or region without the problematic NAT path
4. **Iterate on NAT tuning**
   * Based on observations, we can:
     * Suggest concrete changes (more IPs, ports per VM, timeout tuning)
     * Re-run tests to confirm that NAT reuse patterns disappear and handshake reliability improves

Our goal is to help you reach a configuration where:

* Your traffic reaches us reliably and predictably, even under load
* Both sides have enough observability to catch issues early and correct them quickly
