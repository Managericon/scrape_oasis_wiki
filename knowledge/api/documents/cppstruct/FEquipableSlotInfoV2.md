---
id: "api:cppstruct:FEquipableSlotInfoV2"
title: "FEquipableSlotInfoV2"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FEquipableSlotInfoV2.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FEquipableSlotInfoV2

可装备槽位信息
  描述一个物品可以装备到的目标位置

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParentItem` | `FItemDefineID` | 父物品DefineID<br>	  如果是装备到背包槽位上，则为无效物品（FItemDefineID()）<br>	  如果是作为配件装备到某个物品上，则为该物品的DefineID |
| `SlotName` | `FName` | 目标槽位名称 |
| `OccupiedItem` | `FItemDefineID` | 当前占据该槽位的物品（如果有）<br>	  无效则表示槽位为空 |
| `bIsOccupied` | `bool` | 该槽位是否已被占据 |
