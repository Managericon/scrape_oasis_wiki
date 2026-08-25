---
id: "api:cppstruct:FAnimNode_CopyPoseFromMesh"
title: "FAnimNode_CopyPoseFromMesh"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CopyPoseFromMesh.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_CopyPoseFromMesh

Simple controller to copy a bone's transform to another one.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceMeshComponent` | `TWeakObjectPtr < USkeletalMeshComponent >` | This is used by default if it's valid |
| `bUseAttachedParent` | `bool` | If SourceMeshComponent is not valid, and if this is true, it will look for attahced parent as a source |
