---
id: "api:class:UGCGameSystem"
title: "UGCGameSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9F%BA%E7%A1%80%E5%8A%9F%E8%83%BD/UGCGameSystem.json"
category: "API Wiki/class/和平全局接口/基础功能"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCGameSystem

游戏通用接口库

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCGameSystemImplementation.PlayerAntiAFKData` | `-` | - |
| `UGCGameSystem._RateLimiters` | `-` | - |
| `UGCGameSystem.GameMode` | `-` | GameMode变量<br>生效范围：服务器 |
| `UGCGameSystem.GameState` | `-` | GameState变量<br>生效范围：服务器&客户端 |
| `UGCGameSystem.UGCSTExtraGMDelegatesMgr` | `-` | 全局事件代理<br>生效范围：服务器 |
| `UGCGameSystem.ApplyPlayerJoinStoppedDelegate` | `-` | 停止补充玩家时触发<br>生效范围：服务器<br>@param ApplyPlayerJoinStoppedReason EApplyPlayerJoinStoppedReason @停止补充玩家的原因 |
| `UGCGameSystem.ApplyPlayerJoinSucceededDelegate` | `-` | 通过补充玩家接口（UGCGameSystem.ApplyPlayerJoin、UGCGameSystem.ApplyPlayerJoinLimitCount），使得每一名玩家加入成功时触发<br>生效范围：服务器<br>@param UID number @玩家 UID<br>@param RemainingPlayerCountToJoin number @剩余需要加入的玩家数量 |

## Functions

### `GetAllPlayerController`

```text
GetAllPlayerController(NotIgnorePureSpectator: boolean) -> APlayerController[]
```

获取所有的 PlayerController，客户端仅能拿到自己的PlayerController
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotIgnorePureSpectator` | `boolean` | 是否包含非玩家观战者（全局观战） |

**Returns**

| Type | Description |
|---|---|
| `APlayerController[]` | - |

### `GetAllPlayerPawn`

```text
GetAllPlayerPawn() -> ASTExtraPlayerCharacter[]
```

获取所有的 PlayerPawn
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `ASTExtraPlayerCharacter[]` | - |

### `GetAllPlayerState`

```text
GetAllPlayerState(NotIgnorePureSpectator?: boolean) -> ASTExtraPlayerState[]
```

获取所有的 PlayerState，客户端仅能拿到所有队友的PlayerState
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotIgnorePureSpectator?` | `boolean` | 是否包含非玩家观战者(全局观战)，客户端不生效 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraPlayerState[]` | - |

### `GetAllPlayerKey`

```text
GetAllPlayerKey(NotIgnorePureSpectator?: boolean) -> int[]
```

获取所有的 PlayerKey，包括敌人的，该接口通过Pawn获取敌人的PlayerKey，如果敌人没有Pawn，则获取的UID不全
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotIgnorePureSpectator?` | `boolean` | 是否包含非玩家观战者(全局观战)，客户端不生效 |

**Returns**

| Type | Description |
|---|---|
| `int[]` | PlayerKey列表 |

### `GetAllUID`

```text
GetAllUID(NotIgnorePureSpectator: boolean) -> int[]
```

获取所有的 UID，包括敌人的，该接口通过Pawn获取敌人的UID，如果敌人没有Pawn，则获取的UID不全
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotIgnorePureSpectator` | `boolean` | 是否包含非玩家观战者(全局观战) |

**Returns**

| Type | Description |
|---|---|
| `int[]` | 玩家UID列表 |

### `GetPlayerKeyByPlayerController`

```text
GetPlayerKeyByPlayerController(PlayerController: ASTExtraPlayerController) -> number
```

通过PlayerController获取PlayerKey
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `ASTExtraPlayerController` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | PlayerKey，无效时返回-1 |

### `GetPlayerKeyByPlayerPawn`

```text
GetPlayerKeyByPlayerPawn(PlayerPawn: ASTExtraPlayerCharacter) -> number
```

通过PlayerPawn获取PlayerKey
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `ASTExtraPlayerCharacter` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | PlayerKey，无效时返回-1 |

### `GetPlayerKeyByPlayerState`

```text
GetPlayerKeyByPlayerState(PlayerState: ASTExtraPlayerState) -> number
```

通过PlayerState获取PlayerKey
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerState` | `ASTExtraPlayerState` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | PlayerKey，无效时返回-1 |

### `GetPlayerKeyByUID`

```text
GetPlayerKeyByUID(UID: number) -> number
```

通过 UID 获取 PlayerKey，客户端也可以获取敌人的UID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | PlayerKey，无效时返回-1 |

### `GetPlayerControllerByPlayerKey`

```text
GetPlayerControllerByPlayerKey(PlayerKey: number) -> APlayerController
```

根据 PlayerKey 获取 PlayerController
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家唯一 Key |

**Returns**

| Type | Description |
|---|---|
| `APlayerController` | 玩家 Controller |

### `GetPlayerControllerByUID`

```text
GetPlayerControllerByUID(UID: number) -> ASTExtraPlayerController
```

通过UID获取PlayerController
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家UID |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraPlayerController` | 玩家 Controller |

### `GetPlayerControllerByPlayerState`

```text
GetPlayerControllerByPlayerState(PlayerState: ASTExtraPlayerState) -> ASTExtraPlayerController
```

通过PlayerState获取PlayerController，客户端只能通过PlayerState获取当前客户端的PlayerController
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerState` | `ASTExtraPlayerState` | - |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraPlayerController` | 玩家 Controller |

### `GetPlayerControllerByPlayerPawn`

```text
GetPlayerControllerByPlayerPawn(PlayerPawn: ASTExtraPlayerCharacter) -> ASTExtraPlayerController
```

通过PlayerPawn获取PlayerController，客户端只能通过PlayerPawn获取当前客户端的PlayerController
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `ASTExtraPlayerCharacter` | - |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraPlayerController` | 玩家 Controller |

### `GetAIControllerByPlayerKey`

```text
GetAIControllerByPlayerKey(AIPlayerKey: number) -> AFakePlayerAIController
```

根据 AIPlayerKey 获取 AIController
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AIPlayerKey` | `number` | 假玩家唯一 Key |

**Returns**

| Type | Description |
|---|---|
| `AFakePlayerAIController` | 假玩家 AIController |

