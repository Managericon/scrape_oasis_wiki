---
id: "api:class:UDistributionVectorUniformCurve"
title: "UDistributionVectorUniformCurve"
source: "https://developer.gp.qq.com/api/class/detail/Others/UDistributionVectorUniformCurve.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UDistributionVectorUniformCurve

## Inheritance

`UDistributionVector`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConstantCurve` | `FInterpCurveTwoVectors` | Keyframe data for how output constant varies over time. |
| `bLockAxes1` | `uint32` | If true, X == Y == Z ie. only one degree of freedom. If false, each axis is picked independently. |
| `bLockAxes2` | `uint32` | - |
| `LockedAxes` | `TEnumAsByte < enum EDistributionVectorLockFlags >` | - |
| `MirrorFlags` | `TEnumAsByte < enum EDistributionVectorMirrorFlags >` | - |
| `bUseExtremes` | `uint32` | - |

## Language

`cpp`
