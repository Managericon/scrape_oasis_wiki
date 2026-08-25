---
id: "api:class:UNavLocalGridManager"
title: "UNavLocalGridManager"
source: "https://developer.gp.qq.com/api/class/detail/Others/UNavLocalGridManager.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UNavLocalGridManager

Manager for local navigation grids
  
   Builds non overlapping grid from multiple sources, that can be used later for pathfinding.
   Check also: UGridPathFollowingComponent, FNavLocalGridData

## Inheritance

`UObject`

## Functions

### `SetLocalNavigationGridDensity`

```text
SetLocalNavigationGridDensity(WorldContextObject: UObject *, CellSize: float) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `CellSize` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `AddLocalNavigationGridForPoint`

```text
AddLocalNavigationGridForPoint(WorldContextObject: UObject *, Location: FVector &, Radius2D: int32, Height: float, bRebuildGrids: bool) -> int32
```

creates new grid data for single point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Location` | `FVector &` | - |
| `Radius2D` | `int32` | - |
| `Height` | `float` | - |
| `bRebuildGrids` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `AddLocalNavigationGridForPoints`

```text
AddLocalNavigationGridForPoints(WorldContextObject: UObject *, Locations: TArray < FVector > &, Radius2D: int32, Height: float, bRebuildGrids: bool) -> int32
```

creates single grid data for set of points

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Locations` | `TArray < FVector > &` | - |
| `Radius2D` | `int32` | - |
| `Height` | `float` | - |
| `bRebuildGrids` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `AddLocalNavigationGridForBox`

```text
AddLocalNavigationGridForBox(WorldContextObject: UObject *, Location: FVector &, Extent: FVector, Rotation: FRotator, Radius2D: int32, Height: float, bRebuildGrids: bool) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Location` | `FVector &` | - |
| `Extent` | `FVector` | - |
| `Rotation` | `FRotator` | - |
| `Radius2D` | `int32` | - |
| `Height` | `float` | - |
| `bRebuildGrids` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `AddLocalNavigationGridForCapsule`

```text
AddLocalNavigationGridForCapsule(WorldContextObject: UObject *, Location: FVector &, CapsuleRadius: float, CapsuleHalfHeight: float, Radius2D: int32, Height: float, bRebuildGrids: bool) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Location` | `FVector &` | - |
| `CapsuleRadius` | `float` | - |
| `CapsuleHalfHeight` | `float` | - |
| `Radius2D` | `int32` | - |
| `Height` | `float` | - |
| `bRebuildGrids` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `RemoveLocalNavigationGrid`

```text
RemoveLocalNavigationGrid(WorldContextObject: UObject *, GridId: int32, bRebuildGrids: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `GridId` | `int32` | - |
| `bRebuildGrids` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FindLocalNavigationGridPath`

```text
FindLocalNavigationGridPath(WorldContextObject: UObject *, Start: FVector &, End: FVector &, PathPoints: TArray < FVector > &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector &` | - |
| `End` | `FVector &` | - |
| `PathPoints` | `TArray < FVector > &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`