### `GetPlayerPawnByPlayerKey`

```text
GetPlayerPawnByPlayerKey(PlayerKey: number) -> PlayerPawn
```

根据 PlayerKey 获取 PlayerPawn（不会获取到尸体）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家唯一 Key |

**Returns**

| Type | Description |
|---|---|
| `PlayerPawn` | 玩家 Pawn |

### `GetPlayerPawnByUID`

```text
GetPlayerPawnByUID(UID: number) -> ASTExtraPlayerCharacter
```

通过UID获取PlayerPawn，客户端也可以获取敌人的Pawn
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家UID |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraPlayerCharacter` | 玩家 Pawn |

### `GetPlayerPawnByPlayerState`

```text
GetPlayerPawnByPlayerState(PlayerState: ASTExtraPlayerState) -> ASTExtraPlayerCharacter
```

通过PlayerState获取PlayerPawn
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerState` | `ASTExtraPlayerState` | - |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraPlayerCharacter` | 玩家 Pawn |

### `GetPlayerPawnByPlayerController`

```text
GetPlayerPawnByPlayerController(PlayerController: ASTExtraPlayerController) -> ASTExtraPlayerCharacter
```

通过PlayerController获取PlayerPawn
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `ASTExtraPlayerController` | - |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraPlayerCharacter` | 玩家 Pawn |

### `GetPlayerStateByPlayerKey`

```text
GetPlayerStateByPlayerKey(PlayerKey: number) -> APlayerState
```

根据 PlayerKey 获取 PlayerState，客户端只能拿到队友的PlayerState
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家唯一 Key |

**Returns**

| Type | Description |
|---|---|
| `APlayerState` | 玩家 PlayerState |

### `GetPlayerStateByPlayerPawn`

```text
GetPlayerStateByPlayerPawn(PlayerPawn: ASTExtraPlayerCharacter) -> ASTExtraPlayerState
```

通过 PlayerPawn 获取 PlayerState，客户端仅能拿到所有队友的PlayerState
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `ASTExtraPlayerCharacter` | - |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraPlayerState` | 玩家 PlayerState |

### `GetPlayerStateByUID`

```text
GetPlayerStateByUID(UID: number) -> PlayerState
```

根据 UID 获取 PlayerState，客户端仅能拿到所有队友的PlayerState
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |

**Returns**

| Type | Description |
|---|---|
| `PlayerState` | 玩家 PlayerState |

### `GetPlayerStateByPlayerController`

```text
GetPlayerStateByPlayerController(PlayerController: ASTExtraPlayerController) -> PlayerState
```

根据 PlayerController 获取 PlayerState
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `ASTExtraPlayerController` | 玩家 Controller |

**Returns**

| Type | Description |
|---|---|
| `PlayerState` | 玩家 PlayerState |

### `GetUIDByPlayerController`

```text
GetUIDByPlayerController(PlayerController: ASTExtraPlayerController) -> number
```

根据 PlayerController 获取 UID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `ASTExtraPlayerController` | 玩家 Controller |

**Returns**

| Type | Description |
|---|---|
| `number` | 玩家 UID |

### `GetUIDByPlayerState`

```text
GetUIDByPlayerState(PlayerState: PlayerState) -> number
```

根据 PlayerState 获取 UID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerState` | `PlayerState` | 玩家 PlayerState |

**Returns**

| Type | Description |
|---|---|
| `number` | 玩家 UID |

### `GetUIDByPlayerPawn`

```text
GetUIDByPlayerPawn(PlayerPawn: ASTExtraPlayerCharacter) -> number
```

根据 PlayerPawn 获取 UID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `ASTExtraPlayerCharacter` | 玩家 PlayerPawn |

**Returns**

| Type | Description |
|---|---|
| `number` | 玩家 UID |

### `GetUIDByPlayerKey`

```text
GetUIDByPlayerKey(PlayerKey: number) -> string
```

根据 PlayerKey 获取 UID，通过Pawn获取敌人的UID，如果敌人Pawn死亡则获取的结果不全
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 PlayerKey |

**Returns**

| Type | Description |
|---|---|
| `string` | 玩家 UID |

### `NewObject`

```text
NewObject(Outer: UObject, Class: UClass, Name: string) -> UObject
```

创建 Object
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Outer` | `UObject` | - |
| `Class` | `UClass` | - |
| `Name` | `string` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject` | 创建的对象 |

### `SpawnActor`

```text
SpawnActor(WorldContextObject: UObject, ActorClass: UClass, Location: Vector, Rotation: Rotator, Scale3D: Vector, Owner: Actor) -> Actor
```

【废弃】请使用 UGCActorComponentUtility.SpawnActor
创建 Actor
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `ActorClass` | `UClass` | 需要使用 UE.LoadClass 加载对应 Class 再作为参数传入 |
| `Location` | `Vector` | 可使用 Vector.New(x,y,z) 创建,结构 {X=x,Y=y,Z=z} |
| `Rotation` | `Rotator` | 可使用 Rotator.New(Roll,Pitch,Yaw) 创建,结构 {Roll=Roll, Pitch=Pitch, Yaw=Yaw} |
| `Scale3D` | `Vector` | 可使用 Vector.New(x,y,z) 创建,结构 {X=x,Y=y,Z=z}，不传缩放默认为 0，建议传 {X=1,Y=1,Z=1} |
| `Owner` | `Actor` | Actor 的拥有者 |

**Returns**

| Type | Description |
|---|---|
| `Actor` | 创建的Actor |

### `GetRespawnComponent`

```text
GetRespawnComponent() -> UPlayerRespawnComponent
```

【废弃】请使用 UGCPlayerPawnSystem
获取复活组件
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `UPlayerRespawnComponent` | 复活组件 |

### `SetPlayerRespawnInfo`

```text
SetPlayerRespawnInfo(PlayerKey: number, IsUseRespawnLocation: boolean, RespawnLocation: FTransform)
```

【废弃】请使用 UGCPlayerPawnSystem
设置复活信息
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | PlayerKey |
| `IsUseRespawnLocation` | `boolean` | 是否使用复活点 是：复活点复活 否：出生点复活 |
| `RespawnLocation` | `FTransform` | 复活点位置 |

### `RespawnPlayer`

