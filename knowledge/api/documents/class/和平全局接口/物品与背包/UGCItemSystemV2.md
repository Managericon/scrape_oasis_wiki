---
id: "api:class:UGCItemSystemV2"
title: "UGCItemSystemV2"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81%E4%B8%8E%E8%83%8C%E5%8C%85/UGCItemSystemV2.json"
category: "API Wiki/class/和平全局接口/物品与背包"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCItemSystemV2

V2道具系统接口库

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCItemSystemV2._GetterOverrides` | `-` | 存储外部注册的 Get 重写委托 key: 函数名（如 "GetItemNameV2ByDefineID"）, value: 重写函数 @type table |

## Functions

### `RegisterItemPropertyGetOverride`

```text
RegisterItemPropertyGetOverride(Key: EItemOverrideKey) -> boolean
```

注册物品属性读取函数
生效范围：服务器&客户端分别注册

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `EItemOverrideKey` | 属性枚举值，使用 EItemOverrideKey.XXX |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否注册成功 |

### `UnregisterItemPropertyGetOverride`

```text
UnregisterItemPropertyGetOverride(Key: EItemOverrideKey|nil) -> boolean
```

注销物品属性读取函数
生效范围：服务器&客户端分别反注册

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `EItemOverrideKey\|nil` | 属性枚举值，使用 EItemOverrideKey.XXX；不传则清除所有 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否注销成功 |

### `GetConfigItemHandle`

```text
GetConfigItemHandle(ItemID: number) -> UBattleItemHandleBase
```

获取物品 ItemHandle 配置
可以通过它取得所有物品中配置的数据（只读）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `UBattleItemHandleBase` | 配置数据 |

### `GetItemInstanceDataManager`

```text
GetItemInstanceDataManager() -> UUGCBattleItemInstanceDataManager
```

获取物品实例数据管理器
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `UUGCBattleItemInstanceDataManager` | 实例数据管理器 |

### `IsUGCItemV2`

```text
IsUGCItemV2(ItemID: number) -> boolean
```

是否为绿洲物品（物资编辑器中自定义物品）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为绿洲物品 |

### `IsShouldPersist`

```text
IsShouldPersist(ItemID: number) -> boolean
```

是否持久化
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否持久化 |

### `IsObjEditorItemV2`

```text
IsObjEditorItemV2(ItemID: number) -> boolean
```

是否为V2版本物编创建的物品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为V2版本物编创建的物品 |

### `GetItemNameV2`

```text
GetItemNameV2(ItemID: number) -> string
```

返回物品名称
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品名称 |

### `GetItemNameV2ByDefineID`

```text
GetItemNameV2ByDefineID(ItemDefineID: FItemDefineID) -> string
```

返回物品名称（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品名称 |

### `GetItemSubTypeV2`

```text
GetItemSubTypeV2(ItemID: number) -> number
```

返回物品子类型SubType，(比如武器类别为1，M146子类型为101)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品子类型 |

### `GetItemIconTextureV2`

```text
GetItemIconTextureV2(ItemID: number) -> FSoftObjectPath
```

返回物品图标路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 物品图标路径 |

### `GetItemIconTextureV2ByDefineID`

```text
GetItemIconTextureV2ByDefineID(ItemDefineID: FItemDefineID) -> FSoftObjectPath
```

返回物品图标路径（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 物品图标路径 |

### `GetOwnBackpackComponent`

```text
GetOwnBackpackComponent(ItemHandle: UBattleItemHandleBase) -> BackpackComponentV2
```

读取物品所在背包
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemHandle` | `UBattleItemHandleBase` | 物品 Handle |

**Returns**

| Type | Description |
|---|---|
| `BackpackComponentV2` | V2背包组件 |

### `GetItemIconWithPlayerSkinV2`

```text
GetItemIconWithPlayerSkinV2(ItemID: number, PlayerController: PlayerController) -> FSoftObjectPath
```

返回物品图标路径(带玩家皮肤)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |
| `PlayerController` | `PlayerController` | 玩家 PlayerController |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 物品图标路径 |

