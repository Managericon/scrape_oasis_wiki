---
id: "api:class:UBackgroundBlur"
title: "UBackgroundBlur"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBackgroundBlur.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBackgroundBlur

A background blur is a container widget that can contain one child widget, providing an opportunity 
  to surround it with adjustable padding and apply a post-process Gaussian blur to all content beneath the widget.
 
   Single Child
   Blur Effect

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Padding` | `FMargin` | The padding area between the slot and the content it contains. |
| `HorizontalAlignment` | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the content horizontally. |
| `VerticalAlignment` | `TEnumAsByte < EVerticalAlignment >` | The alignment of the content vertically. |
| `bApplyAlphaToBlur` | `bool` | True to modulate the strength of the blur based on the widget alpha. |
| `BlurStrength` | `float` | How blurry the background is.  Larger numbers mean more blurry but will result in larger runtime cost on the gpu. |
| `bOverrideAutoRadiusCalculation` | `bool` | Whether or not the radius should be computed automatically or if it should use the radius |
| `BlurType` | `TEnumAsByte < EBlurType >` | Blur type |
| `BlurDirection` | `float` | Blur direction for directional blur |
| `BlurCenter` | `FVector2D` | Blur center for radial and rotate blur |
| `BlurRadius` | `int32` | This is the number of pixels which will be weighted in each direction from any given pixel when computing the blur<br>	  A larger value is more costly but allows for stronger blurs. |
| `BlurMask` | `UTexture *` | A blur mask texture |
| `LowQualityFallbackBrush` | `FSlateBrush` | An image to draw instead of applying a blur when low quality override mode is enabled. <br>	  You can enable low quality mode for background blurs by setting the cvar Slate.ForceBackgroundBlurLowQualityOverride to 1. <br>	  This is usually done in the project's scalability settings |
| `BlurMaskBrush` | `FSlateBrush` | - |

## Functions

### `SetPadding`

```text
SetPadding(InPadding: FMargin) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPadding` | `FMargin` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHorizontalAlignment`

```text
SetHorizontalAlignment(InHorizontalAlignment: EHorizontalAlignment) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InHorizontalAlignment` | `EHorizontalAlignment` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVerticalAlignment`

```text
SetVerticalAlignment(InVerticalAlignment: EVerticalAlignment) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVerticalAlignment` | `EVerticalAlignment` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetApplyAlphaToBlur`

```text
SetApplyAlphaToBlur(bInApplyAlphaToBlur: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInApplyAlphaToBlur` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlurRadius`

```text
SetBlurRadius(InBlurRadius: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlurRadius` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlurStrength`

```text
SetBlurStrength(InStrength: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStrength` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlurDirection`

```text
SetBlurDirection(InDirection: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDirection` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlurCenter`

```text
SetBlurCenter(InCenter: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCenter` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlurMask`

```text
SetBlurMask(InTexture: UTexture *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTexture` | `UTexture *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLowQualityFallbackBrush`

```text
SetLowQualityFallbackBrush(InBrush: FSlateBrush &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBrush` | `FSlateBrush &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
