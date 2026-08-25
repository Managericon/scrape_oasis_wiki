---
id: "api:cppstruct:FAnimPhysBodyDefinition_UE5"
title: "FAnimPhysBodyDefinition_UE5"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimPhysBodyDefinition_UE5.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimPhysBodyDefinition_UE5

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoundBone` | `FBoneReference` | - |
| `BoxExtents` | `FVector` | Extents of the box to use for simulation |
| `LocalJointOffset` | `FVector` | Vector relative to the body being simulated to attach the constraint to |
| `ConstraintSetup` | `FAnimPhysConstraintSetup_UE5` | Data describing the constraints we will apply to the body |
| `CollisionType` | `AnimPhysCollisionType` | Resolution method for planar limits |
| `SphereCollisionRadius` | `float` | Radius to use if CollisionType is set to CustomSphere |
