---
id: "api:cppstruct:FDynamicTextureInstance"
title: "FDynamicTextureInstance"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FDynamicTextureInstance.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FDynamicTextureInstance

Serialized ULevel information about dynamic texture instances

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Texture` | `UTexture2D *` | Texture that is used by a dynamic UPrimitiveComponent. |
| `bAttached` | `bool` | Whether the primitive that uses this texture is attached to the scene or not. |
| `OriginalRadius` | `float` | Original bounding sphere radius, at the time the TexelFactor was calculated originally. |
