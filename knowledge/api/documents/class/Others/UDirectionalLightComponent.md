---
id: "api:class:UDirectionalLightComponent"
title: "UDirectionalLightComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UDirectionalLightComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UDirectionalLightComponent

A light component that has parallel rays. Will provide a uniform lighting across any affected surface (eg. The Sun). This will affect all objects in the defined light-mass importance volume.

## Inheritance

`ULightComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnableLightShaftOcclusion` | `uint32` | Whether to occlude fog and atmosphere inscattering with screenspace blurred occlusion from this light. |
| `OcclusionMaskDarkness` | `float` | Controls how dark the occlusion masking is, a value of 1 results in no darkening term. |
| `OcclusionDepthRange` | `float` | Everything closer to the camera than this distance will occlude light shafts. |
| `LightShaftOverrideDirection` | `FVector` | Can be used to make light shafts come from somewhere other than the light's actual direction.<br>	  This will only be used when non-zero.  It does not have to be normalized. |
| `WholeSceneDynamicShadowRadius_DEPRECATED` | `float` | - |
| `DynamicShadowDistanceMovableLight` | `float` | How far Cascaded Shadow Map dynamic shadows will cover for a movable light, measured from the camera.<br>	  A value of 0 disables the dynamic shadow. |
| `DynamicShadowDistanceStationaryLight` | `float` | How far Cascaded Shadow Map dynamic shadows will cover for a stationary light, measured from the camera.<br>	  A value of 0 disables the dynamic shadow. |
| `DynamicShadowCascades` | `int32` | Number of cascades to split the view frustum into for the whole scene dynamic shadow.<br>	  More cascades result in better shadow resolution, but adds significant rendering cost. |
| `CascadeDistributionExponent` | `float` | Controls whether the cascades are distributed closer to the camera (larger exponent) or further from the camera (smaller exponent).<br>	  An exponent of 1 means that cascade transitions will happen at a distance proportional to their resolution. |
| `CascadeTransitionFraction` | `float` | Proportion of the fade region between cascades.<br>	  Pixels within the fade region of two cascades have their shadows blended to avoid hard transitions between quality levels.<br>	  A value of zero eliminates the fade region, creating hard transitions.<br>	  Higher values increase the size of the fade region, creating a more gradual transition between cascades.<br>	  The value is expressed as a percentage proportion (i.e. 0.1 = 10% overlap).<br>	  Ideal values are the smallest possible which still hide the transition.<br>	  An increased fade region size causes an increase in shadow rendering cost. |
| `ShadowDistanceFadeoutFraction` | `float` | Controls the size of the fade out region at the far extent of the dynamic shadow's influence.<br>	  This is specified as a fraction of DynamicShadowDistance. |
| `bUseIndependentShadowBound` | `uint32` | - |
| `ShadowCenterOffset` | `float` | Offset of the CSM shadow center in the viewing direction. |
| `ShadowIndependentRadius` | `float` | - |
| `bUseInsetShadowsForMovableObjects` | `uint32` | Stationary lights only: Whether to use per-object inset shadows for movable components, even though cascaded shadow maps are enabled.<br>	  This allows dynamic objects to have a shadow even when they are outside of the cascaded shadow map, which is important when DynamicShadowDistanceStationaryLight is small.<br>	  If DynamicShadowDistanceStationaryLight is large (currently > 8000), this will be forced off.<br>	  Disabling this can reduce shadowing cost significantly with many movable objects. |
| `FarShadowCascadeCount` | `int32` | 0: no DistantShadowCascades, otherwise the count of cascades between WholeSceneDynamicShadowRadius and DistantShadowDistance that are covered by distant shadow cascades. |
| `FarShadowDistance` | `float` | Distance at which the far shadow cascade should end.  Far shadows will cover the range between 'Dynamic Shadow Distance' and this distance. |
| `DistanceFieldShadowDistance` | `float` | Distance at which the ray traced shadow cascade should end.  Distance field shadows will cover the range between 'Dynamic Shadow Distance' this distance. |
| `ForwardShadingPriority` | `int32` | Forward lighting priority for the single directional light that will be used for forward shading, translucent, single layer water and volumetric fog.<br>	 When two lights have equal priorities, the selection will be based on their overall brightness as a fallback. |
| `LightSourceAngle` | `float` | Light source angle in degrees, used for dynamic shadowing methods.<br>	  Currently only Ray Traced Distance Field shadows and Capsule shadows support area shadows, and therefore make use of LightSourceAngle. |
| `TraceDistance` | `float` | Determines how far shadows can be cast, in world units.  Larger values increase the shadowing cost. |
| `LightmassSettings` | `FLightmassDirectionalLightSettings` | The Lightmass settings for this object. |
| `bCastModulatedShadows` | `uint32` | Whether the light should cast modulated shadows from dynamic objects (mobile only).  Also requires Cast Shadows to be set to True. |
| `bCastsLandscapeShadow` | `uint32` | - |
| `LandscapeShadowColor` | `float` | - |
| `LandscapeShadowOffset` | `float` | - |
| `LandscapeShadowSoftHeight` | `float` | - |
| `LandscapeShadowPixelPrecision` | `float` | - |
| `LandscapeGeometry` | `ULandscapeGeometryAsset *` | - |
| `bCastPhotonShadow` | `uint32` | #if WITH_PHOTON_SHADOW<br>	 Whether the light should cast photon shadow for character<br>	 #endif |
| `bCastPhotonPerObjectShadow` | `uint32` | - |
| `SoftShadowSoftness` | `float` | - |
| `ShadowBlendFactor` | `float` | - |
| `BoundsScale` | `float` | - |
| `NearPlaneOffset` | `float` | - |
| `FarPlaneOffset` | `float` | - |
| `SplitNearOffset` | `float` | - |
| `SplitFarOffset` | `float` | - |
| `ShadowMapResolution` | `float` | - |
| `ModulatedShadowColor` | `FColor` | Color to modulate against the scene color when rendering modulated shadows. (mobile only) |
| `ACESParameters` | `TArray < FACESParameter >` | - |
| `bUsedAsAtmosphereSunLight` | `uint32` | - |
| `bCastsCloudShadow` | `uint32` | - |
| `CloudShadowTexture` | `UTexture *` | - |
| `CloudShadowTileSize` | `float` | - |
| `CloudShadowDensity` | `float` | - |
| `CloudShadowWinSpeed` | `FVector2D` | - |
| `bUseGridShadow` | `uint32` | - |
| `GridShadowSplitSettings` | `TArray < FGridShadowSplitSettings >` | - |

