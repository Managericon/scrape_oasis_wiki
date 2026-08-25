---
id: "api:class:UNavCollision"
title: "UNavCollision"
source: "https://developer.gp.qq.com/api/class/detail/Others/UNavCollision.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UNavCollision

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CylinderCollision` | `TArray < FNavCollisionCylinder >` | list of nav collision cylinders |
| `BoxCollision` | `TArray < FNavCollisionBox >` | list of nav collision boxes |
| `AreaClass` | `TSubclassOf < UNavArea >` | navigation area type (empty = default obstacle) |
| `bIsDynamicObstacle` | `uint32` | If set, mesh will be used as dynamic obstacle (don't create navmesh on top, much faster addingremoving) |
| `bGatherConvexGeometry` | `uint32` | If set, convex collisions will be exported offline for faster runtime navmesh building (increases memory usage) |

## Language

`cpp`
