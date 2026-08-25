---
id: "api:cppstruct:FSlateFontInfo"
title: "FSlateFontInfo"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FSlateFontInfo.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FSlateFontInfo

A representation of a font in Slate.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FontObject` | `UObject *` | The font object (valid when used from UMG or a Slate widget style asset) |
| `FontMaterial` | `UObject *` | The material to use when rendering this font |
| `OutlineSettings` | `FFontOutlineSettings` | Settings for applying an outline to a font |
| `TypefaceFontName` | `FName` | The name of the font to use from the default typeface (None will use the first entry) |
| `Size` | `int32` | The font size is a measure in point values.  The conversion of points to Slate Units is done at 96 dpi.  So if <br>	  you're using a tool like Photoshop to prototype layouts and UI mock ups, be sure to change the default dpi <br>	  measurements from 72 dpi to 96 dpi.<br>	  手机端无法渲染过大的字体图集，且出于内存考虑也不宜将字体设置过大。若有大字体需求，请用小字体+调整Scale的方案。 See MAXFONTSIZE |
| `FontName_DEPRECATED` | `FName` | The name of the font |
| `Hinting_DEPRECATED` | `EFontHinting` | The hinting algorithm to use with the font |
