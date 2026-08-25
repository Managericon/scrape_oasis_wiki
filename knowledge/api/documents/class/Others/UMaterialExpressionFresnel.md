---
id: "api:class:UMaterialExpressionFresnel"
title: "UMaterialExpressionFresnel"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionFresnel.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialExpressionFresnel

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ExponentIn` | `FExpressionInput` | - |
| `Exponent` | `float` | The exponent to pass into the pow() function |
| `BaseReflectFractionIn` | `FExpressionInput` | - |
| `BaseReflectFraction` | `float` | Specifies the fraction of specular reflection when the surfaces is viewed from straight on.<br>	  A value of 1 effectively disables Fresnel. |
| `Normal` | `FExpressionInput` | The normal to dot with the camera FVector |

## Language

`cpp`
