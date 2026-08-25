---
id: "api:class:UTextureLightProfile"
title: "UTextureLightProfile"
source: "https://developer.gp.qq.com/api/class/detail/Others/UTextureLightProfile.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UTextureLightProfile

## Inheritance

`UTexture2D`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Brightness` | `float` | Light brightness in Lumens, imported from IES profile, <= 0 if the profile is used for masking only. Use with InverseSquareFalloff. |
| `TextureMultiplier` | `float` | Multiplier to map texture value to result to integrate over the sphere to 1.0f |

## Language

`cpp`
