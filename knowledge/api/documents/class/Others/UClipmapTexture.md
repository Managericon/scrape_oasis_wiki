---
id: "api:class:UClipmapTexture"
title: "UClipmapTexture"
source: "https://developer.gp.qq.com/api/class/detail/Others/UClipmapTexture.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UClipmapTexture

Runtime virtual texture UObject

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bSkipOneMip` | `bool` | - |
| `DisFirstMip` | `float` | - |
| `bUsePointSample` | `bool` | - |
| `bUseBorder` | `bool` | - |
| `TileSize` | `int32` | - |
| `FirstMipImageSize` | `int32` | - |
| `NumTile` | `int32` | - |
| `bUseCompressType` | `bool` | - |
| `NormalSetting` | `FClipmapSetting` | - |
| `CompressSetting` | `TMap < FString , FClipmapSetting >` | - |
| `bsRGB` | `bool` | - |
| `FileDDCPath` | `FString` | - |
| `ClipmapInfos` | `FClipmapInfos` | - |
| `CompressInfos` | `TMap < FString , FClipmapInfos >` | - |
| `DebugName` | `FString` | - |
| `HashNum` | `uint32` | - |
| `Owner` | `UClipmapTextureComponent *` | - |
| `OriginTexture` | `UTexture2D *` | - |
| `TargetTexture` | `TSoftObjectPtr < UTexture2D >` | - |

## Functions

### `CreateClipmapTargetTexture`

```text
CreateClipmapTargetTexture() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
