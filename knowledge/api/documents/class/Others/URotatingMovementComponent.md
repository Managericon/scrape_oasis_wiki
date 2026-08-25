---
id: "api:class:URotatingMovementComponent"
title: "URotatingMovementComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/URotatingMovementComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# URotatingMovementComponent

Performs continuous rotation of a component at a specific rotation rate.
  Rotation can optionally be offset around a pivot point.
  Collision testing is not performed during movement.

## Inheritance

`UMovementComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RotationRate` | `FRotator` | How fast to update rollpitchyaw of the component we update. |
| `PivotTranslation` | `FVector` | Translation of pivot point around which we rotate, relative to current rotation.<br>	  For instance, with PivotTranslation set to (X=+100, Y=0, Z=0), rotation will occur<br>	  around the point +100 units along the local X axis from the center of the object,<br>	  rather than around the object's origin (the default). |
| `bRotationInLocalSpace` | `uint32` | Whether rotation is applied in local or world space. |
| `bCirculatingRotation` | `bool` | - |
| `RotationAngle` | `FRotator` | - |
| `OriginRotator` | `FRotator` | - |
| `bCircleFlag` | `bool` | - |

## Language

`cpp`
