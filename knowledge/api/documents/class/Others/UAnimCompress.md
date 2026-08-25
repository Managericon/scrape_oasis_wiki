---
id: "api:class:UAnimCompress"
title: "UAnimCompress"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAnimCompress.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAnimCompress

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Description` | `FString` | Name of Compression Scheme used for this asset |
| `bNeedsSkeleton` | `uint32` | Compression algorithms requiring a skeleton should set this value to true. |
| `TranslationCompressionFormat` | `TEnumAsByte < AnimationCompressionFormat >` | Format for bitwise compression of translation data. |
| `RotationCompressionFormat` | `TEnumAsByte < AnimationCompressionFormat >` | Format for bitwise compression of rotation data. |
| `ScaleCompressionFormat` | `TEnumAsByte < AnimationCompressionFormat >` | Format for bitwise compression of scale data. |
| `MaxCurveError` | `float` | Max error for compression of curves using remove redundant keys |

## Language

`cpp`
