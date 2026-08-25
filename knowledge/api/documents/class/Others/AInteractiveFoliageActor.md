---
id: "api:class:AInteractiveFoliageActor"
title: "AInteractiveFoliageActor"
source: "https://developer.gp.qq.com/api/class/detail/Others/AInteractiveFoliageActor.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AInteractiveFoliageActor

## Inheritance

`AStaticMeshActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CapsuleComponent` | `UCapsuleComponent *` | Collision cylinder |
| `TouchingActorEntryPosition` | `FVector` | Position of the last actor to enter the collision cylinder.<br>	  This currently does not handle multiple actors affecting the foliage simultaneously. |
| `FoliageVelocity` | `FVector` | Simulated physics state |
| `FoliageForce` | `FVector` | @todo document |
| `FoliagePosition` | `FVector` | @todo document |
| `FoliageDamageImpulseScale` | `float` | Scales forces applied from damage events. |
| `FoliageTouchImpulseScale` | `float` | Scales forces applied from touch events. |
| `FoliageStiffness` | `float` | Determines how strong the force that pushes toward the spring's center will be. |
| `FoliageStiffnessQuadratic` | `float` | Same as FoliageStiffness, but the strength of this force increases with the square of the distance to the spring's center.<br>	  This force is used to prevent the spring from extending past a certain point due to touch and damage forces. |
| `FoliageDamping` | `float` | Determines the amount of energy lost by the spring as it oscillates.<br>	  This force is similar to air friction. |
| `MaxDamageImpulse` | `float` | Clamps the magnitude of each damage force applied. |
| `MaxTouchImpulse` | `float` | Clamps the magnitude of each touch force applied. |
| `MaxForce` | `float` | Clamps the magnitude of combined forces applied each update. |
| `Mass` | `float` | - |

## Functions

### `CapsuleTouched`

```text
CapsuleTouched(OverlappedComp: UPrimitiveComponent *, Other: AActor *, OtherComp: UPrimitiveComponent *, OtherBodyIndex: int32, bFromSweep: bool, OverlapInfo: FHitResult &) -> void
```

Called when capsule is touched

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OverlappedComp` | `UPrimitiveComponent *` | - |
| `Other` | `AActor *` | - |
| `OtherComp` | `UPrimitiveComponent *` | - |
| `OtherBodyIndex` | `int32` | - |
| `bFromSweep` | `bool` | - |
| `OverlapInfo` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
