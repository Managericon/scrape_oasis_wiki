---
id: "api:cppstruct:FSubModeDynamicLevelsEntry"
title: "FSubModeDynamicLevelsEntry"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FSubModeDynamicLevelsEntry.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FSubModeDynamicLevelsEntry

从 INI 读取的单个 SubModeDynamicLevels 条目

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SubModeIds` | `TArray < int64 >` | 该条目对应的 SubModeId 数组（支持多个 SubModeId 共享同一组 DynamicLevelPaths） |
| `DynamicLevelBlockCoords` | `TArray < FString >` | 该 SubMode 对应的 DynamicLevels 区块坐标集合（INI 中以字符串 "x,y" 形式填写）。<br>	   例：DynamicLevelBlockCoords=("3,1", "5,2")<br>	   FIntPoint 无法被 Config 文本反序列化，故用字符串保存，运行时解析。<br>	   当该 SubMode 激活时，与这些坐标匹配的 Reorg 关卡将被跳过。<br>	   为空表示无区块替换，所有 Reorg 关卡正常加载。<br>	   旧版 DynamicLevelPaths（完整关卡路径列表）仅保留作开发者人工核对，已不参与运行逻辑，见下方注释字段。 |
