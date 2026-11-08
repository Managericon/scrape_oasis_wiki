---
id: "api:cppstruct:FBackpackV2CheckCapacityResult"
title: "FBackpackV2CheckCapacityResult"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FBackpackV2CheckCapacityResult.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FBackpackV2CheckCapacityResult

CheckCapacity 的检查结果

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bPassed` | `bool` | 检查是否通过（未超容为 true） |
| `PartialExtraItems` | `TMap < FItemDefineID , int32 >` | 添加时可部分容纳的物品<br>	  仅当 CheckCapacity 参数只设置了 ExtraItems，并且检查结果为 false 时有效<br>	  例如 ExtraItems 中 A 物品 10 个，实际只能容纳 5 个：bPassed 为 false，此处记录 A 物品 5 个 |
| `PartialMergeItems` | `TMap < FItemDefineID , int32 >` | Merge 时可部分容纳的物品<br>	  仅当 CheckCapacity 参数只设置了 MergeItems，并且检查结果为 false 时有效<br>	  例如 MergeItems 中 A 物品 10 个，实际只能容纳 5 个：bPassed 为 false，此处记录 A 物品 5 个 |
