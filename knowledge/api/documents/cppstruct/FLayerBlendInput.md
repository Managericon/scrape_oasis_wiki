---
id: "api:cppstruct:FLayerBlendInput"
title: "FLayerBlendInput"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FLayerBlendInput.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FLayerBlendInput

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LayerName` | `FName` | - |
| `BlendType` | `TEnumAsByte < ELandscapeLayerBlendType >` | - |
| `LayerInput` | `FExpressionInput` | - |
| `HeightInput` | `FExpressionInput` | - |
| `PreviewWeight` | `float` | - |
| `ConstLayerInput` | `FVector` | only used if LayerInput is not hooked up |
| `ConstHeightInput` | `float` | only used if HeightInput is not hooked up |