```text
RespawnPlayer(PlayerKey: number)
```

【废弃】复活单个角色
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | PlayerKey |

### `RespawnAllPlayers`

```text
RespawnAllPlayers()
```

【废弃】请使用 UGCPlayerPawnSystem
复活所有角色
生效范围：服务器

### `GetPlayerNum`

```text
GetPlayerNum(IsIgnoreAI: boolean) -> number
```

获取玩家数量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsIgnoreAI` | `boolean` | 是否忽略 AI |

**Returns**

| Type | Description |
|---|---|
| `number` | 玩家数量 |

### `GetControllerByPawn`

```text
GetControllerByPawn(PlayerPawn: APawn) -> AController
```

获取角色 Controller，包括 AI
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `APawn` | - |

**Returns**

| Type | Description |
|---|---|
| `AController` | - |

### `ApplyRadialDamageWhiteList`

```text
ApplyRadialDamageWhiteList(BaseDamage: number, MinimumDamage: number, Origin: Vector, DamageInnerRadius: number, DamageOuterRadius: number, DamageFalloff: number, DamageTypeTags: FGameplayTag[], GivenActors: Actor[], DamageCauser: Actor, InstigatedByController: Controller, DamagePreventionChannel: ECollisionChannel, ItemID: number) -> boolean
```

造成爆炸类伤害，指定列表内 Actor 接受伤害
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BaseDamage` | `number` | 伤害值（最大） |
| `MinimumDamage` | `number` | 最小伤害 |
| `Origin` | `Vector` | 伤害中心 |
| `DamageInnerRadius` | `number` | 伤害内圈范围（受到最大伤害) |
| `DamageOuterRadius` | `number` | 伤害外圈范围（伤害持续衰减） |
| `DamageFalloff` | `number` | 内圈至外圈伤害衰减指数 |
| `DamageTypeTags` | `FGameplayTag[]` | 造成伤害的自定义类型列表 |
| `GivenActors` | `Actor[]` | 指定受伤害的 Actor 列表 |
| `DamageCauser` | `Actor` | 造成伤害的人/物体 |
| `InstigatedByController` | `Controller` | 煽动者的玩家控制器 |
| `DamagePreventionChannel` | `ECollisionChannel` | 伤害可见性阻挡通道 |
| `ItemID` | `number` | 造成伤害的物品 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否造成伤害 |

### `ApplyRadialDamage`

```text
ApplyRadialDamage(BaseDamage: number, MinimumDamage: number, Origin: Vector, DamageInnerRadius: number, DamageOuterRadius: number, DamageFalloff: number, DamageTypeTags: FGameplayTag[], IgnoreActors: Actor[], DamageCauser: Actor, InstigatedByController: Controller, DamagePreventionChannel: ECollisionChannel, ItemID: number) -> boolean
```

造成爆炸伤害
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BaseDamage` | `number` | 伤害值（最大） |
| `MinimumDamage` | `number` | 最小伤害 |
| `Origin` | `Vector` | 伤害中心 |
| `DamageInnerRadius` | `number` | 伤害内圈范围（受到最大伤害) |
| `DamageOuterRadius` | `number` | 伤害外圈范围（伤害持续衰减） |
| `DamageFalloff` | `number` | 内圈至外圈伤害衰减指数 |
| `DamageTypeTags` | `FGameplayTag[]` | 造成伤害的自定义类型列表 |
| `IgnoreActors` | `Actor[]` | 伤害忽略 Actor 列表 |
| `DamageCauser` | `Actor` | 造成伤害的人/物体 |
| `InstigatedByController` | `Controller` | 煽动者的玩家控制器 |
| `DamagePreventionChannel` | `ECollisionChannel` | 伤害可见性阻挡通道 |
| `ItemID` | `number` | 造成伤害的物品 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否造成伤害 |

### `ApplyPointDamage`

```text
ApplyPointDamage(DamagedActor: Actor, BaseDamage: number, HitFromDirection: Vector, HitInfo: FHitResult, EventInstigator: Controller, DamageCauser: Actor, DamageTypeTags: FGameplayTag[], ItemID: number) -> number
```

造成点伤害
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DamagedActor` | `Actor` | 伤害目标 |
| `BaseDamage` | `number` | 伤害值 |
| `HitFromDirection` | `Vector` | 伤害来源方向（如子弹射击方向） |
| `HitInfo` | `FHitResult` | 命中信息 |
| `EventInstigator` | `Controller` | 事件煽动者的玩家控制器 |
| `DamageCauser` | `Actor` | 造成伤害的人/物体 |
| `DamageTypeTags` | `FGameplayTag[]` | 造成伤害的自定义类型列表 |
| `ItemID` | `number` | 造成伤害的物品 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 实际伤害 |

### `ApplyAvatarPositionDamage`

```text
ApplyAvatarPositionDamage(DamagedActor: Actor, BaseDamage: number, EventInstigator: Controller, DamageCauser: Actor, AvatarDamagePosition: EAvatarDamagePosition, DamageTypeTags: FGameplayTag[]) -> number
```

造成部位伤害
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DamagedActor` | `Actor` | 伤害目标 |
| `BaseDamage` | `number` | 伤害值 |
| `EventInstigator` | `Controller` | 事件煽动者的玩家控制器 |
| `DamageCauser` | `Actor` | 造成伤害的人/物体 |
| `AvatarDamagePosition` | `EAvatarDamagePosition` | 造成伤害的部位 |
| `DamageTypeTags` | `FGameplayTag[]` | 造成伤害的自定义类型列表 |

**Returns**

| Type | Description |
|---|---|
| `number` | 实际伤害 |

### `ApplyDamage`

```text
ApplyDamage(DamagedActor: Actor, BaseDamage: number, EventInstigator: Controller, DamageCauser: Actor, DamageTypeTags: FGameplayTag[]) -> number
```

造成伤害
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DamagedActor` | `Actor` | 伤害目标 |
| `BaseDamage` | `number` | 伤害值 |
| `EventInstigator` | `Controller` | 事件煽动者的玩家控制器 |
| `DamageCauser` | `Actor` | 造成伤害的人/物体 |
| `DamageTypeTags` | `FGameplayTag[]` | 造成伤害的自定义类型列表 |

**Returns**

| Type | Description |
|---|---|
| `number` | 实际伤害 |

