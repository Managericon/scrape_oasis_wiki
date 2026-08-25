---
id: "api:class:UBorder"
title: "UBorder"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBorder.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBorder

A border is a container widget that can contain one child widget, providing an opportunity 
  to surround it with a background image and adjustable padding.
 
   Single Child
   Image

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `HorizontalAlignment` | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the content horizontally. |
| `VerticalAlignment` | `TEnumAsByte < EVerticalAlignment >` | The alignment of the content vertically. |
| `bShowEffectWhenDisabled` | `uint8` | Whether or not to show the disabled effect when this border is disabled |
| `ContentColorAndOpacity` | `FLinearColor` | Color and opacity multiplier of content in the border |
| `ContentColorAndOpacityDelegate` | `FGetLinearColor` | A bindable delegate for the ContentColorAndOpacity. |
| `ResetBlendColor` | `bool` | - |
| `Padding` | `FMargin` | The padding area between the slot and the content it contains. |
| `Background` | `FSlateBrush` | Brush to drag as the background |
| `BackgroundDelegate` | `FGetSlateBrush` | A bindable delegate for the Brush. |
| `BrushColor` | `FLinearColor` | Color and opacity of the actual border image |
| `BrushColorDelegate` | `FGetLinearColor` | A bindable delegate for the BrushColor. |
| `DesiredSizeScale` | `FVector2D` | Scales the computed desired size of this border and its contents. Useful<br>	  for making things that slide open without having to hard-code their size.<br>	  Note: if the parent widget is set up to ignore this widget's desired size,<br>	  then changing this value will have no effect. |
| `OnMouseButtonDownEvent` | `FOnPointerEvent` | - |
| `OnMouseButtonUpEvent` | `FOnPointerEvent` | - |
| `OnMouseMoveEvent` | `FOnPointerEvent` | - |
| `OnMouseDoubleClickEvent` | `FOnPointerEvent` | - |

## Functions

### `SetContentColorAndOpacity`

```text
SetContentColorAndOpacity(InContentColorAndOpacity: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InContentColorAndOpacity` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetResetBlendColor`

```text
SetResetBlendColor(bResetBlendColor: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bResetBlendColor` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

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

### `SetBrushColor`

```text
SetBrushColor(InBrushColor: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBrushColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrush`

```text
SetBrush(InBrush: FSlateBrush &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBrush` | `FSlateBrush &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrushFromAsset`

```text
SetBrushFromAsset(Asset: USlateBrushAsset *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Asset` | `USlateBrushAsset *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrushFromTexture`

```text
SetBrushFromTexture(Texture: UTexture2D *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Texture` | `UTexture2D *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrushFromMaterial`

```text
SetBrushFromMaterial(Material: UMaterialInterface *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Material` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDynamicMaterial`

```text
GetDynamicMaterial() -> UMaterialInstanceDynamic *
```

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | - |

### `SetDesiredSizeScale`

```text
SetDesiredSizeScale(InScale: FVector2D) -> void
```

Sets the DesireSizeScale of this border.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InScale` | `FVector2D` | The X and Y multipliers for the desired size |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
