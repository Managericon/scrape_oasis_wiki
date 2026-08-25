---
id: "api:class:UDistributionVectorUniform"
title: "UDistributionVectorUniform"
source: "https://developer.gp.qq.com/api/class/detail/Others/UDistributionVectorUniform.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UDistributionVectorUniform

## Inheritance

`UDistributionVector`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Max` | `FVector` | Upper end of FVector magnitude range. |
| `Min` | `FVector` | Lower end of FVector magnitude range. |
| `bLockAxes` | `uint32` | If true, X == Y == Z ie. only one degree of freedom. If false, each axis is picked independently. |
| `LockedAxes` | `TEnumAsByte < enum EDistributionVectorLockFlags >` | - |
| `MirrorFlags` | `TEnumAsByte < enum EDistributionVectorMirrorFlags >` | - |
| `bUseExtremes` | `uint32` | - |

## Language

`cpp`