### `SendPlayerSettlement`

```text
SendPlayerSettlement(PlayerKey: number) -> boolean
```

【废弃】发送玩家结算（代表玩家已经完成了游戏，后台进行完成率统计，每个玩家正常结束游戏都需要发送）
最新：现已废弃，调用无效果，可以无需再调用，会在玩家退出游戏和触发 UGC请求退出DS Action 时自动发送
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 Key |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否发送成功。现在总是返回 true |

### `DisconnectClient`

```text
DisconnectClient()
```

断开客户端连接。DS关闭后，需要同步关闭客户端对服务器的长链接检测，否则玩家客户端会弹出无法连接到服务器的报错信息。
生效范围：客户端

### `OpenPlayerJoin`

```text
OpenPlayerJoin()
```

开启补充玩家（需要先开启补充玩家，发送补充玩家申请才会有效）
例：成局人数最小为 10 人，最大 20 人，匹配设置中设置 10 人，然后开启补充玩家，申请 10 人的补充名额
生效范围：服务器

### `StopPlayerJoin`

```text
StopPlayerJoin()
```

停止补充玩家（清空补充玩家申请记录）                            
生效范围：服务器

### `ApplyPlayerJoin`

```text
ApplyPlayerJoin(Count: number, TeamID: number)
```

申请补充玩家（申请数量会累加,需先调用 UGCGameSystem.OpenPlayerJoin 开启补充玩家）
例：成局人数最小为10人，最大20人，匹配设置中设置10人，然后开启补充玩家，申请10人的补充名额
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Count` | `number` | 需要补充的玩家数量 |
| `TeamID` | `number` | 队伍ID |

### `ApplyPlayerJoinLimitCount`

```text
ApplyPlayerJoinLimitCount(TeamPlayerCounts: table<int, int>)
```

申请补充玩家（申请数量会累加,需先调用 UGCGameSystem.OpenPlayerJoin 开启补充玩家）
例：成局人数最小为10人，最大20人，匹配设置中设置10人，然后开启补充玩家，申请10人的补充名额。但不会使得对局玩家的数量超过项目设置中 “小队玩家数量（TeamPlayers） * 队伍数量（NumberOfTeams）”设置的数量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamPlayerCounts` | `table` | 需要补充的玩家数量，形式如同：TeamPlayerCounts = { [TeamID1] = PlayerCount1, [TeamID2] = PlayerCount2, ... } |

### `EnterSpectating`

```text
EnterSpectating(PlayerController: PlayerController) -> number
```

进入观战，默认观战任意队友
可以通过 UGCGameSystem.ChangeAllowOBPlayerKeys 自定义可观战玩家列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 进入观战的玩家 Controller |

**Returns**

| Type | Description |
|---|---|
| `number` | 被观战的玩家的 PlayerKey |

### `LeaveSpectating`

```text
LeaveSpectating(PlayerController: PlayerController)
```

退出观战
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 退出观战的玩家 Controller |

### `ChangeAllowOBPlayerKeys`

```text
ChangeAllowOBPlayerKeys(PlayerController: PlayerController, PlayerKeyList: int32[])
```

设置可被观战玩家列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 可被观战玩家列表的 Controller |
| `PlayerKeyList` | `int32[]` | 可观战玩家列表数组 |

### `MyObserversChangeTarget`

```text
MyObserversChangeTarget(PlayerController: PlayerController)
```

让观战我的人切换别的观战目标，只有当观战对象的Pawn死亡时才生效
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 不再被观战的玩家 Controller |

### `IsEnableGM`

```text
IsEnableGM(PlayerController: PlayerController) -> boolean
```

是否开启 GM，自定义 GM 逻辑和界面可接入此开关，正式服中此开关为 false
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家 Controller |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否开启 GM |

### `IsServer`

```text
IsServer() -> boolean
```

是否为服务端
逻辑依赖 UGCGameSystem.GameState，在 GameState 初始化前的逻辑不建议调用此函数判断
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为服务端 |

### `IsDebug`

```text
IsDebug() -> boolean
```

是否在 Debug（编辑器 Debug 调试）
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为 Debug 环境 |

### `GetPlatformInfo`

```text
GetPlatformInfo() -> string
```

获取平台类型
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `string` | 共有三种平台类型："PIE", "WINRELEASE", "CLIENT" |

### `GetAllAIController`

```text
GetAllAIController() -> AFakePlayerAIController[]
```

获取所有的 AIController
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `AFakePlayerAIController[]` | 获取所有的 AIController,获取失败时将返回 nil |

### `ReturnToLobby`

```text
ReturnToLobby()
```

主动返回大厅（使用此接口返回大厅的玩家不会弹出重进战斗对话框）
生效范围：客户端

### `ChangeOBPlayer`

```text
ChangeOBPlayer(PlayerController: PlayerController, PlayerKey: number)
```

改变当前观战目标（仅限观战中使用）
例：被观战的玩家被淘汰后，需要使用此接口，切换至其他玩家进行观战
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 自己的 PlayerController |
| `PlayerKey` | `number` | 观战目标玩家 PlayerKey |

### `SendModeCustomEvent`

```text
SendModeCustomEvent(EventName: string, ...: any)
```

向模式编辑器发送自定义事件
根据自定义事件参数顺序传入,如 SendModeCustomEvent(EventName,param1,param2)
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EventName` | `string` | 事件名 |
| `...` | `any` | 自定义事件参数 |

### `GetServerTimeSec`

```text
GetServerTimeSec() -> number
```

获取当前服务器时间
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `number` | 当前服务器时间（UTC）:单位秒 |

### `SetTimer`

```text
SetTimer(Object: UObject, CallbackFunction: LuaFunction, Time: number, IsLooping: boolean) -> ULuaSingleDelegate
```

设置定时器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject` | 对象 |
| `CallbackFunction` | `LuaFunction` | Lua 回调函数 |
| `Time` | `number` | 定时时长 |
| `IsLooping` | `boolean` | 是否循环 |

**Returns**

| Type | Description |
|---|---|
| `ULuaSingleDelegate` | 定时器句柄，定时器回调 |

### `ClearTimer`

```text
ClearTimer(Object: UObject, TimerHandle: ULuaSingleDelegate)
```

