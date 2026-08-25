---
id: "api:class:UMaterialExpressionFunctionOutput"
title: "UMaterialExpressionFunctionOutput"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionFunctionOutput.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialExpressionFunctionOutput

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OutputName` | `FString` | The output's name, which will be drawn on the connector in function call expressions that use this function. |
| `Description` | `FString` | The output's description, which will be used as a tooltip on the connector in function call expressions that use this function. |
| `SortPriority` | `int32` | Controls where the output is displayed relative to the other outputs. |
| `A` | `FExpressionInput` | Stores the expression in the material function connected to this output. |
| `bLastPreviewed` | `uint32` | Whether this output was previewed the last time this function was edited. |
| `Id` | `FGuid` | Id of this input, used to maintain references through name changes. |

## Language

`cpp`
