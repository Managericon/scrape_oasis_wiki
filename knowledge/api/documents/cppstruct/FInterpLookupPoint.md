---
id: "api:cppstruct:FInterpLookupPoint"
title: "FInterpLookupPoint"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FInterpLookupPoint.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FInterpLookupPoint

Array of group names to retrieve position and rotation data from instead of using the data stored in the keyframe.
  A value of NAME_None means to use the PosTrack and EulerTrack data for the keyframe.
  There needs to be the same amount of elements in this array as there are keyframes.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GroupName` | `FName` | - |
| `Time` | `float` | - |