移除定时器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject` | 上下文对象 |
| `TimerHandle` | `ULuaSingleDelegate` | 定时器句柄，定时器回调 |

### `SendTLog`

```text
SendTLog(Key: string, Value: string)
```

记录埋点日志
value 中多个字段建议使用_（下划线）分割
例: ItemName_NormalItem_Count_1
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `string` | 日志索引 |
| `Value` | `string` | 日志内容 |

### `SendGreyTLog`

```text
SendGreyTLog(ID: number, PlayerKey: number)
```

记录灰度埋点日志
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ID` | `number` | 灰度 ID |
| `PlayerKey` | `number` | 玩家 ID |

### `SendGameTlog`

```text
SendGameTlog(Index: number, UID: number, CustomData: table)
```

发送游戏日志
生效范围：服务器
注意：函数会先做本地参数校验和频率限制；命中拦截时会直接 return，不会真正发包。
Index 范围与 CustomData 结构规范，不符合条件会被拦截：
  · [800800, 801800]：自定义TLog，CustomData 无结构限制
  · [801801, 802800]：二级及以下货币TLog，CustomData 必须包含以下字段，否则会被拦截：
    AfterMoney(number/必填)、iMoney(number/必填)、Reason(number/必填)、SubReason(number/必填)、
    AddOrReduce(number/必填)、iMoneyType(number/必填)、CustomData(table/必填，空传{})
  · [802801, 804800]：物品流传说信息TLog，CustomData 必须包含以下字段，否则会被拦截：
    iGoodsType(number/必填)、iGoodsId(number/必填)、iGoodsName(string/必填)、iCount(number/必填)、
    AfterCount(number/必填)、Reason(number/必填)、SubReason(number/必填)、AddOrReduce(number/必填)、
    CustomData(table/必填，空传{})
拦截原因说明：
  1) Index 为 nil、非 number、或不在 [800800, 804800] 范围内
  2) UID 为 nil 或非 number
  3) CustomData 为 nil 或非 table
  4) 当 Index 属于 [801801, 802800] 或 [802801, 804800] 时，对应必填字段缺失或类型不符
  5) 触发频率限制（一分钟100次）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `number` | 日志索引，必填；具体范围与校验规则见上方说明 |
| `UID` | `number` | 玩家UID，必填；当前实现不支持传空，传 nil 或非 number 会在本地校验阶段被拦截，日志不会发出去；UID无效/错误仍可能导致上报失败 |
| `CustomData` | `table` | 自定义数据，必填 table；具体校验规则见上方说明 |

### `SendLiveStreamingTLog`

```text
SendLiveStreamingTLog(LogType: number, Id: number, Value: table)
```

发送直播日志
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LogType` | `number` | 类型 1-赛事，2-人生 |
| `Id` | `number` | 事件ID(自定义) |
| `Value` | `table` | 事件内容(自定义) |

### `SetTournamentInfo`

```text
SetTournamentInfo(PlayerKey: number, bEscaped: boolean, PersonRank: number, TeamRank: number, MatchResult: ETournamentMatchResult)
```

设置赛事信息
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家Key |
| `bEscaped` | `boolean` | 是否逃跑 |
| `PersonRank` | `number` | 个人排名 |
| `TeamRank` | `number` | 队伍排名 |
| `MatchResult` | `ETournamentMatchResult` | 胜利失败信息 |

### `SetMoveInputEventEnable`

```text
SetMoveInputEventEnable(PlayerController: PlayerController, IsEnable: boolean, IsOverride: boolean)
```

是否关闭移动输入事件
IsOverride 开启后需要在 PlayerController 重载 UGCMoveEvent(Vector2D) 事件
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |
| `IsEnable` | `boolean` | 是否关闭 |
| `IsOverride` | `boolean` | 是否重载（原移动输入会被覆盖） |

### `SetLookInputEventEnable`

```text
SetLookInputEventEnable(PlayerController: PlayerController, IsEnable: boolean, IsOverride: boolean)
```

开启/关闭旋转输入事件
IsOverride 开启后需要在 PlayerController 重载 UGCLookEvent(Vector2D) 事件
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |
| `IsEnable` | `boolean` | 是否开启 |
| `IsOverride` | `boolean` | 是否重载（原旋转输入会被覆盖） |

### `ClientPlayCameraShake`

```text
ClientPlayCameraShake(PlayerController: ASTExtraPlayerController, CameraShakeType: EPESkillCameraShakeType, ShakeScale: number, Duration: number)
```

在PlayerController对应的客户端震屏
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `ASTExtraPlayerController` | 震屏玩家的 PlayerController |
| `CameraShakeType` | `EPESkillCameraShakeType` | 震屏类型(随机方向/X方向/Y方向) |
| `ShakeScale` | `number` | 震屏强度 |
| `Duration` | `number` | 震屏时间(单位:秒，<=0 表示一直持续) |

### `ClientStopCameraShake`

```text
ClientStopCameraShake(PlayerController: ASTExtraPlayerController, CameraShakeType: EPESkillCameraShakeType)
```

在PlayerController对应的客户端停止某类型的震屏
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `ASTExtraPlayerController` | 震屏玩家的 PlayerController |
| `CameraShakeType` | `EPESkillCameraShakeType` | 震屏类型(随机方向/X方向/Y方向) |

### `GetTableData`

```text
GetTableData(TablePath: string) -> any
```

根据表格路径获取表格内容
TablePath支持以下格式(...表示相对Asset目录的路径, 如Data/Table)：
.../TableName
UGCGameSystem.GetUGCResourcesFullPath('Asset/.../TableName.TableName')
/Game/.../TableName.TableName
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TablePath` | `string` | 表格路径 |

**Returns**

| Type | Description |
|---|---|
| `any` | 表格全部内容 |

### `GetTableCount`

```text
GetTableCount(TablePath: string) -> number
```

根据表格路径获取表格行数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TablePath` | `string` | 表格路径，支持格式见UGCGameSystem.GetTableData |

**Returns**

| Type | Description |
|---|---|
| `number` | 表格行数 |

### `GetTableDataByRowName`

```text
GetTableDataByRowName(TablePath: string, RowName: number) -> any
```

根据表格路径，以及key获取表格内容
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TablePath` | `string` | 表格路径，支持格式见UGCGameSystem.GetTableData |
| `RowName` | `number` | key值 string型或者int型都可以 |

