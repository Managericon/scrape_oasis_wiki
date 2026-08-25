---
id: "api:class:ULandscapeMaterialIdLayerInfoObject"
title: "ULandscapeMaterialIdLayerInfoObject"
source: "https://developer.gp.qq.com/api/class/detail/Others/ULandscapeMaterialIdLayerInfoObject.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ULandscapeMaterialIdLayerInfoObject

## Inheritance

`ULandscapeLayerInfoObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BiomesOwner` | `ULandscapeBiomesInfoObject *` | Owner Biomes of this LayerInfoObject. Do not modify this Owner unless necessary. |
| `DisplayName` | `FName` | - |
| `LayerIndex` | `int32` | Layer index of this layer info object, can be re-ordered. |
| `DiffuseTexture` | `UTexture2D *` | Diffuse Texture |
| `NormalmapTexture` | `UTexture2D *` | Normalmap Texture |
| `TextureRotation` | `float` | Rotation (in degree) applied when sampling diffusenormal texture |
| `TextureTiling` | `FVector2D` | Scaling applied when sampling diffusenormal texture |
| `TextureTilingFar` | `FVector2D` | - |
| `TextureTilingFarScale` | `FVector2D` | - |
| `TextureFarUVParam` | `FVector2D` | - |
| `HeightBlendThresholdSoftness` | `float` | ThresholdSoftness adjusts how sharp the edges of the height blend will be. The greater the value is, the softer the edge would be. |
| `HeightContrast` | `float` | HeightContrast adjust sampled height value's contrast. |
| `DeltaForceHeightBlendSharpness` | `float` | - |
| `DisplacementLocalBias` | `float` | Convert displacement from texture space to world space, unit is meter. |
| `DisplacementIntensity` | `float` | Scalar applied to displacement, applied after LocalBias is applied. |

## Language

`cpp`
