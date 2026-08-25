---
id: "api:cppstruct:FAnimNode_BoneFollowChain"
title: "FAnimNode_BoneFollowChain"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_BoneFollowChain.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_BoneFollowChain

make bone list move like snake

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BasePose` | `FPoseLink` | - |
| `ToParentDisTolerence` | `int32` | - |
| `ToParentMaxDisTolerence` | `int32` | - |
| `bLeaderBoneMoveFromAnim` | `bool` | - |
| `bClearParentBonePathWhenNoMove` | `bool` | - |
| `bEnableTerrainAdaptFeature` | `bool` | - |
| `TerrainTraceStart` | `float` | - |
| `TerrainTraceEnd` | `float` | - |
| `ToParentRotationScale` | `float` | - |
| `bLerpBoneRotaion` | `bool` | - |
| `bLerpBoneRotaionCalcCurFrameBoneTransform` | `bool` | - |
| `MaxBonePathRecordBufferSize` | `int32` | - |
| `LeaderBone` | `FBoneReference` | - |
| `FollowBoneList` | `TArray < FBoneReference >` | - |
