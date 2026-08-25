---
id: "api:class:UMaterialExpressionMaterialFunctionCall"
title: "UMaterialExpressionMaterialFunctionCall"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionMaterialFunctionCall.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialExpressionMaterialFunctionCall

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaterialFunction` | `UMaterialFunction *` | The function to call. |
| `FunctionInputs` | `TArray < struct FFunctionExpressionInput >` | Array of all the function inputs that this function exposes. |
| `FunctionOutputs` | `TArray < struct FFunctionExpressionOutput >` | Array of all the function outputs that this function exposes. |

## Functions

### `SetMaterialFunction`

```text
SetMaterialFunction(NewMaterialFunction: UMaterialFunction *) -> ENGINE_API bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewMaterialFunction` | `UMaterialFunction *` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API bool` | - |

## Language

`cpp`
