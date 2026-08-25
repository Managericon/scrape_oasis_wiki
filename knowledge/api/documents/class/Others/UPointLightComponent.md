---
id: "api:class:UPointLightComponent"
title: "UPointLightComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPointLightComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPointLightComponent

A light component which emits light from a single point equally in all directions.

## Inheritance

`ULightComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Radius_DEPRECATED` | `float` | - |
| `AttenuationRadius` | `float` | Bounds the light's visible influence.  <br>	  This clamping of the light's influence is not physically correct but very important for performance, larger lights cost more. |
| `bUseInverseSquaredFalloff` | `uint32` | Whether to use physically based inverse squared distance falloff, where AttenuationRadius is only clamping the light's contribution.  <br>	  Disabling inverse squared falloff can be useful when placing fill lights (don't want a super bright spot near the light).<br>	  When enabled, the light's Intensity is in units of lumens, where 1700 lumens is a 100W lightbulb.<br>	  When disabled, the light's Intensity is a brightness scale. |
| `LightFalloffExponent` | `float` | Controls the radial falloff of the light when UseInverseSquaredFalloff is disabled. <br>	  2 is almost linear and very unrealistic and around 8 it looks reasonable.<br>	  With large exponents, the light has contribution to only a small area of its influence radius but still costs the same as low exponents. |
| `SourceRadius` | `float` | Radius of light source shape.<br>	  Note that light sources shapes which intersect shadow casting geometry can cause shadowing artifacts. |
| `SoftSourceRadius` | `float` | Soft radius of light source shape.<br>	 Note that light sources shapes which intersect shadow casting geometry can cause shadowing artifacts. |
| `SourceLength` | `float` | Length of light source shape.<br>	  Note that light sources shapes which intersect shadow casting geometry can cause shadowing artifacts. |
| `bSimulateRectLight` | `uint32` | By luciuszhang: when in rect light mode, source radius is the rect light source width. |
| `bSimulatePortalLight` | `uint32` | By luciuszhang: Portal light will be used in lightmass for IdeaBake, it is just a flag for Rect Light. |
| `RectLightSourceWidth` | `float` | By luciuszhang: rect light source width. |
| `RectLightSourceHeight` | `float` | By luciuszhang: rect light source height. |
| `bEnableForVertexPointLight` | `uint32` | - |
| `LightmassSettings` | `FLightmassPointLightSettings` | The Lightmass settings for this object. |

## Functions

### `SetAttenuationRadius`

```text
SetAttenuationRadius(NewRadius: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRadius` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLightFalloffExponent`

```text
SetLightFalloffExponent(NewLightFalloffExponent: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightFalloffExponent` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSourceRadius`

```text
SetSourceRadius(bNewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSoftSourceRadius`

```text
SetSoftSourceRadius(bNewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSourceLength`

```text
SetSourceLength(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSimulateRectLight`

```text
SetSimulateRectLight(newValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `newValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSimulatePortalLight`

```text
SetSimulatePortalLight(newValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `newValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRectLightSourceWidth`

```text
SetRectLightSourceWidth(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRectLightSourceHeight`

```text
SetRectLightSourceHeight(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
