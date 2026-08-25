---
id: "api:class:UMaterialInterface"
title: "UMaterialInterface"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialInterface.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
