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

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bPickUpWidgetEnable` | `bool` | 是否启用拾取物控件 |
| `PickUpWidgetClass` | `TSoftClassPtr < UUGCWrapperPositionWidget >` | 拾取物控件蓝图路径 |
| `PickUpWidgetLocOffset` | `FVector` | 拾取物控件位置偏移 |
| `PickUpWidgetMaxShowNum` | `int32` | 拾取物控件最大显示个数 |

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

### `TryGetBatchedMeshes`

```text
TryGetBatchedMeshes(InItemID: int32) -> bool
```

尝试用合批缓存创建并附加组件到拾取物
	  只在客户端有效（IS_CLIENT）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InItemID` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true=合批命中，已创建组件；false=未命中或关闭，走原逻辑 |

### `SubmitForCaching`

```text
SubmitForCaching(InItemID: int32, SourceActors: TArray < AActor * > &) -> bool
```

提交源 Actor 给合批缓存；请求被受理后注册替换回调。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InItemID` | `int32` | - |
| `SourceActors` | `TArray < AActor * > &` | 当前已附加到拾取物的显示用子Actor |

**Returns**

| Type | Description |
|---|---|
| `bool` | true=已提交、已去重或等待材质；false=数量不足、请求拒绝或已同步命中缓存并替换 |

### `CanShowPickUpWidget`

```text
CanShowPickUpWidget() -> bool
```

拾取物控件是否可见
	  可重载并自定义
	  客户端 被调用

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

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

### `OnBatchedMeshesReplaced`

```text
OnBatchedMeshesReplaced() -> void
```

合批结果已替换原始子Actor后回调（用于清空 Lua MeshActorList 等）
	  客户端 被调用

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
