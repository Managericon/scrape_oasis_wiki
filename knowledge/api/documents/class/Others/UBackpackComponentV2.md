---
id: "api:class:UBackpackComponentV2"
title: "UBackpackComponentV2"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBackpackComponentV2.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBackpackComponentV2

V2背包内核组件

## Inheritance

`UCommonBackpackComponent` -> `IUGCItemContainerInterface` -> `IUGCItemEquipTargetInterface` -> `IUGCGamePartPlayerComponentInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Warehouse` | `UUGCItemWarehouse_Backpack *` | 仓库对象<br>	  基类：UUGCItemWarehouseBase |

## Functions

### `RemoveItemNewFlag`

```text
RemoveItemNewFlag(DefineID: FItemDefineID &) -> void
```

移除物品新标记
	  DS、Client 可调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `FItemDefineID &` | 物品实例ID |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableItemNewFlag`

```text
EnableItemNewFlag() -> void
```

激活物品新标记
	  DS、Client 可调用

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableItemNewFlag`

```text
DisableItemNewFlag(bForever: bool) -> void
```

失效物品新标记
	  DS、Client 可调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bForever` | `bool` | 是否永久失效 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetItemIsNew`

```text
GetItemIsNew(DefineID: FItemDefineID &) -> bool
```

获取物品是否新标记
	  Client 可调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `FItemDefineID &` | 物品实例ID |

**Returns**

| Type | Description |
|---|---|
| `bool` | 物品是否有新标记 |

### `CheckInitPersistCompleted`

```text
CheckInitPersistCompleted() -> bool
```

查询背包是否初始化完成，完成后才可以进行背包操作

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Events

### `CanAddItemV2`

```text
CanAddItemV2(ItemID: int32, Count: int32) -> int32
```

能否添加物品，能添加多少物品
	  可重载并自定义
	  DS 被调用
	  
	  能通过此事件，决定调用 AddItemV2 时，允许添加多少物品。
	  即使此事件允许添加物品，也可能因为其它限制因素导致物品添加数量减少或添加失败。
	  部分强制添加物品的情形，会跳过此事件。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `int32` | 物品ID |
| `Count` | `int32` | 需要添加的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `int32` | 允许添加的物品数量，如果等于 Count 表示允许添加所有需要的物品 |

### `CanAddItemByDefineIDV2`

```text
CanAddItemByDefineIDV2(DefineID: FItemDefineID &, Count: int32) -> int32
```

能否添加物品，能添加多少物品
	  可重载并自定义
	  DS 被调用
	  
	  能通过此事件，决定添加某个实例物品时，允许添加多少物品。
	  此接口针对具体实例，调用AddItemV2、调用AddItemByDefineIDV2、物品转移等情形都可能触发此事件。
	  单次调用 AddItemV2 可能触发多次针对不同实例的 CanAddItemByDefineIDV2 判断。
	  即使此事件允许添加物品，也可能因为其它限制因素导致物品添加数量减少或添加失败。
	  部分强制添加物品的情形，会跳过此事件。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `FItemDefineID &` | - |
| `Count` | `int32` | 需要添加的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `int32` | 允许添加的物品数量，如果等于 Count 表示允许添加所有需要的物品 |

### `OnAddItemV2`

```text
OnAddItemV2(ItemDefineID: FItemDefineID &, Count: int32) -> void
```

当添加物品实例后回调
	  可重载并自定义
	  DS 被调用
	  
	  当物品实例被成功添加时触发此事件。
	  单次 AddItemV2 可能触发多次针对不同实例的 OnAddItem 调用（生成多个堆叠的情况）。
	  如果物品触发了自动装备，可能装备相关事件会先于 OnAddItemV2 被触发。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID |
| `Count` | `int32` | 已添加的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanMergeItemV2`

```text
CanMergeItemV2(ItemDefineID: FItemDefineID &, CountNow: int32, MergeCount: int32) -> int32
```

能否合并物品(将新增的物品叠加到已有格子上)
	  可重载并自定义
	  DS 被调用
	  
	  能通过此事件，决定多少物品能堆叠到已有堆叠（ItemDefineID）上。
	  此接口针对具体实例，调用AddItemV2、调用AddItemByDefineIDV2、物品转移等情形都可能触发此事件。
	  单次 AddItemV2 可能触发多次针对不同实例的 CanMergeItem 判断（向多个堆叠合并时）。
	  即使此事件允许堆叠物品，也可能因为其它限制因素导致物品堆叠数量减少或堆叠失败。
	  部分情形下会跳过此事件。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID |
| `CountNow` | `int32` | 当前实例的物品数量 |
| `MergeCount` | `int32` | 即将合并到此实例，新增的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `int32` | 允许合并到格子的物品数量，如果等于 Count 表示允许合并所有需要的物品 |

### `OnMergeItemV2`

```text
OnMergeItemV2(ItemDefineID: FItemDefineID &, OldCount: int32, MergeCount: int32) -> void
```

当合并物品后回调(将新增的物品叠加到已有格子上)
	  可重载并自定义
	  DS 被调用
	  
	  此接口针对具体实例，调用AddItemV2、调用AddItemByDefineIDV2、物品转移等情形都可能触发此事件。
	  单次 AddItemV2 可能触发多次针对不同实例的 OnMergeItemV2 事件（向多个堆叠合并时）。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID |
| `OldCount` | `int32` | 合并前的物品数量 |
| `MergeCount` | `int32` | 此次合并操作新增的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanRemoveItemV2`

