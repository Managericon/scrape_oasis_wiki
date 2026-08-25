---
id: "api:cppstruct:FFontOutlineSettings"
title: "FFontOutlineSettings"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FFontOutlineSettings.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FFontOutlineSettings

Settings for applying an outline to a font

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OutlineSize` | `int32` | Size of the outline in slate units (at 1.0 font scale this unit is a pixel) |
| `OutlineMaterial` | `UObject *` | Optional material to apply to the outline |
| `OutlineColor` | `FLinearColor` | The color of the outline for any character in this font |
| `bSeparateFillAlpha` | `bool` | If checked, the outline will be completely translucent where the filled area will be.  This allows for a separate fill alpha value<br>	  The trade off when enabling this is slightly worse quality for completely opaque fills where the inner outline border meets the fill area |
