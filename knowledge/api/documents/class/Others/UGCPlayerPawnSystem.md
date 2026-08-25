---
id: "api:class:UGCPlayerPawnSystem"
title: "UGCPlayerPawnSystem"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGCPlayerPawnSystem.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCPlayerPawnSystem

角色系统接口库

## Functions

### `HasPawnState`

```text
HasPawnState(PlayerPawn: PlayerPawn, PawnState: EPawnState) -> boolean
```

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
| `boolean` | - |

### `AllowPawnState`

```text
AllowPawnState(PlayerPawn: PlayerPawn, PawnState: EPawnState) -> boolean
```

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
| `boolean` | - |

### `SwitchPoseState`

```text
SwitchPoseState(PlayerPawn: PlayerPawn, PoseState: ESTEPoseState) -> boolean
```

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
| `boolean` | - |

### `EnterPawnState`

```text
EnterPawnState(PlayerPawn: PlayerPawn, PawnState: EPawnState) -> boolean
```

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
| `boolean` | - |

### `LeavePawnState`

```text
LeavePawnState(PlayerPawn: PlayerPawn, PawnState: EPawnState) -> boolean
```

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
| `boolean` | - |

### `DisabledPawnState`

```text
DisabledPawnState(PlayerPawn: PlayerPawn, PawnState: EPawnState, IsDisabled: boolean)
```

禁用指定状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `PawnState` | `EPawnState` | 角色状态 |
| `IsDisabled` | `boolean` | 是否禁用 |

### `GetIsFPP`

```text
GetIsFPP(PlayerPawn: PlayerPawn) -> boolean
```

获取是否第一人称视角
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | - |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是不是 FPP 模式 |

### `SetIsFPP`

```text
SetIsFPP(PlayerPawn: PlayerPawn, IsFPP: boolean, bForce: boolean) -> boolean
```

设置是否第一人称视角
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `IsFPP` | `boolean` | 是否第一人称 |
| `bForce` | `boolean` | 强制设置人称 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 设置是否成功 |

### `GetIsTPP`

```text
GetIsTPP(PlayerPawn: PlayerPawn) -> boolean
```

获取是否第三人称视角
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | - |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否第三人称 |

### `SetIsTPP`

```text
SetIsTPP(PlayerPawn: PlayerPawn, IsTPP: boolean, bForce: boolean) -> boolean
```

设置是否第三人称视角
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `IsTPP` | `boolean` | 是否第三人称 |
| `bForce` | `boolean` | 强制设置 TPP 模式 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 设置是否成功 |

### `GetIsInvincible`

```text
GetIsInvincible(PlayerPawn: PlayerPawn) -> boolean
```

获取是否无敌
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否无敌 |

### `SetIsInvincible`

```text
SetIsInvincible(PlayerPawn: PlayerPawn, IsInvincible: boolean)
```

设置是否无敌
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `IsInvincible` | `boolean` | 是否无敌 |

### `TryEnterParachuteState`

```text
TryEnterParachuteState(PlayerPawn: PlayerPawn, CheckPawnState: EPawnState[], CanOpenParachuteHeight: number, ForceOpenParachuteHeight: number, CloseParachuteHeight: number, bParachuteAvatarNotShown: boolean)
```

尝试进入跳伞状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `CheckPawnState` | `EPawnState[]` | 不允许进入跳伞的角色状态 |
| `CanOpenParachuteHeight` | `number` | 允许开伞高度 |
| `ForceOpenParachuteHeight` | `number` | 强制开伞高度 |
| `CloseParachuteHeight` | `number` | 关伞高度 |
| `bParachuteAvatarNotShown` | `boolean` | 是否不显示伞包 |

### `ExitParachuteState`

```text
ExitParachuteState(PlayerPawn: PlayerPawn)
```

退出跳伞状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

### `HideBoneByBoneName`

```text
HideBoneByBoneName(PlayerPawn: PlayerPawn, BoneName: string, bHide: boolean)
```

