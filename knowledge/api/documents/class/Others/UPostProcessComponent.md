---
id: "api:class:UPostProcessComponent"
title: "UPostProcessComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPostProcessComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPostProcessComponent

PostProcessComponent. Enables Post process controls for blueprints.
 	Will use a parent UShapeComponent to provide volume data if available.

## Inheritance

`USceneComponent` -> `IInterface_PostProcessVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Settings` | `FPostProcessSettings` | Post process settings to use for this volume. |
| `Priority` | `float` | Priority of this volume. In the case of overlapping volumes the one with the highest priority<br>	  overrides the lower priority ones. The order is undefined if two or more overlapping volumes have the same priority. |
| `BlendRadius` | `float` | World space radius around the volume that is used for blending (only if not unbound). |
| `BlendWeight` | `float` | 0:no effect, 1:full effect |
| `bEnabled` | `uint32` | Whether this volume is enabled or not. |
| `bUnbound` | `uint32` | set this to false to use the parent shape component as volume bounds. True affects the whole world regardless. |

## Functions

### `AddOrUpdateBlendable`

```text
AddOrUpdateBlendable(InBlendableObject: TScriptInterface < IBlendableInterface >, InWeight: float) -> ENGINE_API void
```

Adds an Blendable (implements IBlendableInterface) to the array of Blendables (if it doesn't exist) and update the weight

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlendableObject` | `TScriptInterface < IBlendableInterface >` | - |
| `InWeight` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `AddWeatherCompTag`

```text
AddWeatherCompTag() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearCustomGIFallbackSH`

```text
ClearCustomGIFallbackSH() -> ENGINE_API void
```

Clear all Custom GI Fallback SH coefficients (reset to zero)

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GenerateCustomGIFallbackSH`

```text
GenerateCustomGIFallbackSH() -> ENGINE_API void
```

Generate Custom GI Fallback SH coefficients from directional colors using Monte Carlo integration

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GenerateCustomGIFallbackSHFromCubeMap`

```text
GenerateCustomGIFallbackSHFromCubeMap() -> ENGINE_API void
```

Generate Spherical Harmonics coefficients from CubeMap texture using Monte Carlo sampling

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

## Language

`cpp`
