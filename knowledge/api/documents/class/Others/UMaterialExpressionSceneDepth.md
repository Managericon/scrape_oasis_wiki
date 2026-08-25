---
id: "api:class:UMaterialExpressionSceneDepth"
title: "UMaterialExpressionSceneDepth"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSceneDepth.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialExpressionSceneDepth

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputMode` | `TEnumAsByte < enum EMaterialSceneAttributeInputMode :: Type >` | Coordinates - UV coordinates to apply to the scene depth lookup.<br>	 OffsetFraction - An offset to apply to the scene depth lookup in a 2d fraction of the screen. |
| `Input` | `FExpressionInput` | Based on the input mode the input will be treated as either:<br>	 UV coordinates to apply to the scene depth lookup or <br>	 an offset to apply to the scene depth lookup, in a 2d fraction of the screen. |
| `Coordinates_DEPRECATED` | `FExpressionInput` | - |
| `ConstInput` | `FVector2D` | only used if Input is not hooked up |

## Language

`cpp`
