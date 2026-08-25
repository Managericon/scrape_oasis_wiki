---
id: "api:class:UBackpackComponent"
title: "UBackpackComponent"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/%E8%83%8C%E5%8C%85%E7%BB%84%E4%BB%B6%E7%B1%BB/UBackpackComponent.json"
category: "API Wiki/class/和平类事件/背包组件类"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBackpackComponent

背包组件

## Inheritance

`UActorComponent` -> `IItemContainerInterface` -> `IItemFactoryInterface` -> `ICommonBackpackInterface`

## Delegates

### `UGC_ItemOperationFailedDelegate`

```text
UGC_ItemOperationFailedDelegate(DefineID: const FItemDefineID&, OperationType: EBattleItemOperationType, OperationFailedReason: EBattleItemOperationFailedReason) -> void
```

Delegate
	  生效范围SC
	  物品操作失败时通知

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `const FItemDefineID&` | 物品DefineID |
| `OperationType` | `EBattleItemOperationType` | 操作类型 |
| `OperationFailedReason` | `EBattleItemOperationFailedReason` | 失败原因 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_ItemOperationDelegate`

```text
UGC_ItemOperationDelegate(DefineID: const FItemDefineID&, OperationType: EBattleItemOperationType, Reason: uint8) -> void
```

Delegate
	  生效范围SC
	  物品操作时通知

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `const FItemDefineID&` | 物品DefineID |
| `OperationType` | `EBattleItemOperationType` | 操作类型 |
| `Reason` | `uint8` | 操作原因 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_ItemBeforeRemovedDelegate`

```text
UGC_ItemBeforeRemovedDelegate(DefineID: const FItemDefineID&) -> void
```

Delegate
	  生效范围S
	  物品被移除前通知

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `const FItemDefineID&` | 物品DefineID |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_CapacityUpdatedDelegate`

```text
UGC_CapacityUpdatedDelegate() -> void
```

Delegate
	  生效范围SC
	  背包最大容量变化时通知

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
