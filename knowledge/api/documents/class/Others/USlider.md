---
id: "api:class:USlider"
title: "USlider"
source: "https://developer.gp.qq.com/api/class/detail/Others/USlider.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# USlider

A simple widget that shows a sliding bar with a handle that allows you to control the value between 0..1.
 
   No Children

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `float` | The volume value to display. |
| `ValueDelegate` | `FGetFloat` | A bindable delegate to allow logic to drive the value of the widget |
| `WidgetStyle` | `FSliderStyle` | The progress bar style |
| `Orientation` | `TEnumAsByte < EOrientation >` | The slider's orientation. |
| `SliderBarColor` | `FLinearColor` | The color to draw the slider bar in. |
| `SliderHandleColor` | `FLinearColor` | The color to draw the slider handle in. |
| `IndentHandle` | `bool` | Whether the slidable area should be indented to fit the handle. |
| `Locked` | `bool` | Whether the handle is interactive or fixed. |
| `StepSize` | `float` | The amount to adjust the value by, when using a controller or keyboard |
| `IsFocusable` | `bool` | Should the slider be focusable? |
| `SupportClickChange` | `bool` | - |

## Functions

### `GetValue`

```text
GetValue() -> float
```

Gets the current value of the slider.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetValue`

```text
SetValue(InValue: float) -> void
```

Sets the current value of the slider.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIndentHandle`

```text
SetIndentHandle(InValue: bool) -> void
```

Sets if the slidable area should be indented to fit the handle

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLocked`

```text
SetLocked(InValue: bool) -> void
```

Sets the handle to be interactive or fixed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetStepSize`

```text
SetStepSize(InValue: float) -> void
```

Sets the amount to adjust the value by, when using a controller or keyboard

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSliderBarColor`

```text
SetSliderBarColor(InValue: FLinearColor) -> void
```

Sets the color of the slider bar

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSliderHandleColor`

```text
SetSliderHandleColor(InValue: FLinearColor) -> void
```

Sets the color of the handle bar

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnMouseCaptureBegin`

```text
OnMouseCaptureBegin() -> void
```

Invoked when the mouse is pressed and a capture begins.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMouseCaptureEnd`

```text
OnMouseCaptureEnd() -> void
```

Invoked when the mouse is released and a capture ends.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnControllerCaptureBegin`

```text
OnControllerCaptureBegin() -> void
```

Invoked when the controller capture begins.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnControllerCaptureEnd`

```text
OnControllerCaptureEnd() -> void
```

Invoked when the controller capture ends.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnValueChanged`

```text
OnValueChanged(Value: float) -> void
```

Called when the value is changed by slider or typing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
