---
id: "api:class:UMaterialExpressionParameter"
title: "UMaterialExpressionParameter"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionParameter.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialExpressionParameter

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | The name of the parameter |
| `bCanCollectedForCustomData` | `bool` | - |
| `CustomDataIndex` | `int32` | - |
| `ExpressionGUID` | `FGuid` | GUID that should be unique within the material, this is used for parameter renaming. |
| `Group` | `FName` | The name of the parameter Group to display in MaterialInstance Editor. Default is None group |
| `SortPriority` | `int32` | Controls where the this parameter is displayed in a material instance parameter list.  The lower the number the higher up in the parameter list. |

## Language

`cpp`
