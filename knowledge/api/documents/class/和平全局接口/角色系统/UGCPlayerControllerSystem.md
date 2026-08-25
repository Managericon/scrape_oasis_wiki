---
id: "api:class:UGCPlayerControllerSystem"
title: "UGCPlayerControllerSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%A7%92%E8%89%B2%E7%B3%BB%E7%BB%9F/UGCPlayerControllerSystem.json"
category: "API Wiki/class/和平全局接口/角色系统"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCPlayerControllerSystem

玩家控制器系统

## Functions

### `DisableJoyStickSprint`

```text
DisableJoyStickSprint(PlayerController: PlayerController)
```

禁用摇杆触发疾跑
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |

### `EnableJoyStickSprint`

```text
EnableJoyStickSprint(PlayerController: PlayerController)
```

启用摇杆触发疾跑
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |

### `GetTeamID`

```text
GetTeamID(PlayerController: PlayerController) -> number
```

通过 PlayerController 获取 TeamID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | 玩家队伍 ID |

### `GetPlayerCharacter`

```text
GetPlayerCharacter(PlayerController: PlayerController) -> ASTExtraBaseCharacter
```

获取玩家角色
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraBaseCharacter` | 玩家角色 |

### `TeleportTo`

```text
TeleportTo(PlayerController: PlayerController, X: number, Y: number, Z: number)
```

瞬移至坐标
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |
| `X` | `number` | X坐标 |
| `Y` | `number` | Y坐标 |
| `Z` | `number` | Z坐标 |

### `SetControlRotation`

```text
SetControlRotation(PlayerController: PlayerController, NewRotation: Rotator)
```

设置控制旋转
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |
| `NewRotation` | `Rotator` | 新旋转量 可使用Rotator.New(Roll,Pitch,Yaw)创建,结构{Roll=Roll, Pitch=Pitch, Yaw=Yaw} |

### `EnableBulletTrackEffect`

```text
EnableBulletTrackEffect(PlayerController: PlayerController)
```

启用子弹尾迹特效
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |

### `NotifyBattleBeginPlay`

```text
NotifyBattleBeginPlay(PlayerController: PlayerController)
```

使玩家立刻进入游戏。首先设置PlayerController蓝图上的DelayNotifyBattleBeginPlay，设置之后在切换DS，或者进入游戏的两种情况下的loading图会延长，接着调用本接口，即可立刻跳过loading图进入游戏
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |

### `IsLocalController`

```text
IsLocalController(InController: AController) -> boolean
```

判断是否为主控端
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InController` | `AController` | Pawn |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当前端是否为主控端 |

## Language

`lua`