**Returns**

| Type | Description |
|---|---|
| `any` | 表格某行内容 |

### `GetDataTableData`

```text
GetDataTableData(DataTable: UDataTable) -> any
```

获取指定DataTable的表格内容
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DataTable` | `UDataTable` | 要读取的表格 |

**Returns**

| Type | Description |
|---|---|
| `any` | 表格全部内容 |

### `GetDataTableDataByRowName`

```text
GetDataTableDataByRowName(DataTable: UDataTable, RowName: string) -> any
```

获取指定DataTable的指定行的表格内容
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DataTable` | `UDataTable` | 要读取的表格 |
| `RowName` | `string` | 行名 |

**Returns**

| Type | Description |
|---|---|
| `any` | 指定行的全部内容 |

### `GetDataTableRowCount`

```text
GetDataTableRowCount(DataTable: UDataTable) -> number
```

获取指定DataTable的行数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DataTable` | `UDataTable` | 要读取的表格 |

**Returns**

| Type | Description |
|---|---|
| `number` | 行数 |

### `AsyncGetTableData`

```text
AsyncGetTableData(TablePath: string, CallBack: function, CallBack_self: UObject)
```

异步根据表格路径获取表格内容
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TablePath` | `string` | 表格路径，支持格式见UGCGameSystem.GetTableData |
| `CallBack` | `function` | lua普通函数或lambda函数, 加载完成的资源会作为参数传给CallBack函数 (注意带函数定义带冒号和不带的区别) |
| `CallBack_self` | `UObject` | 这是为了兼容CallBack函数定义带冒号和不带冒号两种情况。如果带冒号(table:func()型,CallBack_self传入table);如果不带冒号,CallBack_self传入nil |

### `AsyncGetTableCount`

```text
AsyncGetTableCount(TablePath: string, CallBack: function, CallBack_self: UObject)
```

异步根据表格路径获取表格行数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TablePath` | `string` | 表格路径，支持格式见UGCGameSystem.GetTableData |
| `CallBack` | `function` | lua普通函数或lambda函数, 加载完成的资源会作为参数传给CallBack函数 (注意带函数定义带冒号和不带的区别) |
| `CallBack_self` | `UObject` | 这是为了兼容CallBack函数定义带冒号和不带冒号两种情况。如果带冒号(table:func()型,CallBack_self传入table);如果不带冒号,CallBack_self传入nil |

### `AsyncGetTableDataByRowName`

```text
AsyncGetTableDataByRowName(TablePath: string, RowName: string, CallBack: function, CallBack_self: UObject)
```

异步根据表格路径获取表格内容
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TablePath` | `string` | 表格路径，支持格式见UGCGameSystem.GetTableData |
| `RowName` | `string` | 查询关键字 |
| `CallBack` | `function` | lua普通函数或lambda函数, 加载完成的资源会作为参数传给CallBack函数 (注意带函数定义带冒号和不带的区别) |
| `CallBack_self` | `UObject` | 这是为了兼容CallBack函数定义带冒号和不带冒号两种情况。如果带冒号(table:func()型,CallBack_self传入table);如果不带冒号,CallBack_self传入nil |

### `IsMyFriend`

```text
IsMyFriend(UID: number) -> boolean
```

是否为好友
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为好友 |

### `AddFriend`

```text
AddFriend(UID: number)
```

添加好友
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |

### `GetUGCResourcesFullPath`

```text
GetUGCResourcesFullPath(RelativePath: string) -> string
```

获取资源的完整加载路径
仅自己工程下资源需要使用此函数获取路径，和平精英目录资源不需要使用此函数拼接路径
例：自己工程资源
local ClassPath = "Asset/MyBlueprint.MyBlueprint_C"
UE.LoadClass(UGCGameSystem.GetUGCResourcesFullPath(ClassPath))
例：和平精英目录资源
local ClassPath = "/Game/Arts_PlayerBluePrints/Vehicle/VH_Buggy/BP_VH_Buggy.BP_VH_Buggy_C"
UE.LoadClass(ClassPath)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RelativePath` | `string` | 工程资源路径 |

**Returns**

| Type | Description |
|---|---|
| `string` | 完整资源路径 |

### `UGCRequire`

```text
UGCRequire(RelativePath: string) -> any
```

用于替代原生require，如果需要将功能发布至资源商店，需要使用此函数 require lua 文件
例：require("Script.MyLua");
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RelativePath` | `string` | Lua 文件路径 |

**Returns**

| Type | Description |
|---|---|
| `any` | 加载的 lua 文件 |

### `ShowUGCRankAndAchievementUI`

```text
ShowUGCRankAndAchievementUI()
```

显示绿洲段位，徽章结算界面
会自动显示段位变化以及新增徽章
详细内容参考：https://developer.gp.qq.com/wikieditor/#/catalog/375
生效范围：客户端

### `GetSTExtraGMDelegatesMgr`

```text
GetSTExtraGMDelegatesMgr() -> UObject
```

获取 DS 全局事件代理
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `UObject` | 全局代理类 |

### `GetLocalPlayerController`

```text
GetLocalPlayerController() -> ASTExtraPlayerController
```

获取客户端当前的 PlayerController
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `ASTExtraPlayerController` | 当前正在控制的玩家 |

### `GetLocalPlayerPawn`

```text
GetLocalPlayerPawn() -> PlayerPawn
```

获取客户端当前的 PlayerPawn
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `PlayerPawn` | 当前的PlayerPawn |

### `GetLocalPlayerState`

```text
GetLocalPlayerState() -> ASTExtraPlayerState
```

获取客户端当前的 PlayerState
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `ASTExtraPlayerState` | 当前的PlayerState |

### `GetLocalPlayerKey`

```text
GetLocalPlayerKey() -> number
```

获取客户端当前的 PlayerKey
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `number` | 当前的PlayerKey |

### `GetGameMode`

```text
GetGameMode() -> AUGCGameModeBase
```

获取当前的 GameMode
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `AUGCGameModeBase` | 当前的 GameMode |

### `GetGameState`

```text
GetGameState() -> AUGCGameStateBase
```

获取当前的 GameState
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `AUGCGameStateBase` | 当前的 GameState |

