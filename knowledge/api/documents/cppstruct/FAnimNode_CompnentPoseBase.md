---
id: "api:cppstruct:FAnimNode_CompnentPoseBase"
title: "FAnimNode_CompnentPoseBase"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_CompnentPoseBase.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_CompnentPoseBase

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bActiveNode` | `bool` | Engine Modify<br>	 Enable Node to be ignored at runtime but keep alpha value no change<br>	 false will ignore (do no or skip) evaluate, but no affect on update |
| `Alpha` | `float` | - |
| `AlphaScaleBias` | `FInputScaleBias` | - |
| `LODThreshold` | `int32` | Max LOD that this node is allowed to run<br>	 For example if you have LODThreadhold to be 2, it will run until LOD 2 (based on 0 index)<br>	 when the component LOD becomes 3, it will stop updateevaluate<br>	 currently transition would be issue and that has to be re-visited |
| `ActualAlpha` | `float` | - |
