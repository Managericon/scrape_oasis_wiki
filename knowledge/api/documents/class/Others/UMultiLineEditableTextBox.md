---
id: "api:class:UMultiLineEditableTextBox"
title: "UMultiLineEditableTextBox"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMultiLineEditableTextBox.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMultiLineEditableTextBox

Allows a user to enter multiple lines of text

## Inheritance

`UTextLayoutWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Text` | `FText` | The text content for this editable text box widget |
| `HintText` | `FText` | Hint text that appears when there is no text in the text box |
| `HintTextDelegate` | `FGetText` | A bindable delegate to allow logic to drive the hint text of the widget |
| `WidgetStyle` | `FEditableTextBoxStyle` | The style |
| `TextStyle` | `FTextBlockStyle` | The text style |
| `bIsReadOnly` | `bool` | Sets whether this text block can be modified interactively by the user |
| `AllowContextMenu` | `bool` | Whether the context menu can be opened |
| `Style_DEPRECATED` | `USlateWidgetStyleAsset *` | - |
| `Font_DEPRECATED` | `FSlateFontInfo` | Font color and opacity (overrides Style) |
| `ForegroundColor_DEPRECATED` | `FLinearColor` | Text color and opacity (overrides Style) |
| `BackgroundColor_DEPRECATED` | `FLinearColor` | The color of the backgroundborder around the editable text (overrides Style) |
| `ReadOnlyForegroundColor_DEPRECATED` | `FLinearColor` | Text color and opacity when read-only (overrides Style) |

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

### `SetIsEnableMultiLineTextInsertNewLine`

```text
SetIsEnableMultiLineTextInsertNewLine(bEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

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

## Language

`cpp`
