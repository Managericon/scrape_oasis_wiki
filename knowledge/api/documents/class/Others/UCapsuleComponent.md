---
id: "api:class:UCapsuleComponent"
title: "UCapsuleComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCapsuleComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UCapsuleComponent

A capsule generally used for simple collision. Bounds are rendered as lines in the editor.

## Inheritance

`UShapeComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CapsuleHalfHeight` | `float` | Half-height, from center of capsule to the end of top or bottom hemisphere.  <br>	 	This cannot be less than CapsuleRadius. |
| `CapsuleRadius` | `float` | Radius of cap hemispheres and center cylinder. <br>	 	This cannot be more than CapsuleHalfHeight. |
| `UseDelayPhysicUpdated` | `int32` | - |
| `bTransformDataDirty` | `bool` | - |
| `CapsuleHeight_DEPRECATED` | `float` | - |

## Functions

### `SetCapsuleSize`

```text
SetCapsuleSize(InRadius: float, InHalfHeight: float, bUpdateOverlaps: bool) -> void
```

Change the capsule size. This is the unscaled size, before component scale is applied.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRadius` | `float` | : radius of end-cap hemispheres and center cylinder. |
| `InHalfHeight` | `float` | : half-height, from capsule center to end of top or bottom hemisphere. |
| `bUpdateOverlaps` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCapsuleRadius`

```text
SetCapsuleRadius(Radius: float, bUpdateOverlaps: bool) -> void
```

Set the capsule radius. This is the unscaled radius, before component scale is applied.
	  If this capsule collides, updates touching array for owner actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Radius` | `float` | : radius of end-cap hemispheres and center cylinder. |
| `bUpdateOverlaps` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCapsuleHalfHeight`

```text
SetCapsuleHalfHeight(HalfHeight: float, bUpdateOverlaps: bool) -> void
```

Set the capsule half-height. This is the unscaled half-height, before component scale is applied.
	  If this capsule collides, updates touching array for owner actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HalfHeight` | `float` | : half-height, from capsule center to end of top or bottom hemisphere. |
| `bUpdateOverlaps` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetScaledCapsuleRadius`

```text
GetScaledCapsuleRadius() -> float
```

Returns the capsule radius scaled by the component scale.

**Returns**

| Type | Description |
|---|---|
| `float` | The capsule radius scaled by the component scale. |

### `GetScaledCapsuleHalfHeight`

```text
GetScaledCapsuleHalfHeight() -> float
```

Returns the capsule half-height scaled by the component scale. This includes both the cylinder and hemisphere cap.

**Returns**

| Type | Description |
|---|---|
| `float` | The capsule half-height scaled by the component scale. |

### `GetScaledCapsuleHalfHeight_WithoutHemisphere`

```text
GetScaledCapsuleHalfHeight_WithoutHemisphere() -> float
```

Returns the capsule half-height minus radius (to exclude the hemisphere), scaled by the component scale.
	 From the center of the capsule this is the vertical distance along the straight cylindrical portion to the point just before the curve of top hemisphere begins.

**Returns**

| Type | Description |
|---|---|
| `float` | The capsule half-height minus radius, scaled by the component scale. |

### `GetScaledCapsuleSize`

```text
GetScaledCapsuleSize(OutRadius: float &, OutHalfHeight: float &) -> void
```

Returns the capsule radius and half-height scaled by the component scale. Half-height includes the hemisphere end cap.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutRadius` | `float &` | Radius of the capsule, scaled by the component scale. |
| `OutHalfHeight` | `float &` | Half-height of the capsule, scaled by the component scale. Includes the hemisphere end cap. |

**Returns**

| Type | Description |
|---|---|
| `void` | The capsule radius and half-height scaled by the component scale. |

### `GetScaledCapsuleSize_WithoutHemisphere`

```text
GetScaledCapsuleSize_WithoutHemisphere(OutRadius: float &, OutHalfHeightWithoutHemisphere: float &) -> void
```

Returns the capsule radius and half-height scaled by the component scale. Half-height excludes the hemisphere end cap.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutRadius` | `float &` | Radius of the capsule, ignoring component scaling. |
| `OutHalfHeightWithoutHemisphere` | `float &` | Half-height of the capsule, scaled by the component scale. Excludes the hemisphere end cap. |

**Returns**

| Type | Description |
|---|---|
| `void` | The capsule radius and half-height scaled by the component scale. |

### `GetUnscaledCapsuleRadius`

```text
GetUnscaledCapsuleRadius() -> float
```

Returns the capsule radius, ignoring component scaling.

**Returns**

| Type | Description |
|---|---|
| `float` | the capsule radius, ignoring component scaling. |

### `GetUnscaledCapsuleHalfHeight`

```text
GetUnscaledCapsuleHalfHeight() -> float
```

Returns the capsule half-height, ignoring component scaling. This includes the hemisphere end cap.

**Returns**

| Type | Description |
|---|---|
| `float` | The capsule radius, ignoring component scaling. |

### `GetUnscaledCapsuleHalfHeight_WithoutHemisphere`

```text
GetUnscaledCapsuleHalfHeight_WithoutHemisphere() -> float
```

Returns the capsule half-height minus radius (to exclude the hemisphere), ignoring component scaling. This excludes the hemisphere end cap.
	 From the center of the capsule this is the vertical distance along the straight cylindrical portion to the point just before the curve of top hemisphere begins.

**Returns**

| Type | Description |
|---|---|
| `float` | The capsule half-height minus radius, ignoring component scaling. |

### `GetUnscaledCapsuleSize`

```text
GetUnscaledCapsuleSize(OutRadius: float &, OutHalfHeight: float &) -> void
```

Returns the capsule radius and half-height scaled by the component scale. Half-height includes the hemisphere end cap.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutRadius` | `float &` | Radius of the capsule, scaled by the component scale. |
| `OutHalfHeight` | `float &` | Half-height of the capsule, scaled by the component scale. Includes the hemisphere end cap. |

**Returns**

| Type | Description |
|---|---|
| `void` | The capsule radius and half-height scaled by the component scale. |

### `GetUnscaledCapsuleSize_WithoutHemisphere`

```text
GetUnscaledCapsuleSize_WithoutHemisphere(OutRadius: float &, OutHalfHeightWithoutHemisphere: float &) -> void
```

Returns the capsule radius and half-height, ignoring component scaling. Half-height excludes the hemisphere end cap.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutRadius` | `float &` | Radius of the capsule, ignoring component scaling. |
| `OutHalfHeightWithoutHemisphere` | `float &` | Half-height of the capsule, scaled by the component scale. Excludes the hemisphere end cap. |

**Returns**

| Type | Description |
|---|---|
| `void` | The capsule radius and half-height (excluding hemisphere end cap), ignoring component scaling. |

### `GetShapeScale`

```text
GetShapeScale() -> float
```

Get the scale used by this shape. This is a uniform scale that is the minimum of any non-uniform scaling.

**Returns**

| Type | Description |
|---|---|
| `float` | the scale used by this shape. |

## Language

`cpp`
