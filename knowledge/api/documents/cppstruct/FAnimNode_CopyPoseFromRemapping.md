---
id: "api:cppstruct:FAnimNode_CopyPoseFromRemapping"
title: "FAnimNode_CopyPoseFromRemapping"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CopyPoseFromRemapping.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_CopyPoseFromRemapping

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceMeshComponent` | `TWeakObjectPtr < USkeletalMeshComponent >` | This is used by default if it's valid |
| `bUseAttachedParent` | `bool` | If SourceMeshComponent is not valid, and if this is true, it will look for attahced parent as a source |
| `bIkGunValid` | `bool` | - |
| `bParentPoseOffset` | `bool` | - |
| `NewFPPPoseOffset` | `FNewFPPPoseOffset` | - |
| `BoneNeedRelevant` | `TMap < FName , FName >` | - |
