---
id: "api:class:UTextureLODSettings"
title: "UTextureLODSettings"
source: "https://developer.gp.qq.com/api/class/detail/Others/UTextureLODSettings.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UTextureLODSettings

Structure containing all information related to an LOD group and providing helper functions to calculate
  the LOD bias of a given group.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TextureLODGroups` | `TArray < FTextureLODGroup >` | Array of LOD settings with entries per group. |
| `TextureLODGroupsFilterCache` | `TMap < TEnumAsByte < TextureGroup > , ETextureSamplerFilter >` | - |

## Language

`cpp`
