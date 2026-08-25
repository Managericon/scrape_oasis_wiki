---
id: "api:class:UMaterialExpressionTextureSampleParameter"
title: "UMaterialExpressionTextureSampleParameter"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTextureSampleParameter.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialExpressionTextureSampleParameter

## Inheritance

`UMaterialExpressionTextureSample`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `ExpressionGUID` | `FGuid` | GUID that should be unique within the material, this is used for parameter renaming. |
| `Group` | `FName` | The name of the parameter Group to display in MaterialInstance Editor. Default is None group |
| `SortPriority` | `int32` | Controls where the this parameter is displayed in a material instance parameter list.  The lower the number the higher up in the parameter list. |

## Language

`cpp`
