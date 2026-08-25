---
id: "api:class:AStaticMeshActor"
title: "AStaticMeshActor"
source: "https://developer.gp.qq.com/api/class/detail/Others/AStaticMeshActor.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AStaticMeshActor

StaticMeshActor is an instance of a UStaticMesh in the world.
  Static meshes are geometry that do not animate or otherwise deform, and are more efficient to render than other types of geometry.
  Static meshes dragged into the level from the Content Browser are automatically converted to StaticMeshActors.
 
  @see UStaticMesh

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StaticMeshComponent` | `UStaticMeshComponent *` | - |
| `bStaticMeshReplicateMovement` | `bool` | This static mesh should replicate movement. Automatically sets the RemoteRole and bReplicateMovement flags. Meant to be edited on placed actors (those other two properties are not) |
| `NavigationGeometryGatheringMode` | `ENavDataGatheringMode` | - |

## Language

`cpp`
