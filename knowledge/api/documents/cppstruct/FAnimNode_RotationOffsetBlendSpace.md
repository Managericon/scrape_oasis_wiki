---
id: "api:cppstruct:FAnimNode_RotationOffsetBlendSpace"
title: "FAnimNode_RotationOffsetBlendSpace"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_RotationOffsetBlendSpace.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_RotationOffsetBlendSpace

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BasePose` | `FPoseLink` | - |
| `LODThreshold` | `int32` | Max LOD that this node is allowed to run<br>	 For example if you have LODThreadhold to be 2, it will run until LOD 2 (based on 0 index)<br>	 when the component LOD becomes 3, it will stop updateevaluate<br>	 currently transition would be issue and that has to be re-visited |
| `bIsLODEnabled` | `bool` | - |
| `Alpha` | `float` | - |
| `AlphaScaleBias` | `FInputScaleBias` | - |
| `ActualAlpha` | `float` | - |
