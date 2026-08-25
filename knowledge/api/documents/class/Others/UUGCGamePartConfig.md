---
id: "api:class:UUGCGamePartConfig"
title: "UUGCGamePartConfig"
source: "https://developer.gp.qq.com/api/class/detail/Others/UUGCGamePartConfig.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UUGCGamePartConfig

GamePart配置基类

## Inheritance

`UPrimaryDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GamePartName` | `FName` | GamePart名称 |
| `DependentGameParts` | `TArray < FName >` | 依赖的的GamePart列表 |
| `GlobalActorClass` | `TSubclassOf < AActor >` | GlobalActor类配置 |
| `PlayerComponentConfigs` | `TArray < FUGCGamePartPlayerComponentConfig >` | GamePart PlayerComponent配置列表 |

## Language

`cpp`
