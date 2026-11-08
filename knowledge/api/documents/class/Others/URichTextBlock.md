---
id: "api:class:URichTextBlock"
title: "URichTextBlock"
source: "https://developer.gp.qq.com/api/class/detail/Others/URichTextBlock.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# URichTextBlock

The rich text block
 
   Fancy Text
   No Children

## Inheritance

`UTextLayoutWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Text` | `FText` | The text to display |
| `TextStyleSet` | `UDataTable *` | The data table containing rich text styles |
| `DecoratorClasses` | `TArray < TSubclassOf < URichTextBlockDecorator > >` | Decorator classes to instantiate |
| `DefaultTextStyleOverride` | `FTextBlockStyle` | Text style to apply by default to text in this block |
| `MinDesiredWidth` | `float` | The minimum desired size for the text |
| `bOverrideDefaultStyle` | `bool` | True to specify the default text style for this rich text inline, overriding any default provided in the style set table |
| `DefaultTextStyle` | `FTextBlockStyle` | - |
| `InstanceDecorators` | `TArray < URichTextBlockDecorator * >` | - |

## Functions

### `SetDefaultColorAndOpacity`

```text
SetDefaultColorAndOpacity(InColorAndOpacity: FSlateColor) -> UMG_API void
```

Sets the color and opacity of the default text in this rich text block

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColorAndOpacity` | `FSlateColor` | The new text color and opacity |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `SetDefaultShadowColorAndOpacity`

```text
SetDefaultShadowColorAndOpacity(InShadowColorAndOpacity: FLinearColor) -> UMG_API void
```

Sets the color and opacity of the default text drop shadow
	  Note: if opacity is zero no shadow will be drawn

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InShadowColorAndOpacity` | `FLinearColor` | The new drop shadow color and opacity |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `SetDefaultShadowOffset`

```text
SetDefaultShadowOffset(InShadowOffset: FVector2D) -> UMG_API void
```

Sets the offset that the default text drop shadow should be drawn at

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InShadowOffset` | `FVector2D` | The new offset |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `SetDefaultFont`

```text
SetDefaultFont(InFontInfo: FSlateFontInfo) -> UMG_API void
```

Dynamically set the default font info for this rich text block

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFontInfo` | `FSlateFontInfo` | The new font info |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `SetDefaultStrikeBrush`

```text
SetDefaultStrikeBrush(InStrikeBrush: FSlateBrush &) -> UMG_API void
```

Dynamically set the default strike brush for this rich text block

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStrikeBrush` | `FSlateBrush &` | The new brush to use to strike through text |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `SetMinDesiredWidth`

```text
SetMinDesiredWidth(InMinDesiredWidth: float) -> UMG_API void
```

Set the minimum desired width for this rich text block

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMinDesiredWidth` | `float` | new minimum desired width |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `SetAutoWrapText`

```text
SetAutoWrapText(InAutoTextWrap: bool) -> UMG_API void
```

Set the auto wrap for this rich text block

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAutoTextWrap` | `bool` | to turn wrap on or off |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `SetDefaultTextStyle`

```text
SetDefaultTextStyle(InDefaultTextStyle: FTextBlockStyle &) -> UMG_API void
```

Wholesale override of the currently established default text style

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDefaultTextStyle` | `FTextBlockStyle &` | The new text style to apply to all default (i.e. undecorated) text in the block |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `SetDefaultMaterial`

```text
SetDefaultMaterial(InMaterial: UMaterialInterface *) -> UMG_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMaterial` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `ClearAllDefaultStyleOverrides`

```text
ClearAllDefaultStyleOverrides() -> UMG_API void
```

Remove all overrides made to the default text style and return to the style specified in the style set data table

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `GetDefaultDynamicMaterial`

```text
GetDefaultDynamicMaterial() -> UMG_API UMaterialInstanceDynamic *
```

Creates a dynamic material for the default font or returns it if it already exists

**Returns**

| Type | Description |
|---|---|
| `UMG_API UMaterialInstanceDynamic *` | - |

### `SetDecorators`

```text
SetDecorators(InDecoratorClasses: TArray < TSubclassOf < URichTextBlockDecorator > > &) -> UMG_API void
```

Replaces the existing decorators with the list provided

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDecoratorClasses` | `TArray < TSubclassOf < URichTextBlockDecorator > > &` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `GetText`

```text
GetText() -> UMG_API FText
```

Returns widgets text.

**Returns**

| Type | Description |
|---|---|
| `UMG_API FText` | - |

### `SetText`

```text
SetText(InText: FText &) -> UMG_API virtual void
```

Directly sets the widget text.
	  Warning: This will wipe any binding created for the Text property!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText &` | The text to assign to the widget |

**Returns**

| Type | Description |
|---|---|
| `UMG_API virtual void` | - |

### `GetTextStyleSet`

```text
GetTextStyleSet() -> UMG_API UDataTable *
```

**Returns**

| Type | Description |
|---|---|
| `UMG_API UDataTable *` | - |

### `SetTextStyleSet`

```text
SetTextStyleSet(NewTextStyleSet: UDataTable *) -> UMG_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTextStyleSet` | `UDataTable *` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `GetDecoratorByClass`

```text
GetDecoratorByClass(DecoratorClass: TSubclassOf < URichTextBlockDecorator >) -> UMG_API URichTextBlockDecorator *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DecoratorClass` | `TSubclassOf < URichTextBlockDecorator >` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API URichTextBlockDecorator *` | - |

### `RefreshTextLayout`

```text
RefreshTextLayout() -> UMG_API void
```

Causes the text to reflow it's layout and re-evaluate any decorators

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

## Language

`cpp`
