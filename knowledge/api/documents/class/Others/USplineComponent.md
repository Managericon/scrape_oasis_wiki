---
id: "api:class:USplineComponent"
title: "USplineComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/USplineComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# USplineComponent

A spline component is a spline shape which can be used for other purposes (e.g. animating objects). It contains debug rendering capabilities.

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SplineCurves` | `FSplineCurves` | - |
| `SplineInfo_DEPRECATED` | `FInterpCurveVector` | Deprecated - please use GetSplinePointsPosition() to fetch this FInterpCurve |
| `SplineRotInfo_DEPRECATED` | `FInterpCurveQuat` | Deprecated - please use GetSplinePointsRotation() to fetch this FInterpCurve |
| `SplineScaleInfo_DEPRECATED` | `FInterpCurveVector` | Deprecated - please use GetSplinePointsScale() to fetch this FInterpCurve |
| `SplineReparamTable_DEPRECATED` | `FInterpCurveFloat` | - |
| `bAllowSplineEditingPerInstance_DEPRECATED` | `bool` | - |
| `ReparamStepsPerSegment` | `int32` | Number of steps per spline segment to place in the reparameterization table |
| `Duration` | `float` | Specifies the duration of the spline in seconds |
| `bStationaryEndpoints` | `bool` | Whether the endpoints of the spline are considered stationary when traversing the spline at non-constant velocity.  Essentially this sets the endpoints' tangents to zero vectors. |
| `bSplineHasBeenEdited` | `bool` | Whether the spline has been edited from its default by the spline component visualizer |
| `bModifiedByConstructionScript` | `bool` | Whether the UCS has made changes to the spline points |
| `bInputSplinePointsToConstructionScript` | `bool` | Whether the spline points should be passed to the User Construction Script so they can be further manipulated by it.<br>	  If false, they will not be visible to it, and it will not be able to influence the per-instance positions set in the editor. |
| `bDrawDebug` | `bool` | If true, the spline will be rendered if the Splines showflag is set. |
| `bClosedLoop` | `bool` | Whether the spline is to be considered as a closed loop.<br>	  Use SetClosedLoop() to set this property, and IsClosedLoop() to read it. |
| `bLoopPositionOverride` | `bool` | - |
| `LoopPosition` | `float` | - |
| `DefaultUpVector` | `FVector` | Default up vector in local space to be used when calculating transforms along the spline |
| `bUseConfigRotation` | `bool` | Engine Modify Start |
| `bUseConfigRotationXY` | `bool` | - |
| `EditorUnselectedSplineSegmentColor` | `FLinearColor` | Engine Modify End<br>	 <br>	 Color of an unselected spline component segment in the editor |
| `EditorSelectedSplineSegmentColor` | `FLinearColor` | Color of a selected spline component segment in the editor |
| `bAllowDiscontinuousSpline` | `bool` | Whether the spline's leave and arrive tangents can be different |
| `bShouldVisualizeScale` | `bool` | Whether scale visualization should be displayed |
| `ScaleVisualizationWidth` | `float` | Width of spline in editor for use with scale visualization |
| `PostionModifyer` | `USplineComponentEditorModifer *` | - |
| `SelectedIndexs` | `TSet < int32 >` | - |
| `SnappingType` | `ESplineSnappingType` | - |
| `SnapInterval` | `float` | - |
| `SnapTopDownRange` | `FVector2D` | - |
| `TraceLength` | `float` | - |

## Functions

### `UpdateSpline`

```text
UpdateSpline() -> void
```

Update the spline tangents and SplineReparamTable

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDistanceAlongSplineAtSplineInputKey`

```text
GetDistanceAlongSplineAtSplineInputKey(InKey: float) -> float
```

Get distance along the spline at the provided input key value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InKey` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetUnselectedSplineSegmentColor`

```text
SetUnselectedSplineSegmentColor(SegmentColor: FLinearColor &) -> void
```

Specify unselected spline component segment color in the editor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SegmentColor` | `FLinearColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSelectedSplineSegmentColor`

```text
SetSelectedSplineSegmentColor(SegmentColor: FLinearColor &) -> void
```

Specify selected spline component segment color in the editor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SegmentColor` | `FLinearColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EditorSnapToGround`

```text
EditorSnapToGround() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EditorNormalizeSplineTangent`

```text
EditorNormalizeSplineTangent() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDrawDebug`

```text
SetDrawDebug(bShow: bool) -> void
```

Specify whether this spline should be rendered when the EditorGame spline show flag is set

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bShow` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetClosedLoop`

```text
SetClosedLoop(bInClosedLoop: bool, bUpdateSpline: bool) -> void
```

Specify whether the spline is a closed loop or not. The loop position will be at 1.0 after the last point's input key

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInClosedLoop` | `bool` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetClosedLoopAtPosition`