### `GetItemIconWithPlayerSkinV2ByDefineID`

```text
GetItemIconWithPlayerSkinV2ByDefineID(ItemDefineID: FItemDefineID, PlayerController: PlayerController) -> FSoftObjectPath
```

返回物品图标路径(带玩家皮肤)（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |
| `PlayerController` | `PlayerController` | 玩家 PlayerController |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 物品图标路径 |

### `GetWhiteIconTextureV2`

```text
GetWhiteIconTextureV2(ItemID: number) -> FSoftObjectPath
```

返回物品剪影图标路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 剪影图标路径 |

### `GetWhiteIconTextureV2ByDefineID`

```text
GetWhiteIconTextureV2ByDefineID(ItemDefineID: FItemDefineID) -> FSoftObjectPath
```

返回物品剪影图标路径（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 剪影图标路径 |

### `GetBigIconTextureV2`

```text
GetBigIconTextureV2(ItemID: number) -> FSoftObjectPath
```

返回物品装备栏图标路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 装备栏图标路径 |

### `GetBigIconTextureV2ByDefineID`

```text
GetBigIconTextureV2ByDefineID(ItemDefineID: FItemDefineID) -> FSoftObjectPath
```

返回物品装备栏图标路径（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 装备栏图标路径 |

### `GetBigIconTextureWithPlayerSkinV2`

```text
GetBigIconTextureWithPlayerSkinV2(ItemID: number, PlayerController: PlayerController) -> FSoftObjectPath
```

返回物品装备栏图标路径(带玩家皮肤)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |
| `PlayerController` | `PlayerController` | 玩家 PlayerController |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 装备栏图标路径 |

### `GetBigIconTextureWithPlayerSkinV2ByDefineID`

```text
GetBigIconTextureWithPlayerSkinV2ByDefineID(ItemDefineID: FItemDefineID, PlayerController: PlayerController) -> FSoftObjectPath
```

返回物品装备栏图标路径(带玩家皮肤)（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |
| `PlayerController` | `PlayerController` | 玩家 PlayerController |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 装备栏图标路径 |

### `GetItemDetailV2`

```text
GetItemDetailV2(ItemID: number) -> string
```

返回物品详情
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品详情 |

### `GetItemDetailV2ByDefineID`

```text
GetItemDetailV2ByDefineID(ItemDefineID: FItemDefineID) -> string
```

返回物品详情（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品详情 |

### `GetItemPickupDetailV2`

```text
GetItemPickupDetailV2(ItemID: number) -> string
```

返回物品拾取描述
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品拾取描述 |

### `GetItemPickupDetailV2ByDefineID`

```text
GetItemPickupDetailV2ByDefineID(ItemDefineID: FItemDefineID) -> string
```

返回物品拾取描述（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品拾取描述 |

### `ItemHasTagV2`

```text
ItemHasTagV2(ItemID: number, Tag: string) -> boolean
```

是否含有某个 Tag
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |
| `Tag` | `string` | 物品 Tag |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否含有 Tag |

### `GetItemTagsV2`

```text
GetItemTagsV2(ItemID: number) -> string[]
```

返回物品所有 Tag
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `string[]` | 物品所有 Tag |

### `ItemCanDropV2`

```text
ItemCanDropV2(ItemID: number) -> boolean
```

返回物品是否可丢弃
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 物品是否可丢弃 |

### `ItemCanRemoveV2`

```text
ItemCanRemoveV2(ItemID: number) -> boolean
```

返回物品是否可销毁
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 物品是否可销毁 |

### `IsCanUseV2`

```text
IsCanUseV2(ItemID: number) -> boolean
```

返回物品在背包中是否可以使用
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否可以使用 |

### `GetItemMaxNumberOfStacksV2`

```text
GetItemMaxNumberOfStacksV2(ItemID: number) -> number
```

返回物品最大堆叠数量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品最大堆叠数量 |

### `GetItemQualityV2`

```text
GetItemQualityV2(ItemID: number) -> number
```