根据玩家角色的骨骼名称修改骨骼的显隐性
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `BoneName` | `string` | 骨骼名称 |
| `bHide` | `boolean` | true隐藏，false显示 |

### `SetAvatarVisibility`

```text
SetAvatarVisibility(PlayerPawn: PlayerPawn, bHide: boolean, ExcludingAvatarSlot: EAvatarSlotType[])
```

设置角色Avatar的显隐
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `bHide` | `boolean` | true显示，false隐藏 |
| `ExcludingAvatarSlot` | `EAvatarSlotType[]` | 排除的AvatarSlot类型 |

### `ChangeAvatarMesh`

```text
ChangeAvatarMesh(PlayerPawn: PlayerPawn, SkeletalMesh: UClass|string)
```

切换玩家角色使用的全身骨骼体
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `SkeletalMesh` | `UClass\|string` | 全身骨骼体蓝图类或路径 |

### `RecoverAvatarMesh`

```text
RecoverAvatarMesh(PlayerPawn: PlayerPawn)
```

恢复玩家角色使用的全身骨骼体
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

### `SkipSpawnDeadTombBox`

```text
SkipSpawnDeadTombBox(PlayerPawn: PlayerPawn, bIsSkip: boolean)
```

玩家死亡取消生成盒子
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `bIsSkip` | `boolean` | 玩家是否取消生成死亡盒子 |

### `GetPartTypeSockets`

```text
GetPartTypeSockets(Character: ACharacter) -> UPartTypeSocket[]
```

获取角色骨骼里所有的PartTypeSocket
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `ACharacter` | 角色 |

**Returns**

| Type | Description |
|---|---|
| `UPartTypeSocket[]` | PartTypeSocket列表 |

### `SetDefaultPlayerRespawnPointSelectionMethod`

```text
SetDefaultPlayerRespawnPointSelectionMethod(Method: EUGCPlayerRespawnPointSelectionMethod, RespawnMethodInfo: FVector)
```

设置玩家的默认复活方式
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Method` | `EUGCPlayerRespawnPointSelectionMethod` | 复活方式 |
| `RespawnMethodInfo` | `FVector` | 指定复活位置（仅选择复活方式为指定复活点生效） |

### `SetDefaultPlayerSpawnPointSelectionMethod`

```text
SetDefaultPlayerSpawnPointSelectionMethod(Method: EUGCPlayerSpawnPointSelectionMethod, SpawnMethodInfo: FVector|uint8, PlayerStartInfo: boolean)
```

设置玩家默认的出生方式
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Method` | `EUGCPlayerSpawnPointSelectionMethod` | 出生方式 |
| `SpawnMethodInfo` | `FVector\|uint8` | 出生点类型 |
| `PlayerStartInfo` | `boolean` | 是否随机出生点ID |

### `RespawnPlayer`

```text
RespawnPlayer(PlayerKey: number, RespawnDelayTime: number, IsDestoryAlivePawn: boolean, DestroyDelayTime: number)
```

复活单个角色
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | PlayerKey |
| `RespawnDelayTime` | `number` | 复活延时时间，默认为0 |
| `IsDestoryAlivePawn` | `boolean` | 是否销毁当前未死亡的角色 |
| `DestroyDelayTime` | `number` | 销毁未死亡角色的延时时间，默认为0.01，销毁时间不能设为零，否则角色不销毁 |

### `RespawnAllPlayers`

```text
RespawnAllPlayers(RespawnDelayTime: number, IsDestroyAlivePawn: boolean, DestroyDelayTime: number)
```

