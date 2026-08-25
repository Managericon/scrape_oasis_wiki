---
id: "api:class:UMaterialExpressionSceneTexture"
title: "UMaterialExpressionSceneTexture"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSceneTexture.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialExpressionSceneTexture

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Coordinates` | `FExpressionInput` | UV in 0..1 range |
| `SceneTextureId` | `TEnumAsByte < ESceneTextureId >` | Which scene texture (screen aligned texture) we want to make a lookup into |
| `bClampUVs` | `bool` | Clamps texture coordinates to the range 0 to 1. Incurs a performance cost. |
| `bFiltered` | `bool` | Whether to use point sampled texture lookup (default) or using [bi-linear] filtered (can be slower, avoid faceted lock with distortions), some SceneTextures cannot be filtered |

## Language

`cpp`