```text
SetClosedLoopAtPosition(bInClosedLoop: bool, Key: float, bUpdateSpline: bool) -> void
```

Specify whether the spline is a closed loop or not, and if so, the input key corresponding to the loop point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInClosedLoop` | `bool` | - |
| `Key` | `float` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsClosedLoop`

```text
IsClosedLoop() -> bool
```

Check whether the spline is a closed loop or not

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ClearSplinePoints`

```text
ClearSplinePoints(bUpdateSpline: bool) -> void
```

Clears all the points in the spline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddPoint`

```text
AddPoint(Point: FSplinePoint &, bUpdateSpline: bool) -> void
```

Adds an FSplinePoint to the spline. This contains its input key, position, tangent, rotation and scale.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FSplinePoint &` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddPoints`

```text
AddPoints(Points: TArray < FSplinePoint > &, bUpdateSpline: bool) -> void
```

Adds an array of FSplinePoints to the spline.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Points` | `TArray < FSplinePoint > &` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddSplinePoint`

```text
AddSplinePoint(Position: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type, bUpdateSpline: bool) -> void
```

Adds a point to the spline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Position` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddSplinePointAtIndex`

```text
AddSplinePointAtIndex(Position: FVector &, Index: int32, CoordinateSpace: ESplineCoordinateSpace :: Type, bUpdateSpline: bool) -> void
```

Adds a point to the spline at the specified index

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Position` | `FVector &` | - |
| `Index` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveSplinePoint`

```text
RemoveSplinePoint(Index: int32, bUpdateSpline: bool) -> void
```

Removes point at specified index from the spline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddSplineWorldPoint`

```text
AddSplineWorldPoint(Position: FVector &) -> void
```

Adds a world space point to the spline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Position` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddSplineLocalPoint`

```text
AddSplineLocalPoint(Position: FVector &) -> void
```

Adds a local space point to the spline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Position` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSplinePoints`

```text
SetSplinePoints(Points: TArray < FVector > &, CoordinateSpace: ESplineCoordinateSpace :: Type, bUpdateSpline: bool) -> void
```

Sets the spline to an array of points

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Points` | `TArray < FVector > &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSplineWorldPoints`

```text
SetSplineWorldPoints(Points: TArray < FVector > &) -> void
```

Sets the spline to an array of world space points

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Points` | `TArray < FVector > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSplineLocalPoints`

```text
SetSplineLocalPoints(Points: TArray < FVector > &) -> void
```

Sets the spline to an array of local space points

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Points` | `TArray < FVector > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLocationAtSplinePoint`

```text
SetLocationAtSplinePoint(PointIndex: int32, InLocation: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type, bUpdateSpline: bool) -> void
```

Move an existing point to a new location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `InLocation` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWorldLocationAtSplinePoint`

```text
SetWorldLocationAtSplinePoint(PointIndex: int32, InLocation: FVector &) -> void
```

Move an existing point to a new world location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `InLocation` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTangentAtSplinePoint`

```text
SetTangentAtSplinePoint(PointIndex: int32, InTangent: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type, bUpdateSpline: bool) -> void
```

Specify the tangent at a given spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `InTangent` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTangentsAtSplinePoint`

```text
SetTangentsAtSplinePoint(PointIndex: int32, InArriveTangent: FVector &, InLeaveTangent: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type, bUpdateSpline: bool) -> void
```

Specify the tangents at a given spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `InArriveTangent` | `FVector &` | - |
| `InLeaveTangent` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetUpVectorAtSplinePoint`

```text
SetUpVectorAtSplinePoint(PointIndex: int32, InUpVector: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type, bUpdateSpline: bool) -> void
```

Specify the up vector at a given spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `InUpVector` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSplinePointType`

```text
GetSplinePointType(PointIndex: int32) -> ESplinePointType :: Type
```

Get the type of a spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `ESplinePointType :: Type` | - |

### `SetSplinePointType`

```text
SetSplinePointType(PointIndex: int32, Type: ESplinePointType :: Type, bUpdateSpline: bool) -> void
```

Specify the type of a spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `Type` | `ESplinePointType :: Type` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetNumberOfSplinePoints`

```text
GetNumberOfSplinePoints() -> int32
```

Get the number of points that make up this spline

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetLocationAtSplinePoint`

```text
GetLocationAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Get the location at spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetWorldLocationAtSplinePoint`

```text
GetWorldLocationAtSplinePoint(PointIndex: int32) -> FVector
```

Get the world location at spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetDirectionAtSplinePoint`

```text
GetDirectionAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Get the location at spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTangentAtSplinePoint`

```text
GetTangentAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Get the tangent at spline point. This fetches the Leave tangent of the point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetArriveTangentAtSplinePoint`

```text
GetArriveTangentAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Get the arrive tangent at spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetLeaveTangentAtSplinePoint`

```text
GetLeaveTangentAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Get the leave tangent at spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRotationAtSplinePoint`

```text
GetRotationAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FRotator
```

Get the rotation at spline point as a rotator

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `GetUpVectorAtSplinePoint`

```text
GetUpVectorAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Get the up vector at spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRightVectorAtSplinePoint`

```text
GetRightVectorAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Get the right vector at spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRollAtSplinePoint`

```text
GetRollAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type) -> float
```

Get the amount of roll at spline point, in degrees

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetScaleAtSplinePoint`

```text
GetScaleAtSplinePoint(PointIndex: int32) -> FVector
```

Get the scale at spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTransformAtSplinePoint`

```text
GetTransformAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseScale: bool) -> FTransform
```

Get the transform at spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseScale` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `GetLocationAndTangentAtSplinePoint`

```text
GetLocationAndTangentAtSplinePoint(PointIndex: int32, Location: FVector &, Tangent: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type) -> void
```

Get location and tangent at a spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `Location` | `FVector &` | - |
| `Tangent` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLocalLocationAndTangentAtSplinePoint`

```text
GetLocalLocationAndTangentAtSplinePoint(PointIndex: int32, LocalLocation: FVector &, LocalTangent: FVector &) -> void
```

Get local location and tangent at a spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `LocalLocation` | `FVector &` | - |
| `LocalTangent` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDistanceAlongSplineAtSplinePoint`

```text
GetDistanceAlongSplineAtSplinePoint(PointIndex: int32) -> float
```

Get the distance along the spline at the spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetSplineLength`

```text
GetSplineLength() -> float
```