## Functions

### `SetCastPhotonPerObjectShadow`

```text
SetCastPhotonPerObjectShadow(InValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDynamicShadowDistanceMovableLight`

```text
SetDynamicShadowDistanceMovableLight(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDynamicShadowDistanceStationaryLight`

```text
SetDynamicShadowDistanceStationaryLight(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDynamicShadowCascades`

```text
SetDynamicShadowCascades(NewValue: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCascadeDistributionExponent`

```text
SetCascadeDistributionExponent(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCascadeTransitionFraction`

```text
SetCascadeTransitionFraction(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetShadowDistanceFadeoutFraction`

```text
SetShadowDistanceFadeoutFraction(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetForwardShadingPriority`

```text
SetForwardShadingPriority(NewValue: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetEnableLightShaftOcclusion`

```text
SetEnableLightShaftOcclusion(bNewValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOcclusionMaskDarkness`

```text
SetOcclusionMaskDarkness(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLightShaftOverrideDirection`

```text
SetLightShaftOverrideDirection(NewValue: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCastsCloudShadow`

```text
SetCastsCloudShadow(InValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCloudShadowTexture`

```text
SetCloudShadowTexture(InTexture: UTexture *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTexture` | `UTexture *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCloudShadowTileSize`

```text
SetCloudShadowTileSize(InValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCloudShadowDensity`

```text
SetCloudShadowDensity(InDensity: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDensity` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCloudShadowWinSpeed`

```text
SetCloudShadowWinSpeed(InWinSpeed: FVector2D &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InWinSpeed` | `FVector2D &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
