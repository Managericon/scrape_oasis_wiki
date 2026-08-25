---
id: "api:class:UCurveBase"
title: "UCurveBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCurveBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UCurveBase

Defines a curve of interpolated points to evaluate over a given range

## Inheritance

`UObject` -> `FCurveOwnerInterface`

## Functions

### `GetTimeRange`

```text
GetTimeRange(MinTime: float &, MaxTime: float &) -> void
```

Get the time range across all curves

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MinTime` | `float &` | - |
| `MaxTime` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetValueRange`

```text
GetValueRange(MinValue: float &, MaxValue: float &) -> void
```

Get the value range across all curves

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MinValue` | `float &` | - |
| `MaxValue` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
