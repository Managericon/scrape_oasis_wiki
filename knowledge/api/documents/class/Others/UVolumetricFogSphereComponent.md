---
id: "api:class:UVolumetricFogSphereComponent"
title: "UVolumetricFogSphereComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UVolumetricFogSphereComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UVolumetricFogSphereComponent

Used to create local volumetric fog.

## Inheritance

`USphereComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VolumetricFogAlbedo` | `FColor` | The height fog particle reflectiveness used by volumetric fog.<br>	  Water particles in air have an albedo near white, while dust has slightly darker value. |
| `VolumetricFogEmissive` | `FLinearColor` | Light emitted by height fog.  This is a density so more light is emitted the further you are looking through the fog.<br>	  In most cases skylight is a better choice, however right now volumetric fog does not support precomputed lighting,<br>	  So stationary skylights are unshadowed and static skylights don't affect volumetric fog at all. |
| `VolumetricFogExtinctionScale` | `float` | Scales the height fog particle extinction amount used by volumetric fog.  Values larger than 1 cause fog particles everywhere absorb more light. |

## Functions

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

## Language

`cpp`
