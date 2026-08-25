---
id: "api:class:AUGCPickUpWrapperActor"
title: "AUGCPickUpWrapperActor"
source: "https://developer.gp.qq.com/api/class/detail/Others/AUGCPickUpWrapperActor.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AUGCPickUpWrapperActor

地面拾取物Actor

## Inheritance

`APickUpWrapperActor`

## Functions

### `OnRep_DefineID_BP`

```text
OnRep_DefineID_BP() -> void
```

拾取物DefineID更改时触发
	  生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDefineID`

```text
GetDefineID() -> FItemDefineID
```

获取拾取物物品的实例ID
	  DS & 客户端 可调用

**Returns**

| Type | Description |
|---|---|
| `FItemDefineID` | 实例ID |

### `GetItemCount`

```text
GetItemCount() -> int32
```

获取拾取物物品的物品数量
	  DS & 客户端 可调用

**Returns**

| Type | Description |
|---|---|
| `int32` | 物品数量 |

## Events

### `OnInitPickupWrapper`

```text
OnInitPickupWrapper() -> void
```

当地面拾取物初始化后回调
	  可重载并自定义
	  DS & 客户端 被调用
	 
	  能通过此事件，实现自定义的初始化逻辑

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnItemPickup`

```text
OnItemPickup(PickupCharacter: ASTExtraBaseCharacter *, PickupCount: int32, NewItemCount: int32) -> void
```

当地面拾取物被拾取后回调
	  可重载并自定义
	  DS 被调用
	 
	  能通过此事件，实现自定义的被拾取后处理逻辑

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PickupCharacter` | `ASTExtraBaseCharacter *` | 拾取物品的角色 |
| `PickupCount` | `int32` | 拾取数量 |
| `NewItemCount` | `int32` | 拾取后的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnItemCountChange`

```text
OnItemCountChange(OldItemCount: int32, NewItemCount: int32) -> void
```

当地面拾取物物品数量改变时回调(拾取物销毁时也会有回调)
	  如果是拾取导致的改变，时机略晚于 OnItemPickup
	  可重载并自定义
	  DS & 客户端 被调用
	 
	  能通过此事件，实现自定义的物品数量改变处理逻辑

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldItemCount` | `int32` | 改变前的物品数量 |
| `NewItemCount` | `int32` | 改变后的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnUnInitPickupWrapper`

```text
OnUnInitPickupWrapper() -> void
```

当地面拾取物销毁前回调
	  可重载并自定义
	  DS & 客户端 被调用
	 
	  能通过此事件，实现自定义的反初始化逻辑

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
