---
id: "api:class:APhysicsVolume"
title: "APhysicsVolume"
source: "https://developer.gp.qq.com/api/class/detail/Others/APhysicsVolume.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# APhysicsVolume

PhysicsVolume: A bounding volume which affects actor physics.
  Each AActor is affected at any time by one PhysicsVolume.

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TerminalVelocity` | `float` | Terminal velocity of pawns using CharacterMovement when falling. |
| `Priority` | `int32` | Determines which PhysicsVolume takes precedence if they overlap (higher number = higher priority). |
| `FluidFriction` | `float` | This property controls the amount of friction applied by the volume as pawns using CharacterMovement move through it. The higher this value, the harder it will feel to move through |
| `bWaterVolume` | `uint32` | True if this volume contains a fluid like water |
| `bPhysicsOnContact` | `uint32` | By default, the origin of an AActor must be inside a PhysicsVolume for it to affect the actor. However if this flag is true, the other actor only has to touch the volume to be affected by it. |

## Language

`cpp`
