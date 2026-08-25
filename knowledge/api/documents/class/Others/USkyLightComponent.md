---
id: "api:class:USkyLightComponent"
title: "USkyLightComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/USkyLightComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# USkyLightComponent

## Inheritance

`ULightComponentBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceType` | `TEnumAsByte < enum ESkyLightSourceType >` | Indicates where to get the light contribution from. |
| `Cubemap` | `UTextureCube *` | Cubemap to use for sky lighting if SourceType is set to SLS_SpecifiedCubemap. |
| `SourceCubemapAngle` | `float` | Angle to rotate the source cubemap when SourceType is set to SLS_SpecifiedCubemap. |
| `CubemapResolution` | `int32` | Maximum resolution for the very top processed cubemap mip. Must be a power of 2. |
| `SkyDistanceThreshold` | `float` | Distance from the sky light at which any geometry should be treated as part of the sky.<br>	  This is also used by reflection captures, so update reflection captures to see the impact. |
| `bCaptureEmissiveOnly` | `bool` | Only capture emissive materials. Skips all lighting making the capture cheaper. Recomended when using CaptureEveryFrame |
| `bLowerHemisphereIsBlack` | `bool` | Whether all distant lighting from the lower hemisphere should be set to LowerHemisphereColor.<br>	  Enabling this is accurate when lighting a scene on a planet where the ground blocks the sky,<br>	  However disabling it can be useful to approximate skylight bounce lighting (eg Movable light). |
| `LowerHemisphereColor` | `FLinearColor` | - |
| `OcclusionMaxDistance` | `float` | Max distance that the occlusion of one point will affect another.<br>	  Higher values increase the cost of Distance Field AO exponentially. |
| `Contrast` | `float` | Contrast S-curve applied to the computed AO.  A value of 0 means no contrast increase, 1 is a significant contrast increase. |
| `OcclusionExponent` | `float` | Exponent applied to the computed AO.  Values lower than 1 brighten occlusion overall without losing contact shadows. |
| `MinOcclusion` | `float` | Controls the darkest that a fully occluded area can get.  This tends to destroy contact shadows, use Contrast or OcclusionExponent instead. |
| `OcclusionTint` | `FColor` | Tint color on occluded areas, artistic control. |
| `OcclusionCombineMode` | `TEnumAsByte < enum EOcclusionCombineMode >` | Controls how occlusion from Distance Field Ambient Occlusion is combined with Screen Space Ambient Occlusion. |
| `bForceHide` | `uint8` | Whether to hide the primitive in game, if the primitive is Visible. |
| `FakeSkyLightAOClampMin` | `float` | - |
| `BlendDestinationCubemap` | `UTextureCube *` | - |

## Functions

### `SetIntensity`

```text
SetIntensity(NewIntensity: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewIntensity` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIndirectLightingIntensity`

```text
SetIndirectLightingIntensity(NewIntensity: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewIntensity` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricScatteringIntensity`

```text
SetVolumetricScatteringIntensity(NewIntensity: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewIntensity` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLightColor`

```text
SetLightColor(NewLightColor: FLinearColor) -> void
```

Set color of the light

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCubemap`

```text
SetCubemap(NewCubemap: UTextureCube *) -> void
```

Sets the cubemap used when SourceType is set to SpecifiedCubemap, and causes a skylight update on the next tick.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewCubemap` | `UTextureCube *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCubemapBlend`

```text
SetCubemapBlend(SourceCubemap: UTextureCube *, DestinationCubemap: UTextureCube *, InBlendFraction: float) -> void
```

Creates sky lighting from a blend between two cubemaps, which is only valid when SourceType is set to SpecifiedCubemap.
	  This can be used to seamlessly transition sky lighting between different times of day.
	  The caller should continue to update the blend until BlendFraction is 0 or 1 to reduce rendering cost.
	  The caller is responsible for avoiding pops due to changing the source or destination.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceCubemap` | `UTextureCube *` | - |
| `DestinationCubemap` | `UTextureCube *` | - |
| `InBlendFraction` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOcclusionTint`

```text
SetOcclusionTint(InTint: FColor &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTint` | `FColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOcclusionContrast`

```text
SetOcclusionContrast(InOcclusionContrast: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOcclusionContrast` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOcclusionExponent`

```text
SetOcclusionExponent(InOcclusionExponent: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOcclusionExponent` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMinOcclusion`

```text
SetMinOcclusion(InMinOcclusion: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMinOcclusion` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetForceHide`

```text
SetForceHide(bInForceHide: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInForceHide` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RecaptureSky`

```text
RecaptureSky() -> void
```

Recaptures the scene for the skylight.
	  This is useful for making sure the sky light is up to date after changing something in the world that it would capture.
	  Warning: this is very costly and will definitely cause a hitch.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
