---
id: "api:cppstruct:FFontData"
title: "FFontData"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FFontData.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FFontData

Payload data describing an individual font in a typeface. Keep this lean as it's also used as a key!

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FontFilename` | `FString` | The filename of the font to use.<br>	  This variable is ignored if we have a font face asset, and is set to the .ufont file in a cooked build. |
| `Hinting` | `EFontHinting` | The hinting algorithm to use with the font.<br>	  This variable is ignored if we have a font face asset, and is synchronized with the font face asset on load in a cooked build. |
| `LoadingPolicy` | `EFontLoadingPolicy` | Enum controlling how this font should be loaded at runtime. See the enum for more explanations of the options.<br>	  This variable is ignored if we have a font face asset, and is synchronized with the font face asset on load in a cooked build. |
| `FontFaceAsset` | `UObject *` | Font data v3. This points to a font face asset. |
| `BulkDataPtr_DEPRECATED` | `UFontBulkData *` | Legacy font data v2. This used to be where font data was stored prior to font face assets. <br>	  This can be removed once we no longer support loading packages older than FEditorObjectVersion::AddedFontFaceAssets (as can UFontBulkData itself). |
| `FontData_DEPRECATED` | `TArray < uint8 >` | Legacy font data v1. This used to be where font data was stored prior to font bulk data.<br>	  This can be removed once we no longer support loading packages older than VER_UE4_SLATE_BULK_FONT_DATA. |