```text
CanRemoveItemV2(ItemDefineID: FItemDefineID &, Count: int32) -> int32
```

能否移除物品，能移除多少物品
	  可重载并自定义
	  DS、Client 被调用
	  
	  能通过此事件，决定多少物品能被移除。
	  此接口针对具体实例，调用RemoveItemV2、调用RemoveItemByDefineIDV2、物品转移等情形都可能触发此事件。
	  单次 RemoveItemV2 可能触发多次针对不同实例的 CanRemoveItemV2 判断（单个堆叠数量不足时）。
	  即使此事件允许移除物品，也可能因为其它限制因素导致移除数量减少或移除失败。
	  部分情形下会跳过此事件。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID |
| `Count` | `int32` | 需要移除的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `int32` | 允许移除的物品数量，如果等于 Count 表示允许移除所有需要的物品 |

### `OnRemoveItemV2`

```text
OnRemoveItemV2(ItemDefineID: FItemDefineID &, Count: int32) -> void
```

当移除物品后回调
	  可重载并自定义
	  DS 被调用
	  
	  此接口针对具体实例，调用RemoveItemV2、调用RemoveItemByDefineIDV2、物品转移等情形都可能触发此事件。
	  单次 RemoveItemV2 可能触发多次针对不同实例的 OnRemoveItemV2 事件（单个堆叠数量不足时）。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID，移除后可能已不存在于背包 |
| `Count` | `int32` | 已移除的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanDropItemV2`

```text
CanDropItemV2(ItemDefineID: FItemDefineID &, Count: int32) -> int32
```

能否丢弃物品，能丢弃多少物品
	  可重载并自定义
	  DS、Client 被调用
	  
	  能通过此事件，决定多少物品能被丢弃。
	  此接口针对具体实例，调用DropItemV2、调用DropItemByDefineIDV2等情形都可能触发此事件。
	  单次 调用 DropItemV2 可能触发多次针对不同实例的 CanDropItemV2 判断（单个堆叠数量不足时）。
	  即使此事件允许丢弃物品，也可能因为其它限制因素导致丢弃数量减少或丢弃失败。
	  部分情形下会跳过此事件。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID |
| `Count` | `int32` | 需要丢弃的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `int32` | 允许丢弃的物品数量，如果等于 Count 表示允许丢弃所有需要的物品 |

### `OnDropItemV2`

```text
OnDropItemV2(ItemDefineID: FItemDefineID &, Count: int32) -> void
```

当丢弃物品后回调
	  可重载并自定义
	  DS 被调用
	  
	  当物品被成功丢弃时，触发此事件。
	  此接口针对具体实例，调用DropItemV2、调用DropItemByDefineIDV2等情形都可能触发此事件。
	  单次 DropItemV2 可能触发多次针对不同实例的 OnDropItemV2 事件（单个堆叠数量不足时）。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID，丢弃后可能已不存在于背包 |
| `Count` | `int32` | 已丢弃的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanUseItemV2`

```text
CanUseItemV2(ItemDefineID: FItemDefineID &) -> bool
```

能否使用物品
	  可重载并自定义
	  DS、Client 被调用
	  
	  DS 触发使用物品时，会触发并判断能否使用。
	  即使此事件允许使用物品，也可能因为其它限制因素导致使用失败。
	  部分情形下会跳过此事件。
	  
	  Client 背包UI选中物品时，会触发并判断是否显示使用按钮。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID |

**Returns**

| Type | Description |
|---|---|
| `bool` | 物品是否能够被使用 |

### `OnUseItemV2`

```text
OnUseItemV2(ItemDefineID: FItemDefineID &) -> void
```

当物品触发使用后回调
	  可重载并自定义
	  DS 被调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnDisuseItemV2`

```text
OnDisuseItemV2(ItemDefineID: FItemDefineID &) -> void
```

当物品触发 DisUseItem 完成后回调
	  可重载并自定义
	  DS 被调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanAttachToSlot_Implementation`

```text
CanAttachToSlot_Implementation(SlotName: FName &, ItemDefineID: FItemDefineID &) -> bool
```

其它物品是否能装备到此槽位
	  当物品尝试装备在背包槽位时触发
	  
	  DS 被调用
	  
	  开发者能通过此事件，决定调用 EquipItemV2 时，是否允许装备。
	  即使此事件允许装备物品，也可能因为其它限制因素导致物品装备失败。
	  部分强制装备物品的情形，会跳过此事件。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotName` | `FName &` | 槽位名称 |
| `ItemDefineID` | `FItemDefineID &` | 即将装备在此槽位的物品 |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `OnAttachToSlot_Implementation`

```text
OnAttachToSlot_Implementation(SlotName: FName &, ItemDefineID: FItemDefineID &) -> void
```

当其它物品装备到此槽位
	  当物品成功装备在背包槽位时触发
	  
	  DS 被调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotName` | `FName &` | 槽位名称 |
