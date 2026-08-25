---
id: "api:class:UColorSlider"
title: "UColorSlider"
source: "https://developer.gp.qq.com/api/class/detail/Others/UColorSlider.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UColorSlider

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ColorHSVDelegate` | `FGetLinearColor` | - |
| `SliderHandleColorDelegate` | `FGetLinearColor` | - |
| `bUseHandleColorOrCurrentColor` | `bool` | - |
| `ColorHSV` | `FLinearColor` | - |
| `SliderHandleColor` | `FLinearColor` | - |
| `Channel` | `EColorSliderChannels` | - |
| `SliderStyle` | `FSliderStyle` | - |
| `SliderBarFrame` | `FSlateBrush` | - |

## Functions

### `GetColor`

```text
GetColor() -> FLinearColor
```

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `SetColor`

```text
SetColor(InColorHSV: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColorHSV` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSliderHandleColor`

```text
SetSliderHandleColor(InSliderHandleColor: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSliderHandleColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetColorSliderChannels`

```text
GetColorSliderChannels() -> EColorSliderChannels
```

**Returns**

| Type | Description |
|---|---|
| `EColorSliderChannels` | - |

### `SetColorSliderChannels`

```text
SetColorSliderChannels(InChannel: EColorSliderChannels) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InChannel` | `EColorSliderChannels` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetUseHandleColorOrCurrentColor`

```text
SetUseHandleColorOrCurrentColor(bUse: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bUse` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnInteractiveChangeBegin`

```text
OnInteractiveChangeBegin() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInteractiveChangeEnd`

```text
OnInteractiveChangeEnd() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnValueChanged`

```text
OnValueChanged(InValue: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
