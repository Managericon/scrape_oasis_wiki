---
id: "api:class:USpinBox"
title: "USpinBox"
source: "https://developer.gp.qq.com/api/class/detail/Others/USpinBox.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# USpinBox

A numerical entry box that allows for direct entry of the number or allows the user to click and slide the number.

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `float` | Value stored in this spin box |
| `ValueDelegate` | `FGetFloat` | A bindable delegate to allow logic to drive the value of the widget |
| `WidgetStyle` | `FSpinBoxStyle` | The Style |
| `Style_DEPRECATED` | `USlateWidgetStyleAsset *` | - |
| `Delta` | `float` | The amount by which to change the spin box value as the slider moves. |
| `SliderExponent` | `float` | The exponent by which to increase the delta as the mouse moves. 1 is constant (never increases the delta). |
| `Font` | `FSlateFontInfo` | Font color and opacity (overrides style) |
| `Justification` | `TEnumAsByte < ETextJustify :: Type >` | The justification the value text should appear as. |
| `MinDesiredWidth` | `float` | The minimum width of the spin box |
| `ClearKeyboardFocusOnCommit` | `bool` | Whether to remove the keyboard focus from the spin box when the value is committed |
| `SelectAllTextOnCommit` | `bool` | Whether to select the text in the spin box when the value is committed |
| `ForegroundColor` | `FSlateColor` | - |
| `bOverride_MinValue` | `uint32` | Whether the optional MinValue attribute of the widget is set |
| `bOverride_MaxValue` | `uint32` | Whether the optional MaxValue attribute of the widget is set |
| `bOverride_MinSliderValue` | `uint32` | Whether the optional MinSliderValue attribute of the widget is set |
| `bOverride_MaxSliderValue` | `uint32` | Whether the optional MaxSliderValue attribute of the widget is set |
| `MinValue` | `float` | The minimum allowable value that can be manually entered into the spin box |
| `MaxValue` | `float` | The maximum allowable value that can be manually entered into the spin box |
| `MinSliderValue` | `float` | The minimum allowable value that can be specified using the slider |
| `MaxSliderValue` | `float` | The maximum allowable value that can be specified using the slider |

## Functions

### `GetValue`

```text
GetValue() -> float
```

Get the current value of the spin box.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetValue`

```text
SetValue(NewValue: float) -> void
```

Set the value of the spin box.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMinValue`

```text
GetMinValue() -> float
```

Get the current minimum value that can be manually set in the spin box.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetMinValue`

```text
SetMinValue(NewValue: float) -> void
```

Set the minimum value that can be manually set in the spin box.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMinValue`

```text
ClearMinValue() -> void
```

Clear the minimum value that can be manually set in the spin box.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMaxValue`

```text
GetMaxValue() -> float
```

Get the current maximum value that can be manually set in the spin box.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetMaxValue`

```text
SetMaxValue(NewValue: float) -> void
```

Set the maximum value that can be manually set in the spin box.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMaxValue`

```text
ClearMaxValue() -> void
```

Clear the maximum value that can be manually set in the spin box.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMinSliderValue`

```text
GetMinSliderValue() -> float
```

Get the current minimum value that can be specified using the slider.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetMinSliderValue`

```text
SetMinSliderValue(NewValue: float) -> void
```

Set the minimum value that can be specified using the slider.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMinSliderValue`

```text
ClearMinSliderValue() -> void
```

Clear the minimum value that can be specified using the slider.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMaxSliderValue`

```text
GetMaxSliderValue() -> float
```

Get the current maximum value that can be specified using the slider.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetMaxSliderValue`

```text
SetMaxSliderValue(NewValue: float) -> void
```

Set the maximum value that can be specified using the slider.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMaxSliderValue`

```text
ClearMaxSliderValue() -> void
```

Clear the maximum value that can be specified using the slider.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetForegroundColor`

```text
SetForegroundColor(InForegroundColor: FSlateColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InForegroundColor` | `FSlateColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnValueChanged`

```text
OnValueChanged(InValue: float) -> void
```

Called when the value is changed interactively by the user

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnValueCommitted`

```text
OnValueCommitted(InValue: float, CommitMethod: ETextCommit::Type) -> void
```

Called when the value is committed. Occurs when the user presses Enter or the text box loses focus.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `float` | - |
| `CommitMethod` | `ETextCommit::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnBeginSliderMovement`

```text
OnBeginSliderMovement() -> void
```

Called right before the slider begins to move

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnEndSliderMovement`

```text
OnEndSliderMovement(InValue: float) -> void
```

Called right after the slider handle is released by the user

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
