---
id: "api:cppstruct:FWeightmapLayerAllocationInfo"
title: "FWeightmapLayerAllocationInfo"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FWeightmapLayerAllocationInfo.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FWeightmapLayerAllocationInfo

Stores information about which weightmap texture and channel each layer is stored

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LayerInfo` | `ULandscapeLayerInfoObject *` | - |
| `WeightmapTextureIndex` | `uint8` | - |
| `WeightmapTextureChannel` | `uint8` | - |
| `bUseForWeightmapPCOnly` | `TEnumAsByte < ELandscapeWeightmapUsage >` | - |
| `WeightmapTextureIndex_ForPC` | `uint8` | - |
| `WeightmapTextureChannel_ForPC` | `uint8` | - |
| `CustomWeightName` | `FName` | - |
| `CustomWeightChannelCount` | `int32` | - |
