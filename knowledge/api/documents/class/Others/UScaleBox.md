---
id: "api:class:UScaleBox"
title: "UScaleBox"
source: "https://developer.gp.qq.com/api/class/detail/Others/UScaleBox.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UScaleBox

Allows you to place content with a desired size and have it scale to meet the constraints placed on this box's alloted area.  If
  you needed to have a background image scale to fill an area but not become distorted with different aspect ratios, or if you need
  to auto fit some text to an area, this is the control for you.
 
   Single Child
   Aspect Ratio

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Stretch` | `TEnumAsByte < EStretch :: Type >` | The stretching rule to apply when content is stretched |
| `StretchDirection` | `TEnumAsByte < EStretchDirection :: Type >` | Controls in what direction content can be scaled |
| `UserSpecifiedScale` | `float` | Optional scale that can be specified by the User. Used only for UserSpecified stretching. |
| `UserSpecifiedScaleBias` | `float` | Scale bias that can fit to the content, especially for the text exceeded the bounds. <br>	 #if UMG_SCALE_BIAS |
| `IgnoreInheritedScale` | `bool` | Optional bool to ignore the inherited scale. Applies inverse scaling to counteract parents before applying the local scale operation. |
| `UsePcParams` | `bool` | - |
| `StretchPc` | `TEnumAsByte < EStretch :: Type >` | - |
| `StretchDirectionPc` | `TEnumAsByte < EStretchDirection :: Type >` | - |
| `UserSpecifiedScalePc` | `float` | - |
| `UserSpecifiedScaleBiasPc` | `float` | - |
| `IgnoreInheritedScalePc` | `bool` | - |
| `bSingleLayoutPass` | `bool` | Only perform a single layout pass, if you do this, it can save a considerable<br>	  amount of time, however, some things like text may not look correct.  You may also<br>	  see the UI judder between frames.  This generally is caused by not explicitly<br>	  sizing the widget, and instead allowing it to layout based on desired size along<br>	  which won't work in Single Layout Pass mode. |
| `bFroceSlateLayoutCachingCalcSize` | `bool` | - |
| `bForceUseLastUnPrepassChildSize` | `bool` | - |

## Functions

### `SetStretch`

```text
SetStretch(InStretch: EStretch :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStretch` | `EStretch :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetStretchDirection`

```text
SetStretchDirection(InStretchDirection: EStretchDirection :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStretchDirection` | `EStretchDirection :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetUserSpecifiedScale`

```text
SetUserSpecifiedScale(InUserSpecifiedScale: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InUserSpecifiedScale` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIgnoreInheritedScale`

```text
SetIgnoreInheritedScale(bInIgnoreInheritedScale: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInIgnoreInheritedScale` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetUserSpecifiedScaleBias`

```text
SetUserSpecifiedScaleBias(InUserSpecifiedScaleBias: float) -> void
```

#if UMG_SCALEBOX_BIAS

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InUserSpecifiedScaleBias` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPcParamController`

```text
SetPcParamController(InValue: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnUIRectOffsetChange`

```text
OnUIRectOffsetChange() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
