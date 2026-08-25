---
id: "api:cppstruct:FAnimNode_CopyBoneDelta"
title: "FAnimNode_CopyBoneDelta"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CopyBoneDelta.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_CopyBoneDelta

Simple controller to copy a transform relative to the ref pose to the target bone,
 	instead of the copy bone node which copies the absolute transform

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceBone` | `FBoneReference` | - |
| `TargetBone` | `FBoneReference` | - |
| `bCopyTranslation` | `bool` | - |
| `bCopyRotation` | `bool` | - |
| `bCopyScale` | `bool` | - |
| `CopyMode` | `CopyBoneDeltaMode` | - |
| `TranslationMultiplier` | `float` | - |
| `RotationMultiplier` | `float` | - |
| `ScaleMultiplier` | `float` | - |
