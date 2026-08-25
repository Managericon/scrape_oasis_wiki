---
id: "api:class:ULandscapeInfo"
title: "ULandscapeInfo"
source: "https://developer.gp.qq.com/api/class/detail/Others/ULandscapeInfo.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ULandscapeInfo

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LandscapeActor` | `TLazyObjectPtr < ALandscape >` | - |
| `LandscapeGuid` | `FGuid` | - |
| `ComponentSizeQuads` | `int32` | - |
| `SubsectionSizeQuads` | `int32` | - |
| `ComponentNumSubsections` | `int32` | - |
| `DrawScale` | `FVector` | - |
| `Proxies` | `TSet < ALandscapeStreamingProxy * >` | - |
| `Layers` | `TArray < FLandscapeInfoLayerSettings >` | - |
| `RChannelLayer` | `TWeakObjectPtr < ULandscapeLayerInfoObject >` | - |
| `GChannelLayer` | `TWeakObjectPtr < ULandscapeLayerInfoObject >` | - |
| `BChannelLayer` | `TWeakObjectPtr < ULandscapeLayerInfoObject >` | - |
| `AChannelLayer` | `TWeakObjectPtr < ULandscapeLayerInfoObject >` | - |
| `RChannelCustomWeight` | `int32` | - |
| `GChannelCustomWeight` | `int32` | - |
| `BChannelCustomWeight` | `int32` | - |
| `AChannelCustomWeight` | `int32` | - |

## Language

`cpp`
