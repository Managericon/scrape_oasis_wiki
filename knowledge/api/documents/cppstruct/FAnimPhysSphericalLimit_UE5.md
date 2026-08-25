---
id: "api:cppstruct:FAnimPhysSphericalLimit_UE5"
title: "FAnimPhysSphericalLimit_UE5"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimPhysSphericalLimit_UE5.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimPhysSphericalLimit_UE5

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DrivingBone` | `FBoneReference` | Bone to attach the sphere to |
| `SphereLocalOffset` | `FVector` | Local offset for the sphere, if no driving bone is set this is in node space, otherwise bone space |
| `LimitRadius` | `float` | Radius of the sphere |
| `LimitType` | `ESphericalLimitType_UE5` | Whether to lock bodies inside or outside of the sphere |
