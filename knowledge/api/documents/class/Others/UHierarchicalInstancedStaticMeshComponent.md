---
id: "api:class:UHierarchicalInstancedStaticMeshComponent"
title: "UHierarchicalInstancedStaticMeshComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UHierarchicalInstancedStaticMeshComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UHierarchicalInstancedStaticMeshComponent

## Inheritance

`UInstancedStaticMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SortedInstances` | `TArray < int32 >` | - |
| `NumBuiltInstances` | `int32` | - |
| `BuiltInstanceBounds` | `FBox` | - |
| `UnbuiltInstanceBounds` | `FBox` | - |
| `UnbuiltInstanceBoundsList` | `TArray < FBox >` | - |
| `UnbuiltInstanceIndexList` | `TArray < int32 >` | - |
| `bEnableDensityScaling` | `uint32` | - |
| `OcclusionLayerNumNodes` | `int32` | - |
| `CacheMeshExtendedBounds` | `FBoxSphereBounds` | - |
| `bDisableCollision` | `bool` | - |
| `MinInstancesToSplitNode` | `int32` | Culling by Num |
| `OptimiMinInstancesToSplitNode` | `int32` | Culling by Num For Optimization FClusterTree |
| `IsOpenTreeOptimi` | `bool` | Mark Use OptimiMinInstancesToSplitNode With FClusterTree |
| `InstanceCullDistanceByVolume` | `float` | Instance Culling by CullDistanceVolume |
| `bEnableScaleOpt` | `bool` | - |
| `AverageScale` | `FVector` | - |

## Functions

### `RemoveInstances`

```text
RemoveInstances(InstancesToRemove: TArray < int32 > &) -> bool
```

Removes all the instances with indices specified in the InstancesToRemove array. Returns true on success.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstancesToRemove` | `TArray < int32 > &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`
