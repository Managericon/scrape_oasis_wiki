---
id: "api:class:ALandscape"
title: "ALandscape"
source: "https://developer.gp.qq.com/api/class/detail/Others/ALandscape.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ALandscape

## Inheritance

`ALandscapeProxy`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaterialIdUserSettings` | `FMaterialIdUserSettings` | - |
| `UseFarLandNormalDistance` | `float` | - |
| `BlendFarLandNormalDistance` | `float` | - |
| `FarLandVertexColorThreshold` | `float` | - |
| `FarLandVertexColorBlendThreshold` | `float` | - |
| `bUseLandscapeDeform` | `bool` | - |
| `bCanUseMaterialIdShading` | `bool` | - |
| `CurrentBiomesIndex` | `int32` | Current selected biomes info |
| `bTextureArrayDirty` | `bool` | - |
| `PaintingCustomWeightLayerIndex` | `int32` | - |
| `MatIdLayerVisibility` | `TArray < bool >` | - |
| `FarLandDiffuseTexture` | `UTexture2D *` | - |
| `FarLandNormalTexture` | `UTexture2D *` | - |
| `FarLandInfoDebug` | `TMap < ULandscapeComponent * , FFarLandInfo >` | - |
| `ExportSplatmapTexture` | `UTexture2D *` | - |
| `Platform` | `EMyLandscapePlatfromConfiguration` | - |
| `PCConfig` | `FMyLandscapeConfigurationParams` | - |
| `MobileConfig` | `FMyLandscapeConfigurationParams` | - |

## Functions

### `EnumerateLandscapePaintMatIDLayers`

```text
EnumerateLandscapePaintMatIDLayers(Landscape: ALandscapeProxy *) -> LANDSCAPE_API TArray < FName >
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Landscape` | `ALandscapeProxy *` | - |

**Returns**

| Type | Description |
|---|---|
| `LANDSCAPE_API TArray < FName >` | - |

### `IsMaterialIDLandscape`

```text
IsMaterialIDLandscape(Landscape: ALandscapeProxy *) -> LANDSCAPE_API bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Landscape` | `ALandscapeProxy *` | - |

**Returns**

| Type | Description |
|---|---|
| `LANDSCAPE_API bool` | - |

### `SetLandscapeCorner`

```text
SetLandscapeCorner() -> LANDSCAPE_API void
```

**Returns**

| Type | Description |
|---|---|
| `LANDSCAPE_API void` | - |

### `SplitFarLandTextureForComponent`

```text
SplitFarLandTextureForComponent() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetFarLandTextureInfo`

```text
GetFarLandTextureInfo() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GenerateSplatmapMip`

```text
GenerateSplatmapMip() -> LANDSCAPE_API void
```

**Returns**

| Type | Description |
|---|---|
| `LANDSCAPE_API void` | - |

### `ExportWeightAsSplatmapMipEditor`

```text
ExportWeightAsSplatmapMipEditor() -> LANDSCAPE_API void
```

**Returns**

| Type | Description |
|---|---|
| `LANDSCAPE_API void` | - |

### `BuildLandscapeStaticMesh`

```text
BuildLandscapeStaticMesh() -> void
```

UFUNCTION(CallInEditor, Category = "Build Static Mesh", meta = (CallInEditor = "true"))

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