返回物品品质
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品品质 |

### `GetItemQualityV2ByDefineID`

```text
GetItemQualityV2ByDefineID(ItemDefineID: FItemDefineID) -> number
```

返回物品品质（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品品质 |

### `GetItemCustomizedTypeV2`

```text
GetItemCustomizedTypeV2(ItemID: number) -> string
```

返回物品自定义类型
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品自定义类型 |

### `LoadItemCustomData`

```text
LoadItemCustomData(ItemDefineID: FItemDefineID) -> table
```

获取物品自定义实例化数据
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品DefineID |

**Returns**

| Type | Description |
|---|---|
| `table` | 物品自定义实例化数据table |

### `SaveItemCustomData`

```text
SaveItemCustomData(ItemDefineID: FItemDefineID, ItemCustomData: table) -> boolean
```

保存物品自定义实例化数据
注意: 实例数据也包含了和平内置数据，应避免直接覆盖，采用下述方式添加数据
local CustomData = UGCItemSystemV2.LoadItemCustomData(ItemDefineID)
CustomData.NewKey = NewTableData -- 填充新的数据
UGCItemSystemV2.SaveItemCustomData(ItemDefineID, CustomData)
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品DefineID |
| `ItemCustomData` | `table` | 物品自定义实例化数据table |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 保存成功or失败 |

### `GetItemDefineID`

```text
GetItemDefineID(ItemID: number) -> FItemDefineID
```

通过物品ID创建一个全新的物品实例，并返回 DefineID
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `FItemDefineID` | 物品 DefineID |

### `SetItemCommonReason`

```text
SetItemCommonReason(ItemDefineID: FItemDefineID, Reason: number)
```

设置物品通用 Reason
用于操作物品时指定其中一些行为
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |
| `Reason` | `number` | Reason |

### `GetItemCommonReason`

```text
GetItemCommonReason(ItemDefineID: FItemDefineID) -> number
```

获取物品通用 Reason
用于操作物品时指定其中一些行为
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `number` | Reason |

### `GetEquipTargetSlots`

```text
GetEquipTargetSlots(ItemID: number) -> string[]
```

获取装备物品拥有的槽位列表
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `string[]` | 物品拥有的所有槽位 |

### `GetDisplayNameBySlotName`

```text
GetDisplayNameBySlotName(ItemID: number, SlotName: string) -> string
```

获取槽位对应的展示名
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |
| `SlotName` | `string` | 槽位名 |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品槽位的展示名称 |

### `GetAttachTargetItem`

```text
GetAttachTargetItem(ItemDefineID: ItemDefineID) -> bool,ItemDefineID,FName
```

获取物品附加在哪个物品上
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `ItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `bool,ItemDefineID,FName` | 物品是否正附加在另一个物品上,物品附加的目标物品 DefineID,物品附加的目标物品槽位 |

### `GetAttachChildItem`

```text
GetAttachChildItem(AttachParentID: ItemDefineID, AttachSlot: string) -> ItemDefineID
```

获取附加在物品上的子物品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttachParentID` | `ItemDefineID` | 父物品的 DefineID |
| `AttachSlot` | `string` | 父物品的槽位名 |

**Returns**

| Type | Description |
|---|---|
| `ItemDefineID` | 附加在此槽位上的子物品 DefineID |

### `GetAttachChildrenItem`

```text
GetAttachChildrenItem(AttachParentID: ItemDefineID) -> ItemDefineID[]
```

获取所有附加在物品上的子物品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttachParentID` | `ItemDefineID` | 父物品的 DefineID |

**Returns**

| Type | Description |
|---|---|
| `ItemDefineID[]` | 所有子物品 DefineID, 数组元素与父物品槽位一一对应，可能存在无效的 ItemDefineID |

### `GetAttachAllowSlots`

```text
GetAttachAllowSlots(AttachParentID: number, AttachChildID: number) -> string[]
```

获取子物品可以 Attach 到父物品的哪些 Slot(不考虑槽位启用状态)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttachParentID` | `number` | 父物品的 ItemID |
| `AttachChildID` | `number` | 子物品的 ItemID |

