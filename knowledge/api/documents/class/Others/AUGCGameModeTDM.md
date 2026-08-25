---
id: "api:class:AUGCGameModeTDM"
title: "AUGCGameModeTDM"
source: "https://developer.gp.qq.com/api/class/detail/Others/AUGCGameModeTDM.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AUGCGameModeTDM

团竞游戏模式类

## Inheritance

`ABRGameModeTeam_DeathMatch` -> `IUGCGetDynamicConfigInterface`

## Events

### `UGC_PlayerPreLoadingEvent`

```text
UGC_PlayerPreLoadingEvent(UID: int64, PlayerKey: int64, TeamID: int32) -> void
```

玩家预加载事件，此时玩家还在Loading中，尚未触发PostLogin，PlayerController尚未创建。	
	  生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `int64` | UID |
| `PlayerKey` | `int64` | PlayerKey |
| `TeamID` | `int32` | 队伍ID |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_PlayerLoginEvent`

```text
UGC_PlayerLoginEvent(PlayerController: APlayerController *) -> void
```

玩家Loading结束，进入游戏，PlayerController创建完毕，且数据初始化完成。	
	  生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `APlayerController *` | 玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_PlayerExitEvent`

```text
UGC_PlayerExitEvent(PlayerController: APlayerController *) -> void
```

玩家离开，PlayerController，PlayerPawn，PlayerState等玩家信息即将销毁。
	  生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `APlayerController *` | 玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_PlayerKilledEvent`

```text
UGC_PlayerKilledEvent(Killer: AController *, VictimPlayer: AController *, VictimPawn: APawn *, DamageType: EDamageType :: DamageType) -> void
```

玩家被淘汰事件。
	  生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Killer` | `AController *` | 淘汰对方的玩家 |
| `VictimPlayer` | `AController *` | 被淘汰玩家 |
| `VictimPawn` | `APawn *` | 被淘汰玩家Pawn |
| `DamageType` | `EDamageType :: DamageType` | 伤害类型 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_PlayerRespawnEvent`

```text
UGC_PlayerRespawnEvent(RespawnedController: AController *) -> void
```

玩家复活事件。
	  生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RespawnedController` | `AController *` | 被复活的Controller |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_SpawnedAIEvent`

```text
UGC_SpawnedAIEvent(NewAIController: AAIController *) -> void
```

AI创建事件，此时AIController创建完毕，且数据初始化完成。
	  生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAIController` | `AAIController *` | 新创建的AIController |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_PlayerPickUpEvent`

```text
UGC_PlayerPickUpEvent(PlayerController: ASTExtraPlayerController *, Target: AActor *, ItemResId: int32, PickCount: int32) -> void
```

玩家拾取事件
	 生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `ASTExtraPlayerController *` | 玩家控制器 |
| `Target` | `AActor *` | 拾取的目标,盒子Actor或者单个掉落物 |
| `ItemResId` | `int32` | 拾取到的物品资源id |
| `PickCount` | `int32` | 拾取的数量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
