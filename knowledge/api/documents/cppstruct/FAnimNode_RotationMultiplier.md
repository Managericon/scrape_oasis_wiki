---
id: "api:cppstruct:FAnimNode_RotationMultiplier"
title: "FAnimNode_RotationMultiplier"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_RotationMultiplier.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_RotationMultiplier

Simple controller that multiplies scalar value to the translationrotationscale of a single bone.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetBone` | `FBoneReference` | Name of bone to control. This is the main bone chain to modify from. |
| `SourceBone` | `FBoneReference` | Source to get transform from |
| `Multiplier` | `float` | - |
| `RotationAxisToRefer` | `TEnumAsByte < EBoneAxis >` | - |
| `bIsAdditive` | `bool` | - |
