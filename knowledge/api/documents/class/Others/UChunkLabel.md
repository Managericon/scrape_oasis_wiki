---
id: "api:class:UChunkLabel"
title: "UChunkLabel"
source: "https://developer.gp.qq.com/api/class/detail/Others/UChunkLabel.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UChunkLabel

## Inheritance

`UPrimaryDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Rules` | `FPrimaryAssetRules` | Management rules for this specific asset, if set it will override the type rules |
| `LogicChunkName` | `FString` | True to Label everything in this directory and sub directories |
| `FinalChunkName` | `FString` | - |
| `ChunkOutputPath` | `FString` | - |
| `bIsRuntimeLabel` | `uint32` | Set to true if the label asset itself should be cooked and available at runtime. This does not affect the assets that are labeled, they are set with cook rule |
| `Key` | `FString` | - |
| `IV` | `FString` | - |
| `ManagerRuleNames` | `TArray < FString >` | - |
| `bUpdateManagerRulesWhenSaved` | `bool` | - |
| `bForceReloadManagerRule` | `bool` | - |

## Language

`cpp`
