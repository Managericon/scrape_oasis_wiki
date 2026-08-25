---
id: "api:class:UMaterialExpressionLandscapeMaterialIdSample"
title: "UMaterialExpressionLandscapeMaterialIdSample"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLandscapeMaterialIdSample.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialExpressionLandscapeMaterialIdSample

## Inheritance

`UMaterialExpressionTextureSample`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DiffuseSamplerType` | `TEnumAsByte < enum EMaterialSamplerType >` | - |
| `NormalSamplerType` | `TEnumAsByte < enum EMaterialSamplerType >` | - |
| `bUseTextureTransform` | `bool` | If apply rotationscaling separately when sample diffusenormal texture array. |
| `bUseDeltaForceHeightBlend` | `bool` | - |
| `bUseLargeWeight` | `bool` | - |
| `LargeWeight` | `float` | - |
| `bSkipNormalLowQuality` | `bool` | - |
| `bUseFarUV` | `bool` | - |
| `DeltaForceHeightBlendFactorInput` | `FExpressionInput` | - |
| `FarUVFactorInput` | `FExpressionInput` | - |
| `bUseApplyNoiseLow` | `bool` | - |
| `bUseApplyNoiseHigh` | `bool` | - |
| `bUseApplyNoiseMedium` | `bool` | - |
| `bUseApplyNoiseUltimateHigh` | `bool` | - |
| `bUseOneTextureInsteadFar` | `bool` | - |
| `bHasHole` | `bool` | - |
| `bUseLayerDensity` | `bool` | - |
| `bDebugES2` | `bool` | - |
| `bDebugBlend4Pixels` | `bool` | - |
| `ExpressionGUID` | `FGuid` | GUID that should be unique within the material, this is used for parameter renaming. |
| `NumParentInputs` | `int32` | Number of inputs from parent class |

## Language

`cpp`
