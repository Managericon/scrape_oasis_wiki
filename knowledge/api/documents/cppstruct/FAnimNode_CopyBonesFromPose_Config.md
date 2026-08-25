---
id: "api:cppstruct:FAnimNode_CopyBonesFromPose_Config"
title: "FAnimNode_CopyBonesFromPose_Config"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CopyBonesFromPose_Config.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_CopyBonesFromPose_Config

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Bone` | `FBoneReference` | Source Bone Name to get transform from |
| `bCopyTranslation` | `bool` | If Translation should be copied |
| `bCopyRotation` | `bool` | If Rotation should be copied |
| `bCopyRotation_Roll` | `bool` | - |
| `bCopyRotation_Pitch` | `bool` | - |
| `bCopyRotation_Yaw` | `bool` | - |
| `bCopyScale` | `bool` | - |
| `ControlSpace` | `TEnumAsByte < EBoneControlSpace >` | Space to convert transforms into prior to copying components |
