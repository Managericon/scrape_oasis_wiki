---
id: "api:class:ASTExtraPlayerController"
title: "ASTExtraPlayerController"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/%E8%A7%92%E8%89%B2%E6%8E%A7%E5%88%B6%E7%B1%BB%EF%BC%88PlayerController%EF%BC%89/ASTExtraPlayerController.json"
category: "API Wiki/class/和平类事件/角色控制类（PlayerController）"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ASTExtraPlayerController

主角控制器

## Inheritance

`AUAEPlayerController` -> `IInGameReconnectingInterface` -> `IGameplayTaskOwnerInterface` -> `ISTExtraPlayerController_UGCEventInterface` -> `IGISPlayerInterface` -> `IClickActorPCInterface` -> `IGetCommonBackpackInterface` -> `IUniversalTaskOwnerInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BackpackComponent` | `UBackpackComponent *` | 背包组件 |

## Functions

### `GetPlayerCharacterSafety`

```text
GetPlayerCharacterSafety() -> ASTExtraBaseCharacter *
```

获得主角Pawn,如果正在观战,取出来是nullptr

**Returns**

| Type | Description |
|---|---|
| `ASTExtraBaseCharacter *` | 主角Pawn |

## Events

### `UGCMoveEvent`

```text
UGCMoveEvent(Axis: FVector2D) -> void
```

角色移动控制事件，需要通过接口GameSystem.SetMoveInputEventEnable开启，每次触发会执行两次该事件，分别返回X和Y值

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Axis` | `FVector2D` | 向量单位，取值范围（-1~1） |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGCLookEvent`

```text
UGCLookEvent(Rot: FVector2D) -> void
```

玩家转向控制事件，需要通过接口GameSystem.SetLookInputEventEnable开启，每次触发会执行两次该事件，分别返回X和Y值

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rot` | `FVector2D` | 向量单位，取值范围（-1~1） |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_PlayerLostConnectionEvent`

```text
UGC_PlayerLostConnectionEvent() -> void
```

玩家断线事件。

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_PlayerReconnectedEvent`

```text
UGC_PlayerReconnectedEvent(IsRecovered: bool) -> void
```

玩家重连事件。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsRecovered` | `bool` | 是否为静默重连，为false则为杀进程重连 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_InitializationCompleteEvent`

```text
UGC_InitializationCompleteEvent() -> void
```

初始化完毕
	 生效范围S

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_PickupItemEvent`

```text
UGC_PickupItemEvent(ItemID: int32, Count: int32) -> bool
```

获取道具事件，可控制当前道具是否允许获取
	 生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `int32` | 物品ID |
| `Count` | `int32` | 拾取数量 (-1表示此时数量未知) |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否允许拾取 |

### `UGC_SwitchWeaponControlEvent`

```text
UGC_SwitchWeaponControlEvent(SwitchSlot: ESurviveWeaponPropSlot) -> bool
```

切换武器控制事件，可控制当前武器是否允许切换，返回false则无法切换
	 生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SwitchSlot` | `ESurviveWeaponPropSlot` | 武器槽位 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否允许切换 |

### `UGC_StartFireControlEvent`

```text
UGC_StartFireControlEvent() -> bool
```

开火控制事件，可控制是否允许开火，返回false则无法开火
	 生效范围C

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否允许开火 |

### `UGC_ReloadControlEvent`

```text
UGC_ReloadControlEvent() -> bool
```

换弹控制事件，可控制是否允许换弹，返回false则无法换弹
	 生效范围C

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否允许开火 |

### `UGC_OpenScopeControlEvent`

```text
UGC_OpenScopeControlEvent() -> bool
```

开镜控制事件，可控制是否允许开镜，返回false则无法开镜
	 生效范围C

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否允许开镜 |

### `UGC_ThrowGrenadeEvent`

```text
UGC_ThrowGrenadeEvent() -> bool
```

投掷控制事件，可控制是否允许投掷，返回false则无法投掷
	 生效范围C

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否允许投掷 |

### `UGC_IsSpectatingEvent`

```text
UGC_IsSpectatingEvent(bIsSpec: bool) -> void
```

是否在观战事件
	 生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsSpec` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | 是否在观战 |

### `UGC_FingerMoveEvent`

```text
UGC_FingerMoveEvent(FingerIndex: ETouchIndex :: Type, Loc: FVector) -> void
```

手指移动事件
	 生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex :: Type` | - |
| `Loc` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_ReleaseScreenEvent`

```text
UGC_ReleaseScreenEvent(FingerIndex: ETouchIndex :: Type) -> void
```

松开屏幕事件
	 生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_TouchScreenEvent`

```text
UGC_TouchScreenEvent(FingerIndex: ETouchIndex :: Type, Loc: FVector) -> void
```

触摸屏幕事件
	 生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex :: Type` | - |
| `Loc` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
