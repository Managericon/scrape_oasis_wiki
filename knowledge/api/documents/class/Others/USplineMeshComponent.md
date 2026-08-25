---
id: "api:class:USplineMeshComponent"
title: "USplineMeshComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/USplineMeshComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# USplineMeshComponent

A Spline Mesh Component is a derivation of a Static Mesh Component which can be deformed using a spline. Only a start and end position (and tangent) can be specified.

## Inheritance

`UStaticMeshComponent` -> `IInterface_CollisionDataProvider`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SplineParams` | `FSplineMeshParams` | Spline that is used to deform mesh |
| `SplineUpDir` | `FVector` | Axis (in component space) that is used to determine X axis for co-ordinates along spline |
| `bAllowSplineEditingPerInstance` | `uint32` | If true, spline keys may be edited per instance in the level viewport. Otherwise, the spline should be initialized in the construction script. |
| `bSmoothInterpRollScale` | `uint32` | If true, will use smooth interpolation (ease inout) for Scale, Roll, and Offset along this section of spline. If false, uses linear |
| `ForwardAxis` | `TEnumAsByte < ESplineMeshAxis :: Type >` | Chooses the forward axis for the spline mesh orientation |
| `SplineBoundaryMin` | `float` | Minimum coordinate along the spline forward axis which corresponds to start of spline. If set to 0.0, will use bounding box to determine bounds |
| `SplineBoundaryMax` | `float` | Maximum coordinate along the spline forward axis which corresponds to end of spline. If set to 0.0, will use bounding box to determine bounds |
| `BodySetup` | `UBodySetup *` | - |
| `CachedMeshBodySetupGuid` | `FGuid` | - |
| `bMeshDirty` | `uint32` | - |
| `bHasBeenBakedWithLandcape` | `uint32` | - |

## Functions

### `UpdateMesh`

```text
UpdateMesh() -> void
```

Update the collision and render state on the spline mesh following changes to its geometry

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetStartPosition`

```text
GetStartPosition() -> FVector
```

Get the start position of spline in local space

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SetStartPosition`

```text
SetStartPosition(StartPos: FVector, bUpdateMesh: bool) -> void
```

Set the start position of spline in local space

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartPos` | `FVector` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetStartTangent`

```text
GetStartTangent() -> FVector
```

Get the start tangent vector of spline in local space

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SetStartTangent`

```text
SetStartTangent(StartTangent: FVector, bUpdateMesh: bool) -> void
```

Set the start tangent vector of spline in local space

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartTangent` | `FVector` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetEndPosition`

```text
GetEndPosition() -> FVector
```

Get the end position of spline in local space

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SetEndPosition`

```text
SetEndPosition(EndPos: FVector, bUpdateMesh: bool) -> void
```

Set the end position of spline in local space

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EndPos` | `FVector` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetEndTangent`

```text
GetEndTangent() -> FVector
```

Get the end tangent vector of spline in local space

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SetEndTangent`

```text
SetEndTangent(EndTangent: FVector, bUpdateMesh: bool) -> void
```

Set the end tangent vector of spline in local space

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EndTangent` | `FVector` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetStartAndEnd`

```text
SetStartAndEnd(StartPos: FVector, StartTangent: FVector, EndPos: FVector, EndTangent: FVector, bUpdateMesh: bool) -> void
```

Set the start and end, position and tangent, all in local space

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartPos` | `FVector` | - |
| `StartTangent` | `FVector` | - |
| `EndPos` | `FVector` | - |
| `EndTangent` | `FVector` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetStartScale`

```text
GetStartScale() -> FVector2D
```

Get the start scaling

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetStartScale`

```text
SetStartScale(StartScale: FVector2D, bUpdateMesh: bool) -> void
```

Set the start scaling

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartScale` | `FVector2D` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetStartRoll`

```text
GetStartRoll() -> float
```

Get the start roll

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetStartRoll`

```text
SetStartRoll(StartRoll: float, bUpdateMesh: bool) -> void
```

Set the start roll

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartRoll` | `float` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetStartOffset`

```text
GetStartOffset() -> FVector2D
```

Get the start offset

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetStartOffset`

```text
SetStartOffset(StartOffset: FVector2D, bUpdateMesh: bool) -> void
```

Set the start offset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartOffset` | `FVector2D` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetEndScale`

```text
GetEndScale() -> FVector2D
```

Get the end scaling

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetEndScale`

```text
SetEndScale(EndScale: FVector2D, bUpdateMesh: bool) -> void
```

Set the end scaling

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EndScale` | `FVector2D` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetEndRoll`

```text
GetEndRoll() -> float
```

Get the end roll

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetEndRoll`

```text
SetEndRoll(EndRoll: float, bUpdateMesh: bool) -> void
```

Set the end roll

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EndRoll` | `float` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetEndOffset`

```text
GetEndOffset() -> FVector2D
```

Get the end offset

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetEndOffset`

```text
SetEndOffset(EndOffset: FVector2D, bUpdateMesh: bool) -> void
```

Set the end offset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EndOffset` | `FVector2D` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetForwardAxis`

```text
GetForwardAxis() -> ESplineMeshAxis :: Type
```

Get the forward axis

**Returns**

| Type | Description |
|---|---|
| `ESplineMeshAxis :: Type` | - |

### `SetForwardAxis`

```text
SetForwardAxis(InForwardAxis: ESplineMeshAxis :: Type, bUpdateMesh: bool) -> void
```

Set the forward axis

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InForwardAxis` | `ESplineMeshAxis :: Type` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSplineUpDir`

```text
GetSplineUpDir() -> FVector
```

Get the spline up direction

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SetSplineUpDir`

```text
SetSplineUpDir(InSplineUpDir: FVector &, bUpdateMesh: bool) -> void
```

Set the spline up direction

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSplineUpDir` | `FVector &` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBoundaryMin`

```text
GetBoundaryMin() -> float
```

Get the boundary min

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetBoundaryMin`

```text
SetBoundaryMin(InBoundaryMin: float, bUpdateMesh: bool) -> void
```

Set the boundary min

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBoundaryMin` | `float` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBoundaryMax`

```text
GetBoundaryMax() -> float
```

Get the boundary max

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetBoundaryMax`

```text
SetBoundaryMax(InBoundaryMax: float, bUpdateMesh: bool) -> void
```

Set the boundary max

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBoundaryMax` | `float` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
