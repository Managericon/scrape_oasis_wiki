---
id: "api:class:UColorPicker"
title: "UColorPicker"
source: "https://developer.gp.qq.com/api/class/detail/Others/UColorPicker.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UColorPicker

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ColorHSV` | `FLinearColor` | - |
| `ColorHSVDelegate` | `FGetLinearColor` | - |
| `Brush` | `FSlateBrush` | - |

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

### `HandleHexSRGBBoxText`

```text
HandleHexSRGBBoxText() -> FString
```

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `HandleHexLinearString`

```text
HandleHexLinearString() -> FString
```

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

## Delegates

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

### `OnMouseCaptureBegin`

```text
OnMouseCaptureBegin() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMouseCaptureEnd`

```text
OnMouseCaptureEnd() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
