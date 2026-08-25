---
id: "api:class:UGCPawnAttrSystem"
title: "UGCPawnAttrSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%A7%92%E8%89%B2%E7%B3%BB%E7%BB%9F/UGCPawnAttrSystem.json"
category: "API Wiki/class/和平全局接口/角色系统"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCPawnAttrSystem

【废弃】角色属性系统接口库

## Functions

### `SetHealth`

```text
SetHealth(PlayerPawn: PlayerPawn, Health: number)
```

【废弃】请使用 UGCAttributeSystem
设置血量(不会超过最大血量)
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `Health` | `number` | 血量 |

### `GetHealth`

```text
GetHealth(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取当前血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 血量 |

### `SetHealthMax`

```text
SetHealthMax(PlayerPawn: PlayerPawn, HealthMax: number)
```

【废弃】请使用 UGCAttributeSystem
设置血量上限（当前血量不会变化）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `HealthMax` | `number` | 最大血量 |

### `GetHealthMax`

```text
GetHealthMax(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取血量上限
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 最大血量 |

### `SetSignal`

```text
SetSignal(PlayerPawn: PlayerPawn, Signal: number)
```

【废弃】请使用 UGCAttributeSystem
设置信号值（不会超过最大值）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `Signal` | `number` | 信号值 |

### `GetSignal`

```text
GetSignal(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取信号值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 信号值 |

### `GetSignalMax`

```text
GetSignalMax(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取信号值上限
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 最大信号值 |

### `SetEnergy`

```text
SetEnergy(PlayerPawn: PlayerPawn, Energy: number)
```

【废弃】请使用 UGCAttributeSystem
设置能量值（设置的值不能超过能量值上限[默认100]）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `Energy` | `number` | 能量值 |

### `GetEnergy`

```text
GetEnergy(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取能量值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 能量值 |

### `GetEnergyMax`

```text
GetEnergyMax(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取能量值上限
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 最大能量值 |

### `SetSpeedScale`

```text
SetSpeedScale(PlayerPawn: PlayerPawn, SpeedScale: number)
```

【废弃】请使用 UGCAttributeSystem
设置移动速度总系数，影响走路、冲刺、蹲下、趴下与游泳速度
注：该接口已废弃，请改用其他各移动状态的速度修改接口
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `SpeedScale` | `number` | 移动速度总系数 |

### `GetSpeedScale`

```text
GetSpeedScale(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取移动速度总系数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 移动速度总系数 |

### `GetWalkSpeedScale`

```text
GetWalkSpeedScale(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取走路移动速度系数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 走路移动速度系数 |

### `SetWalkSpeedScale`

```text
SetWalkSpeedScale(PlayerPawn: PlayerPawn, WalkSpeedScale: number)
```

【废弃】请使用 UGCAttributeSystem
设置走路移动速度系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `WalkSpeedScale` | `number` | 走路移动速度系数 |

### `GetSprintSpeedScale`

```text
GetSprintSpeedScale(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取疾跑移动速度系数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 疾跑移动速度系数 |

### `SetSprintSpeedScale`

```text
SetSprintSpeedScale(PlayerPawn: PlayerPawn, SprintSpeedScale: number)
```

【废弃】请使用 UGCAttributeSystem
设置疾跑移动速度系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `SprintSpeedScale` | `number` | 疾跑移动速度系数 |

### `GetCrouchSpeedScale`

```text
GetCrouchSpeedScale(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取蹲下移动速度系数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 蹲下移动速度系数 |

### `SetCrouchSpeedScale`

```text
SetCrouchSpeedScale(PlayerPawn: PlayerPawn, CrouchSpeedScale: number)
```

【废弃】请使用 UGCAttributeSystem
设置蹲下移动速度系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `CrouchSpeedScale` | `number` | 蹲下移动速度系数 |

### `GetProneSpeedScale`

```text
GetProneSpeedScale(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取趴下移动速度系数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 趴下移动速度系数 |

### `SetProneSpeedScale`

```text
SetProneSpeedScale(PlayerPawn: PlayerPawn, ProneSpeedScale: number)
```

【废弃】请使用 UGCAttributeSystem
设置趴下移动速度系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `ProneSpeedScale` | `number` | 趴下移动速度系数 |

### `GetSwimSpeedScale`

```text
GetSwimSpeedScale(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取游泳移动速度系数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 游泳移动速度系数 |

### `SetSwimSpeedScale`

```text
SetSwimSpeedScale(PlayerPawn: PlayerPawn, SwimSpeedScale: number)
```

【废弃】请使用 UGCAttributeSystem
设置游泳移动速度系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `SwimSpeedScale` | `number` | 游泳移动速度系数 |

### `GetCurrentFOVTPP`

```text
GetCurrentFOVTPP(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取当前第三人称视角FOV
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 当前FOV |

### `SetCurrentFOVTPP`

```text
SetCurrentFOVTPP(PlayerPawn: PlayerPawn, CurrentFOV: number)
```

【废弃】请使用 UGCAttributeSystem
设置当前第三人称视角FOV
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `CurrentFOV` | `number` | FOV |

### `GetCanSwitchFPP`

```text
GetCanSwitchFPP(PlayerPawn: PlayerPawn) -> boolean
```

【废弃】请使用 UGCAttributeSystem
获取是否可以切换至第一人称视角
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否可切换至第一人称 |

### `SetCanSwitchFPP`

```text
SetCanSwitchFPP(PlayerPawn: PlayerPawn, CanSwitchFPP: boolean)
```

【废弃】请使用 UGCAttributeSystem
设置是否可以切换至第一人称视角
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `CanSwitchFPP` | `boolean` | 是否可切换至第一人称 |

### `GetCurrentFOVFPP`

```text
GetCurrentFOVFPP(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取当前第一人称视角FOV
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 当前第一人称FOV |

### `SetCurrentFOVFPP`

```text
SetCurrentFOVFPP(PlayerPawn: PlayerPawn, CurrentFOV_FPP: number)
```

【废弃】请使用 UGCAttributeSystem
设置当前第一人称视角FOV 
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `CurrentFOV_FPP` | `number` | FOV |

### `GetHearRadius`

```text
GetHearRadius(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取听觉半径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 半径 |

### `GetPickUpRadius`

```text
GetPickUpRadius(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取拾取半径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 半径 |

### `GetShowPlayerName`

```text
GetShowPlayerName(PlayerPawn: PlayerPawn) -> boolean
```

【废弃】请使用 UGCAttributeSystem
获取是否显示玩家名称
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 显示玩家名称 |

### `SetShowPlayerName`

```text
SetShowPlayerName(PlayerPawn: PlayerPawn, ShowPlayerName: boolean)
```

【废弃】请使用 UGCAttributeSystem
设置是否显示玩家名称
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `ShowPlayerName` | `boolean` | 显示玩家名称 |

### `GetIsAI`

```text
GetIsAI(PlayerPawn: PlayerPawn) -> boolean
```

【废弃】请使用 UGCAttributeSystem
获取是否AI
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否AI |

### `GetPlayerName`

```text
GetPlayerName(PlayerPawn: PlayerPawn) -> string
```

【废弃】请使用 UGCAttributeSystem
获取玩家名称
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `string` | 玩家名称 |

### `GetPlayerKey`

```text
GetPlayerKey(PlayerPawn: PlayerPawn) -> string
```

【废弃】请使用 UGCAttributeSystem
获取字符串玩家PlayerKey
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `string` | 玩家PlayerKey |

### `GetPlayerKeyInt64`

```text
GetPlayerKeyInt64(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取64位玩家Key
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 玩家Key |

### `GetPlayerUID`

```text
GetPlayerUID(PlayerPawn: PlayerPawn) -> string
```

【废弃】请使用 UGCAttributeSystem
获取玩家UID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `string` | 玩家 UID |

### `GetPlayerTeamIndex`

```text
GetPlayerTeamIndex(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取玩家队伍中序号（非TeamID，而是玩家在队伍中的序号）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 玩家UID |

### `GetJumpType`

```text
GetJumpType(PlayerPawn: PlayerPawn) -> ECharacterJumpType
```

【废弃】请使用 UGCAttributeSystem
获取跳跃类型
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `ECharacterJumpType` | 跳跃类型 |

### `GetJumpHeight`

```text
GetJumpHeight(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取跳跃高度
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 跳跃高度 |

### `GetJumpZVelocity`

```text
GetJumpZVelocity(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取跳跃时的初速度
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 跳跃时的初速度 |

### `SetJumpZVelocity`

```text
SetJumpZVelocity(PlayerPawn: PlayerPawn, JumpZVelocity: number)
```

【废弃】请使用 UGCAttributeSystem
设置跳跃时的初速度
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `JumpZVelocity` | `number` | 跳跃时的初速度 |

### `GetStandHalfHeight`

```text
GetStandHalfHeight(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取站立半高
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 站立半高 |

### `GetStandRadius`

```text
GetStandRadius(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取站立半径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 站立半径 |

### `GetCrouchHalfHeight`

```text
GetCrouchHalfHeight(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取蹲伏半高
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 蹲伏半高 |

### `GetProneHalfHeight`

```text
GetProneHalfHeight(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取匍匐半高
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 匍匐半高 |

### `GetTeamID`

```text
GetTeamID(PlayerPawn: PlayerPawn) -> number
```

【废弃】请使用 UGCAttributeSystem
获取TeamID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 队伍ID |

## Language

`lua`
