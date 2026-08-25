---
id: "api:class:UTextBlock"
title: "UTextBlock"
source: "https://developer.gp.qq.com/api/class/detail/Others/UTextBlock.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UTextBlock

A simple static text widget.
 
   No Children
   Text

## Inheritance

`UTextLayoutWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Text` | `FText` | The text to display |
| `TextDelegate` | `FGetText` | A bindable delegate to allow logic to drive the text of the widget |
| `ColorAndOpacity` | `FSlateColor` | The color of the text |
| `ColorAndOpacityDelegate` | `FGetSlateColor` | A bindable delegate for the ColorAndOpacity. |
| `Font` | `FSlateFontInfo` | The font to render the text with |
| `ShadowOffset` | `FVector2D` | The direction the shadow is cast |
| `ShadowColorAndOpacity` | `FLinearColor` | The color of the shadow |
| `ShadowColorAndOpacityDelegate` | `FGetLinearColor` | A bindable delegate for the ShadowColorAndOpacity. |
| `MinDesiredWidth` | `float` | The minimum desired size for the text |
| `AutoEllipsisText` | `bool` | - |
| `MutiEllipsisText` | `bool` | - |
| `MutiEllipsisLine` | `int32` | - |
| `bWrapWithInvalidationPanel` | `bool` | If true, it will automatically wrap this text widget with an invalidation panel |

## Functions

### `SetColorAndOpacity`

```text
SetColorAndOpacity(InColorAndOpacity: FSlateColor) -> void
```

Sets the color and opacity of the text in this text block

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColorAndOpacity` | `FSlateColor` | The new text color and opacity |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetColorRGBStr`

```text
SetColorRGBStr(HexString: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HexString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOpacity`

```text
SetOpacity(InOpacity: float) -> void
```

Sets the opacity of the text in this text block

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOpacity` | `float` | The new text opacity |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetShadowColorAndOpacity`

```text
SetShadowColorAndOpacity(InShadowColorAndOpacity: FLinearColor) -> void
```

Sets the color and opacity of the text drop shadow
	  Note: if opacity is zero no shadow will be drawn

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InShadowColorAndOpacity` | `FLinearColor` | The new drop shadow color and opacity |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetShadowOffset`

```text
SetShadowOffset(InShadowOffset: FVector2D) -> void
```

Sets the offset that the text drop shadow should be drawn at

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InShadowOffset` | `FVector2D` | The new offset |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFont`

```text
SetFont(InFontInfo: FSlateFontInfo) -> void
```

Dynamically set the font info for this text block

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFontInfo` | `FSlateFontInfo` | THe new font info |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetJustification`

```text
SetJustification(InJustification: ETextJustify :: Type) -> void
```

Set the text justification for this text block

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InJustification` | `ETextJustify :: Type` | new justification |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVerticalJustification`

```text
SetVerticalJustification(InJustification: ETextVerticalJustify :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InJustification` | `ETextVerticalJustify :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNeedVerticalJustificationWhenOverflow`

```text
SetNeedVerticalJustificationWhenOverflow(InEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMinDesiredWidth`

```text
SetMinDesiredWidth(InMinDesiredWidth: float) -> void
```

Set the minimum desired width for this text block

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMinDesiredWidth` | `float` | new minimum desired width |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAutoEllipsisText`

```text
SetAutoEllipsisText(InAutoEllipsisText: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAutoEllipsisText` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWrapTextAt`

```text
SetWrapTextAt(InWrapTextAt: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InWrapTextAt` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMutiEllipsisText`

```text
SetMutiEllipsisText(InMutiEllipsisText: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMutiEllipsisText` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetText`

```text
GetText() -> FText
```

Gets the widget text

**Returns**

| Type | Description |
|---|---|
| `FText` | The widget text |

### `GetLocalText`

```text
GetLocalText() -> FText
```

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `SetText`

```text
SetText(InText: FText) -> void
```

Directly sets the widget text.
	  Warning: This will wipe any binding created for the Text property!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText` | The text to assign to the widget |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnTextBlockTextChangeDelegate`

```text
OnTextBlockTextChangeDelegate(TextChanged: FText) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TextChanged` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
