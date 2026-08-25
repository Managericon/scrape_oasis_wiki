---
id: "api:class:VirtualItemManager"
title: "VirtualItemManager"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/VirtualItemManager.json"
category: "API Wiki/class/和平全局接口/商业化与功能模板"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# VirtualItemManager

UGC虚拟物品全局管理器

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VirtualItemManager.OnVirtualItemNumUpdatedDelegate` | `-` | 生效范围：客户端<br>虚拟物品数量发生变化时触发 |
| `VirtualItemManager.OnItemNumUpdatedDelegate` | `-` | 生效范围：客户端<br>物品数量（包括背包物品）发生变化时触发 |
| `VirtualItemManager.AddItemResultDelegate` | `-` | 添加物品后触发<br>生效范围：客户端&&服务器<br>@param Result VirtualItemAddItemResult @添加结果 |
| `VirtualItemManager.RemoveItemResultDelegate` | `-` | 移除物品后触发<br>生效范围：客户端&&服务器<br>@param Result VirtualItemRemoveItemResult @移除结果 |
| `VirtualItemManager.TransferToBackpackResultDelegate` | `-` | 转移虚拟物品到背包时触发<br>生效范围：客户端&&服务器<br>@param Result VirtualItemTransferResult @转移结果 |
| `VirtualItemManager.TableDataReadyDelegate` | `-` | 表格配置数据加载好时触发<br>生效范围：客户端&&服务器 |

## Functions

### `AddVirtualItems`

```text
AddVirtualItems(PlayerController: UUGCPlayerController, ItemList: table, RequestMark: string) -> boolean
```

添加多种虚拟物品
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `UUGCPlayerController` | 玩家控制器 |
| `ItemList` | `table` | 物品列表，key为物品ID，value为数量 |
| `RequestMark` | `string` | 发起请求标记。会传回AddItemResultDelegate的Result中，可以省略 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否添加成功 |

### `AddVirtualItem`

```text
AddVirtualItem(PlayerController: UUGCPlayerController, ItemID: number, Num: number, RequestMark: string) -> boolean
```

添加虚拟物品 
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `UUGCPlayerController` | 玩家控制器 |
| `ItemID` | `number` | 虚拟物品ID |
| `Num` | `number` | 添加的物品数量 |
| `RequestMark` | `string` | 发起请求标记。会传回AddItemResultDelegate的Result中，可以省略 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否添加成功 |

### `RemoveVirtualItem`

```text
RemoveVirtualItem(PlayerController: UUGCPlayerController, ItemID: number, Num: number, Callback: Delegate)
```

移除虚拟物品 
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `UUGCPlayerController` | 玩家控制器 |
| `ItemID` | `number` | 虚拟物品ID |
| `Num` | `number` | 移除的物品数量 |
| `Callback` | `Delegate` | 回调，可不传参 |

### `RemoveItem`

```text
RemoveItem(PlayerController: UUGCPlayerController, ItemID: number, Num: number, Callback: Delegate|function)
```

移除虚拟物品，如果物品配置了到背包的映射，则只以背包中的数量为准
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `UUGCPlayerController` | 玩家控制器 |
| `ItemID` | `number` | 虚拟物品ID |
| `Num` | `number` | 移除的物品数量 |
| `Callback` | `Delegate\|function` | 回调，可不传参 |

### `GetVirtualItemNum`

```text
GetVirtualItemNum(ItemID: number, PlayerController: UUGCPlayerController) -> number
```

获取虚拟物品数量（不包含已转移背包的数量）
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetItemNum`

```text
GetItemNum(ItemID: number, PlayerController: UUGCPlayerController) -> number
```

获取虚拟物品数量（包括已转移到背包的物品）
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetFreeItemNum`

```text
GetFreeItemNum(ItemID: number, PlayerController: UUGCPlayerController) -> number
```

获取非绿洲币购买的物品数量
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetOasisItemNum`

```text
GetOasisItemNum(ItemID: number, PlayerController: UUGCPlayerController) -> number
```

获取绿洲币购买的物品数量
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetMappedItemNum`

```text
GetMappedItemNum(ItemID: number, PlayerController: UUGCPlayerController) -> number
```

获取已映射到背包的物品数量
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `TransferToBackpack`

```text
TransferToBackpack(PlayerController: PlayerController, ItemID: number, ItemNum: number, bPartial: boolean)
```

将虚拟物品转移到背包（需配置映射表UGCObjectMapping）
 生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |
| `ItemID` | `number` | 物品ID |
| `ItemNum` | `number` | 数量, 不传则默认全部转移 |
| `bPartial` | `boolean` | 是否在背包空间不足时部分转移, 默认false |

### `GetItemDatas`

```text
GetItemDatas() -> table
```

获取所有虚拟物品ID的信息
 生效范围：客户端&&服务器

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `GetItemData`

```text
GetItemData(ItemID: number) -> table
```

获取虚拟物品ID的信息
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `table` | 如果没有对应的值则返回nil |

### `GetClassicItemID`

```text
GetClassicItemID(ItemID: number) -> number
```

【废弃】请使用 GetMappedItemID
 获取经典物品ID
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 虚拟物品ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 如果没有对应的值则返回nil |

### `GetMappedItemID`

```text
GetMappedItemID(ItemID: number) -> number
```

获取虚拟物品ID对应的背包物品ID
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 虚拟物品ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 背包物品ID，如果没有配置虚拟物品ID到UGCObjectMapping表中，则返回nil |

### `GetReverseMappingDatas`

```text
GetReverseMappingDatas() -> table
```

获取所有经典物品ID到虚拟物品ID映射数据
 生效范围：客户端&&服务器

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `GetIsEnableMappingItem`

```text
GetIsEnableMappingItem() -> boolean
```

获取是否已启用虚拟物品到背包物品的映射
 生效范围：客户端&&服务器

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetVirtualItemID`

```text
GetVirtualItemID(ClassicItemID: number) -> number
```

获取虚拟物品ID
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ClassicItemID` | `number` | 经典物品ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 如果没有对应的值则返回nil |

### `GetOwnedVirtualItems`

```text
GetOwnedVirtualItems(PlayerController: UUGCPlayerController) -> table
```

获取所有已持有的虚拟物品
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `GetOwnedItems`

```text
GetOwnedItems(PlayerController: UUGCPlayerController) -> table
```

获取所有已持有的物品（包括已映射到背包的经典物品）
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `GetUntransferredItems`

```text
GetUntransferredItems(PlayerController: UUGCPlayerController) -> table
```

获取未转移到背包的物品
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `SetAutoTransferActive`

```text
SetAutoTransferActive(bActive: boolean)
```

设置是否开启自动转移背包
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bActive` | `boolean` | 是否开启自动转移 |

### `SetGetItemUIActive`

```text
SetGetItemUIActive(bShow: bool)
```

设置是否显示获得物品弹窗
如果在已显示弹窗后设置为不显示，则在当前所有弹窗显示结束后再生效

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bShow` | `bool` | 是否显示 |

## Language

`lua`
