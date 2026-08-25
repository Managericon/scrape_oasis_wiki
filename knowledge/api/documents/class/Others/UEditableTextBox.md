---
id: "api:class:UEditableTextBox"
title: "UEditableTextBox"
source: "https://developer.gp.qq.com/api/class/detail/Others/UEditableTextBox.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UEditableTextBox

Allows the user to type in custom text.  Only permits a single line of text to be entered.
  
   No Children
   Text Entry

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Text` | `FText` | The text content for this editable text box widget |
| `TextDelegate` | `FGetText` | A bindable delegate to allow logic to drive the text of the widget |
| `WidgetStyle` | `FEditableTextBoxStyle` | The style |
| `Style_DEPRECATED` | `USlateWidgetStyleAsset *` | Style used for the text box |
| `HintText` | `FText` | Hint text that appears when there is no text in the text box |
| `HintTextDelegate` | `FGetText` | A bindable delegate to allow logic to drive the hint text of the widget |
| `Font_DEPRECATED` | `FSlateFontInfo` | Font color and opacity (overrides Style) |
| `ForegroundColor_DEPRECATED` | `FLinearColor` | Text color and opacity (overrides Style) |
| `BackgroundColor_DEPRECATED` | `FLinearColor` | The color of the backgroundborder around the editable text (overrides Style) |
| `ReadOnlyForegroundColor_DEPRECATED` | `FLinearColor` | Text color and opacity when read-only (overrides Style) |
| `IsReadOnly` | `bool` | Sets whether this text box can actually be modified interactively by the user |
| `IsPassword` | `bool` | Sets whether this text box is for storing a password |
| `MinimumDesiredWidth` | `float` | Minimum width that a text block should be |
| `Padding_DEPRECATED` | `FMargin` | Padding between the boxborder and the text widget inside (overrides Style) |
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

Provide a alternative mechanism for error reporting.

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `SetText`

```text
SetText(InText: FText) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHintText`

```text
SetHintText(InText: FText) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetError`

```text
SetError(InError: FText) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InError` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIsReadOnly`

```text
SetIsReadOnly(bReadOnly: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bReadOnly` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearError`

```text
ClearError() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HasError`

```text
HasError() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

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

## Language

`cpp`
