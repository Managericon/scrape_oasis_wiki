---
id: "api:class:UMaterialExpressionTextureCoordinate"
title: "UMaterialExpressionTextureCoordinate"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTextureCoordinate.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialExpressionTextureCoordinate

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CoordinateIndex` | `int32` | Texture coordinate index |
| `UTiling` | `float` | Controls how much the texture tiles horizontally, by scaling the U component of the vertex UVs by the specified amount. |
| `VTiling` | `float` | Controls how much the texture tiles vertically, by scaling the V component of the vertex UVs by the specified amount. |
| `UnMirrorU` | `uint32` | Would like to unmirror U or V <br>	   - if the texture is mirrored and if you would like to undo mirroring for this texture sample, use this to unmirror |
| `UnMirrorV` | `uint32` | - |

## Language

`cpp`
