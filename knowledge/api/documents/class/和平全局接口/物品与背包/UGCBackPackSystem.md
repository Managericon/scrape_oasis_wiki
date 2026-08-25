---
id: "api:class:UGCBackPackSystem"
title: "UGCBackPackSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81%E4%B8%8E%E8%83%8C%E5%8C%85/UGCBackPackSystem.json"
category: "API Wiki/class/和平全局接口/物品与背包"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCBackPackSystem

背包系统接口库

## Functions

### `GetBackpackComponent`

```text
GetBackpackComponent(PlayerPawn: PlayerPawn) -> UBackpackComponent
```

获取背包组件(客户端仅能获取到自己的）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `UBackpackComponent` | 背包组件 |

### `AddItem`

```text
AddItem(PlayerPawn: PlayerPawn, ItemID: number, Count: number) -> boolean
```

添加道具
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `ItemID` | `number` | 物品ID |
| `Count` | `number` | 数量 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `DropItem`

```text
DropItem(PlayerPawn: PlayerPawn, ItemID: number, Count: number, IsDestroy: boolean) -> boolean
```

掉落道具（入参为ItemID，不关心具体哪个道具）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `ItemID` | `number` | 物品ID |
| `Count` | `number` | 数量 |
| `IsDestroy` | `boolean` | 是否直接销毁，不掉落地面 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `UseItem`

```text
UseItem(PlayerPawn: PlayerPawn, ItemID: number) -> boolean
```

使用道具（入参为ItemID，不关心具体哪个道具）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `DisuseItem`

```text
DisuseItem(PlayerPawn: PlayerPawn, ItemID: number) -> boolean
```

停止使用物品（入参为ItemID，默认选择同ID第一个，仅对物资编辑器生成的绷带，饮料类物资生效）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `DropItemByInstanceID`

```text
DropItemByInstanceID(PlayerPawn: PlayerPawn, InstanceID: number, Count: number, IsDestroy: boolean) -> boolean
```

根据InstanceID（物品实例ID）掉落道具
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `InstanceID` | `number` | 物品实例ID（唯一） |
| `Count` | `number` | 数量 |
| `IsDestroy` | `boolean` | 是否直接销毁，不掉落地面 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `UseItemByInstanceID`

```text
UseItemByInstanceID(PlayerPawn: PlayerPawn, InstanceID: number) -> boolean
```

根据InstanceID（物品实例ID）使用道具
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `InstanceID` | `number` | 物品实例ID（唯一） |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `DisuseItemByInstanceID`

```text
DisuseItemByInstanceID(PlayerPawn: PlayerPawn, InstanceID: number) -> boolean
```

根据InstanceID（物品实例ID）停止使用道具（仅对物资编辑器生成的绷带，饮料类物资生效）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `InstanceID` | `number` | 物品实例ID（唯一） |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetItemCount`

```text
GetItemCount(PlayerPawn: PlayerPawn, ItemID: number) -> number
```

获取道具数量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 背包内物品数量 |

### `GetAllItemData`

```text
GetAllItemData(PlayerPawn: PlayerPawn) -> @LuaTable<ItemData>,
```

获取背包里所有道具数据
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `@LuaTable,` | ItemData结构：ItemID,InstanceID,Count,Type,SubType,IsAvatar |

### `GetAllItemDataByItemID`

```text
GetAllItemDataByItemID(PlayerPawn: PlayerPawn, ItemID: number) -> table
```

获取ItemData列表
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `table` | LuaTable |

### `GetItemDataByInstanceID`

```text
GetItemDataByInstanceID(PlayerPawn: PlayerPawn, InstanceID: number) -> FBattleItemData
```

根据InstanceID（物品实例ID）获取ItemData
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `InstanceID` | `number` | 物品实例ID（唯一） |

**Returns**

| Type | Description |
|---|---|
| `FBattleItemData` | 战斗物品数据 |

### `GetCapacity`

```text
GetCapacity(PlayerPawn: PlayerPawn) -> number
```

获取背包剩余容量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 剩余容量 |

### `GetMaxCapacity`

```text
GetMaxCapacity(PlayerPawn: PlayerPawn) -> number
```

获取背包最大剩余容量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 最大剩余容量 |

### `HasItemBySubType`

```text
HasItemBySubType(PlayerPawn: PlayerPawn, ItemSubType: number) -> boolean
```

是否拥有某类物品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `ItemSubType` | `number` | 道具字类型 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetWeaponsInBackpack`

```text
GetWeaponsInBackpack(PlayerPawn: PlayerPawn) -> table
```

获取背包中的武器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `table` | FBattleItemData |

### `GetWeaponAttachmentsInBackpack`

```text
GetWeaponAttachmentsInBackpack(PlayerPawn: PlayerPawn) -> table
```

获取背包中的武器配件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `table` | FBattleItemData |

### `GetArmorInBackpack`

```text
GetArmorInBackpack(PlayerPawn: PlayerPawn) -> FBattleItemData
```

获取当前防弹衣
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `FBattleItemData` | 物品数据 |

### `GetHelmetInBackpack`

```text
GetHelmetInBackpack(PlayerPawn: PlayerPawn) -> FBattleItemData
```

获取当前头盔
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `FBattleItemData` | 物品数据 |

### `GetConsumablesInBackpack`

```text
GetConsumablesInBackpack(PlayerPawn: PlayerPawn) -> table
```

获取背包中的所有消耗品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `table` | FBattleItemData |

### `IsAttachItemType`

```text
IsAttachItemType(ItemID: number) -> boolean
```

通过传入物品ID判断是否拥有某类物品，例：可传入AKM的物品ID，判断是否拥有枪械
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `IsGunItemType`

```text
IsGunItemType(ItemID: number) -> boolean
```

传入物品ID判断是否为枪械
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetPickupWrapperClassPath`

```text
GetPickupWrapperClassPath(ItemID: number) -> string
```

获取PickupWrapperClass路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `string` | - |

### `GetAllAttachmentDefineIDInBackpack`

```text
GetAllAttachmentDefineIDInBackpack(PlayerPawn: PlayerPawn) -> table
```

获取背包内所有枪械配件DefineID
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `table` | AttachmentDefineID列表 LuaTable |

### `GetAllUnEquipedAttachmentDefineIDInBackpack`

```text
GetAllUnEquipedAttachmentDefineIDInBackpack(PlayerPawn: PlayerPawn) -> table
```

获取背包内所有未装备的枪械配件DefineID
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `table` | AttachmentDefineID列表 LuaTable |

## Language

`lua`
