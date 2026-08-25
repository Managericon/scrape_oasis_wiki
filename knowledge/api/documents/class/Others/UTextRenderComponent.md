---
id: "api:class:UTextRenderComponent"
title: "UTextRenderComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UTextRenderComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UTextRenderComponent

Renders text in the world with given font. Contains usual font related attributes such as Scale, Alignment, Color etc.

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Text` | `FText` | Text content, can be multi line using   <br>as line separator |
| `TextMaterial` | `UMaterialInterface *` | Text material |
| `Font` | `UFont *` | Text font |
| `HorizontalAlignment` | `TEnumAsByte < enum EHorizTextAligment >` | Horizontal text alignment |
| `VerticalAlignment` | `TEnumAsByte < enum EVerticalTextAligment >` | Vertical text alignment |
| `TextRenderColor` | `FColor` | Color of the text, can be accessed as vertex color |
| `XScale` | `float` | Horizontal scale, default is 1.0 |
| `YScale` | `float` | Vertical scale, default is 1.0 |
| `WorldSize` | `float` | Vertical size of the fonts largest character in world units. Transform, XScale and YScale will affect final size. |
| `InvDefaultSize` | `float` | The inverse of the Font's character height. |
| `HorizSpacingAdjust` | `float` | Horizontal adjustment per character, default is 0.0 |
| `VertSpacingAdjust` | `float` | Vertical adjustment per character, default is 0.0 |
| `bAlwaysRenderAsText` | `uint32` | Allows text to draw unmodified when using debug visualization modes. |

## Functions

### `SetText`

```text
SetText(Value: FString &) -> void
```

Change the text value and signal the primitives to be rebuilt 
	  The FString variant is deprecated in favor of the FText variant

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetText`

```text
K2_SetText(Value: FText &) -> void
```

Change the text value and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTextMaterial`

```text
SetTextMaterial(Material: UMaterialInterface *) -> void
```

Change the text material and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Material` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFont`

```text
SetFont(Value: UFont *) -> void
```

Change the font and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `UFont *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHorizontalAlignment`

```text
SetHorizontalAlignment(Value: EHorizTextAligment) -> void
```

Change the horizontal alignment and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `EHorizTextAligment` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVerticalAlignment`

```text
SetVerticalAlignment(Value: EVerticalTextAligment) -> void
```

Change the vertical alignment and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `EVerticalTextAligment` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTextRenderColor`

```text
SetTextRenderColor(Value: FColor) -> void
```

Change the text render color and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetXScale`

```text
SetXScale(Value: float) -> void
```

Change the text X scale and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetYScale`

```text
SetYScale(Value: float) -> void
```

Change the text Y scale and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHorizSpacingAdjust`

```text
SetHorizSpacingAdjust(Value: float) -> void
```

Change the text horizontal spacing adjustment and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVertSpacingAdjust`

```text
SetVertSpacingAdjust(Value: float) -> void
```

Change the text vertical spacing adjustment and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWorldSize`

```text
SetWorldSize(Value: float) -> void
```

Change the world size of the text and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTextLocalSize`

```text
GetTextLocalSize() -> FVector
```

Get local size of text

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTextWorldSize`

```text
GetTextWorldSize() -> FVector
```

Get world space size of text

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

## Language

`cpp`