Returns total length along this spline

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetDefaultUpVector`

```text
SetDefaultUpVector(UpVector: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type) -> void
```

Sets the default up vector used by this spline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UpVector` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDefaultUpVector`

```text
GetDefaultUpVector(CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Gets the default up vector used by this spline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetInputKeyAtDistanceAlongSpline`

```text
GetInputKeyAtDistanceAlongSpline(Distance: float) -> float
```

Given a distance along the length of this spline, return the corresponding input key at that point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetTimeAtDistanceAlongSpline`

```text
GetTimeAtDistanceAlongSpline(Distance: float) -> float
```

Given a distance along the length of this spline, return the corresponding time at that point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetLocationAtDistanceAlongSpline`

```text
GetLocationAtDistanceAlongSpline(Distance: float, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a distance along the length of this spline, return the point in space where this puts you

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetWorldLocationAtDistanceAlongSpline`

```text
GetWorldLocationAtDistanceAlongSpline(Distance: float) -> FVector
```

Given a distance along the length of this spline, return the point in world space where this puts you

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetDirectionAtDistanceAlongSpline`

```text
GetDirectionAtDistanceAlongSpline(Distance: float, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a distance along the length of this spline, return a unit direction vector of the spline tangent there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetWorldDirectionAtDistanceAlongSpline`

```text
GetWorldDirectionAtDistanceAlongSpline(Distance: float) -> FVector
```

Given a distance along the length of this spline, return a unit direction vector of the spline tangent there, in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTangentAtDistanceAlongSpline`

```text
GetTangentAtDistanceAlongSpline(Distance: float, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a distance along the length of this spline, return the tangent vector of the spline there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetWorldTangentAtDistanceAlongSpline`

```text
GetWorldTangentAtDistanceAlongSpline(Distance: float) -> FVector
```

Given a distance along the length of this spline, return the tangent vector of the spline there, in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRotationAtDistanceAlongSpline`

```text
GetRotationAtDistanceAlongSpline(Distance: float, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FRotator
```

Given a distance along the length of this spline, return a rotation corresponding to the spline's rotation there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `GetWorldRotationAtDistanceAlongSpline`

```text
GetWorldRotationAtDistanceAlongSpline(Distance: float) -> FRotator
```

Given a distance along the length of this spline, return a rotation corresponding to the spline's rotation there, in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `GetUpVectorAtDistanceAlongSpline`

```text
GetUpVectorAtDistanceAlongSpline(Distance: float, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a distance along the length of this spline, return a unit direction vector corresponding to the spline's up vector there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRightVectorAtDistanceAlongSpline`

```text
GetRightVectorAtDistanceAlongSpline(Distance: float, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a distance along the length of this spline, return a unit direction vector corresponding to the spline's right vector there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRollAtDistanceAlongSpline`

```text
GetRollAtDistanceAlongSpline(Distance: float, CoordinateSpace: ESplineCoordinateSpace :: Type) -> float
```

Given a distance along the length of this spline, return the spline's roll there, in degrees.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetScaleAtDistanceAlongSpline`

```text
GetScaleAtDistanceAlongSpline(Distance: float) -> FVector
```

Given a distance along the length of this spline, return the spline's scale there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTransformAtDistanceAlongSpline`

```text
GetTransformAtDistanceAlongSpline(Distance: float, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseScale: bool) -> FTransform
```

Given a distance along the length of this spline, return an FTransform corresponding to that point on the spline.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseScale` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `GetLocationAtTime`

```text
GetLocationAtTime(Time: float, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseConstantVelocity: bool) -> FVector
```

Given a time from 0 to the spline duration, return the point in space where this puts you

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetWorldLocationAtTime`

```text
GetWorldLocationAtTime(Time: float, bUseConstantVelocity: bool) -> FVector
```

Given a time from 0 to the spline duration, return the point in space where this puts you

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetDirectionAtTime`

```text
GetDirectionAtTime(Time: float, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseConstantVelocity: bool) -> FVector
```

Given a time from 0 to the spline duration, return a unit direction vector of the spline tangent there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetWorldDirectionAtTime`

```text
GetWorldDirectionAtTime(Time: float, bUseConstantVelocity: bool) -> FVector
```

Given a time from 0 to the spline duration, return a unit direction vector of the spline tangent there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTangentAtTime`

```text
GetTangentAtTime(Time: float, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseConstantVelocity: bool) -> FVector
```

Given a time from 0 to the spline duration, return the spline's tangent there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRotationAtTime`

```text
GetRotationAtTime(Time: float, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseConstantVelocity: bool) -> FRotator
```

Given a time from 0 to the spline duration, return a rotation corresponding to the spline's position and direction there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `GetWorldRotationAtTime`

```text
GetWorldRotationAtTime(Time: float, bUseConstantVelocity: bool) -> FRotator
```

Given a time from 0 to the spline duration, return a rotation corresponding to the spline's position and direction there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `GetUpVectorAtTime`

```text
GetUpVectorAtTime(Time: float, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseConstantVelocity: bool) -> FVector
```

Given a time from 0 to the spline duration, return the spline's up vector there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRightVectorAtTime`

```text
GetRightVectorAtTime(Time: float, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseConstantVelocity: bool) -> FVector
```

Given a time from 0 to the spline duration, return the spline's right vector there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTransformAtTime`

```text
GetTransformAtTime(Time: float, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseConstantVelocity: bool, bUseScale: bool) -> FTransform
```

Given a time from 0 to the spline duration, return the spline's transform at the corresponding position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseConstantVelocity` | `bool` | - |
| `bUseScale` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `GetRollAtTime`

```text
GetRollAtTime(Time: float, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseConstantVelocity: bool) -> float
```

Given a time from 0 to the spline duration, return the spline's roll there, in degrees.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetScaleAtTime`

```text
GetScaleAtTime(Time: float, bUseConstantVelocity: bool) -> FVector
```

Given a time from 0 to the spline duration, return the spline's scale there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `FindInputKeyClosestToWorldLocation`

```text
FindInputKeyClosestToWorldLocation(WorldLocation: FVector &) -> float
```

Given a location, in world space, return the input key closest to that location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `FindLocationClosestToWorldLocation`

```text
FindLocationClosestToWorldLocation(WorldLocation: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a location, in world space, return the point on the curve that is closest to the location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `FindDirectionClosestToWorldLocation`

```text
FindDirectionClosestToWorldLocation(WorldLocation: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a location, in world spcae, return a unit direction vector of the spline tangent closest to the location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `FindTangentClosestToWorldLocation`

```text
FindTangentClosestToWorldLocation(WorldLocation: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a location, in world space, return the tangent vector of the spline closest to the location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `FindRotationClosestToWorldLocation`

```text
FindRotationClosestToWorldLocation(WorldLocation: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FRotator
```

Given a location, in world space, return rotation corresponding to the spline's rotation closest to the location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `FindUpVectorClosestToWorldLocation`

```text
FindUpVectorClosestToWorldLocation(WorldLocation: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a location, in world space, return a unit direction vector corresponding to the spline's up vector closest to the location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `FindRightVectorClosestToWorldLocation`

```text
FindRightVectorClosestToWorldLocation(WorldLocation: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a location, in world space, return a unit direction vector corresponding to the spline's right vector closest to the location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `FindRollClosestToWorldLocation`

```text
FindRollClosestToWorldLocation(WorldLocation: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type) -> float
```

Given a location, in world space, return the spline's roll closest to the location, in degrees.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `FindScaleClosestToWorldLocation`

```text
FindScaleClosestToWorldLocation(WorldLocation: FVector &) -> FVector
```

Given a location, in world space, return the spline's scale closest to the location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `FindTransformClosestToWorldLocation`

```text
FindTransformClosestToWorldLocation(WorldLocation: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseScale: bool) -> FTransform
```

Given a location, in world space, return an FTransform closest to that location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseScale` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

## Language

`cpp`
