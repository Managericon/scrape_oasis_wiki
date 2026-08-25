---
id: "api:cppstruct:FAnimNode_LayeredBoneBlend"
title: "FAnimNode_LayeredBoneBlend"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_LayeredBoneBlend.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_LayeredBoneBlend

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BasePose` | `FPoseLink` | The source pose |
| `BlendPoses` | `TArray < FPoseLink >` | Each layer's blended pose |
| `LayerSetup` | `TArray < FInputBlendPose >` | Configuration for the parts of the skeleton to blend for each layer. Allows<br>	  certain parts of the tree to be blended out or omitted from the pose. |
| `BlendWeights` | `TArray < float >` | The weights of each layer |
| `bMeshSpaceRotationBlend` | `bool` | Whether to blend bone rotations in mesh space or in local space |
| `CurveBlendOption` | `TEnumAsByte < enum ECurveBlendOption :: Type >` | How to blend the layers together |
| `bBlendRootMotionBasedOnRootBone` | `bool` | Whether to incorporate the per-bone blend weight of the root bone when lending root motion |
| `bHasRelevantPoses` | `bool` | - |
| `PerBoneBlendWeights` | `TArray < FPerBoneBlendWeight >` | - |
| `SkeletonGuid` | `FGuid` | - |
| `VirtualBoneGuid` | `FGuid` | - |
| `DesiredBoneBlendWeightsInitMesh` | `TWeakObjectPtr < USkeletalMesh >` | - |
