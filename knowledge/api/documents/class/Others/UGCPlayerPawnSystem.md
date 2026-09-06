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
ChangeAvatarMesh(PlayerPawn: PlayerPawn, SkeletalMesh: UClass|string, bIsUseBoneRetarget: boolean)
```

切换玩家角色使用的全身骨骼体
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `SkeletalMesh` | `UClass\|string` | 全身骨骼体蓝图类或路径 |
| `bIsUseBoneRetarget` | `boolean` | 是否使用骨骼重定向,默认false,外部导入的骨骼体需要设置为true |

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

### `ConfirmCarryOther`

```text
ConfirmCarryOther(InPawn: PlayerPawn, InTargetPawn: PlayerPawn) -> boolean
```

确认背负倒地队友
生效范围：服务器
前置条件：
   1. 被背负者处于倒地状态（IsHaveLastBreathStatus）
   2. 背负者未在背负他人（CarryWho == nil）
   3. 双方都允许背负/被背负（bEnableCarryOther / bEnableCarriedByOther）
   4. 不在脱离CD中
   5. 背负者与被背负者距离在检测范围内

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 背负者 |
| `InTargetPawn` | `PlayerPawn` | 被背负的倒地队友 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否调用了 RPC（不代表背负成功，需用 GetCarryState 验证） |

### `ConfirmPutDownCarried`

```text
ConfirmPutDownCarried(InPawn: PlayerPawn) -> boolean
```

确认放下被背负的队友
生效范围：服务器
前置条件：
   1. 正在背负他人（CarryWho != nil）
   2. 当前状态为 Carring

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 背负者 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否调用了 RPC |

### `InterruptCarry`

```text
InterruptCarry(InPawn: PlayerPawn, bIsCarrier: boolean) -> boolean
```

中断背负（单方面中断）
生效范围：服务器
前置条件：
   bIsCarrier=true  时：正在背负他人（CarryWho != nil）
   bIsCarrier=false 时：正在被他人背负（BeCarriedByWho != nil）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |
| `bIsCarrier` | `boolean` | 是否是背负方 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否调用了函数 |

### `BreakAwayFromCarrier`

```text
BreakAwayFromCarrier(InPawn: PlayerPawn) -> boolean
```

被背负者主动脱离
生效范围：服务器
前置条件：
   1. 正在被他人背负（BeCarriedByWho != nil）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 被背负的角色 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否调用了 RPC |

### `SetCarryOtherEnabled`

```text
SetCarryOtherEnabled(InPawn: PlayerPawn, bEnable: boolean)
```

设置是否允许背负倒地队友
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |
| `bEnable` | `boolean` | 是否允许 |

### `SetBeCarriedEnabled`

```text
SetBeCarriedEnabled(InPawn: PlayerPawn, bEnable: boolean)
```

设置是否允许被他人背负
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |
| `bEnable` | `boolean` | 是否允许 |

### `SetCarryDetectRange`

```text
SetCarryDetectRange(InPawn: PlayerPawn, Radius: number, Angle: number, Offset: number)
```

设置背负检测范围
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |
| `Radius` | `number` | 检测半径 |
| `Angle` | `number` | 扇形角度 |
| `Offset` | `number` | 检测中心前向偏移 |

### `SetBreakAwayCooldown`

```text
SetBreakAwayCooldown(InPawn: PlayerPawn, Cooldown: number)
```

设置脱离冷却时间
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |
| `Cooldown` | `number` | 冷却时间（秒，0=无CD） |

### `GetCarryState`

```text
GetCarryState(InPawn: PlayerPawn) -> ECarringState
```

获取背负状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |

**Returns**

| Type | Description |
|---|---|
| `ECarringState` | 背负状态枚举 |

### `GetCarryTarget`

```text
GetCarryTarget(InPawn: PlayerPawn) -> PlayerPawn
```

获取正在背负的目标
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |

**Returns**

| Type | Description |
|---|---|
| `PlayerPawn` | 被背负的角色，无则返回nil |

### `GetCarriedByWho`

```text
GetCarriedByWho(InPawn: PlayerPawn) -> PlayerPawn
```

获取谁在背我
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |

**Returns**

| Type | Description |
|---|---|
| `PlayerPawn` | 背负者，无则返回nil |

### `IsBeingCarried`

```text
IsBeingCarried(InPawn: PlayerPawn) -> boolean
```

是否正在被背负
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否正在被背负 |

### `IsCarryingOther`

```text
IsCarryingOther(InPawn: PlayerPawn) -> boolean
```

是否正在背负他人
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否正在背负他人 |

### `IsCarriedByAI`

```text
IsCarriedByAI(InPawn: PlayerPawn) -> boolean
```

是否被AI背负
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否被AI背负 |

### `AddOnCarryStateChanged`

```text
AddOnCarryStateChanged(InPawn: PlayerPawn, Callback: function, Context: table)
```

监听背负状态变化事件
生效范围：服务器
 bIsCarrier=true=Character是背负方，false=Character是被背负方
 LastState/NewState 为 ECarringState 枚举: None(0)=无 Waitting(1)=等待 PuttingUp(2)=搬起中 Carring(3)=背负中 PuttingDown(4)=放下中
 背负开始: LastState~=Carring → NewState=Carring
 背负结束: LastState=Carring → NewState=None (放下/脱离/自杀/中断都是这个转换)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 要监听的玩家角色 |
| `Callback` | `function` | 回调函数 function(Character, bIsCarrier, LastState, NewState) |
| `Context` | `table` | 回调绑定的 self 对象（用于 Remove 时精确匹配，回调时作为 self 参数） |

### `RemoveOnCarryStateChanged`

```text
RemoveOnCarryStateChanged(InPawn: PlayerPawn, Callback: function, Context: table)
```

取消监听背负状态变化事件
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 要取消监听的玩家角色 |
| `Callback` | `function` | 注册时传入的回调函数 |
| `Context` | `table` | 注册时传入的 self 对象 |

### `ConfirmCarryDeadBox`

```text
ConfirmCarryDeadBox(InPawn: PlayerPawn, InTargetDeadBox: PlayerTombBox) -> boolean
```

确认搬起死亡盒子
生效范围：服务器
前置条件：
   1. 目标死亡盒子有效且未被搬运
   2. 当前未在搬运其他盒子（状态为 None）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 搬运者 |
| `InTargetDeadBox` | `PlayerTombBox` | 目标死亡盒子 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否调用了 RPC（不代表搬起成功，需用 GetCarryDeadBoxState 验证） |

### `ConfirmPutDownDeadBox`

```text
ConfirmPutDownDeadBox(InPawn: PlayerPawn) -> boolean
```

确认放下正在搬运的死亡盒子
生效范围：服务器
前置条件：
   1. 正在搬运死亡盒子（状态非 None）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 搬运者 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否调用了 RPC |

### `InterruptCarryDeadBox`

```text
InterruptCarryDeadBox(InPawn: PlayerPawn) -> boolean
```

中断搬运死亡盒子
生效范围：服务器
前置条件：
   1. 正在搬运死亡盒子（状态非 None）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否调用了函数 |

### `SetCarryDeadBoxEnabled`

```text
SetCarryDeadBoxEnabled(InPawn: PlayerPawn, bEnable: boolean)
```

设置搬运死亡盒子功能开关（全局）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色（作为 WorldContext） |
| `bEnable` | `boolean` | 是否允许 |

### `SetCarryDeadBoxDetectRange`

```text
SetCarryDeadBoxDetectRange(InPawn: PlayerPawn, Radius: number, Angle: number, Offset: number)
```

设置搬运检测范围
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |
| `Radius` | `number` | 检测半径 |
| `Angle` | `number` | 扇形角度 |
| `Offset` | `number` | 检测中心前向偏移 |

### `SetCarryDeadBoxPutDownParams`

```text
SetCarryDeadBoxPutDownParams(InPawn: PlayerPawn, HalfExtent: FVector, ForwardDist: number, DownwardDist: number)
```

设置放下检测参数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |
| `HalfExtent` | `FVector` | 检测盒半边长 |
| `ForwardDist` | `number` | 前向检测距离 |
| `DownwardDist` | `number` | 向下检测距离 |

### `GetCarryDeadBoxState`

```text
GetCarryDeadBoxState(InPawn: PlayerPawn) -> ECarringState
```

获取搬运死亡盒子状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |

**Returns**

| Type | Description |
|---|---|
| `ECarringState` | 搬运状态枚举 |

### `GetCarriedDeadBox`

```text
GetCarriedDeadBox(InPawn: PlayerPawn) -> PlayerTombBox
```

获取正在搬运的死亡盒子
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |

**Returns**

| Type | Description |
|---|---|
| `PlayerTombBox` | 死亡盒子对象，无则返回nil |

### `IsCarryingDeadBox`

```text
IsCarryingDeadBox(InPawn: PlayerPawn) -> boolean
```

是否正在搬运死亡盒子
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 角色 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否正在搬运死亡盒子 |

### `AddOnCarryDeadBoxStateChanged`

```text
AddOnCarryDeadBoxStateChanged(InPawn: PlayerPawn, Callback: function, Context: table)
```

监听搬运死亡盒子状态变化事件
生效范围：服务器
 Character=角色自身（仅有搬运方，无被搬运方概念）
 LastState/NewState 为 ECarringState 枚举: None(0)=无 Waitting(1)=等待 PuttingUp(2)=搬起中 Carring(3)=搬运中 PuttingDown(4)=放下中
 搬运开始: LastState~=Carring → NewState=Carring
 搬运结束: LastState=Carring → NewState=None (放下/中断)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 要监听的玩家角色（搬运者） |
| `Callback` | `function` | 回调函数 function(Character, LastState, NewState) |
| `Context` | `table` | 回调绑定的 self 对象（用于 Remove 时精确匹配，回调时作为 self 参数） |

### `RemoveOnCarryDeadBoxStateChanged`

```text
RemoveOnCarryDeadBoxStateChanged(InPawn: PlayerPawn, Callback: function, Context: table)
```

取消监听搬运死亡盒子状态变化事件
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `PlayerPawn` | 要取消监听的玩家角色 |
| `Callback` | `function` | 注册时传入的回调函数 |
| `Context` | `table` | 注册时传入的 self 对象 |

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

### `PickUpWrapperActor`

```text
PickUpWrapperActor(PlayerPawn: PlayerPawn, TargetWrapper: AActor, ItemData: FPickUpItemData, PickupCount: number)
```

拾取地面物品
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `TargetWrapper` | `AActor` | 目标地面拾取物 |
| `ItemData` | `FPickUpItemData` | 拾取物品数据（可通过 WrapperActor:GetDataList() 获取） |
| `PickupCount` | `number` | 拾取数量 |

## Language

`lua`
