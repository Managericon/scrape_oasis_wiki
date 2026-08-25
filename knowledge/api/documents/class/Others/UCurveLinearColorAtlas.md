---
id: "api:class:UCurveLinearColorAtlas"
title: "UCurveLinearColorAtlas"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCurveLinearColorAtlas.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UCurveLinearColorAtlas

Manages gradient LUT textures for registered actors and assigns them to the corresponding materials on the actor

## Inheritance

`UTexture2D`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TextureSize` | `uint32` | - |
| `bSquareResolution` | `uint32` | Set texture height equal to texture width. |
| `TextureHeight` | `uint32` | - |
| `GradientCurves` | `TArray < UCurveLinearColor * >` | - |
| `bIsDirty` | `uint32` | - |
| `bDisableAllAdjustments` | `uint32` | Disable all color adjustments to preserve negative values in curves. Color adjustments clamp to 0 when enabled. |
| `bHasCachedColorAdjustments` | `uint32` | - |
| `CachedColorAdjustments` | `FCurveAtlasColorAdjustments` | - |

## Functions

### `GetCurvePosition`

```text
GetCurvePosition(InCurve: UCurveLinearColor *, Position: float &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCurve` | `UCurveLinearColor *` | - |
| `Position` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`
