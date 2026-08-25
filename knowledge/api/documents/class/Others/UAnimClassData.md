---
id: "api:class:UAnimClassData"
title: "UAnimClassData"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAnimClassData.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAnimClassData

## Inheritance

`UObject` -> `IAnimClassInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BakedStateMachines` | `TArray < FBakedAnimationStateMachine >` | - |
| `TargetSkeleton` | `USkeleton *` | Target skeleton for this blueprint class |
| `AnimNotifies` | `TArray < FAnimNotifyEvent >` | A list of anim notifies that state machines (or anything else) may reference |
| `RootAnimNodeIndex` | `int32` | - |
| `OrderedSavedPoseIndices` | `TArray < int32 >` | - |
| `RootAnimNodeProperty` | `UStructProperty *` | - |
| `AnimNodeProperties` | `TArray < UStructProperty * >` | - |
| `SyncGroupNames` | `TArray < FName >` | - |

## Language

`cpp`
