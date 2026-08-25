---
id: "api:cppstruct:FBoneNode"
title: "FBoneNode"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FBoneNode.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FBoneNode

Each Bone node in BoneTree

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name_DEPRECATED` | `FName` | Name of bone, this is the search criteria to match with mesh bone. This will be NAME_None if deleted. |
| `ParentIndex_DEPRECATED` | `int32` | Parent Index. -1 if not used. The root has 0 as its parent. Do not delete the element but set this to -1. If it is revived by other reason, fix up this link. |
| `TranslationRetargetingMode` | `TEnumAsByte < EBoneTranslationRetargetingMode :: Type >` | Retargeting Mode for Translation Component. |
| `PerBoneOverrideRetargetingModeConfig` | `TMap < FName , TEnumAsByte < EBoneTranslationRetargetingMode :: Type > >` | - |
