---
id: "api:class:UGCItemSystem"
title: "UGCItemSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81%E4%B8%8E%E8%83%8C%E5%8C%85/UGCItemSystem.json"
category: "API Wiki/class/和平全局接口/物品与背包"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCItemSystem

道具系统接口库

## Functions

### `GetItemType`

```text
GetItemType(ItemID: number) -> number
```

获取物品ItemType
对应表格数据：和平精英\表格\物品表中ItemType列
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品类型 |

### `GetItemSubType`

```text
GetItemSubType(ItemID: number) -> number
```

获取ItemSubType
对应表格数据：和平精英\表格\物品表中ItemSubType列
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品子类型 |

### `GetItemData`

```text
GetItemData(ItemID: number) -> FBattleItem_TabRes
```

获取道具数据
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `FBattleItem_TabRes` | 物品数据 |

### `IsUGCItem`

```text
IsUGCItem(ItemID: number) -> boolean
```

是否为绿洲物品（物资编辑器中自定义物品）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为绿洲物品 |

### `IsCanUseInBackpack`

```text
IsCanUseInBackpack(ItemID: number) -> boolean
```

返回道具在背包中是否可以使用
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否可以使用 |

### `GetPickupWrapperClassPath`

```text
GetPickupWrapperClassPath(ItemID: number) -> string
```

通过ItemID获取Wrapper路径
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `string` | Wrapper路径 |

### `SetWrapperToGround`

```text
SetWrapperToGround(WrapperActor: APickUpWrapperActor) -> boolean
```

将Wrapper设置贴在地面
Wrapper.bDropedByPlayer为True时，贴地功能生效
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WrapperActor` | `APickUpWrapperActor` | 可拾取物 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetWrapperItemID`

```text
GetWrapperItemID(WrapperActor: APickUpWrapperActor) -> number
```

获取Wrapper关联的ItemID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WrapperActor` | `APickUpWrapperActor` | 可拾取物 |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品ID |

### `ModifyWrapperItemCount`

```text
ModifyWrapperItemCount(WrapperActor: APickUpWrapperActor, Count: number) -> boolean
```

修改Wrpaaer中物品的数量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WrapperActor` | `APickUpWrapperActor` | 可拾取物 |
| `Count` | `number` | 修改后的数量 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `DoPickWrapper`

```text
DoPickWrapper(PlayerPawn: PlayerPawn, WrapperActor: APickUpWrapperActor) -> boolean
```

拾取Wrapper
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | - |
| `WrapperActor` | `APickUpWrapperActor` | 可拾取物 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `IsWrapperDropedByPlayer`

```text
IsWrapperDropedByPlayer(WrapperActor: APickUpWrapperActor) -> boolean
```

Wrapper是否是由玩家丢弃生成
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WrapperActor` | `APickUpWrapperActor` | 可拾取物 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `SetWrapperPickUpRadius`

```text
SetWrapperPickUpRadius(WrapperActor: APickUpWrapperActor, Radius: number) -> boolean
```

设置Wrapper的可拾取范围
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WrapperActor` | `APickUpWrapperActor` | 可拾取物 |
| `Radius` | `number` | 可拾取范围，单位厘米 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

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

### `GetBigQualityTexturePath`

```text
GetBigQualityTexturePath(QualityRank: number) -> string
```

获取品质色的128*256纹理路径
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

## Language

`lua`
