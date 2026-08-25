---
id: "api:cppstruct:FPrimaryAssetRules"
title: "FPrimaryAssetRules"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FPrimaryAssetRules.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FPrimaryAssetRules

Structure defining rules for what to do with assets, this is defined per type and can be overridden per asset

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Priority` | `int32` | Primary Assets with a higher priority will take precedence over lower priorities when assigning management for referenced assets. If priorities match, both will manage the same Secondary Asset. |
| `bApplyRecursively` | `bool` | If true, this rule will apply to all referenced Secondary Assets recursively, as long as they are not managed by a higher-priority Primary Asset. |
| `PriorityRule` | `EPrimaryAssetPriorityRule` | SetManageReferences时优先级规则. |
| `ChunkId` | `int32` | Assets will be put into this Chunk ID specifically, if set to something other than -1. The default Chunk is Chunk 0. |
| `CookRule` | `EPrimaryAssetCookRule` | Rule describing when this asset should be cooked. |
| `ManagementRules` | `TArray < FManagementRule >` | - |
