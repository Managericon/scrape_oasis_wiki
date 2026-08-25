---
id: "api:class:UColorGradientSlider"
title: "UColorGradientSlider"
source: "https://developer.gp.qq.com/api/class/detail/Others/UColorGradientSlider.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UColorGradientSlider

## Inheritance

`UColorGradient`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SliderStyle` | `FSliderStyle` | - |
| `BarFrameNormal` | `FSlateBrush` | - |
| `BarFrameSelect` | `FSlateBrush` | - |
| `DefaultSelectIndex` | `int32` | - |
| `CurSelectIndex` | `int32` | - |

## Functions

### `GetCurSelectIndex`

```text
GetCurSelectIndex() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetCurSelectIndex`

```text
SetCurSelectIndex(Idx: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Idx` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDatas`

```text
SetDatas(datas: TArray < FColorGradientCellInfo > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `datas` | `TArray < FColorGradientCellInfo > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnPercentChanged`

```text
OnPercentChanged(Idx: int32, InPercent: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Idx` | `int32` | - |
| `InPercent` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnChildSelected`

```text
OnChildSelected(Idx: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Idx` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
