---
id: "api-chunk:class:6"
title: "Oasis API class chunk 6"
source: "https://developer.gp.qq.com/api/"
category: "API Wiki/class"
kind: "api_chunk"
---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionNoise.json -->

# UMaterialExpressionNoise

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Position` | `FExpressionInput` | 2 to 3 dimensional vector |
| `FilterWidth` | `FExpressionInput` | scalar, to clamp the Levels at pixel level, can be computed like this: max(length(ddx(Position)), length(ddy(Position)) |
| `Scale` | `float` | can also be done with a multiply on the Position |
| `Quality` | `int32` | Lower numbers are faster and lower quality, higher numbers are slower and higher quality |
| `NoiseFunction` | `TEnumAsByte < enum ENoiseFunction >` | Noise function, affects performance and look |
| `bTurbulence` | `uint32` | How multiple frequencies are getting combined |
| `Levels` | `int32` | 1 = fast but little detail, .. larger numbers cost more performance |
| `OutputMin` | `float` | - |
| `OutputMax` | `float` | - |
| `LevelScale` | `float` | usually 2 but higher values allow efficient use of few levels |
| `bTiling` | `uint32` | Whether to use tiling noise pattern, useful for baking to seam-free repeating textures |
| `RepeatSize` | `uint32` | How many units in each tile (if Tiling is on) |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionNormalize.json -->

# UMaterialExpressionNormalize

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VectorInput` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionOneMinus.json -->

# UMaterialExpressionOneMinus

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionPanner.json -->

# UMaterialExpressionPanner

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Coordinate` | `FExpressionInput` | - |
| `Time` | `FExpressionInput` | - |
| `Speed` | `FExpressionInput` | - |
| `SpeedX` | `float` | - |
| `SpeedY` | `float` | - |
| `ConstCoordinate` | `uint32` | only used if Coordinate is not hooked up |
| `bFractionalPart` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionParameter.json -->

# UMaterialExpressionParameter

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | The name of the parameter |
| `bCanCollectedForCustomData` | `bool` | - |
| `CustomDataIndex` | `int32` | - |
| `ExpressionGUID` | `FGuid` | GUID that should be unique within the material, this is used for parameter renaming. |
| `Group` | `FName` | The name of the parameter Group to display in MaterialInstance Editor. Default is None group |
| `SortPriority` | `int32` | Controls where the this parameter is displayed in a material instance parameter list.  The lower the number the higher up in the parameter list. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionParticleSubUV.json -->

# UMaterialExpressionParticleSubUV

## Inheritance

`UMaterialExpressionTextureSample`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bBlend` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionPerInstanceCustomData.json -->

# UMaterialExpressionPerInstanceCustomData

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultValue` | `FExpressionInput` | - |
| `ConstDefaultValue` | `FVector4` | - |
| `DataIndex` | `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionPower.json -->

# UMaterialExpressionPower

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Base` | `FExpressionInput` | - |
| `Exponent` | `FExpressionInput` | - |
| `ConstExponent` | `float` | only used if Exponent is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionPreviousFrameSwitch.json -->

# UMaterialExpressionPreviousFrameSwitch

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CurrentFrame` | `FExpressionInput` | - |
| `PreviousFrame` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionPSCustomData.json -->

# UMaterialExpressionPSCustomData

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultValue` | `FExpressionInput` | - |
| `ConstDefaultValue` | `float` | - |
| `DataIndex` | `uint32` | - |
| `IsScalar` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionQualitySwitch.json -->

# UMaterialExpressionQualitySwitch

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Default` | `FExpressionInput` | Default connection, used when a specific quality level input is missing. |
| `Inputs` | `FExpressionInput` | - |
| `SerializationVersion` | `int32` | Only used during serialization. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionReflectionVectorWS.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionReroute.json -->

# UMaterialExpressionReroute

## Inheritance

`UMaterialExpressionRerouteBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | Link to the input expression to be evaluated |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionRotateAboutAxis.json -->

# UMaterialExpressionRotateAboutAxis

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NormalizedRotationAxis` | `FExpressionInput` | - |
| `RotationAngle` | `FExpressionInput` | - |
| `PivotPoint` | `FExpressionInput` | - |
| `Position` | `FExpressionInput` | - |
| `Period` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionRotator.json -->

# UMaterialExpressionRotator

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Coordinate` | `FExpressionInput` | - |
| `Time` | `FExpressionInput` | - |
| `CenterX` | `float` | - |
| `CenterY` | `float` | - |
| `Speed` | `float` | - |
| `ConstCoordinate` | `uint32` | only used if Coordinate is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionRound.json -->

# UMaterialExpressionRound

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionRuntimeVirtualTextureOutput.json -->

# UMaterialExpressionRuntimeVirtualTextureOutput

Material output expression for writing to a runtime virtual texture.

## Inheritance

`UMaterialExpressionCustomOutput`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BaseColor` | `FExpressionInput` | Input for Base Color to output to virtual texture. |
| `Specular` | `FExpressionInput` | Input for Specular to output to virtual texture. |
| `Roughness` | `FExpressionInput` | Input for Roughness to output to virtual texture. |
| `Normal` | `FExpressionInput` | Input for Surface Normal to output to virtual texture. |
| `WorldHeight` | `FExpressionInput` | Input for World Height to output to virtual texture. |
| `Opacity` | `FExpressionInput` | Input for Opacity value used for blending to virtual texture. |
| `Mask` | `FExpressionInput` | Input for Mask to output to virtual texture. |
| `Displacement` | `FExpressionInput` | Input for World Height to output to virtual texture. |
| `Mask4` | `FExpressionInput` | Input for Mask to output to virtual texture. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSaturate.json -->

# UMaterialExpressionSaturate

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionScalarParameter.json -->

# UMaterialExpressionScalarParameter

## Inheritance

`UMaterialExpressionParameter`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultValue` | `float` | - |
| `SliderMin` | `float` | Sets the lower bound for the slider on this parameter in the material instance editor. |
| `SliderMax` | `float` | Sets the upper bound for the slider on this parameter in the material instance editor. <br>	  The slider will be disabled if SliderMax <= SliderMin. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSceneColor.json -->

# UMaterialExpressionSceneColor

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputMode` | `TEnumAsByte < enum EMaterialSceneAttributeInputMode :: Type >` | Coordinates - UV coordinates to apply to the scene color lookup.<br>	 OffsetFraction - 	An offset to apply to the scene color lookup in a 2d fraction of the screen. |
| `Input` | `FExpressionInput` | Based on the input mode the input will be treated as either:<br>	 UV coordinates to apply to the scene color lookup or <br>	 an offset to apply to the scene color lookup, in a 2d fraction of the screen. |
| `OffsetFraction_DEPRECATED` | `FExpressionInput` | - |
| `ConstInput` | `FVector2D` | only used if Input is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSceneDepth.json -->

# UMaterialExpressionSceneDepth

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputMode` | `TEnumAsByte < enum EMaterialSceneAttributeInputMode :: Type >` | Coordinates - UV coordinates to apply to the scene depth lookup.<br>	 OffsetFraction - An offset to apply to the scene depth lookup in a 2d fraction of the screen. |
| `Input` | `FExpressionInput` | Based on the input mode the input will be treated as either:<br>	 UV coordinates to apply to the scene depth lookup or <br>	 an offset to apply to the scene depth lookup, in a 2d fraction of the screen. |
| `Coordinates_DEPRECATED` | `FExpressionInput` | - |
| `ConstInput` | `FVector2D` | only used if Input is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSceneDepthWithoutWater.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSceneTexture.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionScreenPosition.json -->

# UMaterialExpressionScreenPosition

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Mapping` | `TEnumAsByte < EMaterialExpressionScreenPositionMapping >` | View input property to be accessed |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSetMaterialAttributes.json -->

# UMaterialExpressionSetMaterialAttributes

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Inputs` | `TArray < FExpressionInput >` | - |
| `AttributeSetTypes` | `TArray < FGuid >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionShadowScaleCustomOutput.json -->

# UMaterialExpressionShadowScaleCustomOutput

## Inheritance

`UMaterialExpressionCustomOutput`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSign.json -->

# UMaterialExpressionSign

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSine.json -->

# UMaterialExpressionSine

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |
| `Period` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSingleLayerWaterMaterialOutput.json -->

# UMaterialExpressionSingleLayerWaterMaterialOutput

Material output expression for writing single layer water volume material properties.

## Inheritance

`UMaterialExpressionCustomOutput`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ScatteringCoefficients` | `FExpressionInput` | Input for scattering coefficient describing how light scatter around and is absorbed. Valid range is [0,+inf[. Unit is 1cm. |
| `AbsorptionCoefficients` | `FExpressionInput` | Input for scattering coefficient describing how light bounce is absorbed. Valid range is [0,+inf[. Unit is 1cm. |
| `PhaseG` | `FExpressionInput` | Input for phase function 'g' parameter describing how much forward(g>0) or backward (g<0) light scatter around. Valid range is [-1,1]. |
| `ColorScaleBehindWater` | `FExpressionInput` | Input for custom color multiplier for scene color behind water. Can be used for caustics textures etc. Defaults to 1.0. Valid range is [0,+inf[. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSobol.json -->

# UMaterialExpressionSobol

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Cell` | `FExpressionInput` | 2D integer cell in 256x256 grid.<br>	   Uses cell (0,0) if not connected |
| `Index` | `FExpressionInput` | - |
| `Seed` | `FExpressionInput` | - |
| `ConstIndex` | `uint32` | - |
| `ConstSeed` | `FVector2D` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSpeedTree.json -->

# UMaterialExpressionSpeedTree

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GeometryType` | `TEnumAsByte < enum ESpeedTreeGeometryType >` | - |
| `WindType` | `TEnumAsByte < enum ESpeedTreeWindType >` | - |
| `LODType` | `TEnumAsByte < enum ESpeedTreeLODType >` | - |
| `BillboardThreshold` | `float` | - |
| `bAccurateWindVelocities` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSphereMask.json -->

# UMaterialExpressionSphereMask

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FExpressionInput` | 1 to 4 dimensional vector, should be the same type as B |
| `B` | `FExpressionInput` | 1 to 4 dimensional vector, should be the same type as A |
| `Radius` | `FExpressionInput` | in the units that A and B are measured, if not hooked up the internal constant is used |
| `Hardness` | `FExpressionInput` | 0..1 for the range of 0\% to 100\%, if not hooked up the internal constant is used |
| `AttenuationRadius` | `float` | in the unit that A and B are measured |
| `HardnessPercent` | `float` | in percent 0%=soft .. 100%=hard |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSphericalParticleOpacity.json -->

# UMaterialExpressionSphericalParticleOpacity

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Density` | `FExpressionInput` | Density of the particle sphere. |
| `ConstantDensity` | `float` | Constant density of the particle sphere.  Will be overridden if Density is connected. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSquareRoot.json -->

# UMaterialExpressionSquareRoot

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionStaticBool.json -->

# UMaterialExpressionStaticBool

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionStaticBoolParameter.json -->

# UMaterialExpressionStaticBoolParameter

## Inheritance

`UMaterialExpressionParameter`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultValue` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionStaticComponentMaskParameter.json -->

# UMaterialExpressionStaticComponentMaskParameter

## Inheritance

`UMaterialExpressionParameter`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |
| `DefaultR` | `uint32` | - |
| `DefaultG` | `uint32` | - |
| `DefaultB` | `uint32` | - |
| `DefaultA` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionStaticSwitch.json -->

# UMaterialExpressionStaticSwitch

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultValue` | `uint32` | - |
| `A` | `FExpressionInput` | - |
| `B` | `FExpressionInput` | - |
| `Value` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionStaticSwitchParameter.json -->

# UMaterialExpressionStaticSwitchParameter

## Inheritance

`UMaterialExpressionStaticBoolParameter`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FExpressionInput` | - |
| `B` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionSubtract.json -->

# UMaterialExpressionSubtract

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FExpressionInput` | - |
| `B` | `FExpressionInput` | - |
| `ConstA` | `float` | only used if A is not hooked up |
| `ConstB` | `float` | only used if B is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTangent.json -->

# UMaterialExpressionTangent

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |
| `Period` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTangentOutput.json -->

# UMaterialExpressionTangentOutput

## Inheritance

`UMaterialExpressionCustomOutput`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTemporalSobol.json -->

# UMaterialExpressionTemporalSobol

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Index` | `FExpressionInput` | - |
| `Seed` | `FExpressionInput` | - |
| `ConstIndex` | `uint32` | - |
| `ConstSeed` | `FVector2D` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTerrainBlend.json -->

# UMaterialExpressionTerrainBlend

## Inheritance

`UMaterialExpressionTerrainBlendBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UV` | `FExpressionInput` | - |
| `Inputs` | `TArray < FTerrainLayer >` | - |
| `ConstCoordinate` | `uint32` | only used if Coordinates is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTerrainBlendBase.json -->

# UMaterialExpressionTerrainBlendBase

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DDxDDyTiling` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTerrainBlendDesert.json -->

# UMaterialExpressionTerrainBlendDesert

## Inheritance

`UMaterialExpressionTerrainBlendBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UV` | `FExpressionInput` | - |
| `Inputs` | `TArray < FTerrainLayerDesert >` | - |
| `ConstCoordinate` | `uint32` | only used if Coordinates is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTerrainBlendHeight.json -->

# UMaterialExpressionTerrainBlendHeight

## Inheritance

`UMaterialExpressionTerrainBlendBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UV` | `FExpressionInput` | - |
| `CameraWeight` | `FExpressionInput` | - |
| `bUseHPTerrainHeight` | `bool` | - |
| `Inputs` | `TArray < FTerrainLayerHeight >` | - |
| `ConstCoordinate` | `uint32` | only used if Coordinates is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTerrainBlendHeightBlend.json -->

# UMaterialExpressionTerrainBlendHeightBlend

## Inheritance

`UMaterialExpressionTerrainBlendBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UV` | `FExpressionInput` | - |
| `CameraWeight` | `FExpressionInput` | - |
| `HeightGlobal` | `FExpressionInput` | - |
| `Inputs` | `TArray < FTerrainLayerHeightBlend >` | - |
| `ConstCoordinate` | `uint32` | only used if Coordinates is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTexcoordAddressing.json -->

# UMaterialExpressionTexcoordAddressing

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Coordinates` | `FExpressionInput` | - |
| `ConstCoordinate` | `uint32` | only used if Coordinates is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTextureBase.json -->

# UMaterialExpressionTextureBase

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Texture` | `UTexture *` | - |
| `SamplerType` | `TEnumAsByte < enum EMaterialSamplerType >` | - |
| `IsDefaultMeshpaintTexture` | `uint32` | Is default selected texture when using mesh paint mode texture painting |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTextureCoordinate.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTextureProperty.json -->

# UMaterialExpressionTextureProperty

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TextureObject` | `FExpressionInput` | - |
| `Property` | `TEnumAsByte < EMaterialExposedTextureProperty >` | Texture property to be accessed |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTextureSample.json -->

# UMaterialExpressionTextureSample

## Inheritance

`UMaterialExpressionTextureBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Coordinates` | `FExpressionInput` | - |
| `TextureObject` | `FExpressionInput` | Texture object input which overrides Texture if specified. <br>	  This only shows up in material functions and is used to implement texture parameters without actually putting the texture parameter in the function. |
| `MipValue` | `FExpressionInput` | Meaning depends on MipValueMode, a single unit is one mip level |
| `CoordinatesDX` | `FExpressionInput` | Enabled only if MipValueMode == TMVM_Derivative |
| `CoordinatesDY` | `FExpressionInput` | Enabled only if MipValueMode == TMVM_Derivative |
| `MipValueMode` | `TEnumAsByte < enum ETextureMipValueMode >` | Defines how the MipValue property is applied to the texture lookup |
| `SamplerSource` | `TEnumAsByte < enum ESamplerSourceMode >` | Controls where the sampler for this texture lookup will come from.  <br>	  Choose 'from texture asset' to make use of the UTexture addressing settings,<br>	  Otherwise use one of the global samplers, which will not consume a sampler slot.<br>	  This allows materials to use more than 16 unique textures on SM5 platforms. |
| `ConstCoordinate` | `uint32` | only used if Coordinates is not hooked up |
| `ConstMipValue` | `int32` | only used if MipValue is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTextureSampleParameter.json -->

# UMaterialExpressionTextureSampleParameter

## Inheritance

`UMaterialExpressionTextureSample`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `ExpressionGUID` | `FGuid` | GUID that should be unique within the material, this is used for parameter renaming. |
| `Group` | `FName` | The name of the parameter Group to display in MaterialInstance Editor. Default is None group |
| `SortPriority` | `int32` | Controls where the this parameter is displayed in a material instance parameter list.  The lower the number the higher up in the parameter list. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTextureSampleParameterSubUV.json -->

# UMaterialExpressionTextureSampleParameterSubUV

## Inheritance

`UMaterialExpressionTextureSampleParameter2D`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bBlend` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTime.json -->

# UMaterialExpressionTime

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bIgnorePause` | `uint32` | This time continues advancing regardless of whether the game is paused. |
| `bOverride_Period` | `uint32` | Enables or disables the Period value. |
| `Period` | `float` | Time will loop around once it gets to Period. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTransform.json -->

# UMaterialExpressionTransform

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | input expression for this transform |
| `TransformSourceType` | `TEnumAsByte < enum EMaterialVectorCoordTransformSource >` | Source coordinate space of the FVector |
| `TransformType` | `TEnumAsByte < enum EMaterialVectorCoordTransform >` | Destination coordinate space of the FVector |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTransformPosition.json -->

# UMaterialExpressionTransformPosition

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | input expression for this transform |
| `TransformSourceType` | `TEnumAsByte < enum EMaterialPositionTransformSource >` | source format of the position that will be transformed |
| `TransformType` | `TEnumAsByte < enum EMaterialPositionTransformSource >` | type of transform to apply to the input expression |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionTruncate.json -->

# UMaterialExpressionTruncate

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionVectorNoise.json -->

# UMaterialExpressionVectorNoise

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Position` | `FExpressionInput` | 2 to 3 dimensional vector |
| `NoiseFunction` | `TEnumAsByte < enum EVectorNoiseFunction >` | Noise function, affects performance and look |
| `Quality` | `int32` | For noise functions where applicable, lower numbers are faster and lower quality, higher numbers are slower and higher quality |
| `bTiling` | `uint32` | Whether tile the noise pattern, useful for baking to seam-free repeating textures |
| `TileSize` | `uint32` | How many units in each tile (if Tiling is on) <br>	   For Perlin noise functions, Tile Size must be a multiple of three |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionVectorParameter.json -->

# UMaterialExpressionVectorParameter

## Inheritance

`UMaterialExpressionParameter`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultValue` | `FLinearColor` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionVertexInterpolator.json -->

# UMaterialExpressionVertexInterpolator

## Inheritance

`UMaterialExpressionCustomOutput`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionViewProperty.json -->

# UMaterialExpressionViewProperty

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Property` | `TEnumAsByte < EMaterialExposedViewProperty >` | View input property to be accessed |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionWorldPosition.json -->

# UMaterialExpressionWorldPosition

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WorldPositionShaderOffset` | `TEnumAsByte < EWorldPositionIncludedOffsets >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialFunction.json -->

# UMaterialFunction

A Material Function is a collection of material expressions that can be reused in different materials

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StateId` | `FGuid` | Used by materials using this function to know when to recompile. |
| `Description` | `FString` | Description of the function which will be displayed as a tooltip wherever the function is used. |
| `bExposeToLibrary` | `uint32` | Whether to list this function in the material function library, which is a window in the material editor that lists categorized functions. |
| `bUseFullPrecision` | `uint32` | Whether forces the function to use full (highp) precision in the pixel shader. |
| `FunctionExpressions` | `TArray < UMaterialExpression * >` | Array of material expressions, excluding Comments.  Used by the material editor. |
| `bReentrantFlag` | `uint32` | Transient flag used to track re-entrance in recursive functions like IsDependent. |
| `ParentFunction` | `UMaterialFunction *` | Used in the material editor, points to the function asset being edited, which this function is just a preview for. |
| `LibraryCategories_DEPRECATED` | `TArray < FString >` | Categories that this function belongs to in the material function library.  <br>	  Ideally categories should be chosen carefully so that there are not too many. |
| `LibraryCategoriesText` | `TArray < FText >` | Categories that this function belongs to in the material function library.  <br>	  Ideally categories should be chosen carefully so that there are not too many. |
| `FunctionEditorComments` | `TArray < UMaterialExpressionComment * >` | Array of comments associated with this material; viewed in the material editor. |
| `PreviewMaterial` | `UMaterial *` | - |
| `CombinedInputTypes` | `uint32` | - |
| `CombinedOutputTypes` | `uint32` | - |
| `ThumbnailInfo` | `UThumbnailInfo *` | Information for thumbnail rendering |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialInstance.json -->

# UMaterialInstance

## Inheritance

`UMaterialInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MeshLogicType` | `int32` | 材质实例的功能分类：1:挂件 |
| `PhysMaterial` | `UPhysicalMaterial *` | Physical material to use for this graphics material. Used for sounds, effects etc. |
| `Parent` | `UMaterialInterface *` | Parent material. |
| `bOverride_IncludeShaderCode` | `uint32` | - |
| `bIncludeShaderCode` | `uint32` | - |
| `bHasStaticPermutationResource` | `uint32` | Indicates whether the instance has static permutation resources (which are required when static parameters are present)<br>	  Read directly from the rendering thread, can only be modified with the use of a FMaterialUpdateContext.<br>	  When true, StaticPermutationMaterialResources will always be valid and non-null. |
| `bOverrideSubsurfaceProfile` | `uint32` | Defines if SubsurfaceProfile from this instance is used or it uses the parent one. |
| `FontParameterValues` | `TArray < FFontParameterValue >` | Font parameters. |
| `ScalarParameterValues` | `TArray < FScalarParameterValue >` | Scalar parameters. |
| `TextureParameterValues` | `TArray < FTextureParameterValue >` | Texture parameters. |
| `VectorParameterValues` | `TArray < FVectorParameterValue >` | Vector parameters. |
| `CustomParameterValues` | `TArray < FCustomParameterValue >` | 项目自定义参数值数组。 承载 Atlas Clipmap 等原先寄生在 ScalarParameterValues TextureParameterValues 上的扩展数据。 仅当 IsScalarParameterUsedAsAtlasPosition IsTextureParameterUsedAsClipmap GetClipmapParameterValue 等编辑期或预处理逻辑读取， 渲染线程所需的数值仍然仅依赖 ScalarParameterValues TextureParameterValues。 注意：不标 BlueprintReadOnly —— FCustomParameterValue 含 TSoftObjectPtr ECustomParameterKind 等 非蓝图兼容字段，UHT 会报 "Type 'TArray' is not supported by blueprint"。 这个数组原本就不是蓝图 API 面（蓝图继续通过 ScalarTexture Parameter 接口读写）。 |
| `DynamicInstancingParameters` | `TMap < FString , FVector4 >` | Dynamic instancing parameters. |
| `bOverrideBaseProperties_DEPRECATED` | `bool` | - |
| `BasePropertyOverrides` | `FMaterialInstanceBasePropertyOverrides` | - |
| `PermutationTextureReferences` | `TArray < UTexture * >` | Cached texture references from all expressions in the material (including nested functions).<br>	 This is used to link uniform texture expressions which were stored in the DDC with the UTextures that they reference. |
| `bEnableTexture2DArrayShaderVariant` | `uint32` | - |
| `ReferencedTextureGuids` | `TArray < FGuid >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialInstanceDynamic.json -->

# UMaterialInstanceDynamic

## Inheritance

`UMaterialInstance`

## Functions

### `SetScalarParameterValue`

```text
SetScalarParameterValue(ParameterName: FName, Value: float) -> void
```

Set a MID scalar (float) parameter value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_GetScalarParameterValue`

```text
K2_GetScalarParameterValue(ParameterName: FName) -> float
```

Get the current scalar (float) parameter value from an MID

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetTextureParameterValue`

```text
SetTextureParameterValue(ParameterName: FName, Value: UTexture *) -> void
```

Set an MID texture parameter value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Value` | `UTexture *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_GetTextureParameterValue`

```text
K2_GetTextureParameterValue(ParameterName: FName) -> UTexture *
```

Get the current MID texture parameter value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UTexture *` | - |

### `SetVectorParameterValue`

```text
SetVectorParameterValue(ParameterName: FName, Value: FLinearColor) -> void
```

Set an MID vector parameter value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Value` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_GetVectorParameterValue`

```text
K2_GetVectorParameterValue(ParameterName: FName) -> FLinearColor
```

Get the current MID vector parameter value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `K2_InterpolateMaterialInstanceParams`

```text
K2_InterpolateMaterialInstanceParams(SourceA: UMaterialInstance *, SourceB: UMaterialInstance *, Alpha: float) -> void
```

Interpolates the scalar and vector parameters of this material instance based on two other material instances, and an alpha blending factor
	  The output is the object itself (this).
	  Supports the case SourceA==this || SourceB==this
	  Both material have to be from the same base material

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceA` | `UMaterialInstance *` | value that is used for Alpha=0, silently ignores the case if 0 |
| `SourceB` | `UMaterialInstance *` | value that is used for Alpha=1, silently ignores the case if 0 |
| `Alpha` | `float` | usually in the range 0..1, values outside the range extrapolate |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_CopyMaterialInstanceParameters`

```text
K2_CopyMaterialInstanceParameters(Source: UMaterialInterface *) -> void
```

Copies over parameters given a material interface (copy each instance following the hierarchy)
	  Very slow implementation, avoid using at runtime. Hopefully we can replace ity later with something like CopyInterpParameters()
	  The output is the object itself (this).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Source` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CopyInterpParameters`

```text
CopyInterpParameters(Source: UMaterialInstance *) -> void
```

Copies over parameters given a material instance (only copy from the instance, not following the hierarchy)
	  much faster than K2_CopyMaterialInstanceParameters(),
	  The output is the object itself (this).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Source` | `UMaterialInstance *` | ignores the call if 0 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CopyParameterOverrides`

```text
CopyParameterOverrides(MaterialInstance: UMaterialInstance *) -> void
```

Copy parameter values from another material instance. This will copy only
	  parameters explicitly overridden in that material instance!!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MaterialInstance` | `UMaterialInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialInterface.json -->

# UMaterialInterface

## Inheritance

`UObject` -> `IBlendableInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SubsurfaceProfile` | `USubsurfaceProfile *` | SubsurfaceProfile, for Screen Space Subsurface Scattering |
| `LightmassSettings` | `FLightmassMaterialInterfaceSettings` | The Lightmass settings for this object. |
| `TextureStreamingData` | `TArray < FMaterialTextureInfo >` | Data used by the texture streaming to know how each texture is sampled by the material. Sorted by names for quick access. |

## Functions

### `GetBaseMaterial`

```text
GetBaseMaterial() -> ENGINE_API UMaterial *
```

Walks up parent chain and finds the base Material that this is an instance of. Just calls the virtual GetMaterial()

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API UMaterial *` | - |

### `GetPhysicalMaterial`

```text
GetPhysicalMaterial() -> UPhysicalMaterial *
```

Return a pointer to the physical material used by this material instance.

**Returns**

| Type | Description |
|---|---|
| `UPhysicalMaterial *` | The physical material. |

### `SetForceMipLevelsToBeResident`

```text
SetForceMipLevelsToBeResident(OverrideForceMiplevelsToBeResident: bool, bForceMiplevelsToBeResidentValue: bool, ForceDuration: float, CinematicTextureGroups: int32) -> ENGINE_API virtual void
```

Force the streaming system to disregard the normal logic for the specified duration and
	  instead always load all mip-levels for all textures used by this material.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OverrideForceMiplevelsToBeResident` | `bool` | - Whether to use (true) or ignore (false) the bForceMiplevelsToBeResidentValue parameter. |
| `bForceMiplevelsToBeResidentValue` | `bool` | - true forces all mips to stream in. false lets other factors decide what to do with the mips. |
| `ForceDuration` | `float` | - Number of seconds to keep all mip-levels in memory, disregarding the normal priority logic. Negative value turns it off. |
| `CinematicTextureGroups` | `int32` | - Bitfield indicating texture groups that should use extra high-resolution mips |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API virtual void` | - |

### `SetStreamingTextureMipOffset`

```text
SetStreamingTextureMipOffset(NewMipOffset: int32, SizeLimited: bool) -> ENGINE_API virtual void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewMipOffset` | `int32` | - |
| `SizeLimited` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API virtual void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialParameterCollection.json -->

# UMaterialParameterCollection

Asset class that contains a list of parameter names and their default values. 
  Any number of materials can reference these parameters and get new values when the parameter values are changed.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StateId` | `FGuid` | Used by materials using this collection to know when to recompile. |
| `ScalarParameters` | `TArray < FCollectionScalarParameter >` | - |
| `VectorParameters` | `TArray < FCollectionVectorParameter >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialParameterCollectionInstance.json -->

# UMaterialParameterCollectionInstance

Class that stores per-world instance parameter data for a given UMaterialParameterCollection resource. 
  Instances of this class are always transient.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Collection` | `UMaterialParameterCollection *` | Collection resource this instance is based off of. |
| `World` | `UWorld *` | World that owns this instance. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialShaderQualitySettings.json -->

# UMaterialShaderQualitySettings

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ForwardSettingMap` | `TMap < FName , UShaderPlatformQualitySettings * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMatIDFallbackConfig.json -->

# UMatIDFallbackConfig

## Inheritance

`UDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `IDToFallbackLayers` | `TMap < FString , FMatIDFallbackArray >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMediaPlayer.json -->

# UMediaPlayer

Implements a media player asset that can play movies and other media sources.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CacheAhead` | `FTimespan` | Duration of samples to cache ahead of the play head.<br>	 <br>	  @see CacheBehind, CacheBehindGame |
| `CacheBehind` | `FTimespan` | Duration of samples to cache behind the play head (when not running as game).<br>	 <br>	  @see CacheAhead, CacheBehindGame |
| `CacheBehindGame` | `FTimespan` | Duration of samples to cache behind the play head (when running as game).<br>	 <br>	  @see CacheAhead, CacheBehind |
| `NativeAudioOut` | `bool` | Output any audio via the operating system's sound mixer instead of a Sound Wave asset.<br>	 <br>	  If enabled, the assigned Sound Wave asset will be ignored. The SetNativeVolume<br>	  function can then be used to change the audio output volume at runtime. Note that<br>	  not all media player plug-ins may support native audio output on all platforms.<br>	 <br>	  @see SetNativeVolume |
| `PlayOnOpen` | `bool` | Automatically start playback after media opened successfully.<br>	 <br>	  If disabled, listen to the OnMediaOpened Blueprint event to detect when<br>	  the media finished opening, and then start playback using the Play function.<br>	 <br>	  @see OpenFile, OpenPlaylist, OpenPlaylistIndex, OpenSource, OpenUrl, Play |
| `Shuffle` | `uint32` | Whether playback should shuffle media sources in the play list.<br>	 <br>	  @see OpenPlaylist, OpenPlaylistIndex |
| `Loop` | `uint32` | Whether the player should loop when media playback reaches the end.<br>	 <br>	  Use the SetLooping function to change this value at runtime.<br>	 <br>	  @see IsLooping, SetLooping |
| `Playlist` | `UMediaPlaylist *` | The play list to use, if any.<br>	 <br>	  Use the OpenPlaylist or OpenPlaylistIndex function to change this value at runtime.<br>	 <br>	  @see OpenPlaylist, OpenPlaylistIndex |
| `PlaylistIndex` | `int32` | The current index of the source in the play list being played.<br>	 <br>	  Use the Previous and Next methods to change this value at runtime.<br>	 <br>	  @see Next, Previous |
| `HorizontalFieldOfView` | `float` | The initial horizontal field of view (in Euler degrees; default = 90).<br>	 <br>	  This setting is used only for 360 videos. It determines the portion of the<br>	  video that is visible at a time. To modify the field of view at runtime in<br>	  Blueprints, use the SetHorizontalFieldOfView function.<br>	 <br>	  @see GetHorizontalFieldOfView, SetHorizontalFieldOfView, VerticalFieldOfView, ViewRotation |
| `VerticalFieldOfView` | `float` | The initial vertical field of view (in Euler degrees; default = 60).<br>	 <br>	  This setting is used only for 360 videos. It determines the portion of the<br>	  video that is visible at a time. To modify the field of view at runtime in<br>	  Blueprints, use the SetHorizontalFieldOfView function.<br>	 <br>	  Please note that some 360 video players may be able to change only the<br>	  horizontal field of view, and this setting may be ignored.<br>	 <br>	  @see GetVerticalFieldOfView, SetVerticalFieldOfView, HorizontalFieldOfView, ViewRotation |
| `ViewRotation` | `FRotator` | The initial view rotation.<br>	 <br>	  This setting is used only for 360 videos. It determines the rotation of<br>	  the video's view. To modify the view orientation at runtime in Blueprints,<br>	  use the GetViewRotation and SetViewRotation functions.<br>	 <br>	  Please note that not all players may support video view rotations.<br>	 <br>	  @see GetViewRotation, SetViewRotation, HorizontalFieldOfView, VerticalFieldOfView |
| `PlayerGuid` | `FGuid` | The player's globally unique identifier. |

## Functions

### `CanPause`

```text
CanPause() -> bool
```

Check whether media playback can be paused right now.
	 
	  Playback can be paused if the media supports pausing and if it is currently playing.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if pausing playback can be paused, false otherwise. |

### `CanPlaySource`

```text
CanPlaySource(MediaSource: UMediaSource *) -> bool
```

Check whether the specified media source can be played by this player.
	 
	  If a desired player name is set for this player, it will only check
	  whether that particular player type can play the specified source.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MediaSource` | `UMediaSource *` | The media source to check. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the media source can be opened, false otherwise. |

### `CanPlayUrl`

```text
CanPlayUrl(Url: FString &) -> bool
```

Check whether the specified URL can be played by this player.
	 
	  If a desired player name is set for this player, it will only check
	  whether that particular player type can play the specified URL.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Url` | `FString &` | The URL to check. |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Close`

```text
Close() -> void
```

Close the currently open media, if any.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAudioTrackChannels`

```text
GetAudioTrackChannels(TrackIndex: int32, FormatIndex: int32) -> int32
```

Get the number of channels in the specified audio track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackIndex` | `int32` | Index of the audio track, or INDEX_NONE for the selected one. |
| `FormatIndex` | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `int32` | Number of channels. |

### `GetAudioTrackSampleRate`

```text
GetAudioTrackSampleRate(TrackIndex: int32, FormatIndex: int32) -> int32
```

Get the sample rate of the specified audio track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackIndex` | `int32` | Index of the audio track, or INDEX_NONE for the selected one. |
| `FormatIndex` | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `int32` | Samples per second. |

### `GetAudioTrackType`

```text
GetAudioTrackType(TrackIndex: int32, FormatIndex: int32) -> FString
```

Get the type of the specified audio track format.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackIndex` | `int32` | The index of the track, or INDEX_NONE for the selected one. |
| `FormatIndex` | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `FString` | Audio format type string. |

### `GetDesiredPlayerName`

```text
GetDesiredPlayerName() -> FName
```

Get the name of the current desired native player.

**Returns**

| Type | Description |
|---|---|
| `FName` | The name of the desired player, or NAME_None if not set. |

### `GetDuration`

```text
GetDuration() -> FTimespan
```

Get the media's duration.

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | A time span representing the duration. |

### `GetHorizontalFieldOfView`

```text
GetHorizontalFieldOfView() -> float
```

Get the current horizontal field of view (only for 360 videos).

**Returns**

| Type | Description |
|---|---|
| `float` | Horizontal field of view (in Euler degrees). |

### `GetMediaName`

```text
GetMediaName() -> FText
```

Get the human readable name of the currently loaded media source.

**Returns**

| Type | Description |
|---|---|
| `FText` | Media source name, or empty text if no media is opened |

### `GetNumTracks`

```text
GetNumTracks(TrackType: EMediaPlayerTrack) -> int32
```

Get the number of tracks of the given type.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackType` | `EMediaPlayerTrack` | The type of media tracks. |

**Returns**

| Type | Description |
|---|---|
| `int32` | Number of tracks. |

### `GetNumTrackFormats`

```text
GetNumTrackFormats(TrackType: EMediaPlayerTrack, TrackIndex: int32) -> int32
```

Get the number of formats of the specified track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackType` | `EMediaPlayerTrack` | The type of media tracks. |
| `TrackIndex` | `int32` | The index of the track. |

**Returns**

| Type | Description |
|---|---|
| `int32` | Number of formats. |

### `GetPlayerName`

```text
GetPlayerName() -> FName
```

Get the name of the current native media player.

**Returns**

| Type | Description |
|---|---|
| `FName` | Player name, or NAME_None if not available. |

### `GetPlaylist`

```text
GetPlaylist() -> UMediaPlaylist *
```

Get the current play list.
	 
	  Media players always have a valid play list. In C++ code you can use
	  the GetPlaylistRef to get a reference instead of a pointer to it.

**Returns**

| Type | Description |
|---|---|
| `UMediaPlaylist *` | The play list. |

### `GetPlaylistIndex`

```text
GetPlaylistIndex() -> int32
```

Get the current play list index.

**Returns**

| Type | Description |
|---|---|
| `int32` | Play list index. |

### `GetRate`

```text
GetRate() -> float
```

Get the media's current playback rate.

**Returns**

| Type | Description |
|---|---|
| `float` | The playback rate. |

### `GetSelectedTrack`

```text
GetSelectedTrack(TrackType: EMediaPlayerTrack) -> int32
```

Get the index of the currently selected track of the given type.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackType` | `EMediaPlayerTrack` | The type of track to get. |

**Returns**

| Type | Description |
|---|---|
| `int32` | The index of the selected track, or INDEX_NONE if no track is active. |

### `GetSupportedRates`

```text
GetSupportedRates(OutRates: TArray < FFloatRange > &, Unthinned: bool) -> void
```

Get the supported playback rates.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutRates` | `TArray < FFloatRange > &` | - |
| `Unthinned` | `bool` | Whether the rates are for unthinned playback. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTime`

```text
GetTime() -> FTimespan
```

Get the media's current playback time.

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | Playback time. |

### `GetTrackDisplayName`

```text
GetTrackDisplayName(TrackType: EMediaPlayerTrack, TrackIndex: int32) -> FText
```

Get the human readable name of the specified track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackType` | `EMediaPlayerTrack` | The type of track. |
| `TrackIndex` | `int32` | The index of the track, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `FText` | Display name. |

### `GetTrackFormat`

```text
GetTrackFormat(TrackType: EMediaPlayerTrack, TrackIndex: int32) -> int32
```

Get the index of the active format of the specified track type.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackType` | `EMediaPlayerTrack` | The type of track. |
| `TrackIndex` | `int32` | The index of the track, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `int32` | The index of the selected format. |

### `GetTrackLanguage`

```text
GetTrackLanguage(TrackType: EMediaPlayerTrack, TrackIndex: int32) -> FString
```

Get the language tag of the specified track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackType` | `EMediaPlayerTrack` | The type of track. |
| `TrackIndex` | `int32` | The index of the track, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `FString` | Language tag, i.e. "en-US" for English, or "und" for undefined. |

### `GetUrl`

```text
GetUrl() -> const FString &
```

Get the URL of the currently loaded media, if any.

**Returns**

| Type | Description |
|---|---|
| `const FString &` | Media URL, or empty string if no media was loaded. |

### `GetVerticalFieldOfView`

```text
GetVerticalFieldOfView() -> float
```

Get the current vertical field of view (only for 360 videos).

**Returns**

| Type | Description |
|---|---|
| `float` | Vertical field of view (in Euler degrees), or 0.0 if not available. |

### `GetVideoTrackAspectRatio`

```text
GetVideoTrackAspectRatio(TrackIndex: int32, FormatIndex: int32) -> float
```

Get the aspect ratio of the specified video track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackIndex` | `int32` | Index of the video track, or INDEX_NONE for the selected one. |
| `FormatIndex` | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `float` | Aspect ratio. |

### `GetVideoTrackDimensions`

```text
GetVideoTrackDimensions(TrackIndex: int32, FormatIndex: int32) -> FIntPoint
```

Get the current dimensions of the specified video track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackIndex` | `int32` | The index of the track, or INDEX_NONE for the selected one. |
| `FormatIndex` | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `FIntPoint` | Video dimensions (in pixels). |

### `GetVideoTrackFrameRate`

```text
GetVideoTrackFrameRate(TrackIndex: int32, FormatIndex: int32) -> float
```

Get the frame rate of the specified video track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackIndex` | `int32` | The index of the track, or INDEX_NONE for the selected one. |
| `FormatIndex` | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `float` | Frame rate (in frames per second). |

### `GetVideoTrackFrameRates`

```text
GetVideoTrackFrameRates(TrackIndex: int32, FormatIndex: int32) -> FFloatRange
```

Get the supported range of frame rates of the specified video track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackIndex` | `int32` | The index of the track, or INDEX_NONE for the selected one. |
| `FormatIndex` | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `FFloatRange` | Frame rate range (in frames per second). |

### `GetVideoTrackType`

```text
GetVideoTrackType(TrackIndex: int32, FormatIndex: int32) -> FString
```

Get the type of the specified video track format.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackIndex` | `int32` | The index of the track, or INDEX_NONE for the selected one. |
| `FormatIndex` | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `FString` | Video format type string. |

### `GetViewRotation`

```text
GetViewRotation() -> FRotator
```

Get the current view rotation (only for 360 videos).

**Returns**

| Type | Description |
|---|---|
| `FRotator` | View rotation, or zero rotator if not available. |

### `HasError`

```text
HasError() -> bool
```

Check whether the player is in an error state.
	 
	  When the player is in an error state, no further operations are possible.
	  The current media must be closed, and a new media source must be opened
	  before the player can be used again. Errors are usually caused by faulty
	  media files or interrupted network connections.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsBuffering`

```text
IsBuffering() -> bool
```

Check whether playback is buffering data.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if looping, false otherwise. |

### `IsConnecting`

```text
IsConnecting() -> bool
```

Check whether the player is currently connecting to a media source.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if connecting, false otherwise. |

### `IsLooping`

```text
IsLooping() -> bool
```

Check whether playback is looping.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if looping, false otherwise. |

### `IsPaused`

```text
IsPaused() -> bool
```

Check whether playback is currently paused.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if playback is paused, false otherwise. |

### `IsPlaying`

```text
IsPlaying() -> bool
```

Check whether playback has started.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if playback has started, false otherwise. |

### `IsPreparing`

```text
IsPreparing() -> bool
```

Check whether the media is currently opening or buffering.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if playback is being prepared, false otherwise. |

### `IsReady`

```text
IsReady() -> bool
```

Check whether media is ready for playback.
	 
	  A player is ready for playback if it has a media source opened that
	  finished preparing and is not in an error state.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if media is ready, false otherwise. |

### `Next`

```text
Next() -> bool
```

Open the next item in the current play list.
	 
	  The player will start playing the new media source if it was playing
	  something previously, otherwise it will only open the media source.

**Returns**

| Type | Description |
|---|---|
| `bool` | true on success, false otherwise. |

### `OpenFile`

```text
OpenFile(FilePath: FString &) -> bool
```

Opens the specified media file path.
	 
	  A return value of true indicates that the player will attempt to open
	  the media, but it may fail to do so later for other reasons, i.e. if
	  a connection to the media server timed out. Use the OnMediaOpened and
	  OnMediaOpenFailed delegates to detect if and when the media is ready!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FilePath` | `FString &` | The file path to open. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the file path will be opened, false otherwise. |

### `OpenPlaylist`

```text
OpenPlaylist(InPlaylist: UMediaPlaylist *) -> bool
```

Open the first media source in the specified play list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPlaylist` | `UMediaPlaylist *` | The play list to open. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the source will be opened, false otherwise. |

### `OpenPlaylistIndex`

```text
OpenPlaylistIndex(InPlaylist: UMediaPlaylist *, Index: int32) -> bool
```

Open a particular media source in the specified play list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPlaylist` | `UMediaPlaylist *` | The play list to open. |
| `Index` | `int32` | The index of the source to open. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the source will be opened, false otherwise. |

### `OpenSource`

```text
OpenSource(MediaSource: UMediaSource *) -> bool
```

Open the specified media source.
	 
	  A return value of true indicates that the player will attempt to open
	  the media, but it may fail to do so later for other reasons, i.e. if
	  a connection to the media server timed out. Use the OnMediaOpened and
	  OnMediaOpenFailed delegates to detect if and when the media is ready!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MediaSource` | `UMediaSource *` | The media source to open. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the source will be opened, false otherwise. |

### `OpenUrl`

```text
OpenUrl(Url: FString &) -> bool
```

Opens the specified media URL.
	 
	  A return value of true indicates that the player will attempt to open
	  the media, but it may fail to do so later for other reasons, i.e. if
	  a connection to the media server timed out. Use the OnMediaOpened and
	  OnMediaOpenFailed delegates to detect if and when the media is ready!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Url` | `FString &` | The URL to open. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the URL will be opened, false otherwise. |

### `Pause`

```text
Pause() -> bool
```

Pauses media playback.
	 
	  This is the same as setting the playback rate to 0.0.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if playback is being paused, false otherwise. |

### `Play`

```text
Play() -> bool
```

Starts media playback.
	 
	  This is the same as setting the playback rate to 1.0.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if playback is starting, false otherwise. |

### `Previous`

```text
Previous() -> bool
```

Open the previous item in the current play list.
	 
	  The player will start playing the new media source if it was playing
	  something previously, otherwise it will only open the media source.

**Returns**

| Type | Description |
|---|---|
| `bool` | true on success, false otherwise. |

### `Reopen`

```text
Reopen() -> bool
```

Reopens the currently opened media or play list.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the media will be opened, false otherwise. |

### `Rewind`

```text
Rewind() -> bool
```

Rewinds the media to the beginning.
	 
	  This is the same as seeking to zero time.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if rewinding, false otherwise. |

### `Seek`

```text
Seek(Time: FTimespan &) -> bool
```

Seeks to the specified playback time.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `FTimespan &` | The playback time to set. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true on success, false otherwise. |

### `SelectTrack`

```text
SelectTrack(TrackType: EMediaPlayerTrack, TrackIndex: int32) -> bool
```

Select the active track of the given type.
	 
	  The selected track will use its currently active format. Active formats will
	  be remembered on a per track basis. The first available format is active by
	  default. To switch the track format, use SetTrackFormat instead.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackType` | `EMediaPlayerTrack` | The type of track to select. |
| `TrackIndex` | `int32` | The index of the track to select, or INDEX_NONE to deselect. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the track was selected, false otherwise. |

### `SetDesiredPlayerName`

```text
SetDesiredPlayerName(PlayerName: FName) -> void
```

Set the name of the desired native player.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerName` | `FName` | The name of the player to set. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLooping`

```text
SetLooping(Looping: bool) -> bool
```

Enables or disables playback looping.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Looping` | `bool` | Whether playback should be looped. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true on success, false otherwise. |

### `SetRate`

```text
SetRate(Rate: float) -> bool
```

Changes the media's playback rate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rate` | `float` | The playback rate to set. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true on success, false otherwise. |

### `SetNativeVolume`

```text
SetNativeVolume(Volume: float) -> bool
```

Set the volume on the native player if not mixing with Sound Wave asset.
	 
	  The SetNativeVolume can be used to change the audio output volume at runtime. Note that
	  not all media player plug-ins may support native audio output on all platforms.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Volume` | `float` | The volume to set. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true on success, false otherwise. |

### `SetTrackFormat`

```text
SetTrackFormat(TrackType: EMediaPlayerTrack, TrackIndex: int32, FormatIndex: int32) -> bool
```

Set the format on the specified track.
	 
	  Selecting the format will not switch to the specified track. To switch
	  tracks, use SelectTrack instead. If the track is already selected, the
	  format change will be applied immediately.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackType` | `EMediaPlayerTrack` | The type of track to update. |
| `TrackIndex` | `int32` | The index of the track to update. |
| `FormatIndex` | `int32` | The index of the format to select (must be valid). |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the track was selected, false otherwise. |

### `SetVideoTrackFrameRate`

```text
SetVideoTrackFrameRate(TrackIndex: int32, FormatIndex: int32, FrameRate: float) -> bool
```

Set the frame rate of the specified video track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackIndex` | `int32` | The index of the track, or INDEX_NONE for the selected one. |
| `FormatIndex` | `int32` | Index of the track format, or INDEX_NONE for the selected one. |
| `FrameRate` | `float` | The frame rate to set (must be in range of format's supported frame rates). |

**Returns**

| Type | Description |
|---|---|
| `bool` | true on success, false otherwise. |

### `SetViewField`

```text
SetViewField(Horizontal: float, Vertical: float, Absolute: bool) -> bool
```

Set the field of view (only for 360 videos).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Horizontal` | `float` | Horizontal field of view (in Euler degrees). |
| `Vertical` | `float` | Vertical field of view (in Euler degrees). |
| `Absolute` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true on success, false otherwise. |

### `SetViewRotation`

```text
SetViewRotation(Rotation: FRotator &, Absolute: bool) -> bool
```

Set the view's rotation (only for 360 videos).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rotation` | `FRotator &` | The desired view rotation. |
| `Absolute` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true on success, false otherwise. |

### `SupportsRate`

```text
SupportsRate(Rate: float, Unthinned: bool) -> bool
```

Check whether the specified playback rate is supported.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rate` | `float` | The playback rate to check. |
| `Unthinned` | `bool` | Whether no frames should be dropped at the given rate. |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SupportsScrubbing`

```text
SupportsScrubbing() -> bool
```

Check whether the currently loaded media supports scrubbing.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if scrubbing is supported, false otherwise. |

### `SupportsSeeking`

```text
SupportsSeeking() -> bool
```

Check whether the currently loaded media can jump to a certain position.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if seeking is supported, false otherwise. |

### `SetAudioDeviceGUID`

```text
SetAudioDeviceGUID(DeviceGUID: FString &) -> void
```

Sets the audio device for the media player; currently only effective on PC platforms.
	  add by watsonxie

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeviceGUID` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnEndReached`

```text
OnEndReached() -> void
```

A delegate that is invoked when playback has reached the end of the media.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMediaClosed`

```text
OnMediaClosed() -> void
```

A delegate that is invoked when a media source has been closed.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMediaOpened`

```text
OnMediaOpened(OpenedUrl: FString) -> void
```

A delegate that is invoked when a media source has been opened.
	 
	  Depending on whether the underlying player implementation opens the media
	  synchronously or asynchronously, this event may be executed before or
	  after the call to OpenSource  OpenUrl returns.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OpenedUrl` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMediaOpenFailed`

```text
OnMediaOpenFailed(FailedUrl: FString) -> void
```

A delegate that is invoked when a media source has failed to open.
	 
	  This delegate is only executed if OpenSource  OpenUrl returned true and
	  the media failed to open asynchronously later. It is not executed if
	  OpenSource  OpenUrl returned false, indicating an immediate failure.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FailedUrl` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPlaybackResumed`

```text
OnPlaybackResumed() -> void
```

A delegate that is invoked when media playback has been resumed.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPlaybackSuspended`

```text
OnPlaybackSuspended() -> void
```

A delegate that is invoked when media playback has been suspended.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnSeekCompleted`

```text
OnSeekCompleted() -> void
```

A delegate that is invoked when a seek operation completed successfully.
	 
	  Depending on whether the underlying player implementation performs seeks
	  synchronously or asynchronously, this event may be executed before or
	  after the call to Seek returns.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTracksChanged`

```text
OnTracksChanged() -> void
```

A delegate that is invoked when the media track collection changed.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMediaPlayFirstFrame`

```text
OnMediaPlayFirstFrame() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMediaPlaylist.json -->

# UMediaPlaylist

Implements a media play list.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Loop` | `uint32` | Whether the play list should loop (default = true). |
| `Items` | `TArray < UMediaSource * >` | List of media sources to play. |

## Functions

### `Add`

```text
Add(MediaSource: UMediaSource *) -> bool
```

Add a media source to the play list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MediaSource` | `UMediaSource *` | The media source to append. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the media source was added, false otherwise. |

### `AddFile`

```text
AddFile(FilePath: FString &) -> bool
```

Add a media file path to the play list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FilePath` | `FString &` | The file path to add. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the file was added, false otherwise. |

### `AddUrl`

```text
AddUrl(Url: FString &) -> bool
```

Add a media URL to the play list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Url` | `FString &` | The URL to add. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the URL was added, false otherwise. |

### `Get`

```text
Get(Index: int32) -> UMediaSource *
```

Get the media source at the specified index.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | The index of the media source to get. |

**Returns**

| Type | Description |
|---|---|
| `UMediaSource *` | The media source, or nullptr if the index doesn't exist. |

### `GetNext`

```text
GetNext(InOutIndex: int32 &) -> UMediaSource *
```

Get the next media source in the play list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOutIndex` | `int32 &` | Index of the current media source (will contain the new index). |

**Returns**

| Type | Description |
|---|---|
| `UMediaSource *` | The media source after the current one, or nullptr if the list is empty. |

### `GetPrevious`

```text
GetPrevious(InOutIndex: int32 &) -> UMediaSource *
```

Get the previous media source in the play list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOutIndex` | `int32 &` | Index of the current media source (will contain the new index). |

**Returns**

| Type | Description |
|---|---|
| `UMediaSource *` | The media source before the current one, or nullptr if the list is empty. |

### `GetRandom`

```text
GetRandom(OutIndex: int32 &) -> UMediaSource *
```

Get a random media source in the play list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutIndex` | `int32 &` | Will contain the index of the returned media source. |

**Returns**

| Type | Description |
|---|---|
| `UMediaSource *` | The random media source, or nullptr if the list is empty. |

### `Insert`

```text
Insert(MediaSource: UMediaSource *, Index: int32) -> void
```

Insert a media source into the play list at the given position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MediaSource` | `UMediaSource *` | The media source to insert. |
| `Index` | `int32` | The index to insert into. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Num`

```text
Num() -> int32
```

Get the number of media sources in the play list.

**Returns**

| Type | Description |
|---|---|
| `int32` | Number of media sources. |

### `Remove`

```text
Remove(MediaSource: UMediaSource *) -> bool
```

Remove all occurrences of the given media source in the play list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MediaSource` | `UMediaSource *` | The media source to remove. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the media source was removed, false otherwise. |

### `RemoveAt`

```text
RemoveAt(Index: int32) -> bool
```

Remove the media source at the specified position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | The index of the media source to remove. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the media source was removed, false otherwise. |

### `Replace`

```text
Replace(Index: int32, Replacement: UMediaSource *) -> bool
```

Replace the media source at the specified position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | The index of the media source to replace. |
| `Replacement` | `UMediaSource *` | The replacement media source. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the media source was replaced, false otherwise. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMediaSoundComponent.json -->

# UMediaSoundComponent

Implements a sound component for playing a media player's audio output.

## Inheritance

`USynthComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Channels` | `EMediaSoundChannels` | Media sound channel type. |
| `MediaPlayer` | `UMediaPlayer *` | The media player asset associated with this component. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMediaSource.json -->

# UMediaSource

Abstract base class for media sources.
 
  Media sources describe the location andor settings of media objects that can
  be played in a media player, such as a video file on disk, a video stream on
  the internet, or a web cam attached to or built into the target device. The
  location is encoded as a media URL string, whose URI scheme and optional file
  extension will be used to locate a suitable media player.

## Inheritance

`UObject` -> `IMediaOptions`

## Functions

### `GetUrl`

```text
GetUrl() -> FString
```

Get the media source's URL string (must be implemented in child classes).

**Returns**

| Type | Description |
|---|---|
| `FString` | The media URL. |

### `Validate`

```text
Validate() -> bool
```

Validate the media source settings (must be implemented in child classes).

**Returns**

| Type | Description |
|---|---|
| `bool` | true if validation passed, false otherwise. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMediaTexture.json -->

# UMediaTexture

Implements a texture asset for rendering video tracks from UMediaPlayer assets.

## Inheritance

`UTexture`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AddressX` | `TEnumAsByte < TextureAddress >` | The addressing mode to use for the X axis. |
| `AddressY` | `TEnumAsByte < TextureAddress >` | The addressing mode to use for the Y axis. |
| `AutoClear` | `bool` | Whether to clear the texture when no media is being played (default = enabled). |
| `ClearColor` | `FLinearColor` | The color used to clear the texture if AutoClear is enabled (default = black). |
| `MediaPlayer` | `UMediaPlayer *` | The media player asset associated with this texture. |

## Functions

### `GetAspectRatio`

```text
GetAspectRatio() -> float
```

Gets the current aspect ratio of the texture.

**Returns**

| Type | Description |
|---|---|
| `float` | Texture aspect ratio. |

### `GetHeight`

```text
GetHeight() -> int32
```

Gets the current height of the texture.

**Returns**

| Type | Description |
|---|---|
| `int32` | Texture height (in pixels). |

### `GetWidth`

```text
GetWidth() -> int32
```

Gets the current width of the texture.

**Returns**

| Type | Description |
|---|---|
| `int32` | Texture width (in pixels). |

### `ResetFirstFrame`

```text
ResetFirstFrame() -> void
```

Reset The IsFirstFrameRender&IsFirstFrameNotify to false for iOS

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMenuAnchor.json -->

# UMenuAnchor

The Menu Anchor allows you to specify an location that a popup menu should be anchored to, 
  and should be summoned from.
   Single Child
   Popup

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MenuClass` | `TSubclassOf < UUserWidget >` | The widget class to spawn when the menu is required.  Creates the widget freshly each time.  <br>	  If you want to customize the creation of the popup, you should bind a function to OnGetMenuContentEvent <br>	  instead. |
| `OnGetMenuContentEvent` | `FGetWidget` | Called when the menu content is requested to allow a more customized handling over what to display |
| `Placement` | `TEnumAsByte < EMenuPlacement >` | The placement location of the summoned widget. |
| `ShouldDeferPaintingAfterWindowContent` | `bool` | - |
| `UseApplicationMenuStack` | `bool` | Does this menu behave like a normal stacked menu? Set it to false to control the menu's lifetime yourself. |

## Functions

### `ToggleOpen`

```text
ToggleOpen(bFocusOnOpen: bool) -> void
```

Toggles the menus open state.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bFocusOnOpen` | `bool` | Should we focus the popup as soon as it opens? |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Open`

```text
Open(bFocusMenu: bool) -> void
```

Opens the menu if it is not already open

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bFocusMenu` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Close`

```text
Close() -> void
```

Closes the menu if it is currently open.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsOpen`

```text
IsOpen() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the popup is open; false otherwise. |

### `ShouldOpenDueToClick`

```text
ShouldOpenDueToClick() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if we should open the menu due to a click. Sometimes we should not, if |

### `GetMenuPosition`

```text
GetMenuPosition() -> FVector2D
```

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | The current menu position |

### `HasOpenSubMenus`

```text
HasOpenSubMenus() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether this menu has open submenus |

## Delegates

### `OnMenuOpenChanged`

```text
OnMenuOpenChanged(bIsOpen: bool) -> void
```

Called when the opened state of the menu changes

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsOpen` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMeshComponent.json -->

# UMeshComponent

MeshComponent is an abstract base for any component that is an instance of a renderable collection of triangles.
 
  @see UStaticMeshComponent
  @see USkeletalMeshComponent

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OverrideMaterials` | `TArray < UMaterialInterface * >` | Per-Component material overrides.  These must NOT be set directly or a race condition can occur between GC and the rendering thread. |
| `OverlayMaterial` | `UMaterialInterface *` | Translucent material to blend on top of this mesh. Mesh will be rendered twice - once with a base material and once with overlay material |
| `IndexedOverlayMaterials` | `TArray < UMaterialInterface * >` | Overlay materials applied to each material slot. |
| `IndexedOverrideOutlineMaterials` | `TArray < UMaterialInterface * >` | Override overlay outline materials applied to each material slot. |
| `bUseIndexedOverlayMaterials` | `bool` | Whether to use IndexedOverlayMaterials (or OverlayMaterial). |
| `bUseOverlayMaterials` | `bool` | Whether to render overlay materials. (Indexed or not) |
| `OverlayMaterialMaxDrawDistance` | `float` | The max draw distance for overlay material. A distance of 0 indicates that overlay will be culled using primitive max distance. |
| `bIsEnableRetrieveDefaultMat` | `bool` | - |

## Functions

### `GetMaterials`

```text
GetMaterials() -> TArray < class UMaterialInterface * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < class UMaterialInterface * >` | - |

### `GetMaterialIndex`

```text
GetMaterialIndex(MaterialSlotName: FName) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MaterialSlotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetMaterialSlotNames`

```text
GetMaterialSlotNames() -> TArray < FName >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < FName >` | - |

### `IsMaterialSlotNameValid`

```text
IsMaterialSlotNameValid(MaterialSlotName: FName) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MaterialSlotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `EnableMeshClipPlane`

```text
EnableMeshClipPlane(ClipPlane: FPlane &, PlaneIndex: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ClipPlane` | `FPlane &` | - |
| `PlaneIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableMeshClipPlane`

```text
DisableMeshClipPlane(PlaneIndex: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlaneIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableMeshClipArc`

```text
EnableMeshClipArc(ClipPlane: FPlane &, ClipSphere: FVector4 &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ClipPlane` | `FPlane &` | - |
| `ClipSphere` | `FVector4 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableMeshClipArc`

```text
DisableMeshClipArc() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableMeshClip4Planes`

```text
EnableMeshClip4Planes(ClipPlanes: TArray < FPlane > &, bBox: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ClipPlanes` | `TArray < FPlane > &` | - |
| `bBox` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableMeshClip4Planes`

```text
DisableMeshClip4Planes() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOverlayMaterial`

```text
GetOverlayMaterial() -> UMaterialInterface *
```

Get the overlay material used by this instance

**Returns**

| Type | Description |
|---|---|
| `UMaterialInterface *` | - |

### `SetOverlayMaterial`

```text
SetOverlayMaterial(NewOverlayMaterial: UMaterialInterface *) -> void
```

Change the overlay material used by this instance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewOverlayMaterial` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetUseIndexedOverlayMaterials`

```text
GetUseIndexedOverlayMaterials() -> bool
```

Get UseIndexedOverlayMaterials

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetUseIndexedOverlayMaterials`

```text
SetUseIndexedOverlayMaterials(bNewUseIndexedOverlayMaterials: bool) -> void
```

Set UseIndexedOverlayMaterials

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewUseIndexedOverlayMaterials` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetUseOverlayMaterials`

```text
GetUseOverlayMaterials() -> bool
```

Get UseOverlayMaterials

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetUseOverlayMaterials`

```text
SetUseOverlayMaterials(bNewUseOverlayMaterials: bool) -> void
```

Set UseOverlayMaterials

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewUseOverlayMaterials` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetIndexedOverlayMaterials`

```text
GetIndexedOverlayMaterials() -> TArray < class UMaterialInterface * >
```

Get IndexedOverlayMaterials

**Returns**

| Type | Description |
|---|---|
| `TArray < class UMaterialInterface * >` | - |

### `SetIndexedOverlayMaterial`

```text
SetIndexedOverlayMaterial(ElementIndex: int32, Material: UMaterialInterface *) -> void
```

Set IndexedOverlayMaterials

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ElementIndex` | `int32` | - |
| `Material` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOverlayMaterialMaxDrawDistance`

```text
SetOverlayMaterialMaxDrawDistance(InMaxDrawDistance: float) -> void
```

Change the overlay material max draw distance used by this instance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMaxDrawDistance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetIndexedOverrideOutlineMaterials`

```text
GetIndexedOverrideOutlineMaterials() -> TArray < class UMaterialInterface * >
```

Get IndexedOverrideOutlineMaterials

**Returns**

| Type | Description |
|---|---|
| `TArray < class UMaterialInterface * >` | - |

### `SetIndexedOverrideOutlineMaterials`

```text
SetIndexedOverrideOutlineMaterials(ElementIndex: int32, Material: UMaterialInterface *) -> void
```

Set IndexedOverrideOutlineMaterials

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ElementIndex` | `int32` | - |
| `Material` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PrestreamTextures`

```text
PrestreamTextures(Seconds: float, bPrioritizeCharacterTextures: bool, CinematicTextureGroups: int32) -> void
```

Tell the streaming system to start loading all textures with all mip-levels.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Seconds` | `float` | Number of seconds to force all mip-levels to be resident |
| `bPrioritizeCharacterTextures` | `bool` | Whether character textures should be prioritized for a while by the streaming system |
| `CinematicTextureGroups` | `int32` | Bitfield indicating which texture groups that use extra high-resolution mips |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetScalarParameterValueOnMaterials`

```text
SetScalarParameterValueOnMaterials(ParameterName: FName, ParameterValue: float) -> void
```

Material parameter setting and caching 
	 Set all occurrences of Scalar Material Parameters with ParameterName in the set of materials of the SkeletalMesh to ParameterValue

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `ParameterValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVectorParameterValueOnMaterials`

```text
SetVectorParameterValueOnMaterials(ParameterName: FName, ParameterValue: FVector) -> void
```

Set all occurrences of Vector Material Parameters with ParameterName in the set of materials of the SkeletalMesh to ParameterValue

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `ParameterValue` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMeshSimplificationSettings.json -->

# UMeshSimplificationSettings

## Inheritance

`UDeveloperSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MeshReductionModuleName` | `FName` | Mesh reduction plugin to use when simplifying mesh geometry |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMeshVertexPainterKismetLibrary.json -->

# UMeshVertexPainterKismetLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `PaintVerticesSingleColor`

```text
PaintVerticesSingleColor(StaticMeshComponent: UStaticMeshComponent *, FillColor: FLinearColor &, bConvertToSRGB: bool) -> void
```

Paints vertex colors on a mesh component in a specified color.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StaticMeshComponent` | `UStaticMeshComponent *` | - |
| `FillColor` | `FLinearColor &` | - |
| `bConvertToSRGB` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PaintVerticesLerpAlongAxis`

```text
PaintVerticesLerpAlongAxis(StaticMeshComponent: UStaticMeshComponent *, StartColor: FLinearColor &, EndColor: FLinearColor &, Axis: EVertexPaintAxis, bConvertToSRGB: bool) -> void
```

Paints vertex colors on a mesh component lerping from the start to the end color along the specified axis.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StaticMeshComponent` | `UStaticMeshComponent *` | - |
| `StartColor` | `FLinearColor &` | - |
| `EndColor` | `FLinearColor &` | - |
| `Axis` | `EVertexPaintAxis` | - |
| `bConvertToSRGB` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemovePaintedVertices`

```text
RemovePaintedVertices(StaticMeshComponent: UStaticMeshComponent *) -> void
```

Removes vertex colors on a mesh component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StaticMeshComponent` | `UStaticMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMicroTransactionBase.json -->

# UMicroTransactionBase

## Inheritance

`UPlatformInterfaceBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AvailableProducts` | `TArray < struct FPurchaseInfo >` | The list of products available to purchase, filled out by the time a MTD_PurchaseQueryComplete is fired |
| `LastError` | `FString` | In case of errors, this will describe the most recent error |
| `LastErrorSolution` | `FString` | In case of errors, this will describe possible solutions (if there are any) |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UModelComponent.json -->

# UModelComponent

ModelComponents are PrimitiveComponents that represent elements of BSP geometry in a ULevel object.
  They are used exclusively by ULevel and are not intended as general-purpose components.
 
  @see ULevel

## Inheritance

`UPrimitiveComponent` -> `IInterface_CollisionDataProvider`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ModelBodySetup` | `UBodySetup *` | Description of collision |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMorphTarget.json -->

# UMorphTarget

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BaseSkelMesh` | `USkeletalMesh *` | USkeletalMesh that this vertex animation works on. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMouseCursorBinding.json -->

# UMouseCursorBinding

## Inheritance

`UPropertyBinding`

## Functions

### `GetValue`

```text
GetValue() -> EMouseCursor :: Type
```

**Returns**

| Type | Description |
|---|---|
| `EMouseCursor :: Type` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovementComponent.json -->

# UMovementComponent

MovementComponent is an abstract component class that defines functionality for moving a PrimitiveComponent (our UpdatedComponent) each tick.
  Base functionality includes:
     - Restricting movement to a plane or axis.
     - Utility functions for special handling of collision results (SlideAlongSurface(), ComputeSlideVector(), TwoWallAdjust()).
     - Utility functions for moving when there may be initial penetration (SafeMoveUpdatedComponent(), ResolvePenetration()).
     - Automatically registering the component tick and finding a component to move on the owning Actor.
  Normally the root component of the owning actor is moved, however another component may be selected (see SetUpdatedComponent()).
  During swept (non-teleporting) movement only collision of UpdatedComponent is considered, attached components will teleport to the end location ignoring collision.

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UpdatedComponent` | `USceneComponent *` | The component we move and update.<br>	  If this is null at startup and bAutoRegisterUpdatedComponent is true, the owning Actor's root component will automatically be set as our UpdatedComponent at startup.<br>	  @see bAutoRegisterUpdatedComponent, SetUpdatedComponent(), UpdatedPrimitive |
| `UpdatedPrimitive` | `UPrimitiveComponent *` | UpdatedComponent, cast as a UPrimitiveComponent. May be invalid if UpdatedComponent was null or not a UPrimitiveComponent. |
| `Velocity` | `FVector` | Current velocity of updated component. |
| `PlaneConstraintNormal` | `FVector` | The normal or axis of the plane that constrains movement, if bConstrainToPlane is enabled.<br>	  If for example you wanted to constrain movement to the X-Z plane (so that Y cannot change), the normal would be set to X=0 Y=1 Z=0.<br>	  This is recalculated whenever PlaneConstraintAxisSetting changes. It is normalized once the component is registered with the game world.<br>	  @see bConstrainToPlane, SetPlaneConstraintNormal(), SetPlaneConstraintFromVectors() |
| `PlaneConstraintOrigin` | `FVector` | The origin of the plane that constrains movement, if plane constraint is enabled. <br>	  This defines the behavior of snapping a position to the plane, such as by SnapUpdatedComponentToPlane().<br>	  @see bConstrainToPlane, SetPlaneConstraintOrigin(). |
| `bUpdateOnlyIfRendered` | `uint8` | If true, skips TickComponent() if UpdatedComponent was not recently rendered. |
| `bAutoUpdateTickRegistration` | `uint8` | If true, whenever the updated component is changed, this component will enable or disable its tick dependent on whether it has something to update.<br>	  This will NOT enable tick at startup if bAutoActivate is false, because presumably you have a good reason for not wanting it to start ticking initially. |
| `bTickBeforeOwner` | `uint8` | If true, after registration we will add a tick dependency to tick before our owner (if we can both tick).<br>	  This is important when our tick causes an update in the owner's position, so that when the owner ticks it uses the most recent position without lag.<br>	  Disabling this can improve performance if both objects tick but the order of ticks doesn't matter. |
| `bAutoRegisterUpdatedComponent` | `uint8` | If true, registers the owner's Root component as the UpdatedComponent if there is not one currently assigned. |
| `bConstrainToPlane` | `uint8` | If true, movement will be constrained to a plane.<br>	  @see PlaneConstraintNormal, PlaneConstraintOrigin, PlaneConstraintAxisSetting |
| `bSnapToPlaneAtStart` | `uint8` | If true and plane constraints are enabled, then the updated component will be snapped to the plane when first attached. |
| `bAutoRegisterPhysicsVolumeUpdates` | `uint8` | If true, then applies the value of bComponentShouldUpdatePhysicsVolume to the UpdatedComponent. If false, will not change bShouldUpdatePhysicsVolume on the UpdatedComponent at all.<br>	  @see bComponentShouldUpdatePhysicsVolume |
| `bComponentShouldUpdatePhysicsVolume` | `uint8` | If true, enables bShouldUpdatePhysicsVolume on the UpdatedComponent during initialization from SetUpdatedComponent(), otherwise disables such updates.<br>	  Only enabled if bAutoRegisterPhysicsVolumeUpdates is true.<br>	  WARNING: UpdatePhysicsVolume is potentially expensive if overlap events are also disabled because it requires a separate query against all physics volumes in the world. |
| `PlaneConstraintAxisSetting` | `EPlaneConstraintAxisSetting` | Setting that controls behavior when movement is restricted to a 2D plane defined by a specific axisnormal,<br>	  so that movement along the locked axis is not be possible.<br>	  @see SetPlaneConstraintAxisSetting |

## Functions

### `GetGravityZ`

```text
GetGravityZ() -> float
```

Returns gravity that affects this component

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetMaxSpeed`

```text
GetMaxSpeed() -> float
```

Returns maximum speed of component in current movement mode.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `K2_GetMaxSpeedModifier`

```text
K2_GetMaxSpeedModifier() -> float
```

Returns a scalar applied to the maximum velocity that the component can currently move.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `K2_GetModifiedMaxSpeed`

```text
K2_GetModifiedMaxSpeed() -> float
```

Returns the result of GetMaxSpeed()  GetMaxSpeedModifier().

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `IsExceedingMaxSpeed`

```text
IsExceedingMaxSpeed(MaxSpeed: float) -> bool
```

Returns true if the current velocity is exceeding the given max speed (usually the result of GetMaxSpeed()), within a small error tolerance.
	  Note that under normal circumstances updates cause by acceleration will not cause this to be true, however external forces or changes in the max speed limit
	  can cause the max speed to be violated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MaxSpeed` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `StopMovementImmediately`

```text
StopMovementImmediately() -> void
```

Stops movement immediately (zeroes velocity, usually zeros acceleration for components with acceleration).

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPhysicsVolume`

```text
GetPhysicsVolume() -> APhysicsVolume *
```

Returns the PhysicsVolume this MovementComponent is using, or the world's default physics volume if none.

**Returns**

| Type | Description |
|---|---|
| `APhysicsVolume *` | - |

### `PhysicsVolumeChanged`

```text
PhysicsVolumeChanged(NewVolume: APhysicsVolume *) -> void
```

Delegate when PhysicsVolume of UpdatedComponent has been changed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewVolume` | `APhysicsVolume *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetUpdatedComponent`

```text
SetUpdatedComponent(NewUpdatedComponent: USceneComponent *) -> void
```

Assign the component we move and update.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewUpdatedComponent` | `USceneComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_MoveUpdatedComponent`

```text
K2_MoveUpdatedComponent(Delta: FVector, NewRotation: FRotator, OutHit: FHitResult &, bSweep: bool, bTeleport: bool) -> bool
```

Moves our UpdatedComponent by the given Delta, and sets rotation to NewRotation.
	  Respects the plane constraint, if enabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delta` | `FVector` | - |
| `NewRotation` | `FRotator` | - |
| `OutHit` | `FHitResult &` | - |
| `bSweep` | `bool` | - |
| `bTeleport` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if some movement occurred, false if no movement occurred. Result of any impact will be stored in OutHit. |

### `SetPlaneConstraintAxisSetting`

```text
SetPlaneConstraintAxisSetting(NewAxisSetting: EPlaneConstraintAxisSetting) -> void
```

Set the plane constraint axis setting.
	  Changing this setting will modify the current value of PlaneConstraintNormal.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAxisSetting` | `EPlaneConstraintAxisSetting` | New plane constraint axis setting. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPlaneConstraintAxisSetting`

```text
GetPlaneConstraintAxisSetting() -> EPlaneConstraintAxisSetting
```

Get the plane constraint axis setting.

**Returns**

| Type | Description |
|---|---|
| `EPlaneConstraintAxisSetting` | - |

### `SetPlaneConstraintNormal`

```text
SetPlaneConstraintNormal(PlaneNormal: FVector) -> void
```

Sets the normal of the plane that constrains movement, enforced if the plane constraint is enabled.
	  Changing the normal automatically sets PlaneConstraintAxisSetting to "Custom".

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlaneNormal` | `FVector` | The normal of the plane. If non-zero in length, it will be normalized. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPlaneConstraintFromVectors`

```text
SetPlaneConstraintFromVectors(Forward: FVector, Up: FVector) -> void
```

Uses the Forward and Up vectors to compute the plane that constrains movement, enforced if the plane constraint is enabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Forward` | `FVector` | - |
| `Up` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPlaneConstraintOrigin`

```text
SetPlaneConstraintOrigin(PlaneOrigin: FVector) -> void
```

Sets the origin of the plane that constrains movement, enforced if the plane constraint is enabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlaneOrigin` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPlaneConstraintEnabled`

```text
SetPlaneConstraintEnabled(bEnabled: bool) -> void
```

Sets whether or not the plane constraint is enabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPlaneConstraintNormal`

```text
GetPlaneConstraintNormal() -> const FVector &
```

Returns the normal of the plane that constrains movement, enforced if the plane constraint is enabled.

**Returns**

| Type | Description |
|---|---|
| `const FVector &` | - |

### `GetPlaneConstraintOrigin`

```text
GetPlaneConstraintOrigin() -> const FVector &
```

Get the plane constraint origin. This defines the behavior of snapping a position to the plane, such as by SnapUpdatedComponentToPlane().

**Returns**

| Type | Description |
|---|---|
| `const FVector &` | The origin of the plane that constrains movement, if the plane constraint is enabled. |

### `ConstrainDirectionToPlane`

```text
ConstrainDirectionToPlane(Direction: FVector) -> FVector
```

Constrain a direction vector to the plane constraint, if enabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Direction` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `ConstrainLocationToPlane`

```text
ConstrainLocationToPlane(Location: FVector) -> FVector
```

Constrain a position vector to the plane constraint, if enabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Location` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `ConstrainNormalToPlane`

```text
ConstrainNormalToPlane(Normal: FVector) -> FVector
```

Constrain a normal vector (of unit length) to the plane constraint, if enabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Normal` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SnapUpdatedComponentToPlane`

```text
SnapUpdatedComponentToPlane() -> void
```

Snap the updated component to the plane constraint, if enabled.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMoviePlayerSettings.json -->

# UMoviePlayerSettings

Implements the settings for the Windows target platform.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bWaitForMoviesToComplete` | `bool` | If enabled, The game waits for startup movies to complete even if loading has finished. |
| `bMoviesAreSkippable` | `TArray < FString >` | If enabled, Startup movies can be skipped by the user when a mouse button is pressed. |
| `StartupMovies` | `TArray < FString >` | Movies to play on startup. Note that these must be in your game's GameContentMovies directory. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieScene.json -->

# UMovieScene

Implements a movie scene asset.

## Inheritance

`UMovieSceneSignedObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Spawnables` | `TArray < FMovieSceneSpawnable >` | Data-only blueprints for all of the objects that we we're able to spawn.<br>	  These describe objects and actors that we may instantiate at runtime,<br>	  or create proxy objects for previewing in the editor. |
| `Possessables` | `TArray < FMovieScenePossessable >` | Typed slots for already-spawned objects that we are able to control with this MovieScene |
| `ObjectBindings` | `TArray < FMovieSceneBinding >` | Tracks bound to possessed or spawned objects |
| `MasterTracks` | `TArray < UMovieSceneTrack * >` | Master tracks which are not bound to spawned or possessed objects |
| `CameraCutTrack` | `UMovieSceneTrack *` | The camera cut track is a specialized track for switching between cameras on a cinematic |
| `SelectionRange` | `FFloatRange` | User-defined selection range. |
| `PlaybackRange` | `FFloatRange` | User-defined playback range for this movie scene. Must be a finite range. Relative to this movie-scene's 0-time origin. |
| `bForceFixedFrameIntervalPlayback` | `bool` | - |
| `FixedFrameInterval` | `float` | - |
| `InTime_DEPRECATED` | `float` | - |
| `OutTime_DEPRECATED` | `float` | - |
| `StartTime_DEPRECATED` | `float` | - |
| `EndTime_DEPRECATED` | `float` | - |
| `EmptySections` | `TArray < UMovieSceneSection * >` | - |
| `bPlaybackRangeLocked` | `bool` | User-defined playback range is locked. |
| `ObjectsToDisplayNames` | `TMap < FString , FText >` | Maps object GUIDs to user defined display names. |
| `ObjectsToLabels` | `TMap < FString , FMovieSceneTrackLabels >` | Maps object GUIDs to user defined labels. |
| `EditorData` | `FMovieSceneEditorData` | Editor only data that needs to be saved between sessions for editing but has no runtime purpose |
| `RootFolders` | `TArray < UMovieSceneFolder * >` | The root folders for this movie scene. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieScene2DTransformSection.json -->

# UMovieScene2DTransformSection

A transform section

## Inheritance

`UMovieSceneSection` -> `IKeyframeSection<F2DTransformKey>`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Translation` | `FRichCurve` | Translation curves |
| `Rotation` | `FRichCurve` | Rotation curve |
| `Scale` | `FRichCurve` | Scale curves |
| `Shear` | `FRichCurve` | Shear curve |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieScene3DAttachSection.json -->

# UMovieScene3DAttachSection

A 3D Attach section

## Inheritance

`UMovieScene3DConstraintSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AttachSocketName` | `FName` | - |
| `AttachComponentName` | `FName` | - |
| `AttachmentLocationRule` | `EAttachmentRule` | - |
| `AttachmentRotationRule` | `EAttachmentRule` | - |
| `AttachmentScaleRule` | `EAttachmentRule` | - |
| `DetachmentLocationRule` | `EDetachmentRule` | - |
| `DetachmentRotationRule` | `EDetachmentRule` | - |
| `DetachmentScaleRule` | `EDetachmentRule` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieScene3DConstraintSection.json -->

# UMovieScene3DConstraintSection

Base class for 3D constraint section

## Inheritance

`UMovieSceneSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConstraintId` | `FGuid` | The possessable guid that this constraint uses |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieScene3DConstraintTrack.json -->

# UMovieScene3DConstraintTrack

Base class for constraint tracks (tracks that are dependent upon other objects).

## Inheritance

`UMovieSceneTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConstraintSections` | `TArray < UMovieSceneSection * >` | List of all constraint sections. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieScene3DPathSection.json -->

# UMovieScene3DPathSection

A 3D Path section

## Inheritance

`UMovieScene3DConstraintSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TimingCurve` | `FRichCurve` | Timing Curve |
| `FrontAxisEnum` | `MovieScene3DPathSection_Axis` | Front Axis |
| `UpAxisEnum` | `MovieScene3DPathSection_Axis` | Up Axis |
| `bFollow` | `uint32` | Follow Curve |
| `bReverse` | `uint32` | Reverse Timing |
| `bForceUpright` | `uint32` | Force Upright |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieScene3DTransformSection.json -->

# UMovieScene3DTransformSection

A 3D transform section

## Inheritance

`UMovieSceneSection` -> `IKeyframeSection<FTransformKey>`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TransformMask` | `FMovieSceneTransformMask` | - |
| `Translation` | `FRichCurve` | Translation curves |
| `Rotation` | `FRichCurve` | Rotation curves |
| `Scale` | `FRichCurve` | Scale curves |
| `ManualWeight` | `FRichCurve` | Manual weight curve |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneActorReferenceSection.json -->

# UMovieSceneActorReferenceSection

A single actor reference point section

## Inheritance

`UMovieSceneSection` -> `IKeyframeSection<FGuid>`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActorGuidIndexCurve` | `FIntegralCurve` | Curve data |
| `ActorGuidStrings` | `TArray < FString >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneAudioSection.json -->

# UMovieSceneAudioSection

Audio section, for use in the master audio, or by attached audio objects

## Inheritance

`UMovieSceneSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sound` | `USoundBase *` | The sound cue or wave that this section plays |
| `StartOffset` | `float` | The offset into the beginning of the audio clip |
| `AudioStartTime_DEPRECATED` | `float` | The absolute time that the sound starts playing at |
| `AudioDilationFactor_DEPRECATED` | `float` | The amount which this audio is time dilated by |
| `AudioVolume_DEPRECATED` | `float` | The volume the sound will be played with. |
| `SoundVolume` | `FRichCurve` | The volume the sound will be played with. |
| `PitchMultiplier` | `FRichCurve` | The pitch multiplier the sound will be played with. |
| `bSuppressSubtitles` | `bool` | - |
| `bOverrideAttenuation` | `bool` | Should the attenuation settings on this section be used. |
| `AttenuationSettings` | `USoundAttenuation *` | The attenuation settings to use. |
| `OnQueueSubtitles` | `FOnQueueSubtitles` | Called when subtitles are sent to the SubtitleManager.  Set this delegate if you want to hijack the subtitles for other purposes |
| `OnAudioFinished` | `FOnAudioFinished` | called when we finish playing audio, either because it played to completion or because a Stop() call turned it off early |
| `OnAudioPlaybackPercent` | `FOnAudioPlaybackPercent` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneAudioTrack.json -->

# UMovieSceneAudioTrack

Handles manipulation of audio.

## Inheritance

`UMovieSceneNameableTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AudioSections` | `TArray < UMovieSceneSection * >` | List of all master audio sections |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneBindingOverrides.json -->

# UMovieSceneBindingOverrides

A one-to-many definition of movie scene object binding IDs to overridden objects that should be bound to that binding.

## Inheritance

`UObject` -> `IMovieSceneBindingOverridesInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BindingData` | `TArray < FMovieSceneBindingOverrideData >` | The actual binding data |

## Functions

### `GetBindingData`

```text
GetBindingData() -> const TArray < FMovieSceneBindingOverrideData > &
```

**Returns**

| Type | Description |
|---|---|
| `const TArray < FMovieSceneBindingOverrideData > &` | - |

### `MakeBindingID`

```text
MakeBindingID(InBindingID: FGuid &, InSequenceID: FMovieSceneSequenceID, InSpace: EMovieSceneObjectBindingSpace) -> FMovieSceneObjectBindingID
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBindingID` | `FGuid &` | - |
| `InSequenceID` | `FMovieSceneSequenceID` | - |
| `InSpace` | `EMovieSceneObjectBindingSpace` | - |

**Returns**

| Type | Description |
|---|---|
| `FMovieSceneObjectBindingID` | - |

### `GetGuidStr`

```text
GetGuidStr(BindingID: FMovieSceneObjectBindingID &) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BindingID` | `FMovieSceneObjectBindingID &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneBoolSection.json -->

# UMovieSceneBoolSection

A single bool section.

## Inheritance

`UMovieSceneSection` -> `IKeyframeSection<bool>`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultValue_DEPRECATED` | `bool` | The default value to use when no keys are present - use GetCurve().SetDefaultValue() |
| `BoolCurve` | `FIntegralCurve` | Ordered curve data |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneBuiltInEasingFunction.json -->

# UMovieSceneBuiltInEasingFunction

## Inheritance

`UObject` -> `IMovieSceneEasingFunction`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Type` | `EMovieSceneBuiltInEasing` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneByteSection.json -->

# UMovieSceneByteSection

A single byte section.

## Inheritance

`UMovieSceneSection` -> `IKeyframeSection<uint8>`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ByteCurve` | `FIntegralCurve` | Ordered curve data |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneByteTrack.json -->

# UMovieSceneByteTrack

Handles manipulation of byte properties in a movie scene

## Inheritance

`UMovieScenePropertyTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Enum` | `UEnum *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneCameraAnimSection.json -->

# UMovieSceneCameraAnimSection

## Inheritance

`UMovieSceneSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AnimData` | `FMovieSceneCameraAnimSectionData` | - |
| `CameraAnim_DEPRECATED` | `UCameraAnim *` | Deprecated members |
| `PlayRate_DEPRECATED` | `float` | - |
| `PlayScale_DEPRECATED` | `float` | - |
| `BlendInTime_DEPRECATED` | `float` | - |
| `BlendOutTime_DEPRECATED` | `float` | - |
| `bLooping_DEPRECATED` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneCameraAnimTrack.json -->

# UMovieSceneCameraAnimTrack

## Inheritance

`UMovieSceneNameableTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CameraAnimSections` | `TArray < UMovieSceneSection * >` | List of all sections |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneCameraCutSection.json -->

# UMovieSceneCameraCutSection

Movie CameraCuts are sections on the CameraCuts track, that show what the viewer "sees"

## Inheritance

`UMovieSceneSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CameraGuid` | `FGuid` | The camera possessable or spawnable that this movie CameraCut uses |
| `BlendInTime` | `float` | - |
| `BlendInType` | `EMovieSceneBuiltInEasing` | - |
| `BlendOutTime` | `float` | - |
| `BlendOutType` | `EMovieSceneBuiltInEasing` | - |
| `bUseAutoFixupConsecutive` | `bool` | - |
| `bLockControlRotation` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneCameraCutTrack.json -->

# UMovieSceneCameraCutTrack

Handles manipulation of CameraCut properties in a movie scene.

## Inheritance

`UMovieSceneNameableTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bUseFixupConsecutive` | `bool` | - |
| `Sections` | `TArray < UMovieSceneSection * >` | All movie scene sections. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneCameraShakeSection.json -->

# UMovieSceneCameraShakeSection

## Inheritance

`UMovieSceneSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ShakeData` | `FMovieSceneCameraShakeSectionData` | - |
| `ShakeClass_DEPRECATED` | `TSubclassOf < UCameraShake >` | - |
| `PlayScale_DEPRECATED` | `float` | - |
| `PlaySpace_DEPRECATED` | `TEnumAsByte < ECameraAnimPlaySpace :: Type >` | - |
| `UserDefinedPlaySpace_DEPRECATED` | `FRotator` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneCameraShakeTrack.json -->

# UMovieSceneCameraShakeTrack

## Inheritance

`UMovieSceneNameableTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CameraShakeSections` | `TArray < UMovieSceneSection * >` | List of all sections |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneCapture.json -->

# UMovieSceneCapture

Class responsible for capturing scene data

## Inheritance

`UObject` -> `IMovieSceneCaptureInterface` -> `ICaptureProtocolHost`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CaptureType` | `FCaptureProtocolID` | The type of capture protocol to use |
| `ProtocolSettings` | `UMovieSceneCaptureProtocolSettings *` | Settings specific to the capture protocol |
| `Settings` | `FMovieSceneCaptureSettings` | Settings that define how to capture |
| `bUseSeparateProcess` | `bool` | Whether to capture the movie in a separate process or not |
| `bCloseEditorWhenCaptureStarts` | `bool` | When enabled, the editor will shutdown when the capture starts |
| `AdditionalCommandLineArguments` | `FString` | Additional command line arguments to pass to the external process when capturing |
| `InheritedCommandLineArguments` | `FString` | Command line arguments inherited from this process |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneCaptureEnvironment.json -->

# UMovieSceneCaptureEnvironment

## Inheritance

`UObject`

## Functions

### `GetCaptureFrameNumber`

```text
GetCaptureFrameNumber() -> int32
```

Get the frame number of the current capture

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetCaptureElapsedTime`

```text
GetCaptureElapsedTime() -> float
```

Get the total elapsed time of the current capture in seconds

**Returns**

| Type | Description |
|---|---|
| `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneCinematicShotSection.json -->

# UMovieSceneCinematicShotSection

Implements a cinematic shot section.

## Inheritance

`UMovieSceneSubSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DisplayName` | `FText` | The Shot's display name |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneColorSection.json -->

# UMovieSceneColorSection

A single floating point section

## Inheritance

`UMovieSceneSection` -> `IKeyframeSection<FColorKey>`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RedCurve` | `FRichCurve` | Red curve data |
| `GreenCurve` | `FRichCurve` | Green curve data |
| `BlueCurve` | `FRichCurve` | Blue curve data |
| `AlphaCurve` | `FRichCurve` | Alpha curve data |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneColorTrack.json -->

# UMovieSceneColorTrack

Handles manipulation of float properties in a movie scene

## Inheritance

`UMovieScenePropertyTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bIsSlateColor_DEPRECATED` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneComponentMaterialTrack.json -->

# UMovieSceneComponentMaterialTrack

A material track which is specialized for animation materials which are owned by actor components.

## Inheritance

`UMovieSceneMaterialTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaterialIndex` | `int32` | The index of this material this track is animating. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneEasingExternalCurve.json -->

# UMovieSceneEasingExternalCurve

## Inheritance

`UObject` -> `IMovieSceneEasingFunction`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Curve` | `UCurveFloat *` | Curve data |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneEnumSection.json -->

# UMovieSceneEnumSection

A single enum section.

## Inheritance

`UMovieSceneSection` -> `IKeyframeSectionEnum`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EnumCurve` | `FIntegralCurve` | Ordered curve data |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneEnumTrack.json -->

# UMovieSceneEnumTrack

Handles manipulation of byte properties in a movie scene

## Inheritance

`UMovieScenePropertyTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Enum` | `UEnum *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneEventRepeaterSection.json -->

# UMovieSceneEventRepeaterSection

NewEvent section that will trigger its NewEvent exactly once, every time it is evaluated.

## Inheritance

`UMovieSceneNewEventSectionBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Event` | `FMovieSceneEventWrapper` | The NewEvent that should be triggered each time this section is evaluated |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneEventSection.json -->

# UMovieSceneEventSection

Implements a section in movie scene event tracks.

## Inheritance

`UMovieSceneSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Events_DEPRECATED` | `FNameCurve` | - |
| `EventData` | `FMovieSceneEventSectionData` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneEventTimelinessSection.json -->

# UMovieSceneEventTimelinessSection

## Inheritance

`UMovieSceneNewEventSectionBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Events` | `TArray < FMovieSceneEventWrapper >` | Array of values that correspond to each key time <br>		 The NewEvent that should be triggered each time this section is evaluated |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneEventTrack.json -->

# UMovieSceneEventTrack

Implements a movie scene track that triggers discrete events during playback.

## Inheritance

`UMovieSceneNameableTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bFireEventsWhenForwards` | `uint32` | If events should be fired when passed playing the sequence forwards. |
| `bFireEventsWhenBackwards` | `uint32` | If events should be fired when passed playing the sequence backwards. |
| `EventPosition` | `EFireEventsAtPosition` | Defines where in the evaluation to trigger events |
| `EventReceivers` | `TArray < FMovieSceneObjectBindingID >` | Defines a list of object bindings on which to trigger the events in this track. When empty, events will trigger in the default event contexts for the playback environment (such as the level blueprint, or widget). |
| `Sections` | `TArray < UMovieSceneSection * >` | The track's sections. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneEventTriggerSection.json -->

# UMovieSceneEventTriggerSection

NewEvent section that triggeres specific timed NewEvents.

## Inheritance

`UMovieSceneNewEventSectionBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `KeyTimes` | `TArray < float >` | Array of times for each key |
| `KeyValues` | `TArray < FMovieSceneEventWrapper >` | Array of values that correspond to each key time |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneFadeSection.json -->

# UMovieSceneFadeSection

A single floating point section.

## Inheritance

`UMovieSceneFloatSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FadeColor` | `FLinearColor` | Fade color. |
| `bFadeAudio` | `uint32` | Fade audio. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneFloatSection.json -->

# UMovieSceneFloatSection

A single floating point section

## Inheritance

`UMovieSceneSection` -> `IKeyframeSection<float>`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FloatCurve` | `FRichCurve` | Curve data |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneFolder.json -->

# UMovieSceneFolder

Reprents a folder used for organizing objects in tracks in a movie scene.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FolderName` | `FName` | The name of this folder. |
| `ChildFolders` | `TArray < UMovieSceneFolder * >` | The folders contained by this folder. |
| `ChildMasterTracks` | `TArray < UMovieSceneTrack * >` | The master tracks contained by this folder. |
| `ChildObjectBindingStrings` | `TArray < FString >` | The guid strings used to serialize the guids for the object bindings contained by this folder. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneIntegerSection.json -->

# UMovieSceneIntegerSection

A single integer section.

## Inheritance

`UMovieSceneSection` -> `IKeyframeSection<int32>`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `IntegerCurve` | `FIntegralCurve` | Ordered curve data |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneLevelVisibilitySection.json -->

# UMovieSceneLevelVisibilitySection

A section for use with the movie scene level visibility track, which controls streamed level visibility.

## Inheritance

`UMovieSceneSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Visibility` | `ELevelVisibility` | Whether or not the levels in this section should be visible or hidden. |
| `LevelNames` | `TArray < FName >` | The short names of the levels who's visibility is controlled by this section. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneLevelVisibilityTrack.json -->

# UMovieSceneLevelVisibilityTrack

A track for controlling the visibility of streamed levels.

## Inheritance

`UMovieSceneNameableTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sections` | `TArray < UMovieSceneSection * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneMarginSection.json -->

# UMovieSceneMarginSection

A section in a Margin track

## Inheritance

`UMovieSceneSection` -> `IKeyframeSection<FMarginKey>`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TopCurve` | `FRichCurve` | Red curve data |
| `LeftCurve` | `FRichCurve` | Green curve data |
| `RightCurve` | `FRichCurve` | Blue curve data |
| `BottomCurve` | `FRichCurve` | Alpha curve data |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneMaterialParameterCollectionTrack.json -->

# UMovieSceneMaterialParameterCollectionTrack

Handles manipulation of material parameter collections in a movie scene.

## Inheritance

`UMovieSceneMaterialTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MPC` | `UMaterialParameterCollection *` | The material parameter collection to manipulate |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneMaterialTrack.json -->

# UMovieSceneMaterialTrack

Handles manipulation of material parameters in a movie scene.

## Inheritance

`UMovieSceneNameableTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sections` | `TArray < UMovieSceneSection * >` | The sections owned by this track . |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneNewEventTrack.json -->

# UMovieSceneNewEventTrack

Implements a movie scene track that triggers discrete events during playback.

## Inheritance

`UMovieSceneNameableTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bFireEventsWhenForwards` | `uint32` | If events should be fired when passed playing the sequence forwards. |
| `bFireEventsWhenBackwards` | `uint32` | If events should be fired when passed playing the sequence backwards. |
| `EventPosition` | `EFireEventsAtPosition` | Defines where in the evaluation to trigger events |
| `Sections` | `TArray < UMovieSceneSection * >` | The track's sections. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneParameterSection.json -->

# UMovieSceneParameterSection

A single movie scene section which can contain data for multiple named parameters.

## Inheritance

`UMovieSceneSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ScalarParameterNamesAndCurves` | `TArray < FScalarParameterNameAndCurve >` | The scalar parameter names and their associated curves. |
| `VectorParameterNamesAndCurves` | `TArray < FVectorParameterNameAndCurves >` | The vector parameter names and their associated curves. |
| `ColorParameterNamesAndCurves` | `TArray < FColorParameterNameAndCurves >` | The vector parameter names and their associated curves. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneParticleParameterTrack.json -->

# UMovieSceneParticleParameterTrack

Handles manipulation of material parameters in a movie scene.

## Inheritance

`UMovieSceneNameableTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sections` | `TArray < UMovieSceneSection * >` | The sections owned by this track . |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneParticleSection.json -->

# UMovieSceneParticleSection

Particle section, for particle toggling and triggering.

## Inheritance

`UMovieSceneSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParticleKeys` | `FIntegralCurve` | Curve containing the particle keys. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneParticleTrack.json -->

# UMovieSceneParticleTrack

Handles triggering of particle emitters

## Inheritance

`UMovieSceneNameableTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParticleSections` | `TArray < UMovieSceneSection * >` | List of all particle sections. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieScenePropertyTrack.json -->

# UMovieScenePropertyTrack

Base class for tracks that animate an object property

## Inheritance

`UMovieSceneNameableTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PropertyName` | `FName` | Name of the property being changed |
| `PropertyPath` | `FString` | Path to the property from the source object being changed |
| `Sections` | `TArray < UMovieSceneSection * >` | All the sections in this list |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSection.json -->

# UMovieSceneSection

Base class for movie scene sections

## Inheritance

`UMovieSceneSignedObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EvalOptions` | `FMovieSceneSectionEvalOptions` | - |
| `Easing` | `FMovieSceneEasingSettings` | - |
| `StartTime` | `float` | The start time of the section |
| `EndTime` | `float` | The end time of the section |
| `RowIndex` | `int32` | The row index that this section sits on |
| `OverlapPriority` | `int32` | This section's priority over overlapping sections |
| `bIsActive` | `uint32` | Toggle whether this section is activeinactive |
| `bIsLocked` | `uint32` | Toggle whether this section is lockedunlocked |
| `bIsInfinite` | `uint32` | Toggle to set this section to be infinite |
| `PreRollTime` | `float` | The amount of time to prepare this section for evaluation before it actually starts. |
| `PostRollTime` | `float` | The amount of time to continue 'postrolling' this section for after evaluation has ended. |
| `BlendType` | `FOptionalMovieSceneBlendType` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSequence.json -->

# UMovieSceneSequence

Abstract base class for movie scene animations (C++ version).

## Inheritance

`UMovieSceneSignedObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EvaluationTemplate` | `FCachedMovieSceneEvaluationTemplate` | - |
| `TemplateParameters` | `FMovieSceneTrackCompilationParams` | - |
| `InstancedSubSequenceEvaluationTemplates` | `TMap < UObject * , FCachedMovieSceneEvaluationTemplate >` | - |
| `bParentContextsAreSignificant` | `bool` | true if the result of GetParentObject is significant in object resolution for LocateBoundObjects.<br>	  When true, if GetParentObject returns nullptr, the PlaybackContext will be used for LocateBoundObjects, other wise the object's parent will be used<br>	  When false, the PlaybackContext will always be used for LocateBoundObjects |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSequencePlayer.json -->

# UMovieSceneSequencePlayer

Abstract class that provides consistent player behaviour for various animation players

## Inheritance

`UObject` -> `IMovieScenePlayer`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Status` | `TEnumAsByte < EMovieScenePlayerStatus :: Type >` | Movie player status. |
| `bReversePlayback` | `uint32` | Whether we're currently playing in reverse. |
| `bPendingFirstUpdate` | `uint32` | True where we're waiting for the first update of the sequence after calling StartPlayingNextTick. |
| `Sequence` | `UMovieSceneSequence *` | The sequence to play back |
| `TimeCursorPosition` | `float` | The current time cursor position within the sequence (in seconds) |
| `StartTime` | `float` | Time time at which to start playing the sequence (defaults to the lower bound of the sequence's play range) |
| `EndTime` | `float` | Time time at which to end playing the sequence (defaults to the upper bound of the sequence's play range) |
| `CurrentNumLoops` | `int32` | The number of times we have looped in the current playback |
| `PlaybackSettings` | `FMovieSceneSequencePlaybackSettings` | Specific playback settings for the animation. |
| `RootTemplateInstance` | `FMovieSceneRootEvaluationTemplateInstance` | The root template instance we're evaluating |

## Functions

### `Play`

```text
Play() -> void
```

Start playback forwards from the current time cursor position, using the current play rate.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlayReverse`

```text
PlayReverse() -> void
```

Reverse playback.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ChangePlaybackDirection`

```text
ChangePlaybackDirection() -> void
```

Changes the direction of playback (go in reverse if it was going forward, or vice versa)

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SeekPosition`

```text
SeekPosition(NewTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlayLooping`

```text
PlayLooping(NumLoops: int32) -> void
```

Start playback from the current time cursor position, looping the specified number of times.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NumLoops` | `int32` | - The number of loops to play. -1 indicates infinite looping. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StartPlayingNextTick`

```text
StartPlayingNextTick() -> void
```

Start playback from the current time cursor position, using the current play rate. Does not update the animation until next tick.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Pause`

```text
Pause() -> void
```

Pause playback.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Scrub`

```text
Scrub() -> void
```

Scrub playback.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Stop`

```text
Stop() -> void
```

Stop playback.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GoToEndAndStop`

```text
GoToEndAndStop() -> void
```

Go to end and stop.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPlaybackPosition`

```text
GetPlaybackPosition() -> float
```

Get the current playback position

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetPlaybackPosition`

```text
SetPlaybackPosition(NewPlaybackPosition: float) -> void
```

Set the current playback position

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlaybackPosition` | `float` | - The new playback position to set. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPlaybackPostionWithloop`

```text
SetPlaybackPostionWithloop(NewTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTargetTimePostionWithloop`

```text
GetTargetTimePostionWithloop(NewTime: float) -> float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `JumpToPosition`

```text
JumpToPosition(NewPlaybackPosition: float) -> void
```

Jump to new playback position

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlaybackPosition` | `float` | - The new playback position to set. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `JumpToPositionEx`

```text
JumpToPositionEx(NewPlaybackPosition: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlaybackPosition` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsPlaying`

```text
IsPlaying() -> bool
```

Check whether the sequence is actively playing.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsPaused`

```text
IsPaused() -> bool
```

Check whether the sequence is paused.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetLength`

```text
GetLength() -> float
```

Get the playback length of the sequence

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetPlayRate`

```text
GetPlayRate() -> float
```

Get the playback rate of this player.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `IsEvaluating`

```text
IsEvaluating() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetPlayRate`

```text
SetPlayRate(PlayRate: float) -> void
```

Set the playback rate of this player. Negative values will play the animation in reverse.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayRate` | `float` | - The new rate of playback for the animation. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPlayLoopCount`

```text
SetPlayLoopCount(NumLoops: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NumLoops` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPlaybackRange`

```text
SetPlaybackRange(NewStartTime: float, NewEndTime: float) -> void
```

Sets the range in time to be played back by this player, overriding the default range stored in the asset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewStartTime` | `float` | The new starting time for playback |
| `NewEndTime` | `float` | The new ending time for playback. Must be larger than the start time. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPlaybackStart`

```text
GetPlaybackStart() -> float
```

Get the offset within the level sequence to start playing

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetPlaybackStartSeconds`

```text
GetPlaybackStartSeconds() -> float
```

Get the offset seconds within the level sequence to start playing

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetPlaybackEnd`

```text
GetPlaybackEnd() -> float
```

Get the offset within the level sequence to finish playing

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetPlaybackEndSeconds`

```text
GetPlaybackEndSeconds() -> float
```

Get the offset seconds within the level sequence to finish playing

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetBoundObjects`

```text
GetBoundObjects(ObjectBinding: FMovieSceneObjectBindingID) -> TArray < UObject * >
```

Retrieve all objects currently bound to the specified binding identifier

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ObjectBinding` | `FMovieSceneObjectBindingID` | - |

**Returns**

| Type | Description |
|---|---|
| `TArray < UObject * >` | - |

## Delegates

### `OnPlay`

```text
OnPlay() -> void
```

Event triggered when the level sequence player is played

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPlayReverse`

```text
OnPlayReverse() -> void
```

Event triggered when the level sequence player is played in reverse

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnStop`

```text
OnStop() -> void
```

Event triggered when the level sequence player is stopped

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPause`

```text
OnPause() -> void
```

Event triggered when the level sequence player is paused

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnFinished`

```text
OnFinished() -> void
```

Event triggered when the level sequence player finishes naturally (without explicitly calling stop)

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnObjectSpawnedEvent`

```text
OnObjectSpawnedEvent(InObject: UObject*, InBindingID: const FGuid&, InSequenceID: FMovieSceneSequenceID) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObject` | `UObject*` | - |
| `InBindingID` | `const FGuid&` | - |
| `InSequenceID` | `FMovieSceneSequenceID` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSignedObject.json -->

# UMovieSceneSignedObject

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Signature` | `FGuid` | Unique generation signature |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSkeletalAnimationSection.json -->

# UMovieSceneSkeletalAnimationSection

Movie scene section that control skeletal animation

## Inheritance

`UMovieSceneSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Params` | `FMovieSceneSkeletalAnimationParams` | - |
| `AnimSequence_DEPRECATED` | `UAnimSequence *` | - |
| `Animation_DEPRECATED` | `UAnimSequenceBase *` | - |
| `StartOffset_DEPRECATED` | `float` | - |
| `EndOffset_DEPRECATED` | `float` | - |
| `PlayRate_DEPRECATED` | `float` | - |
| `bReverse_DEPRECATED` | `uint32` | - |
| `bClearPose_DEPRECATED` | `uint32` | - |
| `bForceUseTPP_DEPRECATED` | `uint32` | - |
| `bSetSequenceEvalReinitStartPosition_DEPRECATED` | `uint32` | - |
| `SlotName_DEPRECATED` | `FName` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSkeletalAnimationTrack.json -->

# UMovieSceneSkeletalAnimationTrack

Handles animation of skeletal mesh actors

## Inheritance

`UMovieSceneNameableTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AnimationSections` | `TArray < UMovieSceneSection * >` | List of all animation sections |
| `bUseLegacySectionIndexBlend` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSpawnTrack.json -->

# UMovieSceneSpawnTrack

Handles when a spawnable should be spawned and destroyed

## Inheritance

`UMovieSceneTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sections` | `TArray < UMovieSceneSection * >` | All the sections in this track |
| `ObjectGuid` | `FGuid` | The guid relating to the object we are to spawn and destroy |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSplineSection.json -->

# UMovieSceneSplineSection

A single floating point section.

## Inheritance

`UMovieSceneFloatSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Guid` | `FGuid` | - |
| `DisplayName` | `FText` | - |
| `bUseLocation` | `bool` | - |
| `bUseRotation` | `bool` | - |
| `bUseScale` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneStringSection.json -->

# UMovieSceneStringSection

A single string section

## Inheritance

`UMovieSceneSection` -> `IKeyframeSection<FString>`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StringCurve` | `FStringCurve` | Curve data |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSubSection.json -->

# UMovieSceneSubSection

Implements a section in sub-sequence tracks.

## Inheritance

`UMovieSceneSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Parameters` | `FMovieSceneSectionParameters` | - |
| `StartOffset_DEPRECATED` | `float` | - |
| `TimeScale_DEPRECATED` | `float` | - |
| `PrerollTime_DEPRECATED` | `float` | - |
| `SubSequence` | `UMovieSceneSequence *` | Movie scene being played by this section.<br>	 <br>	  @todo Sequencer: Should this be lazy loaded? |
| `ActorToRecord` | `TLazyObjectPtr < AActor >` | Target actor to record |
| `TargetSequenceName` | `FString` | Target name of sequence to try to record to (will record automatically to another if this already exists) |
| `TargetPathToRecordTo` | `FDirectoryPath` | Target path of sequence to record to |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSubtitleSection.json -->

# UMovieSceneSubtitleSection

A single floating point section.

## Inheritance

`UMovieSceneSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Params` | `FMovieSceneSubtitleParams` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSubtitleTrack.json -->

# UMovieSceneSubtitleTrack

Handles manipulation of float properties in a movie scene

## Inheritance

`UMovieSceneNameableTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sections` | `TArray < UMovieSceneSection * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSubTrack.json -->

# UMovieSceneSubTrack

A track that holds sub-sequences within a larger sequence.

## Inheritance

`UMovieSceneNameableTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sections` | `TArray < UMovieSceneSection * >` | All movie scene sections. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneTrack.json -->

# UMovieSceneTrack

Base class for a track in a Movie Scene

## Inheritance

`UMovieSceneSignedObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EvalOptions` | `FMovieSceneTrackEvalOptions` | General evaluation options for a given track |
| `EvaluationRunSide` | `int32` | - |
| `MinRunnableTCQuality` | `int32` | - |
| `SavedTrackTags` | `TArray < FString >` | - |
| `TrackTags` | `TArray < TSharedRef < FString > >` | - |
| `TrackTint` | `FColor` | This track's tint color |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneVectorSection.json -->

# UMovieSceneVectorSection

A vector section.

## Inheritance

`UMovieSceneSection` -> `IKeyframeSection<FVectorKey>`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Curves` | `FRichCurve` | Vector t |
| `ChannelsUsed` | `int32` | How many curves are actually used |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneVectorTrack.json -->

# UMovieSceneVectorTrack

Handles manipulation of component transforms in a movie scene

## Inheritance

`UMovieScenePropertyTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NumChannelsUsed` | `int32` | The number of channels used by the vector (2,3, or 4) |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneWidgetMaterialTrack.json -->

# UMovieSceneWidgetMaterialTrack

A material track which is specialized for materials which are owned by widget brushes.

## Inheritance

`UMovieSceneMaterialTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BrushPropertyNamePath` | `TArray < FName >` | The name of the brush property which will be animated by this track. |
| `TrackName` | `FName` | The name of this track, generated from the property name path. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMultiBillBoardComponent.json -->

# UMultiBillBoardComponent

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Elements` | `TArray < FBillBoardMaterialSpriteElement >` | Current array of material billboard elements |
| `BillboardDatas` | `TArray < FBillboardData >` | - |

## Functions

### `GetElements`

```text
GetElements() -> const TArray < FBillBoardMaterialSpriteElement > &
```

**Returns**

| Type | Description |
|---|---|
| `const TArray < FBillBoardMaterialSpriteElement > &` | - |

### `SetElements`

```text
SetElements(NewElements: TArray < FBillBoardMaterialSpriteElement > &) -> void
```

Set all elements of this material billboard component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewElements` | `TArray < FBillBoardMaterialSpriteElement > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddElement`

```text
AddElement(Material: UMaterialInterface *, DistanceToOpacityCurve: UCurveFloat *, bSizeIsInScreenSpace: bool, BaseSizeX: float, BaseSizeY: float, DistanceToSizeCurve: UCurveFloat *) -> void
```

Adds an element to the sprite.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Material` | `UMaterialInterface *` | - |
| `DistanceToOpacityCurve` | `UCurveFloat *` | - |
| `bSizeIsInScreenSpace` | `bool` | - |
| `BaseSizeX` | `float` | - |
| `BaseSizeY` | `float` | - |
| `DistanceToSizeCurve` | `UCurveFloat *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddBillBoard`

```text
K2_AddBillBoard(NewLocation: FVector, UV0: FVector2D, UV1: FVector2D) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector` | - |
| `UV0` | `FVector2D` | - |
| `UV1` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `RemoveBillboard`

```text
RemoveBillboard(ID: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ID` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearAllBillBoards`

```text
ClearAllBillBoards() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBillboardUV`

```text
SetBillboardUV(ID: int32, UV0: FVector2D, UV1: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ID` | `int32` | - |
| `UV0` | `FVector2D` | - |
| `UV1` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CreateMultiBillboardComponent`

```text
CreateMultiBillboardComponent(WorldContextObject: UObject *, MultiBillboardClass: TSubclassOf < UMultiBillBoardComponent >) -> UMultiBillBoardComponent *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `MultiBillboardClass` | `TSubclassOf < UMultiBillBoardComponent >` | - |

**Returns**

| Type | Description |
|---|---|
| `UMultiBillBoardComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMultiLineEditableText.json -->

# UMultiLineEditableText

Editable text box widget

## Inheritance

`UTextLayoutWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Text` | `FText` | The text content for this editable text box widget |
| `HintText` | `FText` | Hint text that appears when there is no text in the text box |
| `HintTextDelegate` | `FGetText` | A bindable delegate to allow logic to drive the hint text of the widget |
| `WidgetStyle` | `FTextBlockStyle` | The style |
| `bIsReadOnly` | `bool` | Sets whether this text block can be modified interactively by the user |
| `Font_DEPRECATED` | `FSlateFontInfo` | Font color and opacity (overrides Style) |
| `AllowContextMenu` | `bool` | Whether the context menu can be opened |
| `UseModiferKeyForNewLine` | `bool` | - |

## Functions

### `GetText`

```text
GetText() -> FText
```

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `SetText`

```text
SetText(InText: FText) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHintText`

```text
SetHintText(InHintText: FText) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InHintText` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIsReadOnly`

```text
SetIsReadOnly(bReadOnly: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bReadOnly` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWidgetStyle`

```text
SetWidgetStyle(InWidgetStyle: FTextBlockStyle &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InWidgetStyle` | `FTextBlockStyle &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetModiferKeyForNewLine`

```text
SetModiferKeyForNewLine(bReadOnly: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bReadOnly` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWrapTextAt`

```text
SetWrapTextAt(InWrapTextAt: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InWrapTextAt` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFont`

```text
SetFont(InFontInfo: FSlateFontInfo) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFontInfo` | `FSlateFontInfo` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetColorAndOpacity`

```text
SetColorAndOpacity(Color: FSlateColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Color` | `FSlateColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnTextChanged`

```text
OnTextChanged(Text: const FText&) -> void
```

Called whenever the text is changed interactively by the user

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Text` | `const FText&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTextCommitted`

```text
OnTextCommitted(Text: const FText&, CommitMethod: ETextCommit::Type) -> void
```

Called whenever the text is committed.  This happens when the user presses enter or the text box loses focus.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Text` | `const FText&` | - |
| `CommitMethod` | `ETextCommit::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTextBeginEditTransation`

```text
OnTextBeginEditTransation() -> void
```

Called to begin an undoable editable text transaction

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTextEndEditTransaction`

```text
OnTextEndEditTransaction(Text: const FText&) -> void
```

Called to end an undoable editable text transaction

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Text` | `const FText&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTextFocusReceived`

```text
OnTextFocusReceived() -> void
```

Called when editable text received focus

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMultiLineEditableTextBox.json -->

# UMultiLineEditableTextBox

Allows a user to enter multiple lines of text

## Inheritance

`UTextLayoutWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Text` | `FText` | The text content for this editable text box widget |
| `HintText` | `FText` | Hint text that appears when there is no text in the text box |
| `HintTextDelegate` | `FGetText` | A bindable delegate to allow logic to drive the hint text of the widget |
| `WidgetStyle` | `FEditableTextBoxStyle` | The style |
| `TextStyle` | `FTextBlockStyle` | The text style |
| `bIsReadOnly` | `bool` | Sets whether this text block can be modified interactively by the user |
| `AllowContextMenu` | `bool` | Whether the context menu can be opened |
| `Style_DEPRECATED` | `USlateWidgetStyleAsset *` | - |
| `Font_DEPRECATED` | `FSlateFontInfo` | Font color and opacity (overrides Style) |
| `ForegroundColor_DEPRECATED` | `FLinearColor` | Text color and opacity (overrides Style) |
| `BackgroundColor_DEPRECATED` | `FLinearColor` | The color of the backgroundborder around the editable text (overrides Style) |
| `ReadOnlyForegroundColor_DEPRECATED` | `FLinearColor` | Text color and opacity when read-only (overrides Style) |

## Functions

### `GetText`

```text
GetText() -> FText
```

Provide a alternative mechanism for error reporting.

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `SetText`

```text
SetText(InText: FText) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHintText`

```text
SetHintText(InText: FText) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetError`

```text
SetError(InError: FText) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InError` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIsReadOnly`

```text
SetIsReadOnly(bReadOnly: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bReadOnly` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIsEnableMultiLineTextInsertNewLine`

```text
SetIsEnableMultiLineTextInsertNewLine(bEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnTextChanged`

```text
OnTextChanged(Text: const FText&) -> void
```

Called whenever the text is changed interactively by the user

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Text` | `const FText&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTextCommitted`

```text
OnTextCommitted(Text: const FText&, CommitMethod: ETextCommit::Type) -> void
```

Called whenever the text is committed.  This happens when the user presses enter or the text box loses focus.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Text` | `const FText&` | - |
| `CommitMethod` | `ETextCommit::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNavArea.json -->

# UNavArea

Class containing definition of a navigation area

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultCost` | `float` | travel cost multiplier for path distance |
| `FixedAreaEnteringCost` | `float` | entering cost |
| `DrawColor` | `FColor` | area color in navigation view |
| `SupportedAgents` | `FNavAgentSelector` | restrict area only to specified agents |
| `bSupportsAgent0` | `uint32` | - |
| `bSupportsAgent1` | `uint32` | - |
| `bSupportsAgent2` | `uint32` | - |
| `bSupportsAgent3` | `uint32` | - |
| `bSupportsAgent4` | `uint32` | - |
| `bSupportsAgent5` | `uint32` | - |
| `bSupportsAgent6` | `uint32` | - |
| `bSupportsAgent7` | `uint32` | - |
| `bSupportsAgent8` | `uint32` | - |
| `bSupportsAgent9` | `uint32` | - |
| `bSupportsAgent10` | `uint32` | - |
| `bSupportsAgent11` | `uint32` | - |
| `bSupportsAgent12` | `uint32` | - |
| `bSupportsAgent13` | `uint32` | - |
| `bSupportsAgent14` | `uint32` | - |
| `bSupportsAgent15` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNavAreaMeta_SwitchByAgent.json -->

# UNavAreaMeta_SwitchByAgent

Class containing definition of a navigation area

## Inheritance

`UNavAreaMeta`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Agent0Area` | `TSubclassOf < UNavArea >` | - |
| `Agent1Area` | `TSubclassOf < UNavArea >` | - |
| `Agent2Area` | `TSubclassOf < UNavArea >` | - |
| `Agent3Area` | `TSubclassOf < UNavArea >` | - |
| `Agent4Area` | `TSubclassOf < UNavArea >` | - |
| `Agent5Area` | `TSubclassOf < UNavArea >` | - |
| `Agent6Area` | `TSubclassOf < UNavArea >` | - |
| `Agent7Area` | `TSubclassOf < UNavArea >` | - |
| `Agent8Area` | `TSubclassOf < UNavArea >` | - |
| `Agent9Area` | `TSubclassOf < UNavArea >` | - |
| `Agent10Area` | `TSubclassOf < UNavArea >` | - |
| `Agent11Area` | `TSubclassOf < UNavArea >` | - |
| `Agent12Area` | `TSubclassOf < UNavArea >` | - |
| `Agent13Area` | `TSubclassOf < UNavArea >` | - |
| `Agent14Area` | `TSubclassOf < UNavArea >` | - |
| `Agent15Area` | `TSubclassOf < UNavArea >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNavCollision.json -->

# UNavCollision

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CylinderCollision` | `TArray < FNavCollisionCylinder >` | list of nav collision cylinders |
| `BoxCollision` | `TArray < FNavCollisionBox >` | list of nav collision boxes |
| `AreaClass` | `TSubclassOf < UNavArea >` | navigation area type (empty = default obstacle) |
| `bIsDynamicObstacle` | `uint32` | If set, mesh will be used as dynamic obstacle (don't create navmesh on top, much faster addingremoving) |
| `bGatherConvexGeometry` | `uint32` | If set, convex collisions will be exported offline for faster runtime navmesh building (increases memory usage) |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNavigationDataChunk.json -->

# UNavigationDataChunk

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NavigationDataName` | `FName` | Name of NavigationData actor that owns this chunk |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNavigationGraphNodeComponent.json -->

# UNavigationGraphNodeComponent

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Node` | `FNavGraphNode` | - |
| `NextNodeComponent` | `UNavigationGraphNodeComponent *` | - |
| `PrevNodeComponent` | `UNavigationGraphNodeComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNavigationInvokerComponent.json -->

# UNavigationInvokerComponent

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TileGenerationRadius` | `float` | - |
| `TileRemovalRadius` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNavigationPath.json -->

# UNavigationPath

UObject wrapper for FNavigationPath

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PathPoints` | `TArray < FVector >` | - |
| `RecalculateOnInvalidation` | `TEnumAsByte < ENavigationOptionFlag :: Type >` | - |

## Functions

### `GetDebugString`

```text
GetDebugString() -> FString
```

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `EnableDebugDrawing`

```text
EnableDebugDrawing(bShouldDrawDebugData: bool, PathColor: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bShouldDrawDebugData` | `bool` | - |
| `PathColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableRecalculationOnInvalidation`

```text
EnableRecalculationOnInvalidation(DoRecalculation: TEnumAsByte < ENavigationOptionFlag :: Type >) -> void
```

if enabled path will request recalculation if it gets invalidated due to a change to underlying navigation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DoRecalculation` | `TEnumAsByte < ENavigationOptionFlag :: Type >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPathLength`

```text
GetPathLength() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetPathCost`

```text
GetPathCost() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `IsPartial`

```text
IsPartial() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsValid`

```text
IsValid() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsStringPulled`

```text
IsStringPulled() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Delegates

### `PathUpdatedNotifier`

```text
PathUpdatedNotifier(AffectedPath: UNavigationPath*, PathEvent: TEnumAsByte<ENavPathEvent::Type>) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AffectedPath` | `UNavigationPath*` | - |
| `PathEvent` | `TEnumAsByte` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNavigationQueryFilter.json -->

# UNavigationQueryFilter

Class containing definition of a navigation query filter

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Areas` | `TArray < FNavigationFilterArea >` | list of overrides for navigation areas |
| `IncludeFlags` | `FNavigationFilterFlags` | required flags of navigation nodes |
| `ExcludeFlags` | `FNavigationFilterFlags` | forbidden flags of navigation nodes |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNavigationSystem.json -->

# UNavigationSystem

## Inheritance

`UBlueprintFunctionLibrary`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MainNavData` | `ANavigationData *` | - |
| `AbstractNavData` | `ANavigationData *` | special navigation data for managing direct paths, not part of NavDataSet! |
| `CrowdManagerClass` | `TSubclassOf < UCrowdManagerBase >` | - |
| `bAutoCreateNavigationData` | `uint32` | Should navigation system spawn default Navigation Data when there's none and there are navigation bounds present? |
| `bAllowClientSideNavigation` | `uint32` | - |
| `bSupportRebuilding` | `uint32` | gets set to true if gathering navigation data (like in navoctree) is required due to the need of navigation generation<br>	 	Is always true in Editor Mode. In other modes it depends on bRebuildAtRuntime of every required NavigationData class' CDO |
| `ObstacleManagerClassPath` | `FSoftClassPath` | - |
| `bInitialBuildingLocked` | `uint32` | if set to true will result navigation system not rebuild navigation until<br>	 	a call to ReleaseInitialBuildingLock() is called. Does not influence<br>	 	editor-time generation (i.e. does influence PIE and Game).<br>	 	Defaults to false. |
| `bWholeWorldNavigable` | `uint32` | If set to true (default) navigation will be generated only within special navigation<br>	 	bounds volumes (like ANavMeshBoundsVolume). Set to false means navigation should be generated<br>	 	everywhere. |
| `bSkipAgentHeightCheckWhenPickingNavData` | `uint32` | false by default, if set to true will result in not caring about nav agent height<br>	 	when trying to match navigation data to passed in nav agent |
| `DataGatheringMode` | `ENavDataGatheringModeConfig` | - |
| `bGenerateNavigationOnlyAroundNavigationInvokers` | `uint32` | If set to true navigation will be generated only around registered "navigation enforcers"<br>		This has a range of consequences (including how navigation octree operates) so it needs to<br>		be a conscious decision.<br>		Once enabled results in whole world being navigable.<br>		@see RegisterNavigationInvoker |
| `ActiveTilesUpdateInterval` | `float` | Minimal time, in seconds, between active tiles set update |
| `SupportedAgents` | `TArray < FNavDataConfig >` | - |
| `DirtyAreasUpdateFreq` | `float` | update frequency for dirty areas on navmesh |
| `NavDataSet` | `TArray < ANavigationData * >` | - |
| `NavDataRegistrationQueue` | `TArray < ANavigationData * >` | - |
| `OperationMode` | `FNavigationSystemRunMode` | - |

## Functions

### `BP_ChangeRecastPartitioning`

```text
BP_ChangeRecastPartitioning(AgentName: FName, High: bool) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AgentName` | `FName` | - |
| `High` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `BP_BuildOne`

```text
BP_BuildOne(AgentName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AgentName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BP_DynamicBuildOne`

```text
BP_DynamicBuildOne(AgentName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AgentName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BP_Build`

```text
BP_Build() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BP_AddDynamicNavAffect`

```text
BP_AddDynamicNavAffect(AgentName: FName, InBounds: FBox &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AgentName` | `FName` | - |
| `InBounds` | `FBox &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `BP_IncrementalBuild`

```text
BP_IncrementalBuild(AgentName: FName) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AgentName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `BP_CancelBuild`

```text
BP_CancelBuild(AgentName: FName) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AgentName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `BP_GetNavigationData`

```text
BP_GetNavigationData(AgentName: FName) -> ANavigationData *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AgentName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `ANavigationData *` | - |

### `GetNavigationSystem`

```text
GetNavigationSystem(WorldContextObject: UObject *) -> UNavigationSystem *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `UNavigationSystem *` | - |

### `K2_ProjectPointToNavigation`

```text
K2_ProjectPointToNavigation(WorldContextObject: UObject *, Point: FVector &, ProjectedLocation: FVector &, NavData: ANavigationData *, FilterClass: TSubclassOf < UNavigationQueryFilter >, QueryExtent: FVector) -> bool
```

Project a point onto the NavigationData

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Point` | `FVector &` | - |
| `ProjectedLocation` | `FVector &` | - |
| `NavData` | `ANavigationData *` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |
| `QueryExtent` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `K2_GetRandomReachablePointInRadius`

```text
K2_GetRandomReachablePointInRadius(WorldContextObject: UObject *, Origin: FVector &, RandomLocation: FVector &, Radius: float, NavData: ANavigationData *, FilterClass: TSubclassOf < UNavigationQueryFilter >, ExtentRadius: float) -> bool
```

Generates a random location reachable from given Origin location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Origin` | `FVector &` | - |
| `RandomLocation` | `FVector &` | - |
| `Radius` | `float` | - |
| `NavData` | `ANavigationData *` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |
| `ExtentRadius` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | Return Value represents if the call was successful |

### `K2_GetRandomPointInNavigableRadius`

```text
K2_GetRandomPointInNavigableRadius(WorldContextObject: UObject *, Origin: FVector &, RandomLocation: FVector &, Radius: float, NavData: ANavigationData *, FilterClass: TSubclassOf < UNavigationQueryFilter >) -> bool
```

Generates a random location in navigable space within given radius of Origin.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Origin` | `FVector &` | - |
| `RandomLocation` | `FVector &` | - |
| `Radius` | `float` | - |
| `NavData` | `ANavigationData *` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | Return Value represents if the call was successful |

### `GetPathCost`

```text
GetPathCost(WorldContextObject: UObject *, PathStart: FVector &, PathEnd: FVector &, PathCost: float &, NavData: ANavigationData *, FilterClass: TSubclassOf < UNavigationQueryFilter >) -> ENavigationQueryResult :: Type
```

Potentially expensive. Use with caution. Consider using UPathFollowingComponent::GetRemainingPathCost instead

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PathStart` | `FVector &` | - |
| `PathEnd` | `FVector &` | - |
| `PathCost` | `float &` | - |
| `NavData` | `ANavigationData *` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |

**Returns**

| Type | Description |
|---|---|
| `ENavigationQueryResult :: Type` | - |

### `GetPathLength`

```text
GetPathLength(WorldContextObject: UObject *, PathStart: FVector &, PathEnd: FVector &, PathLength: float &, NavData: ANavigationData *, FilterClass: TSubclassOf < UNavigationQueryFilter >) -> ENavigationQueryResult :: Type
```

Potentially expensive. Use with caution

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PathStart` | `FVector &` | - |
| `PathEnd` | `FVector &` | - |
| `PathLength` | `float &` | - |
| `NavData` | `ANavigationData *` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |

**Returns**

| Type | Description |
|---|---|
| `ENavigationQueryResult :: Type` | - |

### `IsNavigationBeingBuilt`

```text
IsNavigationBeingBuilt(WorldContextObject: UObject *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsNavigationBeingBuiltOrLocked`

```text
IsNavigationBeingBuiltOrLocked(WorldContextObject: UObject *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SimpleMoveToActor`

```text
SimpleMoveToActor(Controller: AController *, Goal: AActor *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Controller` | `AController *` | - |
| `Goal` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SimpleMoveToLocation`

```text
SimpleMoveToLocation(Controller: AController *, Goal: FVector &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Controller` | `AController *` | - |
| `Goal` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FindPathToLocationSynchronously`

```text
FindPathToLocationSynchronously(WorldContextObject: UObject *, PathStart: FVector &, PathEnd: FVector &, PathfindingContext: AActor *, FilterClass: TSubclassOf < UNavigationQueryFilter >) -> UNavigationPath *
```

Finds path instantly, in a FindPath Synchronously.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PathStart` | `FVector &` | - |
| `PathEnd` | `FVector &` | - |
| `PathfindingContext` | `AActor *` | could be one of following: NavigationData (like Navmesh actor), Pawn or Controller. This parameter determines parameters of specific pathfinding query |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |

**Returns**

| Type | Description |
|---|---|
| `UNavigationPath *` | - |

### `FindPathToActorSynchronously`

```text
FindPathToActorSynchronously(WorldContextObject: UObject *, PathStart: FVector &, GoalActor: AActor *, TetherDistance: float, PathfindingContext: AActor *, FilterClass: TSubclassOf < UNavigationQueryFilter >) -> UNavigationPath *
```

Finds path instantly, in a FindPath Synchronously. Main advantage over FindPathToLocationSynchronously is that
	 	the resulting path will automatically get updated if goal actor moves more than TetherDistance away from last path node

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PathStart` | `FVector &` | - |
| `GoalActor` | `AActor *` | - |
| `TetherDistance` | `float` | - |
| `PathfindingContext` | `AActor *` | could be one of following: NavigationData (like Navmesh actor), Pawn or Controller. This parameter determines parameters of specific pathfinding query |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |

**Returns**

| Type | Description |
|---|---|
| `UNavigationPath *` | - |

### `NavigationRaycast`

```text
NavigationRaycast(WorldContextObject: UObject *, RayStart: FVector &, RayEnd: FVector &, HitLocation: FVector &, FilterClass: TSubclassOf < UNavigationQueryFilter >, Querier: AController *) -> bool
```

Performs navigation raycast on NavigationData appropriate for given Querier.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `RayStart` | `FVector &` | - |
| `RayEnd` | `FVector &` | - |
| `HitLocation` | `FVector &` | if line was obstructed this will be set to hit location. Otherwise it contains SegmentEnd |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |
| `Querier` | `AController *` | if not passed default navigation data will be used |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if line from RayStart to RayEnd was obstructed. Also, true when no navigation data present |

### `SetMaxSimultaneousTileGenerationJobsCount`

```text
SetMaxSimultaneousTileGenerationJobsCount(MaxNumberOfJobs: int32) -> void
```

will limit the number of simultaneously running navmesh tile generation jobs to specified number.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MaxNumberOfJobs` | `int32` | gets trimmed to be at least 1. You cannot use this function to pause navmesh generation |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetMaxSimultaneousTileGenerationJobsCount`

```text
ResetMaxSimultaneousTileGenerationJobsCount() -> void
```

Brings limit of simultaneous navmesh tile generation jobs back to Project Setting's default value

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RegisterNavigationInvoker`

```text
RegisterNavigationInvoker(Invoker: AActor *, TileGenerationRadius: float, TileRemovalRadius: float) -> void
```

Registers given actor as a "navigation enforcer" which means navigation system will
	 	make sure navigation is being generated in specified radius around it.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Invoker` | `AActor *` | - |
| `TileGenerationRadius` | `float` | - |
| `TileRemovalRadius` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnregisterNavigationInvoker`

```text
UnregisterNavigationInvoker(Invoker: AActor *) -> void
```

Removes given actor from the list of active navigation enforcers.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Invoker` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetGeometryGatheringMode`

```text
SetGeometryGatheringMode(NewMode: ENavDataGatheringModeConfig) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewMode` | `ENavDataGatheringModeConfig` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnNavigationBoundsUpdated`

```text
OnNavigationBoundsUpdated(NavVolume: ANavMeshBoundsVolume *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NavVolume` | `ANavMeshBoundsVolume *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ProjectPointToNavigation`

```text
ProjectPointToNavigation(WorldContextObject: UObject *, Point: FVector &, NavData: ANavigationData *, FilterClass: TSubclassOf < UNavigationQueryFilter >, QueryExtent: FVector) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Point` | `FVector &` | - |
| `NavData` | `ANavigationData *` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |
| `QueryExtent` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRandomReachablePointInRadius`

```text
GetRandomReachablePointInRadius(WorldContextObject: UObject *, Origin: FVector &, Radius: float, NavData: ANavigationData *, FilterClass: TSubclassOf < UNavigationQueryFilter >) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Origin` | `FVector &` | - |
| `Radius` | `float` | - |
| `NavData` | `ANavigationData *` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRandomPointInNavigableRadius`

```text
GetRandomPointInNavigableRadius(WorldContextObject: UObject *, Origin: FVector &, Radius: float, NavData: ANavigationData *, FilterClass: TSubclassOf < UNavigationQueryFilter >) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Origin` | `FVector &` | - |
| `Radius` | `float` | - |
| `NavData` | `ANavigationData *` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `UpdateDynamicGenerateTargetNav`

```text
UpdateDynamicGenerateTargetNav(IsAdd: bool, GenerateTargetNav: FDynamicGenerateTargetNavigation) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsAdd` | `bool` | - |
| `GenerateTargetNav` | `FDynamicGenerateTargetNavigation` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnNavDataRegisteredEvent`

```text
OnNavDataRegisteredEvent(NavData: ANavigationData*) -> void
```

UPROPERTY(BlueprintAssignable, Transient)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NavData` | `ANavigationData*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnNavigationGenerationFinishedDelegate`

```text
OnNavigationGenerationFinishedDelegate(NavData: ANavigationData*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NavData` | `ANavigationData*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNavLinkComponent.json -->

# UNavLinkComponent

## Inheritance

`UPrimitiveComponent` -> `INavLinkHostInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Links` | `TArray < FNavigationLink >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNavLinkCustomComponent.json -->

# UNavLinkCustomComponent

Encapsulates NavLinkCustomInterface interface, can be used with Actors not relevant for navigation
   
   Additional functionality:
   - can be toggled
   - can create obstacle area for easierforced separation of link end points
   - can broadcast state changes to nearby agents

## Inheritance

`UNavRelevantComponent` -> `INavLinkCustomInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NavLinkUserId` | `uint32` | link Id assigned by navigation system |
| `EnabledAreaClass` | `TSubclassOf < UNavArea >` | area class to use when link is enabled |
| `DisabledAreaClass` | `TSubclassOf < UNavArea >` | area class to use when link is disabled |
| `LinkRelativeStart` | `FVector` | start point, relative to owner |
| `LinkRelativeEnd` | `FVector` | end point, relative to owner |
| `LinkDirection` | `TEnumAsByte < ENavLinkDirection :: Type >` | direction of link |
| `bLinkEnabled` | `uint32` | is link currently in enabled state? (area class) |
| `bNotifyWhenEnabled` | `uint32` | should link notify nearby agents when it changes state to enabled |
| `bNotifyWhenDisabled` | `uint32` | should link notify nearby agents when it changes state to disabled |
| `bCreateBoxObstacle` | `uint32` | if set, box obstacle area will be added to generation |
| `ObstacleOffset` | `FVector` | offset of simple box obstacle |
| `ObstacleExtent` | `FVector` | extent of simple box obstacle |
| `ObstacleAreaClass` | `TSubclassOf < UNavArea >` | area class for simple box obstacle |
| `BroadcastRadius` | `float` | radius of state change broadcast |
| `BroadcastInterval` | `float` | interval for state change broadcast (0 = single broadcast) |
| `BroadcastChannel` | `TEnumAsByte < ECollisionChannel >` | trace channel for state change broadcast |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNavLinkDefinition.json -->

# UNavLinkDefinition

Class containing definition of a navigation area

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Links` | `TArray < FNavigationLink >` | - |
| `SegmentLinks` | `TArray < FNavigationSegmentLink >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNavLocalGridManager.json -->

# UNavLocalGridManager

Manager for local navigation grids
  
   Builds non overlapping grid from multiple sources, that can be used later for pathfinding.
   Check also: UGridPathFollowingComponent, FNavLocalGridData

## Inheritance

`UObject`

## Functions

### `SetLocalNavigationGridDensity`

```text
SetLocalNavigationGridDensity(WorldContextObject: UObject *, CellSize: float) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `CellSize` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `AddLocalNavigationGridForPoint`

```text
AddLocalNavigationGridForPoint(WorldContextObject: UObject *, Location: FVector &, Radius2D: int32, Height: float, bRebuildGrids: bool) -> int32
```

creates new grid data for single point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Location` | `FVector &` | - |
| `Radius2D` | `int32` | - |
| `Height` | `float` | - |
| `bRebuildGrids` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `AddLocalNavigationGridForPoints`

```text
AddLocalNavigationGridForPoints(WorldContextObject: UObject *, Locations: TArray < FVector > &, Radius2D: int32, Height: float, bRebuildGrids: bool) -> int32
```

creates single grid data for set of points

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Locations` | `TArray < FVector > &` | - |
| `Radius2D` | `int32` | - |
| `Height` | `float` | - |
| `bRebuildGrids` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `AddLocalNavigationGridForBox`

```text
AddLocalNavigationGridForBox(WorldContextObject: UObject *, Location: FVector &, Extent: FVector, Rotation: FRotator, Radius2D: int32, Height: float, bRebuildGrids: bool) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Location` | `FVector &` | - |
| `Extent` | `FVector` | - |
| `Rotation` | `FRotator` | - |
| `Radius2D` | `int32` | - |
| `Height` | `float` | - |
| `bRebuildGrids` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `AddLocalNavigationGridForCapsule`

```text
AddLocalNavigationGridForCapsule(WorldContextObject: UObject *, Location: FVector &, CapsuleRadius: float, CapsuleHalfHeight: float, Radius2D: int32, Height: float, bRebuildGrids: bool) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Location` | `FVector &` | - |
| `CapsuleRadius` | `float` | - |
| `CapsuleHalfHeight` | `float` | - |
| `Radius2D` | `int32` | - |
| `Height` | `float` | - |
| `bRebuildGrids` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `RemoveLocalNavigationGrid`

```text
RemoveLocalNavigationGrid(WorldContextObject: UObject *, GridId: int32, bRebuildGrids: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `GridId` | `int32` | - |
| `bRebuildGrids` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FindLocalNavigationGridPath`

```text
FindLocalNavigationGridPath(WorldContextObject: UObject *, Start: FVector &, End: FVector &, PathPoints: TArray < FVector > &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector &` | - |
| `End` | `FVector &` | - |
| `PathPoints` | `TArray < FVector > &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNavModifierComponent.json -->

# UNavModifierComponent

## Inheritance

`UNavRelevantComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AreaClass` | `TSubclassOf < UNavArea >` | - |
| `FailsafeExtent` | `FVector` | box extent used ONLY when owning actor doesn't have collision component |

## Functions

### `SetAreaClass`

```text
SetAreaClass(NewAreaClass: TSubclassOf < UNavArea >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAreaClass` | `TSubclassOf < UNavArea >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNavMovementComponent.json -->

# UNavMovementComponent

NavMovementComponent defines base functionality for MovementComponents that move any 'agent' that may be involved in AI pathfinding.

## Inheritance

`UMovementComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NavAgentProps` | `FNavAgentProperties` | Properties that define how the component can move. |
| `FixedPathBrakingDistance` | `float` | Braking distance override used with acceleration driven path following (bUseAccelerationForPaths) |
| `bUpdateNavAgentWithOwnersCollision` | `uint32` | If set to true NavAgentProps' radius and height will be updated with Owner's collision capsule size |
| `bUseAccelerationForPaths` | `uint32` | If set, pathfollowing will control character movement via acceleration values. If false, it will set velocities directly. |
| `bUseFixedBrakingDistanceForPaths` | `uint32` | If set, FixedPathBrakingDistance will be used for path following deceleration |
| `MovementState` | `FMovementProperties` | Expresses runtime state of character's movement. Put all temporal changes to movement properties here |

## Functions

### `StopActiveMovement`

```text
StopActiveMovement() -> void
```

Stops applying further movement (usually zeros acceleration).

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopMovementKeepPathing`

```text
StopMovementKeepPathing() -> void
```

Stops movement immediately (reset velocity) but keeps following current path

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsCrouching`

```text
IsCrouching() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if currently crouching |

### `IsFalling`

```text
IsFalling() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if currently falling (not flying, in a non-fluid volume, and not on the ground) |

### `IsMovingOnGround`

```text
IsMovingOnGround() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if currently moving on the ground (e.g. walking or driving) |

### `IsSwimming`

```text
IsSwimming() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if currently swimming (moving through a fluid volume) |

### `IsFlying`

```text
IsFlying() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if currently flying (moving through a non-fluid volume without resting on the ground) |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNavRelevantComponent.json -->

# UNavRelevantComponent

## Inheritance

`UActorComponent` -> `INavRelevantInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bAttachToOwnersRoot` | `uint32` | attach navigation data to entry for owner's root component (depends on its relevancy) |
| `CachedNavParent` | `UObject *` | - |

## Functions

### `SetNavigationRelevancy`

```text
SetNavigationRelevancy(bRelevant: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bRelevant` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNetConnection.json -->

# UNetConnection

## Inheritance

`UPlayer`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Children` | `TArray < UChildConnection * >` | child connections for secondary viewports |
| `Driver` | `UNetDriver *` | Owning net driver |
| `PackageMapClass` | `TSubclassOf < UPackageMap >` | The class name for the PackageMap to be loaded |
| `PackageMap` | `UPackageMap *` | Package map between local and remote. (negotiates net serialization) |
| `OpenChannels` | `TArray < UChannel * >` | @todo document |
| `SentTemporaries` | `TArray < AActor * >` | This actor is bNetTemporary, which means it should never be replicated after it's initial packet is complete |
| `ViewTarget` | `AActor *` | The actor that is currently being viewedcontrolled by the owning controller |
| `OwningActor` | `AActor *` | Reference to controlling actor (usually PlayerController) |
| `MaxPacket` | `int32` | - |
| `InternalAck` | `uint32` | - |
| `URL` | `FURL` | - |
| `NumPacketIdBits` | `int` | Number of bits used for the packet id in the current packet. |
| `PlayerId` | `FUniqueNetIdRepl` | Net id of remote player on this connection. Only valid on client connections (server side). |
| `LastReceiveTime` | `double` | - |
| `LastReceiveRealtime` | `double` | - |
| `LastGoodPacketRealtime` | `double` | - |
| `LastSendTime` | `double` | - |
| `LastTickTime` | `double` | - |
| `QueuedBits` | `int32` | - |
| `TickCount` | `int32` | - |
| `LastRecvAckTime` | `float` | The last time an ack was received |
| `NoPacketTimeOut` | `float` | - |
| `NoAckTimeOut` | `float` | - |
| `PacketsLateFramesArrayCount` | `int32` | - |
| `PacketsArriveFramesArrayCount` | `int32` | - |
| `ChannelsToTick` | `TArray < UChannel * >` | The channels that need ticking. This will be a subset of OpenChannels, only including<br>	  channels that need to process either dormancy or queued bunches. Should be a significant<br>	  optimization over ticking and calling virtual functions on the potentially hundreds of<br>	  OpenChannels every frame. |
| `bOpenClientClampDeltaTime` | `bool` | - |
| `ClientClampDeltaTimeMin` | `float` | - |
| `ClientClampDeltaTimeMax` | `float` | - |
| `NetViewers` | `TArray < FNetViewer >` | - |
| `ShadowNetViewers` | `TArray < FShadowNetViewer >` | - |
| `NeedDealwithRPCBatchChannels` | `TArray < UActorChannel * >` | - |
| `ChannelsRequiringSubobjectGuidCleanup` | `TSet < UActorChannel * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNetDriver.json -->

# UNetDriver

## Inheritance

`UObject` -> `FExec`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NetConnectionClassName` | `FString` | Used to specify the class to use for connections |
| `MaxDownloadSize` | `int32` | @todo document |
| `bClampListenServerTickRate` | `uint32` | @todo document |
| `NetServerMaxTickRate` | `int32` | @todo document |
| `MaxInternetClientRate` | `int32` | @todo document |
| `MaxClientRate` | `int32` | @todo document |
| `ServerTravelPause` | `float` | Amount of time a server will wait before traveling to next map, gives clients time to receive final RPCs on existing level @see NextSwitchCountdown |
| `SpawnPrioritySeconds` | `float` | @todo document |
| `RelevantTimeout` | `float` | @todo document |
| `KeepAliveTime` | `float` | @todo document |
| `InitialConnectTimeout` | `float` | Amount of time to wait for a new net connection to be established before destroying the connection |
| `IgnoreNetReadyReplicateActorCount` | `int32` | Number of prioritized actors which should ignore IsNetReady when gets replicated |
| `ConnectionTimeout` | `float` | Amount of time to wait before considering an established connection timed out.<br>	  Typically shorter than the time to wait on a new connection because this connection<br>	  should already have been setup and any interruption should be trapped quicker. |
| `TimeoutMultiplierForUnoptimizedBuilds` | `float` | A multiplier that is applied to the above values when we are running with unoptimized builds (debug)<br>	 or data (uncooked). This allows us to retain normal timeout behavior while debugging without resorting<br>	 to the nuclear 'notimeouts' option or bumping the values above. If ==0 multiplier = 1 |
| `bNoTimeouts` | `bool` | If true, ignore timeouts completely.  Should be used only in development |
| `SimpleRepClassConfig` | `TArray < FString >` | - |
| `ServerConnection` | `UNetConnection *` | Connection to the server (this net driver is a client) |
| `ClientConnections` | `TArray < UNetConnection * >` | Array of connections to clients (this net driver is a host) |
| `World` | `UWorld *` | World this net driver is associated with |
| `NetConnectionClass` | `UClass *` | The loaded UClass of the net connection type to use |
| `RoleProperty` | `UProperty *` | @todo document |
| `RemoteRoleProperty` | `UProperty *` | @todo document |
| `NetDriverName` | `FName` | Used to specify the net driver to filter actors with (NAME_None \|\| NAME_GameNetDriver is the default net driver) |
| `Time` | `float` | Accumulated time for the net driver, updated by Tick |
| `bOpenClientClampDriverDeltaTime` | `bool` | - |
| `ClientClampDriverDeltaTimeMin` | `float` | - |
| `ClientClampDriverDeltaTimeMax` | `float` | - |
| `NeedResendSubObjectCreateOrRemoveInfoClassConfiges` | `TArray < FString >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UNetworkSettings.json -->

# UNetworkSettings

Network settings.

## Inheritance

`UDeveloperSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bVerifyPeer` | `uint32` | - |
| `bEnableMultiplayerWorldOriginRebasing` | `uint32` | - |
| `MaxRepArraySize` | `int32` | - |
| `MaxRepArrayMemory` | `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9F%BA%E7%A1%80%E5%8A%9F%E8%83%BD/UnrealNetwork.json -->

# UnrealNetwork

虚幻网络库

## Functions

### `RepLazyProperty`

```text
RepLazyProperty(TargetObject: AActor | UActorComponent @属性所在的Actor或Component, PropertyName: string)
```

对声明为复制的Lazy属性执行复制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetObject` | `AActor \| UActorComponent @属性所在的Actor或Component` | 属性所在的Actor或Component |
| `PropertyName` | `string` | 属性名或路径 |

### `CallUnrealRPC`

```text
CallUnrealRPC(TargetPlayerController: APlayerController, TargetObject: AActor | UActorComponent @目标Actor或Component, FunctionName: string)
```

发送可靠单播RPC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetPlayerController` | `APlayerController` | 目标玩家 |
| `TargetObject` | `AActor \| UActorComponent @目标Actor或Component` | 目标Actor或Component |
| `FunctionName` | `string` | RPC函数名 |

### `CallUnrealRPC_Unreliable`

```text
CallUnrealRPC_Unreliable(TargetPlayerController: APlayerController, TargetObject: AActor | UActorComponent @目标Actor或Component, FunctionName: string)
```

发送不可靠单播RPC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetPlayerController` | `APlayerController` | 目标玩家 |
| `TargetObject` | `AActor \| UActorComponent @目标Actor或Component` | 目标Actor或Component |
| `FunctionName` | `string` | RPC函数名 |

### `CallUnrealRPC_Multicast`

```text
CallUnrealRPC_Multicast(TargetObject: AActor | UActorComponent @目标Actor或Component, FunctionName: string)
```

发送可靠广播RPC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetObject` | `AActor \| UActorComponent @目标Actor或Component` | 目标Actor或Component |
| `FunctionName` | `string` | RPC函数名 |

### `CallUnrealRPC_Multicast_Unreliable`

```text
CallUnrealRPC_Multicast_Unreliable(TargetObject: AActor | UActorComponent @目标Actor或Component, FunctionName: string)
```

发送不可靠广播RPC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetObject` | `AActor \| UActorComponent @目标Actor或Component` | 目标Actor或Component |
| `FunctionName` | `string` | RPC函数名 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UObject.json -->

# UObject

Object: The base class all objects.
  This is a built-in Unreal class and it shouldn't be modified by mod authors.
  The full C++ class is located here: Engine\Source\Runtime\CoreUObject\Public\UObject\UObject.h

## Functions

### `ExecuteUbergraph`

```text
ExecuteUbergraph(EntryPoint: int32) -> void
```

Executes some portion of the ubergraph.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EntryPoint` | `int32` | The entry point to start code execution at. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UObjectLibrary.json -->

# UObjectLibrary

Class that holds a library of Objects

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ObjectBaseClass` | `UClass *` | Class that Objects must be of. If ContainsBlueprints is true, this is the native class that the blueprints are instances of and not UClass |
| `bHasBlueprintClasses` | `bool` | True if this library holds blueprint classes, false if it holds other objects |
| `Objects` | `TArray < UObject * >` | List of Objects in library |
| `WeakObjects` | `TArray < TWeakObjectPtr < UObject > >` | Weak pointers to objects |
| `bUseWeakReferences` | `bool` | If this library should use weak pointers |
| `bIsFullyLoaded` | `bool` | True if we've already fully loaded this library, can't do it twice |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UObjectPoolUtility.json -->

# UObjectPoolUtility

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `IsAllocatingObject`

```text
IsAllocatingObject() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UObjectReferencer.json -->

# UObjectReferencer

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ReferencedObjects` | `TArray < UObject * >` | Array of objects being referenced. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UOceanCDLODMeshComponent.json -->

# UOceanCDLODMeshComponent

## Inheritance

`UMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CDLODMeshOverrideMaterial` | `UMaterialInterface *` | The material used to rendering ocean |
| `MaxViewDistance` | `float` | - |
| `MaxCDLODDistance` | `float` | - |
| `LODDistanceRatio` | `float` | - |
| `LOD0Size` | `float` | - |
| `LODCount` | `int32` | - |
| `WaveFadeDistance` | `float` | . amplitude of wave have to fade as 0 for edge quads,this is the fade radius |
| `SeaLevel` | `float` | - |
| `Occlusioncoff` | `float` | - |
| `FFTSampleCount` | `int32` | - |
| `FFTSampleSize` | `float` | . FFT texture sampled by world position, used as  normalize sample position |
| `FFTFoamBlurNormalZ` | `FVector2D` | . X influence the foam shape<br>	. Y : Z of normal vector of FFT wave, at this moment this normal vector haven't be normalize, after z setted, normal vector will be normalized |
| `GerstnerFFTSoftness` | `FVector2D` | GerstnerFFTSoftness holds two waves blend factor in near sea<br>	 .X is Gerstner blend factor, if bigger than 1, wave fade rapidly<br>	 .Y is FFT blend factor, if smaller than 1, wave fade slowly |
| `GridSize` | `int32` | UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = OCeanCDLODMesh) |
| `ShapeUniformValue` | `TArray < int32 >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UOceanFFTComponent.json -->

# UOceanFFTComponent

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DisTexture` | `UTextureRenderTarget2D *` | - |
| `NormalMapTexture` | `UTextureRenderTarget2D *` | - |
| `FFTGridSize` | `int32` | Size of grid for FFT |
| `WaveAmplitude` | `float` | - |
| `FetchLength` | `float` | - |
| `WaveSwell` | `float` | - |
| `WindSpeed` | `FVector2D` | - |
| `SamplePatch` | `FVector2D` | - |
| `WaveSpeed` | `float` | Speed of time for FFT |
| `XYDisplaceFactor` | `float` | - |
| `JacobianFactor` | `float` | - |
| `FoamDissipationSpeed` | `float` | - |
| `FoamFalloffSpeed` | `float` | - |
| `FoamGenerationAmount` | `float` | - |
| `FoamGenerationThreshold` | `float` | - |
| `DisplaceTextureArray` | `TArray < UTexture2D * >` | - |
| `NormalTextureArray` | `TArray < UTexture2D * >` | - |
| `Frameinterval` | `int` | - |
| `FrameNum` | `int32` | - |
| `UpdateNeeded` | `bool` | - |
| `DisRTArray` | `TArray < UTextureRenderTarget2D * >` | - |
| `NormalRTArray` | `TArray < UTextureRenderTarget2D * >` | - |

## Functions

### `Update`

```text
Update(DeltaTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UOceanGerstnerComponent.json -->

# UOceanGerstnerComponent

## Inheritance

`UGerstnerWaves`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GerstnerWaveGenerators` | `TArray < FGerstnerWaterWaveGeneratorSimple >` | - |
| `MaxWaveHeight` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UOceanMeshComponent.json -->

# UOceanMeshComponent

## Inheritance

`UMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OceanMaterial` | `UMaterialInterface *` | The matarial used to rendering ocean |
| `ProjectorMaxWaveSize` | `float` | - |
| `Lod0size` | `int32` | - |
| `ShapeUniformValue` | `TArray < int32 >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UOverlapCheckAreaComponent.json -->

# UOverlapCheckAreaComponent

区域重叠检测组件，能够检测到某个范围内开启重叠检测的Actor

## Inheritance

`UActorComponent` -> `IRegionObjectInterface` -> `IComponentHibernationNotifyInterface`

## Functions

### `CheckOverlapActor`

```text
CheckOverlapActor(DeltaTime: float) -> void
```

生效范围：S
	  触发一次区域重叠检测

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StartCheck`

```text
StartCheck(InIgnoreActorList: TArray < AActor * >, bStopIfStarted: bool) -> void
```

生效范围：S
	  开始检测

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIgnoreActorList` | `TArray < AActor * >` | - |
| `bStopIfStarted` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopCheck`

```text
StopCheck() -> void
```

生效范围：S
	  停止检测

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddIgnoreActors`

```text
AddIgnoreActors(Ignores: TArray < AActor * >) -> void
```

生效范围：S
	  添加要忽略的Actor列表

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Ignores` | `TArray < AActor * >` | 要添加的Actor列表 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveIgnoreActor`

```text
RemoveIgnoreActor(Ignore: AActor *) -> int32
```

生效范围：S
	  移除忽略的Actor列表

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Ignore` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UOverlay.json -->

# UOverlay

Allows widgets to be stacked on top of each other, uses simple flow layout for content on each layer.

## Inheritance

`UPanelWidget`

## Functions

### `AddChildToOverlay`

```text
AddChildToOverlay(Content: UWidget *) -> UOverlaySlot *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UOverlaySlot *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UOverlaySlot.json -->

# UOverlaySlot

Slot for the UOverlay panel.  Allows content to be hover above other content.

## Inheritance

`UPanelSlot`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Padding` | `FMargin` | The padding area between the slot and the content it contains. |
| `HorizontalAlignment` | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the object horizontally. |
| `VerticalAlignment` | `TEnumAsByte < EVerticalAlignment >` | The alignment of the object vertically. |

## Functions

### `SetPadding`

```text
SetPadding(InPadding: FMargin) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPadding` | `FMargin` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHorizontalAlignment`

```text
SetHorizontalAlignment(InHorizontalAlignment: EHorizontalAlignment) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InHorizontalAlignment` | `EHorizontalAlignment` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVerticalAlignment`

```text
SetVerticalAlignment(InVerticalAlignment: EVerticalAlignment) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVerticalAlignment` | `EVerticalAlignment` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPanelSlot.json -->

# UPanelSlot

The base class for all Slots in UMG.

## Inheritance

`UVisual`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Parent` | `UPanelWidget *` | - |
| `Content` | `UWidget *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPanelWidget.json -->

# UPanelWidget

The base class for all UMG panel widgets.  Panel widgets layout a collection of child widgets.

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Slots` | `TArray < UPanelSlot * >` | The slots in the widget holding the child widgets of this panel. |
| `CachedContents_ForGC` | `TArray < UWidget * >` | - |

## Functions

### `GetChildrenCount`

```text
GetChildrenCount() -> int32
```

Gets number of child widgets in the container.

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetChildAt`

```text
GetChildAt(Index: int32) -> UWidget *
```

Gets the widget at an index.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | The index of the widget. |

**Returns**

| Type | Description |
|---|---|
| `UWidget *` | The widget at the given index, or nothing if there is no widget there. |

### `GetChildIndex`

```text
GetChildIndex(Content: UWidget *) -> int32
```

Gets the index of a specific child widget

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `HasChild`

```text
HasChild(Content: UWidget *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if panel contains this widget |

### `RemoveChildAt`

```text
RemoveChildAt(Index: int32) -> bool
```

Removes a child by it's index.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `AddChild`

```text
AddChild(Content: UWidget *) -> UPanelSlot *
```

Adds a new child widget to the container.  Returns the base slot type, 
	  requires casting to turn it into the type specific to the container.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UPanelSlot *` | - |

### `InsertChildAtIndex`

```text
InsertChildAtIndex(Index: int32, Content: UWidget *) -> UPanelSlot *
```

Insert a widget at a specific index, available in game.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UPanelSlot *` | - |

### `ShiftChildToIndex`

```text
ShiftChildToIndex(Index: int32, Child: UWidget *) -> void
```

Moves the child widget from its current index to the new index provided, available in game.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |
| `Child` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveChild`

```text
RemoveChild(Content: UWidget *) -> bool
```

Removes a specific widget from the container.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the widget was found and removed. |

### `HasAnyChildren`

```text
HasAnyChildren() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if there are any child widgets in the panel |

### `ClearChildren`

```text
ClearChildren() -> void
```

Remove all child widgets from the panel widget.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPaperFlipbook.json -->

# UPaperFlipbook

Contains an animation sequence of sprite frames

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FramesPerSecond` | `float` | - |
| `KeyFrames` | `TArray < FPaperFlipbookKeyFrame >` | - |
| `DefaultMaterial` | `UMaterialInterface *` | - |
| `CollisionSource` | `TEnumAsByte < EFlipbookCollisionMode :: Type >` | - |

## Functions

### `GetNumFrames`

```text
GetNumFrames() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetTotalDuration`

```text
GetTotalDuration() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetKeyFrameIndexAtTime`

```text
GetKeyFrameIndexAtTime(Time: float, bClampToEnds: bool) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `bClampToEnds` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetSpriteAtTime`

```text
GetSpriteAtTime(Time: float, bClampToEnds: bool) -> UPaperSprite *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `bClampToEnds` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `UPaperSprite *` | - |

### `GetSpriteAtFrame`

```text
GetSpriteAtFrame(FrameIndex: int32) -> UPaperSprite *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FrameIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `UPaperSprite *` | - |

### `GetNumKeyFrames`

```text
GetNumKeyFrames() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `IsValidKeyFrameIndex`

```text
IsValidKeyFrameIndex(Index: int32) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPaperFlipbookComponent.json -->

# UPaperFlipbookComponent

## Inheritance

`UMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceFlipbook` | `UPaperFlipbook *` | Flipbook currently being played |
| `Material_DEPRECATED` | `UMaterialInterface *` | - |
| `PlayRate` | `float` | Current play rate of the flipbook |
| `bLooping` | `uint32` | Whether the flipbook should loop when it reaches the end, or stop |
| `bReversePlayback` | `uint32` | If playback should move the current position backwards instead of forwards |
| `bPlaying` | `uint32` | Are we currently playing (moving Position) |
| `AccumulatedTime` | `float` | Current position in the timeline |
| `CachedFrameIndex` | `int32` | Last frame index calculated |
| `SpriteColor` | `FLinearColor` | Vertex color to apply to the frames |
| `CachedBodySetup` | `UBodySetup *` | The cached body setup |

## Functions

### `SetFlipbook`

```text
SetFlipbook(NewFlipbook: UPaperFlipbook *) -> bool
```

Change the flipbook used by this instance (will reset the play time to 0 if it is a new flipbook).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewFlipbook` | `UPaperFlipbook *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetFlipbook`

```text
GetFlipbook() -> UPaperFlipbook *
```

Gets the flipbook used by this instance.

**Returns**

| Type | Description |
|---|---|
| `UPaperFlipbook *` | - |

### `SetSpriteColor`

```text
SetSpriteColor(NewColor: FLinearColor) -> void
```

Set color of the sprite

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Play`

```text
Play() -> void
```

Start playback of flipbook

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlayFromStart`

```text
PlayFromStart() -> void
```

Start playback of flipbook from the start

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Reverse`

```text
Reverse() -> void
```

Start playback of flipbook in reverse

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReverseFromEnd`

```text
ReverseFromEnd() -> void
```

Start playback of flipbook in reverse from the end

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Stop`

```text
Stop() -> void
```

Stop playback of flipbook

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsPlaying`

```text
IsPlaying() -> bool
```

Get whether this flipbook is playing or not.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsReversing`

```text
IsReversing() -> bool
```

Get whether we are reversing or not

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetPlaybackPositionInFrames`

```text
SetPlaybackPositionInFrames(NewFramePosition: int32, bFireEvents: bool) -> void
```

Jump to a position in the flipbook (expressed in frames). If bFireEvents is true, event functions will fire, otherwise they will not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewFramePosition` | `int32` | - |
| `bFireEvents` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPlaybackPositionInFrames`

```text
GetPlaybackPositionInFrames() -> int32
```

Get the current playback position (in frames) of the flipbook

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetPlaybackPosition`

```text
SetPlaybackPosition(NewPosition: float, bFireEvents: bool) -> void
```

Jump to a position in the flipbook (expressed in seconds). If bFireEvents is true, event functions will fire, otherwise they will not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPosition` | `float` | - |
| `bFireEvents` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPlaybackPosition`

```text
GetPlaybackPosition() -> float
```

Get the current playback position (in seconds) of the flipbook

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetLooping`

```text
SetLooping(bNewLooping: bool) -> void
```

true means we should loop, false means we should not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewLooping` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsLooping`

```text
IsLooping() -> bool
```

Get whether we are looping or not

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetPlayRate`

```text
SetPlayRate(NewRate: float) -> void
```

Sets the new play rate for this flipbook

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRate` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPlayRate`

```text
GetPlayRate() -> float
```

Get the current play rate for this flipbook

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetNewTime`

```text
SetNewTime(NewTime: float) -> void
```

Set the new playback position time to use

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetFlipbookLength`

```text
GetFlipbookLength() -> float
```

Get length of the flipbook (in seconds)

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetFlipbookLengthInFrames`

```text
GetFlipbookLengthInFrames() -> int32
```

Get length of the flipbook (in frames)

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetFlipbookFramerate`

```text
GetFlipbookFramerate() -> float
```

Get the nominal framerate that the flipbook will be played back at (ignoring PlayRate), in frames per second

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `OnRep_SourceFlipbook`

```text
OnRep_SourceFlipbook(OldFlipbook: UPaperFlipbook *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldFlipbook` | `UPaperFlipbook *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnFinishedPlaying`

```text
OnFinishedPlaying() -> void
```

Event called whenever a non-looping flipbook finishes playing (either reaching the beginning or the end, depending on the play direction)

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPaperGroupedSpriteComponent.json -->

# UPaperGroupedSpriteComponent

A component that handles rendering and collision for many instances of one or more UPaperSprite assets.
 
  @see UPrimitiveComponent, UPaperSprite

## Inheritance

`UMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InstanceMaterials` | `TArray < UMaterialInterface * >` | Array of materials used by the instances |
| `PerInstanceSpriteData` | `TArray < FSpriteInstanceData >` | Array of instances |

## Functions

### `AddInstance`

```text
AddInstance(Transform: FTransform &, Sprite: UPaperSprite *, bWorldSpace: bool, Color: FLinearColor) -> int32
```

Add an instance to this component. Transform can be given either in the local space of this component or world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Transform` | `FTransform &` | - |
| `Sprite` | `UPaperSprite *` | - |
| `bWorldSpace` | `bool` | - |
| `Color` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetInstanceTransform`

```text
GetInstanceTransform(InstanceIndex: int32, OutInstanceTransform: FTransform &, bWorldSpace: bool) -> bool
```

Get the transform for the instance specified. Instance is returned in local space of this component unless bWorldSpace is set.  Returns True on success.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | - |
| `OutInstanceTransform` | `FTransform &` | - |
| `bWorldSpace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `UpdateInstanceTransform`

```text
UpdateInstanceTransform(InstanceIndex: int32, NewInstanceTransform: FTransform &, bWorldSpace: bool, bMarkRenderStateDirty: bool, bTeleport: bool) -> bool
```

Update the transform for the instance specified. Instance is given in local space of this component unless bWorldSpace is set.  Returns True on success.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | - |
| `NewInstanceTransform` | `FTransform &` | - |
| `bWorldSpace` | `bool` | - |
| `bMarkRenderStateDirty` | `bool` | - |
| `bTeleport` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `UpdateInstanceColor`

```text
UpdateInstanceColor(InstanceIndex: int32, NewInstanceColor: FLinearColor, bMarkRenderStateDirty: bool) -> bool
```

Update the color for the instance specified. Returns True on success.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | - |
| `NewInstanceColor` | `FLinearColor` | - |
| `bMarkRenderStateDirty` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `RemoveInstance`

```text
RemoveInstance(InstanceIndex: int32) -> bool
```

Remove the instance specified. Returns True on success.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ClearInstances`

```text
ClearInstances() -> void
```

Clear all instances being rendered by this component

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetInstanceCount`

```text
GetInstanceCount() -> int32
```

Get the number of instances in this component

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SortInstancesAlongAxis`

```text
SortInstancesAlongAxis(WorldSpaceSortAxis: FVector) -> void
```

Sort all instances by their world space position along the specified axis

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldSpaceSortAxis` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPaperRuntimeSettings.json -->

# UPaperRuntimeSettings

Implements the settings for the Paper2D plugin.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnableSpriteAtlasGroups` | `bool` | - |
| `bEnableTerrainSplineEditing` | `bool` | - |
| `bResizeSpriteDataToMatchTextures` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPaperSprite.json -->

# UPaperSprite

Sprite Asset
 
  Stores the data necessary to render a single 2D sprite (from a region of a texture)
  Can also contain collision shapes for the sprite.
 
  @see UPaperSpriteComponent

## Inheritance

`UObject` -> `IInterface_CollisionDataProvider` -> `ISlateTextureAtlasInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceUV` | `FVector2D` | - |
| `SourceDimension` | `FVector2D` | - |
| `SourceTexture` | `UTexture2D *` | - |
| `AdditionalSourceTextures` | `TArray < UTexture * >` | - |
| `BakedSourceUV` | `FVector2D` | - |
| `BakedSourceDimension` | `FVector2D` | - |
| `BakedSourceTexture` | `UTexture2D *` | - |
| `DefaultMaterial` | `UMaterialInterface *` | - |
| `AlternateMaterial` | `UMaterialInterface *` | - |
| `Sockets` | `TArray < FPaperSpriteSocket >` | - |
| `SpriteCollisionDomain` | `TEnumAsByte < ESpriteCollisionMode :: Type >` | - |
| `PixelsPerUnrealUnit` | `float` | - |
| `BodySetup` | `UBodySetup *` | - |
| `AlternateMaterialSplitIndex` | `int32` | - |
| `BakedRenderData` | `TArray < FVector4 >` | - |
| `OriginInSourceImageBeforeTrimming` | `FVector2D` | - |
| `SourceImageDimensionBeforeTrimming` | `FVector2D` | - |
| `bTrimmedInSourceImage` | `bool` | - |
| `bRotatedInSourceImage` | `bool` | - |
| `SourceTextureDimension` | `FVector2D` | - |
| `PivotMode` | `TEnumAsByte < ESpritePivotMode :: Type >` | - |
| `CustomPivotPoint` | `FVector2D` | - |
| `bSnapPivotToPixelGrid` | `bool` | - |
| `CollisionGeometry` | `FSpriteGeometryCollection` | - |
| `CollisionThickness` | `float` | - |
| `RenderGeometry` | `FSpriteGeometryCollection` | - |
| `AtlasGroup` | `UPaperSpriteAtlas *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPaperSpriteAtlas.json -->

# UPaperSpriteAtlas

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AtlasDescription` | `FString` | - |
| `MaxWidth` | `int32` | - |
| `MaxHeight` | `int32` | - |
| `MipCount` | `int32` | - |
| `PaddingType` | `EPaperSpriteAtlasPadding` | - |
| `Padding` | `int32` | - |
| `CompressionSettings` | `TEnumAsByte < enum TextureCompressionSettings >` | - |
| `Filter` | `TEnumAsByte < enum TextureFilter >` | - |
| `GeneratedTextures` | `TArray < UTexture * >` | - |
| `AtlasGUID` | `FGuid` | - |
| `bRebuildAtlas` | `bool` | - |
| `AtlasSlots` | `TArray < FPaperSpriteAtlasSlot >` | - |
| `NumIncrementalBuilds` | `int32` | - |
| `BuiltWidth` | `int32` | - |
| `BuiltHeight` | `int32` | - |
| `BuiltPadding` | `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPaperSpriteBlueprintLibrary.json -->

# UPaperSpriteBlueprintLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `MakeBrushFromSprite`

```text
MakeBrushFromSprite(Sprite: UPaperSprite *, Width: int32, Height: int32) -> FSlateBrush
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Sprite` | `UPaperSprite *` | - |
| `Width` | `int32` | - |
| `Height` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FSlateBrush` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPaperSpriteComponent.json -->

# UPaperSpriteComponent

A component that handles rendering and collision for a single instance of a UPaperSprite asset.
 
  This component is created when you drag a sprite asset from the content browser into a Blueprint, or
  contained inside of the actor created when you drag one into the level.
 
  @see UPrimitiveComponent, UPaperSprite

## Inheritance

`UMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceSprite` | `UPaperSprite *` | - |
| `MaterialOverride_DEPRECATED` | `UMaterialInterface *` | - |
| `SpriteColor` | `FLinearColor` | - |

## Functions

### `SetSprite`

```text
SetSprite(NewSprite: UPaperSprite *) -> bool
```

Change the PaperSprite used by this instance.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewSprite` | `UPaperSprite *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetSprite`

```text
GetSprite() -> UPaperSprite *
```

Gets the PaperSprite used by this instance.

**Returns**

| Type | Description |
|---|---|
| `UPaperSprite *` | - |

### `SetSpriteColor`

```text
SetSpriteColor(NewColor: FLinearColor) -> void
```

Set color of the sprite

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPaperSpriteSheet.json -->

# UPaperSpriteSheet

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SpriteNames` | `TArray < FString >` | - |
| `Sprites` | `TArray < TSoftObjectPtr < UPaperSprite > >` | - |
| `TextureName` | `FString` | - |
| `Texture` | `UTexture2D *` | - |
| `NormalMapTextureName` | `FString` | - |
| `NormalMapTexture` | `UTexture2D *` | - |
| `AssetImportData` | `UAssetImportData *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPaperTerrainComponent.json -->

# UPaperTerrainComponent

The terrain visualization component for an associated spline component.
  This takes a 2D terrain material and instances sprite geometry along the spline path.

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TerrainMaterial` | `UPaperTerrainMaterial *` | The terrain material to apply to this component (set of rules for which sprites are used on different surfaces or the interior) |
| `bClosedSpline` | `bool` | - |
| `bFilledSpline` | `bool` | - |
| `AssociatedSpline` | `UPaperTerrainSplineComponent *` | - |
| `RandomSeed` | `int32` | Random seed used for choosing which spline meshes to use. |
| `SegmentOverlapAmount` | `float` | The overlap amount between segments |
| `TerrainColor` | `FLinearColor` | The color of the terrain (passed to the sprite material as a vertex color) |
| `ReparamStepsPerSegment` | `int32` | Number of steps per spline segment to place in the reparameterization table |
| `SpriteCollisionDomain` | `TEnumAsByte < ESpriteCollisionMode :: Type >` | Collision domain (no collision, 2D (experimental), or 3D) |
| `CollisionThickness` | `float` | The extrusion thickness of collision geometry when using a 3D collision domain |
| `CachedBodySetup` | `UBodySetup *` | Description of collision |

## Functions

### `SetTerrainColor`

```text
SetTerrainColor(NewColor: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPaperTerrainMaterial.json -->

# UPaperTerrainMaterial

Paper Terrain Material
 
  'Material' setup for a 2D terrain spline (stores references to sprites that will be instanced along the spline path, not actually related to UMaterialInterface).

## Inheritance

`UDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Rules` | `TArray < FPaperTerrainMaterialRule >` | - |
| `InteriorFill` | `UPaperSprite *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPaperTileLayer.json -->

# UPaperTileLayer

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LayerName` | `FText` | - |
| `LayerWidth` | `int32` | - |
| `LayerHeight` | `int32` | - |
| `bHiddenInGame` | `uint32` | - |
| `bLayerCollides` | `uint32` | - |
| `bOverrideCollisionThickness` | `uint32` | - |
| `bOverrideCollisionOffset` | `uint32` | - |
| `CollisionThicknessOverride` | `float` | - |
| `CollisionOffsetOverride` | `float` | - |
| `LayerColor` | `FLinearColor` | - |
| `AllocatedWidth` | `int32` | - |
| `AllocatedHeight` | `int32` | - |
| `AllocatedCells` | `TArray < FPaperTileInfo >` | - |
| `TileSet_DEPRECATED` | `UPaperTileSet *` | - |
| `AllocatedGrid_DEPRECATED` | `TArray < int32 >` | - |
| `bHiddenInEditor` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPaperTileMap.json -->

# UPaperTileMap

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MapWidth` | `int32` | - |
| `MapHeight` | `int32` | - |
| `TileWidth` | `int32` | - |
| `TileHeight` | `int32` | - |
| `PixelsPerUnrealUnit` | `float` | - |
| `SeparationPerTileX` | `float` | - |
| `SeparationPerTileY` | `float` | - |
| `SeparationPerLayer` | `float` | - |
| `SelectedTileSet` | `TSoftObjectPtr < UPaperTileSet >` | - |
| `Material` | `UMaterialInterface *` | - |
| `TileLayers` | `TArray < UPaperTileLayer * >` | - |
| `CollisionThickness` | `float` | - |
| `SpriteCollisionDomain` | `TEnumAsByte < ESpriteCollisionMode :: Type >` | - |
| `ProjectionMode` | `TEnumAsByte < ETileMapProjectionMode :: Type >` | - |
| `HexSideLength` | `int32` | - |
| `BodySetup` | `UBodySetup *` | - |
| `LayerNameIndex` | `int32` | The naming index to start at when trying to create a new layer |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPaperTileMapComponent.json -->

# UPaperTileMapComponent

A component that handles rendering and collision for a single instance of a UPaperTileMap asset.
 
  This component is created when you drag a tile map asset from the content browser into a Blueprint, or
  contained inside of the actor created when you drag one into the level.
 
  NOTE: This is an early access preview class.  While not considered production-ready, it is a step beyond
  'experimental' and is being provided as a preview of things to come:
   - We will try to provide forward-compatibility for content you create.
   - The classes may change significantly in the future.
   - The code is in an early state and may not meet the desired polish  quality bar.
   - There is probably no documentation or example content yet.
   - They will be promoted out of 'Early Access' when they are production ready.
 
  @see UPrimitiveComponent, UPaperTileMap

## Inheritance

`UMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MapWidth_DEPRECATED` | `int32` | - |
| `MapHeight_DEPRECATED` | `int32` | - |
| `TileWidth_DEPRECATED` | `int32` | - |
| `TileHeight_DEPRECATED` | `int32` | - |
| `DefaultLayerTileSet_DEPRECATED` | `UPaperTileSet *` | - |
| `Material_DEPRECATED` | `UMaterialInterface *` | - |
| `TileLayers_DEPRECATED` | `TArray < UPaperTileLayer * >` | - |
| `TileMapColor` | `FLinearColor` | - |
| `UseSingleLayerIndex` | `int32` | - |
| `bUseSingleLayer` | `bool` | - |
| `TileMap` | `UPaperTileMap *` | - |
| `bShowPerTileGridWhenSelected` | `bool` | - |
| `bShowPerLayerGridWhenSelected` | `bool` | - |
| `bShowOutlineWhenUnselected` | `bool` | - |

## Functions

### `CreateNewTileMap`

```text
CreateNewTileMap(MapWidth: int32, MapHeight: int32, TileWidth: int32, TileHeight: int32, PixelsPerUnrealUnit: float, bCreateLayer: bool) -> void
```

Creates a new tile map of the specified size, replacing the TileMap reference (or dropping the previous owned one)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MapWidth` | `int32` | Width of the map (in tiles) |
| `MapHeight` | `int32` | Height of the map (in tiles) |
| `TileWidth` | `int32` | Width of one tile (in pixels) |
| `TileHeight` | `int32` | Height of one tile (in pixels) |
| `PixelsPerUnrealUnit` | `float` | - |
| `bCreateLayer` | `bool` | Should an empty layer be created? |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OwnsTileMap`

```text
OwnsTileMap() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetTileMap`

```text
SetTileMap(NewTileMap: UPaperTileMap *) -> bool
```

Change the PaperTileMap used by this instance.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTileMap` | `UPaperTileMap *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetMapSize`

```text
GetMapSize(MapWidth: int32 &, MapHeight: int32 &, NumLayers: int32 &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MapWidth` | `int32 &` | - |
| `MapHeight` | `int32 &` | - |
| `NumLayers` | `int32 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTile`

```text
GetTile(X: int32, Y: int32, Layer: int32) -> FPaperTileInfo
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `X` | `int32` | - |
| `Y` | `int32` | - |
| `Layer` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FPaperTileInfo` | - |

### `SetTile`

```text
SetTile(X: int32, Y: int32, Layer: int32, NewValue: FPaperTileInfo) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `X` | `int32` | - |
| `Y` | `int32` | - |
| `Layer` | `int32` | - |
| `NewValue` | `FPaperTileInfo` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResizeMap`

```text
ResizeMap(NewWidthInTiles: int32, NewHeightInTiles: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewWidthInTiles` | `int32` | - |
| `NewHeightInTiles` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddNewLayer`

```text
AddNewLayer() -> UPaperTileLayer *
```

**Returns**

| Type | Description |
|---|---|
| `UPaperTileLayer *` | - |

### `GetTileMapColor`

```text
GetTileMapColor() -> FLinearColor
```

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `SetTileMapColor`

```text
SetTileMapColor(NewColor: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLayerColor`

```text
GetLayerColor(Layer: int32) -> FLinearColor
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Layer` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `SetLayerColor`

```text
SetLayerColor(NewColor: FLinearColor, Layer: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewColor` | `FLinearColor` | - |
| `Layer` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MakeTileMapEditable`

```text
MakeTileMapEditable() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTileCornerPosition`

```text
GetTileCornerPosition(TileX: int32, TileY: int32, LayerIndex: int32, bWorldSpace: bool) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TileX` | `int32` | - |
| `TileY` | `int32` | - |
| `LayerIndex` | `int32` | - |
| `bWorldSpace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTileCenterPosition`

```text
GetTileCenterPosition(TileX: int32, TileY: int32, LayerIndex: int32, bWorldSpace: bool) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TileX` | `int32` | - |
| `TileY` | `int32` | - |
| `LayerIndex` | `int32` | - |
| `bWorldSpace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTilePolygon`

```text
GetTilePolygon(TileX: int32, TileY: int32, Points: TArray < FVector > &, LayerIndex: int32, bWorldSpace: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TileX` | `int32` | - |
| `TileY` | `int32` | - |
| `Points` | `TArray < FVector > &` | - |
| `LayerIndex` | `int32` | - |
| `bWorldSpace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDefaultCollisionThickness`

```text
SetDefaultCollisionThickness(Thickness: float, bRebuildCollision: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Thickness` | `float` | - |
| `bRebuildCollision` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLayerCollision`

```text
SetLayerCollision(Layer: int32, bHasCollision: bool, bOverrideThickness: bool, CustomThickness: float, bOverrideOffset: bool, CustomOffset: float, bRebuildCollision: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Layer` | `int32` | - |
| `bHasCollision` | `bool` | - |
| `bOverrideThickness` | `bool` | - |
| `CustomThickness` | `float` | - |
| `bOverrideOffset` | `bool` | - |
| `CustomOffset` | `float` | - |
| `bRebuildCollision` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RebuildCollision`

```text
RebuildCollision() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPaperTileSet.json -->

# UPaperTileSet

A tile set is a collection of tiles pulled from a texture that can be used to fill out a tile map.
 
  @see UPaperTileMap, UPaperTileMapComponent

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TileSize` | `FIntPoint` | - |
| `TileSheet` | `UTexture2D *` | - |
| `AdditionalSourceTextures` | `TArray < UTexture * >` | - |
| `BorderMargin` | `FIntMargin` | - |
| `PerTileSpacing` | `FIntPoint` | - |
| `DrawingOffset` | `FIntPoint` | - |
| `WidthInTiles` | `int32` | - |
| `HeightInTiles` | `int32` | - |
| `AllocatedWidth` | `int32` | - |
| `AllocatedHeight` | `int32` | - |
| `PerTileData` | `TArray < FPaperTileMetadata >` | - |
| `Terrains` | `TArray < FPaperTileSetTerrain >` | - |
| `TileWidth_DEPRECATED` | `int32` | - |
| `TileHeight_DEPRECATED` | `int32` | - |
| `Margin_DEPRECATED` | `int32` | - |
| `Spacing_DEPRECATED` | `int32` | - |
| `BackgroundColor` | `FLinearColor` | The background color displayed in the tile set viewer |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleEmitter.json -->

# UParticleEmitter

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EmitterName` | `FName` | The name of the emitter. |
| `SubUVDataOffset` | `int32` | - |
| `EmitterRenderMode` | `TEnumAsByte < enum EEmitterRenderMode >` | How to render the emitter particles. Can be one of the following:<br>	 		ERM_Normal	- As the intended spritemesh<br>	 		ERM_Point	- As a 2x2 pixel block with no scaling and the color set in EmitterEditorColor<br>	 		ERM_Cross	- As a cross of lines, scaled to the size of the particle in EmitterEditorColor<br>	 		ERM_None	- Do not render |
| `LODLevels` | `TArray < UParticleLODLevel * >` | - |
| `ConvertedModules` | `uint32` | - |
| `PeakActiveParticles` | `int32` | - |
| `InitialAllocationCount` | `int32` | Initial allocation count - overrides calculated peak count if > 0 |
| `MediumDetailSpawnRateScale_DEPRECATED` | `float` | Scales the spawn rate of this emitter when the engine is running in medium or low detail mode.<br>	  This can be used to optimize particle draw cost in splitscreen.<br>	  A value of 0 effectively disables this emitter outside of high detail mode,<br>	  And this does not affect spawn per unit, unless the value is 0. |
| `QualityLevelSpawnRateScale` | `float` | - |
| `GPUToCPUEmitterSpawnRateScale` | `float` | - |
| `DetailMode` | `TEnumAsByte < EDetailMode >` | If detail mode is >= system detail mode, primitive won't be rendered. |
| `bIsSoloing` | `uint32` | If true, then show only this emitter in the editor |
| `bCookedOut` | `uint32` | If true, then this emitter was 'cooked out' by the cooker. <br>	 	This means it was completely disabled, but to preserve any<br>	 	indexing schemes, it is left in place. |
| `bDisabledLODsKeepEmitterAlive` | `uint32` | When true, if the current LOD is disabled the emitter will be kept alive. Otherwise, the emitter will be considered complete if the current LOD is disabled. |
| `bDisableWhenInsignficant` | `uint32` | When true, emitters deemed insignificant will have their tick and render disabled Instantly. When false they will simple stop spawning new particles. |
| `SignificanceLevel` | `EParticleSignificanceLevel` | The significance level required of this emitter's owner for this emitter to be active. |
| `bSupportParticleDynamicInstance` | `uint32` | When true, if r.ParticleDynamicinstance = 1 and the particle emitter type support dynamic instance,the same particle emitter will use 1 draw call command to render |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleLODLevel.json -->

# UParticleLODLevel

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Level` | `int32` | The index value of the LOD level |
| `bEnabled` | `uint32` | True if the LOD level is enabled, meaning it should be updated and rendered. |
| `RequiredModule` | `UParticleModuleRequired *` | The required module for this LOD level |
| `Modules` | `TArray < UParticleModule * >` | An array of particle modules that contain the adjusted data for the LOD level |
| `TypeDataModule` | `UParticleModuleTypeDataBase *` | - |
| `SpawnModule` | `UParticleModuleSpawn *` | The SpawnRateBurst module - required by all emitters. |
| `EventGenerator` | `UParticleModuleEventGenerator *` | The optional EventGenerator module. |
| `SpawningModules` | `TArray < UParticleModuleSpawnBase * >` | SpawningModules - These are called to determine how many particles to spawn. |
| `SpawnModules` | `TArray < UParticleModule * >` | SpawnModules - These are called when particles are spawned. |
| `UpdateModules` | `TArray < UParticleModule * >` | UpdateModules - These are called when particles are updated. |
| `OrbitModules` | `TArray < UParticleModuleOrbit * >` | OrbitModules <br>	 	These are used to do offsets of the sprite from the particle location. |
| `EventReceiverModules` | `TArray < UParticleModuleEventReceiverBase * >` | Event receiver modules only! |
| `ConvertedModules` | `uint32` | - |
| `PeakActiveParticles` | `int32` | - |
| `ActualPeakParticles` | `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModule.json -->

# UParticleModule

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bSpawnModule` | `uint32` | If true, the module performs operations on particles during Spawning |
| `bUpdateModule` | `uint32` | If true, the module performs operations on particles during Updating |
| `bFinalUpdateModule` | `uint32` | If true, the module performs operations on particles during final update |
| `bUpdateForGPUEmitter` | `uint32` | If true, the module performs operations on particles during update andor final update for GPU emitters |
| `bCurvesAsColor` | `uint32` | If true, the module displays FVector curves as colors |
| `b3DDrawMode` | `uint32` | If true, the module should render its 3D visualization helper |
| `bSupported3DDrawMode` | `uint32` | If true, the module supports rendering a 3D visualization helper |
| `bEnabled` | `uint32` | If true, the module is enabled |
| `bEditable` | `uint32` | If true, the module has had editing enabled on it |
| `LODDuplicate` | `uint32` | If true, this flag indicates that auto-generation for LOD will result in<br>		an exact duplicate of the module, regardless of the percentage.<br>		If false, it will result in a module with different settings. |
| `bSupportsRandomSeed` | `uint32` | If true, the module supports RandomSeed setting |
| `bRequiresLoopingNotification` | `uint32` | If true, the module should be told when looping |
| `LODValidity` | `uint8` | The LOD levels this module is present in.<br>	 	Bit-flags are used to indicate validity for a given LOD level.<br>	 	For example, if<br>	 		((1 << Level) & LODValidity) != 0<br>	 	then the module is used in that LOD. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleAcceleration.json -->

# UParticleModuleAcceleration

## Inheritance

`UParticleModuleAccelerationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Acceleration` | `FRawDistributionVector` | The initial acceleration of the particle.<br>	 	Value is obtained using the EmitterTime at particle spawn.<br>	 	Each frame, the current and base velocity of the particle <br>	 	is then updated using the formula <br>	 		velocity += acceleration  DeltaTime<br>	 	where DeltaTime is the time passed since the last frame. |
| `bApplyOwnerScale` | `uint32` | If true, then apply the particle system components scale <br>	 	to the acceleration value. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleAccelerationBase.json -->

# UParticleModuleAccelerationBase

## Inheritance

`UParticleModule`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bAlwaysInWorldSpace` | `uint32` | If true, then treat the acceleration as world-space |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleAccelerationConstant.json -->

# UParticleModuleAccelerationConstant

## Inheritance

`UParticleModuleAccelerationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Acceleration` | `FVector` | Constant acceleration for particles in this system. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleAccelerationDrag.json -->

# UParticleModuleAccelerationDrag

## Inheritance

`UParticleModuleAccelerationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DragCoefficient_DEPRECATED` | `UDistributionFloat *` | Per-particle drag coefficient. Evaluted using emitter time. |
| `DragCoefficientRaw` | `FRawDistributionFloat` | Per-particle drag coefficient. Evaluted using emitter time. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleAccelerationDragScaleOverLife.json -->

# UParticleModuleAccelerationDragScaleOverLife

## Inheritance

`UParticleModuleAccelerationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DragScale_DEPRECATED` | `UDistributionFloat *` | Per-particle drag scale. Evaluted using particle relative time. |
| `DragScaleRaw` | `FRawDistributionFloat` | Per-particle drag scale. Evaluted using particle relative time. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleAccelerationOverLifetime.json -->

# UParticleModuleAccelerationOverLifetime

## Inheritance

`UParticleModuleAccelerationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AccelOverLife` | `FRawDistributionVector` | The acceleration of the particle over its lifetime.<br>	 	Value is obtained using the RelativeTime of the partice.<br>	 	The current and base velocity values of the particle <br>	 	are then updated using the formula <br>	 		velocity += acceleration DeltaTime<br>	 	where DeltaTime is the time passed since the last frame. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleAttractorLine.json -->

# UParticleModuleAttractorLine

## Inheritance

`UParticleModuleAttractorBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EndPoint0` | `FVector` | The first endpoint of the line. |
| `EndPoint1` | `FVector` | The second endpoint of the line. |
| `Range` | `FRawDistributionFloat` | The range of the line attractor. |
| `Strength` | `FRawDistributionFloat` | The strength of the line attractor. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleAttractorParticle.json -->

# UParticleModuleAttractorParticle

## Inheritance

`UParticleModuleAttractorBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EmitterName` | `FName` | The source emitter for attractors |
| `Range` | `FRawDistributionFloat` | The radial range of the attraction around the source particle.<br>	 	Particle-life relative. |
| `bStrengthByDistance` | `uint32` | The strength curve is a function of distance or of time. |
| `Strength` | `FRawDistributionFloat` | The strength of the attraction (negative values repel).<br>	 	Particle-life relative if StrengthByDistance is false. |
| `bAffectBaseVelocity` | `uint32` | If true, the velocity adjustment will be applied to the base velocity. |
| `SelectionMethod` | `TEnumAsByte < enum EAttractorParticleSelectionMethod >` | The method to use when selecting an attractor target particle from the emitter.<br>	 	One of the following:<br>	 	Random		- Randomly select a particle from the source emitter.  <br>	 	Sequential  - Select a particle using a sequential order. |
| `bRenewSource` | `uint32` | Whether the particle should grab a new particle if it's source expires. |
| `bInheritSourceVel` | `uint32` | Whether the particle should inherit the source veloctiy if it expires. |
| `LastSelIndex` | `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleAttractorPoint.json -->

# UParticleModuleAttractorPoint

## Inheritance

`UParticleModuleAttractorBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Position` | `FRawDistributionVector` | The position of the point attractor from the source of the emitter. |
| `Range` | `FRawDistributionFloat` | The radial range of the attractor. |
| `Strength` | `FRawDistributionFloat` | The strength of the point attractor. |
| `StrengthByDistance` | `uint32` | The strength curve is a function of distance or of time. |
| `bAffectBaseVelocity` | `uint32` | If true, the velocity adjustment will be applied to the base velocity. |
| `bOverrideVelocity` | `uint32` | If true, set the velocity. |
| `bUseWorldSpacePosition` | `uint32` | If true, treat the position as world space.  So don't transform the the point to localspace. |
| `Positive_X` | `uint32` | Whether particles can move along the positive X axis. |
| `Positive_Y` | `uint32` | Whether particles can move along the positive Y axis. |
| `Positive_Z` | `uint32` | Whether particles can move along the positive Z axis. |
| `Negative_X` | `uint32` | Whether particles can move along the negative X axis. |
| `Negative_Y` | `uint32` | Whether particles can move along the negative Y axis. |
| `Negative_Z` | `uint32` | Whether particles can move along the negative Z axis. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleAttractorPointGravity.json -->

# UParticleModuleAttractorPointGravity

## Inheritance

`UParticleModuleAttractorBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Position` | `FVector` | The position of the point gravity source. |
| `Radius` | `float` | The distance at which the influence of the point begins to falloff. |
| `Strength_DEPRECATED` | `UDistributionFloat *` | The strength of the point source. |
| `StrengthRaw` | `FRawDistributionFloat` | The strength of the point source. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleBeamModifier.json -->

# UParticleModuleBeamModifier

## Inheritance

`UParticleModuleBeamBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ModifierType` | `TEnumAsByte < enum BeamModifierType >` | Whether this module modifies the Source or the Target. |
| `PositionOptions` | `FBeamModifierOptions` | The options associated with the position. |
| `Position` | `FRawDistributionVector` | The value to use when modifying the position. |
| `TangentOptions` | `FBeamModifierOptions` | The options associated with the Tangent. |
| `Tangent` | `FRawDistributionVector` | The value to use when modifying the Tangent. |
| `bAbsoluteTangent` | `uint32` | If true, don't transform the tangent modifier into the tangent basis. |
| `StrengthOptions` | `FBeamModifierOptions` | The options associated with the Strength. |
| `Strength` | `FRawDistributionFloat` | The value to use when modifying the Strength. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleBeamNoise.json -->

# UParticleModuleBeamNoise

## Inheritance

`UParticleModuleBeamBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bLowFreq_Enabled` | `uint32` | Is low frequency noise enabled. |
| `Frequency` | `int32` | The frequency of noise points. |
| `Frequency_LowRange` | `int32` | If not 0, then the frequency will select a random value in the range<br>	 		[Frequency_LowRange..Frequency] |
| `NoiseRange` | `FRawDistributionVector` | The noise point ranges. |
| `NoiseRangeScale` | `FRawDistributionFloat` | A scale factor that will be applied to the noise range. |
| `bNRScaleEmitterTime` | `uint32` | If true,  the NoiseRangeScale will be grabbed based on the emitter time.<br>	 	If false, the NoiseRangeScale will be grabbed based on the particle time. |
| `NoiseSpeed` | `FRawDistributionVector` | The speed with which to move each noise point. |
| `bSmooth` | `uint32` | Whether the noise movement should be smooth or 'jerky'. |
| `NoiseLockRadius` | `float` | Default target-point information to use if the beam method is endpoint. |
| `bNoiseLock` | `uint32` | INTERNAL - Whether the noise points should be locked. |
| `bOscillate` | `uint32` | Whether the noise points should be oscillate. |
| `NoiseLockTime` | `float` | How long the  noise points should be locked - 0.0 indicates forever. |
| `NoiseTension` | `float` | The tension to apply to the tessellated noise line. |
| `bUseNoiseTangents` | `uint32` | If true, calculate tangents at each noise point. |
| `NoiseTangentStrength` | `FRawDistributionFloat` | The strength of noise tangents, if enabled. |
| `NoiseTessellation` | `int32` | The amount of tessellation between noise points. |
| `bTargetNoise` | `uint32` | Whether to apply noise to the target point (or end of line in distance mode...)<br>	 	If true, the beam could potentially 'leave' the target... |
| `FrequencyDistance` | `float` | The distance at which to deposit noise points.<br>	 	If 0.0, then use the static frequency value.<br>	 	If not, distribute noise points at the given distance, up to the static Frequency value.<br>	 	At that point, evenly distribute them along the beam. |
| `bApplyNoiseScale` | `uint32` | If true, apply the noise scale to the beam. |
| `NoiseScale` | `FRawDistributionFloat` | The scale factor to apply to noise range.<br>	 	The lookup value is determined by dividing the number of noise points present by the <br>	 	maximum number of noise points (Frequency). |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleBeamSource.json -->

# UParticleModuleBeamSource

## Inheritance

`UParticleModuleBeamBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceMethod` | `TEnumAsByte < enum Beam2SourceTargetMethod >` | The method flag. |
| `SourceName` | `FName` | The strength of the tangent from the source point for each beam. |
| `bSourceAbsolute` | `uint32` | Whether to treat the as an absolute position in world space. |
| `Source` | `FRawDistributionVector` | Default source-point to use. |
| `bLockSource` | `uint32` | Whether to lock the source to the life of the particle. |
| `SourceTangentMethod` | `TEnumAsByte < enum Beam2SourceTargetTangentMethod >` | The method to use for the source tangent. |
| `SourceTangent` | `FRawDistributionVector` | The tangent for the source point for each beam. |
| `bLockSourceTangent` | `uint32` | Whether to lock the source to the life of the particle. |
| `SourceStrength` | `FRawDistributionFloat` | The strength of the tangent from the source point for each beam. |
| `bLockSourceStength` | `uint32` | Whether to lock the source to the life of the particle. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleBeamTarget.json -->

# UParticleModuleBeamTarget

## Inheritance

`UParticleModuleBeamBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetMethod` | `TEnumAsByte < enum Beam2SourceTargetMethod >` | The method flag. |
| `TargetName` | `FName` | The target point sources of each beam, when using the end point method. |
| `Target` | `FRawDistributionVector` | Default target-point information to use if the beam method is endpoint. |
| `bTargetAbsolute` | `uint32` | Whether to treat the as an absolute position in world space. |
| `bLockTarget` | `uint32` | Whether to lock the Target to the life of the particle. |
| `TargetTangentMethod` | `TEnumAsByte < enum Beam2SourceTargetTangentMethod >` | The method to use for the Target tangent. |
| `TargetTangent` | `FRawDistributionVector` | The tangent for the Target point for each beam. |
| `bLockTargetTangent` | `uint32` | Whether to lock the Target to the life of the particle. |
| `TargetStrength` | `FRawDistributionFloat` | The strength of the tangent from the Target point for each beam. |
| `bLockTargetStength` | `uint32` | Whether to lock the Target to the life of the particle. |
| `LockRadius` | `float` | Default target-point information to use if the beam method is endpoint. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleCameraOffset.json -->

# UParticleModuleCameraOffset

## Inheritance

`UParticleModuleCameraBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CameraOffset` | `FRawDistributionFloat` | The camera-relative offset to apply to sprite location |
| `bSpawnTimeOnly` | `uint32` | If true, the offset will only be processed at spawn time |
| `UpdateMethod` | `TEnumAsByte < enum EParticleCameraOffsetUpdateMethod >` | How to update the offset for this module.<br>	  DirectSet - Set the value directly (overwrite any previous setting)<br>	  Additive  - Add the offset of this module to the existing offset<br>	  Scalar    - Scale the existing offset by the value of this module |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleCollision.json -->

# UParticleModuleCollision

## Inheritance

`UParticleModuleCollisionBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DampingFactor` | `FRawDistributionVector` | How much to `slow' the velocity of the particle after a collision.<br>	 	Value is obtained using the EmitterTime at particle spawn. |
| `DampingFactorRotation` | `FRawDistributionVector` | How much to `slow' the rotation of the particle after a collision.<br>	 	Value is obtained using the EmitterTime at particle spawn. |
| `MaxCollisions` | `FRawDistributionFloat` | The maximum number of collisions a particle can have. <br>	   Value is obtained using the EmitterTime at particle spawn. |
| `CollisionCompletionOption` | `TEnumAsByte < enum EParticleCollisionComplete >` | What to do once a particles MaxCollisions is reached.<br>	 	One of the following:<br>	 	EPCC_Kill<br>	 		Kill the particle when MaxCollisions is reached<br>	 	EPCC_Freeze<br>	 		Freeze in place, NO MORE UPDATES<br>	 	EPCC_HaltCollisions,<br>	 		Stop collision checks, keep updating everything<br>	 	EPCC_FreezeTranslation,<br>	 		Stop translations, keep updating everything else<br>	 	EPCC_FreezeRotation,<br>	 		Stop rotations, keep updating everything else<br>	 	EPCC_FreezeMovement<br>	 		Stop all movement, keep updating |
| `CollisionTypes` | `TArray < TEnumAsByte < enum EObjectTypeQuery > >` | Which ObjectTypes to collide with |
| `bApplyPhysics` | `uint32` | If true, physic will be applied between a particle and the <br>	 	object it collides with. <br>	 	This is one-way - particle --> object. The particle does <br>	 	not have physics applied to it - it just generates an <br>	 	impulse applied to the object it collides with. <br>	  NOTE: having this on prevents the code from running off the game thread. |
| `bIgnoreTriggerVolumes` | `uint32` | Any trigger volumes that are hit will be ignored. NOTE: This can be turned off if the TrigerVolume physics object type is not in the CollisionTypes array.<br>	 Turning this off is strongly recommended as having it on prevents the code from running off the game thread. |
| `ClassesToIgnore` | `TArray < UClass * >` | - |
| `ActorTagsToIgnore` | `TArray < FName >` | - |
| `ComponentClassesToIgnore` | `TArray < UClass * >` | - |
| `ComponentTagsToIgnore` | `TArray < FName >` | - |
| `bTraceByChannel` | `bool` | - |
| `TraceChannel` | `TEnumAsByte < ECollisionChannel >` | - |
| `ParticleMass` | `FRawDistributionFloat` | The mass of the particle - for use when bApplyPhysics is true. <br>	 	Value is obtained using the EmitterTime at particle spawn. |
| `DirScalar` | `float` | The directional scalar value - used to scale the bounds to <br>	 	'assist' in avoiding inter-penetration or large gaps. |
| `bPawnsDoNotDecrementCount` | `uint32` | If true, then collisions with Pawns will still react, but <br>	 	the UsedMaxCollisions count will not be decremented. <br>	 	(ie., They don't 'count' as collisions)<br>	  NOTE: Having this on prevents the code from running in parallel. |
| `bOnlyVerticalNormalsDecrementCount` | `uint32` | If true, then collisions that do not have a vertical hit <br>	 	normal will still react, but UsedMaxCollisions count will <br>	 	not be decremented. (ie., They don't 'count' as collisions)<br>	 	Useful for having particles come to rest on floors. |
| `VerticalFudgeFactor` | `float` | The fudge factor to use to determine vertical.<br>	 	True vertical will have a Hit.Normal.Z == 1.0<br>	 	This will allow for Z components in the range of<br>	 	[1.0-VerticalFudgeFactor..1.0]<br>	 	to count as vertical collisions. |
| `DelayAmount` | `FRawDistributionFloat` | How long to delay before checking a particle for collisions.<br>	 	Value is retrieved using the EmitterTime.<br>	 	During update, the particle flag IgnoreCollisions will be <br>	 	set until the particle RelativeTime has surpassed the <br>	 	DelayAmount. |
| `bDropDetail` | `uint32` | If true, when the World->bDropDetail flag is set, the module will be ignored. |
| `bCollideOnlyIfVisible` | `uint32` | If true, Particle collision only if particle system is currently being rendered. |
| `bIgnoreSourceActor` | `uint32` | If true, then the source actor is ignored in collision checks.<br>	 	Defaults to true. |
| `bClearCacheIgnoreActorsAndCompsOnSpawn` | `uint32` | - |
| `ClearCacheIgnoreActorsAndCompsInterval` | `float` | - |
| `MaxCollisionDistance` | `float` | Max distance at which particle collision will occur. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleCollisionGPU.json -->

# UParticleModuleCollisionGPU

## Inheritance

`UParticleModuleCollisionBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Resilience` | `FRawDistributionFloat` | Dampens the velocity of a particle in the direction normal to the<br>	  collision plane. |
| `ResilienceScaleOverLife` | `FRawDistributionFloat` | Modulates the resilience of the particle over its lifetime. |
| `Friction` | `float` | Friction applied to all particles during a collision or while moving<br>	  along a surface. |
| `RandomSpread` | `float` | Controls how wide the bouncing particles are distributed (0 = disabled). |
| `RandomDistribution` | `float` | Controls bouncing particles distribution (1 = uniform distribution; 2 = squared distribution). |
| `RadiusScale` | `float` | Scale applied to the size of the particle to obtain the collision radius. |
| `RadiusBias` | `float` | Bias applied to the collision radius. |
| `Response` | `TEnumAsByte < EParticleCollisionResponse :: Type >` | How particles respond to a collision event. |
| `CollisionMode` | `TEnumAsByte < EParticleCollisionMode :: Type >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleCollisionHeight.json -->

# UParticleModuleCollisionHeight

## Inheritance

`UParticleModuleCollisionBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CollisionTypes` | `TArray < TEnumAsByte < enum EObjectTypeQuery > >` | Which ObjectTypes to collide with |
| `CollisionStep` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleColor.json -->

# UParticleModuleColor

## Inheritance

`UParticleModuleColorBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartColor` | `FRawDistributionVector` | Initial color for a particle as a function of Emitter time. |
| `StartAlpha` | `FRawDistributionFloat` | Initial alpha for a particle as a function of Emitter time. |
| `StartColorHDR` | `FRawDistributionVector` | Initial color for a particle as a function of Emitter time. |
| `StartAlphaHDR` | `FRawDistributionFloat` | Initial alpha for a particle as a function of Emitter time. |
| `bClampAlpha` | `uint32` | If true, the alpha value will be clamped to the [0..1] range. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleColor_Seeded.json -->

# UParticleModuleColor_Seeded

## Inheritance

`UParticleModuleColor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RandomSeedInfo` | `FParticleRandomSeedInfo` | The random seed(s) to use for looking up values in StartLocation |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleColorBase.json -->

# UParticleModuleColorBase

## Inheritance

`UParticleModule`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bOverrideColorHDR` | `uint32` | If true, allow mobile HDR to use a separate set of color parameters |
| `bOverrideAlphaHDR` | `uint32` | If true, allow mobile HDR to use a separate set of alpha parameters |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleColorOverLife.json -->

# UParticleModuleColorOverLife

## Inheritance

`UParticleModuleColorBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ColorOverLife` | `FRawDistributionVector` | The color to apply to the particle, as a function of the particle RelativeTime. |
| `AlphaOverLife` | `FRawDistributionFloat` | The alpha to apply to the particle, as a function of the particle RelativeTime. |
| `ColorOverLifeHDR` | `FRawDistributionVector` | Initial color for a particle as a function of Emitter time. |
| `AlphaOverLifeHDR` | `FRawDistributionFloat` | Initial alpha for a particle as a function of Emitter time. |
| `bClampAlpha` | `uint32` | If true, the alpha value will be clamped to the [0..1] range. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleColorScaleOverLife.json -->

# UParticleModuleColorScaleOverLife

## Inheritance

`UParticleModuleColorBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ColorScaleOverLife` | `FRawDistributionVector` | The scale factor for the color. |
| `AlphaScaleOverLife` | `FRawDistributionFloat` | The scale factor for the alpha. |
| `ColorScaleOverLifeHDR` | `FRawDistributionVector` | The scale factor for the color. |
| `AlphaScaleOverLifeHDR` | `FRawDistributionFloat` | The scale factor for the alpha. |
| `bEmitterTime` | `uint32` | Whether it is EmitterTime or ParticleTime related. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleEventGenerator.json -->

# UParticleModuleEventGenerator

## Inheritance

`UParticleModuleEventBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Events` | `TArray < struct FParticleEvent_GenerateInfo >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleEventReceiverBase.json -->

# UParticleModuleEventReceiverBase

## Inheritance

`UParticleModuleEventBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EventGeneratorType` | `TEnumAsByte < EParticleEventType >` | The type of event that will generate the kill. |
| `EventName` | `FName` | The name of the emitter of interest for generating the event. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleEventReceiverKillParticles.json -->

# UParticleModuleEventReceiverKillParticles

## Inheritance

`UParticleModuleEventReceiverBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bStopSpawning` | `uint32` | If true, stop this emitter from spawning as well. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleEventReceiverSpawn.json -->

# UParticleModuleEventReceiverSpawn

## Inheritance

`UParticleModuleEventReceiverBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SpawnCount` | `FRawDistributionFloat` | The number of particles to spawn. |
| `bUseParticleTime` | `uint32` | For Death-based event receiving, if this is true, it indicates that the <br>	 	ParticleTime of the event should be used to look-up the SpawnCount.<br>	 	Otherwise (and in all other events received), use the emitter time of <br>	 	the event. |
| `bUsePSysLocation` | `uint32` | If true, use the location of the particle system component for spawning.<br>	 	if false (default), use the location of the particle event. |
| `bInheritVelocity` | `uint32` | If true, use the velocity of the dying particle as the start velocity of <br>	 	the spawned particle. |
| `InheritVelocityScale` | `FRawDistributionVector` | If bInheritVelocity is true, scale the velocity with this. |
| `PhysicalMaterials` | `TArray < UPhysicalMaterial * >` | Array of physical materials that can be used to allow or ban a specific set of materials when receiving collision events. |
| `bBanPhysicalMaterials` | `uint32` | When true, the PhysicalMaterials list is used to ban specified materials for collision events but allow all others.<br>		When false, the PhysicalMaterials list is used to allow only specified materials for collision events and ban all others. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleKillBox.json -->

# UParticleModuleKillBox

## Inheritance

`UParticleModuleKillBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LowerLeftCorner` | `FRawDistributionVector` | The lower left corner of the box. |
| `UpperRightCorner` | `FRawDistributionVector` | The upper right corner of the box. |
| `bAbsolute` | `uint32` | If true, the box coordinates are in world space. |
| `bKillInside` | `uint32` | If true, particles INSIDE the box will be killed. <br>	 	If false (the default), particles OUTSIDE the box will be killed. |
| `bAxisAlignedAndFixedSize` | `uint32` | If true, the box will always be axis aligned and non-scalable. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleKillHeight.json -->

# UParticleModuleKillHeight

## Inheritance

`UParticleModuleKillBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Height` | `FRawDistributionFloat` | The height at which to kill the particle. |
| `bAbsolute` | `uint32` | If true, the height should be treated as a world-space position. |
| `bFloor` | `uint32` | If true, the plane should be considered a floor - ie kill anything BELOW it.<br>	 	If false, if is a ceiling - ie kill anything ABOVE it. |
| `bApplyPSysScale` | `uint32` | If true, take the particle systems scale into account |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLifetime.json -->

# UParticleModuleLifetime

## Inheritance

`UParticleModuleLifetimeBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Lifetime` | `FRawDistributionFloat` | The lifetime of the particle, in seconds. Retrieved using the EmitterTime at the spawn of the particle. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLifetime_Seeded.json -->

# UParticleModuleLifetime_Seeded

## Inheritance

`UParticleModuleLifetime`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RandomSeedInfo` | `FParticleRandomSeedInfo` | The random seed(s) to use for looking up values in StartLocation |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLight.json -->

# UParticleModuleLight

## Inheritance

`UParticleModuleLightBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bUseInverseSquaredFalloff` | `bool` | Whether to use physically based inverse squared falloff from the light.  If unchecked, the LightExponent distribution will be used instead. |
| `bAffectsTranslucency` | `bool` | Whether lights from this module should affect translucency.<br>	  Use with caution.  Modules enabling this should only make a few particle lights at most, and the smaller they are, the less they will cost. |
| `bPreviewLightRadius` | `bool` | Will draw wireframe spheres to preview the light radius if enabled.<br>	  Note: this is intended for previewing and the value will not be saved, it will always revert to disabled. |
| `SpawnFraction` | `float` | Fraction of particles in this emitter to create lights on. |
| `ColorScaleOverLife` | `FRawDistributionVector` | Scale that is applied to the particle's color to calculate the light's color, and can be setup as a curve over the particle's lifetime. |
| `BrightnessOverLife` | `FRawDistributionFloat` | Brightness scale for the light, which can be setup as a curve over the particle's lifetime. |
| `RadiusScale` | `FRawDistributionFloat` | Scales the particle's radius, to calculate the light's radius. |
| `LightExponent` | `FRawDistributionFloat` | Provides the light's exponent when inverse squared falloff is disabled. |
| `LightingChannels` | `FLightingChannels` | Channels that this light should affect.<br>	 Only affect high quality lights<br>	 These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing. |
| `VolumetricScatteringIntensity` | `float` | Intensity of the volumetric scattering from this light.  This scales Intensity and LightColor. |
| `bHighQualityLights` | `bool` | Converts the particle lights into high quality lights as if they came from a PointLightComponent.  High quality lights cost significantly more on both CPU and GPU. |
| `bShadowCastingLights` | `bool` | Whether to cast shadows from the particle lights.  Requires High Quality Lights to be enabled.<br>	  Warning: This can be incredibly expensive on the GPU - use with caution. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLight_Seeded.json -->

# UParticleModuleLight_Seeded

## Inheritance

`UParticleModuleLight`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RandomSeedInfo` | `FParticleRandomSeedInfo` | The random seed(s) to use for looking up values in StartLocation |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLocation.json -->

# UParticleModuleLocation

## Inheritance

`UParticleModuleLocationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartLocation` | `FRawDistributionVector` | The location the particle should be emitted.<br>	 	Relative in local space to the emitter by default.<br>	 	Relative in world space as a WorldOffset module or when the emitter's UseLocalSpace is off.<br>	 	Retrieved using the EmitterTime at the spawn of the particle. |
| `DistributeOverNPoints` | `float` | When set to a non-zero value this will force the particles to only spawn on evenly distributed<br>	   positions between the two points specified. |
| `DistributeThreshold` | `float` | When DistributeOverNPoints is set to a non-zero value, this specifies the ratio of particles spawned<br>	   that should use the distribution.  (For example setting this to 1 will cause all the particles to<br>	   be distributed evenly whereas .75 would cause 14 of the particles to be randomly placed). |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLocation_Seeded.json -->

# UParticleModuleLocation_Seeded

## Inheritance

`UParticleModuleLocation`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RandomSeedInfo` | `FParticleRandomSeedInfo` | The random seed(s) to use for looking up values in StartLocation |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLocationBoneSocket.json -->

# UParticleModuleLocationBoneSocket

## Inheritance

`UParticleModuleLocationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceType` | `TEnumAsByte < enum ELocationBoneSocketSource >` | Whether the module uses Bones or Sockets for locations.<br>	 <br>	 	BONESOCKETSOURCE_Bones		- Use Bones as the source locations.<br>	 	BONESOCKETSOURCE_Sockets	- Use Sockets as the source locations. |
| `UniversalOffset` | `FVector` | An offset to apply to each bonesocket |
| `SourceLocations` | `TArray < struct FLocationBoneSocketInfo >` | The name(s) of the bonesocket(s) to position at. If this is empty, the module will attempt to spawn from all bones or sockets. |
| `SelectionMethod` | `TEnumAsByte < enum ELocationBoneSocketSelectionMethod >` | The method by which to select the bonesocket to spawn at.<br>	 <br>	 	SEL_Sequential			- loop through the bonesocket array in order<br>	 	SEL_Random				- randomly select a bonesocket from the array |
| `bUpdatePositionEachFrame` | `uint32` | If true, update the particle locations each frame with that of the bonesocket |
| `bOrientMeshEmitters` | `uint32` | If true, rotate mesh emitter meshes to orient w the socket |
| `bInheritBoneVelocity` | `uint32` | If true, particles inherit the associated bone velocity when spawned |
| `InheritVelocityScale` | `float` | A scale on how much of the bone's velocity a particle will inherit. |
| `SkelMeshActorParamName` | `FName` | The parameter name of the skeletal mesh actor that supplies the SkelMeshComponent for in-game. |
| `NumPreSelectedIndices` | `int32` | - |
| `EditorSkelMesh` | `USkeletalMesh *` | The name of the skeletal mesh to use in the editor |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLocationDirect.json -->

# UParticleModuleLocationDirect

## Inheritance

`UParticleModuleLocationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Location` | `FRawDistributionVector` | The location of the particle at a give time. Retrieved using the particle RelativeTime. <br>	 	IMPORTANT: the particle location is set to this value, thereby over-writing any previous module impacts. |
| `LocationOffset` | `FRawDistributionVector` | An offset to apply to the position retrieved from the Location calculation. <br>	 	The offset is retrieved using the EmitterTime. <br>	 	The offset will remain constant over the life of the particle. |
| `ScaleFactor` | `FRawDistributionVector` | Scales the velocity of the object at a given point in the time-line. |
| `Direction` | `FRawDistributionVector` | Currently unused. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLocationEmitter.json -->

# UParticleModuleLocationEmitter

## Inheritance

`UParticleModuleLocationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EmitterName` | `FName` | The name of the emitter to use that the source location for particle. |
| `SelectionMethod` | `TEnumAsByte < enum ELocationEmitterSelectionMethod >` | The method to use when selecting a spawn target particle from the emitter.<br>	 	Can be one of the following:<br>	 		ELESM_Random		Randomly select a particle from the source emitter.<br>	 		ELESM_Sequential	Step through each particle from the source emitter in order. |
| `InheritSourceVelocity` | `uint32` | If true, the spawned particle should inherit the velocity of the source particle. |
| `InheritSourceVelocityScale` | `float` | Amount to scale the source velocity by when inheriting it. |
| `bInheritSourceRotation` | `uint32` | If true, the spawned particle should inherit the rotation of the source particle. |
| `InheritSourceRotationScale` | `float` | Amount to scale the source rotation by when inheriting it. |
| `bApplySourceOrbitOffset` | `uint32` | If true, the spawned particle should uses the location with the orbit offset of the source particle. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLocationEmitterDirect.json -->

# UParticleModuleLocationEmitterDirect

## Inheritance

`UParticleModuleLocationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EmitterName` | `FName` | The name of the emitter to use as a source for the location of the particles. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLocationPrimitiveBase.json -->

# UParticleModuleLocationPrimitiveBase

## Inheritance

`UParticleModuleLocationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Positive_X` | `uint32` | Whether the positive X axis is valid for spawning. |
| `Positive_Y` | `uint32` | Whether the positive Y axis is valid for spawning. |
| `Positive_Z` | `uint32` | Whether the positive Z axis is valid for spawning. |
| `Negative_X` | `uint32` | Whether the negative X axis is valid for spawning. |
| `Negative_Y` | `uint32` | Whether the negative Y axis is valid for spawning. |
| `Negative_Z` | `uint32` | Whether the negative Zaxis is valid for spawning. |
| `SurfaceOnly` | `uint32` | Whether particles will only spawn on the surface of the primitive. |
| `Velocity` | `uint32` | Whether the particle should get its velocity from the position within the primitive. |
| `VelocityScale` | `FRawDistributionFloat` | The scale applied to the velocity. (Only used if 'Velocity' is checked). |
| `StartLocation` | `FRawDistributionVector` | The location of the bounding primitive relative to the position of the emitter. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLocationPrimitiveCylinder.json -->

# UParticleModuleLocationPrimitiveCylinder

## Inheritance

`UParticleModuleLocationPrimitiveBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RadialVelocity` | `uint32` | If true, get the particle velocity form the radial distance inside the primitive. |
| `StartRadius` | `FRawDistributionFloat` | The radius of the cylinder. |
| `StartHeight` | `FRawDistributionFloat` | The height of the cylinder, centered about the location. |
| `HeightAxis` | `TEnumAsByte < enum CylinderHeightAxis >` | Determine particle particle system axis that should represent the height of the cylinder.<br>	  Can be one of the following:<br>	    PMLPC_HEIGHTAXIS_X - Orient the height along the particle system X-axis.<br>	    PMLPC_HEIGHTAXIS_Y - Orient the height along the particle system Y-axis.<br>	    PMLPC_HEIGHTAXIS_Z - Orient the height along the particle system Z-axis. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLocationPrimitiveCylinder_Seeded.json -->

# UParticleModuleLocationPrimitiveCylinder_Seeded

## Inheritance

`UParticleModuleLocationPrimitiveCylinder`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RandomSeedInfo` | `FParticleRandomSeedInfo` | The random seed(s) to use for looking up values in StartLocation |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLocationPrimitiveSphere.json -->

# UParticleModuleLocationPrimitiveSphere

## Inheritance

`UParticleModuleLocationPrimitiveBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartRadius` | `FRawDistributionFloat` | The radius of the sphere. Retrieved using EmitterTime. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLocationPrimitiveSphere_Seeded.json -->

# UParticleModuleLocationPrimitiveSphere_Seeded

## Inheritance

`UParticleModuleLocationPrimitiveSphere`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RandomSeedInfo` | `FParticleRandomSeedInfo` | The random seed(s) to use for looking up values in StartLocation |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLocationPrimitiveTriangle.json -->

# UParticleModuleLocationPrimitiveTriangle

## Inheritance

`UParticleModuleLocationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartOffset` | `FRawDistributionVector` | - |
| `Height` | `FRawDistributionFloat` | - |
| `Angle` | `FRawDistributionFloat` | - |
| `Thickness` | `FRawDistributionFloat` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLocationSkelVertSurface.json -->

# UParticleModuleLocationSkelVertSurface

## Inheritance

`UParticleModuleLocationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceType` | `TEnumAsByte < enum ELocationSkelVertSurfaceSource >` | Whether the module uses Verts or Surfaces for locations.<br>	 <br>	 	VERTSURFACESOURCE_Vert		- Use Verts as the source locations.<br>	 	VERTSURFACESOURCE_Surface	- Use Surfaces as the source locations. |
| `UniversalOffset` | `FVector` | An offset to apply to each vertsurface |
| `bUpdatePositionEachFrame` | `uint32` | If true, update the particle locations each frame with that of the vertsurface |
| `bOrientMeshEmitters` | `uint32` | If true, rotate mesh emitter meshes to orient w the vertsurface |
| `bInheritBoneVelocity` | `uint32` | If true, particles inherit the associated bone velocity when spawned |
| `InheritVelocityScale` | `float` | A scale on how much of the bone's velocity a particle will inherit. |
| `SkelMeshActorParamName` | `FName` | The parameter name of the skeletal mesh actor that supplies the SkelMeshComponent for in-game. |
| `ValidAssociatedBones` | `TArray < FName >` | This module will only spawn from verts or surfaces associated with the bones in this list |
| `bEnforceNormalCheck` | `uint32` | When true use the RestrictToNormal and NormalTolerance values to check surface normals |
| `NormalToCompare` | `FVector` | Use this normal to restrict spawning locations |
| `NormalCheckToleranceDegrees` | `float` | Normal tolerance.  0 degrees means it must be an exact match, 180 degrees means it can be any angle. |
| `NormalCheckTolerance` | `float` | Normal tolerance.  Value between 1.0 and -1.0 with 1.0 being exact match, 0.0 being everything up to<br>		perpendicular and -1.0 being any direction or don't restrict at all. |
| `ValidMaterialIndices` | `TArray < int32 >` | Array of material indices that are valid materials to spawn from.<br>	 	If empty, any material will be considered valid |
| `bInheritVertexColor` | `uint32` | If true, particles inherit the associated vertex color on spawn. This feature is not supported for GPU particles. |
| `bInheritUV` | `uint32` | If true, particles inherit the associated UV data on spawn. Accessed through dynamic parameter module X and Y, must be a "Spawn Time Only" parameter on "AutoSet" mode. This feature is not supported for GPU particles. |
| `InheritUVChannel` | `uint32` | UV channel to inherit from the spawn mesh, internally clamped to those available. |
| `EditorSkelMesh` | `USkeletalMesh *` | The name of the skeletal mesh to use in the editor |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLocationStVertSurface.json -->

# UParticleModuleLocationStVertSurface

## Inheritance

`UParticleModuleLocationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceType` | `TEnumAsByte < enum ELocationStVertSurfaceSource >` | Whether the module uses Verts or Surfaces for locations.<br>	 <br>	   ST_VERTSURFACESOURCE_Vert           - Use StoreVertexPostion<br>	 	ST_VERTSURFACESOURCE_ActorVert		- Use Actor Verts as the source locations.<br>	 	ST_VERTSURFACESOURCE_ActorSurface	- Use Actor Surfaces as the source locations. |
| `BrustType` | `TEnumAsByte < enum ELocationStVertBrustType >` | - |
| `ParticleCoutingMethod` | `TEnumAsByte < enum EParticleCoutingMethod >` | - |
| `UniversalOffset` | `FVector` | An offset to apply to each vertsurface |
| `bUpdatePositionEachFrame` | `uint32` | If true, update the particle locations each frame with that of the vertsurface |
| `bOrientMeshEmitters` | `uint32` | If true, rotate mesh emitter meshes to orient w the vertsurface |
| `StMeshActorParamName` | `FName` | The parameter name of the skeletal mesh actor that supplies the SkelMeshComponent for in-game. |
| `VertexPosition` | `TArray < FVector >` | - |
| `VertexNormals` | `TArray < FVector >` | - |
| `EditorStoreTriangleIndexArray` | `TArray < int32 >` | - |
| `EditorStoreTriangleNum` | `int32` | - |
| `EditorStoreSectionCount` | `int32` | - |
| `EditorStoreSectionMinVertexIndexMap` | `TMap < int32 , int32 >` | - |
| `EditorStoreSectionTrianglesMap` | `TMap < int32 , int32 >` | - |
| `PostionScale` | `FVector` | - |
| `ParticleSpeed` | `float` | - |
| `bEnforceNormalCheck` | `uint32` | When true use the RestrictToNormal and NormalTolerance values to check surface normals |
| `NormalToCompare` | `FVector` | Use this normal to restrict spawning locations |
| `NormalCheckToleranceDegrees` | `float` | Normal tolerance.  0 degrees means it must be an exact match, 180 degrees means it can be any angle. |
| `NormalCheckTolerance` | `float` | Normal tolerance.  Value between 1.0 and -1.0 with 1.0 being exact match, 0.0 being everything up to<br>		perpendicular and -1.0 being any direction or don't restrict at all. |
| `bInheritVertexColor` | `uint32` | If true, particles inherit the associated vertex color on spawn. This feature is not supported for GPU particles. |
| `bInheritUV` | `uint32` | If true, particles inherit the associated UV data on spawn. Accessed through dynamic parameter module X and Y, must be a "Spawn Time Only" parameter on "AutoSet" mode. This feature is not supported for GPU particles. |
| `InheritUVChannel` | `uint32` | UV channel to inherit from the spawn mesh, internally clamped to those available. |
| `EditorStMesh` | `UStaticMesh *` | The name of the skeletal mesh to use in the editor |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLocationWorldOffset_Seeded.json -->

# UParticleModuleLocationWorldOffset_Seeded

## Inheritance

`UParticleModuleLocationWorldOffset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RandomSeedInfo` | `FParticleRandomSeedInfo` | The random seed(s) to use for looking up values in StartLocation |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleMeshMaterial.json -->

# UParticleModuleMeshMaterial

## Inheritance

`UParticleModuleMaterialBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MeshMaterials` | `TArray < UMaterialInterface * >` | The array of materials to apply to the mesh particles. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleMeshRotation.json -->

# UParticleModuleMeshRotation

## Inheritance

`UParticleModuleRotationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartRotation` | `FRawDistributionVector` | Initial rotation in ROTATIONS PER SECOND (1 = 360 degrees).<br>	 	The value is retrieved using the EmitterTime. |
| `bInheritParent` | `uint32` | If true, apply the parents rotation as well. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleMeshRotation_Seeded.json -->

# UParticleModuleMeshRotation_Seeded

## Inheritance

`UParticleModuleMeshRotation`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RandomSeedInfo` | `FParticleRandomSeedInfo` | The random seed(s) to use for looking up values in StartLocation |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleMeshRotationRate.json -->

# UParticleModuleMeshRotationRate

## Inheritance

`UParticleModuleRotationRateBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartRotationRate` | `FRawDistributionVector` | Initial rotation rate, in rotations per second.<br>	 	The value is retrieved using the EmitterTime. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleMeshRotationRate_Seeded.json -->

# UParticleModuleMeshRotationRate_Seeded

## Inheritance

`UParticleModuleMeshRotationRate`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RandomSeedInfo` | `FParticleRandomSeedInfo` | The random seed(s) to use for looking up values in StartLocation |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleMeshRotationRateMultiplyLife.json -->

# UParticleModuleMeshRotationRateMultiplyLife

UCLASS(editinlinenew, hidecategories=Object, meta=(DisplayName = "Mesh Rotation Rate  Life"))

## Inheritance

`UParticleModuleRotationRateBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LifeMultiplier` | `FRawDistributionVector` | The scale factor that should be applied to the rotation rate.<br>	 	The value is retrieved using the RelativeTime of the particle. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleMeshRotationRateOverLife.json -->

# UParticleModuleMeshRotationRateOverLife

## Inheritance

`UParticleModuleRotationRateBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RotRate` | `FRawDistributionVector` | The rotation rate desired.<br>	 	The value is retrieved using the RelativeTime of the particle. |
| `bScaleRotRate` | `uint32` | If true, scale the current rotation rate by the value retrieved.<br>	 	Otherwise, set the rotation rate to the value retrieved. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleOrbit.json -->

# UParticleModuleOrbit

## Inheritance

`UParticleModuleOrbitBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ChainMode` | `TEnumAsByte < enum EOrbitChainMode >` | Orbit modules will chain together in the order they appear in the module stack.<br>	 	The combination of a module with the one prior to it is defined by using one<br>	 	of the following enumerations:<br>	 		EOChainMode_Add		Add the values to the previous results<br>	 		EOChainMode_Scale	Multiply the values by the previous results<br>	 		EOChainMode_Link	'Break' the chain and apply the values from the	previous results |
| `OffsetAmount` | `FRawDistributionVector` | The amount to offset the sprite from the particle position. |
| `OffsetOptions` | `FOrbitOptions` | The options associated with the OffsetAmount look-up. |
| `RotationAmount` | `FRawDistributionVector` | The amount (in 'turns') to rotate the offset about the particle position.<br>	 		0.0 = no rotation<br>	 		0.5	= 180 degree rotation<br>	 		1.0 = 360 degree rotation |
| `RotationOptions` | `FOrbitOptions` | The options associated with the RotationAmount look-up. |
| `RotationRateAmount` | `FRawDistributionVector` | The rate (in 'turns') at which to rotate the offset about the particle positon.<br>	 		0.0 = no rotation<br>	 		0.5	= 180 degree rotation<br>	 		1.0 = 360 degree rotation |
| `RotationRateOptions` | `FOrbitOptions` | The options associated with the RotationRateAmount look-up. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleOrbitBase.json -->

# UParticleModuleOrbitBase

## Inheritance

`UParticleModule`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bUseEmitterTime` | `uint32` | If true, distribution values will be retrieved using the EmitterTime.<br>	 	If false (default), they will be retrieved using the Particle.RelativeTime. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleOrientationAxisLock.json -->

# UParticleModuleOrientationAxisLock

## Inheritance

`UParticleModuleOrientationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LockAxisFlags` | `TEnumAsByte < EParticleAxisLock >` | The lock axis flag setting.<br>	 	Can be one of the following:<br>	 		EPAL_NONE			No locking to an axis.<br>	 		EPAL_X				Lock the sprite facing towards +X.<br>	 		EPAL_Y				Lock the sprite facing towards +Y.<br>	 		EPAL_Z				Lock the sprite facing towards +Z.<br>	 		EPAL_NEGATIVE_X		Lock the sprite facing towards -X.<br>	 		EPAL_NEGATIVE_Y		Lock the sprite facing towards -Y.<br>	 		EPAL_NEGATIVE_Z		Lock the sprite facing towards -Z.<br>	 		EPAL_ROTATE_X		Lock the sprite rotation on the X-axis.<br>	 		EPAL_ROTATE_Y		Lock the sprite rotation on the Y-axis.<br>	 		EPAL_ROTATE_Z		Lock the sprite rotation on the Z-axis. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleParameterDynamic.json -->

# UParticleModuleParameterDynamic

## Inheritance

`UParticleModuleParameterBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DynamicParams` | `TArray < struct FEmitterDynamicParameter >` | The dynamic parameters this module uses. |
| `UpdateFlags` | `int32` | Flags for optimizing update |
| `bUsesVelocity` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleParameterDynamic_Seeded.json -->

# UParticleModuleParameterDynamic_Seeded

## Inheritance

`UParticleModuleParameterDynamic`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RandomSeedInfo` | `FParticleRandomSeedInfo` | The random seed(s) to use for looking up values in StartLocation |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModulePivotOffset.json -->

# UParticleModulePivotOffset

## Inheritance

`UParticleModuleLocationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PivotOffset` | `FVector2D` | Offset applied in UV space to the particle vertex positions. Defaults to (0.5,0.5) putting the pivot in the centre of the partilce. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleRequired.json -->

# UParticleModuleRequired

## Inheritance

`UParticleModule`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Material` | `UMaterialInterface *` | The material to utilize for the emitter at this LOD level. |
| `EmitterOrigin` | `FVector` | - |
| `EmitterRotation` | `FRotator` | - |
| `EmitterOrbitOrigin` | `FVector` | - |
| `EmitterRotateAxis` | `EEmitterRotationMode` | - |
| `EmitterOrbitRadius` | `float` | - |
| `EmitterOrbitSpeed` | `float` | - |
| `EmitterInitialDegree` | `float` | - |
| `EmitterInitialRotation` | `float` | - |
| `EmitterSelfRotateAxis` | `EEmitterSelfRotationMode` | - |
| `EmitterSelfRotationSpeed` | `float` | - |
| `ScreenAlignment` | `TEnumAsByte < EParticleScreenAlignment >` | The screen alignment to utilize for the emitter at this LOD level.<br>	 	One of the following:<br>	 	PSA_FacingCameraPosition - Faces the camera position, but is not dependent on the camera rotation.  <br>	 								This method produces more stable particles under camera rotation.<br>	 	PSA_Square			- Uniform scale (via SizeX) facing the camera<br>	 	PSA_Rectangle		- Non-uniform scale (via SizeX and SizeY) facing the camera<br>	 	PSA_Velocity		- Orient the particle towards both the camera and the direction <br>	 						  the particle is moving. Non-uniform scaling is allowed.<br>	 	PSA_TypeSpecific	- Use the alignment method indicated in the type data module.<br>	 	PSA_FacingCameraDistanceBlend - Blends between PSA_FacingCameraPosition and PSA_Square over specified distance. |
| `MinFacingCameraBlendDistance` | `float` | The distance at which PSA_FacingCameraDistanceBlend	is fully PSA_Square |
| `MaxFacingCameraBlendDistance` | `float` | The distance at which PSA_FacingCameraDistanceBlend	is fully PSA_FacingCameraPosition |
| `bUseLocalSpace` | `uint32` | If true, update the emitter in local space |
| `bKillOnDeactivate` | `uint32` | If true, kill the emitter when the particle system is deactivated |
| `bKillOnCompleted` | `uint32` | If true, kill the emitter when it completes |
| `SortMode` | `TEnumAsByte < enum EParticleSortMode >` | The sorting mode to use for this emitter.<br>	 	PSORTMODE_None				- No sorting required.<br>	 	PSORTMODE_ViewProjDepth		- Sort by view projected depth of the particle.<br>	 	PSORTMODE_DistanceToView	- Sort by distance of particle to view in world space.<br>	 	PSORTMODE_Age_OldestFirst	- Sort by age, oldest drawn first.<br>	 	PSORTMODE_Age_NewestFirst	- Sort by age, newest drawn first. |
| `bConsiderOrbitOffsetWhenSort` | `uint32` | - |
| `bUseLegacyEmitterTime` | `uint32` | If true, the EmitterTime for the emitter will be calculated by<br>	 	modulating the SecondsSinceCreation by the EmitterDuration. As<br>	 	this can lead to issues w looping and variable duration, a new<br>	 	approach has been implemented. <br>	 	If false, this new approach is utilized, and the EmitterTime is<br>	 	simply incremented by DeltaTime each tick. When the emitter <br>	 	loops, it adjusts the EmitterTime by the current EmitterDuration<br>	 	resulting in proper loopingdelay behavior. |
| `bRemoveHMDRoll` | `uint32` | If true, removes the HMD view roll (e.g. in VR) |
| `EmitterDuration` | `float` | How long, in seconds, the emitter will run before looping. |
| `EmitterDurationLow` | `float` | The low end of the emitter duration if using a range. |
| `bEmitterDurationUseRange` | `uint32` | If true, select the emitter duration from the range <br>	 		[EmitterDurationLow..EmitterDuration] |
| `bDurationRecalcEachLoop` | `uint32` | If true, recalculate the emitter duration on each loop. |
| `EmitterLoops` | `int32` | The number of times to loop the emitter.<br>	 	0 indicates loop continuously |
| `SpawnRate` | `FRawDistributionFloat` | The rate at which to spawn particles |
| `ParticleBurstMethod` | `TEnumAsByte < EParticleBurstMethod >` | The method to utilize when burst-emitting particles |
| `BurstList` | `TArray < struct FParticleBurst >` | The array of burst entries. |
| `EmitterDelay` | `float` | Indicates the time (in seconds) that this emitter should be delayed in the particle system. |
| `EmitterDelayLow` | `float` | The low end of the emitter delay if using a range. |
| `bEmitterDelayUseRange` | `uint32` | If true, select the emitter delay from the range <br>	 		[EmitterDelayLow..EmitterDelay] |
| `bDelayFirstLoopOnly` | `uint32` | If true, the emitter will be delayed only on the first loop. |
| `InterpolationMethod` | `TEnumAsByte < EParticleSubUVInterpMethod >` | The interpolation method to used for the SubUV image selection.<br>	 	One of the following:<br>	 	PSUVIM_None			- Do not apply SubUV modules to this emitter. <br>	 	PSUVIM_Linear		- Smoothly transition between sub-images in the given order, <br>	 						  with no blending between the current and the next<br>	 	PSUVIM_Linear_Blend	- Smoothly transition between sub-images in the given order, <br>	 						  blending between the current and the next <br>	 	PSUVIM_Random		- Pick the next image at random, with no blending between <br>	 						  the current and the next <br>	 	PSUVIM_Random_Blend	- Pick the next image at random, blending between the current <br>	 						  and the next |
| `SubImages_Horizontal` | `int32` | The number of sub-images horizontally in the texture |
| `SubImages_Vertical` | `int32` | The number of sub-images vertically in the texture |
| `bScaleUV` | `uint32` | Whether to scale the UV or not - ie, the model wasn't setup with sub uvs |
| `RandomImageTime` | `float` | The amount of time (particle-relative, 0.0 to 1.0) to 'lock' on a random sub image<br>	 	    0.0 = change every frame<br>	       1.0 = select a random image at spawn and hold for the life of the particle |
| `RandomImageChanges` | `int32` | The number of times to change a random image over the life of the particle. |
| `bOverrideSystemMacroUV` | `uint32` | Override the system MacroUV settings |
| `MacroUVPosition` | `FVector` | Local space position that UVs generated with the ParticleMacroUV material node will be centered on. |
| `MacroUVRadius` | `float` | World space radius that UVs generated with the ParticleMacroUV material node will tile based on. |
| `bUseMaxDrawCount` | `uint32` | If true, use the MaxDrawCount to limit the number of particles rendered.<br>	 	NOTE: This does not limit the number spawnedupdated, only what is drawn. |
| `MaxDrawCount` | `int32` | The maximum number of particles to DRAW for this emitter.<br>	 	If set to 0, it will use whatever number are present. |
| `UVFlippingMode` | `EParticleUVFlipMode` | Controls UV Flipping for this emitter. |
| `CutoutTexture` | `UTexture2D *` | Texture to generate bounding geometry from. |
| `BoundingMode` | `TEnumAsByte < enum ESubUVBoundingVertexCount >` | More bounding vertices results in reduced overdraw, but adds more triangle overhead.<br>	 The eight vertex mode is best used when the SubUV texture has a lot of space to cut out that is not captured by the four vertex version,<br>	 and when the particles using the texture will be few and large. |
| `OpacitySourceMode` | `TEnumAsByte < enum EOpacitySourceMode >` | - |
| `AlphaThreshold` | `float` | Alpha channel values larger than the threshold are considered occupied and will be contained in the bounding geometry.<br>	 Raising this threshold slightly can reduce overdraw in particles using this animation asset. |
| `CutoutSubImagesX` | `int32` | - |
| `CutoutSubImagesY` | `int32` | The number of sub-images vertically in the texture |
| `bEnableCutOut` | `bool` | - |
| `EmitterNormalsMode` | `TEnumAsByte < enum EEmitterNormalsMode >` | Normal generation mode for this emitter LOD. |
| `NormalsSphereCenter` | `FVector` | When EmitterNormalsMode is ENM_Spherical, particle normals are created to face away from NormalsSphereCenter. <br>	  NormalsSphereCenter is in local space. |
| `NormalsCylinderDirection` | `FVector` | When EmitterNormalsMode is ENM_Cylindrical, <br>	  particle normals are created to face away from the cylinder going through NormalsSphereCenter in the direction NormalsCylinderDirection. <br>	  NormalsCylinderDirection is in local space. |
| `bOrbitModuleAffectsVelocityAlignment` | `uint32` | Ensures that movement generated from the orbit module is applied to velocity-aligned particles |
| `NamedMaterialOverrides` | `TArray < FName >` | Named material overrides for this emitter. <br>		Overrides this emitter's material(s) with those in the correspondingly named slot(s) of the owning system. |
| `UBOBoundingGeometry` | `TArray < FVector2D >` | - |
| `bUseComputeRaster` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleRotation.json -->

# UParticleModuleRotation

## Inheritance

`UParticleModuleRotationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartRotation` | `FRawDistributionFloat` | Initial rotation of the particle (1 = 360 degrees).<br>	 	The value is retrieved using the EmitterTime. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleRotation_Seeded.json -->

# UParticleModuleRotation_Seeded

## Inheritance

`UParticleModuleRotation`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RandomSeedInfo` | `FParticleRandomSeedInfo` | The random seed(s) to use for looking up values in StartLocation |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleRotationOverLifetime.json -->

# UParticleModuleRotationOverLifetime

## Inheritance

`UParticleModuleRotationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RotationOverLife` | `FRawDistributionFloat` | The rotation of the particle (1.0 = 360 degrees).<br>	 	The value is retrieved using the RelativeTime of the particle. |
| `Scale` | `uint32` | If true,  the particle rotation is multiplied by the value retrieved from RotationOverLife.<br>	 	If false, the particle rotation is incremented by the value retrieved from RotationOverLife. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleRotationRate.json -->

# UParticleModuleRotationRate

## Inheritance

`UParticleModuleRotationRateBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartRotationRate` | `FRawDistributionFloat` | Initial rotation rate, in rotations per second.<br>	 	The value is retrieved using the EmitterTime. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleRotationRate_Seeded.json -->

# UParticleModuleRotationRate_Seeded

## Inheritance

`UParticleModuleRotationRate`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RandomSeedInfo` | `FParticleRandomSeedInfo` | The random seed(s) to use for looking up values in StartLocation |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleRotationRateMultiplyLife.json -->

# UParticleModuleRotationRateMultiplyLife

UCLASS(editinlinenew, hidecategories=Object, MinimalAPI, meta=(DisplayName = "Rotation Rate  Life"))

## Inheritance

`UParticleModuleRotationRateBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LifeMultiplier` | `FRawDistributionFloat` | The scale factor that should be applied to the rotation rate.<br>	 	The value is retrieved using the RelativeTime of the particle. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleSize.json -->

# UParticleModuleSize

## Inheritance

`UParticleModuleSizeBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartSize` | `FRawDistributionVector` | The initial size that should be used for a particle.<br>	 	The value is retrieved using the EmitterTime during the spawn of a particle.<br>	 	It is added to the Size and BaseSize fields of the spawning particle. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleSize_Seeded.json -->

# UParticleModuleSize_Seeded

## Inheritance

`UParticleModuleSize`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RandomSeedInfo` | `FParticleRandomSeedInfo` | The random seed(s) to use for looking up values in StartLocation |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleSizeMultiplyLife.json -->

# UParticleModuleSizeMultiplyLife

## Inheritance

`UParticleModuleSizeBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LifeMultiplier` | `FRawDistributionVector` | The scale factor for the size that should be used for a particle.<br>	 	The value is retrieved using the RelativeTime of the particle during its update. |
| `MultiplyX` | `uint32` | If true, the X-component of the scale factor will be applied to the particle size X-component.<br>	 	If false, the X-component is left unaltered. |
| `MultiplyY` | `uint32` | If true, the Y-component of the scale factor will be applied to the particle size Y-component.<br>	 	If false, the Y-component is left unaltered. |
| `MultiplyZ` | `uint32` | If true, the Z-component of the scale factor will be applied to the particle size Z-component.<br>	 	If false, the Z-component is left unaltered. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleSizeScale.json -->

# UParticleModuleSizeScale

## Inheritance

`UParticleModuleSizeBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SizeScale` | `FRawDistributionVector` | The amount the BaseSize should be scaled before being used as the size of the particle. <br>	 	The value is retrieved using the RelativeTime of the particle during its update.<br>	 	NOTE: this module overrides any size adjustments made prior to this module in that frame. |
| `EnableX` | `uint32` | Ignored |
| `EnableY` | `uint32` | Ignored |
| `EnableZ` | `uint32` | Ignored |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleSizeScaleBySpeed.json -->

# UParticleModuleSizeScaleBySpeed

## Inheritance

`UParticleModuleSizeBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SpeedScale` | `FVector2D` | By how much speed affects the size of the particle in each dimension. |
| `MaxScale` | `FVector2D` | The maximum amount by which to scale a particle in each dimension. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleSourceMovement.json -->

# UParticleModuleSourceMovement

## Inheritance

`UParticleModuleLocationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceMovementScale` | `FRawDistributionVector` | The scale factor to apply to the source movement before adding to the particle location.<br>	 	The value is looked up using the particles RELATIVE time [0..1]. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleSpawn.json -->

# UParticleModuleSpawn

## Inheritance

`UParticleModuleSpawnBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Rate` | `FRawDistributionFloat` | The rate at which to spawn particles. |
| `RateScale` | `FRawDistributionFloat` | The scalar to apply to the rate. |
| `ParticleBurstMethod` | `TEnumAsByte < EParticleBurstMethod >` | The method to utilize when burst-emitting particles. |
| `BurstList` | `TArray < FParticleBurst >` | The array of burst entries. |
| `BurstScale` | `FRawDistributionFloat` | Scale all burst entries by this amount. |
| `bApplyGlobalSpawnRateScale` | `uint32` | If true, the SpawnRate will be scaled by the global CVar r.EmitterSpawnRateScale |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleSpawnBase.json -->

# UParticleModuleSpawnBase

## Inheritance

`UParticleModule`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bProcessSpawnRate` | `uint32` | If true, the SpawnRate of the SpawnModule of the emitter will be processed.<br>	 	If mutliple Spawn modules are 'stacked' in an emitter, if ANY of them <br>	 	have this set to false, it will not process the SpawnModule SpawnRate. |
| `bProcessBurstList` | `uint32` | If true, the BurstList of the SpawnModule of the emitter will be processed.<br>	 	If mutliple Spawn modules are 'stacked' in an emitter, if ANY of them <br>	 	have this set to false, it will not process the SpawnModule BurstList. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleSpawnPerUnit.json -->

# UParticleModuleSpawnPerUnit

## Inheritance

`UParticleModuleSpawnBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UnitScalar` | `float` | The scalar to apply to the distance traveled.<br>	 	The value from SpawnPerUnit is divided by this value to give the actual<br>	 	number of particles per unit. |
| `SpawnPerUnit` | `FRawDistributionFloat` | The amount to spawn per meter distribution.<br>	 	The value is retrieved using the EmitterTime. |
| `bIgnoreSpawnRateWhenMoving` | `uint32` | If true, process the default spawn rate when not moving...<br>	 	When not moving, skip the default spawn rate.<br>	 	If false, return the bProcessSpawnRate setting. |
| `MovementTolerance` | `float` | The tolerance for moving vs. not moving w.r.t. the bIgnoreSpawnRateWhenMoving flag.<br>	 	Ie, if (DistanceMoved < (UnitScalar x MovementTolerance)) then consider it not moving. |
| `MaxFrameDistance` | `float` | The maximum valid movement for a single frame.<br>	 	If 0.0, then the check is not performed.<br>	 	Currently, if the distance moved between frames is greater than this<br>	 	then NO particles will be spawned.<br>	 	This is primiarily intended to cover cases where the PSystem is <br>	 	attached to teleporting objects. |
| `bIgnoreMovementAlongX` | `uint32` | If true, ignore the X-component of the movement |
| `bIgnoreMovementAlongY` | `uint32` | If true, ignore the Y-component of the movement |
| `bIgnoreMovementAlongZ` | `uint32` | If true, ignore the Z-component of the movement |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleSubUV.json -->

# UParticleModuleSubUV

## Inheritance

`UParticleModuleSubUVBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Animation` | `USubUVAnimation *` | SubUV animation asset to use.<br>	  When specified, optimal bounding geometry for each SubUV frame will be used when rendering the sprites for this emitter instead of full quads.<br>	  This reduction in overdraw can reduce the GPU cost of rendering the emitter by 2x or 3x, depending on how much unused space was in the texture.<br>	  The bounding geometry is generated off of the texture alpha setup in the SubUV Animation asset, so that has to match what the material is using for opacity, or clipping will occur.<br>	  When specified, SubImages_Horizontal and SubImages_Vertical will come from the asset instead of the Required Module. |
| `SubImageIndex` | `FRawDistributionFloat` | The index of the sub-image that should be used for the particle.<br>	 	The value is retrieved using the RelativeTime of the particles. |
| `bUseRealTime` | `uint32` | If true, use real time when updating the image index.<br>	 	The movie will update regardless of the slomo settings of the game. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleSubUVMovie.json -->

# UParticleModuleSubUVMovie

## Inheritance

`UParticleModuleSubUV`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bUseEmitterTime` | `uint32` | If true, use the emitter time to look up the frame rate.<br>	 	If false (default), use the particle relative time. |
| `FrameRate` | `FRawDistributionFloat` | The frame rate the SubUV images should be 'flipped' thru at. |
| `StartingFrame` | `int32` | The starting image index for the SubUV (1 = the first frame).<br>	 	Assumes order of Left->Right, Top->Bottom<br>	 	If greater than the last frame, it will clamp to the last one.<br>	 	If 0, then randomly selects a starting frame. |
| `bUseSmallImageIndex` | `uint32` | If true, ImageIndex will be limited in 0~NumFrames.<br>	 	If false (default), ImageIndex will increase all the time. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleTrailSource.json -->

# UParticleModuleTrailSource

## Inheritance

`UParticleModuleTrailBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceMethod` | `TEnumAsByte < enum ETrail2SourceMethod >` | The source method for the trail. |
| `SourceName` | `FName` | The name of the source - either the emitter or Actor. |
| `SourceStrength` | `FRawDistributionFloat` | The strength of the tangent from the source point for each Trail. |
| `bLockSourceStength` | `uint32` | Whether to lock the source to the life of the particle. |
| `SourceOffsetCount` | `int32` | SourceOffsetCount<br>	 	The number of source offsets that can be expected to be found on the instance.<br>	 	These must be named<br>	 		TrailSourceOffset# |
| `SourceOffsetDefaults` | `TArray < FVector >` | Default offsets from the source(s). <br>	 	If there are < SourceOffsetCount slots, the grabbing of values will simply wrap. |
| `SelectionMethod` | `TEnumAsByte < enum EParticleSourceSelectionMethod >` | Particle selection method, when using the SourceMethod of Particle. |
| `bInheritRotation` | `uint32` | Interhit particle rotation - only valid for SourceMethod of PET2SRCM_Particle. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleTypeDataAnimTrail.json -->

# UParticleModuleTypeDataAnimTrail

## Inheritance

`UParticleModuleTypeDataBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bDeadTrailsOnDeactivate` | `uint32` | If true, when the system is deactivated, mark trails as dead.<br>	 	This means they will still render, but will not have more particles<br>	 	added to them, even if the system re-activates... |
| `bEnablePreviousTangentRecalculation` | `uint32` | If true, recalculate the previous tangent when a new particle is spawned |
| `bTangentRecalculationEveryFrame` | `uint32` | If true, recalculate tangents every frame to allow velocityacceleration to be applied |
| `TilingDistance` | `float` | The (estimated) covered distance to tile the 2nd UV set at.<br>	 	If 0.0, a second UV set will not be passed in. |
| `DistanceTessellationStepSize` | `float` | The distance step size for tessellation.<br>	 	# Tessellation Points = TruncToInt((Distance Between Spawned Particles)  DistanceTessellationStepSize)). If 0 then there is no distance tessellation. |
| `TangentTessellationStepSize` | `float` | The tangent scalar for tessellation.<br>	 	This is the degree change in the tangent direction [0...180] required to warrant an additional tessellation point. If 0 then there is no tangent tessellation. |
| `WidthTessellationStepSize` | `float` | The width step size for tessellation.<br>	 	This is the number of world units change in the width required to warrant an additional tessellation point. If 0 then there is no width tessellation. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleTypeDataBeam2.json -->

# UParticleModuleTypeDataBeam2

## Inheritance

`UParticleModuleTypeDataBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BeamMethod` | `TEnumAsByte < enum EBeam2Method >` | The method with which to form the beam(s). Must be one of the following:<br>	 		PEB2M_Distance	- Use the distance property to emit a beam along the X-axis of the emitter.<br>	 		PEB2M_Target	- Emit a beam from the source to the supplied target.<br>	 		PEB2M_Branch	- Currently unimplemented. |
| `TextureTile` | `int32` | The number of times to tile the texture along each beam. <br>	   Overridden by TextureTilingDistance if it is > 0.0.<br>	 	1st UV set only. 2nd UV set does not Tile. |
| `TextureTileDistance` | `float` | The distance per texture tile. <br>	 	1st UV set only. 2nd UV set does not Tile. |
| `Sheets` | `int32` | The number of sheets to render |
| `MaxBeamCount` | `int32` | The number of live beams |
| `Speed` | `float` | The speed at which the beam should move from source to target when firing up.<br>	 	'0' indicates instantaneous |
| `InterpolationPoints` | `int32` | Indicates whether the beam should be interpolated.<br>	      <= 0 --> no<br>	      >  0 --> yes (and is equal to the number of interpolation steps that should be taken. |
| `bAlwaysOn` | `uint32` | If true, there will ALWAYS be a beam... |
| `UpVectorStepSize` | `int32` | The approach to use for determining the Up vector(s) for the beam.<br>	 <br>	 	0 indicates that the Up FVector should be calculated at EVERY point in the beam.<br>	 	1 indicates a single Up FVector should be determined at the start of the beam and used at every point.<br>	 	N indicates an Up FVector should be calculated every N points of the beam and interpolated between them.<br>	 	    [NOTE: This mode is currently unsupported.] |
| `BranchParentName` | `FName` | The name of the emitter to branch from (if mode is PEB2M_Branch)<br>	  MUST BE IN THE SAME PARTICLE SYSTEM! |
| `Distance` | `FRawDistributionFloat` | The distance along the X-axis to stretch the beam<br>	 	Distance is only used if BeamMethod is PEB2M_Distance |
| `TaperMethod` | `TEnumAsByte < enum EBeamTaperMethod >` | Tapering mode - one of the following:<br>	 	PEBTM_None		- No tapering is applied<br>	 	PEBTM_Full		- Taper the beam relative to source-->target, regardless of current beam length<br>	 	PEBTM_Partial	- Taper the beam relative to source-->location, 0=source,1=endpoint |
| `TaperFactor` | `FRawDistributionFloat` | Tapering factor, 0 = source of beam, 1 = target |
| `TaperScale` | `FRawDistributionFloat` | Tapering scaling<br>	 	This is intended to be either a constant, uniform or a ParticleParam.<br>	 	If a curve is used, 01 mapping of sourcetarget... which could be integrated into<br>	 	the taper factor itself, and therefore makes no sense. |
| `RenderGeometry` | `uint32` | - |
| `RenderDirectLine` | `uint32` | - |
| `RenderLines` | `uint32` | - |
| `RenderTessellation` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleTypeDataGpu.json -->

# UParticleModuleTypeDataGpu

## Inheritance

`UParticleModuleTypeDataBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EmitterInfo` | `FGPUSpriteEmitterInfo` | Information for runtime simulation. |
| `ResourceData` | `FGPUSpriteResourceData` | Data used to initialize runtime resources. |
| `CameraMotionBlurAmount` | `float` | TEMP: How much to stretch sprites based on camera motion blur. |
| `bClearExistingParticlesOnInit` | `uint32` | When true, all existing partilces are cleared when the emitter is initialized. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleTypeDataMesh.json -->

# UParticleModuleTypeDataMesh

## Inheritance

`UParticleModuleTypeDataBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Mesh` | `UStaticMesh *` | The static mesh to render at the particle positions |
| `CastShadows` | `uint32` | If true, has the meshes cast shadows |
| `DoCollisions` | `uint32` | UNUSED (the collision module dictates doing collisions) |
| `MeshAlignment` | `TEnumAsByte < enum EMeshScreenAlignment >` | The alignment to use on the meshes emitted.<br>	 	The RequiredModule->ScreenAlignment MUST be set to PSA_TypeSpecific to use.<br>	 	One of the following:<br>	 	PSMA_MeshFaceCameraWithRoll<br>	 		Face the camera allowing for rotation around the mesh-to-camera FVector <br>	 		(amount provided by the standard particle sprite rotation).  <br>	 	PSMA_MeshFaceCameraWithSpin<br>	 		Face the camera allowing for the mesh to rotate about the tangential axis.  <br>	 	PSMA_MeshFaceCameraWithLockedAxis<br>	 		Face the camera while maintaining the up FVector as the locked direction. |
| `bOverrideMaterial` | `uint32` | If true, use the emitter material when rendering rather than the one applied <br>	 	to the static mesh model. |
| `bOverrideDefaultMotionBlurSettings` | `uint32` | - |
| `bEnableMotionBlur` | `uint32` | - |
| `Pitch_DEPRECATED` | `float` | deprecated properties for initial orientation |
| `Roll_DEPRECATED` | `float` | - |
| `Yaw_DEPRECATED` | `float` | - |
| `RollPitchYawRange` | `FRawDistributionVector` | The 'pre' rotation pitch (in degrees) to apply to the static mesh used. |
| `AxisLockOption` | `TEnumAsByte < EParticleAxisLock >` | The axis to lock the mesh on. This overrides TypeSpecific mesh alignment as well as the LockAxis module.<br>	 		EPAL_NONE		 -	No locking to an axis.<br>	 		EPAL_X			 -	Lock the mesh X-axis facing towards +X.<br>	 		EPAL_Y			 -	Lock the mesh X-axis facing towards +Y.<br>	 		EPAL_Z			 -	Lock the mesh X-axis facing towards +Z.<br>	 		EPAL_NEGATIVE_X	 -	Lock the mesh X-axis facing towards -X.<br>	 		EPAL_NEGATIVE_Y	 -	Lock the mesh X-axis facing towards -Y.<br>	 		EPAL_NEGATIVE_Z	 -	Lock the mesh X-axis facing towards -Z.<br>	 		EPAL_ROTATE_X	 -	Ignored for mesh emitters. Treated as EPAL_NONE.<br>	 		EPAL_ROTATE_Y	 -	Ignored for mesh emitters. Treated as EPAL_NONE.<br>	 		EPAL_ROTATE_Z	 -	Ignored for mesh emitters. Treated as EPAL_NONE. |
| `bCameraFacing` | `uint32` | If true, then point the X-axis of the mesh towards the camera.<br>	 	When set, AxisLockOption as well as all other locked axisscreen alignment settings are ignored. |
| `CameraFacingUpAxisOption_DEPRECATED` | `TEnumAsByte < enum EMeshCameraFacingUpAxis >` | The axis of the mesh to point up when camera facing the X-axis.<br>	 		CameraFacing_NoneUP			No attempt to face an axis up or down.<br>	 		CameraFacing_ZUp			Z-axis of the mesh should attempt to point up.<br>	 		CameraFacing_NegativeZUp	Z-axis of the mesh should attempt to point down.<br>	 		CameraFacing_YUp			Y-axis of the mesh should attempt to point up.<br>	 		CameraFacing_NegativeYUp	Y-axis of the mesh should attempt to point down. |
| `CameraFacingOption` | `TEnumAsByte < enum EMeshCameraFacingOptions >` | The camera facing option to use:<br>	 	All camera facing options without locked axis assume X-axis will be facing the camera.<br>	 		XAxisFacing_NoUp				- X-axis camera facing, no attempt to face an axis up or down.<br>	 		XAxisFacing_ZUp					- X-axis camera facing, Z-axis of the mesh should attempt to point up.<br>	 		XAxisFacing_NegativeZUp			- X-axis camera facing, Z-axis of the mesh should attempt to point down.<br>	 		XAxisFacing_YUp					- X-axis camera facing, Y-axis of the mesh should attempt to point up.<br>	 		XAxisFacing_NegativeYUp			- X-axis camera facing, Y-axis of the mesh should attempt to point down.<br>	 	All axis-locked camera facing options assume the AxisLockOption is set. EPAL_NONE will be treated as EPAL_X.<br>	 		LockedAxis_ZAxisFacing			- X-axis locked on AxisLockOption axis, rotate Z-axis of the mesh to face towards camera.<br>	 		LockedAxis_NegativeZAxisFacing	- X-axis locked on AxisLockOption axis, rotate Z-axis of the mesh to face away from camera.<br>	 		LockedAxis_YAxisFacing			- X-axis locked on AxisLockOption axis, rotate Y-axis of the mesh to face towards camera.<br>	 		LockedAxis_NegativeYAxisFacing	- X-axis locked on AxisLockOption axis, rotate Y-axis of the mesh to face away from camera.<br>	 	All velocity-aligned options do NOT require the ScreenAlignment be set to PSA_Velocity.<br>	 	Doing so will result in additional work being performed... (it will orient the mesh twice).<br>	 		VelocityAligned_ZAxisFacing         - X-axis aligned to the velocity, rotate the Z-axis of the mesh to face towards camera.<br>	 		VelocityAligned_NegativeZAxisFacing - X-axis aligned to the velocity, rotate the Z-axis of the mesh to face away from camera.<br>	 		VelocityAligned_YAxisFacing         - X-axis aligned to the velocity, rotate the Y-axis of the mesh to face towards camera.<br>	 		VelocityAligned_NegativeYAxisFacing - X-axis aligned to the velocity, rotate the Y-axis of the mesh to face away from camera. |
| `bApplyParticleRotationAsSpin` | `uint32` | If true, apply 'sprite' particle rotation about the orientation axis (direction mesh is pointing).<br>	 	If false, apply 'sprite' particle rotation about the camera facing axis. |
| `bFaceCameraDirectionRatherThanPosition` | `uint32` | If true, all camera facing options will point the mesh against the camera's view direction rather than pointing at the cameras location. <br>		If false, the camera facing will point to the cameras position as normal. |
| `bCollisionsConsiderPartilceSize` | `uint32` | If true, all collisions for mesh particle on this emitter will take the particle size into account.<br>		If false, particle size will be ignored in collision checks. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleTypeDataRibbon.json -->

# UParticleModuleTypeDataRibbon

## Inheritance

`UParticleModuleTypeDataBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaxTessellationBetweenParticles` | `int32` | The maximum amount to tessellate between two particles of the trail. <br>	 	Depending on the distance between the particles and the tangent change, the <br>	 	system will select a number of tessellation points <br>	 		[0..MaxTessellationBetweenParticles] |
| `SheetsPerTrail` | `int32` | The number of sheets to render for the trail. |
| `MaxTrailCount` | `int32` | The number of live trails |
| `MaxParticleInTrailCount` | `int32` | Max particles per trail |
| `bDeadTrailsOnDeactivate` | `uint32` | If true, when the system is deactivated, mark trails as dead.<br>	 	This means they will still render, but will not have more particles<br>	 	added to them, even if the system re-activates... |
| `bDeadTrailsOnSourceLoss` | `uint32` | If true, when the source of a trail is 'lost' (ie, the source particle<br>	 	dies), mark the current trail as dead. |
| `bClipSourceSegement` | `uint32` | If true, do not join the trail to the source position |
| `bEnablePreviousTangentRecalculation` | `uint32` | If true, recalculate the previous tangent when a new particle is spawned |
| `bTangentRecalculationEveryFrame` | `uint32` | If true, recalculate tangents every frame to allow velocityacceleration to be applied |
| `bSpawnInitialParticle` | `uint32` | If true, ribbon will spawn a particle when it first starts moving |
| `RenderAxis` | `TEnumAsByte < enum ETrailsRenderAxisOption >` | The 'render' axis for the trail (what axis the trail is stretched out on)<br>	 		Trails_CameraUp - Traditional camera-facing trail.<br>	 		Trails_SourceUp - Use the up axis of the source for each spawned particle.<br>	 		Trails_WorldUp  - Use the world up axis. |
| `TangentSpawningScalar` | `float` | The tangent scalar for spawning.<br>	 	Angles between tangent A and B are mapped to [0.0f .. 1.0f]<br>	 	This is then multiplied by TangentTessellationScalar to give the number of particles to spawn |
| `bRenderGeometry` | `uint32` | If true, render the trail geometry (this should typically be on) |
| `bRenderSpawnPoints` | `uint32` | If true, render stars at each spawned particle point along the trail |
| `bRenderTangents` | `uint32` | If true, render a line showing the tangent at each spawned particle point along the trail |
| `bRenderTessellation` | `uint32` | If true, render the tessellated path between spawned particles |
| `TilingDistance` | `float` | The (estimated) covered distance to tile the 2nd UV set at.<br>	 	If 0.0, a second UV set will not be passed in. |
| `DistanceTessellationStepSize` | `float` | The distance step size for tessellation.<br>	 	# Tessellation Points = TruncToInt((Distance Between Spawned Particles)  DistanceTessellationStepSize)) |
| `bEnableTangentDiffInterpScale` | `uint32` | If this flag is enabled, the system will scale the number of interpolated vertices<br>	 	based on the difference in the tangents of neighboring particles.<br>	 	Each pair of neighboring particles will compute the following CheckTangent value:<br>	 		CheckTangent = ((ParticleA Tangent DOT ParticleB Tangent) - 1.0f)  0.5f<br>	 	If CheckTangent is LESS THAN 0.5, then the DistanceTessellationStepSize will be <br>	 	scaled based on the result. This will map so that from parallel to orthogonal <br>	 	(0..90 degrees) will scale from [0..1]. Anything greater than 90 degrees will clamp <br>	 	at a scale of 1. |
| `TangentTessellationScalar` | `float` | The tangent scalar for tessellation.<br>	 	Angles between tangent A and B are mapped to [0.0f .. 1.0f]<br>	 	This is then multiplied by TangentTessellationScalar to give the number of points to tessellate |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleVectorFieldGlobal.json -->

# UParticleModuleVectorFieldGlobal

## Inheritance

`UParticleModuleVectorFieldBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bOverrideGlobalVectorFieldTightness` | `uint32` | Property override value for global vector field tightness. |
| `GlobalVectorFieldScale` | `float` | Global vector field scale. |
| `GlobalVectorFieldTightness` | `float` | Global vector field tightness override. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleVectorFieldLocal.json -->

# UParticleModuleVectorFieldLocal

## Inheritance

`UParticleModuleVectorFieldBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VectorField` | `UVectorField *` | Vector field asset to use. |
| `RelativeTranslation` | `FVector` | Translation of the vector field relative to the emitter. |
| `RelativeRotation` | `FRotator` | Rotation of the vector field relative to the emitter. |
| `RelativeScale3D` | `FVector` | Scale of the vector field relative to the emitter. |
| `Intensity` | `float` | Intensity of the local vector field. |
| `Tightness` | `float` | Tightness tweak value: 0: Force 1: Velocity. |
| `bIgnoreComponentTransform` | `uint32` | Ignore component transform. |
| `bTileX` | `uint32` | Tile vector field in x axis? |
| `bTileY` | `uint32` | Tile vector field in y axis? |
| `bTileZ` | `uint32` | Tile vector field in z axis? |
| `bUseFixDT` | `uint32` | Use fix delta time in the simulation? |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleVectorFieldRotation.json -->

# UParticleModuleVectorFieldRotation

## Inheritance

`UParticleModuleVectorFieldBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MinInitialRotation` | `FVector` | Minimum initial rotation applied to the local vector field. |
| `MaxInitialRotation` | `FVector` | Maximum initial rotation applied to the local vector field. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleVectorFieldRotationRate.json -->

# UParticleModuleVectorFieldRotationRate

## Inheritance

`UParticleModuleVectorFieldBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RotationRate` | `FVector` | Constant rotation rate applied to the local vector field. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleVectorFieldScale.json -->

# UParticleModuleVectorFieldScale

## Inheritance

`UParticleModuleVectorFieldBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VectorFieldScale_DEPRECATED` | `UDistributionFloat *` | Per-particle vector field scale. Evaluated using emitter time. |
| `VectorFieldScaleRaw` | `FRawDistributionFloat` | Per-particle vector field scale. Evaluated using emitter time. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleVectorFieldScaleOverLife.json -->

# UParticleModuleVectorFieldScaleOverLife

## Inheritance

`UParticleModuleVectorFieldBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VectorFieldScaleOverLife_DEPRECATED` | `UDistributionFloat *` | Per-particle vector field scale. Evaluated using particle relative time. |
| `VectorFieldScaleOverLifeRaw` | `FRawDistributionFloat` | Per-particle vector field scale. Evaluated using particle relative time. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleVelocity.json -->

# UParticleModuleVelocity

## Inheritance

`UParticleModuleVelocityBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartVelocity` | `FRawDistributionVector` | The velocity to apply to a particle when it is spawned.<br>	 	Value is retrieved using the EmitterTime of the emitter. |
| `StartVelocityRadial` | `FRawDistributionFloat` | The velocity to apply to a particle along its radial direction.<br>	 	Direction is determined by subtracting the location of the emitter from the particle location at spawn.<br>	 	Value is retrieved using the EmitterTime of the emitter. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleVelocity_Seeded.json -->

# UParticleModuleVelocity_Seeded

## Inheritance

`UParticleModuleVelocity`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RandomSeedInfo` | `FParticleRandomSeedInfo` | The random seed(s) to use for looking up values in StartLocation |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleVelocityBase.json -->

# UParticleModuleVelocityBase

## Inheritance

`UParticleModule`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bInWorldSpace` | `uint32` | If true, then treat the velocity as world-space defined.<br>	 	NOTE: LocalSpace emitters that are moving will see strange results... |
| `bApplyOwnerScale` | `uint32` | If true, then apply the particle system components scale to the velocity value. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleVelocityCone.json -->

# UParticleModuleVelocityCone

## Inheritance

`UParticleModuleVelocityBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Angle` | `FRawDistributionFloat` | The Min value represents the inner cone angle value and the Max value represents the outer cone angle value. |
| `Velocity` | `FRawDistributionFloat` | The initial velocity of the particles. |
| `Direction` | `FVector` | The direction FVector of the cone. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleVelocityInheritParent.json -->

# UParticleModuleVelocityInheritParent

## Inheritance

`UParticleModuleVelocityBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Scale` | `FRawDistributionVector` | The scale to apply tot he parent velocity prior to adding it to the particle velocity during spawn.<br>	 	Value is retrieved using the EmitterTime of the emitter. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleVelocityOverLifetime.json -->

# UParticleModuleVelocityOverLifetime

## Inheritance

`UParticleModuleVelocityBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VelOverLife` | `FRawDistributionVector` | The scaling  value applied to the velocity.<br>	 	Value is retrieved using the RelativeTime of the particle. |
| `Absolute` | `uint32` | If true, the velocity will be SET to the value from the above dist.<br>	 	If false, the velocity will be scaled by the above dist. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleVelocityRibbon.json -->

# UParticleModuleVelocityRibbon

## Inheritance

`UParticleModuleVelocityBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParentLinearVel` | `FRawDistributionVector` | - |
| `ParentLinearSpeed` | `FRawDistributionFloat` | - |
| `ParentAngularVel` | `FRawDistributionFloat` | - |
| `AngularSpeedEpsilon` | `float` | The scaling  value applied to the velocity.<br>	 	Value is retrieved using the RelativeTime of the particle. |
| `ParticleTurnRadiusRatio` | `float` | The scaling  value applied to the velocity.<br>	 	Value is retrieved using the RelativeTime of the particle. |
| `ParticleTurnLerp` | `bool` | - |
| `IntensityOverSpeed` | `FRawDistributionFloat` | The scaling  value applied to the velocity.<br>	 	Value is retrieved using the RelativeTime of the particle. |
| `LengthOverSpeed` | `FRawDistributionFloat` | The scaling  value applied to the velocity.<br>	 	Value is retrieved using the RelativeTime of the particle. |
| `MinRibbonBendRadius` | `float` | - |
| `MaxRibbonLength` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleSystem.json -->

# UParticleSystem

A ParticleSystem is a complete particle effect that contains any number of ParticleEmitters. By allowing multiple emitters
  in a system, the designer can create elaborate particle effects that are held in a single system. Once created using
  Cascade, a ParticleSystem can then be inserted into a level or created in script.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SystemUpdateMode` | `TEnumAsByte < enum EParticleSystemUpdateMode >` | - |
| `UpdateTime_FPS` | `float` | UpdateTime_FPS	- the frame per second to update at in FixedTime mode |
| `UpdateTime_Delta` | `float` | UpdateTime_Delta	- internal |
| `WarmupTime` | `float` | WarmupTime - the time to warm-up the particle system when first rendered	<br>	  Warning: WarmupTime is implemented by simulating the particle system for the time requested upon activation.  <br>	  This is extremely prone to cause hitches, especially with large particle counts - use with caution. |
| `WarmupTickRate` | `float` | WarmupTickRate - the time step for each tick during warm up.<br>		Set to 0 to use the default tick time. |
| `bEnableSeparateRendering` | `bool` | - |
| `Emitters` | `TArray < UParticleEmitter * >` | Emitters	- internal - the array of emitters in the system |
| `PreviewComponent` | `UParticleSystemComponent *` | The component used to preview the particle system in Cascade |
| `CurveEdSetup` | `UInterpCurveEdSetup *` | Used for curve editor to remember curve-editing setup. |
| `bOrientZAxisTowardCamera` | `uint32` | If true, the system's Z axis will be oriented toward the camera |
| `LODDistanceCheckTime` | `float` | How often (in seconds) the system should perform the LOD distance check. |
| `bUseDeviceConstBias` | `bool` | - |
| `bUseUltraDeviceBias` | `bool` | - |
| `bUseDeviceQualityBias` | `bool` | - |
| `bUsePCDeviceConstBias` | `bool` | - |
| `bUseCustomCullDistance` | `bool` | - |
| `bUseAbsoluteDistance` | `bool` | default false ,use for cull distance not affected by r.ViewDistanceScale |
| `CustomCullDistance` | `float` | default 0 ,use for mobile particle distance cull |
| `CustomPCCullDistance` | `float` | default -1 then use same distance as mobile do |
| `CullDistanceCheckTime` | `float` | - |
| `LODMethod` | `TEnumAsByte < enum ParticleSystemLODMethod >` | The method of LOD level determination to utilize for this particle system<br>	 	  PARTICLESYSTEMLODMETHOD_Automatic - Automatically set the LOD level, checking every LODDistanceCheckTime seconds.<br>	     PARTICLESYSTEMLODMETHOD_DirectSet - LOD level is directly set by the game code.<br>	     PARTICLESYSTEMLODMETHOD_ActivateAutomatic - LOD level is determined at Activation time, then left alone unless directly set by game code. |
| `LODDistances` | `TArray < float >` | The array of distances for each LOD level in the system.<br>	 	Used when LODMethod is set to PARTICLESYSTEMLODMETHOD_Automatic.<br>	 <br>	 	Example: System with 3 LOD levels<br>	 		LODDistances(0) = 0.0<br>	 		LODDistances(1) = 2500.0<br>	 		LODDistances(2) = 5000.0<br>	 <br>	 		In this case, when the system is [   0.0 ..   2499.9] from the camera, LOD level 0 will be used.<br>	 										 [2500.0 ..   4999.9] from the camera, LOD level 1 will be used.<br>	 										 [5000.0 .. INFINITY] from the camera, LOD level 2 will be used. |
| `bRegenerateLODDuplicate` | `uint32` | Internal value that tracks the regenerate LOD levels preference.<br>	 	If true, when autoregenerating LOD levels in code, the low level will<br>	 	be a duplicate of the high. |
| `LODSettings` | `TArray < struct FParticleSystemLOD >` | - |
| `bUseFixedRelativeBoundingBox` | `uint32` | Whether to use the fixed relative bounding box or calculate it every frame. |
| `FixedRelativeBoundingBox` | `FBox` | Fixed relative bounding box for particle system. |
| `SecondsBeforeInactive` | `float` | Number of seconds of emitter not being rendered that need to pass before it<br>	  no longer gets ticked becomes inactive. |
| `bShouldResetPeakCounts` | `uint32` | EDITOR ONLY: Indicates that Cascade would like to have the PeakActiveParticles count reset |
| `bHasPhysics` | `uint32` | Set during load time to indicate that physics is used... |
| `bUseRealtimeThumbnail` | `uint32` | Inidicates the old 'real-time' thumbnail rendering should be used |
| `ThumbnailImageOutOfDate` | `uint32` | Internal: Indicates the PSys thumbnail image is out of date |
| `Delay` | `float` | How long this Particle system should delay when ActivateSystem is called on it. |
| `DelayLow` | `float` | The low end of the emitter delay if using a range. |
| `bUseDelayRange` | `uint32` | If true, select the emitter delay from the range <br>	 		[DelayLow..Delay] |
| `bAllowGcCluster` | `uint8` | - |
| `bAllowRenderDataUpdateLag` | `uint8` | - |
| `bAllowManagedTicking` | `uint8` | - |
| `bAutoDeactivate` | `bool` | - |
| `MinTimeBetweenTicks` | `uint32` | - |
| `InsignificantReaction` | `EParticleSystemInsignificanceReaction` | The reaction this system takes when all emitters are insignificant. |
| `InsignificanceDelay` | `float` | Time delay between all emitters becoming insignificant and the systems insignificant reaction. |
| `MaxSignificanceLevel` | `EParticleSignificanceLevel` | The maximum level of significance for emitters in this system. Any emitters with a higher significance will be capped at this significance level. |
| `bAllowTickOptimization` | `uint8` | - |
| `bAllowSlowTickWhenInVisiable` | `uint8` | - |
| `bAllowSlowTickWhenFarAway` | `uint8` | - |
| `MacroUVPosition` | `FVector` | Local space position that UVs generated with the ParticleMacroUV material node will be centered on. |
| `MacroUVRadius` | `float` | World space radius that UVs generated with the ParticleMacroUV material node will tile based on. |
| `OcclusionBoundsMethod` | `TEnumAsByte < enum EParticleSystemOcclusionBoundsMethod >` | Which occlusion bounds method to use for this particle system.<br>	 	EPSOBM_None - Don't determine occlusion for this system.<br>	 	EPSOBM_ParticleBounds - Use the bounds of the component when determining occlusion. |
| `CustomOcclusionBounds` | `FBox` | The occlusion bounds to use if OcclusionBoundsMethod is set to EPSOBM_CustomBounds |
| `SoloTracking` | `TArray < struct FLODSoloTrack >` | - |
| `NamedMaterialSlots` | `TArray < FNamedEmitterMaterial >` | Array of named material slots for use by emitters of this system. <br>		Emitters can use these instead of their own materials by providing the name to the NamedMaterialOverrides property of their required module.<br>		These materials can be overridden using CreateNamedDynamicMaterialInstance() on a ParticleSystemComponent. |
| `bInitParticlesOnCanNotEverRender` | `uint8` | - |
| `AvailableDeviceLevel` | `int32` | - |

## Functions

### `ContainsEmitterType`

```text
ContainsEmitterType(TypeData: UClass *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TypeData` | `UClass *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleSystemComponent.json -->

# UParticleSystemComponent

A particle emitter.

## Inheritance

`UPrimitiveComponent` -> `IWTACAggregateInterface` -> `IObjectPoolInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TemplateBindingType` | `EParticleTemplateBindingType` | - |
| `Template` | `UParticleSystem *` | - |
| `SoftTemplate` | `TSoftObjectPtr < UParticleSystem >` | - |
| `EmitterMaterials` | `TArray < UMaterialInterface * >` | - |
| `SkelMeshComponents` | `TArray < USkeletalMeshComponent * >` | The skeletal mesh components used with the socket location module.<br>	 	This is to prevent them from being garbage collected. |
| `bResetOnDetach` | `uint8` | - |
| `bUpdateOnDedicatedServer` | `uint8` | whether to update the particle system on dedicated servers |
| `bAllowRecycling` | `uint8` | If true, this Particle System will be available for recycling after it has completed. Auto-destroyed systems cannot be recycled.<br>	  Some systems (currently particle trail effects) can recycle components to avoid respawning them to play new effects.<br>	  This is only an optimization and does not change particle system behavior, aside from not triggering normal component initialization events more than once. |
| `bAutoManageAttachment` | `uint8` | True if we should automatically attach to AutoAttachParent when activated, and detach from our parent when completed.<br>	  This overrides any current attachment that may be present at the time of activation (deferring initial attachment until activation, if AutoAttachParent is null).<br>	  When enabled, detachment occurs regardless of whether AutoAttachParent is assigned, and the relative transform from the time of activation is restored.<br>	  This also disables attachment on dedicated servers, where we don't actually activate even if bAutoActivate is true.<br>	  @see AutoAttachParent, AutoAttachSocketName, AutoAttachLocationType |
| `bWarmingUp` | `uint8` | - |
| `bOverrideLODMethod` | `uint8` | indicates that the component's LODMethod overrides the Template's |
| `bSkipUpdateDynamicDataDuringTick` | `uint8` | Flag indicating that dynamic updating of render data should NOT occur during Tick.<br>	 	This is used primarily to allow for warming up and simulated effects to a certain state. |
| `LODMethod` | `TEnumAsByte < enum ParticleSystemLODMethod >` | The method of LOD level determination to utilize for this particle system |
| `RequiredSignificance` | `EParticleSignificanceLevel` | The significance this component requires of it's emitters for them to be enabled. |
| `bShouldUseTagGetSkeletalMesh` | `bool` | Array holding name instance parameters for this ParticleSystemComponent.<br>	 	Parameters can be used in Cascade using DistributionFloatVectorParticleParameters. |
| `SkeletalMeshTagName` | `FName` | - |
| `InstanceParameters` | `TArray < FParticleSysParam >` | - |
| `OnParticleSpawn` | `FParticleSpawnSignature` | - |
| `OnParticleBurst` | `FParticleBurstSignature` | - |
| `OnParticleDeath` | `FParticleDeathSignature` | - |
| `OnParticleCollide` | `FParticleCollisionSignature` | - |
| `OldPosition` | `FVector` | - |
| `PartSysVelocity` | `FVector` | - |
| `WarmupTime` | `float` | - |
| `WarmupTickRate` | `float` | - |
| `OverrideEmitterMeshDataMap` | `TMap < FName , UStaticMesh * >` | - |
| `SecondsBeforeInactive` | `float` | Number of seconds of emitter not being rendered that need to pass before it<br>	  no longer gets ticked becomes inactive. |
| `MaxTimeBeforeForceUpdateTransform` | `float` | Time between forced UpdateTransforms for systems that use dynamically calculated bounds,<br>	  Which is effectively how often the bounds are shrunk. |
| `ReplayClips` | `TArray < UParticleSystemReplay * >` | Array of replay clips for this particle system component.  These are serialized to disk.  You really should never add anything to this in the editor.  It's exposed so that you can delete clips if you need to, but be careful when doing so! |
| `CustomTimeDilation` | `float` | Scales DeltaTime in UParticleSystemComponent::Tick(...) |
| `bIsPCPlatformResource` | `bool` | Is PC Redirect Particle Resource |
| `AutoAttachParent` | `TWeakObjectPtr < USceneComponent >` | Component we automatically attach to when activated, if bAutoManageAttachment is true.<br>	  If null during registration, we assign the existing AttachParent and defer attachment until we activate.<br>	  @see bAutoManageAttachment |
| `AutoAttachSocketName` | `FName` | Socket we automatically attach to on the AutoAttachParent, if bAutoManageAttachment is true.<br>	  @see bAutoManageAttachment |
| `AutoAttachLocationRule` | `EAttachmentRule` | Options for how we handle our location when we attach to the AutoAttachParent, if bAutoManageAttachment is true.<br>	  @see bAutoManageAttachment, EAttachmentRule |
| `AutoAttachRotationRule` | `EAttachmentRule` | Options for how we handle our rotation when we attach to the AutoAttachParent, if bAutoManageAttachment is true.<br>	  @see bAutoManageAttachment, EAttachmentRule |
| `AutoAttachScaleRule` | `EAttachmentRule` | Options for how we handle our scale when we attach to the AutoAttachParent, if bAutoManageAttachment is true.<br>	  @see bAutoManageAttachment, EAttachmentRule |
| `bForceNoAsync` | `bool` | - |
| `SystemFixedWorldBounds` | `FBox` | - |
| `SystemFixedLocalBounds` | `FBox` | - |
| `CollisionIgnoreActorList` | `TArray < AActor * >` | - |
| `CollisionIgnoreComponentList` | `TArray < UPrimitiveComponent * >` | - |
| `CollisionIgnoreInfoLastClearTime` | `float` | - |
| `EditorLODLevel` | `int32` | INTERNAL. Used by the editor to set the LODLevel |
| `EditorDetailMode` | `int32` | Used for applying Cascade's detail mode setting to in-level particle systems |
| `AutoAttachLocationType_DEPRECATED` | `TEnumAsByte < EAttachLocation :: Type >` | DEPRECATED: Options for how we handle our location when we attach to the AutoAttachParent, if bAutoManageAttachment is true.<br>	  @see bAutoManageAttachment, EAttachLocation::Type |

## Functions

### `GetDuration`

```text
GetDuration() -> float
```

Returns duration

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetSystemFixedWorldBounds`

```text
SetSystemFixedWorldBounds(WorldBounds: FBox) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldBounds` | `FBox` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSystemFixedLocalBounds`

```text
SetSystemFixedLocalBounds(LocalBounds: FBox) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LocalBounds` | `FBox` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearSystemFixedBounds`

```text
ClearSystemFixedBounds() -> void
```

Clear any previously set fixed bounds for the system instance.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWarmUp`

```text
SetWarmUp(WarmUpTime: float, WarmUpRate: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WarmUpTime` | `float` | - |
| `WarmUpRate` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAutoAttachParams`

```text
SetAutoAttachParams(Parent: USceneComponent *, SocketName: FName, LocationType: EAttachLocation :: Type) -> void
```

DEPRECATED: Set AutoAttachParent, AutoAttachSocketName, AutoAttachLocationType to the specified parameters. Does not change bAutoManageAttachment; that must be set separately.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Parent` | `USceneComponent *` | Component to attach to. |
| `SocketName` | `FName` | Socket on Parent to attach to. |
| `LocationType` | `EAttachLocation :: Type` | Option for how we handle our location when we attach to Parent. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAutoAttachmentParameters`

```text
SetAutoAttachmentParameters(Parent: USceneComponent *, SocketName: FName, LocationRule: EAttachmentRule, RotationRule: EAttachmentRule, ScaleRule: EAttachmentRule) -> void
```

Set AutoAttachParent, AutoAttachSocketName, AutoAttachLocationRule, AutoAttachRotationRule, AutoAttachScaleRule to the specified parameters. Does not change bAutoManageAttachment; that must be set separately.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Parent` | `USceneComponent *` | Component to attach to. |
| `SocketName` | `FName` | Socket on Parent to attach to. |
| `LocationRule` | `EAttachmentRule` | Option for how we handle our location when we attach to Parent. |
| `RotationRule` | `EAttachmentRule` | Option for how we handle our rotation when we attach to Parent. |
| `ScaleRule` | `EAttachmentRule` | Option for how we handle our scale when we attach to Parent. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBeamEndPoint`

```text
SetBeamEndPoint(EmitterIndex: int32, NewEndPoint: FVector) -> void
```

Set the beam end point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to set it on |
| `NewEndPoint` | `FVector` | The value to set it to |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBeamSourcePoint`

```text
SetBeamSourcePoint(EmitterIndex: int32, NewSourcePoint: FVector, SourceIndex: int32) -> void
```

Set the beam source point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to set it on |
| `NewSourcePoint` | `FVector` | The value to set it to |
| `SourceIndex` | `int32` | Which beam within the emitter to set it on |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBeamSourceTangent`

```text
SetBeamSourceTangent(EmitterIndex: int32, NewTangentPoint: FVector, SourceIndex: int32) -> void
```

Set the beam source tangent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to set it on |
| `NewTangentPoint` | `FVector` | The value to set it to |
| `SourceIndex` | `int32` | Which beam within the emitter to set it on |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBeamSourceStrength`

```text
SetBeamSourceStrength(EmitterIndex: int32, NewSourceStrength: float, SourceIndex: int32) -> void
```

Set the beam source strength

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to set it on |
| `NewSourceStrength` | `float` | The value to set it to |
| `SourceIndex` | `int32` | Which beam within the emitter to set it on |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBeamTargetPoint`

```text
SetBeamTargetPoint(EmitterIndex: int32, NewTargetPoint: FVector, TargetIndex: int32) -> void
```

Set the beam target point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to set it on |
| `NewTargetPoint` | `FVector` | The value to set it to |
| `TargetIndex` | `int32` | Which beam within the emitter to set it on |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBeamTargetTangent`

```text
SetBeamTargetTangent(EmitterIndex: int32, NewTangentPoint: FVector, TargetIndex: int32) -> void
```

Set the beam target tangent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to set it on |
| `NewTangentPoint` | `FVector` | The value to set it to |
| `TargetIndex` | `int32` | Which beam within the emitter to set it on |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBeamTargetStrength`

```text
SetBeamTargetStrength(EmitterIndex: int32, NewTargetStrength: float, TargetIndex: int32) -> void
```

Set the beam target strength

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to set it on |
| `NewTargetStrength` | `float` | The value to set it to |
| `TargetIndex` | `int32` | Which beam within the emitter to set it on |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBeamEndPoint`

```text
GetBeamEndPoint(EmitterIndex: int32, OutEndPoint: FVector &) -> bool
```

Get the beam end point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to get the value of |
| `OutEndPoint` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true		EmitterIndex is valid and End point is set - OutEndPoint is valid |

### `GetBeamSourcePoint`

```text
GetBeamSourcePoint(EmitterIndex: int32, SourceIndex: int32, OutSourcePoint: FVector &) -> bool
```

Get the beam source point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to get |
| `SourceIndex` | `int32` | Which beam within the emitter to get |
| `OutSourcePoint` | `FVector &` | Value of source point |

**Returns**

| Type | Description |
|---|---|
| `bool` | true		EmitterIndex and SourceIndex are valid - OutSourcePoint is valid |

### `GetBeamSourceTangent`

```text
GetBeamSourceTangent(EmitterIndex: int32, SourceIndex: int32, OutTangentPoint: FVector &) -> bool
```

Get the beam source tangent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to get |
| `SourceIndex` | `int32` | Which beam within the emitter to get |
| `OutTangentPoint` | `FVector &` | Value of source tangent |

**Returns**

| Type | Description |
|---|---|
| `bool` | true		EmitterIndex and SourceIndex are valid - OutTangentPoint is valid |

### `GetBeamSourceStrength`

```text
GetBeamSourceStrength(EmitterIndex: int32, SourceIndex: int32, OutSourceStrength: float &) -> bool
```

Get the beam source strength

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to get |
| `SourceIndex` | `int32` | Which beam within the emitter to get |
| `OutSourceStrength` | `float &` | Value of source tangent |

**Returns**

| Type | Description |
|---|---|
| `bool` | true		EmitterIndex and SourceIndex are valid - OutSourceStrength is valid |

### `GetBeamTargetPoint`

```text
GetBeamTargetPoint(EmitterIndex: int32, TargetIndex: int32, OutTargetPoint: FVector &) -> bool
```

Get the beam target point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to get |
| `TargetIndex` | `int32` | Which beam within the emitter to get |
| `OutTargetPoint` | `FVector &` | Value of target point |

**Returns**

| Type | Description |
|---|---|
| `bool` | true		EmitterIndex and TargetIndex are valid - OutTargetPoint is valid |

### `GetBeamTargetTangent`

```text
GetBeamTargetTangent(EmitterIndex: int32, TargetIndex: int32, OutTangentPoint: FVector &) -> bool
```

Get the beam target tangent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to get |
| `TargetIndex` | `int32` | Which beam within the emitter to get |
| `OutTangentPoint` | `FVector &` | Value of target tangent |

**Returns**

| Type | Description |
|---|---|
| `bool` | true		EmitterIndex and TargetIndex are valid - OutTangentPoint is valid |

### `GetBeamTargetStrength`

```text
GetBeamTargetStrength(EmitterIndex: int32, TargetIndex: int32, OutTargetStrength: float &) -> bool
```

Get the beam target strength

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to get |
| `TargetIndex` | `int32` | Which beam within the emitter to get |
| `OutTargetStrength` | `float &` | Value of target tangent |

**Returns**

| Type | Description |
|---|---|
| `bool` | true		EmitterIndex and TargetIndex are valid - OutTargetStrength is valid |

### `SetEmitterEnable`

```text
SetEmitterEnable(EmitterName: FName, bNewEnableState: bool) -> void
```

EnablesDisables a sub-emitter

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterName` | `FName` | The name of the sub-emitter to set it on |
| `bNewEnableState` | `bool` | The value to set it to |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFloatParameter`

```text
SetFloatParameter(ParameterName: FName, Param: float) -> void
```

Change a named float parameter

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVectorParameter`

```text
SetVectorParameter(ParameterName: FName, Param: FVector) -> void
```

Set a named vector instance parameter on this ParticleSystemComponent.
	 	Updates the parameter if it already exists, or creates a new entry if not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetColorParameter`

```text
SetColorParameter(ParameterName: FName, Param: FLinearColor) -> void
```

Set a named color instance parameter on this ParticleSystemComponent.
	 	Updates the parameter if it already exists, or creates a new entry if not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetActorParameter`

```text
SetActorParameter(ParameterName: FName, Param: AActor *) -> void
```

Set a named actor instance parameter on this ParticleSystemComponent.
	 	Updates the parameter if it already exists, or creates a new entry if not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMaterialParameter`

```text
SetMaterialParameter(ParameterName: FName, Param: UMaterialInterface *) -> void
```

Set a named material instance parameter on this ParticleSystemComponent.
	 	Updates the parameter if it already exists, or creates a new entry if not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTemplate`

```text
SetTemplate(NewTemplate: UParticleSystem *) -> void
```

Change the ParticleSystem used by this ParticleSystemComponent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTemplate` | `UParticleSystem *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetNumActiveParticles`

```text
GetNumActiveParticles() -> int32
```

Get the current number of active particles in this system

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `BeginTrails`

```text
BeginTrails(InFirstSocketName: FName, InSecondSocketName: FName, InWidthMode: ETrailWidthMode, InWidth: float) -> void
```

Begins all trail emitters in this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFirstSocketName` | `FName` | The name of the first socket for the trail. |
| `InSecondSocketName` | `FName` | The name of the second socket for the trail. |
| `InWidthMode` | `ETrailWidthMode` | How the width value is applied to the trail. |
| `InWidth` | `float` | The width of the trail. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EndTrails`

```text
EndTrails() -> void
```

Ends all trail emitters in this component.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTrailSourceData`

```text
SetTrailSourceData(InFirstSocketName: FName, InSecondSocketName: FName, InWidthMode: ETrailWidthMode, InWidth: float) -> void
```

Sets the defining data for all trails in this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFirstSocketName` | `FName` | The name of the first socket for the trail. |
| `InSecondSocketName` | `FName` | The name of the second socket for the trail. |
| `InWidthMode` | `ETrailWidthMode` | How the width value is applied to the trail. |
| `InWidth` | `float` | The width of the trail. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSocketName`

```text
SetSocketName(InSocketName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocketName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ManuallyTickComponent`

```text
ManuallyTickComponent(DeltaTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_Activate`

```text
K2_Activate(bReset: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bReset` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_ActivateSystem`

```text
K2_ActivateSystem(bFlagAsJustAttached: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bFlagAsJustAttached` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_Deactivate`

```text
K2_Deactivate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DeactivateSystem`

```text
K2_DeactivateSystem() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CreateNamedDynamicMaterialInstance`

```text
CreateNamedDynamicMaterialInstance(InName: FName, SourceMaterial: UMaterialInterface *) -> UMaterialInstanceDynamic *
```

Creates a Dynamic Material Instance for the specified named material override, optionally from the supplied material.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InName` | `FName` | - |
| `SourceMaterial` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | - |

### `GetNamedMaterial`

```text
GetNamedMaterial(InName: FName) -> UMaterialInterface *
```

Returns a named material. If this named material is not found, returns NULL.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UMaterialInterface *` | - |

### `GenerateParticleEvent`

```text
GenerateParticleEvent(InEventName: FName, InEmitterTime: float, InLocation: FVector, InDirection: FVector, InVelocity: FVector) -> void
```

Record a kismet event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InEventName` | `FName` | The name of the event that fired. |
| `InEmitterTime` | `float` | The emitter time when the event fired. |
| `InLocation` | `FVector` | The location of the particle when the event fired. |
| `InDirection` | `FVector` | - |
| `InVelocity` | `FVector` | The velocity of the particle when the event fired. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVectorRandParameter`

```text
SetVectorRandParameter(ParameterName: FName, Param: FVector &, ParamLow: FVector &) -> void
```

Set a named random vector instance parameter on this ParticleSystemComponent.
	 	Updates the parameter if it already exists, or creates a new entry if not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `FVector &` | - |
| `ParamLow` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFloatRandParameter`

```text
SetFloatRandParameter(ParameterName: FName, Param: float, ParamLow: float) -> void
```

Set a named random float instance parameter on this ParticleSystemComponent.
	 	Updates the parameter if it already exists, or creates a new entry if not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `float` | - |
| `ParamLow` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RewindEmitterInstances`

```text
RewindEmitterInstances() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnSystemFinished`

```text
OnSystemFinished(PSystem: UParticleSystemComponent*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PSystem` | `UParticleSystemComponent*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UParticleSystemReplay.json -->

# UParticleSystemReplay

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ClipIDNumber` | `int32` | Unique ID number for this replay clip |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPartTypeSocket.json -->

# UPartTypeSocket

## Inheritance

`USkeletalMeshSocket`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PartType` | `uint8` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPathFollowingComponent.json -->

# UPathFollowingComponent

## Inheritance

`UActorComponent` -> `IAIResourceInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MovementComp` | `UNavMovementComponent *` | associated movement component |
| `MyNavData` | `ANavigationData *` | navigation data for agent described in movement component |

## Functions

### `OnActorBump`

```text
OnActorBump(SelfActor: AActor *, OtherActor: AActor *, NormalImpulse: FVector, Hit: FHitResult &) -> void
```

called when moving agent collides with another actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelfActor` | `AActor *` | - |
| `OtherActor` | `AActor *` | - |
| `NormalImpulse` | `FVector` | - |
| `Hit` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPathActionType`

```text
GetPathActionType() -> EPathFollowingAction :: Type
```

**Returns**

| Type | Description |
|---|---|
| `EPathFollowingAction :: Type` | - |

### `GetPathDestination`

```text
GetPathDestination() -> FVector
```

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `OnNavDataRegistered`

```text
OnNavDataRegistered(NavData: ANavigationData *) -> void
```

called when NavigationSystem registers new navigation data type while this component
	 	instance has empty MyNavData. This is usually the case for AI agents hand-placed
	 	on levels.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NavData` | `ANavigationData *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPathNameMappingDataAsset.json -->

# UPathNameMappingDataAsset

## Inheritance

`UDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VersionID` | `int32` | - |
| `AllPathNameMapForLoad` | `TArray < FName >` | - |
| `AllPathNameMapForWrite` | `TMap < FName , int32 >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPathNameMappingManager.json -->

# UPathNameMappingManager

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PathNameMappingDataAsset` | `UPathNameMappingDataAsset *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPawnAction.json -->

# UPawnAction

Things to remember:
 	 Actions are created paused

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ChildAction` | `UPawnAction *` | Current child node executing on top of this Action |
| `ParentAction` | `UPawnAction *` | - |
| `OwnerComponent` | `UPawnActionsComponent *` | Extra reference to the component this action is being governed by |
| `Instigator` | `UObject *` | indicates an object that caused this action. Used for mass removal of actions <br>	 	by specific object |
| `BrainComp` | `UBrainComponent *` | @Note: THIS IS HERE _ONLY_ BECAUSE OF THE WAY AI MESSAGING IS CURRENTLY IMPLEMENTED. WILL GO AWAY! |
| `bAllowNewSameClassInstance` | `uint32` | if this is FALSE and we're trying to push a new instance of a given class,<br>	 	but the top of the stack is already an instance of that class ignore the attempted push |
| `bReplaceActiveSameClassInstance` | `uint32` | if this is TRUE, when we try to push a new instance of an action who has the<br>	 	same class as the action on the top of the stack, pop the one on the stack, and push the new one<br>	 	NOTE: This trumps bAllowNewClassInstance (e.g. if this is true and bAllowNewClassInstance<br>	 	is false the active instance will still be replaced) |
| `bShouldPauseMovement` | `uint32` | this is a temporary solution to allow having movement action running in background while there's <br>	 	another action on top doing its thing<br>	 	@note should go away once AI resource locking comes on-line |
| `bAlwaysNotifyOnFinished` | `uint32` | if set, action will call OnFinished notify even when ending as FailedToStart |

## Functions

### `GetActionPriority`

```text
GetActionPriority() -> TEnumAsByte < EAIRequestPriority :: Type >
```

**Returns**

| Type | Description |
|---|---|
| `TEnumAsByte < EAIRequestPriority :: Type >` | - |

### `CreateActionInstance`

```text
CreateActionInstance(WorldContextObject: UObject *, ActionClass: TSubclassOf < UPawnAction >) -> UPawnAction *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ActionClass` | `TSubclassOf < UPawnAction >` | - |

**Returns**

| Type | Description |
|---|---|
| `UPawnAction *` | - |

### `Finish`

```text
Finish(WithResult: TEnumAsByte < EPawnActionResult :: Type >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WithResult` | `TEnumAsByte < EPawnActionResult :: Type >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPawnAction_BlueprintBase.json -->

# UPawnAction_BlueprintBase

## Inheritance

`UPawnAction`

## Functions

### `ActionStart`

```text
ActionStart(ControlledPawn: APawn *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ActionTick`

```text
ActionTick(ControlledPawn: APawn *, DeltaSeconds: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ControlledPawn` | `APawn *` | - |
| `DeltaSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ActionPause`

```text
ActionPause(ControlledPawn: APawn *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ActionResume`

```text
ActionResume(ControlledPawn: APawn *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ActionFinished`

```text
ActionFinished(ControlledPawn: APawn *, WithResult: EPawnActionResult :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ControlledPawn` | `APawn *` | - |
| `WithResult` | `EPawnActionResult :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPawnAction_Move.json -->

# UPawnAction_Move

## Inheritance

`UPawnAction`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GoalActor` | `AActor *` | - |
| `GoalLocation` | `FVector` | - |
| `AcceptableRadius` | `float` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | "None" will result in default filter being used |
| `bAllowStrafe` | `uint32` | - |
| `bFinishOnOverlap` | `uint32` | if set to true (default) will make action succeed when the pawn's collision component overlaps with goal's collision component |
| `bUsePathfinding` | `uint32` | if set, movement will use path finding |
| `bAllowPartialPath` | `uint32` | if set, use incomplete path when goal can't be reached |
| `bProjectGoalToNavigation` | `uint32` | if set, GoalLocation will be projected on navigation before using |
| `bUpdatePathToGoal` | `uint32` | if set, path to GoalActor will be updated with goal's movement |
| `bAbortChildActionOnPathChange` | `uint32` | if set, other actions with the same priority will be aborted when path is changed |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPawnAction_Repeat.json -->

# UPawnAction_Repeat

## Inheritance

`UPawnAction`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActionToRepeat` | `UPawnAction *` | Action to repeat. This instance won't really be run, it's a source for copying actions to be actually performed |
| `RecentActionCopy` | `UPawnAction *` | - |
| `ChildFailureHandlingMode` | `TEnumAsByte < EPawnActionFailHandling :: Type >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPawnAction_Sequence.json -->

# UPawnAction_Sequence

## Inheritance

`UPawnAction`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActionSequence` | `TArray < UPawnAction * >` | - |
| `ChildFailureHandlingMode` | `TEnumAsByte < EPawnActionFailHandling :: Type >` | - |
| `RecentActionCopy` | `UPawnAction *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPawnAction_Wait.json -->

# UPawnAction_Wait

uses system timers rather then ticking

## Inheritance

`UPawnAction`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TimeToWait` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPawnActionsComponent.json -->

# UPawnActionsComponent

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ControlledPawn` | `APawn *` | - |
| `ActionStacks` | `TArray < FPawnActionStack >` | - |
| `ActionEvents` | `TArray < FPawnActionEvent >` | - |
| `CurrentAction` | `UPawnAction *` | - |

## Functions

### `K2_PerformAction`

```text
K2_PerformAction(Pawn: APawn *, Action: UPawnAction *, Priority: TEnumAsByte < EAIRequestPriority :: Type >) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Pawn` | `APawn *` | - |
| `Action` | `UPawnAction *` | - |
| `Priority` | `TEnumAsByte < EAIRequestPriority :: Type >` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `K2_PushAction`

```text
K2_PushAction(NewAction: UPawnAction *, Priority: EAIRequestPriority :: Type, Instigator: UObject *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAction` | `UPawnAction *` | - |
| `Priority` | `EAIRequestPriority :: Type` | - |
| `Instigator` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `K2_AbortAction`

```text
K2_AbortAction(ActionToAbort: UPawnAction *) -> EPawnActionAbortState :: Type
```

Aborts given action instance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActionToAbort` | `UPawnAction *` | - |

**Returns**

| Type | Description |
|---|---|
| `EPawnActionAbortState :: Type` | - |

### `K2_ForceAbortAction`

```text
K2_ForceAbortAction(ActionToAbort: UPawnAction *) -> EPawnActionAbortState :: Type
```

Aborts given action instance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActionToAbort` | `UPawnAction *` | - |

**Returns**

| Type | Description |
|---|---|
| `EPawnActionAbortState :: Type` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPawnMovementComponent.json -->

# UPawnMovementComponent

PawnMovementComponent can be used to update movement for an associated Pawn.
  It also provides ways to accumulate and read directional input in a generic way (with AddInputVector(), ConsumeInputVector(), etc).
  @see APawn

## Inheritance

`UNavMovementComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PawnOwner` | `APawn *` | Pawn that owns this component. |

## Functions

### `AddInputVector`

```text
AddInputVector(WorldVector: FVector, bForce: bool) -> void
```

Adds the given vector to the accumulated input in world space. Input vectors are usually between 0 and 1 in magnitude. 
	  They are accumulated during a frame then applied as acceleration during the movement update.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldVector` | `FVector` | - |
| `bForce` | `bool` | If true always add the input, ignoring the result of IsMoveInputIgnored(). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPendingInputVector`

```text
GetPendingInputVector() -> FVector
```

Return the pending input vector in world space. This is the most up-to-date value of the input vector, pending ConsumeMovementInputVector() which clears it.
	  PawnMovementComponents implementing movement usually want to use either this or ConsumeInputVector() as these functions represent the most recent state of input.

**Returns**

| Type | Description |
|---|---|
| `FVector` | The pending input vector in world space. |

### `GetLastInputVector`

```text
GetLastInputVector() -> FVector
```

Return the last input vector in world space that was processed by ConsumeInputVector(), which is usually done by the Pawn or PawnMovementComponent.
	 Any user that needs to know about the input that last affected movement should use this function.

**Returns**

| Type | Description |
|---|---|
| `FVector` | The last input vector in world space that was processed by ConsumeInputVector(). |

### `ConsumeInputVector`

```text
ConsumeInputVector() -> FVector
```

Returns the pending input vector and resets it to zero.
	  This should be used during a movement update (by the Pawn or PawnMovementComponent) to prevent accumulation of control input between frames.
	  Copies the pending input vector to the saved input vector (GetLastMovementInputVector()).

**Returns**

| Type | Description |
|---|---|
| `FVector` | The pending input vector. |

### `IsMoveInputIgnored`

```text
IsMoveInputIgnored() -> bool
```

Helper to see if move input is ignored. If there is no Pawn or UpdatedComponent, returns true, otherwise defers to the Pawn's implementation of IsMoveInputIgnored().

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetPawnOwner`

```text
GetPawnOwner() -> APawn *
```

Return the Pawn that owns UpdatedComponent.

**Returns**

| Type | Description |
|---|---|
| `APawn *` | - |

### `K2_GetInputVector`

```text
K2_GetInputVector() -> FVector
```

(Deprecated) Return the input vector in world space.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPawnNoiseEmitterComponent.json -->

# UPawnNoiseEmitterComponent

PawnNoiseEmitterComponent tracks noise event data used by SensingComponents to hear a Pawn.
  This component is intended to exist on either a Pawn or its Controller. It does nothing on network clients.

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bAIPerceptionSystemCompatibilityMode` | `uint32` | - |
| `LastRemoteNoisePosition` | `FVector` | - |
| `NoiseLifetime` | `float` | - |
| `LastRemoteNoiseVolume` | `float` | - |
| `LastRemoteNoiseTime` | `float` | - |
| `LastLocalNoiseVolume` | `float` | - |
| `LastLocalNoiseTime` | `float` | - |

## Functions

### `MakeNoise`

```text
MakeNoise(NoiseMaker: AActor *, Loudness: float, NoiseLocation: FVector &) -> void
```

Cache noises instigated by the owning pawn for AI sensing

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NoiseMaker` | `AActor *` | - is the actual actor which made the noise |
| `Loudness` | `float` | - is the relative loudness of the noise (0.0 to 1.0) |
| `NoiseLocation` | `FVector &` | - is the position of the noise |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPawnSensingComponent.json -->

# UPawnSensingComponent

SensingComponent encapsulates sensory (ie sight and hearing) settings and functionality for an Actor,
  allowing the actor to seehear Pawns in the world. It does nothing on network clients.

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `HearingThreshold` | `float` | Max distance at which a makenoise(1.0) loudness sound can be heard, regardless of occlusion |
| `LOSHearingThreshold` | `float` | Max distance at which a makenoise(1.0) loudness sound can be heard if unoccluded (LOSHearingThreshold should be > HearingThreshold) |
| `SightRadius` | `float` | Maximum sight distance. |
| `SensingInterval` | `float` | Amount of time between pawn sensing updates. Use SetSensingInterval() to adjust this at runtime. A value <= 0 prevents any updates. |
| `HearingMaxSoundAge` | `float` | - |
| `bEnableSensingUpdates` | `uint32` | If true, component will perform sensing updates. At runtime change this using SetSensingUpdatesEnabled(). |
| `bOnlySensePlayers` | `uint32` | If true, will only sense player-controlled pawns in the world. Default: true |
| `bSeePawns` | `uint32` | If true, we will perform visibility tests and will trigger notifications when a Pawn is visible. Default: true |
| `bHearNoises` | `uint32` | If true, we will perform audibility tests and will be notified when a Pawn makes a noise that can be heard. Default: true<br>	  IMPORTANT NOTE: If we can see pawns (bSeePawns is true), and the pawn is visible, noise notifications are not triggered. |
| `PeripheralVisionAngle` | `float` | How far to the side AI can see, in degrees. Use SetPeripheralVisionAngle to change the value at runtime. |
| `PeripheralVisionCosine` | `float` | Cosine of limits of peripheral vision. Computed from PeripheralVisionAngle. |

## Functions

### `SetSensingInterval`

```text
SetSensingInterval(NewSensingInterval: float) -> void
```

Changes the SensingInterval.
	  If we are currently waiting for an interval, this can either extend or shorten that interval.
	  A value <= 0 prevents any updates.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewSensingInterval` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSensingUpdatesEnabled`

```text
SetSensingUpdatesEnabled(bEnabled: bool) -> void
```

Enables or disables sensing updates. The timer is reset in either case.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPeripheralVisionAngle`

```text
SetPeripheralVisionAngle(NewPeripheralVisionAngle: float) -> void
```

Sets PeripheralVisionAngle. Calculates PeripheralVisionCosine from PeripheralVisionAngle

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPeripheralVisionAngle` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPeripheralVisionAngle`

```text
GetPeripheralVisionAngle() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetPeripheralVisionCosine`

```text
GetPeripheralVisionCosine() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

## Delegates

### `OnSeePawn`

```text
OnSeePawn(Pawn: APawn*) -> void
```

Delegate to execute when we see a Pawn.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Pawn` | `APawn*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnHearNoise`

```text
OnHearNoise(Instigator: APawn*, Location: const FVector&, Volume: float) -> void
```

Delegate to execute when we hear a noise from a Pawn's PawnNoiseEmitterComponent.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Instigator` | `APawn*` | - |
| `Location` | `const FVector&` | - |
| `Volume` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPendingNetGame.json -->

# UPendingNetGame

## Inheritance

`UObject` -> `FNetworkNotify`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NetDriver` | `UNetDriver *` | Net driver created for contacting the new server<br>	  Transferred to world on successful connection |
| `DemoNetDriver` | `UDemoNetDriver *` | Demo Net driver created for loading demos, but we need to go through pending net game<br>	  Transferred to world on successful connection |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPersistBaseComponent.json -->

# UPersistBaseComponent

技能Buff组件

## Inheritance

`UGameplayTasksComponent` -> `IObjectPoolInterface`

## Functions

### `RegisterPersistEffectWithSlot`

```text
RegisterPersistEffectWithSlot(Slot: FGameplayTag, InPE: UPersistEffectBase *, bShouldUnapply: bool) -> bool
```

生效范围：服务器
	  将PersistEffect注册到目标槽位中

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Slot` | `FGameplayTag` | 槽位 |
| `InPE` | `UPersistEffectBase *` | 注册到槽位的PersistEffect |
| `bShouldUnapply` | `bool` | 是否将原来槽位上的PersistEffect进行Unapply |

**Returns**

| Type | Description |
|---|---|
| `bool` | 注册是否成功 |

### `UnRegisterPersistEffectWithSlot`

```text
UnRegisterPersistEffectWithSlot(Slot: FGameplayTag, bShouldUnapply: bool) -> bool
```

生效范围：服务器
	  将目标槽位中的PersistEffect解除注册

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Slot` | `FGameplayTag` | 槽位 |
| `bShouldUnapply` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | 解除注册是否成功 |

### `GetPersistEffectBySlot`

```text
GetPersistEffectBySlot(Slot: FGameplayTag) -> SHADOWTRACKEREXTRA_API UPersistEffectBase *
```

生效范围：服务器&客户端
	  获取目标槽位中的PersistEffect

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Slot` | `FGameplayTag` | 槽位 |

**Returns**

| Type | Description |
|---|---|
| `SHADOWTRACKEREXTRA_API UPersistEffectBase *` | 槽位上的PersistEffect |

## Delegates

### `DynamicStateEnterHandle`

```text
DynamicStateEnterHandle(SelfRef: UPersistBaseComponent*, state: FGameplayTag) -> void
```

Event
	  生效范围：服务器&客户端
	  进入状态事件, 注意：服务端DynamicState是有计数的, 服务端多次EnterDynamicState都会触发这个代理

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelfRef` | `UPersistBaseComponent*` | 监听的组件 |
| `state` | `FGameplayTag` | 进入的状态 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DynamicStateLeaveHandle`

```text
DynamicStateLeaveHandle(SelfRef: UPersistBaseComponent*, state: FGameplayTag) -> void
```

Event
      生效范围：服务器&客户端
      离开状态事件, 注意：服务端DynamicState是有计数的, 服务端多次LeaveDynamicState都会触发这个代理, 只有当前计数为0时再Leave就不会触发

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelfRef` | `UPersistBaseComponent*` | 监听的组件 |
| `state` | `FGameplayTag` | 离开的状态 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DynamicStateInterruptedHandle`

```text
DynamicStateInterruptedHandle(SelfRef: UPersistBaseComponent*, state: FGameplayTag) -> void
```

Event
	  生效范围：服务器&客户端
	  打断状态事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelfRef` | `UPersistBaseComponent*` | 监听的组件 |
| `state` | `FGameplayTag` | 打断的状态 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DynamicStateInterruptedWithSourceHandle`

```text
DynamicStateInterruptedWithSourceHandle(SelfRef: UPersistBaseComponent*, InterruptedState: FGameplayTag, SourceState: FGameplayTag) -> void
```

Event
	  生效范围：服务器
	  打断状态事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelfRef` | `UPersistBaseComponent*` | 监听的组件 |
| `InterruptedState` | `FGameplayTag` | - |
| `SourceState` | `FGameplayTag` | 打断的状态的来源 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DynamicStateDisabledChangedHandle`

```text
DynamicStateDisabledChangedHandle(SelfRef: UPersistBaseComponent*, state: FGameplayTag, bNewDisabled: bool) -> void
```

Event
	  生效范围：服务器&客户端
	  禁用状态事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelfRef` | `UPersistBaseComponent*` | 监听的组件 |
| `state` | `FGameplayTag` | 禁用的状态 |
| `bNewDisabled` | `bool` | 禁用解除禁用 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DynamicStateDisabledResetHandle`

```text
DynamicStateDisabledResetHandle(SelfRef: UPersistBaseComponent*, state: FGameplayTag) -> void
```

Event
	  生效范围：服务器&客户端
	  重置禁用状态事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelfRef` | `UPersistBaseComponent*` | 监听的组件 |
| `state` | `FGameplayTag` | 重置禁用的状态 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPersistEffectBase.json -->

# UPersistEffectBase

PersistEffectBase, PersistEffectSkill和PersistEffectBuff的基类

## Inheritance

`UBasicPersistEffect` -> `IGameplayTaskOwnerInterface` -> `ILimitationInterface` -> `IOwnershipChainInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bPersistOnUnapply` | `bool` | Unapply 时是否缓存到 PlayerState 上的 PersistEffectCacheComponent，<br>	  下次同类型 Apply 会取回并触发 OnRecover |

## Functions

### `HasAuthority`

```text
HasAuthority() -> bool
```

检查当前对象是否运行在服务器端
	  生效范围: 服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `bool` | 否运行在服务器端 |

### `IsAutonomous`

```text
IsAutonomous(bConsiderObReplay: bool) -> const bool
```

检查当前对象是否运行在主控客户端
	  生效范围: 服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bConsiderObReplay` | `bool` | 是否包含观战和回放时的主控端 |

**Returns**

| Type | Description |
|---|---|
| `const bool` | 否运行在主控客户端 |

### `RefreshValidTime`

```text
RefreshValidTime() -> void
```

刷新PersistEffect的生效时间
	  生效范围: 服务器

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTickEnable`

```text
SetTickEnable(bEnable: bool) -> void
```

设置PersistEffect是否每帧执行Tick函数，在服务器调用只会开启服务器的Tick，在客户端调用只会开启客户端的Tick
	  生效范围: 服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetApplyTime`

```text
SetApplyTime(Time: float) -> void
```

设置PersistEffect的生效时间
	  生效范围: 服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetApplyTime`

```text
GetApplyTime() -> float
```

获取PersistEffect的生效时间
	  生效范围: 服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetTimeStamp`

```text
GetTimeStamp() -> float
```

获取当前服务器时间戳
	  生效范围: 服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `HasTag`

```text
HasTag(Tag: FGameplayTag) -> bool
```

检查当前技能或Buff是否有某个类型的Tag
	  生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Tag` | `FGameplayTag` | 要检查的Tag |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否有对应的Tag |

### `GetRemainingTime`

```text
GetRemainingTime() -> float
```

获取剩余时间

**Returns**

| Type | Description |
|---|---|
| `float` | 剩余时间 |

### `SetPersistOnUnapply`

```text
SetPersistOnUnapply(bInPersistOnUnapply: bool) -> void
```

运行时动态修改 bPersistOnUnapply。仅服务端生效，不 Replicated。
	  可在 OnApply  Tick  OnUnApply_BP 等任意服务端时机调用。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInPersistOnUnapply` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ShouldPersistOnUnapply`

```text
ShouldPersistOnUnapply() -> bool
```

读取当前 bPersistOnUnapply (含运行时修改值)。

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetOwnerActor`

```text
GetOwnerActor() -> AActor *
```

获取PersistEffect所属的Actor
	  生效范围: 服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `GetOwnerComponent`

```text
GetOwnerComponent() -> UPersistBaseComponent *
```

获取PersistEffect所属的组件
	  生效范围: 服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `UPersistBaseComponent *` | - |

## Events

### `OnApply_BP`

```text
OnApply_BP(Character: AActor *) -> void
```

当PersistEffect挂载到角色身上时调用
	  生效范围: 服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `AActor *` | 挂载的角色 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnUnApply_BP`

```text
OnUnApply_BP(Character: AActor *, Reason: EPersistEffectUnApplyReason) -> void
```

当PersistEffect从角色身上移除时调用
	  生效范围: 服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `AActor *` | 挂载的角色 |
| `Reason` | `EPersistEffectUnApplyReason` | 移除的原因 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanApply_BP`

```text
CanApply_BP(Character: AActor *) -> bool
```

当PersistEffect挂载到角色身上前检查是否可挂载时调用
	  生效范围: 服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `AActor *` | 尝试挂载的角色 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否可以挂载 |

### `OnMerge_BP`

```text
OnMerge_BP(Target: UPersistEffectBase *, ApplyTime: float) -> void
```

当PersistEffect合并时调用
	  生效范围: 服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `UPersistEffectBase *` | 被合并的PersistEffect |
| `ApplyTime` | `float` | 被合并的PersistEffect的生效时长 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanMerge_BP`

```text
CanMerge_BP(Target: UPersistEffectBase *) -> bool
```

当PersistEffect合并前检查是否可合并时调用
	  生效范围: 服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `UPersistEffectBase *` | 被合并的PersistEffect |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否可以合并 |

### `OnRecover_BP`

```text
OnRecover_BP(Character: AActor *) -> void
```

当PersistEffect从缓存中恢复使用
	  生效范围: 服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `AActor *` | 恢复后的新挂载角色 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Tick_BP`

```text
Tick_BP(Character: AActor *, DeltaTime: float) -> void
```

PersistEffect每帧调用，开启Tick需要SetTickEnable(true)
	  生效范围: 服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `AActor *` | 挂载的角色 |
| `DeltaTime` | `float` | 距离上次触发后经过的时间 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInterrupted_BP`

```text
OnInterrupted_BP(Character: AActor *) -> void
```

当PersistEffect被打断时调用
	  生效范围: 服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `AActor *` | 挂载的角色 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPersistEffectBuff.json -->

# UPersistEffectBuff

Buff系统归属与和平精英的技能系统，用于帮助开发者更方便快捷地实现Buff效果
  通过与Tag、Attribute等系统的配合能够通过配置就实现大部分所需的效果
  对于更细致的Buff效果也可以通过重写BP结尾的函数来实现定制化效果。

## Inheritance

`UPersistEffectBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BuffInfo` | `FPEBuffInfo` | 生效范围：服务器&客户端<br>      Buff蓝图的配置信息 |

## Functions

### `AddStackNum`

```text
AddStackNum(Num: int32) -> void
```

生效范围：服务器
	  修改堆叠层数，修改后的层数大于等于0且小于等于最大堆叠层数(MaxStackNum)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Num` | `int32` | 新增的层数 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetStackNum`

```text
GetStackNum() -> int32
```

生效范围：服务器&客户端
	 获取当前层数

**Returns**

| Type | Description |
|---|---|
| `int32` | 当前层数 |

### `GetCauser`

```text
GetCauser() -> AActor *
```

生效范围：服务器&客户端
      获取Buff的施加者

**Returns**

| Type | Description |
|---|---|
| `AActor *` | 施加者 |

### `SetCauser`

```text
SetCauser(Causer: AActor *) -> void
```

生效范围：服务器
	 设置Buff的施加者

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Causer` | `AActor *` | 施加者 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `TriggerAllLayer`

```text
TriggerAllLayer() -> void
```

生效范围：服务器
      触发当前所有层的Buff的效果

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `TriggerSingleLayer`

```text
TriggerSingleLayer() -> void
```

生效范围：服务器
	  触发单层的Buff的效果

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RefreshBuff`

```text
RefreshBuff() -> void
```

生效范围：服务器
	  重置Buff持续时间

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBuffEnable`

```text
SetBuffEnable(IsEnable: bool) -> void
```

生效范围：服务器
	  设置Buff是否生效

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsEnable` | `bool` | 是否生效 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsBuffEnable`

```text
IsBuffEnable() -> bool
```

生效范围：服务器&客户端
	  获取Buff当前是否生效

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否生效 |

### `Pause`

```text
Pause() -> void
```

生效范围：服务器
	  暂停Buff持续减少剩余时间

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Resume`

```text
Resume() -> void
```

生效范围：服务器
	  恢复Buff持续减少剩余时间

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OverwriteBuffUIInfo`

```text
OverwriteBuffUIInfo(BuffName: FName &, BuffDetail: FString &, BuffIconPath: FString &) -> void
```

生效范围：服务器&客户端
	  更改UI信息，但双端不同步

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BuffName` | `FName &` | Buff名字 |
| `BuffDetail` | `FString &` | Buff描述 |
| `BuffIconPath` | `FString &` | Buff图标路径 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBuffName`

```text
GetBuffName() -> SHADOWTRACKEREXTRA_API FName
```

生效范围：服务器&客户端
	  获取Buff名字

**Returns**

| Type | Description |
|---|---|
| `SHADOWTRACKEREXTRA_API FName` | Buff名字 |

### `GetBuffDetail`

```text
GetBuffDetail() -> SHADOWTRACKEREXTRA_API FString
```

生效范围：服务器&客户端
	  获取Buff描述

**Returns**

| Type | Description |
|---|---|
| `SHADOWTRACKEREXTRA_API FString` | Buff描述 |

### `GetBuffIconPath`

```text
GetBuffIconPath() -> FString
```

生效范围：服务器&客户端
	  获取Buff图标路径

**Returns**

| Type | Description |
|---|---|
| `FString` | Buff图标路径 |

## Events

### `OnTotalDurationChange_BP`

```text
OnTotalDurationChange_BP(Pre: float, Current: float) -> void
```

生效范围：服务器
	  当Buff持续时间改变时调用，如修改ApplyTime、修改StackNum

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Pre` | `float` | 上一次的持续时间 |
| `Current` | `float` | 当前的持续时间 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnStackChange_BP`

```text
OnStackChange_BP(PreNum: int32, CurrentNum: int32) -> void
```

生效范围：服务器&客户端
	  当Buff堆叠层数变化时调用，如调用AddStackNum、消耗一层Buff

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PreNum` | `int32` | 上一次的堆叠层数 |
| `CurrentNum` | `int32` | 当前的堆叠层数 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRefresh_BP`

```text
OnRefresh_BP() -> void
```

生效范围：服务器&客户端
	  Buff刷新时调用

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanTrigger_BP`

```text
CanTrigger_BP() -> bool
```

生效范围：服务器
	  当Buff效果触发前调用，用于改写Buff触发条件，默认实现为直接返回True

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否可以触发 |

### `OnTrigger_BP`

```text
OnTrigger_BP(Reason: EPEBuffTriggerType) -> void
```

生效范围：服务器&客户端
	  当Buff效果触发时调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reason` | `EPEBuffTriggerType` | 触发原因 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnStackNumChange`

```text
OnStackNumChange(ChangeNum: int32) -> void
```

Event
	  生效范围：服务器&客户端
	  Buff层数改变事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ChangeNum` | `int32` | 改变的层数 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnUIInfoChange`

```text
OnUIInfoChange() -> void
```

Event
	  生效范围：客户端
	  Buff的UI信息改变事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPersistEffectSkill.json -->

# UPersistEffectSkill

技能实体

## Inheritance

`UPersistEffectWithState` -> `ISkillObjectInterface` -> `IPESkillTaskTrackConditionFilterInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PESkillSlot` | `FGameplayTag` | 技能槽位Tag |
| `ApplyTagGroup` | `FGameplayTagGroups` | Tag的配置组，包含该技能与各个Tag的互斥关系 |
| `CustomActivateConditions` | `FPESkillConditionContainer` | 技能激活自定义条件 |
| `ConsumeTime` | `EPESkillConsumeTimeType` | CD能量和消耗扣除时机 |
| `SkillCD` | `FPESkillCDWapper` | 技能CD |
| `CostConsume` | `FPESkillConsume` | 技能消耗 |
| `UIInfo` | `FPESkillUIInfo` | 技能外显信息 |
| `SkillGroup` | `FGameplayTag` | 技能组，同组互斥，不能同时激活同组的技能，如果填空的话则没有任何互斥关系 |
| `bDefaultEnable` | `bool` | 默认是否可用，如果配置了false，则需要调用enable才能激活技能 |

## Functions

### `EnableSkill`

```text
EnableSkill() -> void
```

生效范围：S
	  使技能可用

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableSkill`

```text
DisableSkill() -> void
```

生效范围：S
	  使技能不可用

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsSkillEnable`

```text
IsSkillEnable() -> bool
```

生效范围：SC

**Returns**

| Type | Description |
|---|---|
| `bool` | 技能是否可用 |

### `DeActivateSkill`

```text
DeActivateSkill(Reason: EPESkillDeActivateReason) -> void
```

生效范围：SC
	  取消技能释放

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reason` | `EPESkillDeActivateReason` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanActivateSkill`

```text
CanActivateSkill() -> bool
```

生效范围：SC

**Returns**

| Type | Description |
|---|---|
| `bool` | 技能是否可用 |

### `ActivateSkill`

```text
ActivateSkill() -> void
```

生效范围：SC
	  释放技能

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsActivating`

```text
IsActivating() -> bool
```

生效范围：SC

**Returns**

| Type | Description |
|---|---|
| `bool` | 技能是否正在激活 |

### `CheckCDReady`

```text
CheckCDReady() -> bool
```

生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `bool` | 技能CD是否已准备好 |

### `CheckCostReady`

```text
CheckCostReady() -> bool
```

生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `bool` | 技能需要的消耗是否已准备好 |

### `ConsumeCD`

```text
ConsumeCD() -> bool
```

生效范围：服务器
	  消耗CD

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否成功消耗 |

### `ConsumeCost`

```text
ConsumeCost() -> bool
```

生效范围：服务器
	  消耗道具

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否成功消耗 |

### `GetRemainingCDTime`

```text
GetRemainingCDTime() -> float
```

生效范围：服务器&客户端
	  获取CD剩余时间

**Returns**

| Type | Description |
|---|---|
| `float` | 剩余时间 |

### `GetCDRecoveryTime`

```text
GetCDRecoveryTime() -> float
```

生效范围：服务器&客户端
	  获取CD恢复时间

**Returns**

| Type | Description |
|---|---|
| `float` | 剩余时间 |

### `SetCDRecoveryTime`

```text
SetCDRecoveryTime(CDRecoveryTime: float) -> void
```

生效范围：服务器
	  设置CD恢复时间

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CDRecoveryTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCDRecoverRate`

```text
GetCDRecoverRate() -> float
```

生效范围：服务器&客户端
	  获取CD恢复速率

**Returns**

| Type | Description |
|---|---|
| `float` | CD恢复速率 |

### `SetCDRecoverRate`

```text
SetCDRecoverRate(Rate: float) -> void
```

生效范围：服务器
	  设置CD恢复速率

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rate` | `float` | CD恢复速率 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ChargeCDEnergy`

```text
ChargeCDEnergy(ChargeRate: float) -> void
```

生效范围：服务器
	  恢复CD比例，1代表完全恢复一层CD，大于1代表恢复多层，不超过层数上限

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ChargeRate` | `float` | 恢复的层数 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ChargeCDTime`

```text
ChargeCDTime(ChargeTime: float) -> void
```

生效范围：服务器
	  恢复CD固定时间，不超过层数上限

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ChargeTime` | `float` | 恢复的时间，单位秒 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RefreshCD`

```text
RefreshCD() -> void
```

生效范围：服务器
	  刷新技能CD

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCDMaxLayer`

```text
SetCDMaxLayer(InMaxLayer: int) -> void
```

生效范围：服务器
	  设置CD最大层数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMaxLayer` | `int` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OverwriteSkillUIInfo`

```text
OverwriteSkillUIInfo(SkillName: FName, SkillDetail: FString, SkillIconPath: FString) -> void
```

生效范围：服务器&客户端
	  更改UI信息，但双端不同步

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkillName` | `FName` | 技能名字 |
| `SkillDetail` | `FString` | 技能描述 |
| `SkillIconPath` | `FString` | 技能图标路径 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSkillName`

```text
GetSkillName() -> FName
```

生效范围：服务器&客户端
	  获取技能名字

**Returns**

| Type | Description |
|---|---|
| `FName` | 技能名字 |

### `GetSkillDetail`

```text
GetSkillDetail() -> FString
```

生效范围：服务器&客户端
	  获取技能描述

**Returns**

| Type | Description |
|---|---|
| `FString` | 技能描述 |

### `GetSkillIconPath`

```text
GetSkillIconPath() -> FString
```

生效范围：服务器&客户端
	  获取技能图标路径

**Returns**

| Type | Description |
|---|---|
| `FString` | 技能图标路径 |

### `SetShowTipsEnable`

```text
SetShowTipsEnable(bEnable: bool) -> void
```

生效范围：服务器
	  设置是否开启技能激活检查失败显示Tips

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | 是否开启提示 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPlayActivateFailedSoundEnable`

```text
SetPlayActivateFailedSoundEnable(bEnable: bool) -> void
```

生效范围：服务器
	  设置是否开启技能激活检查失败播放提示音

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | 是否开启提示 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSelectTargetActor`

```text
GetSelectTargetActor(SelectType: EPESkillSelectTarget) -> TArray < AActor * >
```

获取技能目标角色

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelectType` | `EPESkillSelectTarget` | 选择类型 |

**Returns**

| Type | Description |
|---|---|
| `TArray < AActor * >` | 技能目标角色 |

### `SetSelectTargetActor`

```text
SetSelectTargetActor(Actors: TArray < AActor * > &) -> void
```

设置技能目标角色

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actors` | `TArray < AActor * > &` | Actor数组 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSelectTargetOneActor`

```text
SetSelectTargetOneActor(pActor: AActor *) -> void
```

设置技能目标角色

**Parameters**

| Name | Type | Description |
|---|---|---|
| `pActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSelectDirection`

```text
SetSelectDirection(Direction: FVector &) -> void
```

设置技能方向

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Direction` | `FVector &` | 方向 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSelectDirection`

```text
GetSelectDirection() -> FVector
```

获取技能方向

**Returns**

| Type | Description |
|---|---|
| `FVector` | 技能方向 |

### `GetSelectTransform`

```text
GetSelectTransform() -> const FTransform &
```

获取技能目标位置

**Returns**

| Type | Description |
|---|---|
| `const FTransform &` | 技能目标位置 |

### `SetSelectTransform`

```text
SetSelectTransform(Transform: FTransform &) -> void
```

设置技能目标位置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Transform` | `FTransform &` | 技能目标位置 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSelectTransforms`

```text
SetSelectTransforms(Transforms: TArray < FTransform > &) -> void
```

设置技能多目标位置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Transforms` | `TArray < FTransform > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSelectTransforms`

```text
GetSelectTransforms() -> const TArray < FTransform > &
```

获取技能多目标位置

**Returns**

| Type | Description |
|---|---|
| `const TArray < FTransform > &` | - |

### `ClearSelectTransforms`

```text
ClearSelectTransforms() -> void
```

清除技能目标位置

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Events

### `OnEnableSkill_BP`

```text
OnEnableSkill_BP() -> bool
```

生效范围：服务器
	  技能可用通知

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `OnDisableSkill_BP`

```text
OnDisableSkill_BP() -> bool
```

生效范围：服务器
	  技能不可用通知

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `OnActivateSkill_BP`

```text
OnActivateSkill_BP() -> bool
```

生效范围：服务器
	  技能被触发

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `OnDeActivateSkill_BP`

```text
OnDeActivateSkill_BP(Reason: EPESkillDeActivateReason) -> void
```

生效范围：服务器
	  技能结束

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reason` | `EPESkillDeActivateReason` | 结束原因 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanActivateSkill_BP`

```text
CanActivateSkill_BP() -> bool
```

生效范围：服务器&客户端
	  技能是否可用

**Returns**

| Type | Description |
|---|---|
| `bool` | 技能是否可释放 |

### `OnCDStateChange_BP`

```text
OnCDStateChange_BP(bIsCD: bool) -> void
```

生效范围：服务器&客户端
	  技能CD状态改变

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsCD` | `bool` | 技能是否CD中 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnUIInfoChange`

```text
OnUIInfoChange() -> void
```

Event
	  生效范围：客户端
	  技能的UI信息改变事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CDStateChangeHandle`

```text
CDStateChangeHandle(IsTrue: bool) -> void
```

Event
	  生效范围：服务器&客户端
	  客户端同步技能CD状态变化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsTrue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPersistEffectWithState.json -->

# UPersistEffectWithState

实现了状态机的PersistEffect，是PersistEffectSkill的基类

## Inheritance

`UPersistEffectBase` -> `IActivityStateInterface` -> `IClientConditionInerterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bTickStateMachineBeforeSequence` | `bool` | 控制Tick中状态机和Sequence的执行顺序<br>	  true: 先TickStateMachine再SequenceWrapper.Tick（默认，与原有逻辑一致）<br>	  false: 先SequenceWrapper.Tick再TickStateMachine |

## Functions

### `GetCurrentStateName`

```text
GetCurrentStateName() -> FName
```

获取当前状态的名字
	  生效范围: 服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `GetCurrentStateTime`

```text
GetCurrentStateTime() -> float
```

获取状态的运行时间
	  生效范围: 服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `JumpToState`

```text
JumpToState(StateName: FName, EnterTime: float, bPause: bool) -> void
```

获取跳转到指定状态
	  生效范围: 服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StateName` | `FName` | 跳转的目标状态名 |
| `EnterTime` | `float` | 跳转到目标状态的时间 |
| `bPause` | `bool` | 是否暂停sequence播放 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPESkillPassiveSkill.json -->

# UPESkillPassiveSkill

被动技能实体

## Inheritance

`UPersistEffectSkill`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaxActivationCount` | `int32` | 最大激活次数，-1表示无限制 |

## Events

### `OnStackChange_BP`

```text
OnStackChange_BP(PreNum: int32, CurrentNum: int32) -> void
```

生效范围：服务器&客户端
	  当 被动技能 堆叠层数变化时调用，比如技能被合并时

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PreNum` | `int32` | 上一次的堆叠层数 |
| `CurrentNum` | `int32` | 当前的堆叠层数 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanClientRPCActivate_BP`

```text
CanClientRPCActivate_BP() -> bool
```

生效范围：服务器
	  当 pes.BlockPassiveSkillClientRPC 开关关闭时，由蓝图决定是否允许客户端 RPC 激活被动技能

**Returns**

| Type | Description |
|---|---|
| `bool` | true 允许激活，false 拒绝激活 |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPESkillWidget.json -->

# UPESkillWidget

技能UI基类

## Inheritance

`UUAEUserWidget` -> `ILuaInterface`

## Functions

### `BindToSlot`

```text
BindToSlot(Comp: UPersistBaseComponent *, SlotName: FGameplayTag) -> void
```

将技能绑定到指定PE组件的指定Slot上
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Comp` | `UPersistBaseComponent *` | 绑定的组件 |
| `SlotName` | `FGameplayTag` | 绑定的槽位 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCurrentSkill`

```text
GetCurrentSkill() -> UPersistEffectSkill *
```

获取当前绑定的技能
	  生效范围C

**Returns**

| Type | Description |
|---|---|
| `UPersistEffectSkill *` | 当前绑定的技能 |

### `BindImageAndTextForSkillNameAndIcon`

```text
BindImageAndTextForSkillNameAndIcon(IconImage: UImage *, NameText: UTextBlock *, DescribeText: UTextBlock *) -> void
```

绑定用于显示技能图标、名字、描述的控件
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IconImage` | `UImage *` | 图标控件 |
| `NameText` | `UTextBlock *` | 名字控件 |
| `DescribeText` | `UTextBlock *` | 描述控件 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RefreshSkillUI`

```text
RefreshSkillUI() -> void
```

刷新当前UI绑定的控件的内容
	  生效范围C

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSkillName`

```text
GetSkillName() -> FName
```

获取技能名字
	  生效范围C

**Returns**

| Type | Description |
|---|---|
| `FName` | 技能名字 |

### `GetSkillDetail`

```text
GetSkillDetail() -> FString
```

获取技能描述
	  生效范围C

**Returns**

| Type | Description |
|---|---|
| `FString` | 技能描述 |

### `GetSkillIcon`

```text
GetSkillIcon() -> FSoftObjectPath
```

获取技能图标
	  生效范围C

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 技能图标 |

### `InitButton`

```text
InitButton(IconImage: UImage *, NameText: UTextBlock *, ClickButton: UButton *) -> void
```

绑定技能按钮控件
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IconImage` | `UImage *` | 图标控件 |
| `NameText` | `UTextBlock *` | 名字控件 |
| `ClickButton` | `UButton *` | 按钮控件 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InitLayer`

```text
InitLayer(LayerText: UTextBlock *, LayerPanel: UPanelWidget *) -> void
```

绑定技能使用层数控件
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LayerText` | `UTextBlock *` | 技能层数 |
| `LayerPanel` | `UPanelWidget *` | 技能层数的Panel控件，控制层数的显隐 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InitCDProgress`

```text
InitCDProgress(CDText: UTextBlock *, CDProgressImage: UImage *, CDProgressPanel: UPanelWidget *) -> void
```

绑定技能CD控件
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CDText` | `UTextBlock *` | 技能CD时间 |
| `CDProgressImage` | `UImage *` | @技能CD进度条 |
| `CDProgressPanel` | `UPanelWidget *` | 整个CD的Panel控件，控制CD的显隐 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InitEnergyProgress`

```text
InitEnergyProgress(EnergyProgressImage: UImage *, EnergyCanvasPanel: UPanelWidget *) -> void
```

绑定技能能量控件
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EnergyProgressImage` | `UImage *` | 技能能量进度条 |
| `EnergyCanvasPanel` | `UPanelWidget *` | 技能能量Panel控件，控制能量进度条的显隐 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InitTagDisableState`

```text
InitTagDisableState(TagDisableCanvasPanel: UPanelWidget *) -> void
```

绑定技能显示TagDisable状态的控件
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagDisableCanvasPanel` | `UPanelWidget *` | 技能TagDisable状态的Panel控件，控制TagDisable状态的显隐 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InitEnableState`

```text
InitEnableState(EnableCanvasPanel: UPanelWidget *) -> void
```

绑定技能显示Enable状态的控件
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EnableCanvasPanel` | `UPanelWidget *` | 技能Enable状态的Panel控件，控制Enable状态的显隐 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InitVirtualJoystick`

```text
InitVirtualJoystick(VirtualJoystickPanel: UPanelWidget *, VirtualJoystick: UPESkillVirtualJoystick *) -> void
```

绑定技能摇杆输入控件
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `VirtualJoystickPanel` | `UPanelWidget *` | - |
| `VirtualJoystick` | `UPESkillVirtualJoystick *` | 技能技能摇杆控件，控制摇杆的生效和失效 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Events

### `OnSkillBound_BP`

```text
OnSkillBound_BP(InOwnerSkill: UPersistEffectSkill *) -> void
```

当控件绑定到新的技能时触发
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOwnerSkill` | `UPersistEffectSkill *` | 当前绑定的技能 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UpdateCD_BP`

```text
UpdateCD_BP(Delta: float) -> void
```

每帧触发，用于更新CD显示
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delta` | `float` | 每帧的时间 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnCDStateChange_BP`

```text
OnCDStateChange_BP(bIsCD: bool) -> void
```

当控件绑定的技能CD状态变化时触发
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsCD` | `bool` | 技能是否处在CD状态 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnSkillUIInfoChange_BP`

```text
OnSkillUIInfoChange_BP() -> void
```

当控件绑定的技能的UI信息变化时触发
	  生效范围C

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnEnableChange_BP`

```text
OnEnableChange_BP(bIsEnable: bool) -> void
```

当控件绑定的技能Enable状态变化时触发
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsEnable` | `bool` | 技能是否Enable |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTagDisableChange_BP`

```text
OnTagDisableChange_BP(bIsDisable: bool) -> void
```

当控件绑定的技能被禁用Tag(PawnState.ActivatingSkill)导致无法激活时触发
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsDisable` | `bool` | 技能是否被Tag禁用 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnSkillDirectionInputEnableChange_BP`

```text
OnSkillDirectionInputEnableChange_BP(bEnable: bool) -> void
```

当控件绑定的技能的摇杆输入生效或失效时触发
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPESkillWithPredict.json -->

# UPESkillWithPredict

带主端预测的技能实,目前暂未有技能实装，待测试

## Inheritance

`UPersistEffectSkill`

## Functions

### `ActivateSkillWithPredict`

```text
ActivateSkillWithPredict() -> void
```

生效范围：SC
	  释放技能带主端预测

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `JumpToStateWithPredict`

```text
JumpToStateWithPredict(StateName: FName, EnterTime: float, bPause: bool) -> void
```

生效范围：SC
	  跳转状态带主端预测

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StateName` | `FName` | - |
| `EnterTime` | `float` | - |
| `bPause` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPhysicalAnimationComponent.json -->

# UPhysicalAnimationComponent

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StrengthMultiplyer` | `float` | Multiplies the strength of any active motors. (can blend from 0-1 for example) |
| `SkeletalMeshComponent` | `USkeletalMeshComponent *` | - |

## Functions

### `SetSkeletalMeshComponent`

```text
SetSkeletalMeshComponent(InSkeletalMeshComponent: USkeletalMeshComponent *) -> void
```

Sets the skeletal mesh we are driving through physical animation. Will erase any existing physical animation data.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSkeletalMeshComponent` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplyPhysicalAnimationSettings`

```text
ApplyPhysicalAnimationSettings(BodyName: FName, PhysicalAnimationData: FPhysicalAnimationData &) -> void
```

Applies the physical animation settings to the body given.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BodyName` | `FName` | - |
| `PhysicalAnimationData` | `FPhysicalAnimationData &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplyPhysicalAnimationSettingsBelow`

```text
ApplyPhysicalAnimationSettingsBelow(BodyName: FName, PhysicalAnimationData: FPhysicalAnimationData &, bIncludeSelf: bool) -> void
```

Applies the physical animation settings to the body given and all bodies below.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BodyName` | `FName` | - |
| `PhysicalAnimationData` | `FPhysicalAnimationData &` | - |
| `bIncludeSelf` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetStrengthMultiplyer`

```text
SetStrengthMultiplyer(InStrengthMultiplyer: float) -> void
```

Updates strength multiplyer and any active motors

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStrengthMultiplyer` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplyPhysicalAnimationProfileBelow`

```text
ApplyPhysicalAnimationProfileBelow(BodyName: FName, ProfileName: FName, bIncludeSelf: bool, bClearNotFound: bool) -> void
```

Applies the physical animation profile to the body given and all bodies below.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BodyName` | `FName` | The body from which we'd like to start applying the physical animation profile. Finds all bodies below in the skeleton hierarchy. None implies all bodies |
| `ProfileName` | `FName` | The physical animation profile we'd like to apply. For each body in the physics asset we search for physical animation settings with this name. |
| `bIncludeSelf` | `bool` | Whether to include the provided body name in the list of bodies we act on (useful to ignore for cases where a root has multiple children) |
| `bClearNotFound` | `bool` | If true, bodies without the given profile name will have any existing physical animation settings cleared. If false, bodies without the given profile name are left untouched. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBodyTargetTransform`

```text
GetBodyTargetTransform(BodyName: FName) -> FTransform
```

Returns the target transform for the given body. If physical animation component is not controlling this body, returns its current transform.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BodyName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPhysicalMaterial.json -->

# UPhysicalMaterial

Physical materials are used to define the response of a physical object when interacting dynamically with the world.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Friction` | `float` | Friction value of surface, controls how easily things can slide on this surface (0 is frictionless, higher values increase the amount of friction) |
| `FrictionCombineMode` | `TEnumAsByte < EFrictionCombineMode :: Type >` | Friction combine mode, controls how friction is computed for multiple materials. |
| `bOverrideFrictionCombineMode` | `bool` | If set we will use the FrictionCombineMode of this material, instead of the FrictionCombineMode found in the project settings. |
| `Restitution` | `float` | Restitution or 'bounciness' of this surface, between 0 (no bounce) and 1 (outgoing velocity is same as incoming). |
| `RestitutionCombineMode` | `TEnumAsByte < EFrictionCombineMode :: Type >` | Restitution combine mode, controls how restitution is computed for multiple materials. |
| `bOverrideRestitutionCombineMode` | `bool` | If set we will use the RestitutionCombineMode of this material, instead of the RestitutionCombineMode found in the project settings. |
| `Density` | `float` | Used with the shape of the object to calculate its mass properties. The higher the number, the heavier the object. g per cubic cm. |
| `RaiseMassToPower` | `float` | Used to adjust the way that mass increases as objects get larger. This is applied to the mass as calculated based on a 'solid' object. <br>	 	In actuality, larger objects do not tend to be solid, and become more like 'shells' (e.g. a car is not a solid piece of metal).<br>	 	Values are clamped to 1 or less. |
| `DestructibleDamageThresholdScale` | `float` | How much to scale the damage threshold by on any destructible we are applied to |
| `PhysicalMaterialProperty` | `UDEPRECATED_PhysicalMaterialPropertyBase *` | UPROPERTY(deprecated) |
| `SurfaceType` | `TEnumAsByte < EPhysicalSurface >` | To edit surface type for your project, use ProjectSettingsPhysicsPhysicalSurface section |
| `TireFrictionScale` | `float` | DEPRECATED - Overall tire friction scalar for every type of tire. This value is multiplied against our parents' values. |
| `TireFrictionScales` | `TArray < FTireFrictionScalePair >` | DEPRECATED - Tire friction scales for specific types of tires. These values are multiplied against our parents' values. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPhysicsAsset.json -->

# UPhysicsAsset

PhysicsAsset contains a set of rigid bodies and constraints that make up a single ragdoll.
  The asset is not limited to human ragdolls, and can be used for any physical simulation using bodies and constraints.
  A SkeletalMesh has a single PhysicsAsset, which allows for easily turning ragdoll physics on or off for many SkeletalMeshComponents
  The asset can be configured inside the Physics Asset Editor.
 
  @see USkeletalMesh

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoundsBodies` | `TArray < int32 >` | Index of bodies that are marked bConsiderForBounds |
| `SkeletalBodySetups` | `TArray < USkeletalBodySetup * >` | Array of SkeletalBodySetup objects. Stores information about collision shape etc. for each body.<br>		Does not include body position - those are taken from mesh. |
| `ConstraintSetup` | `TArray < UPhysicsConstraintTemplate * >` | Array of RB_ConstraintSetup objects. <br>	 	Stores information about a joint between two bodies, such as position relative to each body, joint limits etc. |
| `bUseAsyncScene` | `uint8` | If true, bodies of the physics asset will be put into the asynchronous physics scene. If false, they will be put into the synchronous physics scene. |
| `ThumbnailInfo` | `UThumbnailInfo *` | Information for thumbnail rendering |
| `BodySetup_DEPRECATED` | `TArray < UBodySetup * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPhysicsCollisionHandler.json -->

# UPhysicsCollisionHandler

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ImpactThreshold` | `float` | How hard an impact must be to trigger effectsound |
| `ImpactReFireDelay` | `float` | Min time between effectsound being triggered |
| `DefaultImpactSound` | `USoundBase *` | Sound to play |
| `LastImpactSoundTime` | `float` | Time since last impact sound |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPhysicsConstraintComponent.json -->

# UPhysicsConstraintComponent

This is effectively a joint that allows you to connect 2 rigid bodies together. You can create different types of joints using the various parameters of this component.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConstraintActor1` | `AActor *` | Pointer to first Actor to constrain. |
| `ComponentName1` | `FConstrainComponentPropName` | Name of first component property to constrain. If Actor1 is NULL, will look within Owner.<br>	 	If this is NULL, will use RootComponent of Actor1 |
| `ConstraintActor2` | `AActor *` | Pointer to second Actor to constrain. |
| `ComponentName2` | `FConstrainComponentPropName` | Name of second component property to constrain. If Actor2 is NULL, will look within Owner. <br>	 	If this is NULL, will use RootComponent of Actor2 |
| `ConstraintSetup_DEPRECATED` | `UPhysicsConstraintTemplate *` | - |
| `OnConstraintBroken` | `FConstraintBrokenSignature` | Notification when constraint is broken. |
| `ConstraintInstance` | `FConstraintInstance` | All constraint settings |

## Functions

### `SetConstrainedComponents`

```text
SetConstrainedComponents(Component1: UPrimitiveComponent *, BoneName1: FName, Component2: UPrimitiveComponent *, BoneName2: FName) -> void
```

Directly specify component to connect. Will update frames based on current position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component1` | `UPrimitiveComponent *` | - |
| `BoneName1` | `FName` | - |
| `Component2` | `UPrimitiveComponent *` | - |
| `BoneName2` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BreakConstraint`

```text
BreakConstraint() -> void
```

Break this constraint

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearPositionDrive`

```text
SetLinearPositionDrive(bEnableDriveX: bool, bEnableDriveY: bool, bEnableDriveZ: bool) -> void
```

EnablesDisables linear position drive

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableDriveX` | `bool` | Indicates whether the drive for the X-Axis should be enabled |
| `bEnableDriveY` | `bool` | Indicates whether the drive for the Y-Axis should be enabled |
| `bEnableDriveZ` | `bool` | Indicates whether the drive for the Z-Axis should be enabled |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearVelocityDrive`

```text
SetLinearVelocityDrive(bEnableDriveX: bool, bEnableDriveY: bool, bEnableDriveZ: bool) -> void
```

EnablesDisables linear position drive

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableDriveX` | `bool` | Indicates whether the drive for the X-Axis should be enabled |
| `bEnableDriveY` | `bool` | Indicates whether the drive for the Y-Axis should be enabled |
| `bEnableDriveZ` | `bool` | Indicates whether the drive for the Z-Axis should be enabled |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularOrientationDrive`

```text
SetAngularOrientationDrive(bEnableSwingDrive: bool, bEnableTwistDrive: bool) -> void
```

EnablesDisables angular orientation drive. Only relevant if the AngularDriveMode is set to Twist and Swing

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableSwingDrive` | `bool` | Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |
| `bEnableTwistDrive` | `bool` | Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOrientationDriveTwistAndSwing`

```text
SetOrientationDriveTwistAndSwing(bEnableTwistDrive: bool, bEnableSwingDrive: bool) -> void
```

EnablesDisables angular orientation drive. Only relevant if the AngularDriveMode is set to Twist and Swing

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableTwistDrive` | `bool` | Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |
| `bEnableSwingDrive` | `bool` | Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOrientationDriveSLERP`

```text
SetOrientationDriveSLERP(bEnableSLERP: bool) -> void
```

EnablesDisables the angular orientation slerp drive. Only relevant if the AngularDriveMode is set to SLERP

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableSLERP` | `bool` | Indicates whether the SLERP drive should be enabled. Only relevant if the AngularDriveMode is set to SLERP |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularVelocityDrive`

```text
SetAngularVelocityDrive(bEnableSwingDrive: bool, bEnableTwistDrive: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableSwingDrive` | `bool` | - |
| `bEnableTwistDrive` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularVelocityDriveTwistAndSwing`

```text
SetAngularVelocityDriveTwistAndSwing(bEnableTwistDrive: bool, bEnableSwingDrive: bool) -> void
```

EnablesDisables angular velocity twist and swing drive. Only relevant if the AngularDriveMode is set to Twist and Swing

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableTwistDrive` | `bool` | Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |
| `bEnableSwingDrive` | `bool` | Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularVelocityDriveSLERP`

```text
SetAngularVelocityDriveSLERP(bEnableSLERP: bool) -> void
```

EnablesDisables the angular velocity slerp drive. Only relevant if the AngularDriveMode is set to SLERP

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableSLERP` | `bool` | Indicates whether the SLERP drive should be enabled. Only relevant if the AngularDriveMode is set to SLERP |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularDriveMode`

```text
SetAngularDriveMode(DriveMode: EAngularDriveMode :: Type) -> void
```

Switches the angular drive mode between SLERP and Twist And Swing

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DriveMode` | `EAngularDriveMode :: Type` | The angular drive mode to use. SLERP uses shortest spherical path, but will not work if any angular constraints are locked. Twist and Swing decomposes the path into the different angular degrees of freedom but may experience gimbal lock |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearPositionTarget`

```text
SetLinearPositionTarget(InPosTarget: FVector &) -> void
```

Sets the target position for the linear drive.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPosTarget` | `FVector &` | Target position |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearVelocityTarget`

```text
SetLinearVelocityTarget(InVelTarget: FVector &) -> void
```

Sets the target velocity for the linear drive.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVelTarget` | `FVector &` | Target velocity |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearDriveParams`

```text
SetLinearDriveParams(PositionStrength: float, VelocityStrength: float, InForceLimit: float) -> void
```

Sets the drive params for the linear drive.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PositionStrength` | `float` | Positional strength for the drive (stiffness) |
| `VelocityStrength` | `float` | Velocity strength of the drive (damping) |
| `InForceLimit` | `float` | Max force applied by the drive |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularOrientationTarget`

```text
SetAngularOrientationTarget(InPosTarget: FRotator &) -> void
```

Sets the target orientation for the angular drive.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPosTarget` | `FRotator &` | Target orientation |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularVelocityTarget`

```text
SetAngularVelocityTarget(InVelTarget: FVector &) -> void
```

Sets the target velocity for the angular drive.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVelTarget` | `FVector &` | Target velocity |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularDriveParams`

```text
SetAngularDriveParams(PositionStrength: float, VelocityStrength: float, InForceLimit: float) -> void
```

Sets the drive params for the angular drive.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PositionStrength` | `float` | Positional strength for the drive (stiffness) |
| `VelocityStrength` | `float` | Velocity strength of the drive (damping) |
| `InForceLimit` | `float` | Max force applied by the drive |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearXLimit`

```text
SetLinearXLimit(ConstraintType: ELinearConstraintMotion, LimitSize: float) -> void
```

Sets the LinearX Motion Type

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConstraintType` | `ELinearConstraintMotion` | New Constraint Type |
| `LimitSize` | `float` | Size of limit |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearYLimit`

```text
SetLinearYLimit(ConstraintType: ELinearConstraintMotion, LimitSize: float) -> void
```

Sets the LinearY Motion Type

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConstraintType` | `ELinearConstraintMotion` | New Constraint Type |
| `LimitSize` | `float` | Size of limit |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearZLimit`

```text
SetLinearZLimit(ConstraintType: ELinearConstraintMotion, LimitSize: float) -> void
```

Sets the LinearZ Motion Type

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConstraintType` | `ELinearConstraintMotion` | New Constraint Type |
| `LimitSize` | `float` | Size of limit |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularSwing1Limit`

```text
SetAngularSwing1Limit(MotionType: EAngularConstraintMotion, Swing1LimitAngle: float) -> void
```

Sets the Angular Swing1 Motion Type

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MotionType` | `EAngularConstraintMotion` | - |
| `Swing1LimitAngle` | `float` | Size of limit in degrees |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularSwing2Limit`

```text
SetAngularSwing2Limit(MotionType: EAngularConstraintMotion, Swing2LimitAngle: float) -> void
```

Sets the Angular Swing2 Motion Type

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MotionType` | `EAngularConstraintMotion` | - |
| `Swing2LimitAngle` | `float` | Size of limit in degrees |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularTwistLimit`

```text
SetAngularTwistLimit(ConstraintType: EAngularConstraintMotion, TwistLimitAngle: float) -> void
```

Sets the Angular Twist Motion Type

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConstraintType` | `EAngularConstraintMotion` | New Constraint Type |
| `TwistLimitAngle` | `float` | Size of limit in degrees |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearBreakable`

```text
SetLinearBreakable(bLinearBreakable: bool, LinearBreakThreshold: float) -> void
```

Sets the Linear Breakable properties

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bLinearBreakable` | `bool` | Whether it is possible to break the joint with linear force |
| `LinearBreakThreshold` | `float` | Force needed to break the joint |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularBreakable`

```text
SetAngularBreakable(bAngularBreakable: bool, AngularBreakThreshold: float) -> void
```

Sets the Angular Breakable properties

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bAngularBreakable` | `bool` | Whether it is possible to break the joint with angular force |
| `AngularBreakThreshold` | `float` | Torque needed to break the joint |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCurrentTwist`

```text
GetCurrentTwist() -> float
```

Gets the current Angular Twist of the constraint

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetCurrentSwing1`

```text
GetCurrentSwing1() -> float
```

Gets the current Swing1 of the constraint

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetCurrentSwing2`

```text
GetCurrentSwing2() -> float
```

Gets the current Swing2 of the constraint

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetConstraintReferenceFrame`

```text
SetConstraintReferenceFrame(Frame: EConstraintFrame :: Type, RefFrame: FTransform &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Frame` | `EConstraintFrame :: Type` | - |
| `RefFrame` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetConstraintReferencePosition`

```text
SetConstraintReferencePosition(Frame: EConstraintFrame :: Type, RefPosition: FVector &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Frame` | `EConstraintFrame :: Type` | - |
| `RefPosition` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetConstraintReferenceOrientation`

```text
SetConstraintReferenceOrientation(Frame: EConstraintFrame :: Type, PriAxis: FVector &, SecAxis: FVector &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Frame` | `EConstraintFrame :: Type` | - |
| `PriAxis` | `FVector &` | - |
| `SecAxis` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDisableCollision`

```text
SetDisableCollision(bDisableCollision: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bDisableCollision` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetConstraintForce`

```text
GetConstraintForce(OutLinearForce: FVector &, OutAngularForce: FVector &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutLinearForce` | `FVector &` | - |
| `OutAngularForce` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsBroken`

```text
IsBroken() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPhysicsConstraintTemplate.json -->

# UPhysicsConstraintTemplate

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultInstance` | `FConstraintInstance` | - |
| `ProfileHandles` | `TArray < FPhysicsConstraintProfileHandle >` | Handles to the constraint profiles applicable to this constraint |
| `DefaultProfile` | `FConstraintProfileProperties` | When no profile is selected, use these settings. Only needed in editor as we serialize it into DefaultInstance on save |
| `JointName_DEPRECATED` | `FName` | - |
| `ConstraintBone1_DEPRECATED` | `FName` | - |
| `ConstraintBone2_DEPRECATED` | `FName` | - |
| `Pos1_DEPRECATED` | `FVector` | - |
| `PriAxis1_DEPRECATED` | `FVector` | - |
| `SecAxis1_DEPRECATED` | `FVector` | - |
| `Pos2_DEPRECATED` | `FVector` | - |
| `PriAxis2_DEPRECATED` | `FVector` | - |
| `SecAxis2_DEPRECATED` | `FVector` | - |
| `bEnableProjection_DEPRECATED` | `uint32` | - |
| `ProjectionLinearTolerance_DEPRECATED` | `float` | - |
| `ProjectionAngularTolerance_DEPRECATED` | `float` | - |
| `LinearXMotion_DEPRECATED` | `TEnumAsByte < enum ELinearConstraintMotion >` | - |
| `LinearYMotion_DEPRECATED` | `TEnumAsByte < enum ELinearConstraintMotion >` | - |
| `LinearZMotion_DEPRECATED` | `TEnumAsByte < enum ELinearConstraintMotion >` | - |
| `LinearLimitSize_DEPRECATED` | `float` | - |
| `bLinearLimitSoft_DEPRECATED` | `uint32` | - |
| `LinearLimitStiffness_DEPRECATED` | `float` | - |
| `LinearLimitDamping_DEPRECATED` | `float` | - |
| `bLinearBreakable_DEPRECATED` | `uint32` | - |
| `LinearBreakThreshold_DEPRECATED` | `float` | - |
| `AngularSwing1Motion_DEPRECATED` | `TEnumAsByte < enum EAngularConstraintMotion >` | - |
| `AngularSwing2Motion_DEPRECATED` | `TEnumAsByte < enum EAngularConstraintMotion >` | - |
| `AngularTwistMotion_DEPRECATED` | `TEnumAsByte < enum EAngularConstraintMotion >` | - |
| `bSwingLimitSoft_DEPRECATED` | `uint32` | - |
| `bTwistLimitSoft_DEPRECATED` | `uint32` | - |
| `Swing1LimitAngle_DEPRECATED` | `float` | - |
| `Swing2LimitAngle_DEPRECATED` | `float` | - |
| `TwistLimitAngle_DEPRECATED` | `float` | - |
| `SwingLimitStiffness_DEPRECATED` | `float` | - |
| `SwingLimitDamping_DEPRECATED` | `float` | - |
| `TwistLimitStiffness_DEPRECATED` | `float` | - |
| `TwistLimitDamping_DEPRECATED` | `float` | - |
| `bAngularBreakable_DEPRECATED` | `uint32` | - |
| `AngularBreakThreshold_DEPRECATED` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPhysicsHandleComponent.json -->

# UPhysicsHandleComponent

Utility object for moving physics objects around.

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GrabbedComponent` | `UPrimitiveComponent *` | Component we are currently holding |
| `bSoftAngularConstraint` | `uint32` | - |
| `bSoftLinearConstraint` | `uint32` | - |
| `bInterpolateTarget` | `uint32` | - |
| `LinearDamping` | `float` | Linear damping of the handle spring. |
| `LinearStiffness` | `float` | Linear stiffness of the handle spring |
| `AngularDamping` | `float` | Angular stiffness of the handle spring |
| `AngularStiffness` | `float` | Angular stiffness of the handle spring |
| `InterpolationSpeed` | `float` | How quickly we interpolate the physics target transform |

## Functions

### `GrabComponent`

```text
GrabComponent(Component: UPrimitiveComponent *, InBoneName: FName, GrabLocation: FVector, bConstrainRotation: bool) -> ENGINE_API virtual void
```

Grab the specified component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent *` | - |
| `InBoneName` | `FName` | - |
| `GrabLocation` | `FVector` | - |
| `bConstrainRotation` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API virtual void` | - |

### `GrabComponentAtLocation`

```text
GrabComponentAtLocation(Component: UPrimitiveComponent *, InBoneName: FName, GrabLocation: FVector) -> ENGINE_API void
```

Grab the specified component at a given location. Does NOT constraint rotation which means the handle will pivot about GrabLocation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent *` | - |
| `InBoneName` | `FName` | - |
| `GrabLocation` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GrabComponentAtLocationWithRotation`

```text
GrabComponentAtLocationWithRotation(Component: UPrimitiveComponent *, InBoneName: FName, Location: FVector, Rotation: FRotator) -> ENGINE_API void
```

Grab the specified component at a given location and rotation. Constrains rotation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent *` | - |
| `InBoneName` | `FName` | - |
| `Location` | `FVector` | - |
| `Rotation` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `ReleaseComponent`

```text
ReleaseComponent() -> ENGINE_API virtual void
```

Release the currently held component

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API virtual void` | - |

### `GetGrabbedComponent`

```text
GetGrabbedComponent() -> ENGINE_API class UPrimitiveComponent *
```

Returns the currently grabbed component, or null if nothing is grabbed.

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API class UPrimitiveComponent *` | - |

### `SetTargetLocation`

```text
SetTargetLocation(NewLocation: FVector) -> ENGINE_API void
```

Set the target location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetTargetRotation`

```text
SetTargetRotation(NewRotation: FRotator) -> ENGINE_API void
```

Set the target rotation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRotation` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetTargetLocationAndRotation`

```text
SetTargetLocationAndRotation(NewLocation: FVector, NewRotation: FRotator) -> ENGINE_API void
```

Set target location and rotation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector` | - |
| `NewRotation` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GetTargetLocationAndRotation`

```text
GetTargetLocationAndRotation(TargetLocation: FVector &, TargetRotation: FRotator &) -> ENGINE_API void
```

Get the current location and rotation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetLocation` | `FVector &` | - |
| `TargetRotation` | `FRotator &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetLinearDamping`

```text
SetLinearDamping(NewLinearDamping: float) -> ENGINE_API void
```

Set linear damping

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLinearDamping` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetLinearStiffness`

```text
SetLinearStiffness(NewLinearStiffness: float) -> ENGINE_API void
```

Set linear stiffness

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLinearStiffness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetAngularDamping`

```text
SetAngularDamping(NewAngularDamping: float) -> ENGINE_API void
```

Set angular damping

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAngularDamping` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetAngularStiffness`

```text
SetAngularStiffness(NewAngularStiffness: float) -> ENGINE_API void
```

Set angular stiffness

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAngularStiffness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetInterpolationSpeed`

```text
SetInterpolationSpeed(NewInterpolationSpeed: float) -> ENGINE_API void
```

Set interpolation speed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewInterpolationSpeed` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPhysicsSettings.json -->

# UPhysicsSettings

Default physics settings.

## Inheritance

`UDeveloperSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ServerPvdThresholdMs` | `float` | Default ServerPvdThresholdMs. |
| `ClientPvdThresholdMs` | `float` | Default ClientPvdThresholdMs. |
| `ServerPvdRecordTimeSeconds` | `int32` | Default ServerPvdRecordTimeSeconds. |
| `ClientPvdRecordTimeSeconds` | `int32` | Default ClientPvdRecordTimeSeconds. |
| `DefaultGravityZ` | `float` | Default gravity. |
| `DefaultTerminalVelocity` | `float` | Default terminal velocity for Physics Volumes. |
| `DefaultFluidFriction` | `float` | Default fluid friction for Physics Volumes. |
| `SimulateScratchMemorySize` | `int32` | Amount of memory to reserve for PhysX simulate(), this is per pxscene and will be rounded up to the next 16K boundary |
| `RagdollAggregateThreshold` | `int32` | Threshold for ragdoll bodies above which they will be added to an aggregate before being added to the scene |
| `TriangleMeshTriangleMinAreaThreshold` | `float` | Triangles from triangle meshes (BSP) with an area less than or equal to this value will be removed from physics collision data. Set to less than 0 to disable. |
| `bEnableAsyncScene` | `bool` | Enables the use of an async scene |
| `bEnableShapeSharing` | `bool` | Enables shape sharing between sync and async scene for static rigid actors |
| `bEnablePCM` | `bool` | Enables persistent contact manifolds. This will generate fewer contact points, but with more accuracy. Reduces stability of stacking, but can help energy conservation. |
| `bEnableStabilization` | `bool` | Enables stabilization of contacts for slow moving bodies. This will help improve the stability of stacking. |
| `bWarnMissingLocks` | `bool` | Whether to warn when physics locks are used incorrectly. Turning this off is not recommended and should only be used by very advanced users. |
| `bEnable2DPhysics` | `bool` | Can 2D physics be used (Box2D)? |
| `PhysicErrorCorrection` | `FRigidBodyErrorCorrectionNew` | Error correction data for replicating simulated physics (rigid bodies) |
| `LockedAxis_DEPRECATED` | `TEnumAsByte < ESettingsLockedAxis :: Type >` | - |
| `DefaultDegreesOfFreedom` | `TEnumAsByte < ESettingsDOF :: Type >` | Useful for constraining all objects in the world, for example if you are making a 2D game using 3D environments. |
| `BounceThresholdVelocity` | `float` | Minimum relative velocity required for an object to bounce. A typical value for simulation stability is about 0.2  gravity |
| `FrictionCombineMode` | `TEnumAsByte < EFrictionCombineMode :: Type >` | Friction combine mode, controls how friction is computed for multiple materials. |
| `RestitutionCombineMode` | `TEnumAsByte < EFrictionCombineMode :: Type >` | Restitution combine mode, controls how restitution is computed for multiple materials. |
| `MaxAngularVelocity` | `float` | Max angular velocity that a simulated object can achieve. |
| `MaxDepenetrationVelocity` | `float` | Max velocity which may be used to depenetrate simulated physics objects. 0 means no maximum. |
| `ContactOffsetMultiplier` | `float` | Contact offset multiplier. When creating a physics shape we look at its bounding volume and multiply its minimum value by this multiplier. A bigger number will generate contact points earlier which results in higher stability at the cost of performance. |
| `MinContactOffset` | `float` | Min Contact offset. |
| `MaxContactOffset` | `float` | Max Contact offset. |
| `bSimulateSkeletalMeshOnDedicatedServer` | `bool` | If true, simulate physics for this component on a dedicated server.<br>	  This should be set if simulating physics and replicating with a dedicated server. |
| `DefaultShapeComplexity` | `TEnumAsByte < ECollisionTraceFlag >` | Determines the default physics shape complexity. |
| `bDefaultHasComplexCollision_DEPRECATED` | `bool` | If true, static meshes will use per poly collision as complex collision by default. If false the default behavior is the same as UseSimpleAsComplex. |
| `bSuppressFaceRemapTable` | `bool` | If true, the internal physx face to UE face mapping will not be generated. This is a memory optimization available if you do not rely on face indices returned by scene queries. |
| `bSupportUVFromHitResults` | `bool` | If true, store extra information to allow FindCollisionUV to derive UV info from a line trace hit result, using the FindCollisionUV utility |
| `bDisableActiveActors` | `bool` | If true, physx will not update unreal with any bodies that have moved during the simulation. This should only be used if you have no physx simulation or you are manually updating the unreal data via polling physx. |
| `bDisableCCD` | `bool` | If true CCD will be ignored. This is an optimization when CCD is never used which removes the need for physx to check it internally. |
| `bEnableEnhancedDeterminism` | `bool` | If set to true, the scene will use enhanced determinism at the cost of a bit more resources. See eENABLE_ENHANCED_DETERMINISM to learn about the specifics |
| `MaxPhysicsDeltaTime` | `float` | Max Physics Delta Time to be clamped. |
| `bSubstepping` | `bool` | Whether to substep the physics simulation. This feature is still experimental. Certain functionality might not work correctly |
| `bSubsteppingAsync` | `bool` | Whether to substep the async physics simulation. This feature is still experimental. Certain functionality might not work correctly |
| `MaxSubstepDeltaTime` | `float` | Max delta time (in seconds) for an individual simulation substep. |
| `MaxSubsteps` | `int32` | Max number of substeps for physics simulation. |
| `ServerMaxSubstepDeltaTime` | `float` | pixelchen 服务器单独设置MaxSubstepDeltaTime |
| `ServerMaxSubsteps` | `int32` | pixelchen 服务器单独设置MaxSubsteps |
| `SyncSceneSmoothingFactor` | `float` | Physics delta time smoothing factor for sync scene. |
| `AsyncSceneSmoothingFactor` | `float` | Physics delta time smoothing factor for async scene. |
| `InitialAverageFrameRate` | `float` | Physics delta time initial average. |
| `PhysXTreeRebuildRate` | `int` | The number of frames it takes to rebuild the PhysX scene query AABB tree. The bigger the number, the smaller fetchResults takes per frame, but the more the tree deteriorates until a new tree is built |
| `PhysicalSurfaces` | `TArray < FPhysicalSurfaceName >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPhysicsSpringComponent.json -->

# UPhysicsSpringComponent

Note: this component is still work in progress. Uses raycast springs for simple vehicle forces
 	Used with objects that have physics to create a spring down the X direction
 	ie. point X in the direction you want generate spring.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SpringStiffness` | `float` | Specifies how much strength the spring has. The higher the SpringStiffness the more force the spring can push on a body with. |
| `SpringDamping` | `float` | Specifies how quickly the spring can absorb energy of a body. The higher the damping the less oscillation |
| `SpringLengthAtRest` | `float` | Determines how long the spring will be along the X-axis at rest. The spring will apply 0 force on a body when it's at rest. |
| `SpringRadius` | `float` | Determines the radius of the spring. |
| `SpringChannel` | `TEnumAsByte < enum ECollisionChannel >` | Strength of thrust force applied to the base object. |
| `bIgnoreSelf` | `bool` | If true, the spring will ignore all components in its own actor |
| `SpringCompression` | `float` | The current compression of the spring. A spring at rest will have SpringCompression 0. |

## Functions

### `GetNormalizedCompressionScalar`

```text
GetNormalizedCompressionScalar() -> float
```

Returns the spring compression as a normalized scalar along spring direction.
	   0 implies spring is at rest
	   1 implies fully compressed

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetSpringRestingPoint`

```text
GetSpringRestingPoint() -> FVector
```

Returns the spring resting point in world space.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetSpringCurrentEndPoint`

```text
GetSpringCurrentEndPoint() -> FVector
```

Returns the spring current end point in world space.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetSpringDirection`

```text
GetSpringDirection() -> FVector
```

Returns the spring direction from start to resting point

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPhysicsThrusterComponent.json -->

# UPhysicsThrusterComponent

Used with objects that have physics to apply a force down the negative-X direction
 	ie. point X in the direction you want the thrust in.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ThrustStrength` | `float` | Strength of thrust force applied to the base object. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPixelProjectedReflectionComponent.json -->

# UPixelProjectedReflectionComponent

UPixelProjectedReflectionComponent

## Inheritance

`USceneCaptureComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PreviewBox` | `UBoxComponent *` | - |
| `NormalDistortionStrength` | `float` | Controls the strength of normals when distorting the planar reflection. |
| `SkyDistanceFadeoutStart` | `float` | Receiving pixels at this distance from the reflection plane will begin to fade out the planar reflection. |
| `SkyDistanceFadeoutEnd` | `float` | Receiving pixels at this distance from the reflection plane will have completely faded out the planar reflection. |
| `DistanceFromPlaneFadeStart_DEPRECATED` | `float` | - |
| `DistanceFromPlaneFadeEnd_DEPRECATED` | `float` | - |
| `DistanceFromPlaneFadeoutStart` | `float` | Receiving pixels at this distance from the reflection plane will begin to fade out the planar reflection. |
| `DistanceFromPlaneFadeoutEnd` | `float` | Receiving pixels at this distance from the reflection plane will have completely faded out the planar reflection. |
| `AngleFromPlaneFadeStart` | `float` | Receiving pixels whose normal is at this angle from the reflection plane will begin to fade out the planar reflection. |
| `AngleFromPlaneFadeEnd` | `float` | Receiving pixels whose normal is at this angle from the reflection plane will have completely faded out the planar reflection. |
| `HeightAdjustmentVolumes` | `TArray < APixelProjectedReflectionHeightAdjustmentVolume * >` | - |
| `VisibilityVolumes` | `TArray < APixelProjectedReflectionVisibilityVolume * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPlanarReflectionComponent.json -->

# UPlanarReflectionComponent

UPlanarReflectionComponent

## Inheritance

`USceneCaptureComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PreviewBox` | `UBoxComponent *` | - |
| `NormalDistortionStrength` | `float` | Controls the strength of normals when distorting the planar reflection. |
| `PrefilterRoughnessY` | `float` | The vertical roughness value to prefilter the planar reflection texture with, useful for hiding low resolution.  Larger values have larger GPU cost. |
| `PrefilterRoughnessDistanceY` | `float` | The vertical distance at which the prefilter roughness value will be achieved. |
| `ScreenPercentage` | `int32` | Downsample percent, can be used to reduce GPU time rendering the planar reflection. |
| `ExtraFOV` | `float` | Additional FOV used when rendering to the reflection texture.  <br>	  This is useful when normal distortion is causing reads outside the reflection texture. <br>	  Larger values increase rendering thread and GPU cost, as more objects and triangles have to be rendered into the planar reflection. |
| `DistanceFromPlaneFadeStart_DEPRECATED` | `float` | - |
| `DistanceFromPlaneFadeEnd_DEPRECATED` | `float` | - |
| `DistanceFromPlaneFadeoutStart` | `float` | Receiving pixels at this distance from the reflection plane will begin to fade out the planar reflection. |
| `DistanceFromPlaneFadeoutEnd` | `float` | Receiving pixels at this distance from the reflection plane will have completely faded out the planar reflection. |
| `AngleFromPlaneFadeStart` | `float` | Receiving pixels whose normal is at this angle from the reflection plane will begin to fade out the planar reflection. |
| `AngleFromPlaneFadeEnd` | `float` | Receiving pixels whose normal is at this angle from the reflection plane will have completely faded out the planar reflection. |
| `bRenderSceneTwoSided` | `bool` | Whether to render the scene as two-sided, which can be useful to hide artifacts where normal distortion would read 'under' an object that has been clipped by the reflection plane. <br>	  With this setting enabled, the backfaces of a mesh would be displayed in the clipped region instead of the background which is potentially a bright sky.<br>	  Be sure to add the water plane to HiddenActors if enabling this, as the water plane will now block the reflection. |
| `bBlurHorizontal` | `bool` | Whether to blur along horizontal direction |
| `PrefilterRoughnessX` | `float` | The horizontal roughness value to prefilter the planar reflection texture with, useful for hiding low resolution.  Larger values have larger GPU cost. |
| `PrefilterRoughnessDistanceX` | `float` | The horizontal distance at which the prefilter roughness value will be achieved. |
| `PrefilterRoughnessLowerBound` | `float` | The Roughness Threshold For Prefilter |
| `ScreenSizeCullScale` | `float` | The ScreenSize Cull Scale |
| `FrustumOptim` | `bool` | Frustum Cull Range Optimization |
| `NoReflectionShadow` | `bool` | Do Not Render Shadow for PlanarRefelction |
| `FrameBufferCache` | `bool` | Enable FrameBuffer Cache Or Not |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPlaneReflectionCaptureComponent.json -->

# UPlaneReflectionCaptureComponent

## Inheritance

`UReflectionCaptureComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InfluenceRadiusScale` | `float` | Radius of the area that can receive reflections from this capture. |
| `PreviewInfluenceRadius` | `UDrawSphereComponent *` | - |
| `PreviewCaptureBox` | `UBoxComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPlatformEventsComponent.json -->

# UPlatformEventsComponent

Component to handle receiving notifications from the OS about platform events.

## Inheritance

`UActorComponent`

## Functions

### `IsInLaptopMode`

```text
IsInLaptopMode() -> bool
```

Check whether a convertible laptop is laptop mode.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if in laptop mode, false otherwise or if not a convertible laptop. |

### `IsInTabletMode`

```text
IsInTabletMode() -> bool
```

Check whether a convertible laptop is laptop mode.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if in tablet mode, false otherwise or if not a convertible laptop. |

### `SupportsConvertibleLaptops`

```text
SupportsConvertibleLaptops() -> bool
```

Check whether the platform supports convertible laptops.
	 
	  Note: This does not necessarily mean that the platform is a convertible laptop.
	  For example, convertible laptops running Windows 7 or older will return false,
	  and regular laptops running Windows 8 or newer will return true.

**Returns**

| Type | Description |
|---|---|
| `bool` | true for convertible laptop platforms, false otherwise. |

## Delegates

### `PlatformChangedToLaptopModeDelegate`

```text
PlatformChangedToLaptopModeDelegate() -> void
```

This is called when a convertible laptop changed into laptop mode.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlatformChangedToTabletModeDelegate`

```text
PlatformChangedToTabletModeDelegate() -> void
```

This is called when a convertible laptop changed into tablet mode.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPlatformGameInstance.json -->

# UPlatformGameInstance

UObject based class for handling mobile events. Having this object as an option gives the app lifetime access to these global delegates. The component UApplicationLifecycleComponent is destroyed at level loads

## Inheritance

`UGameInstance`

## Delegates

### `ApplicationWillDeactivateDelegate`

```text
ApplicationWillDeactivateDelegate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationHasReactivatedDelegate`

```text
ApplicationHasReactivatedDelegate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationWillEnterBackgroundDelegate`

```text
ApplicationWillEnterBackgroundDelegate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationHasEnteredForegroundDelegate`

```text
ApplicationHasEnteredForegroundDelegate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationWillTerminateDelegate`

```text
ApplicationWillTerminateDelegate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationRegisteredForRemoteNotificationsDelegate`

```text
ApplicationRegisteredForRemoteNotificationsDelegate(inArray: const TArray<uint8>&) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `inArray` | `const TArray&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationRegisteredForUserNotificationsDelegate`

```text
ApplicationRegisteredForUserNotificationsDelegate(inInt: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `inInt` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationFailedToRegisterForRemoteNotificationsDelegate`

```text
ApplicationFailedToRegisterForRemoteNotificationsDelegate(inString: FString) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `inString` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationReceivedRemoteNotificationDelegate`

```text
ApplicationReceivedRemoteNotificationDelegate(inString: FString, inAppState: EApplicationState::Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `inString` | `FString` | - |
| `inAppState` | `EApplicationState::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationReceivedLocalNotificationDelegate`

```text
ApplicationReceivedLocalNotificationDelegate(inString: FString, inInt: int32, inAppState: EApplicationState::Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `inString` | `FString` | - |
| `inInt` | `int32` | - |
| `inAppState` | `EApplicationState::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationReceivedScreenOrientationChangedNotificationDelegate`

```text
ApplicationReceivedScreenOrientationChangedNotificationDelegate(inScreenOrientation: EScreenOrientation::Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `inScreenOrientation` | `EScreenOrientation::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPlatformInterfaceBase.json -->

# UPlatformInterfaceBase

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AllDelegates` | `TArray < struct FDelegateArray >` | Array of delegate arrays. Only add and remove via helper functions, and call via the helper delegate call function |

## Language

`cpp`

