---
id: "api:class:UMaterialExpressionDepthFade"
title: "UMaterialExpressionDepthFade"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionDepthFade.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialExpressionDepthFade

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InOpacity` | `FExpressionInput` | Input opacity which will be scaled by the result of the fade. |
| `FadeDistance` | `FExpressionInput` | World space distance over which the fade should take place. |
| `OpacityDefault` | `float` | Opacity which will be scaled by the result of the fade.  This is used when InOpacity is unconnected. |
| `FadeDistanceDefault` | `float` | World space distance over which the fade should take place.  This is used when FadeDistance is unconnected. |
| `bSupportFPR` | `bool` | - |
| `bClampSceneDepth` | `bool` | - |

## Language

`cpp`
