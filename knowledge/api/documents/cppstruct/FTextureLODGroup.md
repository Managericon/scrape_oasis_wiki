---
id: "api:cppstruct:FTextureLODGroup"
title: "FTextureLODGroup"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FTextureLODGroup.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FTextureLODGroup

LOD settings for a single texture group.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Group` | `TEnumAsByte < TextureGroup >` | Minimum LOD mip count below which the code won't bias. |
| `LODBias` | `int32` | Group LOD bias. |
| `NumStreamedMips` | `int32` | Number of mip-levels that can be streamed. -1 means all mips can stream. |
| `MipGenSettings` | `TEnumAsByte < TextureMipGenSettings >` | Defines how the the mip-map generation works, e.g. sharpening |
| `MinLODSize` | `int32` | - |
| `MaxLODSize` | `int32` | - |
| `MinMagFilter` | `FName` | - |
| `MipFilter` | `FName` | - |
