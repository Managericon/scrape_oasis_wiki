---
id: "api:cppstruct:FStaticMaterial"
title: "FStaticMaterial"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FStaticMaterial.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FStaticMaterial

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaterialInterface` | `UMaterialInterface *` | - |
| `MaterialSlotName` | `FName` | This name should be use by the gameplay to avoid error if the skeletal mesh Materials array topology change |
| `UVChannelData` | `FMeshUVChannelInfo` | Data used for texture streaming relative to each UV channels. |
| `MaterialSoftRef` | `FSoftObjectPath` | Soft Reference to MaterialInterface |
| `ImportedMaterialSlotName` | `FName` | This name should be use when we re-import a skeletal mesh so we can order the Materials array like it should be |
