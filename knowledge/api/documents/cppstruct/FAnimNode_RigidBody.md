---
id: "api:cppstruct:FAnimNode_RigidBody"
title: "FAnimNode_RigidBody"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_RigidBody.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_RigidBody

Controller that simulates physics based on the physics asset of the skeletal mesh component

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OverridePhysicsAsset` | `UPhysicsAsset *` | Physics asset to use. If empty use the skeletal mesh's default physics asset |
| `LastUsePhysicsAsset` | `TWeakObjectPtr < UPhysicsAsset >` | - |
| `OverrideWorldGravity` | `FVector` | Override gravity |
| `ExternalForce` | `FVector` | Applies a uniform external force in world space. This allows for easily faking inertia of movement while still simulating in component space for example |
| `OverlapChannel` | `TEnumAsByte < ECollisionChannel >` | The channel we use to find static geometry to collide with |
| `bEnableWorldGeometry` | `bool` | - |
| `SimulationSpace` | `ESimulationSpace` | What space to simulate the bodies in. This affects how velocities are generated |
| `bOverrideWorldGravity` | `bool` | - |
| `CachedBoundsScale` | `float` | Scale of cached bounds (vs. actual bounds).<br>	  Increasing this may improve performance, but overlaps may not work as well.<br>	  (A value of 1.0 effectively disables cached bounds). |
| `bUseCompPhysicsAssetWhenNotSet` | `bool` | - |
| `bUseIntersectDetect` | `bool` | - |
| `bUseMultipleRigidBodyNodeInitDelay` | `bool` | - |
| `bComponentSpaceSimulation_DEPRECATED` | `bool` | - |
| `BoneShiftTolerenceChecker` | `FAnimNodeBoneShiftTolerenceChecker` | Bone Shift Tolerence Check Start |
