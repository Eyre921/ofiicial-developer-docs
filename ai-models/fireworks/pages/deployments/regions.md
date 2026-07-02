---
title: "Regions"
source: https://docs.fireworks.ai/deployments/regions
path: deployments/regions
---

Fireworks runs a global fleet of hardware on which you can deploy your models.

Fireworks runs a global fleet so you can deploy models close to users, meet data-residency needs, and scale across clouds. This page covers **multi-region** (default behavior and quota groupings), **single-region** availability and hardware, how to **use and change** regions, and **quotas**.

## Multi-region (recommended)

By default, deployments are multi-region: Fireworks can move and spread them across regions as needed. Multi-regions (**GLOBAL**, **US**, **EUROPE**, **APAC**) are high-level groupings of single regions. Your deployment may run in any single region(s) within that multi-region.

<CardGroup>
  <Card title="Flexible, elastic scaling" icon="gauge">
    Utilizing multiple clouds and locations maximizes the odds that there's capacity to scale.
  </Card>

  <Card title="Higher reliability" icon="shield-check">
    Multi-region deployments enable resilience to localized outages, maintaining application availability as workloads scale across regions.
  </Card>
</CardGroup>

### Supported multi-regions

Supported multi-regions: `GLOBAL`, `US`, `EUROPE`, `APAC`.

## Single region availability

Single regions are concrete locations (e.g. `US_IOWA_1`, `EU_FRANKFURT_1`) where your deployment can run. We have the single regions listed below available; we recommend multi-region for most users because of its advantages (elastic scaling, higher reliability). If you have a specific need for a single region, contact [Fireworks](mailto:inquiries@fireworks.ai) to request it. The table below shows which single regions are available and what hardware is offered in each.

| **Region**        | **Accelerator Type(s)**                  |   |
| ----------------- | ---------------------------------------- | - |
| `US_ARIZONA_1`    | `NVIDIA_H100_80GB`                       |   |
| `US_CALIFORNIA_1` | `NVIDIA_H200_141GB`                      |   |
| `US_GEORGIA_2`    | `NVIDIA_B200_180GB`                      |   |
| `US_GEORGIA_3`    | `NVIDIA_H200_141GB`                      |   |
| `US_ILLINOIS_1`   | `NVIDIA_H100_80GB`                       |   |
| `US_ILLINOIS_2`   | `NVIDIA_A100_80GB`                       |   |
| `US_IOWA_1`       | `NVIDIA_H100_80GB`                       |   |
| `US_OHIO_1`       | `NVIDIA_B200_180GB`                      |   |
| `US_TEXAS_2`      | `NVIDIA_H100_80GB`                       |   |
| `US_UTAH_1`       | `NVIDIA_B200_180GB`                      |   |
| `US_VIRGINIA_1`   | `NVIDIA_H100_80GB`, `NVIDIA_H200_141GB`  |   |
| `US_WASHINGTON_2` | `NVIDIA_H100_80GB`                       |   |
| `US_WASHINGTON_3` | `NVIDIA_B200_180GB`                      |   |
| `US_WASHINGTON_4` | `NVIDIA_B200_180GB`                      |   |
| `EU_FRANKFURT_1`  | `NVIDIA_H100_80GB`                       |   |
| `EU_ICELAND_1`    | `NVIDIA_H200_141GB`                      |   |
| `EU_ICELAND_2`    | `NVIDIA_B200_180GB`, `NVIDIA_H200_141GB` |   |
| `AP_TOKYO_1`      | `NVIDIA_H100_80GB`                       |   |
| `AP_TOKYO_2`      | `NVIDIA_H200_141GB`                      |   |

## Using a region

When creating a deployment, you can pass the `--region` flag to pin it to a single region:

```
firectl deployment create accounts/fireworks/models/llama-v3p1-8b-instruct \
    --region GLOBAL
```

## Changing regions

Updating the single region for a deployment in-place is not supported. To move a deployment to a different single region, create a new deployment in the desired region, then delete the old deployment.

## Quotas

Quota is granted at the **multi-region** level for new users. By default, all users receive quota for **GLOBAL** multi-region. For specific single region quota, please contact Fireworks. To view your current quotas, run:

```
firectl quota list
```

To use single regions that are not generally available (see the table above), or to request additional multi-region quota, contact [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai).