### `IsRoomMode`

```text
IsRoomMode() -> boolean
```

判断是否是房间模式
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `boolean` | true表示是房间模式，false表示不是房间模式 |

### `CollectPlayerAntiAFKData`

```text
CollectPlayerAntiAFKData(UID: number, DataKey: string, DataValue: string)
```

反挂机数据收集 在结算数据里上报 1.击杀数-Kill 2.伤害量-DamageAmount 3.移动距离-TravelDistance 4.达到存档数-ReachedArchives
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 上报玩家的UID |
| `DataKey` | `string` | 上报数据的字段名字 |
| `DataValue` | `string` | 上报数据 |

### `GetCurrentLevel`

```text
GetCurrentLevel(WorldContextObject: UObject, bRemovePrefixString: boolean) -> string
```

获取当前关卡
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 关卡上下文对象 |
| `bRemovePrefixString` | `boolean` | 是否移除前缀字符串 |

**Returns**

| Type | Description |
|---|---|
| `string` | 当前关卡的名字 |

### `LoadStreamLevel`

```text
LoadStreamLevel(LevelName: string, bMakeVisibleAfterLoad: boolean, bShouldBlockOnLoad: boolean, LatentInfo: LatentInfo)
```

加载关卡
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LevelName` | `string` | 关卡名字 |
| `bMakeVisibleAfterLoad` | `boolean` | 是否在加载完成后显示关卡 |
| `bShouldBlockOnLoad` | `boolean` | 是否延迟加载 |
| `LatentInfo` | `LatentInfo` | 延迟信息 |

### `UnloadStreamLevel`

```text
UnloadStreamLevel(LevelName: string, LatentInfo: LatentInfo)
```

卸载关卡
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LevelName` | `string` | 关卡名字 |
| `LatentInfo` | `LatentInfo` | 延迟信息 |

### `FlushLevelStreaming`

```text
FlushLevelStreaming()
```

强制刷新关卡流加载
生效范围：服务器

### `MakeWeakObjectPtr`

```text
MakeWeakObjectPtr(InObject: UObject) -> WeakObjectPtr
```

【废弃】创建弱对象指针
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObject` | `UObject` | 对象 |

**Returns**

| Type | Description |
|---|---|
| `WeakObjectPtr` | 弱对象指针 |

### `GetObjectFromWeakObjectPtr`

```text
GetObjectFromWeakObjectPtr(InWeakObjectPtr: WeakObjectPtr) -> UObject
```

【废弃】从弱对象指针获取对象
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InWeakObjectPtr` | `WeakObjectPtr` | 弱对象指针 |

**Returns**

| Type | Description |
|---|---|
| `UObject` | 对象 |

### `IsWeakObjectPtrValid`

```text
IsWeakObjectPtrValid(InWeakObjectPtr: WeakObjectPtr) -> boolean
```

【废弃】判断弱对象指针是否有效
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InWeakObjectPtr` | `WeakObjectPtr` | 弱对象指针 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否有效 |

### `SwitchMouseCursorShowState`

```text
SwitchMouseCursorShowState()
```

切换鼠标显示
生效范围：客户端

### `GetShowMouseCursor`

```text
GetShowMouseCursor() -> boolean
```

获取鼠标显示状态
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否显示鼠标 |

### `SetMouseCursorShowState`

```text
SetMouseCursorShowState(bShow: boolean)
```

设置鼠标显示
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bShow` | `boolean` | 是否显示鼠标 |

### `DrawOutline`

```text
DrawOutline(InActor: AActor, bIsDrawOutline: boolean, OutlineThickness: number, OutlineColor: FLinearColor)
```

设置Actor描边
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |
| `bIsDrawOutline` | `boolean` | 是否描边 |
| `OutlineThickness` | `number` | 描边粗细 |
| `OutlineColor` | `FLinearColor` | 描边颜色 |

### `IsUGCPIE`

```text
IsUGCPIE() -> boolean
```

是否为PIE环境
生效范围：服务器 & 客户端

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为PIE环境 |

### `SpawnEmitterAtLocation`

```text
SpawnEmitterAtLocation(WorldContext: UObject, EmitterTemplate: UParticleSystem, Location: FVector, Rotation: FRotator, Scale: FVector, bAutoDestroy: boolean) -> UParticleSystemComponent
```

在指定位置生成粒子效果，粒子系统播放完成后会自动销毁，不会进行网络复制
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `EmitterTemplate` | `UParticleSystem` | 要创建的粒子系统 |
| `Location` | `FVector` | 位置 |
| `Rotation` | `FRotator` | 旋转 |
| `Scale` | `FVector` | 缩放 |
| `bAutoDestroy` | `boolean` | 是否自动销毁 |

**Returns**

| Type | Description |
|---|---|
| `UParticleSystemComponent` | 粒子系统组件 |

### `SpawnEmitterAttached`

```text
SpawnEmitterAttached(EmitterTemplate: UParticleSystem, AttachComponent: USceneComponent, AttachPointName: string, Location: FVector, Rotation: FRotator, Scale: FVector, LocationType: EAttachLocation, bAutoDestroy: boolean) -> UParticleSystemComponent
```

