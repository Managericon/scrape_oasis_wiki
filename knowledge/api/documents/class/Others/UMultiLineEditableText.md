---
id: "api:class:UMultiLineEditableText"
title: "UMultiLineEditableText"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMultiLineEditableText.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMultiLineEditableText

Editable text box widget

## Inheritance

`UTextLayoutWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Text` | `FText` | The text content for this editable text box widget |
| `HintText` | `FText` | Hint text that appears when there is no text in the text box |
| `HintTextDelegate` | `FGetText` | A bindable delegate to allow logic to drive the hint text of the widget |
| `WidgetStyle` | `FTextBlockStyle` | The style |
| `bIsReadOnly` | `bool` | Sets whether this text block can be modified interactively by the user |
| `Font_DEPRECATED` | `FSlateFontInfo` | Font color and opacity (overrides Style) |
| `AllowContextMenu` | `bool` | Whether the context menu can be opened |
| `UseModiferKeyForNewLine` | `bool` | - |

## Functions

### `GetText`

```text
GetText() -> FText
```

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

### `SetWidgetStyle`

```text
SetWidgetStyle(InWidgetStyle: FTextBlockStyle &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InWidgetStyle` | `FTextBlockStyle &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetModiferKeyForNewLine`

```text
SetModiferKeyForNewLine(bReadOnly: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bReadOnly` | `bool` | - |

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

### `SetFont`

```text
SetFont(InFontInfo: FSlateFontInfo) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFontInfo` | `FSlateFontInfo` | - |

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

Called when editable text received focus

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
