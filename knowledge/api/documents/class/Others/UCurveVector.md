---
id: "api:class:UCurveVector"
title: "UCurveVector"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCurveVector.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UCurveVector

## Inheritance

`UCurveBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FloatCurves` | `FRichCurve` | Keyframe data, one curve for X, Y and Z |

## Functions

### `GetVectorValue`

```text
GetVectorValue(InTime: float) -> ENGINE_API FVector
```

Evaluate this float curve at the specified time

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FVector` | - |

## Language

`cpp`