**Returns**

| Type | Description |
|---|---|
| `string[]` | 所有可装备槽位 FName |

### `GetAttachAllowSlotsByDefineID`

```text
GetAttachAllowSlotsByDefineID(Player: PlayerPawn, AttachParentDefineID: ItemDefineID, AttachChildID: number) -> string[]
```

获取子物品可以 Attach 到父物品`实例` 的哪些 Slot(考虑槽位启用状态)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn` | 玩家 |
| `AttachParentDefineID` | `ItemDefineID` | 父物品的 ItemDefineID |
| `AttachChildID` | `number` | 子物品的 ItemID |

**Returns**

| Type | Description |
|---|---|
| `string[]` | 所有可装备槽位 FName |

### `GetQualityTexturePath`

```text
GetQualityTexturePath(QualityRank: number) -> string
```

获取品质色的128*128纹理路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QualityRank` | `number` | 品质等级 |

**Returns**

| Type | Description |
|---|---|
| `string` | 品质纹理路径 |

### `GetBackpackSimpleNameV2`

```text
GetBackpackSimpleNameV2(ItemID: number) -> string
```

返回物品背包简述
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品背包简写 |

### `GetBackpackSimpleNameV2ByDefineID`

```text
GetBackpackSimpleNameV2ByDefineID(ItemDefineID: FItemDefineID) -> string
```

返回物品背包简述（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品背包简写 |

### `GetBigQualityTexturePath`

```text
GetBigQualityTexturePath(QualityRank: number) -> string
```

获取品质色的128*256纹理路径(废弃，结果同GetQualityTexturePath)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QualityRank` | `number` | 品质等级 |

**Returns**

| Type | Description |
|---|---|
| `string` | 品质纹理路径string |

### `GetQualityBarTexturePath`

```text
GetQualityBarTexturePath(QualityRank: number) -> string
```

获取品质色条纹理路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QualityRank` | `number` | 品质等级 |

**Returns**

| Type | Description |
|---|---|
| `string` | 品质纹理路径string |

### `GetEquipmentQualityTexturePath`

```text
GetEquipmentQualityTexturePath(QualityRank: number) -> string
```

获取装备品质色条纹理路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QualityRank` | `number` | 品质等级 |

**Returns**

| Type | Description |
|---|---|
| `string` | 品质纹理路径string |

### `GetWeaponSlotAttachItemIDs`

```text
GetWeaponSlotAttachItemIDs(ItemID: number, SlotName: string) -> number[]
```

获取武器配件槽位可用配件的物品ID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 武器的物品ID |
| `SlotName` | `string` | 武器槽位名 |

**Returns**

| Type | Description |
|---|---|
| `number[]` | 可用的配件物品ID |

### `GetPickupWrapperListByItemID`

```text
GetPickupWrapperListByItemID(ItemID: number) -> AUGCPickUpWrapperActor[]
```

根据物品ID查询拾取物
生效范围：服务器&客户端, 客户端仅查询本地生成的

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `AUGCPickUpWrapperActor[]` | 拾取物列表 |

### `GetPickupWrapperListByCustomType`

```text
GetPickupWrapperListByCustomType(CustomType: string) -> AUGCPickUpWrapperActor[]
```

根据自定义类型查询拾取物
生效范围：服务器&客户端, 客户端仅查询本地生成的

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CustomType` | `string` | 自定义类型 |

**Returns**

| Type | Description |
|---|---|
| `AUGCPickUpWrapperActor[]` | 拾取物列表 |

### `GetPickupWrapperListByItemTag`

```text
GetPickupWrapperListByItemTag(ItemTag: string) -> AUGCPickUpWrapperActor[]
```

