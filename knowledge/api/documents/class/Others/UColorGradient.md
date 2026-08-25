---
id: "api:class:UColorGradient"
title: "UColorGradient"
source: "https://developer.gp.qq.com/api/class/detail/Others/UColorGradient.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UColorGradient

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ColorRGBs` | `TArray < FColorGradientCellInfo >` | - |

## Functions

### `GetNum`

```text
GetNum() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetCellByIndex`

```text
GetCellByIndex(Idx: int, OutPercent: float &, OutColorRGB: FLinearColor &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Idx` | `int` | - |
| `OutPercent` | `float &` | - |
| `OutColorRGB` | `FLinearColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `FindIndexByPercent`

```text
FindIndexByPercent(InPercent: float) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPercent` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

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

### `ColorRGBsDelegate`

```text
ColorRGBsDelegate() -> TArray<FColorGradientCellInfo>
```

**Returns**

| Type | Description |
|---|---|
| `TArray` | - |

## Language

`cpp`
