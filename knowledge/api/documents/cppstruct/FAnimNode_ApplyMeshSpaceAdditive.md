---
id: "api:cppstruct:FAnimNode_ApplyMeshSpaceAdditive"
title: "FAnimNode_ApplyMeshSpaceAdditive"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_ApplyMeshSpaceAdditive.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_ApplyMeshSpaceAdditive

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Base` | `FPoseLink` | - |
| `Additive` | `FPoseLink` | - |
| `Alpha` | `float` | - |
| `AlphaScaleBias` | `FInputScaleBias` | - |
| `LODThreshold` | `int32` | Max LOD that this node is allowed to run<br>	 For example if you have LODThreadhold to be 2, it will run until LOD 2 (based on 0 index)<br>	 when the component LOD becomes 3, it will stop updateevaluate<br>	 currently transition would be issue and that has to be re-visited |
| `ActualAlpha` | `float` | - |
