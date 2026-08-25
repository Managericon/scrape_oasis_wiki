---
id: "api:class:UTextureRenderTargetCube"
title: "UTextureRenderTargetCube"
source: "https://developer.gp.qq.com/api/class/detail/Others/UTextureRenderTargetCube.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UTextureRenderTargetCube

TextureRenderTargetCube
 
  Cube render target texture resource. This can be used as a target
  for rendering as well as rendered as a regular cube texture resource.

## Inheritance

`UTextureRenderTarget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SizeX` | `int32` | The width of the texture. |
| `ClearColor` | `FLinearColor` | the color the texture is cleared to |
| `OverrideFormat` | `TEnumAsByte < enum EPixelFormat >` | The format of the texture data.											<br>	 Normally the format is derived from bHDR, this allows code to set the format explicitly. |
| `bHDR` | `uint32` | Whether to support storing HDR values, which requires more memory. |
| `bForceLinearGamma` | `uint32` | True to force linear gamma space for this render target |

## Language

`cpp`
