---
id: "api:class:UEditableText"
title: "UEditableText"
source: "https://developer.gp.qq.com/api/class/detail/Others/UEditableText.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UEditableText

Editable text box widget

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Text` | `FText` | The text content for this editable text box widget |
| `TextDelegate` | `FGetText` | A bindable delegate to allow logic to drive the text of the widget |
| `HintText` | `FText` | Hint text that appears when there is no text in the text box |
| `HintTextDelegate` | `FGetText` | A bindable delegate to allow logic to drive the hint text of the widget |
| `WidgetStyle` | `FEditableTextStyle` | The style |
| `Style_DEPRECATED` | `USlateWidgetStyleAsset *` | Text style |
| `BackgroundImageSelected_DEPRECATED` | `USlateBrushAsset *` | Background image for the selected text (overrides Style) |
| `BackgroundImageComposing_DEPRECATED` | `USlateBrushAsset *` | Background image for the composing text (overrides Style) |
| `CaretImage_DEPRECATED` | `USlateBrushAsset *` | Image brush used for the caret (overrides Style) |
| `Font_DEPRECATED` | `FSlateFontInfo` | Font color and opacity (overrides Style) |
| `ColorAndOpacity_DEPRECATED` | `FSlateColor` | Text color and opacity (overrides Style) |
| `IsReadOnly` | `bool` | Sets whether this text box can actually be modified interactively by the user |
| `IsPassword` | `bool` | Sets whether this text box is for storing a password |
| `MinimumDesiredWidth` | `float` | Minimum width that a text block should be |
| `IsCaretMovedWhenGainFocus` | `bool` | Workaround as we lose focus when the auto completion closes. |
| `SelectAllTextWhenFocused` | `bool` | Whether to select all text when the user clicks to give focus on the widget |
| `RevertTextOnEscape` | `bool` | Whether to allow the user to back out of changes when they press the escape key |
| `ClearKeyboardFocusOnCommit` | `bool` | Whether to clear keyboard focus when pressing enter to commit changes |
| `SelectAllTextOnCommit` | `bool` | Whether to select all text when pressing enter to commit changes |
| `AllowContextMenu` | `bool` | Whether the context menu can be opened |
| `KeyboardType` | `TEnumAsByte < EVirtualKeyboardType :: Type >` | If we're on a platform that requires a virtual keyboard, what kind of keyboard should this widget use? |
| `ShapedTextOptions` | `FShapedTextOptions` | Controls how the text within this widget should be shaped. |

## Functions

### `GetText`

```text
GetText() -> FText
```

Gets the widget text

**Returns**

| Type | Description |
|---|---|
| `FText` | The widget text |

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

### `SetIsPassword`

```text
SetIsPassword(InbIsPassword: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InbIsPassword` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHintText`

```text
SetHintText(InHintText: FText) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InHintText` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIsReadOnly`

```text
SetIsReadOnly(InbIsReadyOnly: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InbIsReadyOnly` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFont`

```text
SetFont(Font: FSlateFontInfo) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Font` | `FSlateFontInfo` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetColorAndOpacity`

```text
SetColorAndOpacity(Color: FSlateColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Color` | `FSlateColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnTextChanged`

```text
OnTextChanged(Text: const FText&) -> void
```

Called whenever the text is changed interactively by the user

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Text` | `const FText&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTextCommitted`

```text
OnTextCommitted(Text: const FText&, CommitMethod: ETextCommit::Type) -> void
```

Called whenever the text is committed.  This happens when the user presses enter or the text box loses focus.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Text` | `const FText&` | - |
| `CommitMethod` | `ETextCommit::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTextBeginEditTransation`

```text
OnTextBeginEditTransation() -> void
```

Called to begin an undoable editable text transaction

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTextEndEditTransaction`

```text
OnTextEndEditTransaction(Text: const FText&) -> void
```

Called to end an undoable editable text transaction

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Text` | `const FText&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTextFocusReceived`

```text
OnTextFocusReceived() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
