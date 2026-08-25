---
id: "api:class:UInputKeySelector"
title: "UInputKeySelector"
source: "https://developer.gp.qq.com/api/class/detail/Others/UInputKeySelector.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UInputKeySelector

A widget for selecting a single key or a single key with a modifier.

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WidgetStyle` | `FButtonStyle` | The button style used at runtime |
| `TextStyle` | `FTextBlockStyle` | The button style used at runtime |
| `SelectedKey` | `FInputChord` | The currently selected key chord. |
| `Font_DEPRECATED` | `FSlateFontInfo` | - |
| `Margin` | `FMargin` | The amount of blank space around the text used to display the currently selected key. |
| `ColorAndOpacity_DEPRECATED` | `FLinearColor` | - |
| `KeySelectionText` | `FText` | Sets the text which is displayed while selecting keys. |
| `NoKeySpecifiedText` | `FText` | Sets the text to display when no key text is available or not selecting a key. |
| `bAllowModifierKeys` | `bool` | When true modifier keys such as control and alt are allowed in the <br>	 input chord representing the selected key, if false modifier keys are ignored. |
| `bAllowGamepadKeys` | `bool` | When true gamepad keys are allowed in the input chord representing the selected key, otherwise they are ignored. |
| `EscapeKeys` | `TArray < FKey >` | When true gamepad keys are allowed in the input chord representing the selected key, otherwise they are ignored. |

## Functions

### `SetSelectedKey`

```text
SetSelectedKey(InSelectedKey: FInputChord &) -> void
```

Sets the currently selected key.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSelectedKey` | `FInputChord &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetKeySelectionText`

```text
SetKeySelectionText(InKeySelectionText: FText) -> void
```

Sets the text which is displayed while selecting keys.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InKeySelectionText` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNoKeySpecifiedText`

```text
SetNoKeySpecifiedText(InNoKeySpecifiedText: FText) -> void
```

Sets the text to display when no key text is available or not selecting a key.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNoKeySpecifiedText` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAllowModifierKeys`

```text
SetAllowModifierKeys(bInAllowModifierKeys: bool) -> void
```

Sets whether or not modifier keys are allowed in the selected key.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInAllowModifierKeys` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAllowGamepadKeys`

```text
SetAllowGamepadKeys(bInAllowGamepadKeys: bool) -> void
```

Sets whether or not gamepad keys are allowed in the selected key.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInAllowGamepadKeys` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetIsSelectingKey`

```text
GetIsSelectingKey() -> bool
```

Returns true if the widget is currently selecting a key, otherwise returns false.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetTextBlockVisibility`

```text
SetTextBlockVisibility(InVisibility: ESlateVisibility) -> void
```

Sets the visibility of the text block.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVisibility` | `ESlateVisibility` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnKeySelected`

```text
OnKeySelected(SelectedKey: FInputChord) -> void
```

Called whenever a new key is selected by the user.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelectedKey` | `FInputChord` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnIsSelectingKeyChanged`

```text
OnIsSelectingKeyChanged() -> void
```

Called whenever the key selection mode starts or stops.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
