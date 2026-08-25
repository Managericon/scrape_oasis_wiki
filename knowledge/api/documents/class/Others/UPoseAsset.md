---
id: "api:class:UPoseAsset"
title: "UPoseAsset"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPoseAsset.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPoseAsset

Pose Asset that can be blended by weight of curves

## Inheritance

`UAnimationAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PoseContainer` | `FPoseDataContainer` | Animation Pose Data |
| `bAdditivePose` | `bool` | Whether or not Additive Pose or not - these are property that needs post process, so |
| `BasePoseIndex` | `int32` | if -1, use ref pose |
| `RetargetSource` | `FName` | Base pose to use when retargeting |
| `SourceAnimation` | `UAnimSequence *` | - |
| `bOverridePoseNameFrom_0` | `bool` | - |

## Language

`cpp`
