---
id: "api:class:ACameraRig_Rail"
title: "ACameraRig_Rail"
source: "https://developer.gp.qq.com/api/class/detail/Others/ACameraRig_Rail.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ACameraRig_Rail

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CurrentPositionOnRail` | `float` | Defines current position of the mount point along the rail, in terms of normalized distance from the beginning of the rail. |
| `TransformComponent` | `USceneComponent *` | Root component to give the whole actor a transform. |
| `RailSplineComponent` | `USplineComponent *` | Spline component to define the rail path. |
| `RailCameraMount` | `USceneComponent *` | Component to define the attach point for cameras. Moves along the rail. |
| `PreviewMesh_Rail` | `USplineMeshComponent *` | Preview meshes for visualization |
| `PreviewRailMeshSegments` | `TArray < USplineMeshComponent * >` | - |
| `PreviewRailStaticMesh` | `UStaticMesh *` | - |
| `PreviewMesh_Mount` | `UStaticMeshComponent *` | - |

## Language

`cpp`
