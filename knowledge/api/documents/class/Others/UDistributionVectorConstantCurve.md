---
id: "api:class:UDistributionVectorConstantCurve"
title: "UDistributionVectorConstantCurve"
source: "https://developer.gp.qq.com/api/class/detail/Others/UDistributionVectorConstantCurve.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UDistributionVectorConstantCurve

## Inheritance

`UDistributionVector`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConstantCurve` | `FInterpCurveVector` | Keyframe data for each component (X,Y,Z) over time. |
| `bLockAxes` | `uint32` | If true, X == Y == Z ie. only one degree of freedom. If false, each axis is picked independently. |
| `LockedAxes` | `TEnumAsByte < enum EDistributionVectorLockFlags >` | - |

## Language

`cpp`
