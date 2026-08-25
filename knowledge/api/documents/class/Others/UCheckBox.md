---
id: "api:class:UCheckBox"
title: "UCheckBox"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCheckBox.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UCheckBox

The checkbox widget allows you to display a toggled state of 'unchecked', 'checked' and 
  'indeterminable.  You can use the checkbox for a classic checkbox, or as a toggle button,
  or as radio buttons.
  
   Single Child
   Toggle

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CheckedState` | `ECheckBoxState` | Whether the check box is currently in a checked state |
| `CheckedStateDelegate` | `FGetCheckBoxState` | A bindable delegate for the IsChecked. |
| `WidgetStyle` | `FCheckBoxStyle` | The checkbox bar style |
| `Style_DEPRECATED` | `USlateWidgetStyleAsset *` | Style of the check box |
| `UncheckedImage_DEPRECATED` | `USlateBrushAsset *` | Image to use when the checkbox is unchecked |
| `UncheckedHoveredImage_DEPRECATED` | `USlateBrushAsset *` | Image to use when the checkbox is unchecked and hovered |
| `UncheckedPressedImage_DEPRECATED` | `USlateBrushAsset *` | Image to use when the checkbox is unchecked and pressed |
| `CheckedImage_DEPRECATED` | `USlateBrushAsset *` | Image to use when the checkbox is checked |
| `CheckedHoveredImage_DEPRECATED` | `USlateBrushAsset *` | Image to use when the checkbox is checked and hovered |
| `CheckedPressedImage_DEPRECATED` | `USlateBrushAsset *` | Image to use when the checkbox is checked and pressed |
| `UndeterminedImage_DEPRECATED` | `USlateBrushAsset *` | Image to use when the checkbox is in an ambiguous state and hovered |
| `UndeterminedHoveredImage_DEPRECATED` | `USlateBrushAsset *` | Image to use when the checkbox is checked and hovered |
| `UndeterminedPressedImage_DEPRECATED` | `USlateBrushAsset *` | Image to use when the checkbox is in an ambiguous state and pressed |
| `HorizontalAlignment` | `TEnumAsByte < EHorizontalAlignment >` | How the content of the toggle button should align within the given space |
| `Padding_DEPRECATED` | `FMargin` | Spacing between the check box image and its content |
| `BorderBackgroundColor_DEPRECATED` | `FSlateColor` | The color of the background border |
| `IsFocusable` | `bool` | Sometimes a button should only be mouse-clickable and never keyboard focusable. |
| `ClickMethod` | `TEnumAsByte < EButtonClickMethod :: Type >` | The type of mouse action required by the user to trigger the buttons 'Click' |
| `TouchMethod` | `TEnumAsByte < EButtonTouchMethod :: Type >` | The type of touch action required by the user to trigger the buttons 'Click' |

## Functions

### `IsPressed`

```text
IsPressed() -> bool
```

Returns true if this button is currently pressed

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsChecked`

```text
IsChecked() -> bool
```

Returns true if the checkbox is currently checked

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetCheckedState`

```text
GetCheckedState() -> ECheckBoxState
```

**Returns**

| Type | Description |
|---|---|
| `ECheckBoxState` | the full current checked state. |

### `SetIsChecked`

```text
SetIsChecked(InIsChecked: bool) -> void
```

Sets the checked state.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIsChecked` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCheckedState`

```text
SetCheckedState(InCheckedState: ECheckBoxState) -> void
```

Sets the checked state.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCheckedState` | `ECheckBoxState` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetClickMethod`

```text
SetClickMethod(InClickMethod: EButtonClickMethod :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InClickMethod` | `EButtonClickMethod :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTouchMethod`

```text
SetTouchMethod(InTouchMethod: EButtonTouchMethod :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTouchMethod` | `EButtonTouchMethod :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnCheckStateChanged`

```text
OnCheckStateChanged(bIsChecked: bool) -> void
```

Called when the checked state has changed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsChecked` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
