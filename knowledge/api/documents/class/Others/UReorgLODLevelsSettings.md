---
id: "api:class:UReorgLODLevelsSettings"
title: "UReorgLODLevelsSettings"
source: "https://developer.gp.qq.com/api/class/detail/Others/UReorgLODLevelsSettings.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UReorgLODLevelsSettings

每张地图的 Reorg LOD 关卡路径白名单 INI 配置基类

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LevelPath` | `FString` | 用于匹配的关卡路径前缀（例如 "GameMapsPUBG_Baltic"） |
| `LODLevelsPath` | `TArray < FString >` | 命中后即视为"真正 LOD 关卡"的路径白名单（前缀匹配） |

## Language

`cpp`
