---
id: "api:class:UMaterialExpressionReflectionVectorWS"
title: "UMaterialExpressionReflectionVectorWS"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionReflectionVectorWS.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialExpressionReflectionVectorWS

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CustomWorldNormal` | `FExpressionInput` | Optional world normal to reflect the camera view vector about. If unconnected, pixel normal is used |
| `bNormalizeCustomWorldNormal` | `uint32` | (true): The specified world normal will be normalized. (false): WorldNormal will just be used as is, faster but possible artifacts if normal length isn't 1 |

## Language

`cpp`
