---
id: "api:class:UMaterialExpressionLandscapeLayerCoords"
title: "UMaterialExpressionLandscapeLayerCoords"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLandscapeLayerCoords.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialExpressionLandscapeLayerCoords

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MappingType` | `TEnumAsByte < enum ETerrainCoordMappingType >` | Determines the mapping place to use on the terrain. |
| `CustomUVType` | `TEnumAsByte < enum ELandscapeCustomizedCoordType >` | Determines the mapping place to use on the terrain. |
| `MappingScaleOverride` | `FExpressionInput` | - |
| `MappingScale` | `float` | Uniform scale to apply to the mapping. |
| `MappingRotation` | `float` | Rotation to apply to the mapping. |
| `MappingPanU` | `float` | Offset to apply to the mapping along U. |
| `MappingPanV` | `float` | Offset to apply to the mapping along V. |

## Language

`cpp`
