---
id: "api:class:USlateBlueprintLibrary"
title: "USlateBlueprintLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/USlateBlueprintLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# USlateBlueprintLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `IsUnderLocation`

```text
IsUnderLocation(Geometry: FGeometry &, AbsoluteCoordinate: FVector2D &) -> bool
```

Absolute coordinates could be either desktop or window space depending on what space the root of the widget hierarchy is in.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry &` | - |
| `AbsoluteCoordinate` | `FVector2D &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the provided location in absolute coordinates is within the bounds of this geometry. |

### `AbsoluteToLocal`

```text
AbsoluteToLocal(Geometry: FGeometry &, AbsoluteCoordinate: FVector2D) -> FVector2D
```

Absolute coordinates could be either desktop or window space depending on what space the root of the widget hierarchy is in.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry &` | - |
| `AbsoluteCoordinate` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | Transforms AbsoluteCoordinate into the local space of this Geometry. |

### `LocalToAbsolute`

```text
LocalToAbsolute(Geometry: FGeometry &, LocalCoordinate: FVector2D) -> FVector2D
```

Translates local coordinates into absolute coordinates
	 
	  Absolute coordinates could be either desktop or window space depending on what space the root of the widget hierarchy is in.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry &` | - |
| `LocalCoordinate` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | Absolute coordinates |

### `GetLocalSize`

```text
GetLocalSize(Geometry: FGeometry &) -> FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | the size of the geometry in local space. |

### `GetAbsoluteSize`

```text
GetAbsoluteSize(Geometry: FGeometry &) -> FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | the size of the geometry in absolute space. |

### `GetAbsolutePosition`

```text
GetAbsolutePosition(Geometry: FGeometry &) -> FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `EqualEqual_SlateBrush`

```text
EqualEqual_SlateBrush(A: FSlateBrush &, B: FSlateBrush &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FSlateBrush &` | - |
| `B` | `FSlateBrush &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether brushes A and B are identical. |

### `LocalToViewport`

```text
LocalToViewport(WorldContextObject: UObject *, Geometry: FGeometry &, LocalCoordinate: FVector2D, PixelPosition: FVector2D &, ViewportPosition: FVector2D &) -> void
```

Translates local coordinate of the geometry provided into local viewport coordinates.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Geometry` | `FGeometry &` | - |
| `LocalCoordinate` | `FVector2D` | - |
| `PixelPosition` | `FVector2D &` | The position in the game's viewport, usable for line traces and |
| `ViewportPosition` | `FVector2D &` | The position in the space of other widgets in the viewport. Like if you wanted |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AbsoluteToViewport`

```text
AbsoluteToViewport(WorldContextObject: UObject *, AbsoluteDesktopCoordinate: FVector2D, PixelPosition: FVector2D &, ViewportPosition: FVector2D &) -> void
```

Translates absolute coordinate in desktop space of the geometry provided into local viewport coordinates.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `AbsoluteDesktopCoordinate` | `FVector2D` | - |
| `PixelPosition` | `FVector2D &` | The position in the game's viewport, usable for line traces and |
| `ViewportPosition` | `FVector2D &` | The position in the space of other widgets in the viewport. Like if you wanted |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ScreenToWidgetLocal`

```text
ScreenToWidgetLocal(WorldContextObject: UObject *, Geometry: FGeometry &, ScreenPosition: FVector2D, LocalCoordinate: FVector2D &) -> void
```

Translates a screen position in pixels into the local space of a widget with the given geometry.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Geometry` | `FGeometry &` | - |
| `ScreenPosition` | `FVector2D` | - |
| `LocalCoordinate` | `FVector2D &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ScreenToWidgetAbsolute`

```text
ScreenToWidgetAbsolute(WorldContextObject: UObject *, ScreenPosition: FVector2D, AbsoluteCoordinate: FVector2D &) -> void
```

Translates a screen position in pixels into absolute application coordinates.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ScreenPosition` | `FVector2D` | - |
| `AbsoluteCoordinate` | `FVector2D &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ScreenToViewport`

```text
ScreenToViewport(WorldContextObject: UObject *, ScreenPosition: FVector2D, ViewportPosition: FVector2D &) -> void
```

Translates a screen position in pixels into the local space of the viewport widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ScreenPosition` | `FVector2D` | - |
| `ViewportPosition` | `FVector2D &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSlateConstant_GlobalScrollAmount`

```text
GetSlateConstant_GlobalScrollAmount() -> float
```

Provide GetGlobalScrollAmount() to Lua.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `ReleaseAllMouseCapture`

```text
ReleaseAllMouseCapture() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReleaseMouseCaptureWithIndex`

```text
ReleaseMouseCaptureWithIndex(InIndex: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReleaseAllMousePassThroughCapture`

```text
ReleaseAllMousePassThroughCapture() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReleaseMousePassThroughCaptureWithIndex`

```text
ReleaseMousePassThroughCaptureWithIndex(InIndex: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMouseCaptor`

```text
SetMouseCaptor(PointerIndex: int32, Widget: UWidget *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointerIndex` | `int32` | - |
| `Widget` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetMousePassThroughCaptor`

```text
SetMousePassThroughCaptor(PointerIndex: int32, Widget: UWidget *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointerIndex` | `int32` | - |
| `Widget` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`
