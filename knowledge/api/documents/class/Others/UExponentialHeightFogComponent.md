---
id: "api:class:UExponentialHeightFogComponent"
title: "UExponentialHeightFogComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UExponentialHeightFogComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UExponentialHeightFogComponent

Used to create fogging effects such as clouds but with a density that is related to the height of the fog.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FogDensity` | `float` | Global density factor. |
| `CustomHightFogDensity` | `TArray < FCustomHeightFog >` | - |
| `bUseCustomFog` | `bool` | - |
| `CustomFogLow_Height` | `float` | - |
| `CustomFogLow_DensityCoefficient` | `float` | - |
| `CustomFogLow_Color` | `FLinearColor` | - |
| `CustomFogHigh_Height` | `float` | - |
| `CustomFogHigh_DensityCoefficient` | `float` | - |
| `CustomFogHigh_Color` | `FLinearColor` | - |
| `FogInscatteringColor` | `FLinearColor` | - |
| `InscatteringColorCubemap` | `UTextureCube *` | Cubemap that can be specified for fog color, which is useful to make distant, heavily fogged scene elements match the sky.<br>	  When the cubemap is specified, FogInscatteringColor is ignored and Directional inscattering is disabled. |
| `InscatteringColorCubemapAngle` | `float` | Angle to rotate the InscatteringColorCubemap around the Z axis. |
| `InscatteringTextureTint` | `FLinearColor` | Tint color used when InscatteringColorCubemap is specified, for quick edits without having to reimport InscatteringColorCubemap. |
| `FullyDirectionalInscatteringColorDistance` | `float` | Distance at which InscatteringColorCubemap should be used directly for the Inscattering Color. |
| `NonDirectionalInscatteringColorDistance` | `float` | Distance at which only the average color of InscatteringColorCubemap should be used as Inscattering Color. |
| `DirectionalInscatteringExponent` | `float` | Controls the size of the directional inscattering cone, which is used to approximate inscattering from a directional light.  <br>	  Note: there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used. |
| `DirectionalInscatteringStartDistance` | `float` | Controls the start distance from the viewer of the directional inscattering, which is used to approximate inscattering from a directional light. <br>	  Note: there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used. |
| `DirectionalInscatteringColor` | `FLinearColor` | Controls the color of the directional inscattering, which is used to approximate inscattering from a directional light. <br>	  Note: there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used. |
| `FogHeightFalloff` | `float` | Height density factor, controls how the density increases as height decreases.  <br>	  Smaller values make the visible transition larger. |
| `FogMaxOpacity` | `float` | Maximum opacity of the fog.  <br>	  A value of 1 means the fog can become fully opaque at a distance and replace scene color completely,<br>	  A value of 0 means the fog color will not be factored in at all. |
| `StartDistance` | `float` | Distance from the camera that the fog will start, in world units. |
| `FogCutoffDistance` | `float` | Scene elements past this distance will not have fog applied.  This is useful for excluding skyboxes which already have fog baked in. |
| `Priority` | `int32` | Priority to be rendered with, useful if more than one exponential fogs are visible concurrently |
| `bEnableVolumetricFog` | `bool` | Whether to enable Volumetric fog.  Scalability settings control the resolution of the fog simulation. <br>	  Note that Volumetric fog currently does not support StartDistance, FogMaxOpacity and FogCutoffDistance.<br>	  Volumetric fog also can't match exponential height fog in general as exponential height fog has non-physical behavior. |
| `VolumetricFogScatteringDistribution` | `float` | Controls the scattering phase function - how much incoming light scatters in various directions.<br>	  A distribution value of 0 scatters equally in all directions, while .9 scatters predominantly in the light direction.  <br>	  In order to have visible volumetric fog light shafts from the side, the distribution will need to be closer to 0. |
| `VolumetricFogAlbedo` | `FColor` | The height fog particle reflectiveness used by volumetric fog. <br>	  Water particles in air have an albedo near white, while dust has slightly darker value. |
| `VolumetricFogEmissive` | `FLinearColor` | Light emitted by height fog.  This is a density so more light is emitted the further you are looking through the fog.<br>	  In most cases skylight is a better choice, however right now volumetric fog does not support precomputed lighting, <br>	  So stationary skylights are unshadowed and static skylights don't affect volumetric fog at all. |
| `VolumetricFogExtinctionScale` | `float` | Scales the height fog particle extinction amount used by volumetric fog.  Values larger than 1 cause fog particles everywhere absorb more light. |
| `VolumetricFogDistance` | `float` | Distance over which volumetric fog should be computed.  Larger values extend the effect into the distance but expose under-sampling artifacts in details. |
| `VolumetricFogStaticLightingScatteringIntensity` | `float` | - |
| `bOverrideLightColorsWithFogInscatteringColors` | `bool` | Whether to use FogInscatteringColor for the Sky Light volumetric scattering color and DirectionalInscatteringColor for the Directional Light scattering color. <br>	  Make sure your directional light has 'Atmosphere Sun Light' enabled!<br>	  Enabling this allows Volumetric fog to better match Height fog in the distance, but produces non-physical volumetric lighting that may not match surface lighting. |
| `VolumetricFogStartDistance` | `float` | Distance over which volumetric fog should be computed.  Larger values extend the effect into the distance but expose under-sampling artifacts in details. |
| `VolumetricFogNoiseTexture` | `UTexture2D *` | - |
| `VolumetricFogNoiseTransform` | `FTransform` | - |

## Functions

### `SetFogDensity`

```text
SetFogDensity(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCustomFogHeight`

```text
SetCustomFogHeight(Value: float, index: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |
| `index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCustomFogDensityCoefficient`

```text
SetCustomFogDensityCoefficient(Value: float, index: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |
| `index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCustomFogInscatteringColor`

```text
SetCustomFogInscatteringColor(Value: FLinearColor, index: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FLinearColor` | - |
| `index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFogInscatteringColor`

```text
SetFogInscatteringColor(Value: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInscatteringColorCubemap`

```text
SetInscatteringColorCubemap(Value: UTextureCube *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `UTextureCube *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInscatteringColorCubemapAngle`

```text
SetInscatteringColorCubemapAngle(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFullyDirectionalInscatteringColorDistance`

```text
SetFullyDirectionalInscatteringColorDistance(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNonDirectionalInscatteringColorDistance`

```text
SetNonDirectionalInscatteringColorDistance(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInscatteringTextureTint`

```text
SetInscatteringTextureTint(Value: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDirectionalInscatteringExponent`

```text
SetDirectionalInscatteringExponent(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDirectionalInscatteringStartDistance`

```text
SetDirectionalInscatteringStartDistance(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDirectionalInscatteringColor`

```text
SetDirectionalInscatteringColor(Value: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFogHeightFalloff`

```text
SetFogHeightFalloff(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFogMaxOpacity`

```text
SetFogMaxOpacity(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetStartDistance`

```text
SetStartDistance(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFogCutoffDistance`

```text
SetFogCutoffDistance(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFog`

```text
SetVolumetricFog(bNewValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogScatteringDistribution`

```text
SetVolumetricFogScatteringDistribution(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogExtinctionScale`

```text
SetVolumetricFogExtinctionScale(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogAlbedo`

```text
SetVolumetricFogAlbedo(NewValue: FColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `FColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogEmissive`

```text
SetVolumetricFogEmissive(NewValue: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogDistance`

```text
SetVolumetricFogDistance(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogStartDistance`

```text
SetVolumetricFogStartDistance(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogNoiseTexture`

```text
SetVolumetricFogNoiseTexture(NewValue: UTexture2D *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `UTexture2D *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogNoiseTransform`

```text
SetVolumetricFogNoiseTransform(Transform: FTransform) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Transform` | `FTransform` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
