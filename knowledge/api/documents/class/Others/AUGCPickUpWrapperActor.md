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

### `SetItemOwner`

```text
SetItemOwner(NewItemOwner: ASTExtraPlayerController *) -> void
```

设置物品所有者
	  设置后只有所有者能拾取该物品，其余玩家的拾取请求会被拒绝
	  所有者以 PlayerController 标识，所有者角色死亡重生后依然有效
	  DS 调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewItemOwner` | `ASTExtraPlayerController *` | 物品所有者，传 nullptr 清除所有者，恢复所有玩家可拾取 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetItemOwner`

```text
GetItemOwner() -> ASTExtraPlayerController *
```

获取物品所有者，未设置时返回 nullptr
	  DS & 客户端 可调用

**Returns**

| Type | Description |
|---|---|
| `ASTExtraPlayerController *` | 物品所有者 |

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

### `OpenCustomizeNetRelevantCondition`

```text
OpenCustomizeNetRelevantCondition() -> void
```

开启自定义网络相关性条件
	  DS  可调用

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CustomizeCanNetRelevantFor`

```text
CustomizeCanNetRelevantFor(RealViewer: AActor *, ViewTarget: AActor *, SrcLocation: FVector &) -> bool
```

自定义网络相关性（此Actor是否对目标玩家可见）
	  需要先调用 OpenCustomizeNetRelevantCondition 开启自定义网络相关性
	  此函数返回值只是参与网络相关性计算，如果有其它内置条件，也会影响最终网络相关性结果。
	  计算方式：Result = ResultA and ResultB and ResultC ...
	  
	  可重载并自定义
	  DS 被调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RealViewer` | `AActor *` | 该客户端的 PlayerController，标识“是谁这条连接” |
| `ViewTarget` | `AActor *` | 当前视角 Actor，通常是该玩家的 Pawn；观战时为被观战者 |
| `SrcLocation` | `FVector &` | 摄像机位置（GetPlayerViewPoint），距离判定应使用此点 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否网络相关（此Actor是否对目标玩家可见） |

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
