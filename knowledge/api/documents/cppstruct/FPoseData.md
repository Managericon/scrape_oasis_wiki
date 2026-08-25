---
id: "api:cppstruct:FPoseData"
title: "FPoseData"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FPoseData.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FPoseData

Pose data 
  
  This is one pose data structure
  This will let us blend poses quickly easily
  All poses within this asset should contain same number of tracks, 
  so that we can blend quickly

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LocalSpacePose` | `TArray < FTransform >` | - |
| `LocalSpacePoseMask` | `TArray < bool >` | - |
| `CurveData` | `TArray < float >` | - |
