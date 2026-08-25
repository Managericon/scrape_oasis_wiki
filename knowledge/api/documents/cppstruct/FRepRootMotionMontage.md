---
id: "api:cppstruct:FRepRootMotionMontage"
title: "FRepRootMotionMontage"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FRepRootMotionMontage.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FRepRootMotionMontage

Replicated data when playing a root motion montage.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bIsActive` | `bool` | Whether this has usefulactive data. |
| `AnimMontage` | `UAnimMontage *` | AnimMontage providing Root Motion |
| `Position` | `float` | Track position of Montage |
| `Location` | `FVector_NetQuantize100` | Location |
| `Rotation` | `FRotator` | Rotation |
| `MovementBase` | `UPrimitiveComponent *` | Movement Relative to Base |
| `MovementBaseBoneName` | `FName` | Bone on the MovementBase, if a skeletal mesh. |
| `bRelativePosition` | `bool` | Additional replicated flag, if MovementBase can't be resolved on the client. So we don't use wrong data. |
| `bRelativeRotation` | `bool` | Whether rotation is relative or absolute. |
| `AuthoritativeRootMotion` | `FRootMotionSourceGroup` | State of Root Motion Sources on Authority |
| `Acceleration` | `FVector_NetQuantize10` | Acceleration |
| `LinearVelocity` | `FVector_NetQuantize10` | Velocity |
