---
id: "api:cppstruct:FAnimNode_MoveAdditiveLayering"
title: "FAnimNode_MoveAdditiveLayering"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_MoveAdditiveLayering.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_MoveAdditiveLayering

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BasePose` | `FPoseLink` | - |
| `TargetPose` | `FPoseLink` | - |
| `RefPose` | `FPoseLink` | - |
| `bFixRootRotation` | `bool` | - |
| `ArmMeshSpaceAlphaL` | `float` | - |
| `ArmMeshSpaceAlphaR` | `float` | - |
| `ArmSwayAlphaL` | `float` | - |
| `ArmSwayAlphaR` | `float` | - |
| `HandAlphaL` | `float` | - |
| `HandAlphaR` | `float` | - |
| `UpperPoseOverrideLayerSetup` | `TArray < FInputBlendPose >` | Configuration for the parts of the skeleton to blend for each layer. Allows<br>	  certain parts of the tree to be blended out or omitted from the pose. |
| `SpineLocalSpaceAdditiveLayerSetup` | `TArray < FInputBlendPose >` | - |
| `MeshSpaceAdditiveLayerSetup_Left` | `TArray < FInputBlendPose >` | - |
| `MeshSpaceAdditiveLayerSetup_Right` | `TArray < FInputBlendPose >` | - |
| `ArmLocalSpaceAdditiveLayerSetup` | `TArray < FInputBlendPose >` | - |
| `bEvaluateLayer0` | `bool` | - |
| `bEvaluateLayer1` | `bool` | - |
| `bEvaluateLayer2` | `bool` | - |
| `bEvaluateLayer3` | `bool` | - |
| `SkeletonGuid` | `FGuid` | - |
| `VirtualBoneGuid` | `FGuid` | - |
| `UpperPoseOverrideData` | `FMoveAdditiveLayeringData` | - |
| `SpineLocalSpaceAdditiveData` | `FMoveAdditiveLayeringData` | - |
| `MeshSpaceAdditiveData_Left` | `FMoveAdditiveLayeringData` | - |
| `MeshSpaceAdditiveData_Right` | `FMoveAdditiveLayeringData` | - |
| `ArmLocalSpaceAdditiveData` | `FMoveAdditiveLayeringData` | - |
| `bOutputTargetPose` | `bool` | - |
| `bOutputRefPose` | `bool` | - |
| `bOutputLocalSpaceAdditivePose` | `bool` | - |
| `bOutputMeshSpaceAdditivePose` | `bool` | - |