| `ItemDefineID` | `FItemDefineID &` | 已装备在此槽位的物品 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnDetachBySlot_Implementation`

```text
OnDetachBySlot_Implementation(SlotName: FName &, ItemDefineID: FItemDefineID &) -> void
```

当物品成功从背包槽位卸下时触发
	  
	  DS 被调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotName` | `FName &` | 槽位名称 |
| `ItemDefineID` | `FItemDefineID &` | 已从此槽位卸下的物品 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanAutoEquip`

```text
CanAutoEquip(ItemDefineID: FItemDefineID &) -> bool
```

物品能否自动装备
	  当配置了自动装备的物品尝试自动装备时触发
	 
	  DS 被调用
	 
	  开发者能通过此事件，阻止物品自动装备到背包或Attach到其它物品上。
	  手动装备或主动调用装备时，不受此函数影响。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 即将装备在此槽位的物品 |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `HandleExceedCellCapacity`

```text
HandleExceedCellCapacity(ItemDefineID: FItemDefineID &, Count: int32) -> void
```

处理超过格子容量的物品
	  普通情况下，背包内容量已满时，无法添加物品。
	  但存在特殊情况，背包满容量时依然成功添加物品、原本不占格子的物品变为占用格子、背包容量发生变化。
	  超容量物品会被直接移除，移除后在此函数处理保底逻辑
	  默认保底逻辑为丢弃到地上
	  重写此事件时，请不要将超容量物品在此处重新添加到背包里
	  
	  可重载并自定义
	  DS 被调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 超过容量的物品ID |
| `Count` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnCellCapacityChange`

```text
OnCellCapacityChange(NewCapacity: const int32&) -> void
```

当背包格子容量改变时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewCapacity` | `const int32&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMaxCellCapacityChange`

```text
OnMaxCellCapacityChange(NewCapacity: const int32&) -> void
```

当背包格子容量上限改变时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewCapacity` | `const int32&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWarehouseCellCapacityChange`

```text
OnWarehouseCellCapacityChange(NewCapacity: const int32&) -> void
```

当仓库格子容量改变时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewCapacity` | `const int32&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemUsingStateDelegateV2`

```text
ItemUsingStateDelegateV2(ItemDefineID: FItemDefineID, bUse: bool) -> void
```

背包物品使用状态变化时广播
	  广播范围: 服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品DefefineID |
| `bUse` | `bool` | true:开始使用,false:停止使用 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemChangeDelegateV2`

```text
ItemChangeDelegateV2(ChangeType: const EUGCItemChangeType&, DefineID: const FItemDefineID&) -> void
```

当物品实例数据发生改变时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ChangeType` | `const EUGCItemChangeType&` | - |
| `DefineID` | `const FItemDefineID&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemAddDelegateV2`

```text
ItemAddDelegateV2(DefineID: const FItemDefineID&) -> void
```

当新增物品实例时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `const FItemDefineID&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemUpdateDelegateV2`

```text
ItemUpdateDelegateV2(DefineID: const FItemDefineID&) -> void
```

当物品实例数据更新时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `const FItemDefineID&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemRemoveDelegateV2`

```text
ItemRemoveDelegateV2(DefineID: const FItemDefineID&) -> void
```

当移除物品实例时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `const FItemDefineID&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemInstanceDataChangeV2`

```text
ItemInstanceDataChangeV2() -> void
```

当背包物品实例化数据发生改变时广播
	  广播范围：客户端

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemAttachParentChangeDelegateV2`

```text
ItemAttachParentChangeDelegateV2(ItemDefineID: const FItemDefineID&, OldAttachItem: const FItemDefineID&, OldAttachSlotName: const FName&, NewAttachItem: const FItemDefineID&, NewAttachSlotName: const FName&) -> void
```

当物品附加的Parent发生改变时广播
	  广播范围：服务端 & 客户端
	  
	  ItemDefineID: 哪个物品的 Parent 发生了改变
	  OldAttachItem: 改变之前物品的 Parent
	  OldAttachSlotName: 改变之前物品所在的槽位
	  NewAttachItem: 改变之后物品的 Parent
	  NewAttachSlotName: 改变之后物品所在的槽位
	  如果物品是直接装备在背包上，AttachItem 将为空物品 ( TypeSpecificID 为 0 ) ，AttachSlotName 为背包槽位名称。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `const FItemDefineID&` | - |
| `OldAttachItem` | `const FItemDefineID&` | - |
| `OldAttachSlotName` | `const FName&` | - |
| `NewAttachItem` | `const FItemDefineID&` | - |
| `NewAttachSlotName` | `const FName&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemOperationInfoDelegateV2`

```text
ItemOperationInfoDelegateV2(ItemOperationInfo: FItemOperationInfoV2 const&) -> void
```

当对物品操作成功后广播
	  广播范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemOperationInfo` | `FItemOperationInfoV2 const&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
