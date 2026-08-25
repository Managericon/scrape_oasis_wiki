---
id: "api:class:UMaterialExpressionLandscapeBlendTA"
title: "UMaterialExpressionLandscapeBlendTA"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLandscapeBlendTA.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialExpressionLandscapeBlendTA

## Inheritance

`UMaterialExpressionTerrainBlendBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UV` | `FExpressionInput` | - |
| `DiffuseTexture` | `FExpressionInput` | - |
| `NormalTexture` | `FExpressionInput` | - |
| `HeightTexture` | `FExpressionInput` | - |
| `RoughnessTexture` | `FExpressionInput` | - |
| `Layers` | `TArray < FTerrainLayerTA >` | - |
| `ConstCoordinate` | `uint32` | only used if Coordinates is not hooked up |
| `ExpressionGUID` | `FGuid` | GUID that should be unique within the material, this is used for parameter renaming. |

## Language

`cpp`
