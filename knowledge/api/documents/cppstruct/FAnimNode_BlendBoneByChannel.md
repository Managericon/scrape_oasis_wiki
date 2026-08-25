---
id: "api:cppstruct:FAnimNode_BlendBoneByChannel"
title: "FAnimNode_BlendBoneByChannel"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BlendBoneByChannel.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_BlendBoneByChannel

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FPoseLink` | - |
| `B` | `FPoseLink` | - |
| `Alpha` | `float` | - |
| `AlphaScaleBias` | `FInputScaleBias` | - |
| `BoneDefinitions` | `TArray < FBlendBoneByChannelEntry >` | - |
| `TransformsSpace` | `TEnumAsByte < EBoneControlSpace >` | Space to convert transforms into prior to copying channels |
| `InternalBlendAlpha` | `float` | - |
| `bBIsRelevant` | `bool` | - |
| `ValidBoneEntries` | `TArray < FBlendBoneByChannelEntry >` | - |
