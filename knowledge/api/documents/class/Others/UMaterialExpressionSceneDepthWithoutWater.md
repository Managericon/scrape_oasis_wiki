---
id: "api:class:UMaterialExpressionSceneDepthWithoutWater"
title: "UMaterialExpressionSceneDepthWithoutWater"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSceneDepthWithoutWater.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialExpressionSceneDepthWithoutWater

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputMode` | `TEnumAsByte < enum EMaterialSceneAttributeInputMode :: Type >` | Coordinates - UV coordinates to apply to the scene depth lookup.<br>	 OffsetFraction - An offset to apply to the scene depth lookup in a 2d fraction of the screen. |
| `Input` | `FExpressionInput` | Based on the input mode the input will be treated as either:<br>	 UV coordinates to apply to the scene depth lookup or<br>	 an offset to apply to the scene depth lookup, in a 2d fraction of the screen. |
| `ConstInput` | `FVector2D` | only used if Input is not hooked up |
| `FallbackDepth` | `float` | Depth to fall back to in case the needed texture isn't available on a particular platform or configuration |

## Language

`cpp`