复活所有角色
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RespawnDelayTime` | `number` | 复活延时时间，默认为0 |
| `IsDestroyAlivePawn` | `boolean` | 是否销毁当前未死亡的角色 |
| `DestroyDelayTime` | `number` | 销毁未死亡角色的延时时间，默认为0 |

### `SetRescueInterruptable`

```text
SetRescueInterruptable(InPawn: PlayerPawn, bCanBeInterrupt: boolean, CanBeInterruptWhenOverRadius: number)
```

设置救援队友是否能被打断
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |
| `bCanBeInterrupt` | `boolean` | 是否能被打断 |
| `CanBeInterruptWhenOverRadius` | `number` | 施救者可以移动的范围半径(传入的bCanBeInterrupt为true时这个变量才生效) |

### `SetRescueOtherDuration`

```text
SetRescueOtherDuration(InPawn: PlayerPawn, RescueOtherDuration: number)
```

设置救援队友的时长
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |
| `RescueOtherDuration` | `number` | 救援队友的时长 |

### `SetRescuingSelfCDTime`

```text
SetRescuingSelfCDTime(InPawn: PlayerPawn, RescuingSelfCDTime: number)
```

设置自救的冷却时间
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |
| `RescuingSelfCDTime` | `number` | 救援队友的冷却时间 |

### `ConfirmRescueOther`

```text
ConfirmRescueOther(InPawn: PlayerPawn, InTargetPawn: PlayerPawn)
```

确认救援队友
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |
| `InTargetPawn` | `PlayerPawn` | 救援对象 |

### `ConfirmRescueOtherImmediately`

```text
ConfirmRescueOtherImmediately(InPawn: PlayerPawn, InTargetPawn: PlayerPawn)
```

确认救援队友并将队友立即救起
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |
| `InTargetPawn` | `PlayerPawn` | 救援对象 |

### `SetIsDirectlyDie`

```text
SetIsDirectlyDie(InPawn: PlayerPawn, bIsDirectlyDie: boolean)
```

设置玩家倒地后立即死亡
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |
| `bIsDirectlyDie` | `boolean` | 是否倒地后立即死亡 |

### `DrawOutline`

```text
DrawOutline(InPawn: PlayerPawn, bIsDrawOutline: boolean, OutlineThickness: number, OutlineColor: FLinearColor)
```

设置玩家描边
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |
| `bIsDrawOutline` | `boolean` | 是否描边 |
| `OutlineThickness` | `number` | 描边粗细 |
| `OutlineColor` | `FLinearColor` | 描边颜色 |

### `AddOcclusionHighlight`

```text
AddOcclusionHighlight(TargetCharacter: ACharacter, Causer: AActor, Type: EPEBuffOcclusionHighlightType, Color: FLinearColor) -> number
```

添加透视效果
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetCharacter` | `ACharacter` | 被透视的角色或怪 |
| `Causer` | `AActor` | 透视的发起方 |
| `Type` | `EPEBuffOcclusionHighlightType` | 透视类型(仅Causer透视/Causer及其队友透视/所有人) |
| `Color` | `FLinearColor` | 透视颜色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 透视ID，用于移除透视效果,<=0为无效值 |

### `RemoveOcclusionHighlight`

```text
RemoveOcclusionHighlight(WorldContextObject: UObject, OcclusionID: number)
```

移除透视效果
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `OcclusionID` | `number` | 透视ID，AddOcclusionHighlight函数的返回值, <=0为无效值 |

### `SetOutputBusVolume`

```text
SetOutputBusVolume(InPawn: PlayerPawn, Volume: number)
```

修改角色发出的声音音量
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |
| `Volume` | `number` | 音量大小 |

### `SetEightWayUniformSpeedEnabled`

```text
SetEightWayUniformSpeedEnabled(InPawn: PlayerPawn, Enable: boolean)
```

设置八向移动相同速度
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |
| `Enable` | `boolean` | 是否启用 |

### `SetUpSubViewTargetServer`

```text
SetUpSubViewTargetServer(InPawn: PlayerPawn, bSetUp: boolean, TargetActor: AActor, BlendTime: number)
```

设置ViewTarget
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |
| `bSetUp` | `boolean` | 是否启用 |
| `TargetActor` | `AActor` | 是否启用 |
| `BlendTime` | `number` | 缓动时间 |

## Language

`lua`
