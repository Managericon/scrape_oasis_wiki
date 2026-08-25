---
id: "api:cppstruct:FClothConfig"
title: "FClothConfig"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FClothConfig.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FClothConfig

Holds initial, asset level config for clothing actors.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WindMethod` | `EClothingWindMethod` | - |
| `VerticalConstraintConfig` | `FClothConstraintSetup` | - |
| `HorizontalConstraintConfig` | `FClothConstraintSetup` | - |
| `BendConstraintConfig` | `FClothConstraintSetup` | - |
| `ShearConstraintConfig` | `FClothConstraintSetup` | - |
| `SelfCollisionRadius` | `float` | - |
| `SelfCollisionStiffness` | `float` | - |
| `SelfCollisionCullScale` | `float` | Scale to use for the radius of the culling checks for self collisions.<br>	  Any other self collision body within the radius of this check will be culled.<br>	  This helps performance with higher resolution meshes by reducing the number<br>	  of colliding bodies within the cloth. Reducing this will have a negative<br>	  effect on performance! |
| `Damping` | `FVector` | - |
| `Friction` | `float` | - |
| `WindDragCoefficient` | `float` | - |
| `WindLiftCoefficient` | `float` | - |
| `LinearDrag` | `FVector` | - |
| `AngularDrag` | `FVector` | - |
| `LinearInertiaScale` | `FVector` | - |
| `AngularInertiaScale` | `FVector` | - |
| `CentrifugalInertiaScale` | `FVector` | - |
| `SolverFrequency` | `float` | - |
| `StiffnessFrequency` | `float` | - |
| `GravityScale` | `float` | - |
| `TetherStiffness` | `float` | - |
| `TetherLimit` | `float` | - |
| `CollisionThickness` | `float` | - |
