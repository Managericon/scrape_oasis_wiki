---
id: "api:cppstruct:FAnimMontageInstance"
title: "FAnimMontageInstance"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimMontageInstance.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimMontageInstance

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |
| `MontageNoGCID` | `int64` | - |
| `bPlaying` | `bool` | - |
| `bIsStopping` | `bool` | - |
| `DefaultBlendTimeMultiplier` | `float` | - |
| `IgnoreNotifyType` | `TArray < FString >` | - |
| `CustomSectionsPlayInfo` | `TArray < FMontageSectionsPlayInfo >` | - |
| `NextSections` | `TArray < int32 >` | - |
| `PrevSections` | `TArray < int32 >` | - |
| `ActiveStateBranchingPoints` | `TArray < FAnimNotifyEvent >` | Currently Active AnimNotifyState, stored as a copy of the event as we need to<br>		is removed correctly. |
| `Position` | `float` | - |
| `PlayRate` | `float` | - |
| `Blend` | `FAlphaBlend` | - |
| `DisableRootMotionCount` | `int32` | - |
| `RandomJumpTimes` | `int32` | - |