播放指定效果，该效果会附加到指定组件并跟随其移动。效果播放完成后系统将消失。此效果不进行网络复制
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterTemplate` | `UParticleSystem` | 要创建的粒子系统 |
| `AttachComponent` | `USceneComponent` | 要附加到的组件 |
| `AttachPointName` | `string` | 附加组件中用于生成发射器的可选命名点（若不指定则在附加组件原点生成） |
| `Location` | `FVector` | 根据 LocationType 的值，此参数可为相对于附加组件/点的偏移量；或为绝对世界位置（若 LocationType 为 KeepWorldPosition，则会将该位置转换为相对于附加组件/点的偏移） |
| `Rotation` | `FRotator` | 根据 LocationType 的值，此参数可为相对于附加组件/点的旋转偏移量；或为绝对世界旋转（若 LocationType 为 KeepWorldPosition，则会将该旋转转换为相对于附加组件/点的偏移） |
| `Scale` | `FVector` | 根据 LocationType 的值，此参数可为相对于附加组件的缩放比例；或为绝对世界缩放（若 LocationType 为 KeepWorldPosition，则会将该缩放转换为相对于附加组件的比例） |
| `LocationType` | `EAttachLocation` | 指定 Location 是相对偏移量还是绝对世界位置 |
| `bAutoDestroy` | `boolean` | 粒子系统播放完成后，此组件是自动销毁还是可重新激活 |

**Returns**

| Type | Description |
|---|---|
| `UParticleSystemComponent` | 创建的粒子系统组件 |

### `SpawnDecalAtLocation`

```text
SpawnDecalAtLocation(WorldContext: UObject, DecalMaterial: UMaterialInterface, DecalSize: FVector, Location: FVector, Rotation: FRotator, LifeSpan: number) -> UDecalComponent
```

在指定位置和旋转角度生成一个贴花，生成后无需管理。此效果不进行网络复制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `DecalMaterial` | `UMaterialInterface` | 贴花的材质 |
| `DecalSize` | `FVector` | 贴花的尺寸 |
| `Location` | `FVector` | 贴花在世界空间中的放置位置 |
| `Rotation` | `FRotator` | 贴花在世界空间中的放置旋转 |
| `LifeSpan` | `number` | 贴花组件在时间结束后销毁（0表示永久存在） |

**Returns**

| Type | Description |
|---|---|
| `UDecalComponent` | 创建的贴花组件 |

### `SpawnDecalAtAttached`

```text
SpawnDecalAtAttached(DecalMaterial: UMaterialInterface, DecalSize: FVector, AttachComponent: USceneComponent, AttachPointName: string, Location: FVector, Rotation: FRotator, LocationType: EAttachLocation, LifeSpan: number) -> UDecalComponent
```

在指定组件上生成一个附加并跟随的贴花。此效果不进行网络复制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DecalMaterial` | `UMaterialInterface` | 贴花的材质 |
| `DecalSize` | `FVector` | 贴花的尺寸 |
| `AttachComponent` | `USceneComponent` | 要附加到的组件 |
| `AttachPointName` | `string` | 附加组件中用于生成发射器的可选命名点（若不指定则在附加组件原点生成） |
| `Location` | `FVector` | 根据 LocationType 的值，此参数可为相对于附加组件/点的偏移量；或为绝对世界位置（若 LocationType 指定为 KeepWorldPosition，则会将该位置转换为相对于附加组件/点的偏移） |
| `Rotation` | `FRotator` | 根据 LocationType 的值，此参数可为相对于附加组件/点的旋转偏移量；或为绝对世界旋转（若 LocationType 指定为 KeepWorldPosition，则会将该旋转转换为相对于附加组件/点的偏移） |
| `LocationType` | `EAttachLocation` | 指定 Location 是相对偏移量还是绝对世界位置 |
| `LifeSpan` | `number` | 贴花组件在时间结束后销毁（0 表示永久存在） |

**Returns**

| Type | Description |
|---|---|
| `UDecalComponent` | 创建的贴花组件 |

### `GetTimeSeconds`

```text
GetTimeSeconds(WorldContext: UObject) -> number
```

获得当前游戏开始之后的时间，单位秒，受时间膨胀影响，但不受游戏暂停影响
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `number` | 当前游戏开始之后的时间，单位秒 |

### `DateTimeToTimeStamp`

```text
DateTimeToTimeStamp(DateTime: FDateTime) -> number
```

将日期时间转换为时间戳
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DateTime` | `FDateTime` | 日期时间 |

**Returns**

| Type | Description |
|---|---|
| `number` | 时间戳 |

### `GetCurrentDateTime`

```text
GetCurrentDateTime() -> FDateTime
```

获取当前日期时间
生效范围：服务器 & 客户端

**Returns**

| Type | Description |
|---|---|
| `FDateTime` | 当前日期时间 |

### `GetDSRemainingTime`

```text
GetDSRemainingTime() -> int
```

获取DS剩余时间，单位秒
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `int` | DS剩余时间 |

### `SetDSCloseNotify`

```text
SetDSCloseNotify(NotifyTimes: int[])
```

设置DS关闭通知时间，监听UGCGenericMessageSystem.UserDefinedMessages.UGC.UGCDSShutDownManager.DSCloseNotify，会在到达时间时发送通知，附带参数为DS剩余时间
假设已经到了设置的时间比DS长，例如DS剩余关闭时间是30s，设置的时间组是{50，40，20}，那么会在游戏开始时，50和40两个时间点合并仅发送一次通知，目前仅支持整数时间点
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotifyTimes` | `int[]` | 通知时间组 |

### `GameOver`

```text
GameOver()
```

游戏结束，一键执行发送所有玩家结算，玩家退出和玩家销毁的动作，并关闭DS，这个接口会有一定延时，如果玩家还在游戏内执行，会将玩家强行踢出ds，返回大厅
生效范围：服务器

### `IsObserver`

```text
IsObserver(PlayerController: APlayerController) -> boolean
```

判断玩家是否为观战玩家
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `APlayerController` | 玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为观战玩家 |

### `MakeCustomDamageNumberParams`

```text
MakeCustomDamageNumberParams() -> FUGCDamageNumberParams
```

生成自定义伤害数字默认参数
生效范围：服务器 & 客户端

**Returns**

| Type | Description |
|---|---|
| `FUGCDamageNumberParams` | 自定义伤害数字参数 |

### `AddUGCCustomDamageNumber`

```text
AddUGCCustomDamageNumber(WorldContext: UObject, TargetActor: Actor, Params: FUGCDamageNumberParams) -> boolean
```

显示自定义伤害数字
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `TargetActor` | `Actor` | 伤害数字显示目标 |
| `Params` | `FUGCDamageNumberParams` | 自定义伤害数字参数 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为观战玩家 |

### `IsOuterlineDEV`

```text
IsOuterlineDEV() -> boolean
```

【废弃】请使用 UGCGameSystem.GetDSEnvType
判断是否为外研线
生效范围：服务器 & 客户端

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为外研线 |

### `GetDSEnvType`

```text
GetDSEnvType() -> string
```

获取当前DS所在的运行环境类型
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `string` | 当前DS环境类型，值为 UGCGameSystem.DSEnvType 枚举之一 |

### `IsGray`

```text
IsGray() -> boolean
```

当前玩法是否处于灰度中
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否灰度玩法 |

## Language

`lua`
