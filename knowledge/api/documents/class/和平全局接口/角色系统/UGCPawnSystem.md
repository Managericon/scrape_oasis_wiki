---
id: "api:class:UGCPawnSystem"
title: "UGCPawnSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%A7%92%E8%89%B2%E7%B3%BB%E7%BB%9F/UGCPawnSystem.json"
category: "API Wiki/class/和平全局接口/角色系统"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCPawnSystem

角色系统接口库（废弃，已迁移到 UGCPlayerPawnSystem）

## Functions

### `HasPawnState`

```text
HasPawnState(PlayerPawn: PlayerPawn, PawnState: EPawnState) -> bool
```

【废弃】已迁移到 UGCPlayerPawnSystem
是否在指定状态下
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `PawnState` | `EPawnState` | 角色状态 |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `AllowPawnState`

```text
AllowPawnState(PlayerPawn: PlayerPawn, PawnState: EPawnState) -> bool
```

【废弃】已迁移到 UGCPlayerPawnSystem
是否允许进入指定状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `PawnState` | `EPawnState` | 角色状态 |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SwitchPoseState`

```text
SwitchPoseState(PlayerPawn: PlayerPawn, PoseState: ESTEPoseState) -> bool
```

【废弃】已迁移到 UGCPlayerPawnSystem
切换 Pose 状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `PoseState` | `ESTEPoseState` | 角色状态 |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `EnterPawnState`

```text
EnterPawnState(PlayerPawn: PlayerPawn, PawnState: EPawnState) -> bool
```

【废弃】已迁移到 UGCPlayerPawnSystem
进入指定状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `PawnState` | `EPawnState` | 角色状态 |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `LeavePawnState`

```text
LeavePawnState(PlayerPawn: PlayerPawn, PawnState: EPawnState) -> bool
```

【废弃】已迁移到 UGCPlayerPawnSystem
离开指定状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `PawnState` | `EPawnState` | 角色状态 |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `DisabledPawnState`

```text
DisabledPawnState(PlayerPawn: PlayerPawn, PawnState: EPawnState, IsDisabled: bool)
```

【废弃】已迁移到 UGCPlayerPawnSystem
禁用指定状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `PawnState` | `EPawnState` | 角色状态 |
| `IsDisabled` | `bool` | 是否禁用 |

### `GetIsFPP`

```text
GetIsFPP(PlayerPawn: PlayerPawn) -> bool
```

【废弃】已迁移到 UGCPlayerPawnSystem
获取是否第一人称视角
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是不是 FPP 模式 |

### `SetIsFPP`

```text
SetIsFPP(PlayerPawn: PlayerPawn, IsFPP: bool, bForce: bool) -> bool
```

【废弃】已迁移到 UGCPlayerPawnSystem
设置是否第一人称视角
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `IsFPP` | `bool` | 是否第一人称 |
| `bForce` | `bool` | 强制设置人称 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 设置是否成功 |

### `GetIsTPP`

```text
GetIsTPP(PlayerPawn: PlayerPawn) -> bool
```

【废弃】已迁移到 UGCPlayerPawnSystem
获取是否第三人称视角
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否第三人称 |

### `SetIsTPP`

```text
SetIsTPP(PlayerPawn: PlayerPawn, IsTPP: bool, bForce: bool) -> bool
```

【废弃】已迁移到 UGCPlayerPawnSystem
设置是否第三人称视角
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `IsTPP` | `bool` | 是否第三人称 |
| `bForce` | `bool` | 强制设置 TPP 模式 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 设置是否成功 |

### `GetIsInvincible`

```text
GetIsInvincible(PlayerPawn: PlayerPawn) -> bool
```

【废弃】已迁移到 UGCPlayerPawnSystem
获取是否无敌
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否无敌 |

### `SetIsInvincible`

```text
SetIsInvincible(PlayerPawn: PlayerPawn, IsInvincible: bool)
```

【废弃】已迁移到 UGCPlayerPawnSystem
设置是否无敌
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `IsInvincible` | `bool` | 是否无敌 |

### `TryEnterParachuteState`

```text
TryEnterParachuteState(PlayerPawn: PlayerPawn, CheckPawnState: EPawnState[], CanOpenParachuteHeight: float, ForceOpenParachuteHeight: float, CloseParachuteHeight: float, bParachuteAvatarNotShown: bool)
```

【废弃】已迁移到 UGCPlayerPawnSystem
尝试进入跳伞状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `CheckPawnState` | `EPawnState[]` | 不允许进入跳伞的角色状态 |
| `CanOpenParachuteHeight` | `float` | 允许开伞高度 |
| `ForceOpenParachuteHeight` | `float` | 强制开伞高度 |
| `CloseParachuteHeight` | `float` | 关伞高度 |
| `bParachuteAvatarNotShown` | `bool` | 是否不显示伞包 |

### `ExitParachuteState`

```text
ExitParachuteState(PlayerPawn: PlayerPawn)
```

【废弃】已迁移到 UGCPlayerPawnSystem
退出跳伞状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

### `HideBoneByBoneName`

```text
HideBoneByBoneName(PlayerPawn: PlayerPawn, BoneName: FName, bHide: bool)
```

【废弃】已迁移到 UGCPlayerPawnSystem
根据玩家角色的骨骼名称修改骨骼的显隐性
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `BoneName` | `FName` | 骨骼名称 |
| `bHide` | `bool` | true隐藏，false显示 |

### `ChangeAvatarMesh`

```text
ChangeAvatarMesh(PlayerPawn: PlayerPawn, SkeletalMeshPath: string)
```

【废弃】已迁移到 UGCPlayerPawnSystem
切换玩家角色使用的全身骨骼体
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `SkeletalMeshPath` | `string` | 全身骨骼体路径 |

### `RecoverAvatarMesh`

```text
RecoverAvatarMesh(PlayerPawn: PlayerPawn)
```

【废弃】已迁移到 UGCPlayerPawnSystem
恢复玩家角色使用的全身骨骼体
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

### `SkipSpawnDeadTombBox`

```text
SkipSpawnDeadTombBox(PlayerPawn: PlayerPawn, bIsSkip: bool)
```

【废弃】已迁移到 UGCPlayerPawnSystem
玩家死亡取消生成盒子
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `bIsSkip` | `bool` | 玩家是否取消生成死亡盒子 |

## Language

`lua`
