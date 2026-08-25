---
id: "api:class:ULightComponentBase"
title: "ULightComponentBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/ULightComponentBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ULightComponentBase

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LightGuid` | `FGuid` | GUID used to associate a light component with precomputed shadowing information across levels.<br>	  The GUID changes whenever the light position changes. |
| `Brightness_DEPRECATED` | `float` | - |
| `Intensity` | `float` | Total energy that the light emits.  <br>	  For pointspot lights with inverse squared falloff, this is in units of lumens.  1700 lumens corresponds to a 100W lightbulb. <br>	  For other lights, this is just a brightness multiplier. |
| `LightColor` | `FColor` | Filter color of the light.<br>	  Note that this can change the light's effective intensity. |
| `bAffectsWorld` | `uint32` | Whether the light can affect the world, or whether it is disabled.<br>	  A disabled light will not contribute to the scene in any way.  This setting cannot be changed at runtime and unbuilds lighting when changed.<br>	  Setting this to false has the same effect as deleting the light, so it is useful for non-destructive experiments. |
| `CastShadows` | `uint32` | Whether the light should cast any shadows. |
| `CastStaticShadows` | `uint32` | Whether the light should cast shadows from static objects.  Also requires Cast Shadows to be set to True. |
| `CastDynamicShadows` | `uint32` | Whether the light should cast shadows from dynamic objects.  Also requires Cast Shadows to be set to True. |
| `bAffectTranslucentLighting` | `uint32` | Whether the light affects translucency or not.  Disabling this can save GPU time when there are many small lights. |
| `bCastVolumetricShadow` | `uint32` | Whether the light shadows volumetric fog.  Disabling this can save GPU time. |
| `RequiredDeviceLevel` | `int32` | - |
| `IndirectLightingIntensity` | `float` | Scales the indirect lighting contribution from this light. <br>	  A value of 0 disables any GI from this light. Default is 1. |
| `VolumetricScatteringIntensity` | `float` | Intensity of the volumetric scattering from this light.  This scales Intensity and LightColor. |

## Functions

### `SetCastShadows`

```text
SetCastShadows(bNewValue: bool) -> void
```

Sets whether this light casts shadows

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLightColor`

```text
GetLightColor() -> FLinearColor
```

Gets the light color as a linear color

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `SetCastVolumetricShadow`

```text
SetCastVolumetricShadow(bNewValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
