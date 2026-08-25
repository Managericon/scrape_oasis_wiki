---
id: "api:class:UCompositionGraphCaptureSettings"
title: "UCompositionGraphCaptureSettings"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCompositionGraphCaptureSettings.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UCompositionGraphCaptureSettings

## Inheritance

`UMovieSceneCaptureProtocolSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `IncludeRenderPasses` | `FCompositionGraphCapturePasses` | A list of render passes to include in the capture. Leave empty to export all available passes. |
| `bCaptureFramesInHDR` | `bool` | Whether to capture the frames as HDR textures (.exr format) |
| `HDRCompressionQuality` | `int32` | Compression Quality for HDR Frames (0 for no compression, 1 for default compression which can be slow) |
| `CaptureGamut` | `TEnumAsByte < enum EHDRCaptureGamut >` | The color gamut to use when storing HDR captured data. The gamut depends on whether the bCaptureFramesInHDR option is enabled. |
| `PostProcessingMaterial` | `FSoftObjectPath` | Custom post processing material to use for rendering |

## Language

`cpp`
