---
id: "api:cppstruct:FBackpackV2CheckCapacityParam"
title: "FBackpackV2CheckCapacityParam"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FBackpackV2CheckCapacityParam.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FBackpackV2CheckCapacityParam

CheckCapacity 的检查参数

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ExtraItems` | `TMap < FItemDefineID , int32 >` | 额外的物品，检查时额外计算的物品（可以通过此参数预检查物品加入背包后的情况） |
| `MergeItems` | `TMap < FItemDefineID , int32 >` | 即将 Merge 到已有物品堆叠上的数量<br>	  可以通过此参数预检查堆叠数量增加后占用容量的情况 |
| `ExcludedItems` | `TMap < FItemDefineID , int32 >` | 排除的物品，检查时需要从背包物品列表中排除的物品（可以通过此参数预检查物品离开背包后的情况） |
| `UnEquipOrDetachItems` | `TArray < FItemDefineID >` | 即将取消装备或取消 Attach 的物品<br>	  可以通过此参数预检查这些物品回到背包后占用容量的情况 |
| `RootOperate` | `EBackpackV2RootOperate` | 当前背包根操作<br>	  若 A 操作会引发 B 操作，则 A 为父操作，最父级的操作为根操作<br>	  比如触发丢弃装备时，可能先触发装备卸下，再完成丢弃。则根操作为丢弃。 |