根据物品Tag查询拾取物
生效范围：服务器&客户端, 客户端仅查询本地生成的

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemTag` | `string` | 物品Tag |

**Returns**

| Type | Description |
|---|---|
| `AUGCPickUpWrapperActor[]` | 拾取物列表 |

### `SetEquipSlotEnable`

```text
SetEquipSlotEnable(DefineID: FItemDefineID, SlotName: string)
```

启用物品槽位
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `FItemDefineID` | 物品DefineID |
| `SlotName` | `string` | 槽位名 |

### `GetEquipSlotEnable`

```text
GetEquipSlotEnable(DefineID: FItemDefineID, SlotName: string) -> boolean
```

获取物品槽位是否启用
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `FItemDefineID` | 物品DefineID |
| `SlotName` | `string` | 槽位名 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否启用 |

### `StartCustomizeDrop`

```text
StartCustomizeDrop(DropLocation: FVector, ProduceID: number, ProduceGroupID: number, EntityType: EUGCGenerateItemEntityType, RelatedPlayer: PlayerPawn, DropActorClass: UClass)
```

指定掉落方案进行一次 Wrapper 掉落
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DropLocation` | `FVector` | 掉落中心点 |
| `ProduceID` | `number` | 掉落方案ID |
| `ProduceGroupID` | `number` | 掉落组方案ID(掉落组ID不为-1，掉落组ID生效。掉落组ID为-1,则掉落ID生效) |
| `EntityType` | `EUGCGenerateItemEntityType` | 掉落物类型(可缺省，默认为Wrapper) |
| `RelatedPlayer` | `PlayerPawn` | 当掉落物方向为面相玩家时必须，当掉落物类型为进入背包时必须，其他时候可以为nil |
| `DropActorClass` | `UClass` | 掉落主体Actor类型，应继承自 UGCDropActor_BP, 可以为nil。通过创建自定义蓝图，配置掉落详细参数（掉落间隔、随机掉落范围等等）。 |

### `FindAllNearPickupItemData`

```text
FindAllNearPickupItemData(PlayerPawn: PlayerPawn) -> FUGCPickupItemData[]
```

找到所有玩家角色附近的地面拾取物
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `FUGCPickupItemData[]` | 地面拾取物信息 |

### `FindPickupWrapperActorByRange`

```text
FindPickupWrapperActorByRange(Center: FVector, DistanceRange: number) -> APickUpWrapperActor[]
```

查找指定距离范围内的地面拾取物
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Center` | `FVector` | 中心点坐标 |
| `DistanceRange` | `number` | 查找距离 |

**Returns**

| Type | Description |
|---|---|
| `APickUpWrapperActor[]` | 地面拾取物Actor |

### `TryPickupWrapperItem`

```text
TryPickupWrapperItem(PlayerPawn: PlayerPawn, TargetWrapper: AActor, ItemDefineID: FItemDefineID, PickupCount: number, CheckPickupCondition: boolean)
```

玩家角色尝试拾取地面物品（不播拾取动作）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `TargetWrapper` | `AActor` | 目标地面拾取物 |
| `ItemDefineID` | `FItemDefineID` | 要拾取的物品 DefineID，可缺省，默认取 TargetWrapper 中的物品实例数据 |
| `PickupCount` | `number` | 拾取数量，可缺省，默认拾取1个 |
| `CheckPickupCondition` | `boolean` | 是否检查拾取条件(距离、是否穿墙等)，可缺省，默认为 true |

### `SpawnPickupWrapper`

```text
SpawnPickupWrapper(Location: FVector, ItemID: number, Count: number, CustomData: table) -> APickUpWrapperActor
```

创建地面拾取物
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Location` | `FVector` | 创建位置 |
| `ItemID` | `number` | 拾取物物品ID |
| `Count` | `number` | 拾取物物品数量 |
| `CustomData` | `table` | 物品自定义实例化数据(可缺省，默认无自定义实例化数据) |

**Returns**

| Type | Description |
|---|---|
| `APickUpWrapperActor` | 地面拾取物Actor |

### `GetUGCPickUpListComponent`

```text
GetUGCPickUpListComponent(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器) -> @UUGCPickUpListComponent
```

