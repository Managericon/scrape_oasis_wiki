---
id: "api:class:UFontFace"
title: "UFontFace"
source: "https://developer.gp.qq.com/api/class/detail/Others/UFontFace.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UFontFace

A font face asset contains the raw payload data for a source TTFOTF file as used by FreeType.
  During cook this asset type generates a ".ufont" file containing the raw payload data (unless loaded "Inline").

## Inheritance

`UObject` -> `IFontFaceInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceFilename` | `FString` | The filename of the font face we were created from. This may not always exist on disk, as we may have previously loaded and cached the font data inside this asset. |
| `Hinting` | `EFontHinting` | The hinting algorithm to use with the font face. |
| `LoadingPolicy` | `EFontLoadingPolicy` | Enum controlling how this font face should be loaded at runtime. See the enum for more explanations of the options. |
| `LayoutMethod` | `EFontLayoutMethod` | Which method should we use when laying out the font? Try changing this if you notice clipping or height issues with your font. |
| `FontFaceData_DEPRECATED` | `TArray < uint8 >` | The data associated with the font face. This should always be filled in providing the source filename is valid. |

## Language

`cpp`
