---
id: "api:class:UAIDataProvider_QueryParams"
title: "UAIDataProvider_QueryParams"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAIDataProvider_QueryParams.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAIDataProvider_QueryParams

AIDataProvider_QueryParams is used with environment queries
 
  It allows defining simple parameters for running query,
  which are not tied to any specific pawn, but defined
  for every query execution.

## Inheritance

`UAIDataProvider`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParamName` | `FName` | Arbitrary name this query parameter will be exposed as to outside world (like BT nodes) |
| `FloatValue` | `float` | - |
| `IntValue` | `int32` | - |
| `BoolValue` | `bool` | - |

## Language

`cpp`
