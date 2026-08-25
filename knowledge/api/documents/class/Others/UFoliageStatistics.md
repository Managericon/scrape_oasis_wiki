---
id: "api:class:UFoliageStatistics"
title: "UFoliageStatistics"
source: "https://developer.gp.qq.com/api/class/detail/Others/UFoliageStatistics.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UFoliageStatistics

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `FoliageOverlappingSphereCount`

```text
FoliageOverlappingSphereCount(WorldContextObject: UObject *, StaticMesh: UStaticMesh *, CenterPosition: FVector, Radius: float) -> int32
```

Counts how many foliage instances overlap a given sphere

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `StaticMesh` | `UStaticMesh *` | - |
| `CenterPosition` | `FVector` | The center position of the sphere |
| `Radius` | `float` | The radius of the sphere. |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `FoliageOverlappingBoxCount`

```text
FoliageOverlappingBoxCount(WorldContextObject: UObject *, StaticMesh: UStaticMesh *, Box: FBox) -> int32
```

Gets the number of instances overlapping a provided box

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `StaticMesh` | `UStaticMesh *` | Mesh to count |
| `Box` | `FBox` | Box to overlap |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

## Language

`cpp`
