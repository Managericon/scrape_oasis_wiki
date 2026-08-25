---
id: "api:cppstruct:FAnimPhysSphericalLimit"
title: "FAnimPhysSphericalLimit"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimPhysSphericalLimit.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimPhysSphericalLimit

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DrivingBone` | `FBoneReference` | Bone to attach the sphere to |
| `SphereLocalOffset` | `FVector` | Local offset for the sphere, if no driving bone is set this is in node space, otherwise bone space |
| `LimitRadius` | `float` | Radius of the sphere |
| `LimitType` | `ESphericalLimitType` | Whether to lock bodies inside or outside of the sphere |
| `IsEnabled` | `bool` | - |