获取拾取组件(客户端）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `@UUGCPickUpListComponent` | UGC拾取组件组件 |

### `PauseAutoPick`

```text
PauseAutoPick(InPlayer: PlayerPawn | PlayerController | nil @可选，玩家角色或控制器，不传则自动获取)
```

暂停指定物品的自动拾取
生效范围：客户端
优先使用新拾取组件，若不存在则走经典面板逻辑

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPlayer` | `PlayerPawn \| PlayerController \| nil @可选，玩家角色或控制器，不传则自动获取` | 可选，玩家角色或控制器，不传则自动获取 |

### `StopPick`

```text
StopPick(InPlayer: PlayerPawn | PlayerController | nil @可选，玩家角色或控制器，不传则自动获取)
```

停止拾取（清空拾取列表，关闭数据更新）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPlayer` | `PlayerPawn \| PlayerController \| nil @可选，玩家角色或控制器，不传则自动获取` | 可选，玩家角色或控制器，不传则自动获取 |

### `StartPick`

```text
StartPick(InPlayer: PlayerPawn | PlayerController | nil @可选，玩家角色或控制器，不传则自动获取)
```

开始拾取（开启数据更新）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPlayer` | `PlayerPawn \| PlayerController \| nil @可选，玩家角色或控制器，不传则自动获取` | 可选，玩家角色或控制器，不传则自动获取 |

### `GetHeadDamageReduceV2`

```text
GetHeadDamageReduceV2(ItemID: number) -> number
```

返回外显装备头部减伤属性（仅支持ItemID，如需FItemDefineID请使用GetHeadDamageReduceV2ByDefineID）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 头部减伤值 |

### `GetHeadDamageReduceV2ByDefineID`

```text
GetHeadDamageReduceV2ByDefineID(ItemDefineID: FItemDefineID) -> number
```

返回外显装备头部减伤属性（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `number` | 头部减伤值 |

### `GetBodyDamageReduceV2`

```text
GetBodyDamageReduceV2(ItemID: number) -> number
```

返回外显装备身体减伤属性（仅支持ItemID，如需FItemDefineID请使用GetBodyDamageReduceV2ByDefineID）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 身体减伤值 |

### `GetBodyDamageReduceV2ByDefineID`

```text
GetBodyDamageReduceV2ByDefineID(ItemDefineID: FItemDefineID) -> number
```

返回外显装备身体减伤属性（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `number` | 身体减伤值 |

### `GetItemLevelV2`

```text
GetItemLevelV2(ItemID: number) -> number
```

返回物品等级（仅支持ItemID，如需FItemDefineID请使用GetItemLevelV2ByDefineID）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品等级 |

### `GetItemLevelV2ByDefineID`

```text
GetItemLevelV2ByDefineID(ItemDefineID: FItemDefineID) -> number
```

返回物品等级（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品等级 |

### `GetBackpackCellV2`

```text
GetBackpackCellV2(ItemID: number) -> number
```

返回物品背包格子数（仅支持ItemID，如需FItemDefineID请使用GetBackpackCellV2ByDefineID）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 背包格子数 |

### `GetBackpackCellV2ByDefineID`

```text
GetBackpackCellV2ByDefineID(ItemDefineID: FItemDefineID) -> number
```

返回物品背包格子数（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `number` | 背包格子数 |

### `GetNewDurabilityV2ByDefineID`

```text
GetNewDurabilityV2ByDefineID(ItemDefineID: FItemDefineID) -> number
```

返回物品当前耐久度（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品耐久度 |

### `GetPickupWrapperMeshPathV2`

```text
GetPickupWrapperMeshPathV2(ItemID: number) -> string
```

返回物品拾取包装体模型路径（仅支持ItemID，如需FItemDefineID请使用GetPickupWrapperMeshPathV2ByDefineID）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `string` | 拾取包装体模型路径 |

### `GetPickupWrapperMeshPathV2ByDefineID`

```text
GetPickupWrapperMeshPathV2ByDefineID(ItemDefineID: FItemDefineID) -> string
```

返回物品拾取包装体模型路径（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `string` | 拾取包装体模型路径 |

## Language

`lua`
