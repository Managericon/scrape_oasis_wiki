---
id: "api:cppstruct:FImportanceTexture"
title: "FImportanceTexture"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FImportanceTexture.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FImportanceTexture

Texture processed for importance sampling
 Holds marginal PDF of the rows, as well as the PDF of each row

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Size` | `FIntPoint` | - |
| `NumMips` | `int` | - |
| `MarginalCDF` | `TArray < float >` | - |
| `ConditionalCDF` | `TArray < float >` | - |
| `TextureData` | `TArray < FColor >` | - |
| `Texture` | `TWeakObjectPtr < UTexture2D >` | - |
| `Weighting` | `TEnumAsByte < EImportanceWeight :: Type >` | - |
