---
id: "api-chunk:class:4"
title: "Oasis API class chunk 4"
source: "https://developer.gp.qq.com/api/"
category: "API Wiki/class"
kind: "api_chunk"
---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9F%BA%E7%A1%80%E5%8A%9F%E8%83%BD/UGCGameSystem.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%80%AA%E7%89%A9%E7%B3%BB%E7%BB%9F/UGCGenericCharacterSystem.json -->

# UGCGenericCharacterSystem

怪物系统接口库

## Functions

### `KillGenericCharacter`

```text
KillGenericCharacter(GenericCharacter: AUGCGenericCharacter)
```

强制杀死怪物
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

### `IsAlive`

```text
IsAlive(GenericCharacter: AUGCGenericCharacter) -> boolean
```

小怪是否存活
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 小怪是否存活 |

### `IsGenericCharacter`

```text
IsGenericCharacter(Target: AActor) -> boolean
```

目标是否为小怪
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `AActor` | 目标 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为小怪 |

### `GetHealth`

```text
GetHealth(GenericCharacter: AUGCGenericCharacter) -> number
```

获取小怪血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

**Returns**

| Type | Description |
|---|---|
| `number` | 血量 |

### `GetHealthMax`

```text
GetHealthMax(GenericCharacter: AUGCGenericCharacter) -> number
```

获取小怪血量上限
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

**Returns**

| Type | Description |
|---|---|
| `number` | 血量上限 |

### `SetHealth`

```text
SetHealth(GenericCharacter: AUGCGenericCharacter, Health: number)
```

设置小怪血量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `Health` | `number` | 血量 |

### `SetHealthMax`

```text
SetHealthMax(GenericCharacter: AUGCGenericCharacter, HealthMax: number)
```

设置小怪血量上限
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `HealthMax` | `number` | 血量上限 |

### `EnableMovement`

```text
EnableMovement(GenericCharacter: AUGCGenericCharacter)
```

启动移动能力
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

### `DisableMovement`

```text
DisableMovement(GenericCharacter: AUGCGenericCharacter)
```

关闭移动能力
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

### `SetAvoidanceGroup`

```text
SetAvoidanceGroup(GenericCharacter: AUGCGenericCharacter, AvoidanceGroup: EGenericAvoidanceGroup)
```

设置避障组
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `AvoidanceGroup` | `EGenericAvoidanceGroup` | 避障组 |

### `MoveTo`

```text
MoveTo(GenericCharacter: AUGCGenericCharacter, InDestination: FVector, InStopRadius: number)
```

移动到目标位置(注意不要和行为树移动冲突)
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `InDestination` | `FVector` | 目的地 |
| `InStopRadius` | `number` | 停止距离 |

### `StopMove`

```text
StopMove(GenericCharacter: AUGCGenericCharacter)
```

停止移动(注意不要和行为树移动冲突)
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

### `GetCurrentVelocity`

```text
GetCurrentVelocity(GenericCharacter: AUGCGenericCharacter) -> FVector
```

获取当前怪物动量
生效范围：服务器/客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 当前动量 |

### `SetMaxSpeed`

```text
SetMaxSpeed(GenericCharacter: AUGCGenericCharacter, InSpeed: number, Reason: number)
```

设置最大移动速度
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `InSpeed` | `number` | 速度 |
| `Reason` | `number` | 原因 |

### `GetMaxSpeed`

```text
GetMaxSpeed(GenericCharacter: AUGCGenericCharacter) -> number
```

获取最大移动速度
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

**Returns**

| Type | Description |
|---|---|
| `number` | 最大移动速度 |

### `GetDefaultMaxSpeed`

```text
GetDefaultMaxSpeed(GenericCharacter: AUGCGenericCharacter) -> number
```

获取默认最大移动速度
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

**Returns**

| Type | Description |
|---|---|
| `number` | 默认最大移动速度 |

### `GetTargetEnemy`

```text
GetTargetEnemy(GenericCharacter: AUGCGenericCharacter) -> AActor
```

获取当前仇恨目标
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | 当前仇恨对象 |

### `RunBehavior`

```text
RunBehavior(GenericCharacter: AUGCGenericCharacter, BehaviorTreePath: string)
```

运行指定行为树
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `BehaviorTreePath` | `string` | 行为树路径 |

### `StopBehavior`

```text
StopBehavior(GenericCharacter: AUGCGenericCharacter, Reason: string)
```

停止当前行为树
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `Reason` | `string` | 原因 |

### `OverrideBehaviorTreeSetting`

```text
OverrideBehaviorTreeSetting(GenericCharacter: AUGCGenericCharacter, InBehaviorTreeSetting: FBehaviorTreeReflectSetting)
```

覆盖行为树设置并重新启动行为树
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `InBehaviorTreeSetting` | `FBehaviorTreeReflectSetting` | 新的行为树设置 |

### `GetBehaviorTreeSetting`

```text
GetBehaviorTreeSetting(GenericCharacter: AUGCGenericCharacter) -> FBehaviorTreeReflectSetting
```

获取当前行为树设置
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

**Returns**

| Type | Description |
|---|---|
| `FBehaviorTreeReflectSetting` | - |

### `PauseBehavior`

```text
PauseBehavior(GenericCharacter: AUGCGenericCharacter, Reason: string)
```

暂停当前行为树
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `Reason` | `string` | 原因 |

### `ResumeBehavior`

```text
ResumeBehavior(GenericCharacter: AUGCGenericCharacter, Reason: string)
```

继续当前行为树
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `Reason` | `string` | 原因 |

### `PlayAnimMontage`

```text
PlayAnimMontage(GenericCharacter: AUGCGenericCharacter, AnimMontage: UAnimMontage, InPlayRate: number)
```

播放蒙太奇动画
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `AnimMontage` | `UAnimMontage` | 蒙太奇动画 |
| `InPlayRate` | `number` | 播放速率 |

### `PlayAnimMontageByTag`

```text
PlayAnimMontageByTag(GenericCharacter: AUGCGenericCharacter, AnimGameplayTag: FGameplayTag, InPlayRate: number)
```

通过Tag播放蒙太奇动画
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `AnimGameplayTag` | `FGameplayTag` | 蒙太奇动画Tag |
| `InPlayRate` | `number` | 播放速率 |

### `AddOverrideAnimAsset`

```text
AddOverrideAnimAsset(GenericCharacter: AUGCGenericCharacter, Data: FGenericCharacterAnimOverrideData, BlendTime: number)
```

覆盖指定Tag的动画资源
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `Data` | `FGenericCharacterAnimOverrideData` | 覆写数据 |
| `BlendTime` | `number` | 混合时间 |

### `RemoveOverrideAnimAsset`

```text
RemoveOverrideAnimAsset(GenericCharacter: AUGCGenericCharacter, Data: FGenericCharacterAnimOverrideData, BlendTime: number)
```

移除覆盖指定Tag的动画资源
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `Data` | `FGenericCharacterAnimOverrideData` | 覆写数据 |
| `BlendTime` | `number` | 混合时间 |

### `IsEnableLogicPart`

```text
IsEnableLogicPart(GenericCharacter: AUGCGenericCharacter, InLogicPartTag: FGameplayTag) -> boolean
```

是否启用LogicPart
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `InLogicPartTag` | `FGameplayTag` | LogicPart Tag |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否启用 |

### `SpawnGenericCharacter`

```text
SpawnGenericCharacter(WorldContextObject: UObject, GenericCharacterClass: UClass, Location: FVector, Rotation: FRotator) -> AActor
```

在目标位置刷一个怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `GenericCharacterClass` | `UClass` | 怪物的类 |
| `Location` | `FVector` | 刷怪的位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | 刷出的怪物 |

### `SpawnGenericCharacterByGroup`

```text
SpawnGenericCharacterByGroup(WorldContextObject: UObject, GroupID: number, Location: FVector, Rotation: FRotator) -> AActor
```

在目标位置根据怪物组表中的ID刷一个怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `GroupID` | `number` | 怪物组表中的ID |
| `Location` | `FVector` | 刷怪的位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | 刷出的怪物 |

### `RangeSpawnGenericCharacters`

```text
RangeSpawnGenericCharacters(WorldContextObject: UObject, GenericCharacterClass: UClass, Location: FVector, Rotation: FRotator, Range: number, HeightRange: number, Count: number) -> table
```

在指定位置的圆形范围中寻找合适的地面刷出指定数量的怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `GenericCharacterClass` | `UClass` | 怪物的类 |
| `Location` | `FVector` | 刷怪范围的中心位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |
| `Range` | `number` | 刷怪圆形范围的半径 |
| `HeightRange` | `number` | 怪物刷出位置与中心位置的最大高度差 |
| `Count` | `number` | 刷出怪物的数量 |

**Returns**

| Type | Description |
|---|---|
| `table` | 刷出怪物的列表 |

### `RangeSpawnGenericCharactersByGroup`

```text
RangeSpawnGenericCharactersByGroup(WorldContextObject: UObject, GroupID: number, Location: FVector, Rotation: FRotator, Range: number, HeightRange: number, Count: number) -> table
```

在指定位置的圆形范围中寻找合适的地面刷出指定数量的怪，怪物类型由怪物组表ID指定
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `GroupID` | `number` | 怪物组表中的ID |
| `Location` | `FVector` | 刷怪范围的中心位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |
| `Range` | `number` | 刷怪圆形范围的半径 |
| `HeightRange` | `number` | 怪物刷出位置与中心位置的最大高度差 |
| `Count` | `number` | 刷出怪物的数量 |

**Returns**

| Type | Description |
|---|---|
| `table` | 刷出怪物的列表 |

### `RangeSpawnGenericCharactersOnTime`

```text
RangeSpawnGenericCharactersOnTime(WorldContextObject: UObject, GenericCharacterClass: UClass, Location: FVector, Rotation: FRotator, Range: number, HeightRange: number, MinSpawnCountPerLoop: number, MaxSpawnCountPerLoop: number, LoopTimes: number, IntervalMinTime: number, IntervalMaxTime: number, FirstDelayTime: number, Callback: function, CallbackSelf: table)
```

在指定位置的圆形范围中每隔一定时间寻找合适的地面刷出一定数量的怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `GenericCharacterClass` | `UClass` | 怪物类 |
| `Location` | `FVector` | 刷怪范围的中心位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |
| `Range` | `number` | 刷怪圆形范围的半径 |
| `HeightRange` | `number` | 怪物刷出位置与中心位置的最大高度差 |
| `MinSpawnCountPerLoop` | `number` | 每次刷怪的最小数量 |
| `MaxSpawnCountPerLoop` | `number` | 每次刷怪的最大数量 |
| `LoopTimes` | `number` | 总的刷怪轮数 |
| `IntervalMinTime` | `number` | 刷怪轮次间的最小时间间隔 |
| `IntervalMaxTime` | `number` | 刷怪轮次间的最大时间间隔 |
| `FirstDelayTime` | `number` | 从接口调用到首次刷怪的延迟时间 |
| `Callback` | `function` | 回调函数 |
| `CallbackSelf` | `table` | 回调函数的调用主体，静态函数时留空 |

### `RangeSpawnGenericCharactersByGroupOnTime`

```text
RangeSpawnGenericCharactersByGroupOnTime(WorldContextObject: UObject, GroupID: number, Location: FVector, Rotation: FRotator, Range: number, HeightRange: number, MinSpawnCountPerLoop: number, MaxSpawnCountPerLoop: number, LoopTimes: number, IntervalMinTime: number, IntervalMaxTime: number, FirstDelayTime: number, Callback: function, CallbackSelf: table)
```

在指定位置的圆形范围中每个一定时间寻找合适的地面刷出一定数量的怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `GroupID` | `number` | 怪物组表中的ID |
| `Location` | `FVector` | 刷怪范围的中心位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |
| `Range` | `number` | 刷怪圆形范围的半径 |
| `HeightRange` | `number` | 怪物刷出位置与中心位置的最大高度差 |
| `MinSpawnCountPerLoop` | `number` | 每次刷怪的最小数量 |
| `MaxSpawnCountPerLoop` | `number` | 每次刷怪的最大数量 |
| `LoopTimes` | `number` | 总的刷怪轮数 |
| `IntervalMinTime` | `number` | 刷怪轮次间的最小时间间隔 |
| `IntervalMaxTime` | `number` | 刷怪轮次间的最大时间间隔 |
| `FirstDelayTime` | `number` | 从接口调用到首次刷怪的延迟时间 |
| `Callback` | `function` | 回调函数 |
| `CallbackSelf` | `table` | 回调函数的调用主体，静态函数时留空 |

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

### `GetBlackboard`

```text
GetBlackboard(Actor: AActor) -> UBlackboardComponent
```

获取Actor的BlackboardComponent
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | Actor |

**Returns**

| Type | Description |
|---|---|
| `UBlackboardComponent` | BlackboardComponent |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/UGCGenericMessageSystem.json -->

# UGCGenericMessageSystem

广播信息接口库

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCGenericMessageSystem.Messages` | `-` | - |
| `UGCGenericMessageSystem.GlobalMessageListeners` | `-` | - |
| `UGCGenericMessageSystem.ObjectMessageListeners` | `-` | - |
| `UGCGenericMessageSystem.Messages.UGC.Player` | `-` | 玩家相关消息 |
| `UGCGenericMessageSystem.Messages.UGC.Player.PlayerEnter` | `-` | 玩家进入游戏<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param PlayerKey number @玩家的 PlayerKey |
| `UGCGenericMessageSystem.Messages.UGC.Player.PlayerExit` | `-` | 玩家退出游戏<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param PlayerKey number @玩家的 PlayerKey |
| `UGCGenericMessageSystem.Messages.UGC.Player.PlayerLost` | `-` | 玩家掉线<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param PlayerKey number @玩家的 PlayerKey |
| `UGCGenericMessageSystem.Messages.UGC.Player.PlayerReconnect` | `-` | 玩家重连进入游戏<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param PlayerKey number @玩家的 PlayerKey |
| `UGCGenericMessageSystem.Messages.UGC.PlayerPawn` | `-` | 玩家角色相关的消息 |
| `UGCGenericMessageSystem.Messages.UGC.PlayerPawn.PawnSpawn` | `-` | 玩家角色首次出生<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param PlayerKey number @玩家的 PlayerKey |
| `UGCGenericMessageSystem.Messages.UGC.PlayerPawn.PreTakeDamage` | `-` | 玩家角色受到伤害前（最终伤害计算前)<br>生效范围：服务器<br>ListenedObject：指定被伤害角色，不指定则接收所有角色消息<br>@param VictimPlayer ASTExtraBaseCharacter @造成伤害的玩家角色<br>@param DamageCauserActor AActor @伤害来源<br>@param EventInstigator Controller @伤害来源的玩家控制器<br>@param Damage number @伤害值<br>@param DamageContext FGameMagnitudeContext @伤害事件上下文 |
| `UGCGenericMessageSystem.Messages.UGC.PlayerPawn.PostTakeDamage` | `-` | 玩家角色受到伤害后（最终伤害计算后)<br>生效范围：服务器<br>ListenedObject：指定被伤害角色，不指定则接收所有角色消息<br>@param VictimPlayer ASTExtraBaseCharacter @造成伤害的玩家角色<br>@param DamageCauserActor AActor @伤害来源<br>@param EventInstigator Controller @伤害来源的玩家控制器<br>@param Damage number @伤害值<br>@param DamageContext FGameMagnitudeContext @伤害事件上下文 |
| `UGCGenericMessageSystem.Messages.UGC.PlayerPawn.PreRecoverHealth` | `-` | 玩家角色受到治疗前（最终治疗计算前)<br>生效范围：服务器<br>ListenedObject：指定被伤害角色<br>@param RecoverValue float @预治疗值<br>@param RecoveryInstigator AActor @治疗来源的玩家控制器<br>@param RecoveryCauser Controller @治疗来源<br>@param RecoverTags FGameplayTag[] @治疗附带的Tags |
| `UGCGenericMessageSystem.Messages.UGC.PlayerPawn.PostRecoverHealth` | `-` | 玩家角色受到治疗后（最终治疗计算后)<br>生效范围：服务器<br>ListenedObject：指定被伤害角色<br>@param RecoverValue float @实际治疗值<br>@param RecoveryInstigator AActor @治疗来源的玩家控制器<br>@param RecoveryCauser Controller @治疗来源<br>@param RecoverTags FGameplayTag[] @治疗附带的Tags |
| `UGCGenericMessageSystem.Messages.UGC.PlayerPawn.PawnDefeat` | `-` | 玩家角色被击败<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param VictimPlayerKey number @被击败玩家的 PlayerKey<br>@param InstigatorPlayerKey number @击败玩家的 PlayerKey<br>@param DamageType EDamageType @伤害类型 |
| `UGCGenericMessageSystem.Messages.UGC.PlayerPawn.PawnRespawn` | `-` | 玩家角色重生<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param PlayerKey number @玩家的 PlayerKey |
| `UGCGenericMessageSystem.Messages.UGC.MobPawn` | `-` | - |
| `UGCGenericMessageSystem.Messages.UGC.MobPawn.Spawn` | `-` | 怪物角色首次出生<br>生效范围：服务器&客户端<br>ListenedObject：指定生成的怪物，不指定则接收所有怪物角色消息<br>@param MobPawn AUGCMobCharacter @怪物 |
| `UGCGenericMessageSystem.Messages.UGC.MobPawn.PreTakeDamage` | `-` | 怪物角色受到伤害前（最终伤害计算前)<br>生效范围：服务器<br>ListenedObject：指定被伤害怪物角色，不指定则接收所有怪物角色消息<br>@param MobPawn AUGCMobCharacter @怪物<br>@param DamageCauserActor AActor @伤害来源<br>@param EventInstigator Controller @伤害来源的玩家控制器<br>@param Damage number @伤害值<br>@param DamageContext FGameMagnitudeContext @伤害事件上下文 |
| `UGCGenericMessageSystem.Messages.UGC.MobPawn.PostTakeDamage` | `-` | 怪物角色受到伤害后（最终伤害计算后)<br>生效范围：服务器<br>ListenedObject：指定被伤害怪物角色，不指定则接收所有怪物角色消息<br>@param MobPawn AUGCMobCharacter @怪物<br>@param DamageCauserActor AActor @伤害来源<br>@param EventInstigator Controller @伤害来源的玩家控制器<br>@param Damage number @伤害值<br>@param DamageContext FGameMagnitudeContext @伤害事件上下文 |
| `UGCGenericMessageSystem.Messages.UGC.MobPawn.PreRecoverHealth` | `-` | 怪物角色受到治疗前（最终治疗计算前)<br>生效范围：服务器<br>ListenedObject：指定被伤害怪物角色<br>@param RecoverValue float @预治疗值<br>@param RecoveryInstigator AActor @治疗来源的玩家控制器<br>@param RecoveryCauser Controller @治疗来源<br>@param RecoverTags FGameplayTag[] @治疗附带的Tags |
| `UGCGenericMessageSystem.Messages.UGC.MobPawn.PostRecoverHealth` | `-` | 怪物角色受到治疗后（最终治疗计算后)<br>生效范围：服务器<br>ListenedObject：指定被伤害怪物角色<br>@param RecoverValue float @实际治疗值<br>@param RecoveryInstigator AActor @治疗来源的玩家控制器<br>@param RecoveryCauser Controller @治疗来源<br>@param RecoverTags FGameplayTag[] @治疗附带的Tags |
| `UGCGenericMessageSystem.Messages.UGC.MobPawn.PostBeKilled` | `-` | 怪物角色被击杀<br>生效范围：服务器&客户端<br>ListenedObject：指定被击杀怪物角色，不指定则接收所有怪物角色消息<br>@param MobPawn AUGCMobCharacter @被击杀的怪物<br>@param Killer Controller @击杀该怪物的玩家控制器 |
| `UGCGenericMessageSystem.Messages.UGC.MobPawn.StateChange` | `-` | 怪物角色状态变化<br>生效范围：服务器&客户端<br>ListenedObject：指定改变状态的怪物角色，不指定则接收所有怪物角色消息<br>@param MobPawn AUGCMobCharacter @被击杀的怪物<br>@param OldState EUGCMobState @变化前的状态<br>@param NewState EUGCMobState @变化后的状态 |
| `UGCGenericMessageSystem.Messages.UGC.MobSpawner` | `-` | 刷怪器相关的消息 |
| `UGCGenericMessageSystem.Messages.UGC.MobSpawner.WaveStart` | `-` | 刷怪管理器波次开始<br>生效范围：服务器<br>ListenedObject：指定特定的刷怪管理器，不指定则接收所有刷怪管理器消息<br>@param MobSpawnerManager AUGCMobSpawnerManager @波次所属的刷怪管理器<br>@param WaveIndex number |
| `UGCGenericMessageSystem.Messages.UGC.MobSpawner.WaveEnd` | `-` | 刷怪管理器波次结束<br>生效范围：服务器<br>ListenedObject：指定特定的刷怪管理器，不指定则接收所有刷怪管理器消息<br>@param MobSpawnerManager AUGCMobSpawnerManager @波次所属的刷怪管理器<br>@param WaveIndex number |
| `UGCGenericMessageSystem.Messages.UGC.MobSpawner.AllWaveEnd` | `-` | 刷怪管理器所有波次结束<br>生效范围：服务器<br>ListenedObject：指定特定的刷怪管理器，不指定则接收所有刷怪管理器消息<br>@param MobPawn AUGCMobCharacter @被击杀的怪物 |
| `UGCGenericMessageSystem.Messages.UGC.MobSpawner.AllMobDie` | `-` | 刷怪管理器所有波次的怪物死亡<br>生效范围：服务器<br>ListenedObject：指定特定的刷怪管理器，不指定则接收所有刷怪管理器消息<br>@param MobPawn AUGCMobCharacter @被击杀的怪物 |
| `UGCGenericMessageSystem.Messages.UGC.Client` | `-` | - |
| `UGCGenericMessageSystem.Messages.UGC.Client.MainUI` | `-` | - |
| `UGCGenericMessageSystem.Messages.UGC.Client.MainUI.InitMainUI` | `-` | 初始化和平 MainUI<br>生效范围：客户端<br>ListenedObject：无，全局事件<br>@param PC Controller @初始化 MainUI 的玩家控制器 |
| `UGCGenericMessageSystem.Messages.UGC.Game` | `-` | - |
| `UGCGenericMessageSystem.Messages.UGC.Game.GameEnd` | `-` | 游戏结束<br>生效范围：服务器<br>ListenedObject：无，全局事件 |
| `UGCGenericMessageSystem.Messages.UGC.Game.GameStart` | `-` | 游戏开始<br>生效范围：服务器<br>ListenedObject：无，全局事件 |
| `UGCGenericMessageSystem.Messages.UGC.GamePart` | `-` | - |
| `UGCGenericMessageSystem.Messages.UGC.GamePart.GamePartLoaded` | `-` | GamePart 加载完成。在此消息回调中执行 GetGamePartGlobalActor 以确保 GamePart 对象可用。<br>生效范围：服务器&客户端<br>ListenedObject：无，全局事件<br>@param GamePart string @加载完成的 GamePart 模块 |
| `UGCGenericMessageSystem.Messages.UGC.GamePart.GamePartLoadedForPlayer` | `-` | GamePart 加载完成。在此消息回调中执行 GetGamePartGlobalActor 以确保 GamePart 对象可用。<br>ForPlayer 可区分不同客户端上运行的 GamePart 模块。<br>生效范围：服务器&客户端<br>ListenedObject：无，全局事件<br>@param GamePart string @加载完成的 GamePart 模块<br>@param PlayerController PlayerController @加载完成的 GamePart 模块所属的客户端玩家控制器 |
| `UGCGenericMessageSystem.Messages.UGC.Weapon` | `-` | 枪械相关的消息 |
| `UGCGenericMessageSystem.Messages.UGC.Weapon.BulletHit` | `-` | 枪械的子弹命中<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param Gun ASTExtraShootWeapon @监听的枪械<br>@param Data FBulletHitInfoUploadData @命中数据 |
| `UGCGenericMessageSystem.Messages.UGC.Weapon.Fire` | `-` | 枪械开火<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param Gun ASTExtraShootWeapon @监听的枪械 |
| `UGCGenericMessageSystem.Messages.UGC.Weapon.StopFire` | `-` | 枪械停火<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param Gun ASTExtraShootWeapon @监听的枪械 |
| `UGCGenericMessageSystem.Messages.UGC.Weapon.PostEquipWeapon` | `-` | 枪械装备<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param bIsEquip boolean @是否装备<br>@param Player ASTExtraCharacter @持有者<br>@param Weapon ASTExtraWeapon @当前武器 |
| `UGCGenericMessageSystem.Messages.UGC.Weapon.Reload` | `-` | 枪械换弹<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param Gun ASTExtraShootWeapon @监听的枪械 |
| `UGCGenericMessageSystem.Messages.UGC.Weapon.ScopeIn` | `-` | 枪械开镜<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param Gun ASTExtraShootWeapon @监听的枪械 |
| `UGCGenericMessageSystem.Messages.UGC.Weapon.ScopeOut` | `-` | 枪械关镜<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param Gun ASTExtraShootWeapon @监听的枪械 |
| `UGCGenericMessageSystem.Messages.UGC.Weapon.SwitchWeapon` | `-` | 枪械切换<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param NewGun ASTExtraShootWeapon @新武器<br>@param OldGun ASTExtraShootWeapon @老武器<br>@param Player ASTExtraCharacter @持有者 |
| `UGCGenericMessageSystem.Messages.UGC.Attribute` | `-` | - |
| `UGCGenericMessageSystem.Messages.UGC.Attribute.GlobalAttrChanged` | `-` | 全局属性改变<br>生效范围：服务器<br>ListenedObject：监听的属性，不指定监听的属性则接收所有属性消息<br>@param OwnerActor AActor @属性所有者<br>@param AttrName string @属性名<br>@param CurValue number @属性值 |
| `UGCGenericMessageSystem.Messages.UGC.LevelFlow` | `-` | - |
| `UGCGenericMessageSystem.Messages.UGC.LevelFlow.LevelBegin` | `-` | 关卡开始<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param int CurrentStage @当前关卡数 |
| `UGCGenericMessageSystem.Messages.UGC.LevelFlow.GameBegin` | `-` | 游戏开始<br>生效范围：服务器<br>ListenedObject：无，全局事件 |
| `UGCGenericMessageSystem.Messages.UGC.Task` | `-` | - |
| `UGCGenericMessageSystem.Messages.UGC.Task.TaskCreated` | `-` | 任务模板中所有任务初始化完毕<br>生效范围：服务器&客户端<br>ListenedObject：指定任务监听器，不指定则接受所有任务监听器消息 |
| `UGCGenericMessageSystem.Messages.UGC.PersistEffect` | `-` | - |
| `UGCGenericMessageSystem.Messages.UGC.PersistEffect.ApplyPersistEffect` | `-` | PersistEffect挂载到UPersistBaseComponent<br>生效范围：服务器&客户端<br>ListenedObject：指定UPersistBaseComponent，不指定则接收所有UPersistBaseComponent消息<br>@param PE UPersistEffectBase @当前挂载的PersistEffect |
| `UGCGenericMessageSystem.Messages.UGC.PersistEffect.UnApplyPersistEffect` | `-` | PersistEffect从UPersistBaseComponent上卸载<br>生效范围：服务器&客户端<br>ListenedObject：指定UPersistBaseComponent，不指定则接收所有UPersistBaseComponent消息<br>@param PE UPersistEffectBase @当前卸载的PersistEffect |
| `UGCGenericMessageSystem.Messages.UGC.PersistEffect.ChangeState` | `-` | PersistEffectSkill的状态改变<br>生效范围：服务器&客户端<br>ListenedObject：指定UPersistEffectSkill，不指定则接收所有UPersistEffectSkill消息<br>@param PESkill UPersistEffectSkill @当前改变状态的PersistEffectSkill<br>@param EventType EPSkillEventSkillStateEvent @当前改变后的状态 |
| `UGCGenericMessageSystem.Messages.UGC.Team` | `-` | 队伍相关 |
| `UGCGenericMessageSystem.Messages.UGC.Team.TeammateLogin` | `-` | 有队员加入队伍<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param PlayerKey number @加入队伍玩家的PlayerKey<br>@param TeamID number @队伍ID |
| `UGCGenericMessageSystem.Messages.UGC.AirDrop` | `-` | - |
| `UGCGenericMessageSystem.Messages.UGC.AirDrop.SuccessfullyGeneratedAirDrop` | `-` | 成功生成AirDrop<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param InsID number @空投箱实例ID<br>@param AirDropBox BP_UGCAirDropBox_GamePart_C @空投箱 |
| `UGCGenericMessageSystem.Messages.UGC.AirDrop.SuccessfullyDestroyedAirDrop` | `-` | 成功销毁AirDrop<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param InsID number @空投箱实例ID |
| `UGCGenericMessageSystem.Messages.UGC.AirDrop.SuccessfullyPickedUpAirDrop` | `-` | 成功拾取AirDrop<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param InsID number @空投箱实例ID |
| `UGCGenericMessageSystem.Messages.UGC.TowerWave` | `-` | 塔防波次相关消息 |
| `UGCGenericMessageSystem.Messages.UGC.TowerWave.WaveChanged` | `-` | 波次变化（客户端本地通知）<br>生效范围：客户端<br>ListenedObject：无，全局事件<br>@param CurrentWaveIndex number @当前波次索引（从0开始，-1=未开始）<br>@param TotalWaveCount number @总波次数 |
| `UGCGenericMessageSystem.Messages.UGC.TowerWave.StateChanged` | `-` | 波次状态变化（客户端本地通知）<br>生效范围：客户端<br>ListenedObject：无，全局事件<br>@param CurrentWaveIndex number @当前波次索引<br>@param WaveState number @波次状态（EWaveState枚举值） |
| `UGCGenericMessageSystem.Messages.UGC.TowerWave.CountdownChanged` | `-` | 倒计时变化（客户端本地通知）<br>生效范围：客户端<br>ListenedObject：无，全局事件<br>@param Countdown number @剩余倒计时（秒） |
| `UGCGenericMessageSystem.Messages.UGC.TowerWave.AllComplete` | `-` | 所有波次完成<br>生效范围：服务器&客户端<br>ListenedObject：无，全局事件<br>@param TotalWaveCount number @总波次数 |
| `UGCGenericMessageSystem.Messages.UGC.TowerWave.RequestRoundEnd` | `-` | 请求回合结束（所有波次完成后触发）<br>生效范围：服务器<br>ListenedObject：无，全局事件 |
| `UGCGenericMessageSystem.UserDefinedMessages.UGC.UGCDSShutDownManager.DSCloseNotify` | `-` | DS关闭前通知<br>生效范围：服务器<br>ListenedObject：无，全局事件<br>@param DSRemainingTime table @DS剩余时间，唯一key: DSRemainingTime |

## Functions

### `ListenObjectMessage`

```text
ListenObjectMessage(ListenedObject: UObject, Message: string, Listener: UObject, Callback: function) -> number
```

监听对象的广播信息，作用包含ListenUserDefinedObjectMessage，正常仅调用本接口即可
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ListenedObject` | `UObject` | 被监听对象 |
| `Message` | `string` | 广播信息的索引，后续的广播和监听都通过索引进行操作 |
| `Listener` | `UObject` | 监听对象 |
| `Callback` | `function` | 监听对象监听到广播后调用的回调函数 |

**Returns**

| Type | Description |
|---|---|
| `number` | 返回监听ID |

### `BroadcastUserDefinedObjectMessage`

```text
BroadcastUserDefinedObjectMessage(ListenedObject: UObject, Message: string, ...: any)
```

广播自定义的对象消息
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ListenedObject` | `UObject` | 被监听对象 |
| `Message` | `string` | 广播信息的索引，后续的广播和监听都通过索引进行操作 |
| `...` | `any` | 自定义事件参数 |

### `ListenGlobalMessage`

```text
ListenGlobalMessage(WorldContextObject: UObject, Message: string, Listener: UObject, Callback: function) -> number
```

监听全局的广播信息，作用包含ListenUserDefinedGlobalMessage，正常仅调用本接口即可
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Message` | `string` | 广播信息的索引，后续的广播和监听都通过索引进行操作 |
| `Listener` | `UObject` | 监听对象 |
| `Callback` | `function` | 监听对象监听到广播后调用的回调函数 |

**Returns**

| Type | Description |
|---|---|
| `number` | 返回监听ID |

### `ListenUserDefinedGlobalMessage`

```text
ListenUserDefinedGlobalMessage(WorldContextObject: UObject, Message: string, Listener: UObject, Callback: function) -> number
```

监听自定义的全局广播信息
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Message` | `string` | 广播信息的索引，后续的广播和监听都通过索引进行操作 |
| `Listener` | `UObject` | 监听对象 |
| `Callback` | `function` | 监听对象监听到广播后调用的回调函数 |

**Returns**

| Type | Description |
|---|---|
| `number` | 返回监听ID |

### `BroadcastUserDefinedGlobalMessage`

```text
BroadcastUserDefinedGlobalMessage(Message: string, ...: any)
```

广播自定义的全局消息
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Message` | `string` | 广播信息的索引，后续的广播和监听都通过索引进行操作 |
| `...` | `any` | 自定义事件参数 |

### `UnListenMessage`

```text
UnListenMessage(Listener: UObject|number, Message: string)
```

解除监听对象以及全局的广播信息
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Listener` | `UObject\|number` | 监听对象/监听ID |
| `Message` | `string` | 广播信息的索引，后续的广播和监听都通过索引进行操作 |

### `RegisterUserDefinedMessage`

```text
RegisterUserDefinedMessage(Message: string) -> string
```

注册自定义消息
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Message` | `string` | 广播信息的索引，后续的广播和监听都通过索引进行操作 |

**Returns**

| Type | Description |
|---|---|
| `string` | 返回注册后的Message，与输入的Message相同 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81%E4%B8%8E%E8%83%8C%E5%8C%85/UGCGunSystem.json -->

# UGCGunSystem

枪械系统接口库

## Functions

### `StartFire`

```text
StartFire(Gun: STExtraShootWeapon)
```

开火
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

### `StopFire`

```text
StopFire(Gun: STExtraShootWeapon)
```

停止开火
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

### `EnableInfiniteBullets`

```text
EnableInfiniteBullets(Gun: STExtraShootWeapon, IsEnable: boolean)
```

启用/停用无限子弹（无需换弹）
启用后，弹夹容量无限，一直开火也无需换弹
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `IsEnable` | `boolean` | 启用/停用 |

### `EnableClipInfiniteBullets`

```text
EnableClipInfiniteBullets(Gun: STExtraShootWeapon, IsEnable: boolean)
```

启用/停用弹夹无限子弹（需要换弹一次）
启用后，子弹容量无限，开火会打空弹夹触发换弹
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `IsEnable` | `boolean` | 启用/停用 |

### `ForceReloadAndEnableInfiniteBullets`

```text
ForceReloadAndEnableInfiniteBullets(Gun: STExtraShootWeapon, IsEnable: boolean)
```

启用/停用无限子弹（无需换弹）并且强制换弹
启用后，强制换弹弹夹容量无限，一直开火也无需换弹，避免弹夹内子弹为0时触发检查
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `IsEnable` | `boolean` | 启用/停用 |

### `SetMaxBulletNumInOneClip`

```text
SetMaxBulletNumInOneClip(Gun: STExtraShootWeapon, MaxBulletNumInOneClip: number)
```

设置弹夹容量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `MaxBulletNumInOneClip` | `number` | 弹夹容量 |

### `GetMaxBulletNumInOneClip`

```text
GetMaxBulletNumInOneClip(Gun: STExtraShootWeapon) -> number
```

获取弹夹容量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 弹夹容量 |

### `SetBulletFireSpeed`

```text
SetBulletFireSpeed(Gun: STExtraShootWeapon, BulletFireSpeed: number)
```

设置子弹飞行速度
例：60000代表1秒飞行600米
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `BulletFireSpeed` | `number` | 飞行速度 |

### `GetBulletFireSpeed`

```text
GetBulletFireSpeed(Gun: STExtraShootWeapon) -> number
```

获取子弹飞行速度
例：60000代表1秒飞行600米
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 当前飞行速度 |

### `SetShootIntervalTime`

```text
SetShootIntervalTime(Gun: STExtraShootWeapon, ShootIntervalTime: number)
```

设置射击间隔时间
例：0.1代表0.1秒射击一次
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `ShootIntervalTime` | `number` | 射击间隔时间 |

### `GetShootIntervalTime`

```text
GetShootIntervalTime(Gun: STExtraShootWeapon) -> number
```

获取射击间隔时间
例：0.1代表0.1秒射击一次
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 射击间隔时间 |

### `SetBulletRange`

```text
SetBulletRange(Gun: STExtraShootWeapon, BulletRange: number)
```

设置子弹射程
例：60000射程为600米
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `BulletRange` | `number` | 子弹射程 |

### `GetBulletRange`

```text
GetBulletRange(Gun: STExtraShootWeapon) -> number
```

获取子弹射程
例：60000射程为600米
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 子弹射程 |

### `SetBulletBaseDamage`

```text
SetBulletBaseDamage(Gun: STExtraShootWeapon, BulletBaseDamage: number)
```

设置子弹基础伤害
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `BulletBaseDamage` | `number` | 基础伤害 |

### `GetBulletBaseDamage`

```text
GetBulletBaseDamage(Gun: STExtraShootWeapon) -> number
```

获取子弹基础伤害
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 基础伤害 |

### `SetBulletMinimumDamage`

```text
SetBulletMinimumDamage(Gun: STExtraShootWeapon, BulletMinimumDamage: number)
```

设置子弹最低伤害（子弹经过穿透，距离等衰减后）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `BulletMinimumDamage` | `number` | 最低伤害 |

### `GetBulletMinimumDamage`

```text
GetBulletMinimumDamage(Gun: STExtraShootWeapon) -> number
```

获取子弹最低伤害（子弹经过穿透，距离等衰减后）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 最低伤害 |

### `SetBulletImpulse`

```text
SetBulletImpulse(Gun: STExtraShootWeapon, BulletImpulse: number)
```

设置子弹命中冲量
冲量越大，击退击飞效果越大
参考：破片手雷最大造成冲量为2500
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `BulletImpulse` | `number` | 冲量 |

### `GetBulletImpulse`

```text
GetBulletImpulse(Gun: STExtraShootWeapon) -> number
```

获取子弹命中冲量
冲量越大，击退击飞效果越大
参考：破片手雷最大造成冲量为2500
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 冲量 |

### `SetReloadTime`

```text
SetReloadTime(Gun: STExtraShootWeapon, ReloadTime: number)
```

设置换弹时间
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `ReloadTime` | `number` | 换弹时间 |

### `GetReloadTime`

```text
GetReloadTime(Gun: STExtraShootWeapon) -> number
```

获取换弹时间                 
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 换弹时间 |

### `SetTacticalReloadTime`

```text
SetTacticalReloadTime(Gun: STExtraShootWeapon, TacticalReloadTime: number)
```

设置战术换弹时间（弹夹子弹数不为0）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `TacticalReloadTime` | `number` | 换弹时间 |

### `GetTacticalReloadTime`

```text
GetTacticalReloadTime(Gun: STExtraShootWeapon) -> number
```

获取战术换弹时间（弹夹子弹数不为0）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 换弹时间 |

### `SetVerticalRecoilScale`

```text
SetVerticalRecoilScale(Gun: STExtraShootWeapon, VerticalRecoilScale: number)
```

设置垂直后坐力倍率
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `VerticalRecoilScale` | `number` | 倍率 |

### `GetVerticalRecoilScale`

```text
GetVerticalRecoilScale(Gun: STExtraShootWeapon) -> number
```

获取垂直后坐力倍率
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 倍率 |

### `SetHorizontalRecoilScale`

```text
SetHorizontalRecoilScale(Gun: STExtraShootWeapon, HorizontalRecoilScale: number)
```

设置水平后坐力倍率
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `HorizontalRecoilScale` | `number` | 倍率 |

### `GetHorizontalRecoilScale`

```text
GetHorizontalRecoilScale(Gun: STExtraShootWeapon) -> number
```

获取水平后坐力倍率
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 倍率 |

### `SetDeviationScale`

```text
SetDeviationScale(Gun: STExtraShootWeapon, DeviationScale: number)
```

设置扩散值倍率
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `DeviationScale` | `number` | 倍率 |

### `GetDeviationScale`

```text
GetDeviationScale(Gun: STExtraShootWeapon) -> number
```

获取扩散值倍率
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `number` | 倍率 |

### `Reload`

```text
Reload(PlayerPawn: PlayerPawn)
```

玩家当前武器换弹
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

### `OpenScope`

```text
OpenScope(PlayerPawn: PlayerPawn, IsOpenScope: boolean)
```

玩家当前武器开镜/关镜
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `IsOpenScope` | `boolean` | 开镜/关镜 |

### `GetIsAutoAimEnabled`

```text
GetIsAutoAimEnabled(PlayerPawn: PlayerPawn) -> boolean
```

获取辅助瞄准是否启用 
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 启用/关闭 |

### `SetIsAutoAimEnabled`

```text
SetIsAutoAimEnabled(PlayerPawn: PlayerPawn, IsAutoAimEnabled: boolean)
```

设置自动瞄准是否启用 
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `IsAutoAimEnabled` | `boolean` | 启用/关闭 |

### `AddGunAttachment`

```text
AddGunAttachment(Gun: STExtraShootWeapon, ItemDefineID: ItemDefineID)
```

武器添加指定配件
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `ItemDefineID` | `ItemDefineID` | 物品DefineID |

### `CreateAndAddGunAttachment`

```text
CreateAndAddGunAttachment(Gun: STExtraShootWeapon, ItemID: number)
```

创建新配件并且直接添加到武器
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `ItemID` | `number` | 物品ID |

### `RemoveGunAttachmentBySocketType`

```text
RemoveGunAttachmentBySocketType(Gun: STExtraShootWeapon, SocketType: WeaponAttachmentSocketType)
```

卸载武器指定部位配件
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `SocketType` | `WeaponAttachmentSocketType` | 配件槽位 |

### `GetWeaponAttachmentIDBySocketType`

```text
GetWeaponAttachmentIDBySocketType(Gun: STExtraShootWeapon, SocketType: WeaponAttachmentSocketType) -> ItemDefineID
```

获取特定槽位的配件ItemDefineID
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `SocketType` | `WeaponAttachmentSocketType` | 配件槽位 |

**Returns**

| Type | Description |
|---|---|
| `ItemDefineID` | - |

### `GetAvailableWeaponAttachmentSocketTypeList`

```text
GetAvailableWeaponAttachmentSocketTypeList(Gun: STExtraShootWeapon) -> @AttachmentSocketType
```

获取枪械可用的配件槽位
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `@AttachmentSocketType` | 列表 |

### `GetAvailableWeaponAttachment`

```text
GetAvailableWeaponAttachment(Gun: STExtraShootWeapon) -> @AvailableWeaponAttachment
```

获取武器可用配件(需要武器加载出来才能使用，不能在武器初始化时调用)
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `@AvailableWeaponAttachment` | 列表 |

### `DisuseAllWeaponAttachmentsOnServer`

```text
DisuseAllWeaponAttachmentsOnServer(Gun: STExtraShootWeapon)
```

卸载武器所有配件
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

### `GetWeaponAllAttachmentIDList`

```text
GetWeaponAllAttachmentIDList(Gun: STExtraShootWeapon) -> @AttachmentDefineID
```

获取武器上的所有配件
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |

**Returns**

| Type | Description |
|---|---|
| `@AttachmentDefineID` | 列表 |

### `SetCurrentBulletNumInClip`

```text
SetCurrentBulletNumInClip(Gun: STExtraShootWeapon, Count: int)
```

设置武器弹匣内弹药
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Gun` | `STExtraShootWeapon` | 枪械 |
| `Count` | `int` | 枪械 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCInputSystem.json -->

# UGCInputSystem

输入系统接口库

## Functions

### `BindInputMapping`

```text
BindInputMapping(BindingOwner: UObject, InputTag: UGCGameplayTag|string|FGameplayTag, TriggerEvent: ETriggerEvent, CallbackFunction: fun(InputValue:float, ElapsedTime:float, TriggeredTime:float, InputTag:FGameplayTag) @事件触发回调函数) -> int32
```

绑定指定InputTag事件的回调函数
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BindingOwner` | `UObject` | 绑定输入事件的对象 |
| `InputTag` | `UGCGameplayTag\|string\|FGameplayTag` | 由Tag标识的输入事件 |
| `TriggerEvent` | `ETriggerEvent` | 输入事件类型 |
| `CallbackFunction` | `fun(InputValue:float, ElapsedTime:float, TriggeredTime:float, InputTag:FGameplayTag) @事件触发回调函数` | 事件触发回调函数 |

**Returns**

| Type | Description |
|---|---|
| `int32` | 输入事件绑定的索引，-1时为绑定失败 |

### `RemoveBindingToObject`

```text
RemoveBindingToObject(BindingOwner: UObject)
```

解除与目标Object所有相关的输入事件绑定
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BindingOwner` | `UObject` | 绑定输入事件的对象 |

### `RemoveBinding`

```text
RemoveBinding(WorldContext: UObject, InputBindingHandle: int32)
```

解除指定索引的输入事件绑定
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `InputBindingHandle` | `int32` | 输入事件绑定的索引 |

### `InjectInputMapping`

```text
InjectInputMapping(WorldContext: UObject, InputTag: UGCGameplayTag|string|FGameplayTag, Value: float)
```

通过脚本手动触发某个InputTag
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `InputTag` | `UGCGameplayTag\|string\|FGameplayTag` | 由Tag标识的输入事件 |
| `Value` | `float` | 输入事件的值 |

### `SetBindingConsumeInput`

```text
SetBindingConsumeInput(WorldContext: UObject, InputBindingHandle: int32, bConsumeInput: bool)
```

设置某个输入事件绑定是否消耗输入，消耗输入后，后续的其他输入事件绑定将不被触发
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `InputBindingHandle` | `int32` | 输入事件绑定的索引 |
| `bConsumeInput` | `bool` | 是否消耗Input |

### `GetInputValue`

```text
GetInputValue(WorldContext: UObject, InputTag: UGCGameplayTag|string|FGameplayTag) -> float
```

获取指定InputTag对应Input的当前值
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `InputTag` | `UGCGameplayTag\|string\|FGameplayTag` | 由Tag标识的输入事件 |

**Returns**

| Type | Description |
|---|---|
| `float` | Input当前值，未找到时返回0 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81%E4%B8%8E%E8%83%8C%E5%8C%85/UGCItemSystem.json -->

# UGCItemSystem

道具系统接口库

## Functions

### `GetItemType`

```text
GetItemType(ItemID: number) -> number
```

获取物品ItemType
对应表格数据：和平精英\表格\物品表中ItemType列
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品类型 |

### `GetItemSubType`

```text
GetItemSubType(ItemID: number) -> number
```

获取ItemSubType
对应表格数据：和平精英\表格\物品表中ItemSubType列
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品子类型 |

### `GetItemData`

```text
GetItemData(ItemID: number) -> FBattleItem_TabRes
```

获取道具数据
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `FBattleItem_TabRes` | 物品数据 |

### `IsUGCItem`

```text
IsUGCItem(ItemID: number) -> boolean
```

是否为绿洲物品（物资编辑器中自定义物品）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为绿洲物品 |

### `IsCanUseInBackpack`

```text
IsCanUseInBackpack(ItemID: number) -> boolean
```

返回道具在背包中是否可以使用
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否可以使用 |

### `GetPickupWrapperClassPath`

```text
GetPickupWrapperClassPath(ItemID: number) -> string
```

通过ItemID获取Wrapper路径
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `string` | Wrapper路径 |

### `SetWrapperToGround`

```text
SetWrapperToGround(WrapperActor: APickUpWrapperActor) -> boolean
```

将Wrapper设置贴在地面
Wrapper.bDropedByPlayer为True时，贴地功能生效
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WrapperActor` | `APickUpWrapperActor` | 可拾取物 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetWrapperItemID`

```text
GetWrapperItemID(WrapperActor: APickUpWrapperActor) -> number
```

获取Wrapper关联的ItemID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WrapperActor` | `APickUpWrapperActor` | 可拾取物 |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品ID |

### `ModifyWrapperItemCount`

```text
ModifyWrapperItemCount(WrapperActor: APickUpWrapperActor, Count: number) -> boolean
```

修改Wrpaaer中物品的数量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WrapperActor` | `APickUpWrapperActor` | 可拾取物 |
| `Count` | `number` | 修改后的数量 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `DoPickWrapper`

```text
DoPickWrapper(PlayerPawn: PlayerPawn, WrapperActor: APickUpWrapperActor) -> boolean
```

拾取Wrapper
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | - |
| `WrapperActor` | `APickUpWrapperActor` | 可拾取物 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `IsWrapperDropedByPlayer`

```text
IsWrapperDropedByPlayer(WrapperActor: APickUpWrapperActor) -> boolean
```

Wrapper是否是由玩家丢弃生成
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WrapperActor` | `APickUpWrapperActor` | 可拾取物 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `SetWrapperPickUpRadius`

```text
SetWrapperPickUpRadius(WrapperActor: APickUpWrapperActor, Radius: number) -> boolean
```

设置Wrapper的可拾取范围
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WrapperActor` | `APickUpWrapperActor` | 可拾取物 |
| `Radius` | `number` | 可拾取范围，单位厘米 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetQualityTexturePath`

```text
GetQualityTexturePath(QualityRank: number) -> string
```

获取品质色的128*128纹理路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QualityRank` | `number` | 品质等级 |

**Returns**

| Type | Description |
|---|---|
| `string` | 品质纹理路径 |

### `GetBigQualityTexturePath`

```text
GetBigQualityTexturePath(QualityRank: number) -> string
```

获取品质色的128*256纹理路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QualityRank` | `number` | 品质等级 |

**Returns**

| Type | Description |
|---|---|
| `string` | 品质纹理路径string |

### `GetQualityBarTexturePath`

```text
GetQualityBarTexturePath(QualityRank: number) -> string
```

获取品质色条纹理路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QualityRank` | `number` | 品质等级 |

**Returns**

| Type | Description |
|---|---|
| `string` | 品质纹理路径string |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81%E4%B8%8E%E8%83%8C%E5%8C%85/UGCItemSystemV2.json -->

# UGCItemSystemV2

V2道具系统接口库

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCItemSystemV2._GetterOverrides` | `-` | 存储外部注册的 Get 重写委托 key: 函数名（如 "GetItemNameV2ByDefineID"）, value: 重写函数 @type table |

## Functions

### `RegisterItemPropertyGetOverride`

```text
RegisterItemPropertyGetOverride(Key: EItemOverrideKey) -> boolean
```

注册物品属性读取函数
生效范围：服务器&客户端分别注册

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `EItemOverrideKey` | 属性枚举值，使用 EItemOverrideKey.XXX |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否注册成功 |

### `UnregisterItemPropertyGetOverride`

```text
UnregisterItemPropertyGetOverride(Key: EItemOverrideKey|nil) -> boolean
```

注销物品属性读取函数
生效范围：服务器&客户端分别反注册

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `EItemOverrideKey\|nil` | 属性枚举值，使用 EItemOverrideKey.XXX；不传则清除所有 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否注销成功 |

### `GetConfigItemHandle`

```text
GetConfigItemHandle(ItemID: number) -> UBattleItemHandleBase
```

获取物品 ItemHandle 配置
可以通过它取得所有物品中配置的数据（只读）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `UBattleItemHandleBase` | 配置数据 |

### `GetItemInstanceDataManager`

```text
GetItemInstanceDataManager() -> UUGCBattleItemInstanceDataManager
```

获取物品实例数据管理器
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `UUGCBattleItemInstanceDataManager` | 实例数据管理器 |

### `IsUGCItemV2`

```text
IsUGCItemV2(ItemID: number) -> boolean
```

是否为绿洲物品（物资编辑器中自定义物品）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为绿洲物品 |

### `IsShouldPersist`

```text
IsShouldPersist(ItemID: number) -> boolean
```

是否持久化
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否持久化 |

### `IsObjEditorItemV2`

```text
IsObjEditorItemV2(ItemID: number) -> boolean
```

是否为V2版本物编创建的物品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为V2版本物编创建的物品 |

### `GetItemNameV2`

```text
GetItemNameV2(ItemID: number) -> string
```

返回物品名称
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品名称 |

### `GetItemNameV2ByDefineID`

```text
GetItemNameV2ByDefineID(ItemDefineID: FItemDefineID) -> string
```

返回物品名称（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品名称 |

### `GetItemSubTypeV2`

```text
GetItemSubTypeV2(ItemID: number) -> number
```

返回物品子类型SubType，(比如武器类别为1，M146子类型为101)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品子类型 |

### `GetItemIconTextureV2`

```text
GetItemIconTextureV2(ItemID: number) -> FSoftObjectPath
```

返回物品图标路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 物品图标路径 |

### `GetItemIconTextureV2ByDefineID`

```text
GetItemIconTextureV2ByDefineID(ItemDefineID: FItemDefineID) -> FSoftObjectPath
```

返回物品图标路径（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 物品图标路径 |

### `GetOwnBackpackComponent`

```text
GetOwnBackpackComponent(ItemHandle: UBattleItemHandleBase) -> BackpackComponentV2
```

读取物品所在背包
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemHandle` | `UBattleItemHandleBase` | 物品 Handle |

**Returns**

| Type | Description |
|---|---|
| `BackpackComponentV2` | V2背包组件 |

### `GetItemIconWithPlayerSkinV2`

```text
GetItemIconWithPlayerSkinV2(ItemID: number, PlayerController: PlayerController) -> FSoftObjectPath
```

返回物品图标路径(带玩家皮肤)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |
| `PlayerController` | `PlayerController` | 玩家 PlayerController |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 物品图标路径 |

### `GetItemIconWithPlayerSkinV2ByDefineID`

```text
GetItemIconWithPlayerSkinV2ByDefineID(ItemDefineID: FItemDefineID, PlayerController: PlayerController) -> FSoftObjectPath
```

返回物品图标路径(带玩家皮肤)（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |
| `PlayerController` | `PlayerController` | 玩家 PlayerController |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 物品图标路径 |

### `GetWhiteIconTextureV2`

```text
GetWhiteIconTextureV2(ItemID: number) -> FSoftObjectPath
```

返回物品剪影图标路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 剪影图标路径 |

### `GetWhiteIconTextureV2ByDefineID`

```text
GetWhiteIconTextureV2ByDefineID(ItemDefineID: FItemDefineID) -> FSoftObjectPath
```

返回物品剪影图标路径（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 剪影图标路径 |

### `GetBigIconTextureV2`

```text
GetBigIconTextureV2(ItemID: number) -> FSoftObjectPath
```

返回物品装备栏图标路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 装备栏图标路径 |

### `GetBigIconTextureV2ByDefineID`

```text
GetBigIconTextureV2ByDefineID(ItemDefineID: FItemDefineID) -> FSoftObjectPath
```

返回物品装备栏图标路径（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 装备栏图标路径 |

### `GetBigIconTextureWithPlayerSkinV2`

```text
GetBigIconTextureWithPlayerSkinV2(ItemID: number, PlayerController: PlayerController) -> FSoftObjectPath
```

返回物品装备栏图标路径(带玩家皮肤)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |
| `PlayerController` | `PlayerController` | 玩家 PlayerController |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 装备栏图标路径 |

### `GetBigIconTextureWithPlayerSkinV2ByDefineID`

```text
GetBigIconTextureWithPlayerSkinV2ByDefineID(ItemDefineID: FItemDefineID, PlayerController: PlayerController) -> FSoftObjectPath
```

返回物品装备栏图标路径(带玩家皮肤)（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |
| `PlayerController` | `PlayerController` | 玩家 PlayerController |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 装备栏图标路径 |

### `GetItemDetailV2`

```text
GetItemDetailV2(ItemID: number) -> string
```

返回物品详情
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品详情 |

### `GetItemDetailV2ByDefineID`

```text
GetItemDetailV2ByDefineID(ItemDefineID: FItemDefineID) -> string
```

返回物品详情（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品详情 |

### `GetItemPickupDetailV2`

```text
GetItemPickupDetailV2(ItemID: number) -> string
```

返回物品拾取描述
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品拾取描述 |

### `GetItemPickupDetailV2ByDefineID`

```text
GetItemPickupDetailV2ByDefineID(ItemDefineID: FItemDefineID) -> string
```

返回物品拾取描述（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品拾取描述 |

### `ItemHasTagV2`

```text
ItemHasTagV2(ItemID: number, Tag: string) -> boolean
```

是否含有某个 Tag
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |
| `Tag` | `string` | 物品 Tag |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否含有 Tag |

### `GetItemTagsV2`

```text
GetItemTagsV2(ItemID: number) -> string[]
```

返回物品所有 Tag
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `string[]` | 物品所有 Tag |

### `ItemCanDropV2`

```text
ItemCanDropV2(ItemID: number) -> boolean
```

返回物品是否可丢弃
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 物品是否可丢弃 |

### `ItemCanRemoveV2`

```text
ItemCanRemoveV2(ItemID: number) -> boolean
```

返回物品是否可销毁
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 物品是否可销毁 |

### `IsCanUseV2`

```text
IsCanUseV2(ItemID: number) -> boolean
```

返回物品在背包中是否可以使用
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否可以使用 |

### `GetItemMaxNumberOfStacksV2`

```text
GetItemMaxNumberOfStacksV2(ItemID: number) -> number
```

返回物品最大堆叠数量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品最大堆叠数量 |

### `GetItemQualityV2`

```text
GetItemQualityV2(ItemID: number) -> number
```

返回物品品质
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品品质 |

### `GetItemQualityV2ByDefineID`

```text
GetItemQualityV2ByDefineID(ItemDefineID: FItemDefineID) -> number
```

返回物品品质（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品品质 |

### `GetItemCustomizedTypeV2`

```text
GetItemCustomizedTypeV2(ItemID: number) -> string
```

返回物品自定义类型
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品自定义类型 |

### `LoadItemCustomData`

```text
LoadItemCustomData(ItemDefineID: FItemDefineID) -> table
```

获取物品自定义实例化数据
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品DefineID |

**Returns**

| Type | Description |
|---|---|
| `table` | 物品自定义实例化数据table |

### `SaveItemCustomData`

```text
SaveItemCustomData(ItemDefineID: FItemDefineID, ItemCustomData: table) -> boolean
```

保存物品自定义实例化数据
注意: 实例数据也包含了和平内置数据，应避免直接覆盖，采用下述方式添加数据
local CustomData = UGCItemSystemV2.LoadItemCustomData(ItemDefineID)
CustomData.NewKey = NewTableData -- 填充新的数据
UGCItemSystemV2.SaveItemCustomData(ItemDefineID, CustomData)
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品DefineID |
| `ItemCustomData` | `table` | 物品自定义实例化数据table |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 保存成功or失败 |

### `GetItemDefineID`

```text
GetItemDefineID(ItemID: number) -> FItemDefineID
```

通过物品ID创建一个全新的物品实例，并返回 DefineID
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `FItemDefineID` | 物品 DefineID |

### `SetItemCommonReason`

```text
SetItemCommonReason(ItemDefineID: FItemDefineID, Reason: number)
```

设置物品通用 Reason
用于操作物品时指定其中一些行为
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |
| `Reason` | `number` | Reason |

### `GetItemCommonReason`

```text
GetItemCommonReason(ItemDefineID: FItemDefineID) -> number
```

获取物品通用 Reason
用于操作物品时指定其中一些行为
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `number` | Reason |

### `GetEquipTargetSlots`

```text
GetEquipTargetSlots(ItemID: number) -> string[]
```

获取装备物品拥有的槽位列表
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `string[]` | 物品拥有的所有槽位 |

### `GetDisplayNameBySlotName`

```text
GetDisplayNameBySlotName(ItemID: number, SlotName: string) -> string
```

获取槽位对应的展示名
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |
| `SlotName` | `string` | 槽位名 |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品槽位的展示名称 |

### `GetAttachTargetItem`

```text
GetAttachTargetItem(ItemDefineID: ItemDefineID) -> bool,ItemDefineID,FName
```

获取物品附加在哪个物品上
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `ItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `bool,ItemDefineID,FName` | 物品是否正附加在另一个物品上,物品附加的目标物品 DefineID,物品附加的目标物品槽位 |

### `GetAttachChildItem`

```text
GetAttachChildItem(AttachParentID: ItemDefineID, AttachSlot: string) -> ItemDefineID
```

获取附加在物品上的子物品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttachParentID` | `ItemDefineID` | 父物品的 DefineID |
| `AttachSlot` | `string` | 父物品的槽位名 |

**Returns**

| Type | Description |
|---|---|
| `ItemDefineID` | 附加在此槽位上的子物品 DefineID |

### `GetAttachChildrenItem`

```text
GetAttachChildrenItem(AttachParentID: ItemDefineID) -> ItemDefineID[]
```

获取所有附加在物品上的子物品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttachParentID` | `ItemDefineID` | 父物品的 DefineID |

**Returns**

| Type | Description |
|---|---|
| `ItemDefineID[]` | 所有子物品 DefineID, 数组元素与父物品槽位一一对应，可能存在无效的 ItemDefineID |

### `GetAttachAllowSlots`

```text
GetAttachAllowSlots(AttachParentID: number, AttachChildID: number) -> string[]
```

获取子物品可以 Attach 到父物品的哪些 Slot(不考虑槽位启用状态)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttachParentID` | `number` | 父物品的 ItemID |
| `AttachChildID` | `number` | 子物品的 ItemID |

**Returns**

| Type | Description |
|---|---|
| `string[]` | 所有可装备槽位 FName |

### `GetAttachAllowSlotsByDefineID`

```text
GetAttachAllowSlotsByDefineID(Player: PlayerPawn, AttachParentDefineID: ItemDefineID, AttachChildID: number) -> string[]
```

获取子物品可以 Attach 到父物品`实例` 的哪些 Slot(考虑槽位启用状态)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn` | 玩家 |
| `AttachParentDefineID` | `ItemDefineID` | 父物品的 ItemDefineID |
| `AttachChildID` | `number` | 子物品的 ItemID |

**Returns**

| Type | Description |
|---|---|
| `string[]` | 所有可装备槽位 FName |

### `GetQualityTexturePath`

```text
GetQualityTexturePath(QualityRank: number) -> string
```

获取品质色的128*128纹理路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QualityRank` | `number` | 品质等级 |

**Returns**

| Type | Description |
|---|---|
| `string` | 品质纹理路径 |

### `GetBackpackSimpleNameV2`

```text
GetBackpackSimpleNameV2(ItemID: number) -> string
```

返回物品背包简述
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品背包简写 |

### `GetBackpackSimpleNameV2ByDefineID`

```text
GetBackpackSimpleNameV2ByDefineID(ItemDefineID: FItemDefineID) -> string
```

返回物品背包简述（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品背包简写 |

### `GetBigQualityTexturePath`

```text
GetBigQualityTexturePath(QualityRank: number) -> string
```

获取品质色的128*256纹理路径(废弃，结果同GetQualityTexturePath)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QualityRank` | `number` | 品质等级 |

**Returns**

| Type | Description |
|---|---|
| `string` | 品质纹理路径string |

### `GetQualityBarTexturePath`

```text
GetQualityBarTexturePath(QualityRank: number) -> string
```

获取品质色条纹理路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QualityRank` | `number` | 品质等级 |

**Returns**

| Type | Description |
|---|---|
| `string` | 品质纹理路径string |

### `GetEquipmentQualityTexturePath`

```text
GetEquipmentQualityTexturePath(QualityRank: number) -> string
```

获取装备品质色条纹理路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QualityRank` | `number` | 品质等级 |

**Returns**

| Type | Description |
|---|---|
| `string` | 品质纹理路径string |

### `GetWeaponSlotAttachItemIDs`

```text
GetWeaponSlotAttachItemIDs(ItemID: number, SlotName: string) -> number[]
```

获取武器配件槽位可用配件的物品ID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 武器的物品ID |
| `SlotName` | `string` | 武器槽位名 |

**Returns**

| Type | Description |
|---|---|
| `number[]` | 可用的配件物品ID |

### `GetPickupWrapperListByItemID`

```text
GetPickupWrapperListByItemID(ItemID: number) -> AUGCPickUpWrapperActor[]
```

根据物品ID查询拾取物
生效范围：服务器&客户端, 客户端仅查询本地生成的

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `AUGCPickUpWrapperActor[]` | 拾取物列表 |

### `GetPickupWrapperListByCustomType`

```text
GetPickupWrapperListByCustomType(CustomType: string) -> AUGCPickUpWrapperActor[]
```

根据自定义类型查询拾取物
生效范围：服务器&客户端, 客户端仅查询本地生成的

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CustomType` | `string` | 自定义类型 |

**Returns**

| Type | Description |
|---|---|
| `AUGCPickUpWrapperActor[]` | 拾取物列表 |

### `GetPickupWrapperListByItemTag`

```text
GetPickupWrapperListByItemTag(ItemTag: string) -> AUGCPickUpWrapperActor[]
```

根据物品Tag查询拾取物
生效范围：服务器&客户端, 客户端仅查询本地生成的

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemTag` | `string` | 物品Tag |

**Returns**

| Type | Description |
|---|---|
| `AUGCPickUpWrapperActor[]` | 拾取物列表 |

### `SetEquipSlotEnable`

```text
SetEquipSlotEnable(DefineID: FItemDefineID, SlotName: string)
```

启用物品槽位
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `FItemDefineID` | 物品DefineID |
| `SlotName` | `string` | 槽位名 |

### `GetEquipSlotEnable`

```text
GetEquipSlotEnable(DefineID: FItemDefineID, SlotName: string) -> boolean
```

获取物品槽位是否启用
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `FItemDefineID` | 物品DefineID |
| `SlotName` | `string` | 槽位名 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否启用 |

### `StartCustomizeDrop`

```text
StartCustomizeDrop(DropLocation: FVector, ProduceID: number, ProduceGroupID: number, EntityType: EUGCGenerateItemEntityType, RelatedPlayer: PlayerPawn, DropActorClass: UClass)
```

指定掉落方案进行一次 Wrapper 掉落
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DropLocation` | `FVector` | 掉落中心点 |
| `ProduceID` | `number` | 掉落方案ID |
| `ProduceGroupID` | `number` | 掉落组方案ID(掉落组ID不为-1，掉落组ID生效。掉落组ID为-1,则掉落ID生效) |
| `EntityType` | `EUGCGenerateItemEntityType` | 掉落物类型(可缺省，默认为Wrapper) |
| `RelatedPlayer` | `PlayerPawn` | 当掉落物方向为面相玩家时必须，当掉落物类型为进入背包时必须，其他时候可以为nil |
| `DropActorClass` | `UClass` | 掉落主体Actor类型，应继承自 UGCDropActor_BP, 可以为nil。通过创建自定义蓝图，配置掉落详细参数（掉落间隔、随机掉落范围等等）。 |

### `FindAllNearPickupItemData`

```text
FindAllNearPickupItemData(PlayerPawn: PlayerPawn) -> FUGCPickupItemData[]
```

找到所有玩家角色附近的地面拾取物
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `FUGCPickupItemData[]` | 地面拾取物信息 |

### `FindPickupWrapperActorByRange`

```text
FindPickupWrapperActorByRange(Center: FVector, DistanceRange: number) -> APickUpWrapperActor[]
```

查找指定距离范围内的地面拾取物
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Center` | `FVector` | 中心点坐标 |
| `DistanceRange` | `number` | 查找距离 |

**Returns**

| Type | Description |
|---|---|
| `APickUpWrapperActor[]` | 地面拾取物Actor |

### `TryPickupWrapperItem`

```text
TryPickupWrapperItem(PlayerPawn: PlayerPawn, TargetWrapper: AActor, ItemDefineID: FItemDefineID, PickupCount: number, CheckPickupCondition: boolean)
```

玩家角色尝试拾取地面物品（不播拾取动作）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `TargetWrapper` | `AActor` | 目标地面拾取物 |
| `ItemDefineID` | `FItemDefineID` | 要拾取的物品 DefineID，可缺省，默认取 TargetWrapper 中的物品实例数据 |
| `PickupCount` | `number` | 拾取数量，可缺省，默认拾取1个 |
| `CheckPickupCondition` | `boolean` | 是否检查拾取条件(距离、是否穿墙等)，可缺省，默认为 true |

### `SpawnPickupWrapper`

```text
SpawnPickupWrapper(Location: FVector, ItemID: number, Count: number, CustomData: table) -> APickUpWrapperActor
```

创建地面拾取物
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Location` | `FVector` | 创建位置 |
| `ItemID` | `number` | 拾取物物品ID |
| `Count` | `number` | 拾取物物品数量 |
| `CustomData` | `table` | 物品自定义实例化数据(可缺省，默认无自定义实例化数据) |

**Returns**

| Type | Description |
|---|---|
| `APickUpWrapperActor` | 地面拾取物Actor |

### `GetUGCPickUpListComponent`

```text
GetUGCPickUpListComponent(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器) -> @UUGCPickUpListComponent
```

获取拾取组件(客户端）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `@UUGCPickUpListComponent` | UGC拾取组件组件 |

### `PauseAutoPick`

```text
PauseAutoPick(InPlayer: PlayerPawn | PlayerController | nil @可选，玩家角色或控制器，不传则自动获取)
```

暂停指定物品的自动拾取
生效范围：客户端
优先使用新拾取组件，若不存在则走经典面板逻辑

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPlayer` | `PlayerPawn \| PlayerController \| nil @可选，玩家角色或控制器，不传则自动获取` | 可选，玩家角色或控制器，不传则自动获取 |

### `StopPick`

```text
StopPick(InPlayer: PlayerPawn | PlayerController | nil @可选，玩家角色或控制器，不传则自动获取)
```

停止拾取（清空拾取列表，关闭数据更新）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPlayer` | `PlayerPawn \| PlayerController \| nil @可选，玩家角色或控制器，不传则自动获取` | 可选，玩家角色或控制器，不传则自动获取 |

### `StartPick`

```text
StartPick(InPlayer: PlayerPawn | PlayerController | nil @可选，玩家角色或控制器，不传则自动获取)
```

开始拾取（开启数据更新）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPlayer` | `PlayerPawn \| PlayerController \| nil @可选，玩家角色或控制器，不传则自动获取` | 可选，玩家角色或控制器，不传则自动获取 |

### `GetHeadDamageReduceV2`

```text
GetHeadDamageReduceV2(ItemID: number) -> number
```

返回外显装备头部减伤属性（仅支持ItemID，如需FItemDefineID请使用GetHeadDamageReduceV2ByDefineID）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 头部减伤值 |

### `GetHeadDamageReduceV2ByDefineID`

```text
GetHeadDamageReduceV2ByDefineID(ItemDefineID: FItemDefineID) -> number
```

返回外显装备头部减伤属性（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `number` | 头部减伤值 |

### `GetBodyDamageReduceV2`

```text
GetBodyDamageReduceV2(ItemID: number) -> number
```

返回外显装备身体减伤属性（仅支持ItemID，如需FItemDefineID请使用GetBodyDamageReduceV2ByDefineID）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 身体减伤值 |

### `GetBodyDamageReduceV2ByDefineID`

```text
GetBodyDamageReduceV2ByDefineID(ItemDefineID: FItemDefineID) -> number
```

返回外显装备身体减伤属性（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `number` | 身体减伤值 |

### `GetItemLevelV2`

```text
GetItemLevelV2(ItemID: number) -> number
```

返回物品等级（仅支持ItemID，如需FItemDefineID请使用GetItemLevelV2ByDefineID）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品等级 |

### `GetItemLevelV2ByDefineID`

```text
GetItemLevelV2ByDefineID(ItemDefineID: FItemDefineID) -> number
```

返回物品等级（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品等级 |

### `GetBackpackCellV2`

```text
GetBackpackCellV2(ItemID: number) -> number
```

返回物品背包格子数（仅支持ItemID，如需FItemDefineID请使用GetBackpackCellV2ByDefineID）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 背包格子数 |

### `GetBackpackCellV2ByDefineID`

```text
GetBackpackCellV2ByDefineID(ItemDefineID: FItemDefineID) -> number
```

返回物品背包格子数（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `number` | 背包格子数 |

### `GetNewDurabilityV2ByDefineID`

```text
GetNewDurabilityV2ByDefineID(ItemDefineID: FItemDefineID) -> number
```

返回物品当前耐久度（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品耐久度 |

### `GetPickupWrapperMeshPathV2`

```text
GetPickupWrapperMeshPathV2(ItemID: number) -> string
```

返回物品拾取包装体模型路径（仅支持ItemID，如需FItemDefineID请使用GetPickupWrapperMeshPathV2ByDefineID）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品 ID |

**Returns**

| Type | Description |
|---|---|
| `string` | 拾取包装体模型路径 |

### `GetPickupWrapperMeshPathV2ByDefineID`

```text
GetPickupWrapperMeshPathV2ByDefineID(ItemDefineID: FItemDefineID) -> string
```

返回物品拾取包装体模型路径（支持FItemDefineID，优先读取重写委托，其次读取非实例接口）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `string` | 拾取包装体模型路径 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9C%BA%E6%99%AF%E4%B8%8E%E7%8E%AF%E5%A2%83/UGCLevelFlowSystem.json -->

# UGCLevelFlowSystem

关卡流程系统接口库

## Functions

### `EnableLevelFlow`

```text
EnableLevelFlow(InMgrPath: string)
```

启用关卡流程
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMgrPath` | `string` | 需要注册的 GameModeActorMgr 的路径 |

### `GoToNextLevelForAllPlayers`

```text
GoToNextLevelForAllPlayers() -> boolean
```

当前关卡所有玩家直接跳转到下个关卡，需所有玩家都已达到通关条件
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `boolean` | 所有玩家跳转到下个关卡是否成功 |

### `GoToNextLevelForOnePlayer`

```text
GoToNextLevelForOnePlayer(PlayerController: ASTExtraPlayerController) -> boolean
```

单个玩家直接跳转到下个关卡，需当前玩家已达到通关条件，当前队伍其他玩家仍停留在当前关卡
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `ASTExtraPlayerController` | 玩家 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当前玩家跳转到下个关卡是否成功 |

### `LevelAddScore`

```text
LevelAddScore(TeamID: number, Score: number)
```

给指定队伍关卡加分
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |
| `Score` | `number` | 加分的分数 |

### `LevelSettle`

```text
LevelSettle(TeamID: number, IsFinish: boolean)
```

队伍所在关卡立即结算
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 结算的队伍 |
| `IsFinish` | `boolean` | 是否通关 |

### `GetCurrentLevelStage`

```text
GetCurrentLevelStage(PlayerController: ASTExtraPlayerController) -> number
```

获取当前玩家处于第几关
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `ASTExtraPlayerController` | 玩家 |

**Returns**

| Type | Description |
|---|---|
| `number` | 当前玩家处于第几关 |

### `GetTotalLevelCount`

```text
GetTotalLevelCount() -> number
```

获取总关卡数，随机切换关卡暂时不支持获取总关卡数，需要自定义逻辑
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `number` | 总关卡数 |

### `GameAddScore`

```text
GameAddScore(TeamID: number, Score: number)
```

给指定队伍游戏加分
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |
| `Score` | `number` | 加分的分数 |

### `GameSettle`

```text
GameSettle(IsFinish: boolean)
```

游戏立即结算
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsFinish` | `boolean` | 是否通关 |

### `GetAllPlayerControllerInCurrentLevel`

```text
GetAllPlayerControllerInCurrentLevel() -> APlayerController[]
```

获取关卡里的所有玩家
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `APlayerController[]` | 玩家列表 |

### `GetCurrentLevelActor`

```text
GetCurrentLevelActor() -> UGCLevelActor
```

获取当前副本
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `UGCLevelActor` | 关卡Actor |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCMailSystem.json -->

# UGCMailSystem

邮件系统库

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCMailSystem.MailListUpdateDelegate` | `-` | 玩家邮件列表更新时触发<br>非PIE时，仅在玩家刚进入玩法时触发一次，玩家在局内时后台发送的邮件，会在下一局进入时更新<br>@param UID int @UID<br>@param MailList UGCMailInfo[] @邮件列表 |
| `UGCMailSystem.ClaimMailsResultDelegate` | `-` | 收到领取邮件奖励结果后触发 @param UID int @UID @param ItemList table @奖励物品列表 @param ClaimedMailIDs int[] @已领取的邮件ID数组 @param FailedResults table @失败邮件 |
| `UGCMailSystem.ReadMailsResultDelegate` | `-` | 收到标记邮件已阅读结果后触发 @param UID int @UID @param ReadMailIDs int[] @已阅读的邮件ID数组 @param FailedResults table @失败邮件 |
| `UGCMailSystem.DeleteReadMailsResultDelegate` | `-` | 收到删除已读邮件结果后触发 @param UID int @UID @param DeletedMailIDs int[] @已删除的邮件ID数组 @param FailedResults table @失败邮件 |

## Functions

### `IsMailSystemEnabled`

```text
IsMailSystemEnabled() -> boolean
```

获取邮件系统是否开启，PIE下默认开启
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `boolean` | 邮件系统是否开启 |

### `GetMailList`

```text
GetMailList(UID: int) -> UGCMailInfo[]
```

获取指定玩家的邮件列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `int` | UID |

**Returns**

| Type | Description |
|---|---|
| `UGCMailInfo[]` | 邮件列表 |

### `GetMailInfo`

```text
GetMailInfo(UID: int, MailID: int) -> UGCMailInfo
```

获取指定玩家的邮件信息
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `int` | UID |
| `MailID` | `int` | 邮件ID |

**Returns**

| Type | Description |
|---|---|
| `UGCMailInfo` | 邮件信息，如果不存在则返回 nil |

### `ClaimMailAward`

```text
ClaimMailAward(UID: int, MailIDs: int[])
```

请求领取指定玩家的邮件奖励
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `int` | UID |
| `MailIDs` | `int[]` | 邮件ID数组 |

### `ReadMail`

```text
ReadMail(UID: int, MailIDs: int[])
```

请求标记指定玩家的邮件已读
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `int` | UID |
| `MailIDs` | `int[]` | 邮件ID数组 |

### `DeleteReadMail`

```text
DeleteReadMail(UID: int, MailIDs: int[])
```

请求删除指定玩家的已读邮件
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `int` | UID |
| `MailIDs` | `int[]` | 邮件ID数组 |

### `PIESendMail`

```text
PIESendMail(UID: int, Title: string, Content: string, ExpireTime: int, Attachments: table)
```

发送邮件, 仅PIE环境有效
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `int` | UID |
| `Title` | `string` | 邮件标题 |
| `Content` | `string` | 邮件内容 |
| `ExpireTime` | `int` | 过期时间 |
| `Attachments` | `table` | 附件 {[ItemID]=Count, ...} |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/UI%20%E7%95%8C%E9%9D%A2/UGCMapMarkManagerSystem.json -->

# UGCMapMarkManagerSystem

地图标记管理器系统接口库

## Functions

### `AddCustomMark`

```text
AddCustomMark(WidgetClassPath: string, RangeType: EMarkDispatchRange, RangeRad: number, OwnerPlayerState: PlayerState) -> number
```

添加一个自定义 Mark，需要自行管理位置（Widget 需继承自 MapUIMarkBaseWidget）
必须先调用一次 UpdateMarkLocation，调用 GetMarkLocation 才有效（Rotation 同理）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetClassPath` | `string` | 控件类路径，Widget 需继承自 MapUIMarkBaseWidget |
| `RangeType` | `EMarkDispatchRange` | 标记同步范围 |
| `RangeRad` | `number` | 标记显示范围，超出范围不会显示标记（目标实际距离，单位：cm） |
| `OwnerPlayerState` | `PlayerState` | 同步相关性 PlayerState，主要用于仅同步自身或者队友同步，非必传 |

**Returns**

| Type | Description |
|---|---|
| `number` | 标记 ID |

### `AddLocalCustomMark`

```text
AddLocalCustomMark(WidgetClassPath: string, RangeRad: number) -> number
```

添加一个自定义 Mark，需要自行管理位置（Widget 需继承自 MapUIMarkBaseWidget）
必须先调用一次 UpdateMarkLocation，调用 GetMarkLocation 才有效（Rotation 同理）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetClassPath` | `string` | 控件类路径，Widget 需继承自 MapUIMarkBaseWidget |
| `RangeRad` | `number` | 标记显示范围，超出范围不会显示标记（目标实际距离，单位：cm） |

**Returns**

| Type | Description |
|---|---|
| `number` | 标记 ID |

### `AddPlayerMark`

```text
AddPlayerMark(WidgetClassPath: string, RangeType: EMarkDispatchRange, RangeRad: number, OwnerPlayerState: PlayerState) -> number
```

添加一个玩家 Mark，会根据玩家位置实时更新位置。（Widget 需继承自 UGCMapUIMarkDynamicWidget）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetClassPath` | `string` | 控件类路径，Widget 需继承自 UGCMapUIMarkDynamicWidget |
| `RangeType` | `EMarkDispatchRange` | 标记同步范围 |
| `RangeRad` | `number` | 标记显示范围，超出范围不会显示标记（目标实际距离，单位：cm） |
| `OwnerPlayerState` | `PlayerState` | 标记目标 PlayerState |

**Returns**

| Type | Description |
|---|---|
| `number` | 标记 ID |

### `AddLocalPlayerMark`

```text
AddLocalPlayerMark(WidgetClassPath: string, OwnerPlayerState: PlayerState, RangeRad: number) -> number
```

添加一个玩家Mark，会根据玩家位置实时更新位置。（Widget 需继承自 UGCMapUIMarkDynamicWidget）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetClassPath` | `string` | 控件类路径，Widget 需继承自 UGCMapUIMarkDynamicWidget |
| `OwnerPlayerState` | `PlayerState` | 标记目标 PlayerState |
| `RangeRad` | `number` | 标记显示范围，超出范围不会显示标记（目标实际距离，单位：cm） |

**Returns**

| Type | Description |
|---|---|
| `number` | 标记 ID |

### `RemoveMark`

```text
RemoveMark(InstanceID: number)
```

移除一个标记，此接口的调用者同传入的 InstanceID 匹配。
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 标记 ID |

### `UpdateMarkLocation`

```text
UpdateMarkLocation(InstanceID: number, MarkLocation: Vector, bNeedPrintLog: boolean)
```

更新标记位置，此接口的调用者同传入的 InstanceID 匹配。
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 标记 ID |
| `MarkLocation` | `Vector` | 新 Location |
| `bNeedPrintLog` | `boolean` | 是否输出日志 |

### `UpdateMarkRotation`

```text
UpdateMarkRotation(InstanceID: number, NewRotation: Rotator)
```

更新标记旋转，此接口的调用者同传入的 InstanceID 匹配。
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 标记 ID |
| `NewRotation` | `Rotator` | 新 Rotator 可使用 Rotator.New(Roll,Pitch,Yaw) 创建，结构 {Roll=Roll, Pitch=Pitch, Yaw=Yaw} |

### `GetMarkLocation`

```text
GetMarkLocation(InstanceID: number) -> Vector
```

获取标记位置，此接口的调用者同传入的 InstanceID 匹配。
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 标记 ID |

**Returns**

| Type | Description |
|---|---|
| `Vector` | 标记点 Location |

### `GetMarkRotation`

```text
GetMarkRotation(InstanceID: number) -> Rotator
```

获取标记旋转，此接口的调用者同传入的 InstanceID 匹配。
调用此接口来更新通过 UGCMapMarkManagerSystem.Add[Local]CustomMark 创建的小地图标记控件时，须确保该控件的 Rotate Widget to Angle 选项已勾选。
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 标记 ID |

**Returns**

| Type | Description |
|---|---|
| `Rotator` | 标记点 Rotator 可使用 Rotator.New(Roll,Pitch,Yaw) 创建,结构 {Roll=Roll, Pitch=Pitch, Yaw=Yaw} |

### `GetMarkOwner`

```text
GetMarkOwner(InstanceID: number) -> PlayerState
```

获取标记 Owner，此接口的调用者同传入的 InstanceID 匹配。
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 标记 ID |

**Returns**

| Type | Description |
|---|---|
| `PlayerState` | 标记点对应的 PlayerState |

### `MakeMapMarkGraph`

```text
MakeMapMarkGraph(WorldCorners: FVector[], MarkColor: FColor, RadiusOrLineWidth: number, bRecolorOrBlending: boolean, AddMarkFlag: EAddMarkFlag)
```

在地图上画图
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldCorners` | `FVector[]` | 世界坐标点，按顺序绘制，1个点画圆，2个点画直线，3个点或以上画多边形 |
| `MarkColor` | `FColor` | 图像颜色 |
| `RadiusOrLineWidth` | `number` | 半径或直线宽度 |
| `bRecolorOrBlending` | `boolean` | 覆盖颜色或Alpha混合 |
| `AddMarkFlag` | `EAddMarkFlag` | 生效地图类型 |

### `ClearMapMarkGraph`

```text
ClearMapMarkGraph(ClearMarkFlag: EAddMarkFlag)
```

清除地图上的图案
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ClearMarkFlag` | `EAddMarkFlag` | 生效地图类型 |

### `SetVoiceVisualization`

```text
SetVoiceVisualization(InFlag: EVoiceVisualizationFlag, bIsEnable: boolean)
```

开关小地图上的指定类型音效图标
生效范围：服务端&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFlag` | `EVoiceVisualizationFlag` | 指定音效类型 |
| `bIsEnable` | `boolean` | 开关控制 |

### `IsVoiceVisualizationFlagEnable`

```text
IsVoiceVisualizationFlagEnable(InFlag: EVoiceVisualizationFlag) -> boolean
```

获取小地图上指定类型音效图标的开关状态
生效范围：服务端&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFlag` | `EVoiceVisualizationFlag` | 指定音效类型 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否开启 |

### `GetMapMarkLocation`

```text
GetMapMarkLocation(PlayerState: ASTExtraPlayerState) -> Vector
```

获取和平原生小地图标点位置
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerState` | `ASTExtraPlayerState` | 玩家状态 |

**Returns**

| Type | Description |
|---|---|
| `Vector` | 标记点位置 |

### `ChangeMapByMapID`

```text
ChangeMapByMapID(MapID: number)
```

根据地图ID修改右上角地图
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MapID` | `number` | 地图ID |

### `DrawGuidePathToTarget`

```text
DrawGuidePathToTarget(Params: FGuidePathDrawParams, OnResult: FOnGuidePathResult) -> number
```

请求绘制引导线
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Params` | `FGuidePathDrawParams` | 绘制参数 |
| `OnResult` | `FOnGuidePathResult` | 结果回调 |

**Returns**

| Type | Description |
|---|---|
| `number` | 请求ID |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCMathUtility.json -->

# UGCMathUtility

数学工具接口库

## Functions

### `Sin`

```text
Sin(A: number) -> number
```

返回A的正弦值(sin)，结果为弧度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | sin(A) |

### `Asin`

```text
Asin(A: number) -> number
```

返回A的反正弦值(arcsin)，结果为弧度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | arcsin(A) |

### `Cos`

```text
Cos(A: number) -> number
```

返回A的余弦值(cos)，结果为弧度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | cos(A) |

### `Acos`

```text
Acos(A: number) -> number
```

返回A的反余弦值(arccos)，结果为弧度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | arccos(A) |

### `Tan`

```text
Tan(A: number) -> number
```

返回A的正切值(tan)，结果为弧度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | tan(A) |

### `Atan`

```text
Atan(A: number) -> number
```

返回A的反正切值(arctan)，结果为弧度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | arctan(A) |

### `DegSin`

```text
DegSin(A: number) -> number
```

返回A的正弦值(sin)，结果为角度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | sin(A) |

### `DegAsin`

```text
DegAsin(A: number) -> number
```

返回A的反正弦值(arcsin)，结果为角度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | arcsin(A) |

### `DegCos`

```text
DegCos(A: number) -> number
```

返回A的余弦值(cos)，结果为角度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | cos(A) |

### `DegAcos`

```text
DegAcos(A: number) -> number
```

返回A的反余弦值(arccos)，结果为角度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | arccos(A) |

### `DegTan`

```text
DegTan(A: number) -> number
```

返回A的正切值(tan)，结果为角度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | tan(A) |

### `DegAtan`

```text
DegAtan(A: number) -> number
```

返回A的反正切值(arctan)，结果为角度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | arctan(A) |

### `DegAtan2`

```text
DegAtan2(A: number, B: number) -> number
```

返回A/B的反正切值(atan2)，结果为角度制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |
| `B` | `number` | B |

**Returns**

| Type | Description |
|---|---|
| `number` | arctan(A/B) |

### `RandomFloat`

```text
RandomFloat() -> number
```

返回一个介于0和1之间的随机浮点数

**Returns**

| Type | Description |
|---|---|
| `number` | 随机浮点数 |

### `RandomFloatInRange`

```text
RandomFloatInRange(InMin: number, InMax: number) -> number
```

生成一个介于Min和Max之间的随机数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMin` | `number` | 最小值 |
| `InMax` | `number` | 最大值 |

**Returns**

| Type | Description |
|---|---|
| `number` | 随机数 |

### `Lerp`

```text
Lerp(A: number, B: number, Alpha: number) -> number
```

根据Alpha在A和B之间线性插值（Alpha=0时返回A，Alpha=1时返回B））

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |
| `B` | `number` | B |
| `Alpha` | `number` | Alpha |

**Returns**

| Type | Description |
|---|---|
| `number` | 线性插值 |

### `FClamp`

```text
FClamp(InValue: number, InMin: number, InMax: number) -> number
```

【废弃】请使用 UGCMathUtility.Clamp
返回限制在A和B之间的值（包含A和B）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `number` | 值 |
| `InMin` | `number` | 最小值 |
| `InMax` | `number` | 最大值 |

**Returns**

| Type | Description |
|---|---|
| `number` | 限制后的值 |

### `MapRangeClamped`

```text
MapRangeClamped(InValue: number, InMinIn: number, InMaxIn: number, InMinOut: number, InMaxOut: number) -> number
```

将数值从一个输入范围映射到另一个输出范围（数值会被限制在输入范围内）。（例如：将0.5从0→1范围映射到0→50范围会得到25）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `number` | 值 |
| `InMinIn` | `number` | 输入范围最小值 |
| `InMaxIn` | `number` | 输入范围最大值 |
| `InMinOut` | `number` | 输出范围最小值 |
| `InMaxOut` | `number` | 输出范围最大值 |

**Returns**

| Type | Description |
|---|---|
| `number` | 映射后的值 |

### `NearlyEqualFloat`

```text
NearlyEqualFloat(A: number, B: number, Tolerance: number) -> boolean
```

返回A是否近似等于B（|A - B| < 误差容限）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |
| `B` | `number` | B |
| `Tolerance` | `number` | 误差容限 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否近似等于 |

### `NotEqualFloat`

```text
NotEqualFloat(A: number, B: number) -> boolean
```

如果A不等于B则返回true

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `number` | A |
| `B` | `number` | B |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否不等于 |

### `Now`

```text
Now() -> FDateTime
```

返回当前计算机的本地日期和时间

**Returns**

| Type | Description |
|---|---|
| `FDateTime` | 当前计算机的本地日期和时间 |

### `Today`

```text
Today() -> FDateTime
```

返回当前计算机的本地日期

**Returns**

| Type | Description |
|---|---|
| `FDateTime` | 当前计算机的本地日期 |

### `UtcNow`

```text
UtcNow() -> FDateTime
```

返回当前计算机的UTC日期和时间

**Returns**

| Type | Description |
|---|---|
| `FDateTime` | 当前计算机的UTC日期和时间 |

### `GetYear`

```text
GetYear(A: FDateTime) -> number
```

返回A的年分量值

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | 年分量值 |

### `GetMonth`

```text
GetMonth(A: FDateTime) -> number
```

返回A的月分量值

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | 月分量值 |

### `DaysInMonth`

```text
DaysInMonth(Year: number, Month: number) -> number
```

返回给定年份和月份的天数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Year` | `number` | 年份 |
| `Month` | `number` | 月份 |

**Returns**

| Type | Description |
|---|---|
| `number` | 天数 |

### `AddVector`

```text
AddVector(A: FVector, B: FVector) -> FVector
```

向量加法

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `B` | `FVector` | B |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `AddVector2D`

```text
AddVector2D(A: FVector2D, B: FVector2D) -> FVector2D
```

返回二维向量A和二维向量B的和（A + B）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | A |
| `B` | `FVector2D` | B |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SubtractVector`

```text
SubtractVector(A: FVector, B: FVector) -> FVector
```

向量减法

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `B` | `FVector` | B |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SubtractVector2D`

```text
SubtractVector2D(A: FVector2D, B: FVector2D) -> FVector2D
```

返回二维向量A和二维向量B的差（A - B）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | A |
| `B` | `FVector2D` | B |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `MultiplyVector`

```text
MultiplyVector(A: FVector, B: number) -> FVector
```

将向量A按B缩放

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `B` | `number` | B |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `MultiplyVector2D`

```text
MultiplyVector2D(A: FVector2D, B: number) -> FVector2D
```

将二维向量A按B缩放

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | A |
| `B` | `number` | B |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `VSize`

```text
VSize(A: FVector) -> number
```

返回向量的长度

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `VSize2D`

```text
VSize2D(A: FVector2D) -> number
```

返回二维向量的长度

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `VSizeSquared`

```text
VSizeSquared(A: FVector) -> number
```

返回向量的长度的平方

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `VSizeSquared2D`

```text
VSizeSquared2D(A: FVector2D) -> number
```

返回二维向量的长度的平方

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | A |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `EqualVector`

```text
EqualVector(A: FVector, B: FVector, Tolerance: number) -> boolean
```

判断向量A是否在允许误差范围内等于向量B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `B` | `FVector` | B |
| `Tolerance` | `number` | 允许误差，默认为1.e-4f |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `NotEqualVector`

```text
NotEqualVector(A: FVector, B: FVector, Tolerance: number) -> boolean
```

判断向量A是否在允许误差范围内不等于向量B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `B` | `FVector` | B |
| `Tolerance` | `number` | 允许误差，默认为1.e-4f |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `DotVector`

```text
DotVector(A: FVector, B: FVector) -> number
```

返回两个向量的点积

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `B` | `FVector` | B |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `CrossVector`

```text
CrossVector(A: FVector, B: FVector) -> FVector
```

返回两个向量的叉积

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `B` | `FVector` | B |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `DotVector2D`

```text
DotVector2D(A: FVector2D, B: FVector2D) -> number
```

返回两个二维向量的点积

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | A |
| `B` | `FVector2D` | B |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `CrossVector2D`

```text
CrossVector2D(A: FVector2D, B: FVector2D) -> number
```

返回两个二维向量的叉积

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | A |
| `B` | `FVector2D` | B |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `RotateVector`

```text
RotateVector(A: FVector, B: FRotator) -> FVector
```

返回向量A经过 Rotator B 旋转后的结果

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `B` | `FRotator` | B |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Vector |

### `RotateAngleAxis`

```text
RotateAngleAxis(A: FVector, AngleDeg: number, Axis: FVector) -> FVector
```

返回向量A绕Axis轴旋转AngleDeg角度后的结果

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `AngleDeg` | `number` | AngleDeg |
| `Axis` | `FVector` | Axis |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Vector |

### `Normal`

```text
Normal(A: FVector) -> FVector
```

返回向量A的单位法向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Vector |

### `Normal2D`

```text
Normal2D(A: FVector2D) -> FVector2D
```

返回二维向量A的单位法向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | A |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | Vector |

### `VLerp`

```text
VLerp(A: FVector, B: FVector, Alpha: number) -> FVector
```

根据Alpha值在向量A和向量B之间线性插值（Alpha=0时返回100%A，Alpha=1时返回100%B）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | A |
| `B` | `FVector` | B |
| `Alpha` | `number` | Alpha |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Vector |

### `RandomUnitVector`

```text
RandomUnitVector() -> FVector
```

返回一个长度为1的随机向量

**Returns**

| Type | Description |
|---|---|
| `FVector` | Vector |

### `RandomPointInBoundingBox`

```text
RandomPointInBoundingBox(Origin: FVector, BoxExtent: FVector) -> FVector
```

返回指定边界框内的随机点

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Origin` | `FVector` | Origin |
| `BoxExtent` | `FVector` | BoxExtent |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Point |

### `ProjectVectorOnToVector`

```text
ProjectVectorOnToVector(V: FVector, Target: FVector) -> FVector
```

将向量V投影到目标向量Target上并返回投影向量，如果Target长度接近零，则返回零向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector` | V |
| `Target` | `FVector` | Target |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Vector |

### `FInterpTo`

```text
FInterpTo(Current: number, Target: number, DeltaTime: number, InterpSpeed: number) -> number
```

根据当前值到目标值的插值进行平滑过渡，实现流畅的过度效果

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `number` | 当前值 |
| `Target` | `number` | 目标值 |
| `DeltaTime` | `number` | 平滑时间 |
| `InterpSpeed` | `number` | 插值速度 |

**Returns**

| Type | Description |
|---|---|
| `number` | 新的插值位置 |

### `FInterpConstantTo`

```text
FInterpConstantTo(Current: number, Target: number, DeltaTime: number, InterpSpeed: number) -> number
```

以恒定速率向目标值变换

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `number` | 当前值 |
| `Target` | `number` | 目标值 |
| `DeltaTime` | `number` | 平滑时间 |
| `InterpSpeed` | `number` | 插值速度 |

**Returns**

| Type | Description |
|---|---|
| `number` | Location |

### `VInterpTo`

```text
VInterpTo(Current: FVector, Target: FVector, DeltaTime: number, InterpSpeed: number) -> FVector
```

根据向量表示的当前位置与目标位置的距离平滑地接近目标位置，实现流畅的追踪效果

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FVector` | 当前位置 |
| `Target` | `FVector` | 目标位置 |
| `DeltaTime` | `number` | 平滑时间 |
| `InterpSpeed` | `number` | 插值速度 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 新的插值位置 |

### `VInterpConstantTo`

```text
VInterpConstantTo(Current: FVector, Target: FVector, DeltaTime: number, InterpSpeed: number) -> FVector
```

以恒定速率向向量表示的目标位置移动

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FVector` | 当前位置 |
| `Target` | `FVector` | 目标位置 |
| `DeltaTime` | `number` | 平滑时间 |
| `InterpSpeed` | `number` | 插值速度 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Location |

### `Vector2DInterpTo`

```text
Vector2DInterpTo(Current: FVector2D, Target: FVector2D, DeltaTime: number, InterpSpeed: number) -> FVector2D
```

根据二维向量表示的当前位置与目标位置的距离平滑地接近目标位置，实现流畅的追踪效果

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FVector2D` | 当前位置 |
| `Target` | `FVector2D` | 目标位置 |
| `DeltaTime` | `number` | 平滑时间 |
| `InterpSpeed` | `number` | 插值速度 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 新的插值位置 |

### `Vector2DInterpConstantTo`

```text
Vector2DInterpConstantTo(Current: FVector2D, Target: FVector2D, DeltaTime: number, InterpSpeed: number) -> FVector2D
```

以恒定速率向二维向量表示的目标位置移动

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FVector2D` | 当前位置 |
| `Target` | `FVector2D` | 目标位置 |
| `DeltaTime` | `number` | 平滑时间 |
| `InterpSpeed` | `number` | 插值速度 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | Location |

### `RInterpTo`

```text
RInterpTo(Current: FRotator, Target: FRotator, DeltaTime: number, InterpSpeed: number) -> FRotator
```

根据当前旋转角度平滑过渡到目标旋转角度，实现流畅的旋转效果

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FRotator` | 当前旋转角度 |
| `Target` | `FRotator` | 目标旋转角度 |
| `DeltaTime` | `number` | 平滑时间 |
| `InterpSpeed` | `number` | 插值速度 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 新的插值旋转角度 |

### `RInterpConstantTo`

```text
RInterpConstantTo(Current: FRotator, Target: FRotator, DeltaTime: number, InterpSpeed: number) -> FRotator
```

以恒定速率向目标旋转角度旋转

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FRotator` | 当前旋转角度 |
| `Target` | `FRotator` | 目标旋转角度 |
| `DeltaTime` | `number` | 平滑时间 |
| `InterpSpeed` | `number` | 插值速度 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | Location |

### `FindClosestPointOnSegment`

```text
FindClosestPointOnSegment(Point: FVector, SegmentStart: FVector, SegmentEnd: FVector) -> FVector
```

查找线段上距离给定点最近的点

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | 需要计算最近点的目标点 |
| `SegmentStart` | `FVector` | 线段起点 |
| `SegmentEnd` | `FVector` | 线段终点 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 线段上距离给定点最近的点 |

### `FindClosestPointOnLine`

```text
FindClosestPointOnLine(Point: FVector, LineOrigin: FVector, LineDirection: FVector) -> FVector
```

找到无限长直线上距离给定点最近的点

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | 需要计算最近点的目标点 |
| `LineOrigin` | `FVector` | 直线上的参考点 |
| `LineDirection` | `FVector` | 直线上的方向向量(无需归一化) |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Point |

### `GetPointDistanceToSegment`

```text
GetPointDistanceToSegment(Point: FVector, SegmentStart: FVector, SegmentEnd: FVector) -> number
```

计算点到线段的最短距离

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | 需要计算最近点的目标点 |
| `SegmentStart` | `FVector` | 线段起点 |
| `SegmentEnd` | `FVector` | 线段终点 |

**Returns**

| Type | Description |
|---|---|
| `number` | 点到线段的最短距离 |

### `GetPointDistanceToLine`

```text
GetPointDistanceToLine(Point: FVector, LineOrigin: FVector, LineDirection: FVector) -> number
```

计算点到无限长直线的最短距离

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | 需要计算距离的目标 |
| `LineOrigin` | `FVector` | 直线上的参考点 |
| `LineDirection` | `FVector` | 直线上的方向向量(无需归一化) |

**Returns**

| Type | Description |
|---|---|
| `number` | 点到直线上的最短距离 |

### `ProjectVectorOnToPlane`

```text
ProjectVectorOnToPlane(V: FVector, PlaneNormal: FVector) -> FVector
```

将向量投影到由法向量定义的平面上

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector` | 需要投影的向量 |
| `PlaneNormal` | `FVector` | 法向量 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 投影后的向量 |

### `NegateVector`

```text
NegateVector(V: FVector) -> FVector
```

向量取反

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector` | 需要取反的向量 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 取反后的向量 |

### `ClampVectorSize`

```text
ClampVectorSize(V: FVector, Min: number, Max: number) -> FVector
```

将向量长度限制在最小值和最大值之间

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector` | 需要限制长度的向量 |
| `Min` | `number` | 最小长度 |
| `Max` | `number` | 最大长度 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 限制长度后的向量 |

### `GetMinElement`

```text
GetMinElement(V: FVector) -> number
```

找出向量中(X, Y或Z)的最小分量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector` | 需要计算最小分量的向量 |

**Returns**

| Type | Description |
|---|---|
| `number` | 最小分量 |

### `GetMaxElement`

```text
GetMaxElement(V: FVector) -> number
```

找出向量中(X, Y或Z)的最大分量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector` | 需要计算最大分量的向量 |

**Returns**

| Type | Description |
|---|---|
| `number` | 最大分量 |

### `GetDirectionUnitVector`

```text
GetDirectionUnitVector(From: FVector, To: FVector) -> FVector
```

计算从一个位置指向另一个位置的单位方向向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `From` | `FVector` | 起点 |
| `To` | `FVector` | 终点 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 单位方向向量 |

### `EqualName`

```text
EqualName(A: string, B: string) -> boolean
```

如果A和B相等则返回true (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `string` | A |
| `B` | `string` | B |

**Returns**

| Type | Description |
|---|---|
| `boolean` | true or false |

### `NotEqualName`

```text
NotEqualName(A: string, B: string) -> boolean
```

如果A和B不相等则返回true (A ~= B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `string` | A |
| `B` | `string` | B |

**Returns**

| Type | Description |
|---|---|
| `boolean` | true or false |

### `MakeBox`

```text
MakeBox(Min: FVector, Max: FVector) -> FBox
```

通过最小点和最大点创建一个FBox，并将IsValid设为true

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Min` | `FVector` | 最小点 |
| `Max` | `FVector` | 最大点 |

**Returns**

| Type | Description |
|---|---|
| `FBox` | FBox |

### `MakeBox2D`

```text
MakeBox2D(Min: FVector2D, Max: FVector2D) -> FBox2D
```

通过最小点和最大点创建一个FBox2D，并将IsValid设为true

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Min` | `FVector2D` | 最小点 |
| `Max` | `FVector2D` | 最大点 |

**Returns**

| Type | Description |
|---|---|
| `FBox2D` | FBox2D |

### `MakeVector`

```text
MakeVector(X: number, Y: number, Z: number) -> FVector
```

创建一个向量 {X, Y, Z}

**Parameters**

| Name | Type | Description |
|---|---|---|
| `X` | `number` | X |
| `Y` | `number` | Y |
| `Z` | `number` | Z |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 向量 |

### `BreakVector`

```text
BreakVector(V: FVector) -> number,number,number
```

将向量分解为X、Y和Z分量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector` | 向量 |

**Returns**

| Type | Description |
|---|---|
| `number,number,number` | X,Y,Z |

### `MakeVector2D`

```text
MakeVector2D(X: number, Y: number) -> FVector2D
```

创建一个二维向量 {X, Y}

**Parameters**

| Name | Type | Description |
|---|---|---|
| `X` | `number` | X |
| `Y` | `number` | Y |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 向量 |

### `BreakVector2D`

```text
BreakVector2D(V: FVector2D) -> number,number
```

将二维向量分解为X和Y分量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector2D` | 向量 |

**Returns**

| Type | Description |
|---|---|
| `number,number` | X,Y |

### `GetForwardVector`

```text
GetForwardVector(InRot: FRotator) -> FVector
```

按给定旋转角度旋转世界前向向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRot` | `FRotator` | 旋转角度 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 矩阵 |

### `GetRightVector`

```text
GetRightVector(InRot: FRotator) -> FVector
```

按给定旋转角度旋转世界右向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRot` | `FRotator` | 旋转角度 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 矩阵 |

### `GetUpVector`

```text
GetUpVector(InRot: FRotator) -> FVector
```

按给定旋转角度旋转世界上向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRot` | `FRotator` | 旋转角度 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 矩阵 |

### `GetYawPitchFromVector`

```text
GetYawPitchFromVector(V: FVector) -> number,number
```

将向量分解为Yaw(偏航角)和Pitch(俯仰角)旋转值(角度制，不限制范围)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector` | 向量 |

**Returns**

| Type | Description |
|---|---|
| `number,number` | Yaw,Pitch |

### `MakeRotator`

```text
MakeRotator(Roll: number, Pitch: number, Yaw: number) -> FRotator
```

使用以度数为单位提供的旋转值创建旋转器{Roll, Pitch, Yaw}

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Roll` | `number` | Roll |
| `Pitch` | `number` | Pitch |
| `Yaw` | `number` | Yaw |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `FindLookAtRotation`

```text
FindLookAtRotation(Start: FVector, Target: FVector) -> FRotator
```

查找一个物体在起始位置指向目标位置所需的旋转角度

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `FVector` | 起始位置 |
| `Target` | `FVector` | 目标位置 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `MakeRotFromX`

```text
MakeRotFromX(XAxis: FVector) -> FRotator
```

仅使用X轴构建Rotator。Y和Z轴未指定但将保持正交归一。X轴无需归一化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `XAxis` | `FVector` | X轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `MakeRotFromY`

```text
MakeRotFromY(YAxis: FVector) -> FRotator
```

仅使用Y轴构建Rotator。X和Z轴未指定但将保持正交归一。Y轴无需归一化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `YAxis` | `FVector` | Y轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `MakeRotFromZ`

```text
MakeRotFromZ(ZAxis: FVector) -> FRotator
```

仅使用Z轴构建Rotator。X和Y轴未指定但将保持正交归一。Z轴无需归一化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ZAxis` | `FVector` | Z轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `MakeRotFromXY`

```text
MakeRotFromXY(XAxis: FVector, YAxis: FVector) -> FRotator
```

使用给定的X和Y轴构建矩阵。X轴保持不变，Y轴会微调以确保正交性。Z轴将被计算得出。输入向量无需归一化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `XAxis` | `FVector` | X轴 |
| `YAxis` | `FVector` | Y轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `MakeRotFromXZ`

```text
MakeRotFromXZ(XAxis: FVector, ZAxis: FVector) -> FRotator
```

使用给定的X和Z轴构建矩阵。X轴保持不变，Z轴会微调以确保正交性。Y轴将被计算得出。输入向量无需归一化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `XAxis` | `FVector` | X轴 |
| `ZAxis` | `FVector` | Z轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `MakeRotFromYX`

```text
MakeRotFromYX(YAxis: FVector, XAxis: FVector) -> FRotator
```

使用给定的Y和X轴构建矩阵。Y轴保持不变，X轴会微调以确保正交性。Z轴将被计算得出。输入向量无需归一化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `YAxis` | `FVector` | Y轴 |
| `XAxis` | `FVector` | X轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `MakeRotFromYZ`

```text
MakeRotFromYZ(YAxis: FVector, ZAxis: FVector) -> FRotator
```

使用给定的Y和Z轴构建矩阵。Y轴保持不变，Z轴会微调以确保正交性。X轴将被计算得出。输入向量无需归一化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `YAxis` | `FVector` | Y轴 |
| `ZAxis` | `FVector` | Z轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `MakeRotFromZX`

```text
MakeRotFromZX(ZAxis: FVector, XAxis: FVector) -> FRotator
```

使用给定的Z和X轴构建矩阵。Z轴保持不变，X轴会微调以确保正交性。Y轴将被计算得出。输入向量无需归一化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ZAxis` | `FVector` | Z轴 |
| `XAxis` | `FVector` | X轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `MakeRotFromZY`

```text
MakeRotFromZY(ZAxis: FVector, YAxis: FVector) -> FRotator
```

使用给定的Z和Y轴构建矩阵。Z轴保持不变，Y轴会微调以确保正交性。X轴将被计算得出。输入向量无需归一化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ZAxis` | `FVector` | Z轴 |
| `YAxis` | `FVector` | Y轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 矩阵 |

### `BreakRotator`

```text
BreakRotator(Rotator: FRotator) -> number,number,number
```

将Rotator分解为{Roll, Pitch, Yaw}角度值(单位:度)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rotator` | `FRotator` | Rotator |

**Returns**

| Type | Description |
|---|---|
| `number,number,number` | Roll,Pitch,Yaw |

### `MakeTransform`

```text
MakeTransform(Location: FVector, Rotation: FRotator, Scale: FVector) -> FTransform
```

根据位置、旋转和缩放创建Transform

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Location` | `FVector` | 位置 |
| `Rotation` | `FRotator` | 旋转 |
| `Scale` | `FVector` | 缩放 |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | transformFVecto |

### `BreakTransform`

```text
BreakTransform(Transform: FTransform) -> FVector,FRotator,FVector
```

将transform分解为{Location, Rotation, Scale}值

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Transform` | `FTransform` | Transform |

**Returns**

| Type | Description |
|---|---|
| `FVector,FRotator,FVector` | Location,Rotation,Scale |

### `Conv_VectorToLinearColor`

```text
Conv_VectorToLinearColor(Vector: FVector) -> FLinearColor
```

将向量转换为LinearColor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vector` | `FVector` | 向量 |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | LinearColor |

### `Conv_ColorToLinearColor`

```text
Conv_ColorToLinearColor(Color: FColor) -> FLinearColor
```

将Color转换为LinearColor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Color` | `FColor` | Color |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | LinearColor |

### `Conv_LinearColorToColor`

```text
Conv_LinearColorToColor(LinearColor: FLinearColor) -> FColor
```

将LinearColor转换为Color

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LinearColor` | `FLinearColor` | LinearColor |

**Returns**

| Type | Description |
|---|---|
| `FColor` | Color |

### `Conv_VectorToVector2D`

```text
Conv_VectorToVector2D(Vector: FVector) -> FVector2D
```

将向量转换为二维向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vector` | `FVector` | 向量 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 二维向量 |

### `Conv_Vector2DToVector`

```text
Conv_Vector2DToVector(Vector2D: FVector2D) -> FVector
```

将二维向量转换为向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vector2D` | `FVector2D` | 二维向量 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 向量 |

### `HSVToRGB`

```text
HSVToRGB(H: number, S: number, V: number, A: number) -> FLinearColor
```

根据HSV分量创建颜色

**Parameters**

| Name | Type | Description |
|---|---|---|
| `H` | `number` | 色相 |
| `S` | `number` | 饱和度 |
| `V` | `number` | 明度 |
| `A` | `number` | 透明度 |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | Color |

### `RGBToHSV`

```text
RGBToHSV(Color: FLinearColor) -> number,number,number,number
```

将颜色分解为单独的HSV分量（以及透明度）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Color` | `FLinearColor` | Color |

**Returns**

| Type | Description |
|---|---|
| `number,number,number,number` | H,S,V,A |

### `Conv_HSVToRGB`

```text
Conv_HSVToRGB(HSV: FLinearColor) -> FLinearColor
```

将HSV线性颜色转换为RGB颜色（其中H在R分量，S在G分量，V在B分量）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HSV` | `FLinearColor` | HSV |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | RGB |

### `Conv_RGBToHSV`

```text
Conv_RGBToHSV(RGB: FLinearColor) -> FLinearColor
```

将RGB线性颜色转换为HSV（其中H存储在R分量，S存储在G分量，V存储在B分量）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RGB` | `FLinearColor` | RGB |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | HSV |

### `HexToRGB`

```text
HexToRGB(HexString: string, bSRGB: boolean) -> FLinearColor
```

将十六进制颜色字符串转换为RGB

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HexString` | `string` | 十六进制颜色字符串 |
| `bSRGB` | `boolean` | 是否使用sRGB颜色空间 |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | RGB |

### `RGBToHex`

```text
RGBToHex(RGB: FLinearColor, bSRGB: boolean) -> string
```

将RGB颜色转换为十六进制字符串

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RGB` | `FLinearColor` | RGB |
| `bSRGB` | `boolean` | 是否使用sRGB颜色空间 |

**Returns**

| Type | Description |
|---|---|
| `string` | 十六进制颜色字符串 |

### `Conv_VectorToRotator`

```text
Conv_VectorToRotator(XAxis: FVector) -> FRotator
```

创建一个使X轴朝向指定方向向量的Rotator

**Parameters**

| Name | Type | Description |
|---|---|---|
| `XAxis` | `FVector` | X轴 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | Rotator |

### `Conv_RotatorToVector`

```text
Conv_RotatorToVector(Rotator: FRotator) -> FVector
```

获取旋转后的X轴方向向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rotator` | `FRotator` | Rotator |

**Returns**

| Type | Description |
|---|---|
| `FVector` | X轴 |

### `TransformLocation`

```text
TransformLocation(T: FTransform, Location: FVector) -> FVector
```

使用指定的变换矩阵转换位置坐标
例如：若T是某物体的变换矩阵，此操作会将局部坐标系的位置转换到世界坐标系

**Parameters**

| Name | Type | Description |
|---|---|---|
| `T` | `FTransform` | 变换矩阵 |
| `Location` | `FVector` | 局部坐标系下的位置 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 世界坐标系下的位置 |

### `TransformDirection`

```text
TransformDirection(T: FTransform, Direction: FVector) -> FVector
```

使用指定的变换矩阵转换方向向量 - 不会改变向量长度
例如：若T是某物体的变换矩阵，此操作会将局部坐标系的方向向量转换到世界坐标系

**Parameters**

| Name | Type | Description |
|---|---|---|
| `T` | `FTransform` | 变换矩阵 |
| `Direction` | `FVector` | 局部坐标系下的方向向量 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 世界坐标系下的方向向量 |

### `TransformRotation`

```text
TransformRotation(T: FTransform, Rotation: FRotator) -> FRotator
```

使用指定的变换矩阵转换Rotator
例如：若T是某物体的变换矩阵，此操作会将局部坐标系的旋转转换到世界坐标系

**Parameters**

| Name | Type | Description |
|---|---|---|
| `T` | `FTransform` | 变换矩阵 |
| `Rotation` | `FRotator` | 局部坐标系下的旋转 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 世界坐标系下的旋转 |

### `RandomBool`

```text
RandomBool() -> boolean
```

随机返回 true 或 false，概率各占 50%

**Returns**

| Type | Description |
|---|---|
| `boolean` | true或false |

### `RandomBoolWithWeight`

```text
RandomBoolWithWeight(Weight: number) -> boolean
```

根据指定权重获取随机概率结果。权重范围为 0.0 - 1.0
例如：权重 = 0.6，返回值将有 60% 的概率为 True

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Weight` | `number` | 权重 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | true或false |

### `RandomInteger`

```text
RandomInteger(Max: number) -> number
```

返回一个随机数，范围在0到Max - 1之间，每个数出现的概率相同

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Max` | `number` | 最大值 |

**Returns**

| Type | Description |
|---|---|
| `number` | 随机数 |

### `Clamp`

```text
Clamp(Value: number, Min: number, Max: number) -> number
```

返回限制在A和B之间的值(包含A和B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `number` | 值 |
| `Min` | `number` | 最小值 |
| `Max` | `number` | 最大值 |

**Returns**

| Type | Description |
|---|---|
| `number` | 限制后的值 |

### `RandomIntegerInRange`

```text
RandomIntegerInRange(Min: number, Max: number) -> number
```

返回Min和Max之间的随机整数(包含Min和Max)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Min` | `number` | 最小值 |
| `Max` | `number` | 最大值 |

**Returns**

| Type | Description |
|---|---|
| `number` | 随机整数 |

### `IsPointInBox`

```text
IsPointInBox(Point: FVector, BoxOrigin: FVector, BoxExtent: FVector) -> boolean
```

判断给定点是否在盒子内（包括在盒子边界上的点）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | 要测试的点 |
| `BoxOrigin` | `FVector` | 盒子的原点 |
| `BoxExtent` | `FVector` | 盒子在各个轴上的范围（从原点出发的距离） |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果点在盒子内则返回true；否则返回false |

### `IsPointInBoxWithTransform`

```text
IsPointInBoxWithTransform(Point: FVector, BoxWorldTransform: FTransform, BoxExtent: FVector) -> boolean
```

判断给定点是否在具有特定变换的盒子内（包含边界点)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | 要测试的点 |
| `BoxWorldTransform` | `FTransform` | 盒子从组件空间到世界空间的变换 |
| `BoxExtent` | `FVector` | 盒子在组件空间中的范围（各轴距原点的距离） |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果点在盒子内则返回true；否则返回false |

### `EqualRotator`

```text
EqualRotator(A: FRotator, B: FRotator, ErrorTolerance: number) -> boolean
```

检查Rotator A 和 B 是否在指定误差范围内相等 (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | 旋转量A |
| `B` | `FRotator` | 旋转量B |
| `ErrorTolerance` | `number` | 误差范围 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果旋转量A和B在误差范围内相等则返回true；否则返回false |

### `NotEqualRotator`

```text
NotEqualRotator(A: FRotator, B: FRotator, ErrorTolerance: number) -> boolean
```

检查Rotator A 和 B 是否在指定误差范围内不相等 (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | 旋转量A |
| `B` | `FRotator` | 旋转量B |
| `ErrorTolerance` | `number` | 误差范围 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果旋转量A和B在误差范围内不相等则返回true；否则返回false |

### `ComposeRotators`

```text
ComposeRotators(A: FRotator, B: FRotator) -> FRotator
```

组合两个旋转，返回先应用A再应用B的结果旋转

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | 旋转量A |
| `B` | `FRotator` | 旋转量B |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 先应用A再应用B的结果旋转 |

### `GetAxes`

```text
GetAxes(Rotator: FRotator) -> FVector,FVector,FVector
```

获取该旋转对应的前向、右向和上向三个基准方向向量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rotator` | `FRotator` | 旋转量 |

**Returns**

| Type | Description |
|---|---|
| `FVector,FVector,FVector` | 前向向量,右向向量,上向向量 |

### `NormalRotator`

```text
NormalRotator(A: FRotator) -> FRotator
```

标准化Rotator

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | 旋转量 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 标准化后的旋转量 |

### `RandomRotator`

```text
RandomRotator(bRoll: boolean) -> FRotator
```

生成一个随机旋转角度，可选择是否包含绕Z轴的随机旋转

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bRoll` | `boolean` | 是否包含绕Z轴的随机旋转 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 随机旋转量 |

### `RLerp`

```text
RLerp(A: FRotator, B: FRotator, Alpha: number, bShortestPath: boolean) -> FRotator
```

基于Alpha值在A和B之间线性插值（Alpha=0时返回100%A，Alpha=1时返回100%B）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | 起始旋转量 |
| `B` | `FRotator` | 目标旋转量 |
| `Alpha` | `number` | 插值比例（0-1） |
| `bShortestPath` | `boolean` | 是否采用最短路径插值 |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | 线性插值后的值 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%A4%BE%E4%BA%A4%E7%B3%BB%E7%BB%9F/UGCMessageSystem.json -->

# UGCMessageSystem

游戏聊天通用接口库

## Functions

### `JoinCampMessageChannel`

```text
JoinCampMessageChannel(PlayerKey: number, CampID: number)
```

阵营聊天 开局分阵营或阵营变更时同步阵营信息，创建阵营的聊天室
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家的 PlayerKey |
| `CampID` | `number` | 阵营 ID（传入0为无阵营） |

### `SendSystemMessageToPlayer`

```text
SendSystemMessageToPlayer(PlayerKey: number, MessageTag: string, MessageContent: string, Level: number) -> boolean
```

给单独玩家发送系统消息
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 PlayerKey |
| `MessageTag` | `string` | 消息标题 |
| `MessageContent` | `string` | 消息内容 |
| `Level` | `number` | 消息等级 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否发送成功 |

### `SendSystemMessageToAll`

```text
SendSystemMessageToAll(MessageTag: string, MessageContent: string, Level: number) -> boolean
```

给所有玩家发送系统消息
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MessageTag` | `string` | 消息标题 |
| `MessageContent` | `string` | 消息内容 |
| `Level` | `number` | 消息等级 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否发送成功 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/UGCMiscFunctionSystem.json -->

# UGCMiscFunctionSystem

游戏杂项函数接口库

## Functions

### `StartAirRoute`

```text
StartAirRoute(WorldObjectContext: UObject)
```

开始航线飞行
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldObjectContext` | `UObject` | 世界上下文对象 |

### `StartAirDrop`

```text
StartAirDrop(WorldObjectContext: UObject, Index: number, AirDropType: EAirDropType)
```

【废弃】请使用 UGCAirDropManagerSystem
开始空投
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldObjectContext` | `UObject` | 世界上下文对象 |
| `Index` | `number` | 定时普通空投设置中的配置序号（AirDropConfigsUGC） |
| `AirDropType` | `EAirDropType` | 空投箱空投类型一般为 EAirDropType.AirDrop_NormalAirDrop |

### `StartNormalAirDrop`

```text
StartNormalAirDrop(WorldObjectContext: UObject, StartPos: Vector2D, DropPos: Vector2D, Distance: number, AirDropType: EAirDropType)
```

【废弃】请使用 UGCAirDropManagerSystem
自定义空投
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldObjectContext` | `UObject` | 世界上下文对象 |
| `StartPos` | `Vector2D` | 飞机起始点,结构：{X=x,Y=y} |
| `DropPos` | `Vector2D` | 飞机结束点，结构：{X=x,Y=y} |
| `Distance` | `number` | 空投点距离起始点的比例 （0-1）的一个范围，0=StartPos，1=DropPos |
| `AirDropType` | `EAirDropType` | 空投箱空投类型一般为EAirDropType.AirDrop_NormalAirDrop |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%80%AA%E7%89%A9%E7%B3%BB%E7%BB%9F/UGCMobPawnSystem.json -->

# UGCMobPawnSystem

怪物系统接口库

## Functions

### `SpawnMob`

```text
SpawnMob(WorldContextObject: UObject, MobClass: UClass, Location: FVector, Rotation: FRotator) -> AActor
```

在目标位置刷一个怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `MobClass` | `UClass` | 怪物的类 |
| `Location` | `FVector` | 刷怪的位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | 刷出的怪物 |

### `SpawnMobByMobGroup`

```text
SpawnMobByMobGroup(WorldContextObject: UObject, MobGroupID: number, Location: FVector, Rotation: FRotator) -> AActor
```

在目标位置根据怪物组表中的ID刷一个怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `MobGroupID` | `number` | 怪物组表中的ID |
| `Location` | `FVector` | 刷怪的位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | 刷出的怪物 |

### `RangeSpawnMobs`

```text
RangeSpawnMobs(WorldContextObject: UObject, MobClass: UClass, Location: FVector, Rotation: FRotator, Range: number, HeightRange: number, Count: number) -> table
```

在指定位置的圆形范围中寻找合适的地面刷出指定数量的怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `MobClass` | `UClass` | 怪物的类 |
| `Location` | `FVector` | 刷怪范围的中心位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |
| `Range` | `number` | 刷怪圆形范围的半径 |
| `HeightRange` | `number` | 怪物刷出位置与中心位置的最大高度差 |
| `Count` | `number` | 刷出怪物的数量 |

**Returns**

| Type | Description |
|---|---|
| `table` | 刷出怪物的列表 |

### `RangeSpawnMobsByMobGroup`

```text
RangeSpawnMobsByMobGroup(WorldContextObject: UObject, MobGroupID: number, Location: FVector, Rotation: FRotator, Range: number, HeightRange: number, Count: number) -> table
```

在指定位置的圆形范围中寻找合适的地面刷出指定数量的怪，怪物类型由怪物组表ID指定
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `MobGroupID` | `number` | 怪物组表中的ID |
| `Location` | `FVector` | 刷怪范围的中心位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |
| `Range` | `number` | 刷怪圆形范围的半径 |
| `HeightRange` | `number` | 怪物刷出位置与中心位置的最大高度差 |
| `Count` | `number` | 刷出怪物的数量 |

**Returns**

| Type | Description |
|---|---|
| `table` | 刷出怪物的列表 |

### `RangeSpawnMobsOnTime`

```text
RangeSpawnMobsOnTime(WorldContextObject: UObject, MobClass: UClass, Location: FVector, Rotation: FRotator, Range: number, HeightRange: number, MinSpawnCountPerLoop: number, MaxSpawnCountPerLoop: number, LoopTimes: number, IntervalMinTime: number, IntervalMaxTime: number, FirstDelayTime: number, Callback: function, CallbackSelf: table)
```

在指定位置的圆形范围中每隔一定时间寻找合适的地面刷出一定数量的怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `MobClass` | `UClass` | 怪物类 |
| `Location` | `FVector` | 刷怪范围的中心位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |
| `Range` | `number` | 刷怪圆形范围的半径 |
| `HeightRange` | `number` | 怪物刷出位置与中心位置的最大高度差 |
| `MinSpawnCountPerLoop` | `number` | 每次刷怪的最小数量 |
| `MaxSpawnCountPerLoop` | `number` | 每次刷怪的最大数量 |
| `LoopTimes` | `number` | 总的刷怪轮数 |
| `IntervalMinTime` | `number` | 刷怪轮次间的最小时间间隔 |
| `IntervalMaxTime` | `number` | 刷怪轮次间的最大时间间隔 |
| `FirstDelayTime` | `number` | 从接口调用到首次刷怪的延迟时间 |
| `Callback` | `function` | 回调函数 |
| `CallbackSelf` | `table` | 回调函数的调用主体，静态函数时留空 |

### `RangeSpawnMobsByMobGroupOnTime`

```text
RangeSpawnMobsByMobGroupOnTime(WorldContextObject: UObject, MobGroupID: number, Location: FVector, Rotation: FRotator, Range: number, HeightRange: number, MinSpawnCountPerLoop: number, MaxSpawnCountPerLoop: number, LoopTimes: number, IntervalMinTime: number, IntervalMaxTime: number, FirstDelayTime: number, Callback: function, CallbackSelf: table)
```

在指定位置的圆形范围中每个一定时间寻找合适的地面刷出一定数量的怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `MobGroupID` | `number` | 怪物组表中的ID |
| `Location` | `FVector` | 刷怪范围的中心位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |
| `Range` | `number` | 刷怪圆形范围的半径 |
| `HeightRange` | `number` | 怪物刷出位置与中心位置的最大高度差 |
| `MinSpawnCountPerLoop` | `number` | 每次刷怪的最小数量 |
| `MaxSpawnCountPerLoop` | `number` | 每次刷怪的最大数量 |
| `LoopTimes` | `number` | 总的刷怪轮数 |
| `IntervalMinTime` | `number` | 刷怪轮次间的最小时间间隔 |
| `IntervalMaxTime` | `number` | 刷怪轮次间的最大时间间隔 |
| `FirstDelayTime` | `number` | 从接口调用到首次刷怪的延迟时间 |
| `Callback` | `function` | 回调函数 |
| `CallbackSelf` | `table` | 回调函数的调用主体，静态函数时留空 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E6%B3%95%E8%A7%84%E5%88%99/UGCMultiMode.json -->

# UGCMultiMode

多模式匹配通用接口库

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCMultiMode.NotifyMatchResponseDelegate` | `-` | 通知“开始匹配”的结果。通常会立即通知，然后进入“匹配中”的状态<br>生效范围：客户端<br>@param bSuccess boolean @是否匹配成功。通常来说 true 则把匹配界面切换到匹配中的状态，false 则把匹配界面切换到尚未开始匹配的状态 |
| `UGCMultiMode.NotifyMatchSucceededDelegate` | `-` | 通知在“匹配中”的玩家，匹配成功，即将进入新的对局游戏<br>生效范围：客户端 |
| `UGCMultiMode.NotifyStatusOfReadyMatchChangedDelegate` | `-` | 通知准备匹配的状态变化<br>生效范围：客户端<br>@param UID number @玩家 UID<br>@param NewStatus EStatusOfReadyMatch @新的准备匹配的状态<br>@param OldStatus EStatusOfReadyMatch @老的准备匹配的状态 |

## Functions

### `SetModeChooseUIVisible`

```text
SetModeChooseUIVisible(Visible: boolean)
```

设置模式选择 UI 的显示/隐藏
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Visible` | `boolean` | 设置为显示/隐藏 |

### `SetModeState`

```text
SetModeState(ModeID: number, ModeAvailability: boolean) -> boolean
```

设置模式选择 UI 的子模式可选择状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ModeID` | `number` | 模式 ID |
| `ModeAvailability` | `boolean` | 设置为可用/不可用 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 操作是否成功 |

### `GetModeID`

```text
GetModeID() -> number
```

获取当前模式 ID
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `number` | 当前模式 ID，若不存在则返回 0 |

### `SetModeChooseButtonVisible`

```text
SetModeChooseButtonVisible(Visible: boolean) -> boolean
```

设置模式选择打开按钮的显示/隐藏
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Visible` | `boolean` | 设置为显示/隐藏 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 操作是否成功 |

### `SetPlayerFill`

```text
SetPlayerFill(bPlayerFill: boolean)
```

开启/关闭补人
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bPlayerFill` | `boolean` | 目标状态 |

### `RequestMatch`

```text
RequestMatch(SubModeID: number, ResCallBack: function, Obj: UObject, IsTeamUnfill: boolean) -> boolean
```

开始匹配
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubModeID` | `number` | 子模式 ID |
| `ResCallBack` | `function` | 一个接受 bool 入参的回调函数，发起匹配的结果返回后会调用该函数 |
| `Obj` | `UObject` | 回调函数所属的对象 |
| `IsTeamUnfill` | `boolean` | 是否允许不匹配队友开始匹配 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否请求匹配成功 |

### `RequestCancelMatch`

```text
RequestCancelMatch() -> boolean
```

请求取消匹配
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `boolean` | 请求是否发送成功 |

### `RequestReadyMatch`

```text
RequestReadyMatch(bReady: boolean)
```

请求进入准备匹配状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bReady` | `boolean` | 是否准备匹配 |

### `QueryStatusOfReadyMatch`

```text
QueryStatusOfReadyMatch(UID: number) -> EStatusOfReadyMatch
```

查询准备匹配的状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID，可选，如果传入 nil 或者不传入，那么获取自己的准备匹配状态 |

**Returns**

| Type | Description |
|---|---|
| `EStatusOfReadyMatch` | 准备匹配的状态 |

### `GetModeSetting`

```text
GetModeSetting(ModeID: number) -> ModeSetting
```

获取指定ModeID的配置
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ModeID` | `number` | ModeID |

**Returns**

| Type | Description |
|---|---|
| `ModeSetting` | ModeID对应的设置 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCNavigationSystem.json -->

# UGCNavigationSystem

寻路导航系统接口库

## Functions

### `BuildNavmesh`

```text
BuildNavmesh(WorldContext: UObject, AgentName: FName)
```

同步生成全地图寻路图, 会阻塞服务器运行
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 当前世界上下文 |
| `AgentName` | `FName` | 作用Agent的寻路图名称一般为"Mannequin" |

### `AsyncBuildNavmesh`

```text
AsyncBuildNavmesh(WorldContext: UObject, AgentName: FName)
```

异步生成全地图寻路图
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 当前世界上下文 |
| `AgentName` | `FName` | 作用Agent的寻路图名称一般为"Mannequin" |

### `AddDynamicNavAffect`

```text
AddDynamicNavAffect(WorldContext: UObject, AgentName: FName, InBounds: FBox) -> bool
```

添加寻路图动态影响区域，标记后可只针对该区域增量更新寻路
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 当前世界上下文 |
| `AgentName` | `FName` | 作用Agent的寻路图名称一般为"Mannequin" |
| `InBounds` | `FBox` | 区域大小 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 操作结果 |

### `AsyncIncrementalBuild`

```text
AsyncIncrementalBuild(WorldContext: UObject, AgentName: FName) -> bool
```

区域异步增量生成寻路图，和AddDynamicNavAffect配合使用
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 当前世界上下文 |
| `AgentName` | `FName` | 作用Agent的寻路图名称一般为"Mannequin" |

**Returns**

| Type | Description |
|---|---|
| `bool` | 操作结果 |

### `ProjectPointToNavigation`

```text
ProjectPointToNavigation(WorldContext: UObject, Point: FVector, QueryExtent: FVector) -> bool,FVector
```

投影点到寻路图上的位置
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 当前世界上下文 |
| `Point` | `FVector` | 要投影的点 |
| `QueryExtent` | `FVector` | 投影查询范围 |

**Returns**

| Type | Description |
|---|---|
| `bool,FVector` | 操作结果, @投影位置 |

### `GetRandomReachablePointInRadius`

```text
GetRandomReachablePointInRadius(WorldContext: UObject, Origin: FVector, Radius: float) -> bool,FVector
```

范围获取随机可寻路到达点位
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 当前世界上下文 |
| `Origin` | `FVector` | 查找原点 |
| `Radius` | `float` | 查询范围 |

**Returns**

| Type | Description |
|---|---|
| `bool,FVector` | 操作结果， @可达位置 |

### `IsNavigationBeingBuilt`

```text
IsNavigationBeingBuilt(WorldContext: UObject) -> bool
```

寻路图是否构建
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 当前世界上下文 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 查询结果 |

### `GetNavigationGenerationFinishedDelegate`

```text
GetNavigationGenerationFinishedDelegate(WorldContext: UObject) -> Delegate
```

获取寻路图生成结束Delegate
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 当前世界上下文 |

**Returns**

| Type | Description |
|---|---|
| `Delegate` | 寻路图生成结束Delegate |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9F%BA%E7%A1%80%E5%8A%9F%E8%83%BD/UGCObjectUtility.json -->

# UGCObjectUtility

UObject基础接口库

## Functions

### `FindClass`

```text
FindClass(InClassName: string) -> UClass
```

通过类名(短路径)寻找类
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InClassName` | `string` | 类名 |

**Returns**

| Type | Description |
|---|---|
| `UClass` | 检索到的类 |

### `LoadClass`

```text
LoadClass(InClassPath: string) -> UClass
```

通过完整路径加载类，具体路径可以点击 "右键" - "copy reference" 得到路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InClassPath` | `string` | 类的路径 |

**Returns**

| Type | Description |
|---|---|
| `UClass` | 加载完成的类 |

### `AsyncLoadClass`

```text
AsyncLoadClass(InClassPath: string, Callback: function, Callback_self: UObject) -> boolean
```

通过完整路径异步加载蓝图 Class，路径规则与 LoadClass 相同
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InClassPath` | `string` | 类的路径 |
| `Callback` | `function` | lua普通函数或lambda函数, 加载完成的资源会作为参数传给CallBack函数 (注意带函数定义带冒号和不带的区别) |
| `Callback_self` | `UObject` | 这是为了兼容CallBack函数定义带冒号和不带冒号两种情况。如果带冒号(table:func()型,CallBack_self传入table);如果不带冒号,CallBack_self传入nil |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 加载是否成功 |

### `FindObject`

```text
FindObject(InObjectName: string) -> UObject
```

通过对象名寻找对象，会遍历所有包进行寻找，性能较差，且如果出现冲突，会有警告且返回其中一个
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObjectName` | `string` | 对象名 |

**Returns**

| Type | Description |
|---|---|
| `UObject` | 检索到的对象 |

### `LoadObject`

```text
LoadObject(InObjectPath: string) -> UObject
```

通过完整路径加载对象，性能较好
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObjectPath` | `string` | 对象的路径 |

**Returns**

| Type | Description |
|---|---|
| `UObject` | 加载的对象 |

### `AsyncLoadObject`

```text
AsyncLoadObject(InObjectPath: string, Callback: function, Callback_self: UObject) -> boolean
```

通过完整路径异步加载Object
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObjectPath` | `string` | 对象的路径 |
| `Callback` | `function` | lua普通函数或lambda函数, 加载完成的资源会作为参数传给CallBack函数 (注意带函数定义带冒号和不带的区别) |
| `Callback_self` | `UObject` | 这是为了兼容CallBack函数定义带冒号和不带冒号两种情况。如果带冒号(table:func()型,CallBack_self传入table);如果不带冒号,CallBack_self传入nil |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 加载是否成功 |

### `NewObject`

```text
NewObject(Outer: UObject, InClass: UClass, InObjectName: string) -> UObject
```

通过包名，类名和对象名创建对象
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Outer` | `UObject` | Outer 对象 |
| `InClass` | `UClass` | 类 |
| `InObjectName` | `string` | 对象名 |

**Returns**

| Type | Description |
|---|---|
| `UObject` | 创建的对象 |

### `NewStruct`

```text
NewStruct(InStructName: string, ...: any) -> userdata
```

创建新结构体对象，优先从已有的对象中查找是否有已创建对象。可传递结构体的构造参数，仅已导出结构体支持构造时赋值，传递非法参数时不保证结果正常。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStructName` | `string` | 不带 F 的结构体名字（比如 "Transform"、"ItemDefineID"） |
| `...` | `any` | 结构体的构造参数 |

**Returns**

| Type | Description |
|---|---|
| `userdata` | 新创建的结构体 |

### `NewStructAsTable`

```text
NewStructAsTable(InStructName: string, ...: any) -> table
```

以 lua table 形式创建新结构体，优先从已有的对象中查找是否有已创建对象。可传递结构体的构造参数，传递非法参数时不保证结果正常。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStructName` | `string` | 不带 F 的结构体名字（比如 "Transform"、"ItemDefineID"） |
| `...` | `any` | 结构体的构造参数 |

**Returns**

| Type | Description |
|---|---|
| `table` | 新创建的结构体 table |

### `GetObjectClass`

```text
GetObjectClass(InObject: UObject) -> UClass
```

通过一个对象获取对应的类
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObject` | `UObject` | 对象实例 |

**Returns**

| Type | Description |
|---|---|
| `UClass` | 对应的类 |

### `GetObjectOuter`

```text
GetObjectOuter(InObject: UObject) -> UObject
```

通过一个对象获取对应的包
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObject` | `UObject` | 对象实例 |

**Returns**

| Type | Description |
|---|---|
| `UObject` | 传入对象的 Outer 对象 |

### `GetObjectName`

```text
GetObjectName(InObject: UObject) -> string
```

获取对象的名字
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObject` | `UObject` | 对象实例 |

**Returns**

| Type | Description |
|---|---|
| `string` | 对象的名字 |

### `GetObjectFullName`

```text
GetObjectFullName(InObject: UObject) -> string
```

获取对象的类名以及完整路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObject` | `UObject` | 对象实例 |

**Returns**

| Type | Description |
|---|---|
| `string` | 对象的类以及完整路径 |

### `GetObjectPathName`

```text
GetObjectPathName(InObject: UObject) -> string
```

获取对象的完整路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObject` | `UObject` | 对象实例 |

**Returns**

| Type | Description |
|---|---|
| `string` | 对象的完整路径 |

### `IsObjectValid`

```text
IsObjectValid(InObject: UObject) -> boolean
```

判断对象是否有效
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObject` | `UObject` | 对象实例 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 对象是否有效的判断结果 |

### `IsA`

```text
IsA(InObject: UObject, InClass: UClass) -> boolean
```

判断一个对象是否是特定类的实例
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObject` | `UObject` | 对象实例 |
| `InClass` | `UClass` | 类 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 对象是否是特定类的实例的判断结果 |

### `MarkAsGarbage`

```text
MarkAsGarbage(InObject: UObject)
```

删除对象，将对象标记为带回收的垃圾
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObject` | `UObject` | 对象实例 |

### `MakeSoftObjectPath`

```text
MakeSoftObjectPath(InObjectPath: string) -> FSoftObjectPath
```

通过完整对象路径创建软路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObjectPath` | `string` | 对象的路径 |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | 创建的软路径 |

### `GetPathBySoftObjectPath`

```text
GetPathBySoftObjectPath(InSoftObjectPath: FSoftObjectPath) -> string
```

获取软路径获取对象完整路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSoftObjectPath` | `FSoftObjectPath` | 对象的软路径 |

**Returns**

| Type | Description |
|---|---|
| `string` | 对象的完整路径 |

### `LoadObjectBySoftPath`

```text
LoadObjectBySoftPath(InSoftObjectPath: FSoftObjectPath) -> boolean
```

通过软路径加载对象
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSoftObjectPath` | `FSoftObjectPath` | 对象的软路径 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 加载是否成功 |

### `AsyncLoadObjectBySoftPath`

```text
AsyncLoadObjectBySoftPath(InSoftObjectPath: FSoftObjectPath, Callback: function, Callback_Self: UObject) -> boolean
```

通过软路径异步加载对象
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSoftObjectPath` | `FSoftObjectPath` | 对象的软路径 |
| `Callback` | `function` | lua普通函数或lambda函数, 加载完成的资源会作为参数传给CallBack函数 (注意带函数定义带冒号和不带的区别) |
| `Callback_Self` | `UObject` | 这是为了兼容CallBack函数定义带冒号和不带冒号两种情况。如果带冒号(table:func()型,CallBack_self传入table);如果不带冒号,CallBack_self传入nil |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 加载是否成功 |

### `GetAllActorsOfClass`

```text
GetAllActorsOfClass(WorldContextObject: UObject, ActorClass: UClass) -> AActor[]
```

【废弃】请使用UGCActorComponentUtility.GetAllActorsOfClass
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界中任意对象 |
| `ActorClass` | `UClass` | 要找的Actor对应的类。必须指定，否则结果数组将为空 |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | 找到的Actor数组 |

### `RemoveReferencedObject`

```text
RemoveReferencedObject(Object: UObject)
```

移除引用关联（如果有UObject泄露等问题，可用此函数手动释放Lua侧对UObject的引用）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject` | 需要释放引用的 UObject |

### `GetObjectsOfClass`

```text
GetObjectsOfClass(Class: UClass, bIncludeDerivedClasses: boolean) -> UObject[]
```

以 lua table 形式获取某个类的所有对象列表

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Class` | `UClass` | 要找的 UObject 对应的类 |
| `bIncludeDerivedClasses` | `boolean` | 是否包括派生类 |

**Returns**

| Type | Description |
|---|---|
| `UObject[]` | 找到的 UObject 数组 |

### `GetObjectsWithOuter`

```text
GetObjectsWithOuter(Outer: UObject, bIncludeNestedObjects: boolean) -> UObject[]
```

以 lua table 形式获取以目标对象为 Outer 的所有 UObject 列表

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Outer` | `UObject` | Outer 对象 |
| `bIncludeNestedObjects` | `boolean` | 是否包括嵌套对象 |

**Returns**

| Type | Description |
|---|---|
| `UObject[]` | 找到的 UObject 数组 |

### `ClassIsChildOf`

```text
ClassIsChildOf(TestClass: UClass, ParentClass: UClass) -> boolean
```

判断一个类是否是另一个类的子类

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TestClass` | `UClass` | 子类 |
| `ParentClass` | `UClass` | 父类 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果TestClass等于ParentClass，或者TestClass是ParentClass的子类则返回true；否则返回false。如果任一参数为'None'也返回false |

### `GetDisplayName`

```text
GetDisplayName(Object: UObject) -> string
```

获取对象的显示名称
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject` | 对象实例 |

**Returns**

| Type | Description |
|---|---|
| `string` | 对象的显示名称 |

### `GetClassDefaultObject`

```text
GetClassDefaultObject(Class: UClass) -> UObject
```

获取类默认对象
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Class` | `UClass` | 类 |

**Returns**

| Type | Description |
|---|---|
| `UObject` | 类默认对象 |

### `MakeWeakObjectPtr`

```text
MakeWeakObjectPtr(InObject: UObject) -> WeakObjectPtr
```

创建弱对象指针
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

从弱对象指针获取对象
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

判断弱对象指针是否有效
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InWeakObjectPtr` | `WeakObjectPtr` | 弱对象指针 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否有效 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%A7%92%E8%89%B2%E7%B3%BB%E7%BB%9F/UGCPawnAttrSystem.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%A7%92%E8%89%B2%E7%B3%BB%E7%BB%9F/UGCPawnSystem.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%8A%80%E8%83%BD%E7%B3%BB%E7%BB%9F/UGCPersistEffectSystem.json -->

# UGCPersistEffectSystem

新技能和Buff系统接口库

## Functions

### `AddSkillByClass`

```text
AddSkillByClass(TargetActor: AActor, SkillClass: UClass|string, OverrideApplyTime: number, Slot: UGCGameplayTag|string|FGameplayTag) -> UPersistEffectSkill
```

给指定拥有新技能组件的目标 Actor 添加技能
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标Actor |
| `SkillClass` | `UClass\|string` | 技能蓝图类或蓝图路径 |
| `OverrideApplyTime` | `number` | 技能生效时长(可选，默认为技能类中配置的时长) |
| `Slot` | `UGCGameplayTag\|string\|FGameplayTag` | 由Tag标识的技能槽位 |

**Returns**

| Type | Description |
|---|---|
| `UPersistEffectSkill` | 技能对象 |

### `RemoveSkillInstance`

```text
RemoveSkillInstance(TargetActor: AActor, SkillInstance: UPersistEffectSkill) -> boolean
```

给指定拥有新技能组件的目标 Actor 移除技能
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `SkillInstance` | `UPersistEffectSkill` | 技能对象 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否移除成功 |

### `GetSkillsByClass`

```text
GetSkillsByClass(TargetActor: AActor, SkillClass: UClass|string) -> UPersistEffectSkill[]
```

从指定拥有新技能组件的目标 Actor 获取指定类型的技能
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标Actor |
| `SkillClass` | `UClass\|string` | 技能蓝图类或蓝图路径,为空时获取所有技能 |

**Returns**

| Type | Description |
|---|---|
| `UPersistEffectSkill[]` | 技能列表 |

### `GetSkillsByTag`

```text
GetSkillsByTag(TargetActor: AActor, Tag: UGCGameplayTag|string|FGameplayTag) -> UPersistEffectSkill[]
```

从指定拥有新技能组件的目标 Actor 获取拥有指定 Tag 的技能
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标Actor |
| `Tag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要获取的技能所包含的 Tag,为空时获取所有技能 |

**Returns**

| Type | Description |
|---|---|
| `UPersistEffectSkill[]` | 技能列表 |

### `AddBuffByClass`

```text
AddBuffByClass(TargetActor: AActor, BuffClass: UClass|string, Causer: AActor, OverrideDuration: number, StackNum: number) -> UPersistEffectBuff
```

给指定拥有新技能组件的目标 Actor 添加 Buff
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `BuffClass` | `UClass\|string` | Buff 蓝图类或蓝图路径 |
| `Causer` | `AActor` | Buff释放者（可选，默认为空） |
| `OverrideDuration` | `number` | 技能生效时长（可选，默认为-1代表Buff类中配置的时长） |
| `StackNum` | `number` | Buff的堆叠层数（可选，默认为 1 层） |

**Returns**

| Type | Description |
|---|---|
| `UPersistEffectBuff` | Buff对象 |

### `RemoveBuffByClass`

```text
RemoveBuffByClass(TargetActor: AActor, BuffClass: UClass|string, RemoveNum: number, Causer: AActor) -> boolean
```

给指定拥有新技能组件的目标 Actor 移除 Buff
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `BuffClass` | `UClass\|string` | Buff 蓝图类或蓝图路径 |
| `RemoveNum` | `number` | Buff减少堆叠数量（可选，默认-1移除全部层） |
| `Causer` | `AActor` | 筛选特定的释放者（可选，默认不筛选） |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否移除成功 |

### `RemoveBuffByTag`

```text
RemoveBuffByTag(TargetActor: AActor, Tag: UGCGameplayTag|string|FGameplayTag, RemoveNum: number, Causer: AActor) -> boolean
```

给指定拥有新技能组件的目标 Actor 移除包含某个 Tag 的 Buff
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `Tag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要移除的 Buff 所包含的 Tag |
| `RemoveNum` | `number` | Buff 减少堆叠数量（可选，默认移除全部层） |
| `Causer` | `AActor` | 筛选特定的释放者(可选，默认不筛选) |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否移除成功 |

### `GetBuffsByClass`

```text
GetBuffsByClass(TargetActor: AActor, BuffClass: UClass|string) -> UPersistEffectBuff[]
```

从指定拥有新技能组件的目标 Actor 获取指定类型的Buff
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标Actor |
| `BuffClass` | `UClass\|string` | Buff蓝图类或蓝图路径,为空时获取所有Buff |

**Returns**

| Type | Description |
|---|---|
| `UPersistEffectBuff[]` | Buff列表 |

### `GetBuffsByTag`

```text
GetBuffsByTag(TargetActor: AActor, Tag: UGCGameplayTag|string|FGameplayTag) -> UPersistEffectBuff[]
```

从指定拥有新技能组件的目标 Actor 获取拥有指定Tag的Buff
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标Actor |
| `Tag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要获取的 Buff 所包含的 Tag,为空时获取所有Buff |

**Returns**

| Type | Description |
|---|---|
| `UPersistEffectBuff[]` | Buff列表 |

### `HasDynamicState`

```text
HasDynamicState(TargetActor: AActor, DynamicStateTag: UGCGameplayTag|string|FGameplayTag) -> boolean
```

检查指定拥有新技能组件的目标 Actor 是否包含某个 Tag 标识的状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `DynamicStateTag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要检查的 Tag 标识的状态 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否拥有 Tag 标识的状态 |

### `AllowDynamicState`

```text
AllowDynamicState(TargetActor: AActor, DynamicStateTag: UGCGameplayTag|string|FGameplayTag) -> boolean
```

检查指定拥有新技能组件的目标 Actor 是否允许进入某个 Tag 标识的状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `DynamicStateTag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要检查的 Tag 标识的状态 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否允许进入 Tag 标识的状态 |

### `EnterDynamicState`

```text
EnterDynamicState(TargetActor: AActor, DynamicStateTag: UGCGameplayTag|string|FGameplayTag) -> boolean
```

尝试让拥有新技能组件的目标 Actor 获取指定 Tag 标识的状态，多次获取同一个 Tag 会叠加计数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `DynamicStateTag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要添加的 Tag 标识的状态 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否成功 |

### `LeaveDynamicState`

```text
LeaveDynamicState(TargetActor: AActor, DynamicStateTag: UGCGameplayTag|string|FGameplayTag) -> boolean
```

尝试从拥有新技能组件的目标 Actor 移除指定 Tag 标识的状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `DynamicStateTag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要移除的 Tag 标识的状态 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否有剩余的 Tag。若移除 Tag 的一次计数后还有剩余则返回 False，若全部没有剩余则返回 True |

### `InterruptDynamicState`

```text
InterruptDynamicState(TargetActor: AActor, DynamicStateTag: UGCGameplayTag|string|FGameplayTag) -> boolean
```

将拥有新技能组件的目标 Actor 的 Tag 标识的状态移除并触发打断事件
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `DynamicStateTag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要打断的 Tag 标识的状态 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否成功打断 |

### `SetDynamicStateDisabled`

```text
SetDynamicStateDisabled(TargetActor: AActor, DynamicStateTag: UGCGameplayTag|string|FGameplayTag, bNewDisabled: boolean, bInterrupt: boolean)
```

设置由 Tag 标识的状态的是否禁用，Actor 中 Tag 的禁用计数大于 0 时禁用生效
 - bNewDisabled == True：将拥有新技能组件的目标 Actor 的一组 Tag 标识的状态进行打断，并为这一组 Tag 的禁用计数 +1
 - bNewDisabled == false：将拥有新技能组件的目标 Actor 的一组 Tag 标识的状态禁用计数 -1
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `DynamicStateTag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要增加或减少禁用的 Tag 标识的状态 |
| `bNewDisabled` | `boolean` | 是否禁用 |
| `bInterrupt` | `boolean` | 是否打断，默认为 true |

### `ResetDynamicStateDisabled`

```text
ResetDynamicStateDisabled(TargetActor: AActor, DynamicStateTag: UGCGameplayTag|string|FGameplayTag)
```

重置被禁用的由 Tag 标识的状态，重置后目标 Actor 将允许进入这个 Tag 标识的状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `DynamicStateTag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要增加或减少禁用的 Tag 标识的状态 |

### `GetPersistBaseComponentByContent`

```text
GetPersistBaseComponentByContent(TargetActor: AActor) -> @UPersistBaseComponent
```

从拥有新技能组件的目标 Actor 上获取 PersistBaseComponent 组件
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |

**Returns**

| Type | Description |
|---|---|
| `@UPersistBaseComponent` | 组件 |

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

### `AddFresnelEffect`

```text
AddFresnelEffect(TargetCharacter: ACharacter, Color: FLinearColor, Duration: number)
```

添加菲涅尔效果
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetCharacter` | `ACharacter` | 被透视的角色或怪 |
| `Color` | `FLinearColor` | 颜色 |
| `Duration` | `number` | 时长 |

### `PickTargets`

```text
PickTargets(OwnerActor: AActor, StartTransform: FTransform, TargetPickerParams: FTargetPickerParams, IgnoreActors: AActor[]) -> AActor[]
```

选取参数指定范围内的目标
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor` | 发起选目标的角色 |
| `StartTransform` | `FTransform` | Picker开始位置 |
| `TargetPickerParams` | `FTargetPickerParams` | Picker参数 |
| `IgnoreActors` | `AActor[]` | 忽略的Actors |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | 选中的目标 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%A7%92%E8%89%B2%E7%B3%BB%E7%BB%9F/UGCPlayerControllerSystem.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCPlayerPawnSystem.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%A7%92%E8%89%B2%E7%B3%BB%E7%BB%9F/UGCPlayerStateSystem.json -->

# UGCPlayerStateSystem

玩家数据/状态系统接口库

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCPlayerStateSystem._CrossPlayerChunkDataCallbacks` | `-` | - |
| `UGCPlayerStateSystem._CrossPlayerChunkDataRequestID` | `-` | - |

## Functions

### `IsAlive`

```text
IsAlive(PlayerKey: number) -> boolean
```

是否存活
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `IsExit`

```text
IsExit(PlayerKey: number) -> boolean
```

是否离开游戏（主动退出，非断线）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetUGCVIPLevel`

```text
GetUGCVIPLevel(PlayerKey: number) -> number
```

获取 VIP Level
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetPlayerAccountInfo`

```text
GetPlayerAccountInfo(PlayerKey: number) -> FPlayerAccountInfo
```

获取玩家的账号数据
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `FPlayerAccountInfo` | - |

### `GetPlayerBattleInfo`

```text
GetPlayerBattleInfo(PlayerKey: number) -> FPlayerBattleInfo
```

获取玩家的战斗数据
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `FPlayerBattleInfo` | - |

### `SavePlayerArchiveData`

```text
SavePlayerArchiveData(UID: number, ArchiveData: table) -> boolean
```

保存玩家存档数据（存档数据在 PIE 下无法跨对局保存和读取）!!!!注意，不能在对局结算之后保存存档数据，在对局结算后调用此接口无法成功保存存档数据
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |
| `ArchiveData` | `table` | 存档数据 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `SavePlayerArchiveDataByKey`

```text
SavePlayerArchiveDataByKey(UID: number, Key: string, Value: any) -> boolean
```

按key保存玩家存档数据（存档数据在 PIE 下无法跨对局保存和读取）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |
| `Key` | `string` | 要保存的键名 |
| `Value` | `any` | 要保存的值 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetPlayerArchiveData`

```text
GetPlayerArchiveData(UID: number) -> table
```

获取玩家存档数据（存档数据在 PIE 下无法跨对局保存和读取）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |

**Returns**

| Type | Description |
|---|---|
| `table` | 存档数据 |

### `GetPlayerArchiveDataByKey`

```text
GetPlayerArchiveDataByKey(UID: number, Key: string) -> any
```

按key获取玩家存档数据（存档数据在 PIE 下无法跨对局保存和读取）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |
| `Key` | `string` | 要获取的键名 |

**Returns**

| Type | Description |
|---|---|
| `any` | 对应key的值，key不存在时返回nil |

### `GetTableDataSize`

```text
GetTableDataSize(Data: table) -> number
```

计算Lua table序列化后的字节大小
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Data` | `table` | 要计算大小的table |

**Returns**

| Type | Description |
|---|---|
| `number` | 序列化后的字节大小，计算失败返回-1 |

### `GetPlayerDataSize`

```text
GetPlayerDataSize(UID: number) -> number
```

获取玩家存档数据的总字节大小
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |

**Returns**

| Type | Description |
|---|---|
| `number` | 存档数据的总字节大小，无数据时返回0 |

### `ClearPlayerArchiveData`

```text
ClearPlayerArchiveData()
```

清理玩家存档数据（GM 指令，仅开发环境生效）
生效范围：客户端

### `GetPlayerPlatformGender`

```text
GetPlayerPlatformGender(PlatformGender: number, UID: number) -> number
```

获取玩家账号性别
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlatformGender` | `number` | 从DS获取的玩家性别 |
| `UID` | `number` | 玩家UID |

**Returns**

| Type | Description |
|---|---|
| `number` | 玩家账号性别，0 - 隐藏，1 - 男，2 - 女 |

### `GetTeamID`

```text
GetTeamID(PlayerKey: number) -> number
```

获取 TeamID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetPlayerKeyInt64`

```text
GetPlayerKeyInt64(PlayerState: PlayerState) -> number
```

获取 64 位玩家 PlayerKey
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerState` | `PlayerState` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetPlayerKey`

```text
GetPlayerKey(PlayerState: PlayerState) -> string
```

获取字符串玩家 PlayerKey
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerState` | `PlayerState` | - |

**Returns**

| Type | Description |
|---|---|
| `string` | - |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/UGCPrivilegeSystem.json -->

# UGCPrivilegeSystem

特权系统接口库

## Functions

### `GetPlayerPrivilegesInformation`

```text
GetPlayerPrivilegesInformation(UID: number) -> table
```

获取玩家特权 ID 信息列表，如果玩家没有特权 ID 信息或者在 PIE 环境下返回 nil
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家UID |

**Returns**

| Type | Description |
|---|---|
| `table` | 玩家特权ID信息列表，table = { [id1] = { Description = "" }, [id2] = { Description = "" }, [id3] = { Description = "" }, ... } |

### `DoesPlayerHavePrivileges`

```text
DoesPlayerHavePrivileges(UID: number) -> boolean
```

判断玩家是否拥有特权，没有特权或者在 PIE 环境下返回 false
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家UID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 玩家是否拥有特权 |

### `AddPrivilegeEmblemFlagUI`

```text
AddPrivilegeEmblemFlagUI(PlayerState: PlayerState, NameColorHexStr: string, bHideTeammatePositionItemName: boolean)
```

给指定队友（不包含主控玩家自己）添加绿洲特权徽章UI标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerState` | `PlayerState` | 队友PlayerState |
| `NameColorHexStr` | `string` | 玩家名字颜色 |
| `bHideTeammatePositionItemName` | `boolean` | 是否隐藏队友标记名 |

### `RemovePrivilegeEmblemFlagUI`

```text
RemovePrivilegeEmblemFlagUI(PlayerState: PlayerState)
```

给指定队友（不包含主控玩家自己）移除绿洲特权徽章UI标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerState` | `PlayerState` | 队友PlayerState |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%8A%80%E8%83%BD%E7%B3%BB%E7%BB%9F/UGCProjectileSystem.json -->

# UGCProjectileSystem

抛体系统接口库

## Functions

### `SpawnProjectile`

```text
SpawnProjectile(ProjectileSpawnInfo: ProjectileSpawnInfo) -> APVEProjectileBase
```

生成抛体
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProjectileSpawnInfo` | `ProjectileSpawnInfo` | 抛体生成参数 |

**Returns**

| Type | Description |
|---|---|
| `APVEProjectileBase` | 抛体对象实例 |

### `GetDestroyAfterHit`

```text
GetDestroyAfterHit(Projectile: APVEProjectileBase) -> boolean
```

获取抛体命中之后是否销毁
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APVEProjectileBase` | 抛体 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否命中后销毁 |

### `SetDestroyAfterHit`

```text
SetDestroyAfterHit(Projectile: APVEProjectileBase, bNewDestroyAfterHit: boolean)
```

设置抛体命中之后是否销毁
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APVEProjectileBase` | 抛体 |
| `bNewDestroyAfterHit` | `boolean` | 是否销毁 |

### `GetPMComp`

```text
GetPMComp(Projectile: APVEProjectileBase) -> boolean
```

获取抛体运动组件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APVEProjectileBase` | 抛体 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 抛体运动组件 |

### `SetMoveAfterImpactWithNoLost`

```text
SetMoveAfterImpactWithNoLost(Projectile: APVEProjectileBase, bNeedUpdateImmide: boolean)
```

设置抛体命中之后是否继续移动
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APVEProjectileBase` | 抛体 |
| `bNeedUpdateImmide` | `boolean` | 是否更新组件速度 |

### `GetLastUpdateCompBeforeStop`

```text
GetLastUpdateCompBeforeStop(Projectile: APVEProjectileBase) -> boolean
```

停止前最后更新的组件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APVEProjectileBase` | 抛体 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 最后更新的组件 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%8A%80%E8%83%BD%E7%B3%BB%E7%BB%9F/UGCProjectileSystemV2.json -->

# UGCProjectileSystemV2

技能抛体系统接口库

## Functions

### `CreateProjectile`

```text
CreateProjectile(ProjectileClass: UClass, Owner: AActor, Location: FVector, Direction: FVector, Speed: number, GravityScale: number, DamageValue: number, DamageType: FRestrictedDamageTypeData) -> APESkillProjectileBase
```

发射技能抛体
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProjectileClass` | `UClass` | 抛体类型 |
| `Owner` | `AActor` | 新生成抛体的所属对象 |
| `Location` | `FVector` | 生成坐标 |
| `Direction` | `FVector` | 初始方向 |
| `Speed` | `number` | 初始速度 |
| `GravityScale` | `number` | 初始重力系数 |
| `DamageValue` | `number` | 抛体的伤害值 |
| `DamageType` | `FRestrictedDamageTypeData` | 抛体的伤害类型 |

**Returns**

| Type | Description |
|---|---|
| `APESkillProjectileBase` | 抛体实例 |

### `CreateProjectileSimple`

```text
CreateProjectileSimple(ProjectileClass: UClass, Owner: AActor, Location: FVector, Direction: FVector, Speed: number, GravityScale: number, Target: number) -> APESkillProjectileBase
```

发射技能抛体（不传递伤害）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProjectileClass` | `UClass` | 抛体类型 |
| `Owner` | `AActor` | 新生成抛体的所属对象 |
| `Location` | `FVector` | 生成坐标 |
| `Direction` | `FVector` | 初始方向 |
| `Speed` | `number` | 初始速度 |
| `GravityScale` | `number` | 初始重力系数 |
| `Target` | `number` | 抛体的伤害值 |

**Returns**

| Type | Description |
|---|---|
| `APESkillProjectileBase` | 抛体实例 |

### `SetDirection`

```text
SetDirection(Projectile: APESkillProjectileBase, NewDirection: FVector)
```

设置抛体速度方向
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |
| `NewDirection` | `FVector` | 新方向 |

### `SetSpeed`

```text
SetSpeed(Projectile: APESkillProjectileBase, NewSpeed: number)
```

设置抛体速度大小
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |
| `NewSpeed` | `number` | 新速度 |

### `SetGravityScale`

```text
SetGravityScale(Projectile: APESkillProjectileBase, NewGravityScale: number)
```

设置抛体重力系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |
| `NewGravityScale` | `number` | 新重力系数 |

### `SetDamage`

```text
SetDamage(Projectile: APESkillProjectileBase, NewDamage: number)
```

设置抛体伤害，会覆盖所有的伤害值，伤害方式会调整为常量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |
| `NewDamage` | `number` | 伤害值 |

### `SetTarget`

```text
SetTarget(Projectile: APESkillProjectileBase, NewTarget: APawn)
```

设置抛体目标
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |
| `NewTarget` | `APawn` | 新的目标单位 |

### `GetProjectileMovementComponent`

```text
GetProjectileMovementComponent(Projectile: APESkillProjectileBase) -> UProjectileMovementComponent
```

获取抛体移动组件
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |

**Returns**

| Type | Description |
|---|---|
| `UProjectileMovementComponent` | 抛体组件类 |

### `GetDirection`

```text
GetDirection(Projectile: APESkillProjectileBase) -> FVector
```

获取抛体速度方向
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 当前速度方向 |

### `GetSpeed`

```text
GetSpeed(Projectile: APESkillProjectileBase) -> number
```

获取抛体速度大小
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |

**Returns**

| Type | Description |
|---|---|
| `number` | 新速度 |

### `GetGravityScale`

```text
GetGravityScale(Projectile: APESkillProjectileBase) -> number
```

获取抛体重力系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |

**Returns**

| Type | Description |
|---|---|
| `number` | 新重力系数 |

### `GetTarget`

```text
GetTarget(Projectile: APESkillProjectileBase) -> APawn
```

获取抛体目标
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |

**Returns**

| Type | Description |
|---|---|
| `APawn` | 新的目标单位 |

### `GetProjectileListByGroupKey`

```text
GetProjectileListByGroupKey(TargetActor: APESkillProjectileBase, GroupKey: string) -> APESkillProjectileBase[]
```

获取抛体组中的抛体
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `APESkillProjectileBase` | 发射抛体的角色 |
| `GroupKey` | `string` | 抛体组Key |

**Returns**

| Type | Description |
|---|---|
| `APESkillProjectileBase[]` | 抛体组中的抛体 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E6%B3%95%E8%A7%84%E5%88%99/UGCRankSystem.json -->

# UGCRankSystem

段位专用接口库

## Functions

### `GetUGCRank`

```text
GetUGCRank(PlayerKey: number) -> number
```

查询段位分
调用 UGCRankSystem.AddRankProgress 后，会获取到新段位分
例：开局 2000 积分，中途调用 UGCRankSystem.AddRankProgress 增加 100 积分，再调用 UGCRankSystem.GetUGCRank 则得到 2100 积分
详细使用流程参考 wiki (https://developer.gp.qq.com/wiki/#/lvzhou_duanwei.html)
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 PlayerKey |

**Returns**

| Type | Description |
|---|---|
| `number` | 段位分 |

### `AddRankProgress`

```text
AddRankProgress(PlayerKey: number, Count: number)
```

修改段位分
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 PlayerKey |
| `Count` | `number` | 段位分变化值 |

### `GetUGCGameSeasonId`

```text
GetUGCGameSeasonId() -> number
```

查询当前玩法段位赛 ID
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `number` | 游戏赛季 ID |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/UGCSceneQueryUtility.json -->

# UGCSceneQueryUtility

环境查询工具库

## Functions

### `QueryByLineSingle`

```text
QueryByLineSingle(WorldContextObject: UObject, Start: FVector, End: FVector, QueryType: ESceneQueryType, ActorsToIgnore: AActor[], IgnoreSelf: boolean) -> FHitResult
```

使用射线执行一次环境查询（单个目标）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 射线起点 |
| `End` | `FVector` | 射线终点 |
| `QueryType` | `ESceneQueryType` | 环境查询类型 |
| `ActorsToIgnore` | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| `IgnoreSelf` | `boolean` | 是否忽略自身（默认值：true） |

**Returns**

| Type | Description |
|---|---|
| `FHitResult` | 查询结果，是否找到 |

### `QueryByLineMulti`

```text
QueryByLineMulti(WorldContextObject: UObject, Start: FVector, End: FVector, QueryType: ESceneQueryType, ActorsToIgnore: AActor[], IgnoreSelf: boolean) -> FHitResult[]
```

使用射线执行一次环境查询（多个目标）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 射线起点 |
| `End` | `FVector` | 射线终点 |
| `QueryType` | `ESceneQueryType` | 环境查询类型 |
| `ActorsToIgnore` | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| `IgnoreSelf` | `boolean` | 是否忽略自身（默认值：true） |

**Returns**

| Type | Description |
|---|---|
| `FHitResult[]` | 查询结果数组，是否找到 |

### `QueryBySphereSingle`

```text
QueryBySphereSingle(WorldContextObject: UObject, Start: FVector, End: FVector, QueryType: ESceneQueryType, Radius: number, ActorsToIgnore: AActor[], IgnoreSelf: boolean) -> FHitResult
```

使用球体执行一次环境查询（单个目标）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 射线起点 |
| `End` | `FVector` | 射线终点 |
| `QueryType` | `ESceneQueryType` | 环境查询类型 |
| `Radius` | `number` | 球体半径（默认值：100） |
| `ActorsToIgnore` | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| `IgnoreSelf` | `boolean` | 是否忽略自身（默认值：true） |

**Returns**

| Type | Description |
|---|---|
| `FHitResult` | 查询结果数组，是否找到 |

### `QueryBySphereMulti`

```text
QueryBySphereMulti(WorldContextObject: UObject, Start: FVector, End: FVector, QueryType: ESceneQueryType, Radius: number, ActorsToIgnore: AActor[], IgnoreSelf: boolean) -> FHitResult[]
```

使用球体执行一次环境查询（多个目标）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 射线起点 |
| `End` | `FVector` | 射线终点 |
| `QueryType` | `ESceneQueryType` | 环境查询类型 |
| `Radius` | `number` | 球体半径（默认值：100） |
| `ActorsToIgnore` | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| `IgnoreSelf` | `boolean` | 是否忽略自身（默认值：true） |

**Returns**

| Type | Description |
|---|---|
| `FHitResult[]` | 查询结果数组，是否找到 |

### `QueryByBoxSingle`

```text
QueryByBoxSingle(WorldContextObject: UObject, Start: FVector, End: FVector, QueryType: ESceneQueryType, HalfSize: FVector, Orientation: FRotator, ActorsToIgnore: AActor[], IgnoreSelf: boolean) -> FHitResult
```

使用盒子执行一次环境查询（单个目标）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 射线起点 |
| `End` | `FVector` | 射线终点 |
| `QueryType` | `ESceneQueryType` | 环境查询类型 |
| `HalfSize` | `FVector` | 各轴到盒子中心的距离（默认值：X = 25, Y = 25, Z = 25） |
| `Orientation` | `FRotator` | 盒子朝向（默认值：Pitch = 0, Yaw = 0, Roll = 0） |
| `ActorsToIgnore` | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| `IgnoreSelf` | `boolean` | 是否忽略自身（默认值：true） |

**Returns**

| Type | Description |
|---|---|
| `FHitResult` | 查询结果数组，是否找到 |

### `QueryByBoxMulti`

```text
QueryByBoxMulti(WorldContextObject: UObject, Start: FVector, End: FVector, QueryType: ESceneQueryType, HalfSize: FVector, Orientation: FRotator, ActorsToIgnore: AActor[], IgnoreSelf: boolean) -> FHitResult[]
```

使用盒子执行一次环境查询（多个目标）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 射线起点 |
| `End` | `FVector` | 射线终点 |
| `QueryType` | `ESceneQueryType` | 环境查询类型 |
| `HalfSize` | `FVector` | 各轴到盒子中心的距离（默认值：X = 25, Y = 25, Z = 25） |
| `Orientation` | `FRotator` | 盒子朝向（默认值：Pitch = 0, Yaw = 0, Roll = 0） |
| `ActorsToIgnore` | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| `IgnoreSelf` | `boolean` | 是否忽略自身（默认值：true） |

**Returns**

| Type | Description |
|---|---|
| `FHitResult[]` | 查询结果数组，是否找到 |

### `QueryByCapsuleSingle`

```text
QueryByCapsuleSingle(WorldContextObject: UObject, Start: FVector, End: FVector, QueryType: ESceneQueryType, Radius: number, HalfHeight: number, ActorsToIgnore: AActor[], IgnoreSelf: boolean) -> FHitResult
```

使用胶囊执行一次环境查询（单个目标）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 胶囊起点 |
| `End` | `FVector` | 胶囊终点 |
| `QueryType` | `ESceneQueryType` | 环境查询类型 |
| `Radius` | `number` | 胶囊半径（默认值：100） |
| `HalfHeight` | `number` | 胶囊高度（默认值：50） |
| `ActorsToIgnore` | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| `IgnoreSelf` | `boolean` | 是否忽略自身（默认值：true） |

**Returns**

| Type | Description |
|---|---|
| `FHitResult` | 查询结果数组，是否找到 |

### `QueryByCapsuleMulti`

```text
QueryByCapsuleMulti(WorldContextObject: UObject, Start: FVector, End: FVector, QueryType: ESceneQueryType, Radius: number, HalfHeight: number, ActorsToIgnore: AActor[], IgnoreSelf: boolean) -> FHitResult[]
```

使用胶囊执行一次环境查询（多个目标）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 胶囊起点 |
| `End` | `FVector` | 胶囊终点 |
| `QueryType` | `ESceneQueryType` | 环境查询类型 |
| `Radius` | `number` | 胶囊半径（默认值：100） |
| `HalfHeight` | `number` | 胶囊高度（默认值：50） |
| `ActorsToIgnore` | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| `IgnoreSelf` | `boolean` | 是否忽略自身（默认值：true） |

**Returns**

| Type | Description |
|---|---|
| `FHitResult[]` | 查询结果数组，是否找到 |

### `QueryOverlapActorsBySphere`

```text
QueryOverlapActorsBySphere(WorldContextObject: UObject, Position: FVector, QueryType: ESceneQueryType, Radius: number, ActorsToIgnore: AActor[], ActorClassFilter: UClass, OutActors: AActor[]) -> AActor[]
```

使用球体检测重叠的Actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Position` | `FVector` | 球体中心位置 |
| `QueryType` | `ESceneQueryType` | 环境查询类型 |
| `Radius` | `number` | 球体半径（默认值：100） |
| `ActorsToIgnore` | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| `ActorClassFilter` | `UClass` | Actor类型过滤器（默认值：nil） |
| `OutActors` | `AActor[]` | 输出的Actor数组（如果为nil则创建新数组） |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | 是否找到重叠的Actor，重叠的Actor数组 |

### `QueryByBoxMultiForObjects`

```text
QueryByBoxMultiForObjects(WorldContextObject: UObject, Start: FVector, End: FVector, HalfSize: FVector, Orientation: FRotator, ObjectTypes: EObjectTypeQuery[], bTraceComplex: boolean, ActorsToIgnore: AActor[], DrawDebugType: EDrawDebugTrace, OutHits: FHitResult[], bIgnoreSelf: boolean, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: number) -> FHitResult[]
```

返回所有跟Box沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `HalfSize` | `FVector` | Box边的半长尺寸 |
| `Orientation` | `FRotator` | Box的朝向 |
| `ObjectTypes` | `EObjectTypeQuery[]` | 要检测的对象类型数组 |
| `bTraceComplex` | `boolean` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `AActor[]` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace` | 绘制调试类型 |
| `OutHits` | `FHitResult[]` | 存储所有碰撞结果 |
| `bIgnoreSelf` | `boolean` | 是否忽略自身 |
| `TraceColor` | `FLinearColor` | 未命中时的调试线颜色 |
| `TraceHitColor` | `FLinearColor` | 命中时的调试线颜色 |
| `DrawTime` | `number` | 绘制时间 |

**Returns**

| Type | Description |
|---|---|
| `FHitResult[]` | 是否检测到碰撞，碰撞结果数组 |

### `QueryOverlapActorsBySphereWithFinder`

```text
QueryOverlapActorsBySphereWithFinder(WorldContextObject: UObject, Finder: AActor, Origin: FVector, Radius: number, Channel: ECollisionChannel) -> FHitResult[]
```

在指定位置和半径的球体范围内检测所有重叠的Actor对象

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Finder` | `AActor` | 检测发起者，不被检测 |
| `Origin` | `FVector` | 球体中心位置 |
| `Radius` | `number` | 球体半径 |
| `Channel` | `ECollisionChannel` | 碰撞通道，默认为ECollisionChannel.ECC_WorldDynamic |

**Returns**

| Type | Description |
|---|---|
| `FHitResult[]` | 碰撞结果数组 |

### `QueryBlocksByChannel`

```text
QueryBlocksByChannel(WorldContextObject: UObject, Start: FVector, End: FVector, OutHits: FHitResult[], IgnoreActors: AActor[], TraceChannels: ECollisionChannel[]) -> FHitResult[]
```

检测从起点到终点之间所有阻挡物体的碰撞信息

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `OutHits` | `FHitResult[]` | 存储所有碰撞结果 |
| `IgnoreActors` | `AActor[]` | 需要忽略的Actor列表 |
| `TraceChannels` | `ECollisionChannel[]` | 需要检测的碰撞通道数组 |

**Returns**

| Type | Description |
|---|---|
| `FHitResult[]` | 是否检测到碰撞，碰撞结果数组 |

### `QueryBySphereMultiForObjects`

```text
QueryBySphereMultiForObjects(WorldContextObject: UObject, Start: FVector, End: FVector, Radius: number, ObjectTypes: EObjectTypeQuery[], bTraceComplex: boolean, ActorsToIgnore: AActor[], DrawDebugType: EDrawDebugTrace, OutHits: FHitResult[], bIgnoreSelf: boolean, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: number) -> boolean
```

返回所有跟球体沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文 |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `Radius` | `number` | 扫描球体的半径 |
| `ObjectTypes` | `EObjectTypeQuery[]` | 对象类型列表 |
| `bTraceComplex` | `boolean` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `AActor[]` | 要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace` | 调试模式 |
| `OutHits` | `FHitResult[]` | 碰撞结果列表，按从起点到终点的检测顺序排序。如果存在阻挡性碰撞，它将是列表中的最后一个碰撞结果 |
| `bIgnoreSelf` | `boolean` | 是否忽略自身 |
| `TraceColor` | `FLinearColor` | 未命中时的调试线颜色 |
| `TraceHitColor` | `FLinearColor` | 命中时的调试线颜色 |
| `DrawTime` | `number` | 调试线的持续时间 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果发生碰撞返回true，否则返回false |

### `QueryByLineMultiForObjects`

```text
QueryByLineMultiForObjects(WorldContextObject: UObject, Start: FVector, End: FVector, ObjectTypes: EObjectTypeQuery[], bTraceComplex: boolean, ActorsToIgnore: AActor[], DrawDebugType: EDrawDebugTrace, OutHits: FHitResult[], bIgnoreSelf: boolean, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: number) -> boolean
```

返回所有跟射线碰撞的物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | world上下文对象 |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `ObjectTypes` | `EObjectTypeQuery[]` | 对象类型列表 |
| `bTraceComplex` | `boolean` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `AActor[]` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace` | 调试模式 |
| `OutHits` | `FHitResult[]` | 输出的HitResult列表 |
| `bIgnoreSelf` | `boolean` | 是否忽略自身 |
| `TraceColor` | `FLinearColor` | 未命中时的调试线颜色 |
| `TraceHitColor` | `FLinearColor` | 命中时的调试线颜色 |
| `DrawTime` | `number` | 调试线的持续时间 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | true为检测到碰撞，false为未检测到碰撞 |

### `QueryByLineWithChannel`

```text
QueryByLineWithChannel(OutHit: FHitResult, ContextObject: UObject, Start: FVector, End: FVector, IgnoreActors: AActor[], TraceChannel: ECollisionChannel) -> boolean
```

返回指定通道的射线碰撞的物体的碰撞信息

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutHit` | `FHitResult` | 输出的HitResult |
| `ContextObject` | `UObject` | world上下文对象 |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `IgnoreActors` | `AActor[]` | 需要忽略的Actor列表 |
| `TraceChannel` | `ECollisionChannel` | 碰撞通道 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | true为检测到碰撞，false为未检测到碰撞 |

### `FindPositionToHoldCapsule`

```text
FindPositionToHoldCapsule(WorldContextObject: UObject, SourceLocation: FVector, CapsuleRotation: FRotator, CapsuleRadius: float, CapsuleHalfHeight: float, IgnoreActors: AActor[], DetectObjectTypes: EObjectTypeQuery[], Iterations: int, bNearestLocation: bool) -> boolean, FVector
```

获取一个目标位置附近能容纳胶囊体的坐标，以目标位置为中心，八方向向外迭代寻找位置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | World上下文 |
| `SourceLocation` | `FVector` | 目标位置 |
| `CapsuleRotation` | `FRotator` | 胶囊体的旋转 |
| `CapsuleRadius` | `float` | 胶囊体半径 |
| `CapsuleHalfHeight` | `float` | 胶囊体半高 |
| `IgnoreActors` | `AActor[]` | 需要忽略的Actor列表 |
| `DetectObjectTypes` | `EObjectTypeQuery[]` | 检测的对象类型列表 |
| `Iterations` | `int` | 检测迭代次数 |
| `bNearestLocation` | `bool` | 是否返回最近的位置 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否找到合适的位置 |
| `FVector` | 找到的坐标 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%80%AA%E7%89%A9%E7%B3%BB%E7%BB%9F/UGCSimpleCharacterSystem.json -->

# UGCSimpleCharacterSystem

怪物小动物系统接口库

## Functions

### `GetHealth`

```text
GetHealth(SimpleCharacter: ASTExtraSimpleCharacterBase) -> number
```

获取当前血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SimpleCharacter` | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |

**Returns**

| Type | Description |
|---|---|
| `number` | 血量 |

### `SetHealth`

```text
SetHealth(SimpleCharacter: ASTExtraSimpleCharacterBase, Health: number)
```

设置当前血量（不会超过血量最大值）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SimpleCharacter` | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |
| `Health` | `number` | 血量 |

### `GetHealthMax`

```text
GetHealthMax(SimpleCharacter: ASTExtraSimpleCharacterBase) -> number
```

获取当前最大血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SimpleCharacter` | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |

**Returns**

| Type | Description |
|---|---|
| `number` | 血量 |

### `SetHealthMax`

```text
SetHealthMax(SimpleCharacter: ASTExtraSimpleCharacterBase, HealthMax: number)
```

设置当前最大血量（当前血量不会随之变大，但如果超过最大血量，则会变小）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SimpleCharacter` | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |
| `HealthMax` | `number` | 最大血量 |

### `GetSpeedScale`

```text
GetSpeedScale(SimpleCharacter: ASTExtraSimpleCharacterBase) -> number
```

获取移动速度系数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SimpleCharacter` | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |

**Returns**

| Type | Description |
|---|---|
| `number` | 移动系数 |

### `SetSpeedScale`

```text
SetSpeedScale(SimpleCharacter: ASTExtraSimpleCharacterBase, SpeedScale: number)
```

设置移动速度系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SimpleCharacter` | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |
| `SpeedScale` | `number` | 移动系数 |

### `IsInvincible`

```text
IsInvincible(SimpleCharacter: ASTExtraSimpleCharacterBase) -> boolean
```

获取是否无敌
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SimpleCharacter` | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否无敌 |

### `SetInvincible`

```text
SetInvincible(SimpleCharacter: ASTExtraSimpleCharacterBase, IsInvincible: boolean)
```

设置是否无敌
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SimpleCharacter` | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |
| `IsInvincible` | `boolean` | 是否无敌 |

### `IsAlive`

```text
IsAlive(SimpleCharacter: ASTExtraSimpleCharacterBase) -> boolean
```

获取是否存活
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SimpleCharacter` | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否存活 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%8A%80%E8%83%BD%E7%B3%BB%E7%BB%9F/UGCSkillManagerSystem.json -->

# UGCSkillManagerSystem

【废弃】技能管理系统接口库

## Functions

### `GetSkillManagerComponent`

```text
GetSkillManagerComponent(Actor: Actor) -> SkillManagerComponent
```

【废弃】请使用 UGCPersistEffectSystem
获取技能组件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |

**Returns**

| Type | Description |
|---|---|
| `SkillManagerComponent` | 技能组件 |

### `UseSkill`

```text
UseSkill(Actor: Actor, SkillName: string)
```

【废弃】请使用 UGCPersistEffectSystem
使用技能（技能列表中，技能需配置 SET_KEY_DOWN 事件触发）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillName` | `string` | 技能短名 |

### `StopSkill`

```text
StopSkill(Actor: Actor, SkillName: string)
```

【废弃】请使用 UGCPersistEffectSystem
停止技能
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillName` | `string` | 技能短名 |

### `TriggerSkillEvent`

```text
TriggerSkillEvent(Actor: Actor, SkillName: string, EventType: UTSkillEventType)
```

【废弃】请使用 UGCPersistEffectSystem
使用技能（自定义触发事件类型）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillName` | `string` | 技能短名 |
| `EventType` | `UTSkillEventType` | 事件类型 |

### `UseSkillByPath`

```text
UseSkillByPath(Actor: Actor, SkillPath: string)
```

【废弃】请使用 UGCPersistEffectSystem
根据技能路径使用技能（技能列表中，技能需配置 SET_KEY_DOWN 事件触发）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillPath` | `string` | 技能完整路径 |

### `StopSkillByPath`

```text
StopSkillByPath(Actor: Actor, SkillPath: string)
```

【废弃】请使用 UGCPersistEffectSystem
根据技能路径停止技能
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillPath` | `string` | 技能完整路径 |

### `TriggerSkillEventByPath`

```text
TriggerSkillEventByPath(Actor: Actor, SkillPath: string, EventType: UTSkillEventType)
```

【废弃】请使用 UGCPersistEffectSystem
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillPath` | `string` | 技能完整路径 |
| `EventType` | `UTSkillEventType` | 事件类型 |

### `StopAllSkill`

```text
StopAllSkill(Actor: Actor)
```

【废弃】请使用 UGCPersistEffectSystem
停止所有技能
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |

### `AddSkill`

```text
AddSkill(Actor: Actor, SkillClassPath: string)
```

【废弃】请使用 UGCPersistEffectSystem
添加技能
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillClassPath` | `string` | 技能完整路径 |

### `RemoveSkill`

```text
RemoveSkill(Actor: Actor, SkillClassPath: string)
```

【废弃】请使用 UGCPersistEffectSystem
移除技能
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillClassPath` | `string` | 技能完整路径 |

### `IsSkillRunning`

```text
IsSkillRunning(Actor: Actor) -> boolean
```

【废弃】请使用 UGCPersistEffectSystem
当前是否有技能在执行
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否有技能在执行 |

### `GetSkillCD`

```text
GetSkillCD(Actor: Actor, SkillPath: string) -> number
```

【废弃】请使用 UGCPersistEffectSystem
获取技能冷却
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillPath` | `string` | 技能完整路径 |

**Returns**

| Type | Description |
|---|---|
| `number` | 技能冷却时间 |

### `SetSkillActive`

```text
SetSkillActive(Actor: Actor, SkillPath: string, NewActive: boolean)
```

【废弃】请使用 UGCPersistEffectSystem
激活技能
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillPath` | `string` | 技能完整路径 |
| `NewActive` | `boolean` | 技能状态 |

### `TriggerStringEvent`

```text
TriggerStringEvent(Actor: Actor, SkillPath: string, EventString: string)
```

【废弃】请使用 UGCPersistEffectSystem
向技能抛出一个字符串类型的事件
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillPath` | `string` | 技能完整路径 |
| `EventString` | `string` | 字符串事件 |

### `TriggerUAEEvent`

```text
TriggerUAEEvent(Actor: Actor, SkillPath: string, EventType: UAESkillEvent)
```

【废弃】请使用 UGCPersistEffectSystem
向技能抛出一个预定义的事件
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillPath` | `string` | 技能完整路径 |
| `EventType` | `UAESkillEvent` | 预定义事件 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%A4%BE%E4%BA%A4%E7%B3%BB%E7%BB%9F/UGCSoundManagerSystem.json -->

# UGCSoundManagerSystem

语音系统接口库

## Functions

### `PlaySound2D`

```text
PlaySound2D(AKEvent: UAkAudioEvent) -> number
```

播放 2D 音效
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AKEvent` | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取） |

**Returns**

| Type | Description |
|---|---|
| `number` | 音效 ID |

### `PlaySoundAtLocation`

```text
PlaySoundAtLocation(AKEvent: UAkAudioEvent, Location: Vector, Orientation: Rotator) -> number
```

在指定位置播放音效
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AKEvent` | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取），需要导入音效时选 3D |
| `Location` | `Vector` | 位置 |
| `Orientation` | `Rotator` | 旋转 可使用 Rotator.New(Roll,Pitch,Yaw) 创建,结构 {Roll=Roll, Pitch=Pitch, Yaw=Yaw} |

**Returns**

| Type | Description |
|---|---|
| `number` | 音效 ID |

### `PlaySoundAttachActor`

```text
PlaySoundAttachActor(AKEvent: UAkAudioEvent, AttachedActor: Actor, StopWhenAttachedToDestroyed: boolean) -> number
```

依附于 Actor 播放音效
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AKEvent` | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取） |
| `AttachedActor` | `Actor` | 依附的 Actor |
| `StopWhenAttachedToDestroyed` | `boolean` | 依附的 Actor 销毁时是否停止音效播放 |

**Returns**

| Type | Description |
|---|---|
| `number` | 音效 ID |

### `StopAllSound`

```text
StopAllSound()
```

停止全部音效
生效范围：客户端

### `StopSoundByActor`

```text
StopSoundByActor(Actor: Actor)
```

停止指定 Actor 上的所有音效
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | 指定的Actor |

### `StopSoundByID`

```text
StopSoundByID(ID: number)
```

停止指定 ID 的音效
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ID` | `number` | 音效 ID |

### `PlaySoundWithVolumePitch`

```text
PlaySoundWithVolumePitch(AKEvent: UAkAudioEvent, AttachedActor: Actor, Volume: number, Pitch: number, StopWhenAttachedToDestroyed: boolean) -> number
```

在以指定音量音高的方式播放音效，如果播放的是同一个音效，必须在上次播放完成再开始下一个播放，音效资源必须在最新的UGC编辑器上制作生成的
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AKEvent` | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取） |
| `AttachedActor` | `Actor` | 依附的 Actor |
| `Volume` | `number` | 范围为-12到12的值 如果不想调整该参数就传一个范围以外的值 |
| `Pitch` | `number` | 范围为-2400到2400的值 如果不想调整该参数就传一个范围以外的值 |
| `StopWhenAttachedToDestroyed` | `boolean` | 依附的 Actor 销毁时是否停止音效播放 |

**Returns**

| Type | Description |
|---|---|
| `number` | 音效 ID |

### `PlaySoundWithRange`

```text
PlaySoundWithRange(AKEvent: UAkAudioEvent, AttachedActor: Actor, StartTime: number, EndTime: number, ID: number)
```

播放指定时间范围的音频
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AKEvent` | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取） |
| `AttachedActor` | `Actor` | 依附的 Actor |
| `StartTime` | `number` | 开始时间 |
| `EndTime` | `number` | 结束时间 |
| `ID` | `number` | 音效 ID |

### `PlaySoundWithLoop`

```text
PlaySoundWithLoop(AKEvent: UAkAudioEvent, AttachedActor: Actor)
```

播放循环音频
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AKEvent` | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取） |
| `AttachedActor` | `Actor` | 依附的 Actor |

### `PlaySoundWith2D`

```text
PlaySoundWith2D(AKEvent: UAkAudioEvent, AttachedActor: Actor)
```

播放2D音频
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AKEvent` | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取） |
| `AttachedActor` | `Actor` | 依附的 Actor |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCStringTextUtility.json -->

# UGCStringTextUtility

文本系统接口库

## Functions

### `ExportText`

```text
ExportText(Object: string) -> string
```

导出对象文本，会根据传入的对象类型打印关键信息

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `string` | 文本对象 |

**Returns**

| Type | Description |
|---|---|
| `string` | 文本字符串 |

### `TrimStartOrEnd`

```text
TrimStartOrEnd(InStr: string, TrimStart: boolean, TrimEnd: boolean) -> string
```

修剪字符串的起始和结尾，根据传入的TrimStart和TrimEnd去除字符串头尾的空白字符

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |
| `TrimStart` | `boolean` | 是否修剪起始 |
| `TrimEnd` | `boolean` | 是否修剪结尾 |

**Returns**

| Type | Description |
|---|---|
| `string` | 修剪后的字符串 |

### `SplitToArray`

```text
SplitToArray(InStr: string, Separator: string) -> table
```

将字符串按照分隔符分割成数组

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |
| `Separator` | `string` | 分隔符 |

**Returns**

| Type | Description |
|---|---|
| `table` | 数组 |

### `StartsWith`

```text
StartsWith(InStr: string, InPrefix: string, SearchCase: ESearchCase) -> boolean
```

判断字符串是否以指定的前缀开头

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |
| `InPrefix` | `string` | 前缀 |
| `SearchCase` | `ESearchCase` | 是否区分大小写 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否以指定的前缀开头 |

### `EndWith`

```text
EndWith(InStr: string, InSuffix: string, SearchCase: ESearchCase) -> boolean
```

判断字符串是否以指定的后缀结尾

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |
| `InSuffix` | `string` | 后缀 |
| `SearchCase` | `ESearchCase` | 是否区分大小写 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否以指定的后缀结尾 |

### `InsertIntoString`

```text
InsertIntoString(SourceStr: string, Content: string, Position: number) -> string
```

在字符串的指定位置插入内容

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceStr` | `string` | 源字符串 |
| `Content` | `string` | 插入内容 |
| `Position` | `number` | 插入位置 |

**Returns**

| Type | Description |
|---|---|
| `string` | 字符串 |

### `JoinArrayIntoString`

```text
JoinArrayIntoString(InStrArray: table, Separator: string) -> string
```

将字符串数组连接成字符串

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStrArray` | `table` | 字符串数组 |
| `Separator` | `string` | 分隔符 |

**Returns**

| Type | Description |
|---|---|
| `string` | 字符串 |

### `SplitToCharArray`

```text
SplitToCharArray(InStr: string) -> table
```

将字符串分割成字符数组

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |

**Returns**

| Type | Description |
|---|---|
| `table` | 字符数组 |

### `ComposedOfDigits`

```text
ComposedOfDigits(InStr: string) -> boolean
```

判断字符串是否由数字组成

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否由数字组成 |

### `LeftChop`

```text
LeftChop(InStr: string, Count: number) -> string
```

截断字符串的前n个字符

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |
| `Count` | `number` | 字符数 |

**Returns**

| Type | Description |
|---|---|
| `string` | 字符串 |

### `LeftPad`

```text
LeftPad(InStr: string, StrLen: number) -> string
```

在字符串的左侧填充空白字符使得字符串长度达到指定的长度

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |
| `StrLen` | `number` | 指定的长度 |

**Returns**

| Type | Description |
|---|---|
| `string` | 字符串 |

### `RightChop`

```text
RightChop(InStr: string, Count: number) -> string
```

截断字符串的后n个字符

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |
| `Count` | `number` | 字符数 |

**Returns**

| Type | Description |
|---|---|
| `string` | 字符串 |

### `RightPad`

```text
RightPad(InStr: string, StrLen: number) -> string
```

在字符串的右侧填充空白字符使得字符串长度达到指定的长度

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStr` | `string` | 字符串 |
| `StrLen` | `number` | 指定的长度 |

**Returns**

| Type | Description |
|---|---|
| `string` | 字符串 |

### `LogTree`

```text
LogTree(Desc: string, Var: any)
```

打印变量,特别是对table类型做树形输出,仅DEV打印

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Desc` | `string` | 变量描述 |
| `Var` | `any` | 要输出的变量,可以是任何类型table, bool, number, nil |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%A4%BE%E4%BA%A4%E7%B3%BB%E7%BB%9F/UGCTeamSystem.json -->

# UGCTeamSystem

队伍系统接口库

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCTeamSystem.NotifyInviteToJoinLobbyTeamDelegate` | `-` | 通知被邀请加入大厅队伍<br>生效范围：客户端<br>@param InviteToJoinLobbyTeamToken table @邀请到大厅队伍的 Token。InviteToJoinLobbyTeamToken.InviterUID int @邀请者 UID |
| `UGCTeamSystem.NotifyRequestToJoinLobbyTeamDelegate` | `-` | 通知请求加入大厅队伍<br>生效范围：客户端<br>@param RequestToJoinLobbyTeamToken table @请求加入大厅队伍的 Token。RequestToJoinLobbyTeamToken.TeamID int @队伍 ID |

## Functions

### `GetTeamComponent`

```text
GetTeamComponent() -> TeamModeComponent
```

【废弃】获取队伍组件
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `TeamModeComponent` | 队伍组件 |

### `ChangePlayerTeamID`

```text
ChangePlayerTeamID(PlayerKey: number, TeamID: number)
```

改变玩家 TeamID
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 PlayerKey |
| `TeamID` | `number` | 队伍 ID |

### `GetUIDsByTeamID`

```text
GetUIDsByTeamID(TeamID: number) -> @UID
```

根据TeamID获取对应队伍里所有的玩家UID
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |

**Returns**

| Type | Description |
|---|---|
| `@UID` | 列表 |

### `GetPlayerKeysByTeamID`

```text
GetPlayerKeysByTeamID(TeamID: number, bReturnAsLuaTable: boolean) -> @PlayerKey
```

根据TeamID获取对应队伍里所有的玩家PlayerKey，PlayerKey需要客户端连上DS后，才会被初始化，若在客户端连上DS前调用该接口，返回的PlayerKey列表不准确
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |
| `bReturnAsLuaTable` | `boolean` | 是否以LuaTable返回 |

**Returns**

| Type | Description |
|---|---|
| `@PlayerKey` | 列表 |

### `GetAIPlayerKeysByTeamID`

```text
GetAIPlayerKeysByTeamID(TeamID: number) -> @PlayerKey
```

根据 TeamID 获取对应队伍里所有的假人玩家 AIPlayerKey，PlayerKey需要客户端连上DS后，才会被初始化，若在客户端连上DS前调用该接口，返回的PlayerKey列表不准确
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |

**Returns**

| Type | Description |
|---|---|
| `@PlayerKey` | 列表 |

### `GetPlayerControllersByTeamID`

```text
GetPlayerControllersByTeamID(TeamID: number) -> @PlayerController
```

根据TeamID获取对应队伍里所有的玩家PlayerController
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |

**Returns**

| Type | Description |
|---|---|
| `@PlayerController` | 列表 |

### `GetPlayerPawnsByTeamID`

```text
GetPlayerPawnsByTeamID(TeamID: number) -> @PlayerPawn
```

根据TeamID获取对应队伍里所有的玩家PlayerPawn
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |

**Returns**

| Type | Description |
|---|---|
| `@PlayerPawn` | 列表 |

### `GetPlayerStatesByTeamID`

```text
GetPlayerStatesByTeamID(TeamID: number) -> @PlayerState
```

根据TeamID获取对应队伍里所有的玩家PlayerState
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |

**Returns**

| Type | Description |
|---|---|
| `@PlayerState` | 列表 |

### `GetLobbyTeamUIDsByUID`

```text
GetLobbyTeamUIDsByUID(UID: number) -> number[]
```

【废弃】请使用 UGCTeamSystem.GetLobbyTeammateUIDsByUID
根据玩家的UID获取其大厅里组队的成员 UID 列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |

**Returns**

| Type | Description |
|---|---|
| `number[]` | 玩家 UID 列表 |

### `GetLobbyTeammateUIDsByUID`

```text
GetLobbyTeammateUIDsByUID(UID: number) -> number[]
```

根据玩家的UID获取其大厅里组队的成员 UID 列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |

**Returns**

| Type | Description |
|---|---|
| `number[]` | 玩家 UID 列表 |

### `GetDynamicLobbyTeammateUIDsByUID`

```text
GetDynamicLobbyTeammateUIDsByUID(UID: number) -> number[]
```

根据玩家的UID获取其大厅里组队的成员 UID 列表。跟 UGCTeamSystem.GetLobbyTeammateUIDsByUID 不同的是，此接口会返回动态组队（UGCTeamSystem.InviteToJoinLobbyTeam、UGCTeamSystem.RequestToJoinLobbyTeam）的成员 UID 列表，而 UGCTeamSystem.GetLobbyTeammateUIDsByUID 以及其他接口只会返回从大厅进入战斗对局那一刻的该玩家在大厅组队的成员 UID 列表。
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |

**Returns**

| Type | Description |
|---|---|
| `number[]` | 玩家 UID 列表 |

### `GetLobbyTeamKeysByPlayerKey`

```text
GetLobbyTeamKeysByPlayerKey(PlayerKey: number) -> @PlayerKey
```

【废弃】请使用 UGCTeamSystem.GetLobbyTeammatePlayerKeysByPlayerKey
根据玩家的 PlayerKey 获取其大厅里组队的成员 PlayerKey 列表，PlayerKey需要客户端连上DS后，才会被初始化，若在客户端连上DS前调用该接口，返回的PlayerKey列表不准确
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 PlayerKey |

**Returns**

| Type | Description |
|---|---|
| `@PlayerKey` | 列表 |

### `GetLobbyTeammatePlayerKeysByPlayerKey`

```text
GetLobbyTeammatePlayerKeysByPlayerKey(PlayerKey: number) -> @PlayerKey
```

根据玩家的 PlayerKey 获取其大厅里组队的成员 PlayerKey 列表，PlayerKey需要客户端连上DS后，才会被初始化，若在客户端连上DS前调用该接口，返回的PlayerKey列表不准确
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 PlayerKey |

**Returns**

| Type | Description |
|---|---|
| `@PlayerKey` | 列表 |

### `InviteToJoinLobbyTeam`

```text
InviteToJoinLobbyTeam(InviteeUID: number)
```

邀请玩家加入（我的）大厅队伍
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InviteeUID` | `number` | 被邀请玩家 UID |

### `RespondToInvitingToJoinLobbyTeam`

```text
RespondToInvitingToJoinLobbyTeam(ResponseOfBeingInvitedToJoinLobby: EResponseOfBeingInvitedToJoinLobby, InviteToJoinLobbyTeamToken: table)
```

响应加入大厅队伍的邀请
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ResponseOfBeingInvitedToJoinLobby` | `EResponseOfBeingInvitedToJoinLobby` | 被邀请加入大厅队伍的响应类型：EResponseOfBeingInvitedToJoinLobby |
| `InviteToJoinLobbyTeamToken` | `table` | 邀请到大厅队伍的 Token |

### `RequestToJoinLobbyTeam`

```text
RequestToJoinLobbyTeam(TeamMemberUID: number)
```

玩家请求加入大厅队伍
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamMemberUID` | `number` | 大厅队伍中的玩家 UID |

### `RespondToRequestingToJoinLobbyTeam`

```text
RespondToRequestingToJoinLobbyTeam(ResponseOfBeingRequestedToJoinLobby: EResponseOfBeingRequestedToJoinLobby, RequestToJoinLobbyTeamToken: table)
```

队长响应被加入大厅队伍的请求
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ResponseOfBeingRequestedToJoinLobby` | `EResponseOfBeingRequestedToJoinLobby` | 被请求加入大厅队伍的响应类型：EResponseOfBeingRequestedToJoinLobby |
| `RequestToJoinLobbyTeamToken` | `table` | 请求加入大厅队伍的 Token |

### `QuitLobbyTeam`

```text
QuitLobbyTeam()
```

玩家主动退出大厅队伍
生效范围：客户端

### `KickFromLobbyTeam`

```text
KickFromLobbyTeam(TargetUID: number)
```

队长将指定玩家踢出大厅队伍
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetUID` | `number` | 被踢玩家的 UID |

### `TransferLobbyTeamLeader`

```text
TransferLobbyTeamLeader(NewLeaderUID: number)
```

队长转让大厅队长身份给指定玩家
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLeaderUID` | `number` | 新队长的 UID |

### `GetTeamIDs`

```text
GetTeamIDs() -> @TeamID
```

获取所有队伍的 ID
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `@TeamID` | 列表 |

### `GetPlayerList`

```text
GetPlayerList(bWithOB?: boolean) -> number[]
```

获取所有玩家信息列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bWithOB?` | `boolean` | 是否包含 OB |

**Returns**

| Type | Description |
|---|---|
| `number[]` | 玩家信息列表 |

### `GetTeamSizeByID`

```text
GetTeamSizeByID(TeamID: number) -> number
```

【废弃】请使用 UGCTeamSystem.GetTeamSizeByTeamID
获取队伍中的玩家数量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 玩家数量 |

### `GetTeamSizeByTeamID`

```text
GetTeamSizeByTeamID(TeamID: number) -> number
```

获取队伍中的玩家数量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 玩家数量 |

### `GetTeamLeaderKeyByTeamID`

```text
GetTeamLeaderKeyByTeamID(TeamID: number) -> number[]
```

通过队伍编号获取队长PlayerKey列表（每个在大厅点击开始游戏的玩家都会被设置为队长，例如四人匹配，队伍里只有一个队长，三人匹配，再随机匹配一个队友，三人里面点击开始游戏的是队长，随机匹配的那个队友也是队长，属于他自己那个小队的队长）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |

**Returns**

| Type | Description |
|---|---|
| `number[]` | 队长PlayerKey |

### `GetIsLeaderOrNotByPlayerKey`

```text
GetIsLeaderOrNotByPlayerKey(PlayerKey: number) -> boolean
```

通过玩家PlayerKey查询身份
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 PlayerKey |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否是队长 |

### `GetAllTeammatePlayerState`

```text
GetAllTeammatePlayerState(bExcludeSelf: boolean) -> ASTExtraPlayerState[]
```

获取所有队友的的PlayerState
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bExcludeSelf` | `boolean` | 是否排除玩家自身 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraPlayerState[]` | - |

### `GetTeammatePlayerStateByPlayerKey`

```text
GetTeammatePlayerStateByPlayerKey(PlayerKey: number) -> ASTExtraPlayerState
```

获取指定PlayerKey队友的的PlayerState
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 PlayerKey |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraPlayerState` | - |

### `IsTeamIDValid`

```text
IsTeamIDValid(TeamID: number) -> ASTExtraPlayerState
```

判断TeamID是否合法
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | TeamID |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraPlayerState` | - |

### `GetTeamIDByPlayerKey`

```text
GetTeamIDByPlayerKey(PlayerKey: number) -> number
```

根据PlayerKey获取队伍ID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 PlayerKey |

**Returns**

| Type | Description |
|---|---|
| `number` | 队伍 ID |

### `GetTeammateIndexByPlayerKey`

```text
GetTeammateIndexByPlayerKey(PlayerState: ASTExtraPlayerState, PlayerKey: number) -> number
```

根据PlayerKey获取队友ID(头顶标号)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerState` | `ASTExtraPlayerState` | 玩家 PlayerState |
| `PlayerKey` | `number` | 玩家 PlayerKey |

**Returns**

| Type | Description |
|---|---|
| `number` | 队友 ID |

### `GetAllTeammateIndex`

```text
GetAllTeammateIndex(PlayerState: ASTExtraPlayerState) -> number>
```

获取所有队友的的队友ID(头顶标号)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerState` | `ASTExtraPlayerState` | 玩家 PlayerState |

**Returns**

| Type | Description |
|---|---|
| `number>` | 以PlayerKey为键，队友ID为值的表 |

### `GetPlayerKeyByTeammateIndex`

```text
GetPlayerKeyByTeammateIndex(PlayerState: ASTExtraPlayerState, TeammateIndex: number) -> number
```

根据队友ID(头顶标号)获取队友PlayerKey
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerState` | `ASTExtraPlayerState` | 玩家 PlayerState |
| `TeammateIndex` | `number` | 队友ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 队友 PlayerKey |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/UGCTimerUtility.json -->

# UGCTimerUtility

计时器工具类

## Functions

### `CreateLuaTimer`

```text
CreateLuaTimer(TimeOffset: number, Callback: function, bLoop: boolean, TimerName: string, InitDelay: number, bLog: boolean, bCoroutine: boolean) -> UGCLuaTimerInstance
```

创建 Lua 计时器
 1. TimeOffset > 0，则 TimeOffset 单位是秒。
 2. TimeOffset == 0，遇到 tick 就会执行。
 3. TimeOffset < 0，是负数如 -N 的话，会在间隔 N 帧后执行第一次。如果传入了 InitDelay，则此条略过，按下面 InitDelay 参数说明来执行：
  a) 如果 InitDelay ~= nil(即传入 InitDelay 参数)，则计时器会在 InitDelay 秒后执行第一次；后面根据 TimeOffset 的设置，循环调用。
  b) 如果 InitDelay == 0，则 InsertTimer 时，会立即执行第一次；后面根据 TimeOffset 的设置，循环调用。
  c) 如果 InitDelay == nil(即未传入 InitDelay 参数)，则会在 TimeOffset 后，执行第一次；后面根据 TimeOffset 的设置，循环调用。
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimeOffset` | `number` | 间隔时间 |
| `Callback` | `function` | 回调函数 |
| `bLoop` | `boolean` | 是否循环 |
| `TimerName` | `string` | 计时器名称 |
| `InitDelay` | `number` | 第一次执行延迟时间 |
| `bLog` | `boolean` | 是否记录日志 |
| `bCoroutine` | `boolean` | 是否是协程 |

**Returns**

| Type | Description |
|---|---|
| `UGCLuaTimerInstance` | 创建的计时器实例 |

### `RemoveLuaTimer`

```text
RemoveLuaTimer(TimerInstance: UGCLuaTimerInstance)
```

移除 Lua 计时器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimerInstance` | `UGCLuaTimerInstance` | 计时器实例 |

### `RemoveLuaTimerByName`

```text
RemoveLuaTimerByName(TimerName: string)
```

根据名称移除 Lua 计时器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimerName` | `string` | 计时器名称 |

### `IsLuaTimerExistByName`

```text
IsLuaTimerExistByName(TimerName: string) -> boolean
```

根据名称判断 Lua 计时器是否存在
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimerName` | `string` | 计时器名称 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否存在 |

### `CreateUETimer`

```text
CreateUETimer(CallbackFunction: LuaFunction, Time: number, IsLooping: boolean) -> ULuaSingleDelegate
```

设置 UE 计时器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CallbackFunction` | `LuaFunction` | Lua 回调函数 |
| `Time` | `number` | 定时时长 |
| `IsLooping` | `boolean` | 是否循环 |

**Returns**

| Type | Description |
|---|---|
| `ULuaSingleDelegate` | 计时器句柄，计时器回调 |

### `RemoveUETimer`

```text
RemoveUETimer(TimerHandle: FTimerHandle)
```

移除 UE 计时器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimerHandle` | `FTimerHandle` | 计时器句柄 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCTweenSystem.json -->

# UGCTweenSystem

Tween 动画系统接口库

## Functions

### `MakeConfig`

```text
MakeConfig(Delay: number, RepeatCount: number, bYoyo: boolean, RepeatDelay: number) -> FUnrealTweenConfig
```

创建一个 Tween 配置表

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delay` | `number` | 初始延迟（秒），默认 0 |
| `RepeatCount` | `number` | 重复次数（-1 无限，0 不重复），默认 1 |
| `bYoyo` | `boolean` | 是否往返，默认 false |
| `RepeatDelay` | `number` | 重复间隔（秒），默认 0 |

**Returns**

| Type | Description |
|---|---|
| `FUnrealTweenConfig` | - |

### `GetTweenSubsystem`

```text
GetTweenSubsystem() -> @Tween
```

获取 TweenSubsystem 实例
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `@Tween` | 子系统实例 |

### `TweenActorLocation`

```text
TweenActorLocation(Actor: AActor, TargetLocation: FVector, Duration: number, Easing: EEasingType, Config: FUnrealTweenConfig) -> FTweenHandle
```

移动 Actor 到目标位置
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 目标 Actor |
| `TargetLocation` | `FVector` | 目标位置 |
| `Duration` | `number` | 动画时长（秒） |
| `Easing` | `EEasingType` | 缓动类型（EEasingType 枚举） |
| `Config` | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Returns**

| Type | Description |
|---|---|
| `FTweenHandle` | 动画句柄，用于后续控制 |

### `TweenActorRotation`

```text
TweenActorRotation(Actor: AActor, TargetRotation: FRotator, Duration: number, Easing: EEasingType, bShortestPath: boolean, Config: FUnrealTweenConfig) -> FTweenHandle
```

旋转 Actor 到目标朝向
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 目标 Actor |
| `TargetRotation` | `FRotator` | 目标旋转 |
| `Duration` | `number` | 动画时长（秒） |
| `Easing` | `EEasingType` | 缓动类型（EEasingType 枚举） |
| `bShortestPath` | `boolean` | 是否走最短路径旋转 |
| `Config` | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Returns**

| Type | Description |
|---|---|
| `FTweenHandle` | 动画句柄，用于后续控制 |

### `TweenFloatValue`

```text
TweenFloatValue(Start: number, End: number, Duration: number, Easing: EEasingType, Callback: function, Config: FUnrealTweenConfig) -> FTweenHandle
```

对 float 数值进行插值，每帧通过回调返回当前值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `number` | 起始值 |
| `End` | `number` | 目标值 |
| `Duration` | `number` | 动画时长（秒） |
| `Easing` | `EEasingType` | 缓动类型（EEasingType 枚举） |
| `Callback` | `function` | 每帧回调，签名 function(Obj, Value)，Obj 为 WorldContext，Value 为当前 float 值 |
| `Config` | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Returns**

| Type | Description |
|---|---|
| `FTweenHandle` | 动画句柄，用于后续控制 |

### `TweenVectorValue`

```text
TweenVectorValue(Start: FVector, End: FVector, Duration: number, Easing: EEasingType, Callback: function, Config: FUnrealTweenConfig) -> FTweenHandle
```

对 FVector 数值进行插值，每帧通过回调返回当前值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `FVector` | 起始向量 |
| `End` | `FVector` | 目标向量 |
| `Duration` | `number` | 动画时长（秒） |
| `Easing` | `EEasingType` | 缓动类型（EEasingType 枚举） |
| `Callback` | `function` | 每帧回调，签名 function(Obj, Value)，Obj 为 WorldContext，Value 为当前 FVector 值 |
| `Config` | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Returns**

| Type | Description |
|---|---|
| `FTweenHandle` | 动画句柄，用于后续控制 |

### `TweenRotatorValue`

```text
TweenRotatorValue(Start: FRotator, End: FRotator, Duration: number, Easing: EEasingType, Callback: function, Config: FUnrealTweenConfig) -> FTweenHandle
```

对 FRotator 数值进行插值，每帧通过回调返回当前值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `FRotator` | 起始旋转 |
| `End` | `FRotator` | 目标旋转 |
| `Duration` | `number` | 动画时长（秒） |
| `Easing` | `EEasingType` | 缓动类型（EEasingType 枚举） |
| `Callback` | `function` | 每帧回调，签名 function(Obj, Value)，Obj 为 WorldContext，Value 为当前 FRotator 值 |
| `Config` | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Returns**

| Type | Description |
|---|---|
| `FTweenHandle` | 动画句柄，用于后续控制 |

### `TweenColorValue`

```text
TweenColorValue(Start: FLinearColor, End: FLinearColor, Duration: number, Easing: EEasingType, Callback: function, Config: FUnrealTweenConfig) -> FTweenHandle
```

对 FLinearColor 数值进行插值，每帧通过回调返回当前值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `FLinearColor` | 起始颜色 |
| `End` | `FLinearColor` | 目标颜色 |
| `Duration` | `number` | 动画时长（秒） |
| `Easing` | `EEasingType` | 缓动类型（EEasingType 枚举） |
| `Callback` | `function` | 每帧回调，签名 function(Obj, Value)，Obj 为 WorldContext，Value 为当前 FLinearColor 值 |
| `Config` | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Returns**

| Type | Description |
|---|---|
| `FTweenHandle` | 动画句柄，用于后续控制 |

### `ConfigureTween`

```text
ConfigureTween(Handle: FTweenHandle, Delay: number, RepeatCount: number, bYoyo: boolean, RepeatDelay: number)
```

配置已创建的 Tween 的高级属性（延迟/循环/Yoyo）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Handle` | `FTweenHandle` | 动画句柄 |
| `Delay` | `number` | 初始延迟（秒） |
| `RepeatCount` | `number` | 重复次数（-1 为无限循环，0 为不重复） |
| `bYoyo` | `boolean` | 是否往返播放（A->B->A） |
| `RepeatDelay` | `number` | 每次重复前的等待时间（秒），默认 0 |

### `ChainTween`

```text
ChainTween(Handle: FTweenHandle, NextHandle: FTweenHandle)
```

链式连接两个 Tween：Parent 完成后自动播放 Child
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Handle` | `FTweenHandle` | 父动画句柄 |
| `NextHandle` | `FTweenHandle` | 子动画句柄（将在父动画完成后自动触发） |

### `PauseTween`

```text
PauseTween(Handle: FTweenHandle)
```

暂停 Tween 动画
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Handle` | `FTweenHandle` | 动画句柄 |

### `ResumeTween`

```text
ResumeTween(Handle: FTweenHandle)
```

恢复已暂停的 Tween 动画
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Handle` | `FTweenHandle` | 动画句柄 |

### `KillTween`

```text
KillTween(Handle: FTweenHandle)
```

停止并销毁 Tween 动画
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Handle` | `FTweenHandle` | 动画句柄 |

### `IsTweenValid`

```text
IsTweenValid(Handle: FTweenHandle) -> boolean
```

判断 Tween 句柄是否有效（动画是否仍在运行）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Handle` | `FTweenHandle` | 动画句柄 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 句柄是否有效 |

### `BindCompletedDelegate`

```text
BindCompletedDelegate(Handle: FTweenHandle, Callback: function)
```

绑定 Tween 完成回调
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Handle` | `FTweenHandle` | 动画句柄 |
| `Callback` | `function` | 完成回调，签名 function(Obj, Handle)，Obj 为 WorldContext，Handle 为动画句柄 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%BD%BD%E5%85%B7/UGCVehicleCommonSystem.json -->

# UGCVehicleCommonSystem

载具系统通用功能接口库

## Functions

### `SetVehicleHPMax`

```text
SetVehicleHPMax(Vehicle: ASTExtraVehicleBase, MaxHP: number)
```

设置载具最大血量
本接口不会自动改变载具血量，游戏逻辑中改变载具血量时（比如收到伤害、载具维修等）会考虑载具最大血量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `MaxHP` | `number` | 最大血量 |

### `SetVehicleHP`

```text
SetVehicleHP(Vehicle: ASTExtraVehicleBase, HP: number)
```

设置载具血量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `HP` | `number` | 血量 |

### `SetVehicleFuelPercent`

```text
SetVehicleFuelPercent(Vehicle: ASTExtraVehicleBase, FuelPercent: number)
```

设置载具油量（按照百分比设置）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `FuelPercent` | `number` | 油量百分比 |

### `GetVehicleHPMax`

```text
GetVehicleHPMax(Vehicle: ASTExtraVehicleBase) -> number
```

获得载具最大血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `number` | 载具最大血量 |

### `GetVehicleHP`

```text
GetVehicleHP(Vehicle: ASTExtraVehicleBase) -> number
```

获得载具当前血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `number` | 载具当前血量 |

### `GetVehicleFuelMax`

```text
GetVehicleFuelMax(Vehicle: ASTExtraVehicleBase) -> number
```

获得载具最大油量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `number` | 载具最大油量 |

### `GetVehicleFuelConsumeFactor`

```text
GetVehicleFuelConsumeFactor(Vehicle: ASTExtraVehicleBase) -> number
```

获得当前油耗系数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `number` | 当前油耗系数 |

### `GetVehicleFuel`

```text
GetVehicleFuel(Vehicle: ASTExtraVehicleBase) -> number
```

获得当前油量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `number` | 当前油量 |

### `IsDontConsumeFuel`

```text
IsDontConsumeFuel(Vehicle: ASTExtraVehicleBase) -> boolean
```

获得当前是否不耗油
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当前是否不耗油 |

### `IsDontDamage`

```text
IsDontDamage(Vehicle: ASTExtraVehicleBase) -> boolean
```

获得当前是否不受到伤害
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当前是否不受到伤害 |

### `GetWheelHP`

```text
GetWheelHP(Vehicle: ASTExtraVehicleBase, WheelIndex: number) -> number
```

获得轮胎血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `WheelIndex` | `number` | 轮胎 ID（从 1 开始） |

**Returns**

| Type | Description |
|---|---|
| `number` | 载具轮子血量 |

### `SetWheelHP`

```text
SetWheelHP(Vehicle: ASTExtraVehicleBase, WheelIndex: number, HP: number) -> boolean
```

设置轮胎血量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `WheelIndex` | `number` | 轮胎 ID（从 1 开始） |
| `HP` | `number` | 载具轮子血量 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 设置是否成功 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%BD%BD%E5%85%B7/UGCVehicleSeatSystem.json -->

# UGCVehicleSeatSystem

载具系统座位系统接口库

## Functions

### `ChangePassengerSeat`

```text
ChangePassengerSeat(Vehicle: ASTExtraVehicleBase, Passenger: ASTExtraBaseCharacter, SeatIndex: number)
```

在目标座位上没有乘客时更换乘客座位
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `Passenger` | `ASTExtraBaseCharacter` | 乘客 |
| `SeatIndex` | `number` | 座位 ID |

### `ForceChangePassengerSeat`

```text
ForceChangePassengerSeat(Vehicle: ASTExtraVehicleBase, Passenger: ASTExtraBaseCharacter, SeatIndex: number)
```

在目标座位上有乘客时更换乘客座位
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `Passenger` | `ASTExtraBaseCharacter` | 乘客 |
| `SeatIndex` | `number` | 座位 ID |

### `GetSeatNum`

```text
GetSeatNum(Vehicle: ASTExtraVehicleBase) -> number
```

获得载具座位个数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `number` | 载具座位个数 |

### `GetAvailableSeatNum`

```text
GetAvailableSeatNum(Vehicle: ASTExtraVehicleBase) -> number
```

获得空闲的载具座位个数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `number` | 空闲的载具座位个数 |

### `GetPassenger`

```text
GetPassenger(Vehicle: ASTExtraVehicleBase, SeatIndex: number) -> ASTExtraBaseCharacter
```

获得对应座位的乘客
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatIndex` | `number` | 座位 ID |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraBaseCharacter` | 对应座位的乘客 |

### `IsSeatIndexAvailable`

```text
IsSeatIndexAvailable(Vehicle: ASTExtraVehicleBase, SeatIndex: number) -> boolean
```

获得对应座位是否空着
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatIndex` | `number` | 座位 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 对应座位是否空着 |

### `GetCharacterSeatIndex`

```text
GetCharacterSeatIndex(Vehicle: ASTExtraVehicleBase, Passenger: ASTExtraBaseCharacter, GetBySocket: boolean) -> number
```

获得指定乘客的座位 ID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `Passenger` | `ASTExtraBaseCharacter` | 乘客 |
| `GetBySocket` | `boolean` | BySocket |

**Returns**

| Type | Description |
|---|---|
| `number` | 指定乘客的座位 ID |

### `GetDriver`

```text
GetDriver(Vehicle: ASTExtraVehicleBase) -> ASTExtraBaseCharacter
```

获得司机
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraBaseCharacter` | 司机 |

### `GetPassengers`

```text
GetPassengers(Vehicle: ASTExtraVehicleBase) -> ASTExtraBaseCharacter[]
```

获得所有乘客
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraBaseCharacter[]` | 所有乘客 |

### `GetAvailableSeatIndexes`

```text
GetAvailableSeatIndexes(Vehicle: ASTExtraVehicleBase) -> int32[]
```

获得所有空闲座位的 Index
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `int32[]` | 所有空闲座位的索引 |

### `CanLeanOut`

```text
CanLeanOut(Vehicle: ASTExtraVehicleBase, SeatIndex: number) -> boolean
```

座位上是否可以探头
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatIndex` | `number` | 座位 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否可以探头 |

### `RemoveVehicleWeapon`

```text
RemoveVehicleWeapon(Vehicle: ASTExtraVehicleBase, SeatIndex: number, WeaponIndex: number)
```

移除指定座位上对应 ID 的车载武器
需要这个座位原来也配置了载具武器，且这个载具武器不在使用中
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatIndex` | `number` | 座位 ID |
| `WeaponIndex` | `number` | 车载武器 ID |

### `AddVehicleWeaponFromSupportKit`

```text
AddVehicleWeaponFromSupportKit(Vehicle: ASTExtraVehicleBase, SeatIndex: number, WeaponIndex: number, WeaponIndexSupport: number)
```

将座位武器库中的武器装备到座位武器孔上
需要这个座位原来也配置了载具武器，且这个载具武器不在使用中
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatIndex` | `number` | 座位 ID |
| `WeaponIndex` | `number` | 车载武器 ID |
| `WeaponIndexSupport` | `number` | 武器库武器 ID |

### `SetPassengerVehicleWeapon`

```text
SetPassengerVehicleWeapon(Vehicle: ASTExtraVehicleBase, SeatIndex: number, bControlVehicleWeapon: boolean)
```

设置当前座位上的车载武器是否能使用
需要这个座位原来也配置了载具武器，且乘客正在该座位上
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatIndex` | `number` | 座位 ID |
| `bControlVehicleWeapon` | `boolean` | 是否能控制车载武器 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%BD%BD%E5%85%B7/UGCVehicleSystem.json -->

# UGCVehicleSystem

载具系统接口库

## Functions

### `SpawnVehicle`

```text
SpawnVehicle(VehicleID: number, Location: Vector, Rotation: Rotator, IsForce: boolean) -> ASTExtraVehicleBase
```

【废弃】请使用 UGCVehicleSystem.SpawnVehicleNew
生成载具
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `VehicleID` | `number` | 载具表ID |
| `Location` | `Vector` | 生成位置 |
| `Rotation` | `Rotator` | 旋转 |
| `IsForce` | `boolean` | 是否无视碰撞强行生成 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraVehicleBase` | 载具 |

### `EnterVehicle`

```text
EnterVehicle(Pawn: ASTExtraBaseCharacter, Vehicle: ASTExtraVehicleBase, SeatType: ESTExtraVehicleSeatType, IsForce: boolean)
```

进入载具
仅限普通玩家控制的角色（Character）可以用
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Pawn` | `ASTExtraBaseCharacter` | 普通玩家 |
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatType` | `ESTExtraVehicleSeatType` | 座位类型 |
| `IsForce` | `boolean` | 是否无视距离和阻挡 |

### `ExitVehicle`

```text
ExitVehicle(Pawn: ASTExtraBaseCharacter)
```

离开载具
仅限普通玩家控制的角色可以用
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Pawn` | `ASTExtraBaseCharacter` | 普通玩家 |

### `GetVehicleSeatCount`

```text
GetVehicleSeatCount(Vehicle: ASTExtraVehicleBase) -> number
```

获取载具的座位数量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `number` | 载具的座位数量 |

### `GetVehicleSeatOccupiers`

```text
GetVehicleSeatOccupiers(Vehicle: ASTExtraVehicleBase) -> ASTExtraBaseCharacter[]
```

获取载具座位上的乘客列表（包括司机）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 对应的载具 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraBaseCharacter[]` | 载具上的乘客们（包括司机） |

### `GetVehicleSeatType`

```text
GetVehicleSeatType(Vehicle: ASTExtraVehicleBase, SeatIndex: number) -> ESTExtraVehicleSeatType
```

获取载具对应 SeatIndex 编号的座位类型
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatIndex` | `number` | 座位编号(从1开始) |

**Returns**

| Type | Description |
|---|---|
| `ESTExtraVehicleSeatType` | 载具座位类型 |

### `GetOccupierBySeatIndex`

```text
GetOccupierBySeatIndex(Vehicle: ASTExtraVehicleBase, SeatIndex: number) -> ASTExtraBaseCharacter
```

获取 SeatIndex 编号获取对应座位上的乘客 Pawn
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatIndex` | `number` | 座位编号（从 1 开始） |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraBaseCharacter` | 对应乘客，如果没有则返回 nil |

### `SpawnVehicleNew`

```text
SpawnVehicleNew(VehicleBlueprintPath: string, Location: Vector, Rotation: Rotator, SnapFloor: boolean, IsForce: boolean) -> ASTExtraVehicleBase
```

使用蓝图路径生成载具
不要在 Spawn 之后立马修改载具位置，等载具落地停稳后再修改，不然位置修改会失败（如果有类似需求，建议直接创建在对应点）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `VehicleBlueprintPath` | `string` | 载具蓝图路径，格式类似 /Game/Arts_PlayerBluePrints/Vehicle/VH_Buggy/BP_VH_Buggy.BP_VH_Buggy_C |
| `Location` | `Vector` | 生成位置 |
| `Rotation` | `Rotator` | 旋转 |
| `SnapFloor` | `boolean` | 是否贴地 |
| `IsForce` | `boolean` | 是否无视碰撞强行生成 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraVehicleBase` | 载具 |

### `CharacterEnterVehicle`

```text
CharacterEnterVehicle(Character: ASTExtraBaseCharacter, Vehicle: ASTExtraVehicleBase, SeatType: ESTExtraVehicleSeatType, IsForce: boolean) -> boolean
```

乘客进入载具
仅限普通玩家控制的角色可以用
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `ASTExtraBaseCharacter` | 乘客 |
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatType` | `ESTExtraVehicleSeatType` | 座位类型 |
| `IsForce` | `boolean` | 是否无视距离和阻挡 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否成功 |

### `CharacterLeaveVehicle`

```text
CharacterLeaveVehicle(Character: ASTExtraBaseCharacter)
```

乘客离开当前所在载具
仅限普通玩家控制的角色可以用
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `ASTExtraBaseCharacter` | 乘客 |

### `TeleportVehicleTo`

```text
TeleportVehicleTo(Vehicle: ASTExtraVehicleBase, Location: Vector, Rotator: Rotator)
```

传送载具
不要在 Spawn 之后立马传送载具，等载具落地停稳后再传送，不然传送会失败（如果有类似需求，建议直接创建在对应点）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `Location` | `Vector` | 位置 |
| `Rotator` | `Rotator` | 旋转 |

### `GetForwardSpeed`

```text
GetForwardSpeed(Vehicle: ASTExtraVehicleBase) -> number
```

获得载具当前速度(单位是cm/s)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `number` | 载具当前速度 |

### `IsStoped`

```text
IsStoped(Vehicle: ASTExtraVehicleBase) -> boolean
```

载具是否静止
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 载具是否静止 |

### `IsEngineStarted`

```text
IsEngineStarted(Vehicle: ASTExtraVehicleBase) -> boolean
```

载具引擎是否启动
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 载具引擎是否启动 |

### `GetVehicleHealthState`

```text
GetVehicleHealthState(Vehicle: ASTExtraVehicleBase) -> ESTExtraVehicleHealthState
```

获得当前载具健康状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `ESTExtraVehicleHealthState` | 载具当前健康状态 |

### `DestroySelf`

```text
DestroySelf(Vehicle: ASTExtraVehicleBase)
```

摧毁载具
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

### `Respawn`

```text
Respawn(Vehicle: ASTExtraVehicleBase)
```

重生载具
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

### `GetSeatState`

```text
GetSeatState(Vehicle: ASTExtraVehicleBase, SeatIndex: number) -> boolean
```

指定座位上是否有人
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatIndex` | `number` | 座位 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 指定座位上是否有人 |

### `GetSeatNum`

```text
GetSeatNum(Vehicle: ASTExtraVehicleBase) -> number
```

获得载具座位个数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `number` | 载具座位个数 |

### `GetWheelNum`

```text
GetWheelNum(Vehicle: ASTExtraVehicleBase) -> number
```

获得轮胎数量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `number` | 载具轮子数量 |

### `IsWheelDamageable`

```text
IsWheelDamageable(Vehicle: ASTExtraVehicleBase, WheelIndex: number) -> boolean
```

获得轮胎是否可以被摧毁
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `WheelIndex` | `number` | 轮胎 ID（从 1 开始） |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 轮胎是否可以被摧毁 |

### `SetWheelDamageable`

```text
SetWheelDamageable(Vehicle: ASTExtraVehicleBase, WheelIndex: number, Damageable: boolean)
```

设置轮胎是否可以被摧毁
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `WheelIndex` | `number` | 轮胎ID（从1开始） |
| `Damageable` | `boolean` | 是否可以被摧毁 |

### `StopFireVehicleWeapon`

```text
StopFireVehicleWeapon(Vehicle: ASTExtraVehicleBase, VehicleWeapon: AVehicleShootWeapon)
```

车载武器停止攻击
仅限驾驶位车载武器生效
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `VehicleWeapon` | `AVehicleShootWeapon` | 车载武器 |

### `StartFireVehicleWeapon`

```text
StartFireVehicleWeapon(Vehicle: ASTExtraVehicleBase, VehicleWeapon: AVehicleShootWeapon, Character: ASTExtraBaseCharacter)
```

车载武器开始攻击
仅限驾驶位车载武器生效
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `VehicleWeapon` | `AVehicleShootWeapon` | 车载武器 |
| `Character` | `ASTExtraBaseCharacter` | 攻击者(传入 nil 视为 Driver) |

### `GetVehicleWeapon`

```text
GetVehicleWeapon(Vehicle: ASTExtraVehicleBase, SeatIndex: number, WeaponID: number) -> AVehicleShootWeapon
```

获得指定座位上指定 ID 的武器实例
武器 ID 指载具蓝图中，座位上配置的武器序号
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatIndex` | `number` | 座位ID（从 1 开始） |
| `WeaponID` | `number` | 武器ID（从 1 开始） |

**Returns**

| Type | Description |
|---|---|
| `AVehicleShootWeapon` | 武器实例 |

### `GetAllVehicleWeaponList`

```text
GetAllVehicleWeaponList(Vehicle: ASTExtraVehicleBase) -> AVehicleShootWeapon[]
```

获得所有车载武器的列表
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `AVehicleShootWeapon[]` | 武器列表 |

### `StopMusic`

```text
StopMusic(Vehicle: ASTExtraVehicleBase)
```

暂停播放车载音乐
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

### `GetVehicleType`

```text
GetVehicleType(Vehicle: ASTExtraVehicleBase) -> ESTExtraVehicleType
```

获得载具类型
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `ESTExtraVehicleType` | 载具类型 |

### `StartBrake`

```text
StartBrake(Vehicle: ASTExtraVehicleBase)
```

载具拉起手刹
仅在主控端（驾驶员端）调用有效
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

### `StopBrake`

```text
StopBrake(Vehicle: ASTExtraVehicleBase)
```

载具放下手刹
仅在主控端（驾驶员端）调用有效
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

### `CanDriverBoosting`

```text
CanDriverBoosting(Vehicle: ASTExtraVehicleBase) -> boolean
```

获得载具是否能够加速
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 载具是否能够加速 |

### `StartBoosting`

```text
StartBoosting(Vehicle: ASTExtraVehicleBase)
```

载具加速
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

### `StopBoosting`

```text
StopBoosting(Vehicle: ASTExtraVehicleBase)
```

载具取消加速
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

### `CanDriverUsingHorn`

```text
CanDriverUsingHorn(Vehicle: ASTExtraVehicleBase) -> boolean
```

是否能按喇叭
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否能按喇叭 |

### `StartHorn`

```text
StartHorn(Vehicle: ASTExtraVehicleBase)
```

载具长按喇叭（按下）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

### `StopHorn`

```text
StopHorn(Vehicle: ASTExtraVehicleBase)
```

载具长按喇叭（抬起）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

### `MoveForward`

```text
MoveForward(Vehicle: ASTExtraVehicleBase, Throttle: number)
```

载具前进/后退
需要在驾驶员所在客户端每帧调用
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `Throttle` | `number` | 取值范围[-1,1]，负值代表后退，正值代表前进 |

### `CanDrive`

```text
CanDrive(Vehicle: ASTExtraVehicleBase) -> boolean
```

驾驶员是否可以操控载具
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否可以操控载具 |

### `PlayMusic`

```text
PlayMusic(Vehicle: ASTExtraVehicleBase, MusicIndex: number)
```

播放车载音乐
注意，武装载具不支持车载音乐功能
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `MusicIndex` | `number` | 曲目ID（取值范围[1,8]） |

### `GetVehicleBaseType`

```text
GetVehicleBaseType(Vehicle: ASTExtraVehicleBase) -> ESTExtraVehicleBaseType
```

获取载具的基础类型
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `ESTExtraVehicleBaseType` | 载具基础类型 |

### `ModifyWheeledVehicleDragCoefficientScale`

```text
ModifyWheeledVehicleDragCoefficientScale(Vehicle: ASTExtraVehicleBase, Scale: number)
```

修改空气阻力的倍率
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `Scale` | `number` | 空气阻力的修改倍率 |

### `ModifyWheeledVehicleMaxRPMScale`

```text
ModifyWheeledVehicleMaxRPMScale(Vehicle: ASTExtraVehicleBase, Scale: number)
```

修改引擎最大转速的倍率
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `Scale` | `number` | 引擎最大转速的修改倍率 |

### `ModifyWheeledVehicleTorqueScale`

```text
ModifyWheeledVehicleTorqueScale(Vehicle: ASTExtraVehicleBase, Scale: number)
```

修改引擎扭矩的倍率
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `Scale` | `number` | 引擎扭矩的修改倍率 |

### `BrakeInCustomizeScale`

```text
BrakeInCustomizeScale(Vehicle: ASTExtraVehicleBase, Scale: number)
```

用自定义倍率刹车
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `Scale` | `number` | 自定义刹车倍率 |

### `GetVehicleByPlayerController`

```text
GetVehicleByPlayerController(PlayerController: APlayerController) -> ASTExtraVehicleBase
```

通过 PlayerController 获取 Vehicle
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `APlayerController` | 对应的玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraVehicleBase` | 对应的载具 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCVehicleSystemV2.json -->

# UGCVehicleSystemV2

载具系统接口库V2

## Functions

### `SpawnVehicle`

```text
SpawnVehicle(VehiclePath: string, Location: Vector, Rotation: Rotator, SnapFloor: bool, IsForce: bool) -> ASTExtraVehicleBase
```

使用蓝图路径生成载具
不要在 Spawn 之后立马修改载具位置，等载具落地停稳后再修改，不然位置修改会失败（如果有类似需求，建议直接创建在对应点）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `VehiclePath` | `string` | 载具蓝图路径，格式示例："/Game/Arts_PlayerBluePrints/Vehicle/VH_Buggy/BP_VH_Buggy.BP_VH_Buggy_C" |
| `Location` | `Vector` | 生成位置 |
| `Rotation` | `Rotator` | 旋转。可缺省，默认无旋转 |
| `SnapFloor` | `bool` | 是否贴地。可缺省，默认 true |
| `IsForce` | `bool` | 是否无视碰撞强行生成。 可缺省，默认 false |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraVehicleBase` | 载具 |

### `DestroyVehicle`

```text
DestroyVehicle(Vehicle: ASTExtraVehicleBase)
```

摧毁载具
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

### `Respawn`

```text
Respawn(Vehicle: ASTExtraVehicleBase) -> ASTExtraVehicleBase
```

重生载具
重生将创建新载具，旧的载具将被销毁不再可用
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraVehicleBase` | 重生后的新载具。若为nil，表示操作失败，新的载具不会创建、旧的载具也不会销毁。 |

### `EnterVehicle`

```text
EnterVehicle(Player: PlayerPawn | PlayerController @玩家角色或玩家PlayerController, Vehicle: ASTExtraVehicleBase, SeatIndex: int, IsForce: bool) -> bool
```

玩家角色进入载具
生效范围：服务器&客户端(客户端仅能操作自己的玩家角色)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或玩家PlayerController` | 玩家角色或玩家PlayerController |
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatIndex` | `int` | 座位索引(0为驾驶位，-1表示尝试进入任意空位置)。可缺省，默认-1。 |
| `IsForce` | `bool` | 是否无视距离和阻挡(仅服务器调用支持此项)。可缺省，默认 false |

**Returns**

| Type | Description |
|---|---|
| `bool` | 服务器:是否成功进入 \| 客户端:返回值无意义 |

### `LeaveVehicle`

```text
LeaveVehicle(Player: PlayerPawn | PlayerController @玩家角色或玩家PlayerController, IsForce: bool) -> bool
```

玩家角色离开载具
生效范围：服务器&客户端(客户端仅能操作自己的玩家角色)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或玩家PlayerController` | 玩家角色或玩家PlayerController |
| `IsForce` | `bool` | 是否需要强制离开载具(仅服务器调用支持此项)。可缺省，默认 false |

**Returns**

| Type | Description |
|---|---|
| `bool` | 服务器:是否成功离开 \| 客户端:返回值无意义 |

### `GetVehicleType`

```text
GetVehicleType(Vehicle: ASTExtraVehicleBase) -> ESTExtraVehicleBaseType
```

获取载具类型
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `ESTExtraVehicleBaseType` | 载具基础类型 |

### `CanDrive`

```text
CanDrive(Vehicle: ASTExtraVehicleBase) -> bool
```

驾驶员是否可以操控载具
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否可以操控载具 |

### `MoveForward`

```text
MoveForward(Vehicle: ASTExtraVehicleBase, Throttle: float)
```

操作载具前进/后退
需要在驾驶员所在客户端每帧调用
当地面载具处于前进状态时，输入后退操作，将执行刹车逻辑，受刹车力量系数(BrakeTorqueCoefficient)影响。
当地面载具处于后退状态时，输入前进操作，也将执行刹车逻辑。
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `Throttle` | `float` | 取值范围[-1,1]，负值代表后退，正值代表前进 |

### `MoveTurn`

```text
MoveTurn(Vehicle: ASTExtraVehicleBase, Throttle: float)
```

操作载具打右方向/左方向
需要在驾驶员所在客户端每帧调用
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `Throttle` | `float` | 取值范围[-1,1]，负值代表左方向，正值代表右方向 |

### `CanHandBrake`

```text
CanHandBrake(Vehicle: ASTExtraVehicleBase) -> bool
```

获得载具是否支持(急刹)手刹
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 载具是否能够手刹 |

### `SetHandBrake`

```text
SetHandBrake(Vehicle: ASTExtraVehicleBase, BrakeScale: float)
```

操作载具(急刹)手刹
需要在驾驶员所在客户端调用
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `BrakeScale` | `float` | 刹车倍率，取值范围[0,1]，0为无刹车，1为最强刹车 |

### `CanBoosting`

```text
CanBoosting(Vehicle: ASTExtraVehicleBase) -> bool
```

获得载具能否加速
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 载具是否能够加速 |

### `SetBoosting`

```text
SetBoosting(Vehicle: ASTExtraVehicleBase, Open: bool)
```

开关载具加速
需要在驾驶员所在客户端调用
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `Open` | `bool` | true开启加速，false关闭加速 |

### `CanHorn`

```text
CanHorn(Vehicle: ASTExtraVehicleBase) -> bool
```

获得载具能否按喇叭
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 载具是否能够按喇叭 |

### `SetHorn`

```text
SetHorn(Vehicle: ASTExtraVehicleBase, Open: bool)
```

按下/抬起载具喇叭
需要在驾驶员所在客户端调用
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `Open` | `bool` | true按下喇叭，false抬起喇叭 |

### `GetVelocity`

```text
GetVelocity(Vehicle: ASTExtraVehicleBase) -> FVector
```

获得载具当前速度(单位是cm/s)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 载具当前速度 |

### `GetVehicleHealthState`

```text
GetVehicleHealthState(Vehicle: ASTExtraVehicleBase) -> ESTExtraVehicleHealthState
```

获得当前载具健康状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `ESTExtraVehicleHealthState` | 载具当前健康状态 |

### `CanDamage`

```text
CanDamage(Vehicle: ASTExtraVehicleBase) -> bool
```

获得载具是否能受到伤害
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 载具是否能受到伤害 |

### `SetCanDamage`

```text
SetCanDamage(Vehicle: ASTExtraVehicleBase, CanDamage: bool)
```

设置载具是否能受到伤害
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `CanDamage` | `bool` | 能否受到伤害 |

### `GetSeatNum`

```text
GetSeatNum(Vehicle: ASTExtraVehicleBase) -> int
```

获取座位数量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `int` | 座位数量 |

### `GetSeatDataByIndex`

```text
GetSeatDataByIndex(Vehicle: ASTExtraVehicleBase, SeatIndex: int) -> UGCVehicleSeatData
```

获取座位数据
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatIndex` | `int` | 座位索引 |

**Returns**

| Type | Description |
|---|---|
| `UGCVehicleSeatData` | 座位数据 |

### `GetAllSeatDatas`

```text
GetAllSeatDatas(Vehicle: ASTExtraVehicleBase) -> UGCVehicleSeatData[]
```

获取所有座位数据
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `UGCVehicleSeatData[]` | 座位数据列表 |

### `ChangePassengerSeat`

```text
ChangePassengerSeat(Player: PlayerPawn | PlayerController @玩家角色或玩家PlayerController, SeatIndex: number) -> bool
```

改变玩家乘客的座位
生效范围：服务器&客户端 (客户端执行只能指定空位，否则会失败。服务端执行可以指定有乘客的座位，两人互相交换位置。)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或玩家PlayerController` | 玩家角色或玩家PlayerController |
| `SeatIndex` | `number` | 目标座位 ID |

**Returns**

| Type | Description |
|---|---|
| `bool` | 服务器:是否成功改变 \| 客户端:返回值无意义 |

### `StartFireVehicleWeapon`

```text
StartFireVehicleWeapon(Vehicle: ASTExtraVehicleBase)
```

车载武器开始攻击
仅限驾驶位车载武器生效
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%A4%BE%E4%BA%A4%E7%B3%BB%E7%BB%9F/UGCVoiceManagerSystem.json -->

# UGCVoiceManagerSystem

语音系统接口库

## Functions

### `GetGVoiceInterface`

```text
GetGVoiceInterface() -> UGVoiceInterface
```

获取 Voice 组件
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `UGVoiceInterface` | 对应语音管理类的指针 |

### `GetPlayerMemberID`

```text
GetPlayerMemberID(PlayerKey: number) -> number
```

获取玩家的语音房间 MemberID
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 角色的 PlayerKey |

**Returns**

| Type | Description |
|---|---|
| `number` | 角色语音房间的 MemberID |

### `JoinVoiceRoom`

```text
JoinVoiceRoom(RoomKey: string)
```

加入语音房间
RoomKey 为语音房间唯一标识，可由自己进行拼接
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RoomKey` | `string` | 语音房间 Key |

### `QuitVoiceRoom`

```text
QuitVoiceRoom()
```

退出 UGC 语音房间
生效范围：客户端

### `GetVoiceRoomKey`

```text
GetVoiceRoomKey() -> string
```

获取当前房间 RoomKey
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `string` | 语音房间 Key |

### `SetGlobalVoiceRadius`

```text
SetGlobalVoiceRadius(Radius: number)
```

设置全局语音生效范围
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Radius` | `number` | 全局语音半径（单位：cm） |

### `SetVoiceRoomSoundEnable`

```text
SetVoiceRoomSoundEnable(IsEnable: boolean)
```

开启/关闭语音房间喇叭
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsEnable` | `boolean` | 开启或者关闭喇叭 |

### `SetVoiceRoomMicrophoneEnable`

```text
SetVoiceRoomMicrophoneEnable(IsEnable: boolean)
```

开启/关闭语音房间麦克风
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsEnable` | `boolean` | 开启或者关闭麦克风 |

### `SetGlobalVoiceSoundEnable`

```text
SetGlobalVoiceSoundEnable(IsEnable: boolean)
```

开启/关闭全局语音喇叭
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsEnable` | `boolean` | 开启或者关闭喇叭 |

### `SeGlobalVoiceMicrophoneEnable`

```text
SeGlobalVoiceMicrophoneEnable(IsEnable: boolean)
```

开启/关闭 全局语音麦克风
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsEnable` | `boolean` | 开启或者关闭麦克风 |

### `SetVoiceRoomPlayerMuteState`

```text
SetVoiceRoomPlayerMuteState(MemberID: number, IsMute: boolean)
```

设置语音房间指定玩家语音屏蔽（静音）状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MemberID` | `number` | 当前房间要被屏蔽的玩家的 UID |
| `IsMute` | `boolean` | 是否屏蔽 |

### `SetGlobalVoicePlayerMuteState`

```text
SetGlobalVoicePlayerMuteState(MemberID: number, IsMute: boolean)
```

设置全局房间指定玩家语音屏蔽（静音）状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MemberID` | `number` | 当前房间要被屏蔽的玩家的 MemberID |
| `IsMute` | `boolean` | 是否屏蔽 |

### `IsVoiceRoomSoundEnable`

```text
IsVoiceRoomSoundEnable() -> boolean
```

获得语音房间声音（喇叭）开关状态
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当前房间喇叭状态 |

### `IsVoiceRoomMicrophoneEnable`

```text
IsVoiceRoomMicrophoneEnable() -> boolean
```

获得语音房间麦克风开关状态
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当前房间麦克风状态 |

### `IsGlobalVoiceSoundEnable`

```text
IsGlobalVoiceSoundEnable() -> boolean
```

获得全局语音声音（喇叭）开关状态
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当前房间喇叭状态 |

### `IsGlobalVoiceMicrophoneEnable`

```text
IsGlobalVoiceMicrophoneEnable() -> boolean
```

获得全局语音麦克风开关状态
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当前房间麦克风状态 |

### `JoinGlobalVoiceRoom`

```text
JoinGlobalVoiceRoom(GlobalVoiceRoomId: number)
```

加入全局语音房间（依赖于全局语音房间的某个范围可听可说,区域语音，包厢等等）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GlobalVoiceRoomId` | `number` | 区域小房间的 index |

### `QuitGlobalVoiceRoom`

```text
QuitGlobalVoiceRoom()
```

退出全局语音房间（区域语音，包厢等等）
生效范围：客户端

### `CloseCivilVoiceDetect`

```text
CloseCivilVoiceDetect()
```

关闭文明语音检测和 lbs 小号限制
生效范围：客户端

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81%E4%B8%8E%E8%83%8C%E5%8C%85/UGCWeaponManagerSystem.json -->

# UGCWeaponManagerSystem

武器管理系统接口库

## Functions

### `GetWeaponManagerComponent`

```text
GetWeaponManagerComponent(PlayerPawn: PlayerPawn) -> UWeaponManagerComponent
```

获取武器管理组件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `UWeaponManagerComponent` | 武器管理组件 |

### `GetWeaponBySlot`

```text
GetWeaponBySlot(PlayerPawn: PlayerPawn, Slot: ESurviveWeaponPropSlot) -> ASTExtraWeapon
```

获取对应插槽的武器实例
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `Slot` | `ESurviveWeaponPropSlot` | 武器槽位 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraWeapon` | 武器 |

### `GetCurrentWeapon`

```text
GetCurrentWeapon(PlayerPawn: PlayerPawn) -> ASTExtraWeapon
```

获取当前使用的武器实例
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraWeapon` | 武器 |

### `GetLastUsedWeapon`

```text
GetLastUsedWeapon(PlayerPawn: PlayerPawn) -> ASTExtraWeapon
```

获取上一把武器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraWeapon` | 武器 |

### `GetCurrentWeaponSlot`

```text
GetCurrentWeaponSlot(PlayerPawn: PlayerPawn) -> ESurviveWeaponPropSlot
```

获取当前使用武器插槽
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `ESurviveWeaponPropSlot` | 武器槽位 |

### `SwitchWeaponBySlot`

```text
SwitchWeaponBySlot(PlayerPawn: PlayerPawn, Slot: ESurviveWeaponPropSlot, IsUseAnimation: boolean)
```

切换对应槽位的武器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `Slot` | `ESurviveWeaponPropSlot` | 武器槽位 |
| `IsUseAnimation` | `boolean` | 是否播放使用动画 |

### `CurrentWeaponAttachToBack`

```text
CurrentWeaponAttachToBack(PlayerPawn: PlayerPawn)
```

收起武器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

### `GetWeaponItemID`

```text
GetWeaponItemID(Weapon: ASTExtraWeapon) -> number
```

获取武器ItemID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Weapon` | `ASTExtraWeapon` | 武器 |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品ID,对应物品表中ID |

### `GetWeaponName`

```text
GetWeaponName(Weapon: ASTExtraWeapon) -> string
```

获取武器名
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Weapon` | `ASTExtraWeapon` | 武器 |

**Returns**

| Type | Description |
|---|---|
| `string` | 武器名称 |

### `GetCurrentUsingAmmoID`

```text
GetCurrentUsingAmmoID(PlayerPawn: PlayerPawn) -> number
```

获取当前消耗弹药
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 弹药ID |

### `SetWeaponSlotVisible`

```text
SetWeaponSlotVisible(PlayerPawn: PlayerPawn, WeaponSlot: ESurviveWeaponPropSlot, bVisible: boolean)
```

设置武器的可见性
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `WeaponSlot` | `ESurviveWeaponPropSlot` | 武器槽位 |
| `bVisible` | `boolean` | 是否可见 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9C%BA%E6%99%AF%E4%B8%8E%E7%8E%AF%E5%A2%83/UGCWeatherSystem.json -->

# UGCWeatherSystem

天气系统接口库

## Functions

### `LoadWeatherSequence`

```text
LoadWeatherSequence(PlayerController: PlayerController, WeatherSequence: WeatherSequence, BlendTime: number)
```

加载天气序列
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |
| `WeatherSequence` | `WeatherSequence` | 天气序列资源 |
| `BlendTime` | `number` | 过渡时间 |

### `UnloadWeatherSequence`

```text
UnloadWeatherSequence(PlayerController: PlayerController, WeatherSequence: WeatherSequence)
```

卸载天气序列
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |
| `WeatherSequence` | `WeatherSequence` | 天气序列资源 |

### `SeekWeatherSequence`

```text
SeekWeatherSequence(PlayerController: PlayerController, WeatherSequence: WeatherSequence, Time: number)
```

设置天气序列播放进度
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |
| `WeatherSequence` | `WeatherSequence` | 天气序列资源 |
| `Time` | `number` | 目标时间 |

### `PauseWeatherSequence`

```text
PauseWeatherSequence(PlayerController: PlayerController, WeatherSequence: WeatherSequence)
```

暂停天气序列
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |
| `WeatherSequence` | `WeatherSequence` | 天气序列资源 |

### `ResumeWeatherSequence`

```text
ResumeWeatherSequence(PlayerController: PlayerController, WeatherSequence: WeatherSequence)
```

继续天气序列
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |
| `WeatherSequence` | `WeatherSequence` | 天气序列资源 |

### `GetCurrentWeatherSequence`

```text
GetCurrentWeatherSequence(PlayerController: PlayerController) -> WeatherSequence
```

获取当前天气序列
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `WeatherSequence` | 天气序列资源 |

### `GetCurrentWeatherPlayPercentage`

```text
GetCurrentWeatherPlayPercentage(PlayerController: PlayerController) -> number
```

获取当前天气播放进度
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | 播放进度（0~1） |

### `GetCurrentWeatherTime`

```text
GetCurrentWeatherTime(PlayerController: PlayerController) -> number
```

获取当前天气时间
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | 天气时间（0~24） |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/UI%20%E7%95%8C%E9%9D%A2/UGCWidgetManagerSystem.json -->

# UGCWidgetManagerSystem

UI控件管理器系统接口库

## Functions

### `CreateWidgetAsync`

```text
CreateWidgetAsync(WidgetClassPath: string|FSoftObjectPath, OnCreatedCallback: fun(Widget:UUserWidget))
```

异步创建一个控件，返回控件实例

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetClassPath` | `string\|FSoftObjectPath` | 控件类路径 |
| `OnCreatedCallback` | `fun(Widget:UUserWidget)` | 创建完成回调 |

### `CreateWidget`

```text
CreateWidget(WidgetClass: UClass) -> UUserWidget
```

创建一个控件，返回控件实例

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetClass` | `UClass` | 控件蓝图类 |

**Returns**

| Type | Description |
|---|---|
| `UUserWidget` | 控件实例 |

### `DestroyWidget`

```text
DestroyWidget(Widget: UUserWidget)
```

销毁一个控件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

### `AddToSlot`

```text
AddToSlot(Widget: UUserWidget, SlotName: string, ZOrder: number, AnchorData: FAnchorData)
```

添加一个控件到指定 UI 挂点槽位

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |
| `SlotName` | `string` | 控件槽位名称，默认为 UI.UISlot.MainUISlot_Low |
| `ZOrder` | `number` | 控件层级，默认为 0 |
| `AnchorData` | `FAnchorData` | 控件锚点，默认为 { Anchors = { Minimum = Vector2D.New(0, 0), Maximum = Vector2D.New(1, 1) } } |

### `RemoveFromSlot`

```text
RemoveFromSlot(Widget: UUserWidget)
```

从 UI 挂点槽位移除控件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

### `SetWidgetLayout`

```text
SetWidgetLayout(LayoutPath: string)
```

异步加载并设置当前的 WidgetLayout，同时只能设置一个，旧的 WidgetLayout 会被卸载。传入 “Default” 可卸载 WidgetLayout 回到默认状态。（主要用于可视化屏蔽玩法中不需要的和平 UI，UI 会强制隐藏）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LayoutPath` | `string` | WidgetLayout 引用路径 |

### `ShowWidget`

```text
ShowWidget(Widget: UUserWidget)
```

显示一个控件，需要控件已经挂载到挂点槽上

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

### `HideWidget`

```text
HideWidget(Widget: UUserWidget)
```

隐藏一个控件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

### `IsWidgetAddedToSlot`

```text
IsWidgetAddedToSlot(Widget: UUserWidget) -> boolean
```

判断一个控件是否已经挂载在 UI 挂点上

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否已经挂载 |

### `IsWidgetVisible`

```text
IsWidgetVisible(Widget: UUserWidget) -> boolean
```

判断一个控件是否可见

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否可见 |

### `GetSubWidget`

```text
GetSubWidget(Widget: UUserWidget, SubWidgetName: string) -> UWidget
```

获取子控件，可用于获取 UMG 蓝图里的子控件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |
| `SubWidgetName` | `string` | 子控件名称 |

**Returns**

| Type | Description |
|---|---|
| `UWidget` | 子控件实例 |

### `GetAllWidgetsOfClass`

```text
GetAllWidgetsOfClass(WidgetClass: UClass, bAddedToSlotOnly: boolean) -> UUserWidget[]
```

获取指定类别的所有控件，可筛选只获取已被添加到挂点的控件
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetClass` | `UClass` | 控件类（UUserWidget） |
| `bAddedToSlotOnly` | `boolean` | 是否只获取已添加到挂点的控件 |

**Returns**

| Type | Description |
|---|---|
| `UUserWidget[]` | 控件实例列表 |

### `GetMainUI`

```text
GetMainUI() -> UserWidget
```

获取主 UI 面板实例（MainControlPanelTochButton）
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `UserWidget` | - |

### `GetMainControlUI`

```text
GetMainControlUI() -> UserWidget
```

获取主控制 UI 面板实例（MainControlBaseUI）
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `UserWidget` | - |

### `GetShootingUIPanel`

```text
GetShootingUIPanel() -> UserWidget
```

获取射击相关UI面板实例（ShootingUIPanel）
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `UserWidget` | - |

### `GetSkillRootPanel`

```text
GetSkillRootPanel() -> UserWidget
```

获取技能相关UI面板实例（SkillRootPanel_BP）
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `UserWidget` | - |

### `GetUserWidgetByWidgetLayout`

```text
GetUserWidgetByWidgetLayout(WidgetLayoutPath: string, UserWidgetName: string) -> UserWidget
```

获取通过WidgetLayout加载的自定义UserWidget
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetLayoutPath` | `string` | 控件 ClassPath, 控件需继承自 UUserWidgetLayout |
| `UserWidgetName` | `string` | 控件 Name |

**Returns**

| Type | Description |
|---|---|
| `UserWidget` | - |

### `SubWidgetHiddenLayer`

```text
SubWidgetHiddenLayer(Widget: UserWidget)
```

【废弃】请使用 UGCWidgetManagerSystem.ShowWidget
SubWidgetHiddenLayer为控件减少隐藏层数（主要用于屏蔽玩法中不需要的和平 UI，HiddenLayer>=1，UI 会强制隐藏）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UserWidget` | - |

### `SetVirtualJoystickVisibility`

```text
SetVirtualJoystickVisibility(IsVisibility: boolean)
```

设置摇杆是否可见
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsVisibility` | `boolean` | 是否可见（true 为显示，false 为隐藏） |

### `SetCrosshairVisibility`

```text
SetCrosshairVisibility(IsVisibility: boolean)
```

设置准星是否可见
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsVisibility` | `boolean` | 是否可见（true 为显示，false 为隐藏，在没有被隐藏的情况下禁止将其显示） |

### `Share`

```text
Share(CloseCallBack: function) -> bool
```

弹出分享界面
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CloseCallBack` | `function` | 关闭分享界面回调函数 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 分享调用是否成功 |

### `AddChildToTochButton`

```text
AddChildToTochButton(Widget: UserWidget)
```

把自定义 UI 挂到和平 UI 上并应用自定义布局
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UserWidget` | - |

### `LoadLobbyChatFrameUI`

```text
LoadLobbyChatFrameUI()
```

加载大厅聊天框 UI
生效范围：客户端

### `AddObjectPositionUI`

```text
AddObjectPositionUI(Actor: Actor, WidgetClassPath: string, Offset: FVector, SizeAutoContent: boolean, OutViewHide: boolean, BeOcclusionHide: boolean, ShowSelf: boolean) -> number
```

添加对象位置 UI,头顶 UI（类似血条，玩家名）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | 需要添加位置 UI 的 Actor 对象 |
| `WidgetClassPath` | `string` | 控件 ClassPath 控件需继承自 UObjectPositionWidget |
| `Offset` | `FVector` | 偏移量 |
| `SizeAutoContent` | `boolean` | 大小适配 |
| `OutViewHide` | `boolean` | 控件离开镜头后是否隐藏（比如在背后） |
| `BeOcclusionHide` | `boolean` | 被遮挡后是否隐藏 |
| `ShowSelf` | `boolean` | 是否显示自己的 |

**Returns**

| Type | Description |
|---|---|
| `number` | 实例 Index |

### `AddObjectPositionUI_Custom`

```text
AddObjectPositionUI_Custom(Actor: Actor, WidgetClassPath: string, ObjectPosUIInfo: FObjectPosUIInfo) -> number
```

添加对象位置 UI,头顶 UI（类似血条，玩家名），自定义版本，提供更多参数配置。（ObjectPosUIInfo 可在蓝图中添加参数使用带有默认值的版本）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | 需要添加位置 UI 的 Actor 对象 |
| `WidgetClassPath` | `string` | 控件 ClassPath 控件需继承自 UObjectPositionWidget |
| `ObjectPosUIInfo` | `FObjectPosUIInfo` | 配置属性结构体，可以在蓝图中定义该变量传入 |

**Returns**

| Type | Description |
|---|---|
| `number` | 实例 Index |

### `RemoveObjectPositionUI`

```text
RemoveObjectPositionUI(WorldContent: UObject, InstanceIndex: number)
```

移除对象位置 UI
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContent` | `UObject` | 世界中对象 |
| `InstanceIndex` | `number` | 实例 Index |

### `GetObjectPositionUI`

```text
GetObjectPositionUI(WorldContent: UObject, InstanceIndex: number) -> @Widget
```

根据 InstanceIndex 获取 Widget 实例（Add 之后不能立刻获取到，Widget 有可能还在加载）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContent` | `UObject` | 世界中对象 |
| `InstanceIndex` | `number` | 实例 Index |

**Returns**

| Type | Description |
|---|---|
| `@Widget` | 实例 |

### `SetPlayerStateUIVisibility`

```text
SetPlayerStateUIVisibility(bVisible: boolean) -> number
```

设置玩家状态 UI 可见性
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bVisible` | `boolean` | 是否显示（true 为显示，false 为隐藏） |

**Returns**

| Type | Description |
|---|---|
| `number` | 实际修改的控件数量 |

### `ShowTipsUI`

```text
ShowTipsUI(TipsContent: string)
```

在屏幕中间上方显示 Tips 内容
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TipsContent` | `string` | Tips 文字内容 |

### `ShowTipsUIByServer`

```text
ShowTipsUIByServer(TipsContent: string, PlayerController: PlayerController)
```

在屏幕中间上方显示 Tips 内容，从DS发起，在传入的PC所属的客户端显示
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TipsContent` | `string` | Tips 文字内容 |
| `PlayerController` | `PlayerController` | 玩家控制器 |

### `GetGlobalOBUI`

```text
GetGlobalOBUI() -> UserWidget
```

获取全局观战 UI，仅全局观战模式下生效
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `UserWidget` | - |

### `ChangeMap`

```text
ChangeMap(MapPath: string, MapCentre: FVector, MapSize: number, MapScale: number)
```

修改右上角地图
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MapPath` | `string` | 地图文件路径 |
| `MapCentre` | `FVector` | 地图中心点坐标 |
| `MapSize` | `number` | 地图实际大小 |
| `MapScale` | `number` | 地图缩放比 |

### `ChangeMapByMapID`

```text
ChangeMapByMapID(MapID: number)
```

根据地图ID修改右上角地图
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MapID` | `number` | 地图ID |

### `ProjectWorldLocationToWidgetPosition`

```text
ProjectWorldLocationToWidgetPosition(WorldLocation: FVector) -> FVector2D
```

将世界坐标转换为控件坐标
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector` | 世界坐标 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 控件坐标 |

### `SlotAsCanvasSlot`

```text
SlotAsCanvasSlot(Widget: UUserWidget) -> UCanvasPanelSlot
```

获取 Canvas 插槽
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

**Returns**

| Type | Description |
|---|---|
| `UCanvasPanelSlot` | Canvas 插槽实例 |

### `SlotAsOverlaySlot`

```text
SlotAsOverlaySlot(Widget: UUserWidget) -> @Overlay
```

获取 Overlay 插槽
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

**Returns**

| Type | Description |
|---|---|
| `@Overlay` | 插槽实例 |

### `SlotAsVerticalBoxSlot`

```text
SlotAsVerticalBoxSlot(Widget: UUserWidget) -> @HorizontalBox
```

获取 HorizontalBox 插槽
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget` | 控件实例 |

**Returns**

| Type | Description |
|---|---|
| `@HorizontalBox` | 插槽实例 |

### `GetViewportScale`

```text
GetViewportScale() -> number
```

获取视口缩放比例
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `number` | 缩放比例 |

### `GetViewportSize`

```text
GetViewportSize() -> FVector2D
```

获取视口尺寸
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 视口尺寸 |

### `GetViewportWidgetGeometry`

```text
GetViewportWidgetGeometry() -> FGeometry
```

获取视口 Widget 几何信息
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `FGeometry` | 几何信息 |

### `AbsoluteToLocal`

```text
AbsoluteToLocal(Geometry: FGeometry, AbsoluteCoordinate: FVector2D) -> FVector2D
```

绝对坐标转本地坐标
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry` | 控件几何信息 |
| `AbsoluteCoordinate` | `FVector2D` | 绝对坐标 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 本地坐标 |

### `LocalToAbsolute`

```text
LocalToAbsolute(Geometry: FGeometry, LocalCoordinate: FVector2D) -> FVector2D
```

本地坐标转绝对坐标
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry` | 控件几何信息 |
| `LocalCoordinate` | `FVector2D` | 本地坐标 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 绝对坐标 |

### `GetLocalSize`

```text
GetLocalSize(Geometry: FGeometry) -> FVector2D
```

获取控件的本地尺寸
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry` | 控件几何信息 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 本地尺寸 |

### `GetAbsoluteSize`

```text
GetAbsoluteSize(Geometry: FGeometry) -> FVector2D
```

获取控件的绝对尺寸
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry` | 控件几何信息 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 绝对尺寸 |

### `GetAbsolutePosition`

```text
GetAbsolutePosition(Geometry: FGeometry) -> FVector2D
```

获取控件的绝对位置
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry` | 控件几何信息 |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | 绝对位置 |

### `GetWidgetFromName`

```text
GetWidgetFromName(Widget: UserWidget, UserWidgetName: string) -> UserWidget
```

【废弃】请使用 UGCWidgetManagerSystem.GetSubWidget
通过控件名获取某一控件的子控件
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UserWidget` | - |
| `UserWidgetName` | `string` | 控件 Name |

**Returns**

| Type | Description |
|---|---|
| `UserWidget` | - |

### `LoadMainUIWidgetLayoutByPath`

```text
LoadMainUIWidgetLayoutByPath(WidgetLayoutPath: string)
```

【废弃】请使用 UGCWidgetManagerSystem.SetWidgetLayout
可视化设置主 UI 控件是否可见（主要用于可视化屏蔽玩法中不需要的和平 UI，UI 会强制隐藏）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetLayoutPath` | `string` | 控件 ClassPath, 控件需继承自 UUserWidgetLayout |

### `UnloadMainUIWidgetLayoutByPath`

```text
UnloadMainUIWidgetLayoutByPath(WidgetLayoutPath: string)
```

【废弃】请使用 UGCWidgetManagerSystem.SetWidgetLayout
可视化设置主 UI 控件是否可见（主要用于可视化屏蔽玩法中不需要的和平 UI，UI 会强制隐藏）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetLayoutPath` | `string` | 控件 ClassPath, 控件需继承自 UUserWidgetLayout |

### `AddChildToUISlotByPath`

```text
AddChildToUISlotByPath(WidgetPath: string, UISlotName: string, ZOrder: number, AnchorData: FAnchorData) -> PromiseFuture
```

【废弃】请使用 UGCWidgetManagerSystem.CreateWidgetAsync() + UGCWidgetManagerSystem.AddToSlot()
把自定义 UI 挂到和平 UI 挂点上
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetPath` | `string` | 控件 ClassPath |
| `UISlotName` | `string` | 挂点标识 |
| `ZOrder` | `number` | 层级 |
| `AnchorData` | `FAnchorData` | 控件布局信息 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | PromiseFuture对象 |

### `AddChildToUISlotByWidget`

```text
AddChildToUISlotByWidget(Widget: UserWidget, UISlotName: string, ZOrder: number, AnchorData: FAnchorData)
```

【废弃】请使用 UGCWidgetManagerSystem.AddToSlot
把自定义 UI 挂到和平 UI 挂点上
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UserWidget` | UI |
| `UISlotName` | `string` | 挂点标识 |
| `ZOrder` | `number` | 层级 |
| `AnchorData` | `FAnchorData` | 控件布局信息 |

### `AddWidgetHiddenLayer`

```text
AddWidgetHiddenLayer(Widget: UserWidget)
```

【废弃】请使用 UGCWidgetManagerSystem.HideWidget
为控件添加隐藏层数（主要用于屏蔽玩法中不需要的和平 UI，HiddenLayer>=1，UI 会强制隐藏）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UserWidget` | - |

### `AddNewUI`

```text
AddNewUI(WidgetClassPath: string, IsAdaptation: boolean) -> UserWidget
```

【废弃】请使用 UGCWidgetManagerSystem.CreateWidgetAsync() + UGCWidgetManagerSystem.AddToSlot()
添加新 UI，将会自动完成 AddViewport 显示
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetClassPath` | `string` | Widget 路径 |
| `IsAdaptation` | `boolean` | 是否屏幕适配 |

**Returns**

| Type | Description |
|---|---|
| `UserWidget` | - |

### `CreateNewWidget`

```text
CreateNewWidget(WidgetClassPath: string) -> UserWidget
```

【废弃】请使用 UGCWidgetManagerSystem.CreateWidgetAsync
创建新控件
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetClassPath` | `string` | Widget 路径 |

**Returns**

| Type | Description |
|---|---|
| `UserWidget` | - |

### `CreateNewWidgetAsync`

```text
CreateNewWidgetAsync(WidgetClassPath: string, InCreatedDelegate: ULuaSingleDelegate)
```

【废弃】请使用 UGCWidgetManagerSystem.CreateWidgetAsync
异步创建新控件，并绑定回调
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetClassPath` | `string` | Widget 路径 |
| `InCreatedDelegate` | `ULuaSingleDelegate` | 回调 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGeneralProjectSettings.json -->

# UGeneralProjectSettings

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CompanyName` | `FString` | The name of the company (author, provider) that created the project. |
| `CompanyDistinguishedName` | `FString` | The distinguished name of the company (author, provider) that created the project. |
| `CopyrightNotice` | `FString` | The project's copyright andor trademark notices. |
| `Description` | `FString` | The project's description text. |
| `Homepage` | `FString` | The project's homepage URL. |
| `LicensingTerms` | `FString` | The project's licensing terms. |
| `PrivacyPolicy` | `FString` | The project's privacy policy. |
| `ProjectID` | `FGuid` | The project's unique identifier. |
| `ProjectName` | `FString` | The project's name. |
| `ProjectVersion` | `FString` | The project's version number. |
| `SupportContact` | `FString` | The project's support contact information. |
| `ProjectDisplayedTitle` | `FText` | - |
| `ProjectDebugTitleInfo` | `FText` | - |
| `bShouldWindowPreserveAspectRatio` | `bool` | Should the game's window preserve its aspect ratio when resized by user. |
| `bUseBorderlessWindow` | `bool` | Should the game use a borderless Slate window instead of a window with system title bar and border |
| `bStartInVR` | `bool` | Should the game attempt to start in VR, regardless of whether -vr was set on the commandline |
| `bStartInAR` | `bool` | Should the game start in AR |
| `bAllowWindowResize` | `bool` | - |
| `bAllowClose` | `bool` | - |
| `bAllowMaximize` | `bool` | - |
| `bAllowMinimize` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGIBoxVolumeComponent.json -->

# UGIBoxVolumeComponent

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Extents` | `FVector` | - |
| `FadeExtents_Neg` | `FVector` | - |
| `FadeExtents_Pos` | `FVector` | - |
| `bOutdoorTransition` | `bool` | - |
| `VolumeAlpha` | `float` | - |
| `Brightness` | `float` | - |
| `SkyIntensity` | `float` | - |
| `Priority` | `int32` | - |
| `AmbientCube2` | `FAmbientCube2` | - |
| `DebugColor` | `FColor` | - |
| `bUseProbeForGIVolume` | `bool` | - |
| `TransitionDistance` | `float` | - |
| `AmbientCube` | `FAmbientCube` | - |
| `VolumeProbeGIOptions` | `FVolumeProbeGIOptions` | - |
| `bUseCustomCapture` | `bool` | - |
| `bOldCubemap` | `bool` | - |
| `CapturedTransform` | `FTransform` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGIVolumesContainerComponent.json -->

# UGIVolumesContainerComponent

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Intensities` | `TArray < FLinearColor >` | - |
| `ColorSettings` | `TArray < FAmbientCube2 >` | - |
| `AutomaticCaptureIndices` | `TArray < uint32 >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGridPanel.json -->

# UGridPanel

A panel that evenly divides up available space between all of its children.
  
   Many Children

## Inheritance

`UPanelWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ColumnFill` | `TArray < float >` | The column fill rules |
| `RowFill` | `TArray < float >` | The row fill rules |

## Functions

### `AddChildToGrid`

```text
AddChildToGrid(Content: UWidget *) -> UGridSlot *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UGridSlot *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGridPathFollowingComponent.json -->

# UGridPathFollowingComponent

Path following augmented with local navigation grids
 
   Keeps track of nearby grids and use them instead of navigation path when agent is inside.
   Once outside grid, regular path following is resumed.
 
   This allows creating dynamic navigation obstacles with fully static navigation (e.g. static navmesh),
   as long as they are minor modifications for path. Not recommended for blocking off entire corridors.
 
   Does not replace proper avoidance for dynamic obstacles!

## Inheritance

`UPathFollowingComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GridManager` | `UNavLocalGridManager *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGridSlot.json -->

# UGridSlot

A slot for UGridPanel, these slots all share the same size as the largest slot
  in the grid.

## Inheritance

`UPanelSlot`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Padding` | `FMargin` | The padding area between the slot and the content it contains. |
| `HorizontalAlignment` | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the object horizontally. |
| `VerticalAlignment` | `TEnumAsByte < EVerticalAlignment >` | The alignment of the object vertically. |
| `Row` | `int32` | The row index of the cell this slot is in |
| `RowSpan` | `int32` | - |
| `Column` | `int32` | The column index of the cell this slot is in |
| `ColumnSpan` | `int32` | - |
| `Layer` | `int32` | Positive values offset this cell to be hit-tested and drawn on top of others. Default is 0; i.e. no offset. |
| `Nudge` | `FVector2D` | Offset this slot's content by some amount; positive values offset to lower right |

## Functions

### `SetPadding`

```text
SetPadding(InPadding: FMargin) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPadding` | `FMargin` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRow`

```text
SetRow(InRow: int32) -> void
```

Sets the row index of the slot, this determines what cell the slot is in the panel

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRow` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRowSpan`

```text
SetRowSpan(InRowSpan: int32) -> void
```

How many rows this this slot spans over

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRowSpan` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetColumn`

```text
SetColumn(InColumn: int32) -> void
```

Sets the column index of the slot, this determines what cell the slot is in the panel

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColumn` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetColumnSpan`

```text
SetColumnSpan(InColumnSpan: int32) -> void
```

How many columns this slot spans over

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColumnSpan` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLayer`

```text
SetLayer(InLayer: int32) -> void
```

Sets positive values offset this cell to be hit-tested and drawn on top of others.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InLayer` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHorizontalAlignment`

```text
SetHorizontalAlignment(InHorizontalAlignment: EHorizontalAlignment) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InHorizontalAlignment` | `EHorizontalAlignment` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVerticalAlignment`

```text
SetVerticalAlignment(InVerticalAlignment: EVerticalAlignment) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVerticalAlignment` | `EVerticalAlignment` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGridVisibilityCaptureComponent.json -->

# UGridVisibilityCaptureComponent

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FOVAngle` | `float` | Camera field of view (in degrees). |
| `CaptureViewSize` | `FIntPoint` | - |
| `NearClipPlane` | `float` | - |
| `GridMesh` | `UStaticMesh *` | - |
| `GridMeshSizeScale` | `FVector` | - |
| `GridMeshLocationOffset` | `FVector` | - |
| `bForceLowestLOD` | `uint32` | - |
| `bHiddenFoliage` | `uint32` | - |
| `OcclusionDepthDiffThreshold` | `float` | - |
| `bShouldRenderGridMeshInMainPass` | `uint32` | - |
| `MaxNumProcessWaitingResultCmdsPerFrame` | `int32` | - |
| `MaxNumProcessWaitingCalculateCmdsPerFrame` | `int32` | - |
| `GridSize` | `FIntPoint` | - |
| `RenderTargetToCreateRenderer` | `UTextureRenderTarget2D *` | - |
| `GridMeshComp` | `UInstancedStaticMeshComponent *` | - |

## Functions

### `InitGridIDVisibilityCalculation`

```text
InitGridIDVisibilityCalculation(InGridLocations: TArray < FVector > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InGridLocations` | `TArray < FVector > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CalculateGridIDVisibility`

```text
CalculateGridIDVisibility(GridID: int32, CameraLocations: TArray < FGridVisibilityCameraInfo > &, PotentialGrids: TArray < int32 > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GridID` | `int32` | - |
| `CameraLocations` | `TArray < FGridVisibilityCameraInfo > &` | - |
| `PotentialGrids` | `TArray < int32 > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FinishGridIDVisibilityCalculation`

```text
FinishGridIDVisibilityCalculation() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UHapticFeedbackEffect_Buffer.json -->

# UHapticFeedbackEffect_Buffer

## Inheritance

`UHapticFeedbackEffect_Base`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Amplitudes` | `TArray < uint8 >` | - |
| `SampleRate` | `int` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UHapticFeedbackEffect_Curve.json -->

# UHapticFeedbackEffect_Curve

## Inheritance

`UHapticFeedbackEffect_Base`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `HapticDetails` | `FHapticFeedbackDetails_Curve` | - |
| `AndroidTesting` | `FJsonHaptic` | - |
| `JsonValue` | `FString` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UHapticFeedbackEffect_SoundWave.json -->

# UHapticFeedbackEffect_SoundWave

## Inheritance

`UHapticFeedbackEffect_Base`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SoundWave` | `USoundWave *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UHeadMountedDisplayFunctionLibrary.json -->

# UHeadMountedDisplayFunctionLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `IsHeadMountedDisplayEnabled`

```text
IsHeadMountedDisplayEnabled() -> bool
```

Returns whether or not we are currently using the head mounted display.

**Returns**

| Type | Description |
|---|---|
| `bool` | (Boolean)  status of HMD |

### `IsHeadMountedDisplayConnected`

```text
IsHeadMountedDisplayConnected() -> bool
```

Returns whether or not the HMD hardware is connected and ready to use.  It may or may not actually be in use.

**Returns**

| Type | Description |
|---|---|
| `bool` | (Boolean)  status whether the HMD hardware is connected and ready to use.  It may or may not actually be in use. |

### `EnableHMD`

```text
EnableHMD(bEnable: bool) -> bool
```

Switches tofrom using HMD and stereo rendering.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | (in) 'true' to enable HMD stereo; 'false' otherwise |

**Returns**

| Type | Description |
|---|---|
| `bool` | (Boolean)		True, if the request was successful. |

### `GetHMDDeviceName`

```text
GetHMDDeviceName() -> FName
```

Returns the name of the device, so scripts can modify their behaviour appropriately

**Returns**

| Type | Description |
|---|---|
| `FName` | FName specific to the currently active HMD device type.  "None" implies no device, "Unknown" implies a device with no description. |

### `GetHMDWornState`

```text
GetHMDWornState() -> EHMDWornState :: Type
```

Returns the worn state of the device.

**Returns**

| Type | Description |
|---|---|
| `EHMDWornState :: Type` | Unknown, Worn, NotWorn.  If the platform does not detect this it will always return Unknown. |

### `GetOrientationAndPosition`

```text
GetOrientationAndPosition(DeviceRotation: FRotator &, DevicePosition: FVector &) -> void
```

Grabs the current orientation and position for the HMD.  If positional tracking is not available, DevicePosition will be a zero vector

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeviceRotation` | `FRotator &` | (out) The device's current rotation |
| `DevicePosition` | `FVector &` | (out) The device's current position, in its own tracking space |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HasValidTrackingPosition`

```text
HasValidTrackingPosition() -> bool
```

If the HMD supports positional tracking, whether or not we are currently being tracked

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetNumOfTrackingSensors`

```text
GetNumOfTrackingSensors() -> int32
```

If the HMD has multiple positional tracking sensors, return a total number of them currently connected.

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetTrackingSensorParameters`

```text
GetTrackingSensorParameters(Origin: FVector &, Rotation: FRotator &, LeftFOV: float &, RightFOV: float &, TopFOV: float &, BottomFOV: float &, Distance: float &, NearPlane: float &, FarPlane: float &, IsActive: bool &, Index: int32) -> void
```

If the HMD has a positional sensor, this will return the game-world location of it, as well as the parameters for the bounding region of tracking.
	  This allows an in-game representation of the legal positional tracking range.  All values will be zeroed if the sensor is not available or the HMD does not support it.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Origin` | `FVector &` | (out) Origin, in world-space, of the sensor |
| `Rotation` | `FRotator &` | (out) Rotation, in world-space, of the sensor |
| `LeftFOV` | `float &` | (out) Field-of-view, left from center, in degrees, of the valid tracking zone of the sensor |
| `RightFOV` | `float &` | (out) Field-of-view, right from center, in degrees, of the valid tracking zone of the sensor |
| `TopFOV` | `float &` | (out) Field-of-view, top from center, in degrees, of the valid tracking zone of the sensor |
| `BottomFOV` | `float &` | (out) Field-of-view, bottom from center, in degrees, of the valid tracking zone of the sensor |
| `Distance` | `float &` | (out) Nominal distance to sensor, in world-space |
| `NearPlane` | `float &` | (out) Near plane distance of the tracking volume, in world-space |
| `FarPlane` | `float &` | (out) Far plane distance of the tracking volume, in world-space |
| `IsActive` | `bool &` | (out) True, if the query for the specified sensor succeeded. |
| `Index` | `int32` | (in) Index of the tracking sensor to query |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPositionalTrackingCameraParameters`

```text
GetPositionalTrackingCameraParameters(CameraOrigin: FVector &, CameraRotation: FRotator &, HFOV: float &, VFOV: float &, CameraDistance: float &, NearPlane: float &, FarPlane: float &) -> void
```

If the HMD has a positional sensor, this will return the game-world location of it, as well as the parameters for the bounding region of tracking.
	  This allows an in-game representation of the legal positional tracking range.  All values will be zeroed if the sensor is not available or the HMD does not support it.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CameraOrigin` | `FVector &` | - |
| `CameraRotation` | `FRotator &` | - |
| `HFOV` | `float &` | (out) Field-of-view, horizontal, in degrees, of the valid tracking zone of the sensor |
| `VFOV` | `float &` | (out) Field-of-view, vertical, in degrees, of the valid tracking zone of the sensor |
| `CameraDistance` | `float &` | (out) Nominal distance to sensor, in world-space |
| `NearPlane` | `float &` | (out) Near plane distance of the tracking volume, in world-space |
| `FarPlane` | `float &` | (out) Far plane distance of the tracking volume, in world-space |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsInLowPersistenceMode`

```text
IsInLowPersistenceMode() -> bool
```

Returns true, if HMD is in low persistence mode. 'false' otherwise.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `EnableLowPersistenceMode`

```text
EnableLowPersistenceMode(bEnable: bool) -> void
```

Switches between low and full persistence modes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | (in) 'true' to enable low persistence mode; 'false' otherwise |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetOrientationAndPosition`

```text
ResetOrientationAndPosition(Yaw: float, Options: EOrientPositionSelector :: Type) -> void
```

Resets orientation by setting roll and pitch to 0, assuming that current yaw is forward direction and assuming
	  current position as a 'zero-point' (for positional tracking).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Yaw` | `float` | (in) the desired yaw to be set after orientation reset. |
| `Options` | `EOrientPositionSelector :: Type` | (in) specifies either position, orientation or both should be reset. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetClippingPlanes`

```text
SetClippingPlanes(Near: float, Far: float) -> void
```

Sets near and far clipping planes (NCP and FCP) for stereo rendering. Similar to 'stereo ncp= fcp' console command, but NCP and FCP set by this
	  call won't be saved in .ini file.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Near` | `float` | (in) Near clipping plane, in centimeters |
| `Far` | `float` | (in) Far clipping plane, in centimeters |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetScreenPercentage`

```text
GetScreenPercentage() -> float
```

Returns screen percentage to be used in VR mode.

**Returns**

| Type | Description |
|---|---|
| `float` | (float)	The screen percentage to be used in VR mode. |

### `SetWorldToMetersScale`

```text
SetWorldToMetersScale(WorldContext: UObject *, NewScale: float) -> void
```

Sets the World to Meters scale, which changes the scale of the world as perceived by the player

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject *` | - |
| `NewScale` | `float` | Specifies how many Unreal units correspond to one meter in the real world |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetWorldToMetersScale`

```text
GetWorldToMetersScale(WorldContext: UObject *) -> float
```

Returns the World to Meters scale, which corresponds to the scale of the world as perceived by the player

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | How many Unreal units correspond to one meter in the real world |

### `SetTrackingOrigin`

```text
SetTrackingOrigin(Origin: TEnumAsByte < EHMDTrackingOrigin :: Type >) -> void
```

Sets current tracking origin type (eye level or floor level).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Origin` | `TEnumAsByte < EHMDTrackingOrigin :: Type >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTrackingOrigin`

```text
GetTrackingOrigin() -> TEnumAsByte < EHMDTrackingOrigin :: Type >
```

Returns current tracking origin type (eye level or floor level).

**Returns**

| Type | Description |
|---|---|
| `TEnumAsByte < EHMDTrackingOrigin :: Type >` | - |

### `GetVRFocusState`

```text
GetVRFocusState(bUseFocus: bool &, bHasFocus: bool &) -> void
```

Returns current state of VR focus.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bUseFocus` | `bool &` | (out) if set to true, then this App does use VR focus. |
| `bHasFocus` | `bool &` | (out) if set to true, then this App currently has VR focus. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsSpectatorScreenModeControllable`

```text
IsSpectatorScreenModeControllable() -> bool
```

Return true if spectator screen mode control is available.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetSpectatorScreenMode`

```text
SetSpectatorScreenMode(Mode: ESpectatorScreenMode) -> void
```

Sets the social screen mode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Mode` | `ESpectatorScreenMode` | (in) The social screen Mode. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSpectatorScreenTexture`

```text
SetSpectatorScreenTexture(InTexture: UTexture *) -> void
```

Change the texture displayed on the social screen

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTexture` | `UTexture *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSpectatorScreenModeTexturePlusEyeLayout`

```text
SetSpectatorScreenModeTexturePlusEyeLayout(EyeRectMin: FVector2D, EyeRectMax: FVector2D, TextureRectMin: FVector2D, TextureRectMax: FVector2D, bDrawEyeFirst: bool, bClearBlack: bool) -> void
```

Setup the layout for ESpectatorScreenMode::TexturePlusEye.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EyeRectMin` | `FVector2D` | - |
| `EyeRectMax` | `FVector2D` | - |
| `TextureRectMin` | `FVector2D` | - |
| `TextureRectMax` | `FVector2D` | - |
| `bDrawEyeFirst` | `bool` | - |
| `bClearBlack` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UHierarchicalInstancedStaticMeshComponent.json -->

# UHierarchicalInstancedStaticMeshComponent

## Inheritance

`UInstancedStaticMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SortedInstances` | `TArray < int32 >` | - |
| `NumBuiltInstances` | `int32` | - |
| `BuiltInstanceBounds` | `FBox` | - |
| `UnbuiltInstanceBounds` | `FBox` | - |
| `UnbuiltInstanceBoundsList` | `TArray < FBox >` | - |
| `UnbuiltInstanceIndexList` | `TArray < int32 >` | - |
| `bEnableDensityScaling` | `uint32` | - |
| `OcclusionLayerNumNodes` | `int32` | - |
| `CacheMeshExtendedBounds` | `FBoxSphereBounds` | - |
| `bDisableCollision` | `bool` | - |
| `MinInstancesToSplitNode` | `int32` | Culling by Num |
| `OptimiMinInstancesToSplitNode` | `int32` | Culling by Num For Optimization FClusterTree |
| `IsOpenTreeOptimi` | `bool` | Mark Use OptimiMinInstancesToSplitNode With FClusterTree |
| `InstanceCullDistanceByVolume` | `float` | Instance Culling by CullDistanceVolume |
| `bEnableScaleOpt` | `bool` | - |
| `AverageScale` | `FVector` | - |

## Functions

### `RemoveInstances`

```text
RemoveInstances(InstancesToRemove: TArray < int32 > &) -> bool
```

Removes all the instances with indices specified in the InstancesToRemove array. Returns true on success.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstancesToRemove` | `TArray < int32 > &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UHierarchicalLODSetup.json -->

# UHierarchicalLODSetup

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `HierarchicalLODSetup` | `TArray < struct FHierarchicalSimplification >` | Hierarchical LOD Setup |
| `OverrideBaseMaterial` | `TSoftObjectPtr < UMaterialInterface >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UHLODProxy.json -->

# UHLODProxy

This asset acts as a proxy to a static mesh for ALODActors to display

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ProxyMeshes` | `TArray < FHLODProxyMesh >` | All the mesh proxies we contain |
| `OwningMap` | `TSoftObjectPtr < UWorld >` | Keep hold of the level in the editor to allow for package cleaning etc. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UHorizontalBox.json -->

# UHorizontalBox

Allows widgets to be laid out in a flow horizontally.
 
   Many Children
   Flow Horizontal

## Inheritance

`UPanelWidget`

## Functions

### `AddChildToHorizontalBox`

```text
AddChildToHorizontalBox(Content: UWidget *) -> UHorizontalBoxSlot *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UHorizontalBoxSlot *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UHorizontalBoxSlot.json -->

# UHorizontalBoxSlot

## Inheritance

`UPanelSlot`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Padding` | `FMargin` | The amount of padding between the slots parent and the content. |
| `Size` | `FSlateChildSize` | How much space this slot should occupy in the direction of the panel. |
| `HorizontalAlignment` | `TEnumAsByte < EHorizontalAlignment >` | - |
| `VerticalAlignment` | `TEnumAsByte < EVerticalAlignment >` | - |

## Functions

### `SetPadding`

```text
SetPadding(InPadding: FMargin) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPadding` | `FMargin` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSize`

```text
SetSize(InSize: FSlateChildSize) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSize` | `FSlateChildSize` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHorizontalAlignment`

```text
SetHorizontalAlignment(InHorizontalAlignment: EHorizontalAlignment) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InHorizontalAlignment` | `EHorizontalAlignment` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVerticalAlignment`

```text
SetVerticalAlignment(InVerticalAlignment: EVerticalAlignment) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVerticalAlignment` | `EVerticalAlignment` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UHudSettings.json -->

# UHudSettings

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bShowHUD` | `uint32` | Whether the HUD is visible at all. |
| `DebugDisplay` | `TArray < FName >` | Collection of names specifying what debug info to display for ViewTarget actor. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UIdeaGrassFieldFunctionLibrary.json -->

# UIdeaGrassFieldFunctionLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `IdeaGrassRenderForceTexture`

```text
IdeaGrassRenderForceTexture(GrassFieldData: FIdeaGrassFieldData) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GrassFieldData` | `FIdeaGrassFieldData` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IdeaGrassRenderForceTextureFade`

```text
IdeaGrassRenderForceTextureFade(GrassFieldData: FIdeaGrassFieldData) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GrassFieldData` | `FIdeaGrassFieldData` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IdeaGrassRenderForceTextureTrample`

```text
IdeaGrassRenderForceTextureTrample(GrassFieldData: FIdeaGrassFieldData) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GrassFieldData` | `FIdeaGrassFieldData` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IdeaGrassRenderForceTextureSkill`

```text
IdeaGrassRenderForceTextureSkill(GrassFieldData: FIdeaGrassFieldData) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GrassFieldData` | `FIdeaGrassFieldData` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UImage.json -->

# UImage

The image widget allows you to display a Slate Brush, or texture or material in the UI.
 
   No Children

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BrushImage` | `TSoftObjectPtr < UObject >` | - |
| `bIsEnhancedImage` | `bool` | - |
| `ForceAsyncLoadReference` | `bool` | - |
| `BrushAssetReference` | `FStringAssetReference` | - |
| `Brush` | `FSlateBrush` | Image to draw |
| `BrushMaterialParamNames` | `FString` | - |
| `BrushDelegate` | `FGetSlateBrush` | A bindable delegate for the Image. |
| `ColorAndOpacity` | `FLinearColor` | Color and opacity |
| `ColorAndOpacityDelegate` | `FGetLinearColor` | A bindable delegate for the ColorAndOpacity. |
| `bIsUseEnhancedHitTest` | `bool` | 是否使用自定义触摸响应区域，在运行时修改无效 |
| `HitTestAreaRadius` | `float` | 圆形响应区域的半径，最大为控件边长一半，-1为控件大小一半 |
| `OnMouseButtonDownEvent` | `FOnPointerEvent` | - |

## Functions

### `GetBrush`

```text
GetBrush() -> FSlateBrush
```

**Returns**

| Type | Description |
|---|---|
| `FSlateBrush` | - |

### `SetColorAndOpacity`

```text
SetColorAndOpacity(InColorAndOpacity: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColorAndOpacity` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetColorRGBStr`

```text
SetColorRGBStr(HexString: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HexString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrushImageReference`

```text
SetBrushImageReference(AssetReference: FStringAssetReference) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetReference` | `FStringAssetReference` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrushImageReferenceWithMatchSize`

```text
SetBrushImageReferenceWithMatchSize(AssetReference: FStringAssetReference, bMatchSize: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetReference` | `FStringAssetReference` | - |
| `bMatchSize` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrushImageReferenceWithColor`

```text
SetBrushImageReferenceWithColor(AssetReference: FStringAssetReference, Color: FLinearColor, bMatchSize: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetReference` | `FStringAssetReference` | - |
| `Color` | `FLinearColor` | - |
| `bMatchSize` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOpacity`

```text
SetOpacity(InOpacity: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOpacity` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrush`

```text
SetBrush(InBrush: FSlateBrush &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBrush` | `FSlateBrush &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrushFromAsset`

```text
SetBrushFromAsset(Asset: USlateBrushAsset *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Asset` | `USlateBrushAsset *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrushFromTexture`

```text
SetBrushFromTexture(Texture: UTexture2D *, bMatchSize: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Texture` | `UTexture2D *` | - |
| `bMatchSize` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrushFromTextureDynamic`

```text
SetBrushFromTextureDynamic(Texture: UTexture2DDynamic *, bMatchSize: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Texture` | `UTexture2DDynamic *` | - |
| `bMatchSize` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrushFromMaterial`

```text
SetBrushFromMaterial(Material: UMaterialInterface *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Material` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDynamicMaterial`

```text
GetDynamicMaterial() -> UMaterialInstanceDynamic *
```

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | - |

### `SetDisablePaint`

```text
SetDisablePaint(InDisablePaint: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDisablePaint` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReleaseAsyncSetBrushHandle`

```text
ReleaseAsyncSetBrushHandle() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAsyncLoadImageAssetComplete`

```text
OnAsyncLoadImageAssetComplete() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAsyncLoadAssetComplete`

```text
OnAsyncLoadAssetComplete() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnImageChangeDelegate`

```text
OnImageChangeDelegate(BrushChanged: const FSlateBrush&) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BrushChanged` | `const FSlateBrush&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UImageCaptureSettings.json -->

# UImageCaptureSettings

## Inheritance

`UFrameGrabberProtocolSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CompressionQuality` | `int32` | Level of compression to apply to the image, between 1 (worst quality, best compression) and 100 (best quality, worst compression) |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UImportanceSamplingLibrary.json -->

# UImportanceSamplingLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `RandomSobolFloat`

```text
RandomSobolFloat(Index: int32, Dimension: int32, Seed: float) -> ENGINE_API float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - Which sequential point |
| `Dimension` | `int32` | - Which Sobol dimension (0 to 15) |
| `Seed` | `float` | - Random seed (in the range 0-1) to randomize across multiple sequences |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API float` | Sobol-distributed random number between 0 and 1 |

### `NextSobolFloat`

```text
NextSobolFloat(Index: int32, Dimension: int32, PreviousValue: float) -> ENGINE_API float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - Which sequential point |
| `Dimension` | `int32` | - Which Sobol dimension (0 to 15) |
| `PreviousValue` | `float` | - The Sobol value for Index-1 |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API float` | Sobol-distributed random number between 0 and 1 |

### `RandomSobolCell2D`

```text
RandomSobolCell2D(Index: int32, NumCells: int32, Cell: FVector2D, Seed: FVector2D) -> ENGINE_API FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - Which sequential point in the cell (starting at 0) |
| `NumCells` | `int32` | - Size of cell grid, 1 to 32768. Rounded up to the next power of two |
| `Cell` | `FVector2D` | - Give a point from this integer grid cell |
| `Seed` | `FVector2D` | - Random 2D seed (components in the range 0-1) to randomize across multiple sequences |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FVector2D` | Sobol-distributed random 2D position in the given grid cell |

### `NextSobolCell2D`

```text
NextSobolCell2D(Index: int32, NumCells: int32, PreviousValue: FVector2D) -> ENGINE_API FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - Which sequential point |
| `NumCells` | `int32` | - Size of cell grid, 1 to 32768. Rounded up to the next power of two |
| `PreviousValue` | `FVector2D` | - The Sobol value for Index-1 |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FVector2D` | Sobol-distributed random 2D position in the same grid cell |

### `RandomSobolCell3D`

```text
RandomSobolCell3D(Index: int32, NumCells: int32, Cell: FVector, Seed: FVector) -> ENGINE_API FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - Which sequential point in the cell (starting at 0) |
| `NumCells` | `int32` | - Size of cell grid, 1 to 1024. Rounded up to the next power of two |
| `Cell` | `FVector` | - Give a point from this integer grid cell |
| `Seed` | `FVector` | - Random 3D seed (components in the range 0-1) to randomize across multiple sequences |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FVector` | Sobol-distributed random 3D vector in the given grid cell |

### `NextSobolCell3D`

```text
NextSobolCell3D(Index: int32, NumCells: int32, PreviousValue: FVector) -> ENGINE_API FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - Which sequential point |
| `NumCells` | `int32` | - Size of cell grid, 1 to 1024. Rounded up to the next power of two |
| `PreviousValue` | `FVector` | - The Sobol value for Index-1 |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FVector` | Sobol-distributed random 3D position in the same grid cell |

### `MakeImportanceTexture`

```text
MakeImportanceTexture(Texture: UTexture2D *, WeightingFunc: TEnumAsByte < EImportanceWeight :: Type >) -> ENGINE_API FImportanceTexture
```

Create an FImportanceTexture object for texture-driven importance sampling from a 2D RGBA8 texture

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Texture` | `UTexture2D *` | - Texture object to use. Must be RGBA8 format. |
| `WeightingFunc` | `TEnumAsByte < EImportanceWeight :: Type >` | - How to turn the texture data into probability weights |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FImportanceTexture` | new ImportanceTexture object for use with ImportanceSample |

### `BreakImportanceTexture`

```text
BreakImportanceTexture(ImportanceTexture: FImportanceTexture &, Texture: UTexture2D * &, WeightingFunc: TEnumAsByte < EImportanceWeight :: Type > &) -> ENGINE_API void
```

Get texture used to create an ImportanceTexture object

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImportanceTexture` | `FImportanceTexture &` | - The source ImportanceTexture object |
| `Texture` | `UTexture2D * &` | - |
| `WeightingFunc` | `TEnumAsByte < EImportanceWeight :: Type > &` | - How to turn the texture data into probability weights |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | new ImportanceTexture object for use with ImportanceSample |

### `ImportanceSample`

```text
ImportanceSample(Texture: FImportanceTexture &, Rand: FVector2D &, Samples: int, Intensity: float, SamplePosition: FVector2D &, SampleColor: FLinearColor &, SampleIntensity: float &, SampleSize: float &) -> ENGINE_API void
```

Distribute sample points proportional to Texture2D luminance.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Texture` | `FImportanceTexture &` | - |
| `Rand` | `FVector2D &` | - Random 2D point with components evenly distributed between 0 and 1 |
| `Samples` | `int` | - Total number of samples that will be used |
| `Intensity` | `float` | - Total intensity for light |
| `SamplePosition` | `FVector2D &` | - |
| `SampleColor` | `FLinearColor &` | - |
| `SampleIntensity` | `float &` | - |
| `SampleSize` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInGameAdManager.json -->

# UInGameAdManager

## Inheritance

`UPlatformInterfaceBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bShouldPauseWhileAdOpen` | `uint32` | If true, the game will pause when the user clicks on the ad, which could take over the screen |
| `ClickedBannerDelegates` | `TArray < FOnUserClickedBanner >` | @todo document |
| `ClosedAdDelegates` | `TArray < FOnUserClosedAdvertisement >` | @todo document |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInheritableComponentHandler.json -->

# UInheritableComponentHandler

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Records` | `TArray < FComponentOverrideRecord >` | All component records |
| `UnnecessaryComponents` | `TArray < UActorComponent * >` | List of components that were marked unnecessary, need to keep these around so it doesn't regenerate them when a child asks for one |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInputActionDelegateBinding.json -->

# UInputActionDelegateBinding

## Inheritance

`UInputDelegateBinding`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputActionDelegateBindings` | `TArray < FBlueprintInputActionDelegateBinding >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInputAxisDelegateBinding.json -->

# UInputAxisDelegateBinding

## Inheritance

`UInputDelegateBinding`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputAxisDelegateBindings` | `TArray < FBlueprintInputAxisDelegateBinding >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInputAxisKeyDelegateBinding.json -->

# UInputAxisKeyDelegateBinding

## Inheritance

`UInputDelegateBinding`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputAxisKeyDelegateBindings` | `TArray < FBlueprintInputAxisKeyDelegateBinding >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInputComponent.json -->

# UInputComponent

Implement an Actor component for input bindings.
 
  An Input Component is a transient component that enables an Actor to bind various forms of input events to delegate functions.  
  Input components are processed from a stack managed by the PlayerController and processed by the PlayerInput.
  Each binding can consume the input event preventing other components on the input stack from processing the input.

## Inheritance

`UActorComponent`

## Functions

### `IsControllerKeyDown`

```text
IsControllerKeyDown(Key: FKey) -> bool
```

Returns true if the given keybutton is pressed on the input of the controller (if present)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `WasControllerKeyJustPressed`

```text
WasControllerKeyJustPressed(Key: FKey) -> bool
```

Returns true if the given keybutton was up last frame and down this frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `WasControllerKeyJustReleased`

```text
WasControllerKeyJustReleased(Key: FKey) -> bool
```

Returns true if the given keybutton was down last frame and up this frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetControllerAnalogKeyState`

```text
GetControllerAnalogKeyState(Key: FKey) -> float
```

Returns the analog value for the given keybutton.  If analog isn't supported, returns 1 for down and 0 for up.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetControllerVectorKeyState`

```text
GetControllerVectorKeyState(Key: FKey) -> FVector
```

Returns the vector value for the given keybutton.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTouchState`

```text
GetTouchState(FingerIndex: int32, LocationX: float &, LocationY: float &, bIsCurrentlyPressed: bool &) -> void
```

Returns the location of a touch, and if it's held down

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `int32` | - |
| `LocationX` | `float &` | - |
| `LocationY` | `float &` | - |
| `bIsCurrentlyPressed` | `bool &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetControllerKeyTimeDown`

```text
GetControllerKeyTimeDown(Key: FKey) -> float
```

Returns how long the given keybutton has been down.  Returns 0 if it's up or it just went down this frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetControllerMouseDelta`

```text
GetControllerMouseDelta(DeltaX: float &, DeltaY: float &) -> void
```

Retrieves how far the mouse moved this frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaX` | `float &` | - |
| `DeltaY` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetControllerAnalogStickState`

```text
GetControllerAnalogStickState(WhichStick: EControllerAnalogStick :: Type, StickX: float &, StickY: float &) -> void
```

Retrieves the X and Y displacement of the given analog stick.  For WhickStick, 0 = left, 1 = right.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WhichStick` | `EControllerAnalogStick :: Type` | - |
| `StickX` | `float &` | - |
| `StickY` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInputKeyDelegateBinding.json -->

# UInputKeyDelegateBinding

## Inheritance

`UInputDelegateBinding`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputKeyDelegateBindings` | `TArray < FBlueprintInputKeyDelegateBinding >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInputKeySelector.json -->

# UInputKeySelector

A widget for selecting a single key or a single key with a modifier.

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WidgetStyle` | `FButtonStyle` | The button style used at runtime |
| `TextStyle` | `FTextBlockStyle` | The button style used at runtime |
| `SelectedKey` | `FInputChord` | The currently selected key chord. |
| `Font_DEPRECATED` | `FSlateFontInfo` | - |
| `Margin` | `FMargin` | The amount of blank space around the text used to display the currently selected key. |
| `ColorAndOpacity_DEPRECATED` | `FLinearColor` | - |
| `KeySelectionText` | `FText` | Sets the text which is displayed while selecting keys. |
| `NoKeySpecifiedText` | `FText` | Sets the text to display when no key text is available or not selecting a key. |
| `bAllowModifierKeys` | `bool` | When true modifier keys such as control and alt are allowed in the <br>	 input chord representing the selected key, if false modifier keys are ignored. |
| `bAllowGamepadKeys` | `bool` | When true gamepad keys are allowed in the input chord representing the selected key, otherwise they are ignored. |
| `EscapeKeys` | `TArray < FKey >` | When true gamepad keys are allowed in the input chord representing the selected key, otherwise they are ignored. |

## Functions

### `SetSelectedKey`

```text
SetSelectedKey(InSelectedKey: FInputChord &) -> void
```

Sets the currently selected key.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSelectedKey` | `FInputChord &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetKeySelectionText`

```text
SetKeySelectionText(InKeySelectionText: FText) -> void
```

Sets the text which is displayed while selecting keys.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InKeySelectionText` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNoKeySpecifiedText`

```text
SetNoKeySpecifiedText(InNoKeySpecifiedText: FText) -> void
```

Sets the text to display when no key text is available or not selecting a key.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNoKeySpecifiedText` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAllowModifierKeys`

```text
SetAllowModifierKeys(bInAllowModifierKeys: bool) -> void
```

Sets whether or not modifier keys are allowed in the selected key.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInAllowModifierKeys` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAllowGamepadKeys`

```text
SetAllowGamepadKeys(bInAllowGamepadKeys: bool) -> void
```

Sets whether or not gamepad keys are allowed in the selected key.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInAllowGamepadKeys` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetIsSelectingKey`

```text
GetIsSelectingKey() -> bool
```

Returns true if the widget is currently selecting a key, otherwise returns false.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetTextBlockVisibility`

```text
SetTextBlockVisibility(InVisibility: ESlateVisibility) -> void
```

Sets the visibility of the text block.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVisibility` | `ESlateVisibility` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnKeySelected`

```text
OnKeySelected(SelectedKey: FInputChord) -> void
```

Called whenever a new key is selected by the user.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelectedKey` | `FInputChord` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnIsSelectingKeyChanged`

```text
OnIsSelectingKeyChanged() -> void
```

Called whenever the key selection mode starts or stops.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInputSettings.json -->

# UInputSettings

Project wide settings for input handling

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AxisConfig` | `TArray < struct FInputAxisConfigEntry >` | Properties of Axis controls |
| `bAltEnterTogglesFullscreen` | `uint32` | - |
| `bF11TogglesFullscreen` | `uint32` | - |
| `bUseMouseForTouch` | `uint32` | - |
| `bEnableMouseSmoothing` | `uint32` | - |
| `bEnableFOVScaling` | `uint32` | - |
| `FOVScale` | `float` | - |
| `DoubleClickTime` | `float` | If a key is pressed twice in this amount of time it is considered a "double click" |
| `bCaptureMouseOnLaunch` | `bool` | Controls if the viewport will capture the mouse on Launch of the application |
| `DefaultViewportMouseCaptureMode` | `EMouseCaptureMode` | The default mouse capture mode for the game viewport |
| `bDefaultViewportMouseLock_DEPRECATED` | `bool` | The default mouse lock state when the viewport acquires capture |
| `DefaultViewportMouseLockMode` | `EMouseLockMode` | The default mouse lock state behavior when the viewport acquires capture |
| `ActionMappings` | `TArray < struct FInputActionKeyMapping >` | List of Action Mappings |
| `AxisMappings` | `TArray < struct FInputAxisKeyMapping >` | List of Axis Mappings |
| `bAlwaysShowTouchInterface` | `bool` | Should the touch input interface be shown always, or only when the platform has a touch screen? |
| `bShowConsoleOnFourFingerTap` | `bool` | Whether or not to show the console on 4 finger tap, on mobile platforms |
| `DefaultTouchInterface` | `FSoftObjectPath` | The default on-screen touch input interface for the game (can be null to disable the onscreen interface) |
| `ConsoleKey_DEPRECATED` | `FKey` | The key which opens the console. |
| `ConsoleKeys` | `TArray < FKey >` | The keys which open the console. |

## Functions

### `GetInputSettings`

```text
GetInputSettings() -> UInputSettings *
```

Returns the game local input settings (action mappings, axis mappings, etc...)

**Returns**

| Type | Description |
|---|---|
| `UInputSettings *` | - |

### `AddActionMapping`

```text
AddActionMapping(KeyMapping: FInputActionKeyMapping &, bForceRebuildKeymaps: bool) -> void
```

Programmatically add an action mapping to the project defaults

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyMapping` | `FInputActionKeyMapping &` | - |
| `bForceRebuildKeymaps` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetActionMappingByName`

```text
GetActionMappingByName(InActionName: FName, OutMappings: TArray < FInputActionKeyMapping > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActionName` | `FName` | - |
| `OutMappings` | `TArray < FInputActionKeyMapping > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveActionMapping`

```text
RemoveActionMapping(KeyMapping: FInputActionKeyMapping &, bForceRebuildKeymaps: bool) -> void
```

Programmatically remove an action mapping to the project defaults

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyMapping` | `FInputActionKeyMapping &` | - |
| `bForceRebuildKeymaps` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddAxisMapping`

```text
AddAxisMapping(KeyMapping: FInputAxisKeyMapping &, bForceRebuildKeymaps: bool) -> void
```

Programmatically add an axis mapping to the project defaults

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyMapping` | `FInputAxisKeyMapping &` | - |
| `bForceRebuildKeymaps` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAxisMappingByName`

```text
GetAxisMappingByName(InAxisName: FName, OutMappings: TArray < FInputAxisKeyMapping > &) -> void
```

Retrieve all axis mappings by a certain name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAxisName` | `FName` | - |
| `OutMappings` | `TArray < FInputAxisKeyMapping > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveAxisMapping`

```text
RemoveAxisMapping(KeyMapping: FInputAxisKeyMapping &, bForceRebuildKeymaps: bool) -> void
```

Programmatically remove an axis mapping to the project defaults

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyMapping` | `FInputAxisKeyMapping &` | - |
| `bForceRebuildKeymaps` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SaveKeyMappings`

```text
SaveKeyMappings() -> void
```

Flush the current mapping values to the config file

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetActionNames`

```text
GetActionNames(ActionNames: TArray < FName > &) -> void
```

Populate a list of all defined action names

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActionNames` | `TArray < FName > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAxisNames`

```text
GetAxisNames(AxisNames: TArray < FName > &) -> void
```

Populate a list of all defined axis names

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AxisNames` | `TArray < FName > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ForceRebuildKeymaps`

```text
ForceRebuildKeymaps() -> void
```

When changes are made to the default mappings, push those changes out to PlayerInput key maps

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplySettings`

```text
ApplySettings() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetToDefaultEditorSettings`

```text
ResetToDefaultEditorSettings() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SaveToConfig`

```text
SaveToConfig() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetActionMappings`

```text
GetActionMappings() -> TArray < struct FInputActionKeyMapping >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < struct FInputActionKeyMapping >` | - |

### `GetAxisMappings`

```text
GetAxisMappings() -> TArray < struct FInputAxisKeyMapping >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < struct FInputAxisKeyMapping >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInputTouchDelegateBinding.json -->

# UInputTouchDelegateBinding

## Inheritance

`UInputDelegateBinding`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputTouchDelegateBindings` | `TArray < FBlueprintInputTouchDelegateBinding >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInstancedStaticMeshComponent.json -->

# UInstancedStaticMeshComponent

A component that efficiently renders multiple instances of the same StaticMesh.

## Inheritance

`UStaticMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PerInstanceSMData` | `TArray < FInstancedStaticMeshInstanceData >` | Array of instances, bulk serialized. |
| `InstancingRandomSeed` | `int32` | Value used to seed the random number stream that generates random numbers for each of this mesh's instances.<br>		this is set to zero (default), it will be populated automatically by the editor. |
| `InstanceStartCullDistance` | `int32` | Distance from camera at which each instance begins to fade out. |
| `InstanceEndCullDistance` | `int32` | Distance from camera at which each instance completely fades out. |
| `InstanceNearCullDistance` | `int32` | Distance from camera at which each instance. |
| `bIsFlyType` | `bool` | - |
| `bIsFoliage` | `bool` | - |
| `bIsPCFoliage` | `bool` | - |
| `InstanceReorderTable` | `TArray < int32 >` | Mapping from PerInstanceSMData order to instance render buffer order. If empty, the PerInstanceSMData order is used. |
| `RemovedInstances` | `TArray < int32 >` | - |
| `InstanceVisibilityMapping` | `TMap < int32 , FInstanceVisibilityData >` | - |
| `UseDynamicInstanceBuffer` | `bool` | Set to true to permit updating the vertex buffer used in the instance buffer without recreating it completely. This should be used if you plan on dynamically changing the instances at run-time. |
| `KeepInstanceBufferCPUAccess` | `bool` | Set to true to keep instance buffer accessible by the CPU, otherwise it's discarded and considered never changing, only GPU has a copy of the data. |
| `DynamicInstancingParametersValue` | `TArray < FVector4 >` | - |
| `PerInstanceDynamicInstancingParameterCount` | `int32` | PerInstanceDynamicInstancingParameterCount |
| `PhysicsSerializer` | `UPhysicsSerializer *` | Serialization of all the InstanceBodies. Helps speed up physics creation time. |
| `StashInstanceTransform` | `TMap < int32 , FMatrix >` | - |
| `NumPendingLightmaps` | `int32` | Number of pending lightmaps still to be calculated (Apply()'d). |
| `CachedMappings` | `TArray < FInstancedStaticMeshMappingInfo >` | The mappings for all the instances of this component. |

## Functions

### `AddInstance`

```text
AddInstance(InstanceTransform: FTransform &) -> int32
```

Add an instance to this component. Transform is given in local space of this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceTransform` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `AddInstanceWorldSpace`

```text
AddInstanceWorldSpace(WorldTransform: FTransform &) -> int32
```

Add an instance to this component. Transform is given in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldTransform` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetInstanceTransform`

```text
GetInstanceTransform(InstanceIndex: int32, OutInstanceTransform: FTransform &, bWorldSpace: bool) -> bool
```

Get the transform for the instance specified. Instance is returned in local space of this component unless bWorldSpace is set.  Returns True on success.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | - |
| `OutInstanceTransform` | `FTransform &` | - |
| `bWorldSpace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `UpdateInstanceTransform`

```text
UpdateInstanceTransform(InstanceIndex: int32, NewInstanceTransform: FTransform &, bWorldSpace: bool, bMarkRenderStateDirty: bool, bTeleport: bool) -> bool
```

Update the transform for the instance specified.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | The index of the instance to update |
| `NewInstanceTransform` | `FTransform &` | The new transform |
| `bWorldSpace` | `bool` | If true, the new transform interpreted as a World Space transform, otherwise it is interpreted as Local Space |
| `bMarkRenderStateDirty` | `bool` | If true, the change should be visible immediately. If you are updating many instances you should only set this to true for the last instance. |
| `bTeleport` | `bool` | Whether or not the instance's physics should be moved normally, or teleported (moved instantly, ignoring velocity). |

**Returns**

| Type | Description |
|---|---|
| `bool` | True on success. |

### `RemoveInstance`

```text
RemoveInstance(InstanceIndex: int32) -> bool
```

Remove the instance specified. Returns True on success. Note that this will leave the array in order, but may shrink it.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ClearInstances`

```text
ClearInstances() -> void
```

Clear all instances being rendered by this component.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetInstanceCount`

```text
GetInstanceCount() -> int32
```

Get the number of instances in this component.

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetCullDistances`

```text
SetCullDistances(StartCullDistance: int32, EndCullDistance: int32) -> void
```

Sets the fading start and culling end distances for this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartCullDistance` | `int32` | - |
| `EndCullDistance` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNearCullDistance`

```text
SetNearCullDistance(CullDistance: int32) -> void
```

Sets the cull near distance for this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CullDistance` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetInstancesOverlappingSphere`

```text
GetInstancesOverlappingSphere(Center: FVector &, Radius: float, bSphereInWorldSpace: bool) -> TArray < int32 >
```

Returns the instances with instance bounds overlapping the specified sphere. The return value is an array of instance indices.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Center` | `FVector &` | - |
| `Radius` | `float` | - |
| `bSphereInWorldSpace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `TArray < int32 >` | - |

### `GetInstancesOverlappingBox`

```text
GetInstancesOverlappingBox(Box: FBox &, bBoxInWorldSpace: bool) -> TArray < int32 >
```

Returns the instances with instance bounds overlapping the specified box. The return value is an array of instance indices.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Box` | `FBox &` | - |
| `bBoxInWorldSpace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `TArray < int32 >` | - |

### `HideInstance`

```text
HideInstance(InstanceIndices: TArray < int32 > &) -> bool
```

Update the transform for the instance specified.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndices` | `TArray < int32 > &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True on success. |

### `ShowInstance`

```text
ShowInstance(InstanceIndices: TArray < int32 > &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndices` | `TArray < int32 > &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInt32Binding.json -->

# UInt32Binding

## Inheritance

`UPropertyBinding`

## Functions

### `GetValue`

```text
GetValue() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpCurveEdSetup.json -->

# UInterpCurveEdSetup

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Tabs` | `TArray < struct FCurveEdTab >` | - |
| `ActiveTab` | `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpData.json -->

# UInterpData

Interpolation data, containing keyframe tracks, event tracks etc.
  This does not contain any  AActor  references or state, so can safely be stored in
  packages, shared between multiple MatineeActors etc.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InterpLength` | `float` | Duration of interpolation sequence - in seconds. |
| `PathBuildTime` | `float` | Position in Interp to move things to for path-building in editor. |
| `InterpGroups` | `TArray < UInterpGroup * >` | Actual interpolation data. Groups of InterpTracks. |
| `CurveEdSetup` | `UInterpCurveEdSetup *` | Used for curve editor to remember curve-editing setup. Only loaded in editor. |
| `EdSectionStart` | `float` | Used in editor for defining sections to loop, stretch etc. |
| `EdSectionEnd` | `float` | Used in editor for defining sections to loop, stretch etc. |
| `bShouldBakeAndPrune` | `uint32` | If true, then the matinee should be baked and pruned at cook time. |
| `CachedDirectorGroup` | `UInterpGroupDirector *` | Cached version of the director group, if any, for easy access while in game |
| `AllEventNames` | `TArray < FName >` | Unique names of all events contained across all event tracks |
| `InterpFilters` | `TArray < UInterpFilter * >` | Used for filtering which tracks are currently visible. |
| `SelectedFilter` | `UInterpFilter *` | The currently selected filter. |
| `DefaultFilters` | `TArray < UInterpFilter * >` | Array of default filters. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpFilter.json -->

# UInterpFilter

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Caption` | `FString` | Caption for this filter. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpFilter_Classes.json -->

# UInterpFilter_Classes

## Inheritance

`UInterpFilter`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ClassToFilterBy` | `TSubclassOf < UObject >` | Which class to filter groups by. |
| `TrackClasses` | `TArray < TSubclassOf < UObject > >` | List of allowed track classes.  If empty, then all track classes will be included.  Only groups that<br>		contain at least one of these types of tracks will be displayed. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpFilter_Custom.json -->

# UInterpFilter_Custom

## Inheritance

`UInterpFilter`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GroupsToInclude` | `TArray < UInterpGroup * >` | Which groups are included in this filter. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpGroup.json -->

# UInterpGroup

## Inheritance

`UObject` -> `FInterpEdInputInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InterpTracks` | `TArray < UInterpTrack * >` | - |
| `GroupName` | `FName` | Within an InterpData, all GroupNames must be unique. <br>	 	Used for naming Variable connectors on the Action in Kismet and finding each groups object. |
| `GroupColor` | `FColor` | Colour used for drawing tracks etc. related to this group. |
| `bCollapsed` | `uint32` | Whether or not this group is folded away in the editor. |
| `bVisible` | `uint32` | Whether or not this group is visible in the editor. |
| `bIsFolder` | `uint32` | When enabled, this group is treated like a folder in the editor, which should only be used for organization.  Folders are never associated with actors and don't have a presence in the Kismet graph. |
| `bIsParented` | `uint32` | When true, this group is considered a 'visual child' of another group.  This doesn't at all affect the behavior of the group, it's only for visual organization.  Also, it's implied that the parent is the next prior group in the array that doesn't have a parent. |
| `bIsSelected` | `uint32` | When enabled, this group will be selected in the interp editor. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpGroupCamera.json -->

# UInterpGroupCamera

## Inheritance

`UInterpGroup`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CameraAnimInst` | `UCameraAnim *` | - |
| `CompressTolerance` | `float` | When compress, tolerance option |
| `Target` | `FCameraPreviewInfo` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpGroupInst.json -->

# UInterpGroupInst

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Group` | `UInterpGroup *` | An instance of an UInterpGroup for a particular Actor. There may be multiple InterpGroupInsts for a single<br>	  UInterpGroup in the InterpData, if multiple Actors are connected to the same UInterpGroup. <br>	  The Outer of an UInterpGroupInst is a MatineeActor<br>	 <br>	 UInterpGroup within the InterpData that this is an instance of. |
| `GroupActor` | `AActor *` | Actor that this Group instance is acting upon.<br>	 	NB: that this may be set to NULL at any time as a result of the  AActor  being destroyed. |
| `TrackInst` | `TArray < UInterpTrackInst * >` | Array if InterpTrack instances. TrackInst.Num() == UInterpGroup.InterpTrack.Num() must be true. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpToMovementComponent.json -->

# UInterpToMovementComponent

Move the root component between a series of points over a given time  
 
  @see UMovementComponent

## Inheritance

`UMovementComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Duration` | `float` | How long to take to move from the first point to the last (or vice versa) |
| `bPauseOnImpact` | `uint32` | If true, will pause movement on impact. If false it will behave as if the end of the movement range was reached based on the BehaviourType. |
| `BehaviourType` | `EInterpToBehaviourType` | Movement behaviour of the component |
| `bForceSubStepping` | `uint32` | If true, forces sub-stepping to break up movement into discrete smaller steps to improve accuracy of the trajectory.<br>	  Objects that move in a straight line typically do not need to set this, as movement always uses continuous collision detection (sweeps) so collision is not missed.<br>	  Sub-stepping is automatically enabled when under the effects of gravity or when homing towards a target.<br>	  @see MaxSimulationTimeStep, MaxSimulationIterations |
| `MaxSimulationTimeStep` | `float` | Max time delta for each discrete simulation step.<br>	  Lowering this value can address issues with fast-moving objects or complex collision scenarios, at the cost of performance.<br>	 <br>	  WARNING: if (MaxSimulationTimeStep  MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.<br>	  @see MaxSimulationIterations, bForceSubStepping |
| `MaxSimulationIterations` | `int32` | Max number of iterations used for each discrete simulation step.<br>	  Increasing this value can address issues with fast-moving objects or complex collision scenarios, at the cost of performance.<br>	 <br>	  WARNING: if (MaxSimulationTimeStep  MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.<br>	  @see MaxSimulationTimeStep, bForceSubStepping |
| `ControlPoints` | `TArray < FInterpControlPoint >` | List of control points to visit. |

## Functions

### `StopSimulating`

```text
StopSimulating(HitResult: FHitResult &) -> void
```

Clears the reference to UpdatedComponent, fires stop event, and stops ticking.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HitResult` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestartMovement`

```text
RestartMovement(InitialDirection: float) -> void
```

Reset to start. Sets time to zero and direction to 1.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InitialDirection` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FinaliseControlPoints`

```text
FinaliseControlPoints() -> void
```

Initialise the control points array. Call after adding control points if they are add after begin play .

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnInterpToReverse`

```text
OnInterpToReverse(ImpactResult: const FHitResult&, Time: float) -> void
```

Called when InterpTo impacts something and reverse is enabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `const FHitResult&` | - |
| `Time` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInterpToStop`

```text
OnInterpToStop(ImpactResult: const FHitResult&, Time: float) -> void
```

Called when InterpTo has come to a stop.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `const FHitResult&` | - |
| `Time` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWaitBeginDelegate`

```text
OnWaitBeginDelegate(ImpactResult: const FHitResult&, Time: float) -> void
```

Called when InterpTo has come to a stop but will resume when possible.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `const FHitResult&` | - |
| `Time` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWaitEndDelegate`

```text
OnWaitEndDelegate(ImpactResult: const FHitResult&, Time: float) -> void
```

Called when InterpTo has resumed following a stop.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `const FHitResult&` | - |
| `Time` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnResetDelegate`

```text
OnResetDelegate(ImpactResult: const FHitResult&, Time: float) -> void
```

Called when InterpTo reached the end and reset back to start .

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `const FHitResult&` | - |
| `Time` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrack.json -->

# UInterpTrack

## Inheritance

`UObject` -> `FCurveEdInterface` -> `FInterpEdInputInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SubTracks` | `TArray < UInterpTrack * >` | A list of subtracks that belong to this track |
| `TrackInstClass` | `TSubclassOf < UInterpTrackInst >` | - |
| `ActiveCondition` | `TEnumAsByte < enum ETrackActiveCondition >` | Sets the condition that must be met for this track to be enabled |
| `TrackTitle` | `FString` | Title of track type. |
| `bOnePerGroup` | `uint32` | Whether there may only be one of this track in an UInterpGroup. |
| `bDirGroupOnly` | `uint32` | If this track can only exist inside the Director group. |
| `bDisableTrack` | `uint32` | Whether or not this track should actually update the target actor. |
| `bIsSelected` | `uint32` | Whether or not this track is selected in the editor. |
| `bIsAnimControlTrack` | `uint32` | If true, the  AActor  this track is working on will have BeginAnimControlFinishAnimControl called on it. |
| `bSubTrackOnly` | `uint32` | If this track can only exist as a sub track. |
| `bVisible` | `uint32` | Whether or not this track is visible in the editor. |
| `bIsRecording` | `uint32` | Whether or not this track is recording in the editor. |
| `SubTrackGroups` | `TArray < struct FSubTrackGroup >` | A list of subtrack groups (for editor UI organization only) |
| `SupportedSubTracks` | `TArray < struct FSupportedSubTrackInfo >` | A list of supported tracks that can be a subtrack of this track. |
| `TrackIcon` | `UTexture2D *` | - |
| `bIsCollapsed` | `uint32` | If this track is collapsed. (Only applies  to tracks with subtracks). |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackAnimControl.json -->

# UInterpTrackAnimControl

## Inheritance

`UInterpTrackFloatBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SlotName` | `FName` | Name of slot to use when playing animation. Passed to Actor. <br>	 	When multiple tracks use the same slot name, they are each given a different ChannelIndex when SetAnimPosition is called. |
| `AnimSeqs` | `TArray < struct FAnimControlTrackKey >` | Track of different animations to play and when to start playing them. |
| `bSkipAnimNotifiers` | `uint32` | Skip all anim notifiers |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackBoolProp.json -->

# UInterpTrackBoolProp

## Inheritance

`UInterpTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoolTrack` | `TArray < struct FBoolTrackKey >` | Array of booleans to set. |
| `PropertyName` | `FName` | Name of property in Group  AActor  which this track will modify over time. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackColorProp.json -->

# UInterpTrackColorProp

## Inheritance

`UInterpTrackVectorBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PropertyName` | `FName` | Name of property in Group  AActor  which this track mill modify over time. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackDirector.json -->

# UInterpTrackDirector

## Inheritance

`UInterpTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CutTrack` | `TArray < struct FDirectorTrackCut >` | Array of cuts between cameras. |
| `bSimulateCameraCutsOnClients` | `uint32` | True to allow clients to simulate their own camera cuts.  Can help with latency-induced timing issues. |
| `PreviewCamera` | `ACameraActor *` | The camera actor which the track is currently focused on. Only valid if this track or it's group is selected |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackEvent.json -->

# UInterpTrackEvent

## Inheritance

`UInterpTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EventTrack` | `TArray < struct FEventTrackKey >` | Array of events to fire off. |
| `bFireEventsWhenForwards` | `uint32` | If events should be fired when passed playing the sequence forwards. |
| `bFireEventsWhenBackwards` | `uint32` | If events should be fired when passed playing the sequence backwards. |
| `bFireEventsWhenJumpingForwards` | `uint32` | If true, events on this track are fired even when jumping forwads through a sequence - for example, skipping a cinematic. |
| `bUseCustomEventName` | `uint32` | If checked each key's event name is the exact name of the custom event function in level script that will be called |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackFade.json -->

# UInterpTrackFade

## Inheritance

`UInterpTrackFloatBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bPersistFade` | `uint32` | InterpTrackFade<br>	 <br>	  Special float property track that controls camera fading over time.<br>	  Should live in a Director group. |
| `bFadeAudio` | `uint32` | True to set master audio volume along with the visual fade. |
| `FadeColor` | `FLinearColor` | Color to fade to. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackFloatAnimBPParam.json -->

# UInterpTrackFloatAnimBPParam

## Inheritance

`UInterpTrackFloatBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AnimBlueprintClass` | `UAnimBlueprintGeneratedClass *` | - |
| `AnimClass` | `TSubclassOf < UAnimInstance >` | Materials whose parameters we want to change and the references to those materials. |
| `ParamName` | `FName` | Name of parameter in the MaterialInstance which this track will modify over time. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackFloatBase.json -->

# UInterpTrackFloatBase

## Inheritance

`UInterpTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FloatTrack` | `FInterpCurveFloat` | Actually track data containing keyframes of float as it varies over time. |
| `CurveTension` | `float` | Tension of curve, used for keypoints using automatic tangents. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackFloatMaterialParam.json -->

# UInterpTrackFloatMaterialParam

## Inheritance

`UInterpTrackFloatBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetMaterials` | `TArray < UMaterialInterface * >` | Materials whose parameters we want to change and the references to those materials. |
| `ParamName` | `FName` | Name of parameter in the MaterialInstance which this track will modify over time. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackFloatParticleParam.json -->

# UInterpTrackFloatParticleParam

## Inheritance

`UInterpTrackFloatBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParamName` | `FName` | Name of property in the Emitter which this track mill modify over time. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackFloatProp.json -->

# UInterpTrackFloatProp

## Inheritance

`UInterpTrackFloatBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PropertyName` | `FName` | Name of property in Group  AActor  which this track mill modify over time. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstAnimControl.json -->

# UInterpTrackInstAnimControl

## Inheritance

`UInterpTrackInst`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LastUpdatePosition` | `float` | - |
| `InitPosition` | `FVector` | - |
| `InitRotation` | `FRotator` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstBoolProp.json -->

# UInterpTrackInstBoolProp

## Inheritance

`UInterpTrackInstProperty`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoolProperty` | `UBoolProperty *` | Mask that indicates which bit the boolean property actually uses of the value pointed to by BoolProp. |
| `ResetBool` | `bool` | Saved value for restoring state when exiting Matinee. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstColorProp.json -->

# UInterpTrackInstColorProp

## Inheritance

`UInterpTrackInstProperty`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ResetColor` | `FColor` | Saved value for restoring state when exiting Matinee. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstDirector.json -->

# UInterpTrackInstDirector

## Inheritance

`UInterpTrackInst`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OldViewTarget` | `AActor *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstEvent.json -->

# UInterpTrackInstEvent

## Inheritance

`UInterpTrackInst`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LastUpdatePosition` | `float` | Position we were in last time we evaluated Events. <br>	 	During UpdateTrack, events between this time and the current time will be fired. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstFloatAnimBPParam.json -->

# UInterpTrackInstFloatAnimBPParam

## Inheritance

`UInterpTrackInst`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AnimScriptInstance` | `UAnimInstance *` | MIDs we're using to set the desired parameter. |
| `ResetFloat` | `float` | Saved values for restoring state when exiting Matinee. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstFloatMaterialParam.json -->

# UInterpTrackInstFloatMaterialParam

## Inheritance

`UInterpTrackInst`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaterialInstances` | `TArray < UMaterialInstanceDynamic * >` | MIDs we're using to set the desired parameter. |
| `ResetFloats` | `TArray < float >` | Saved values for restoring state when exiting Matinee. |
| `PrimitiveMaterialRefs` | `TArray < struct FPrimitiveMaterialRef >` | Primitive components on which materials have been overridden. |
| `InstancedTrack` | `UInterpTrackFloatMaterialParam *` | track we are an instance of - used in the editor to propagate changes to the track's Materials array immediately |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstFloatParticleParam.json -->

# UInterpTrackInstFloatParticleParam

## Inheritance

`UInterpTrackInst`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ResetFloat` | `float` | Saved value for restoring state when exiting Matinee. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstFloatProp.json -->

# UInterpTrackInstFloatProp

## Inheritance

`UInterpTrackInstProperty`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ResetFloat` | `float` | Saved value for restoring state when exiting Matinee. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstLinearColorProp.json -->

# UInterpTrackInstLinearColorProp

## Inheritance

`UInterpTrackInstProperty`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ResetColor` | `FLinearColor` | Saved value for restoring state when exiting Matinee. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstMove.json -->

# UInterpTrackInstMove

## Inheritance

`UInterpTrackInst`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ResetLocation` | `FVector` | Saved position. Used in editor for resetting when quitting Matinee. |
| `ResetRotation` | `FRotator` | Saved rotation. Used in editor for resetting when quitting Matinee. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstParticleReplay.json -->

# UInterpTrackInstParticleReplay

## Inheritance

`UInterpTrackInst`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LastUpdatePosition` | `float` | Position we were in last time we evaluated.<br>	 	During UpdateTrack, events between this time and the current time will be processed. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstProperty.json -->

# UInterpTrackInstProperty

## Inheritance

`UInterpTrackInst`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InterpProperty` | `UProperty *` | Function to call after updating the value of the color property. |
| `PropertyOuterObjectInst` | `UObject *` | Pointer to the UObject instance that is the outer of the color property we are interpolating on, this is used to process the property update callback. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstSlomo.json -->

# UInterpTrackInstSlomo

## Inheritance

`UInterpTrackInst`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OldTimeDilation` | `float` | Backup of initial LevelInfo MatineeTimeDilation setting when interpolation started. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstSound.json -->

# UInterpTrackInstSound

## Inheritance

`UInterpTrackInst`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LastUpdatePosition` | `float` | - |
| `PlayAudioComp` | `UAudioComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstToggle.json -->

# UInterpTrackInstToggle

## Inheritance

`UInterpTrackInst`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Action` | `TEnumAsByte < enum ETrackToggleAction >` | - |
| `LastUpdatePosition` | `float` | Position we were in last time we evaluated.<br>	 	During UpdateTrack, toggles between this time and the current time will be processed. |
| `bSavedActiveState` | `uint32` | Cached 'active' state for the toggleable actor before we possessed it; restored when Matinee exits |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstVectorMaterialParam.json -->

# UInterpTrackInstVectorMaterialParam

## Inheritance

`UInterpTrackInst`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaterialInstances` | `TArray < UMaterialInstanceDynamic * >` | MIDs we're using to set the desired parameter. |
| `ResetVectors` | `TArray < FVector >` | Saved values for restoring state when exiting Matinee. |
| `PrimitiveMaterialRefs` | `TArray < struct FPrimitiveMaterialRef >` | Primitive components on which materials have been overridden. |
| `InstancedTrack` | `UInterpTrackVectorMaterialParam *` | Track we are an instance of - used in the editor to propagate changes to the track's Materials array immediately. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstVectorProp.json -->

# UInterpTrackInstVectorProp

## Inheritance

`UInterpTrackInstProperty`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ResetVector` | `FVector` | Saved value for restoring state when exiting Matinee. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstVisibility.json -->

# UInterpTrackInstVisibility

## Inheritance

`UInterpTrackInst`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Action` | `TEnumAsByte < enum EVisibilityTrackAction >` | - |
| `LastUpdatePosition` | `float` | Position we were in last time we evaluated.<br>	 	During UpdateTrack, events between this time and the current time will be processed. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackLinearColorBase.json -->

# UInterpTrackLinearColorBase

## Inheritance

`UInterpTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LinearColorTrack` | `FInterpCurveLinearColor` | Actually track data containing keyframes of a FVector as it varies over time. |
| `CurveTension` | `float` | Tension of curve, used for keypoints using automatic tangents. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackLinearColorProp.json -->

# UInterpTrackLinearColorProp

## Inheritance

`UInterpTrackLinearColorBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PropertyName` | `FName` | Name of property in Group  AActor  which this track mill modify over time. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackMove.json -->

# UInterpTrackMove

Track containing data for moving an actor around over time.

## Inheritance

`UInterpTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PosTrack` | `FInterpCurveVector` | Actual position keyframe data. |
| `EulerTrack` | `FInterpCurveVector` | Actual rotation keyframe data, stored as Euler angles in degrees, for easy editing on curve. |
| `LookupTrack` | `FInterpLookupTrack` | - |
| `LookAtGroupName` | `FName` | When using IMR_LookAtGroup, specifies the Group which this track should always point its actor at. |
| `LinCurveTension` | `float` | Controls the tightness of the curve for the translation path. |
| `AngCurveTension` | `float` | Controls the tightness of the curve for the rotation path. |
| `bUseQuatInterpolation` | `uint32` | Use a Quaternion linear interpolation between keys.<br>	 	This is robust and will find the 'shortest' distance between keys, but does not support ease inout. |
| `bShowArrowAtKeys` | `uint32` | In the editor, show a small arrow at each keyframe indicating the rotation at that key. |
| `bDisableMovement` | `uint32` | Disable previewing of this track - will always position  AActor  at Time=0.0. Useful when keyframing an object relative to this group. |
| `bShowTranslationOnCurveEd` | `uint32` | If false, when this track is displayed on the Curve Editor in Matinee, do not show the Translation tracks. |
| `bShowRotationOnCurveEd` | `uint32` | If false, when this track is displayed on the Curve Editor in Matinee, do not show the Rotation tracks. |
| `bHide3DTrack` | `uint32` | If true, 3D representation of this track in the 3D viewport is disabled. |
| `RotMode` | `TEnumAsByte < enum EInterpTrackMoveRotMode >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackMoveAxis.json -->

# UInterpTrackMoveAxis

## Inheritance

`UInterpTrackFloatBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MoveAxis` | `TEnumAsByte < enum EInterpMoveAxis >` | The axis which this track will use when transforming an actor |
| `LookupTrack` | `FInterpLookupTrack` | Lookup track to use when looking at different groups for transform information |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackParticleReplay.json -->

# UInterpTrackParticleReplay

## Inheritance

`UInterpTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TrackKeys` | `TArray < struct FParticleReplayTrackKey >` | Array of keys |
| `bIsCapturingReplay` | `uint32` | True in the editor if track should be used to capture replay frames instead of play them back |
| `FixedTimeStep` | `float` | Current replay fixed time quantum between frames (one over frame rate) |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackSound.json -->

# UInterpTrackSound

## Inheritance

`UInterpTrackVectorBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sounds` | `TArray < struct FSoundTrackKey >` | Array of sounds to play at specific times. |
| `bPlayOnReverse` | `uint32` | if set, sound plays only when playing the matinee in reverse instead of when the matinee plays forward |
| `bContinueSoundOnMatineeEnd` | `uint32` | If true, sounds on this track will not be forced to finish when the matinee sequence finishes. |
| `bSuppressSubtitles` | `uint32` | If true, don't show subtitles for sounds played by this track. |
| `bTreatAsDialogue` | `uint32` | If true and track is controlling a pawn, makes the pawn "speak" the given audio. |
| `bAttach` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackToggle.json -->

# UInterpTrackToggle

## Inheritance

`UInterpTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ToggleTrack` | `TArray < struct FToggleTrackKey >` | Array of events to fire off. |
| `bActivateSystemEachUpdate` | `uint32` | If true, the track will call ActivateSystem on the emitter each update (the old 'incorrect' behavior).<br>	 	If false (the default), the System will only be activated if it was previously inactive. |
| `bActivateWithJustAttachedFlag` | `uint32` | If true, the track will activate the system w the 'Just Attached' flag. |
| `bFireEventsWhenForwards` | `uint32` | If events should be fired when passed playing the sequence forwards. |
| `bFireEventsWhenBackwards` | `uint32` | If events should be fired when passed playing the sequence backwards. |
| `bFireEventsWhenJumpingForwards` | `uint32` | If true, events on this track are fired even when jumping forwads through a sequence - for example, skipping a cinematic. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackVectorBase.json -->

# UInterpTrackVectorBase

## Inheritance

`UInterpTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VectorTrack` | `FInterpCurveVector` | Actually track data containing keyframes of a FVector as it varies over time. |
| `CurveTension` | `float` | Tension of curve, used for keypoints using automatic tangents. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackVectorMaterialParam.json -->

# UInterpTrackVectorMaterialParam

## Inheritance

`UInterpTrackVectorBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetMaterials` | `TArray < UMaterialInterface * >` | Materials whose parameters we want to change and the references to those materials. |
| `ParamName` | `FName` | Name of parameter in the MaterialInstance which this track will modify over time. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackVectorProp.json -->

# UInterpTrackVectorProp

## Inheritance

`UInterpTrackVectorBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PropertyName` | `FName` | Name of property in Group  AActor  which this track mill modify over time. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackVisibility.json -->

# UInterpTrackVisibility

## Inheritance

`UInterpTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VisibilityTrack` | `TArray < struct FVisibilityTrackKey >` | Array of events to fire off. |
| `bFireEventsWhenForwards` | `uint32` | If events should be fired when passed playing the sequence forwards. |
| `bFireEventsWhenBackwards` | `uint32` | If events should be fired when passed playing the sequence backwards. |
| `bFireEventsWhenJumpingForwards` | `uint32` | If true, events on this track are fired even when jumping forwads through a sequence - for example, skipping a cinematic. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UIntSerialization.json -->

# UIntSerialization

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UnsignedInt16Variable` | `uint16` | - |
| `UnsignedInt32Variable` | `uint32` | - |
| `UnsignedInt64Variable` | `uint64` | - |
| `SignedInt8Variable` | `int8` | - |
| `SignedInt16Variable` | `int16` | - |
| `SignedInt64Variable` | `int64` | - |
| `UnsignedInt8Variable` | `uint8` | - |
| `SignedInt32Variable` | `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UInvalidationBox.json -->

# UInvalidationBox

Invalidate
   Single Child
   Caching  Performance

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bCanCache` | `bool` | Should the invalidation panel cache the widgets?  Making this false makes it so the invalidation<br>	  panel stops acting like an invalidation panel, just becomes a simple container widget. |
| `CacheRelativeTransforms` | `bool` | Caches the locations for child draw elements relative to the invalidation box,<br>	  this adds extra overhead to drawing them every frame.  However, in cases where<br>	  the position of the invalidation boxes changes every frame this can be a big savings. |

## Functions

### `InvalidateCache`

```text
InvalidateCache() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCanCache`

```text
GetCanCache() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetCanCache`

```text
SetCanCache(CanCache: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CanCache` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UKismetAnimationLibrary.json -->

# UKismetAnimationLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `K2_TwoBoneIK`

```text
K2_TwoBoneIK(RootPos: FVector &, JointPos: FVector &, EndPos: FVector &, JointTarget: FVector &, Effector: FVector &, OutJointPos: FVector &, OutEndPos: FVector &, bAllowStretching: bool, StartStretchRatio: float, MaxStretchScale: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RootPos` | `FVector &` | - |
| `JointPos` | `FVector &` | - |
| `EndPos` | `FVector &` | - |
| `JointTarget` | `FVector &` | - |
| `Effector` | `FVector &` | - |
| `OutJointPos` | `FVector &` | - |
| `OutEndPos` | `FVector &` | - |
| `bAllowStretching` | `bool` | - |
| `StartStretchRatio` | `float` | - |
| `MaxStretchScale` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_LookAt`

```text
K2_LookAt(CurrentTransform: FTransform &, TargetPosition: FVector &, LookAtVector: FVector, bUseUpVector: bool, UpVector: FVector, ClampConeInDegree: float) -> FTransform
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CurrentTransform` | `FTransform &` | - |
| `TargetPosition` | `FVector &` | - |
| `LookAtVector` | `FVector` | - |
| `bUseUpVector` | `bool` | - |
| `UpVector` | `FVector` | - |
| `ClampConeInDegree` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UKismetArrayLibrary.json -->

# UKismetArrayLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `Array_Add`

```text
Array_Add(TargetArray: TArray < int32 > &, NewItem: int32 &) -> int32
```

Add item to array

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to add item to |
| `NewItem` | `int32 &` | The item to add to the array |

**Returns**

| Type | Description |
|---|---|
| `int32` | The index of the newly added item |

### `Array_AddUnique`

```text
Array_AddUnique(TargetArray: TArray < int32 > &, NewItem: int32 &) -> int32
```

Add item to array (unique)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to add item to |
| `NewItem` | `int32 &` | The item to add to the array |

**Returns**

| Type | Description |
|---|---|
| `int32` | The index of the newly added item, or INDEX_NONE if the item is already present in the array |

### `Array_Shuffle`

```text
Array_Shuffle(TargetArray: TArray < int32 > &) -> void
```

Shuffle (randomize) the elements of an array

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to shuffle |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Array_Append`

```text
Array_Append(TargetArray: TArray < int32 > &, SourceArray: TArray < int32 > &) -> void
```

Append an array to another array

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to add the source array to |
| `SourceArray` | `TArray < int32 > &` | The array to add to the target array |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Array_Insert`

```text
Array_Insert(TargetArray: TArray < int32 > &, NewItem: int32 &, Index: int32) -> void
```

Insert item at the given index into the array.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to insert into |
| `NewItem` | `int32 &` | The item to insert into the array |
| `Index` | `int32` | The index at which to insert the item into the array |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Array_Remove`

```text
Array_Remove(TargetArray: TArray < int32 > &, IndexToRemove: int32) -> void
```

Remove item at the given index from the array.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to remove from |
| `IndexToRemove` | `int32` | The index into the array to remove from |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Array_RemoveItem`

```text
Array_RemoveItem(TargetArray: TArray < int32 > &, Item: int32 &) -> bool
```

Remove all instances of item from array.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to remove from |
| `Item` | `int32 &` | The item to remove from the array |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if one or more items were removed |

### `Array_Clear`

```text
Array_Clear(TargetArray: TArray < int32 > &) -> void
```

Clear an array, removes all content

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to clear |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Array_Resize`

```text
Array_Resize(TargetArray: TArray < int32 > &, Size: int32) -> void
```

Resize Array to specified size.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to resize |
| `Size` | `int32` | The new size of the array |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Array_Length`

```text
Array_Length(TargetArray: TArray < int32 > &) -> int32
```

Get the number of items in an array

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to get the length of |

**Returns**

| Type | Description |
|---|---|
| `int32` | The length of the array |

### `Array_LastIndex`

```text
Array_LastIndex(TargetArray: TArray < int32 > &) -> int32
```

Get the last valid index into an array

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to perform the operation on |

**Returns**

| Type | Description |
|---|---|
| `int32` | The last valid index of the array |

### `Array_Get`

```text
Array_Get(TargetArray: TArray < int32 > &, Index: int32, Item: int32 &) -> void
```

Given an array and an index, returns a copy of the item found at that index

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to get an item from |
| `Index` | `int32` | The index in the array to get an item from |
| `Item` | `int32 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | A copy of the item stored at the index |

### `Array_Set`

```text
Array_Set(TargetArray: TArray < int32 > &, Index: int32, Item: int32 &, bSizeToFit: bool) -> void
```

Given an array and an index, assigns the item to that array element

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to perform the operation on |
| `Index` | `int32` | The index to assign the item to |
| `Item` | `int32 &` | The item to assign to the index of the array |
| `bSizeToFit` | `bool` | If true, the array will expand if Index is greater than the current size of the array |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Array_Swap`

```text
Array_Swap(TargetArray: TArray < int32 > &, FirstIndex: int32, SecondIndex: int32) -> void
```

Swaps the elements at the specified positions in the specified array
	 If the specified positions are equal, invoking this method leaves the array unchanged

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to perform the operation on |
| `FirstIndex` | `int32` | - |
| `SecondIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Array_Find`

```text
Array_Find(TargetArray: TArray < int32 > &, ItemToFind: int32 &) -> int32
```

Finds the index of the first instance of the item within the array

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to search for the item |
| `ItemToFind` | `int32 &` | The item to look for |

**Returns**

| Type | Description |
|---|---|
| `int32` | The index the item was found at, or -1 if not found |

### `Array_Contains`

```text
Array_Contains(TargetArray: TArray < int32 > &, ItemToFind: int32 &) -> bool
```

Returns true if the array contains the given item

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to search for the item |
| `ItemToFind` | `int32 &` | The item to look for |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the item was found within the array |

### `FilterArray`

```text
FilterArray(TargetArray: TArray < AActor * > &, FilterClass: TSubclassOf < AActor >, FilteredArray: TArray < AActor * > &) -> void
```

Filter an array based on a Class derived from Actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < AActor * > &` | The array to filter from |
| `FilterClass` | `TSubclassOf < AActor >` | The Actor sub-class type that acts as the filter, only objects derived from it will be returned. |
| `FilteredArray` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | An array containing only those objects which are derived from the class specified. |

### `SetArrayPropertyByName`

```text
SetArrayPropertyByName(Object: UObject *, PropertyName: FName, Value: TArray < int32 > &) -> void
```

Not exposed to users. Supports setting an array property on an object by name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `TArray < int32 > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Array_IsValidIndex`

```text
Array_IsValidIndex(TargetArray: TArray < int32 > &, IndexToTest: int32) -> bool
```

Tests if IndexToTest is valid, i.e. greater than or equal to zero, and less than the number of elements in TargetArray.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | Array to use for the IsValidIndex test |
| `IndexToTest` | `int32` | The Index, that we want to test for being valid |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the Index is Valid, i.e. greater than or equal to zero, and less than the number of elements in TargetArray. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UKismetGuidLibrary.json -->

# UKismetGuidLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `EqualEqual_GuidGuid`

```text
EqualEqual_GuidGuid(A: FGuid &, B: FGuid &) -> bool
```

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FGuid &` | - |
| `B` | `FGuid &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_GuidGuid`

```text
NotEqual_GuidGuid(A: FGuid &, B: FGuid &) -> bool
```

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FGuid &` | - |
| `B` | `FGuid &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsValid_Guid`

```text
IsValid_Guid(InGuid: FGuid &) -> bool
```

Checks whether the given GUID is valid

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InGuid` | `FGuid &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Invalidate_Guid`

```text
Invalidate_Guid(InGuid: FGuid &) -> void
```

Invalidates the given GUID

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InGuid` | `FGuid &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `NewGuid`

```text
NewGuid() -> FGuid
```

Returns a new unique GUID

**Returns**

| Type | Description |
|---|---|
| `FGuid` | - |

### `Conv_GuidToString`

```text
Conv_GuidToString(InGuid: FGuid &) -> FString
```

Converts a GUID value to a string, in the form 'A-B-C-D'

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InGuid` | `FGuid &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Parse_StringToGuid`

```text
Parse_StringToGuid(GuidString: FString &, OutGuid: FGuid &, Success: bool &) -> void
```

Converts a String of format EGuidFormats to a Guid. Returns Guid OutGuid, Returns bool Success

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GuidString` | `FString &` | - |
| `OutGuid` | `FGuid &` | - |
| `Success` | `bool &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UKismetInputLibrary.json -->

# UKismetInputLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `CalibrateTilt`

```text
CalibrateTilt() -> void
```

Calibrate the tilt for the input device

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EqualEqual_KeyKey`

```text
EqualEqual_KeyKey(A: FKey, B: FKey) -> bool
```

Test if the input key are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FKey` | - The key to compare against |
| `B` | `FKey` | - The key to compare |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the key are equal, false otherwise |

### `EqualEqual_InputChordInputChord`

```text
EqualEqual_InputChordInputChord(A: FInputChord, B: FInputChord) -> bool
```

Test if the input chords are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FInputChord` | - The chord to compare against |
| `B` | `FInputChord` | - The chord to compare |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the chords are equal, false otherwise |

### `Key_IsModifierKey`

```text
Key_IsModifierKey(Key: FKey &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the key is a modifier key: Ctrl, Command, Alt, Shift |

### `Key_IsGamepadKey`

```text
Key_IsGamepadKey(Key: FKey &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the key is a gamepad button |

### `Key_IsMouseButton`

```text
Key_IsMouseButton(Key: FKey &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the key is a mouse button |

### `Key_IsKeyboardKey`

```text
Key_IsKeyboardKey(Key: FKey &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the key is a keyboard button |

### `Key_IsFloatAxis`

```text
Key_IsFloatAxis(Key: FKey &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the key is a float axis |

### `Key_IsVectorAxis`

```text
Key_IsVectorAxis(Key: FKey &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the key is a vector axis |

### `Key_GetDisplayName`

```text
Key_GetDisplayName(Key: FKey &) -> FText
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | The display name of the key. |

### `InputEvent_IsRepeat`

```text
InputEvent_IsRepeat(Input: FInputEvent &) -> bool
```

Returns whether or not this character is an auto-repeated keystroke

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if this character is a repeat |

### `InputEvent_IsShiftDown`

```text
InputEvent_IsShiftDown(Input: FInputEvent &) -> bool
```

Returns true if either shift key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if shift is pressed |

### `InputEvent_IsLeftShiftDown`

```text
InputEvent_IsLeftShiftDown(Input: FInputEvent &) -> bool
```

Returns true if left shift key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if left shift is pressed. |

### `InputEvent_IsRightShiftDown`

```text
InputEvent_IsRightShiftDown(Input: FInputEvent &) -> bool
```

Returns true if right shift key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if right shift is pressed. |

### `InputEvent_IsControlDown`

```text
InputEvent_IsControlDown(Input: FInputEvent &) -> bool
```

Returns true if either control key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if control is pressed |

### `InputEvent_IsLeftControlDown`

```text
InputEvent_IsLeftControlDown(Input: FInputEvent &) -> bool
```

Returns true if left control key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if left control is pressed |

### `InputEvent_IsRightControlDown`

```text
InputEvent_IsRightControlDown(Input: FInputEvent &) -> bool
```

Returns true if left control key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if left control is pressed |

### `InputEvent_IsAltDown`

```text
InputEvent_IsAltDown(Input: FInputEvent &) -> bool
```

Returns true if either alt key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if alt is pressed |

### `InputEvent_IsLeftAltDown`

```text
InputEvent_IsLeftAltDown(Input: FInputEvent &) -> bool
```

Returns true if left alt key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if left alt is pressed |

### `InputEvent_IsRightAltDown`

```text
InputEvent_IsRightAltDown(Input: FInputEvent &) -> bool
```

Returns true if right alt key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if right alt is pressed |

### `InputEvent_IsCommandDown`

```text
InputEvent_IsCommandDown(Input: FInputEvent &) -> bool
```

Returns true if either command key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if command is pressed |

### `InputEvent_IsLeftCommandDown`

```text
InputEvent_IsLeftCommandDown(Input: FInputEvent &) -> bool
```

Returns true if left command key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if left command is pressed |

### `InputEvent_IsRightCommandDown`

```text
InputEvent_IsRightCommandDown(Input: FInputEvent &) -> bool
```

Returns true if right command key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if right command is pressed |

### `GetKeyByName`

```text
GetKeyByName(KeyName: FName &) -> FKey
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `FKey` | - |

### `GetKey`

```text
GetKey(Input: FKeyEvent &) -> FKey
```

Returns the key for this event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FKeyEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FKey` | Key name |

### `GetUserIndex`

```text
GetUserIndex(Input: FKeyEvent &) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FKeyEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetAnalogValue`

```text
GetAnalogValue(Input: FAnalogInputEvent &) -> float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FAnalogInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `PointerEvent_GetScreenSpacePosition`

```text
PointerEvent_GetScreenSpacePosition(Input: FPointerEvent &) -> FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | The position of the cursor in screen space |

### `PointerEvent_GetLastScreenSpacePosition`

```text
PointerEvent_GetLastScreenSpacePosition(Input: FPointerEvent &) -> FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | The position of the cursor in screen space last time we handled an input event |

### `PointerEvent_GetCursorDelta`

```text
PointerEvent_GetCursorDelta(Input: FPointerEvent &) -> FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | the distance the mouse traveled since the last event was handled. |

### `PointerEvent_IsMouseButtonDown`

```text
PointerEvent_IsMouseButtonDown(Input: FPointerEvent &, MouseButton: FKey) -> bool
```

Mouse buttons that are currently pressed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |
| `MouseButton` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `PointerEvent_GetEffectingButton`

```text
PointerEvent_GetEffectingButton(Input: FPointerEvent &) -> FKey
```

Mouse button that caused this event to be raised (possibly EB_None)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FKey` | - |

### `PointerEvent_GetWheelDelta`

```text
PointerEvent_GetWheelDelta(Input: FPointerEvent &) -> float
```

How much did the mouse wheel turn since the last mouse event

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `PointerEvent_GetUserIndex`

```text
PointerEvent_GetUserIndex(Input: FPointerEvent &) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | The index of the user that caused the event |

### `PointerEvent_GetPointerIndex`

```text
PointerEvent_GetPointerIndex(Input: FPointerEvent &) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | The unique identifier of the pointer (e.g., finger index) |

### `PointerEvent_GetTouchpadIndex`

```text
PointerEvent_GetTouchpadIndex(Input: FPointerEvent &) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | The index of the touch pad that generated this event (for platforms with multiple touch pads per user) |

### `PointerEvent_IsTouchEvent`

```text
PointerEvent_IsTouchEvent(Input: FPointerEvent &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | Is this event a result from a touch (as opposed to a mouse) |

### `PointerEvent_TouchForce`

```text
PointerEvent_TouchForce(Input: FPointerEvent &) -> float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `PointerEvent_GetGestureType`

```text
PointerEvent_GetGestureType(Input: FPointerEvent &) -> ESlateGesture
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `ESlateGesture` | The type of touch gesture |

### `PointerEvent_GetGestureDelta`

```text
PointerEvent_GetGestureDelta(Input: FPointerEvent &) -> FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | The change in gesture value since the last gesture event of the same type. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UKismetInternationalizationLibrary.json -->

# UKismetInternationalizationLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `SetCurrentCulture`

```text
SetCurrentCulture(Culture: FString &, SaveToConfig: bool) -> bool
```

Set the current culture.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Culture` | `FString &` | The culture to set, as an IETF language tag (eg, "zh-Hans-CN"). |
| `SaveToConfig` | `bool` | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the culture was set, false otherwise. |

### `GetCurrentCulture`

```text
GetCurrentCulture() -> FString
```

Get the current culture as an IETF language tag:
	   - A two-letter ISO 639-1 language code (eg, "zh").
	   - An optional four-letter ISO 15924 script code (eg, "Hans").
	   - An optional two-letter ISO 3166-1 country code (eg, "CN").

**Returns**

| Type | Description |
|---|---|
| `FString` | The culture as an IETF language tag (eg, "zh-Hans-CN"). |

### `SetCurrentLanguage`

```text
SetCurrentLanguage(Culture: FString &, SaveToConfig: bool) -> bool
```

Set only the current language (for localization).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Culture` | `FString &` | The language to set, as an IETF language tag (eg, "zh-Hans-CN"). |
| `SaveToConfig` | `bool` | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the language was set, false otherwise. |

### `GetCurrentLanguage`

```text
GetCurrentLanguage() -> FString
```

Get the current language (for localization) as an IETF language tag:
	   - A two-letter ISO 639-1 language code (eg, "zh").
	   - An optional four-letter ISO 15924 script code (eg, "Hans").
	   - An optional two-letter ISO 3166-1 country code (eg, "CN").

**Returns**

| Type | Description |
|---|---|
| `FString` | The language as an IETF language tag (eg, "zh-Hans-CN"). |

### `SetCurrentLocale`

```text
SetCurrentLocale(Culture: FString &, SaveToConfig: bool) -> bool
```

Set only the current locale (for internationalization).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Culture` | `FString &` | The locale to set, as an IETF language tag (eg, "zh-Hans-CN"). |
| `SaveToConfig` | `bool` | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the locale was set, false otherwise. |

### `GetCurrentLocale`

```text
GetCurrentLocale() -> FString
```

Get the current locale (for internationalization) as an IETF language tag:
	   - A two-letter ISO 639-1 language code (eg, "zh").
	   - An optional four-letter ISO 15924 script code (eg, "Hans").
	   - An optional two-letter ISO 3166-1 country code (eg, "CN").

**Returns**

| Type | Description |
|---|---|
| `FString` | The locale as an IETF language tag (eg, "zh-Hans-CN"). |

### `SetCurrentLanguageAndLocale`

```text
SetCurrentLanguageAndLocale(Culture: FString &, SaveToConfig: bool) -> bool
```

Set the current language (for localization) and locale (for internationalization).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Culture` | `FString &` | The language and locale to set, as an IETF language tag (eg, "zh-Hans-CN"). |
| `SaveToConfig` | `bool` | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the language and locale were set, false otherwise. |

### `SetCurrentAssetGroupCulture`

```text
SetCurrentAssetGroupCulture(AssetGroup: FName, Culture: FString &, SaveToConfig: bool) -> bool
```

Set the given asset group category culture from an IETF language tag (eg, "zh-Hans-CN").

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetGroup` | `FName` | The asset group to set the culture for. |
| `Culture` | `FString &` | The culture to set, as an IETF language tag (eg, "zh-Hans-CN"). |
| `SaveToConfig` | `bool` | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the culture was set, false otherwise. |

### `GetCurrentAssetGroupCulture`

```text
GetCurrentAssetGroupCulture(AssetGroup: FName) -> FString
```

Get the given asset group category culture.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetGroup` | `FName` | The asset group to get the culture for. |

**Returns**

| Type | Description |
|---|---|
| `FString` | The culture as an IETF language tag (eg, "zh-Hans-CN"). |

### `ClearCurrentAssetGroupCulture`

```text
ClearCurrentAssetGroupCulture(AssetGroup: FName, SaveToConfig: bool) -> void
```

Clear the given asset group category culture.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetGroup` | `FName` | The asset group to clear the culture for. |
| `SaveToConfig` | `bool` | If true, save the new setting to the users' "GameUserSettings" config so that it persists after a reload. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UKismetMaterialLibrary.json -->

# UKismetMaterialLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `SetScalarParameterValue`

```text
SetScalarParameterValue(WorldContextObject: UObject *, Collection: UMaterialParameterCollection *, ParameterName: FName, ParameterValue: float) -> ENGINE_API void
```

Sets a scalar parameter value on the material collection instance. Logs if ParameterName is invalid.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Collection` | `UMaterialParameterCollection *` | - |
| `ParameterName` | `FName` | - |
| `ParameterValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetVectorParameterValue`

```text
SetVectorParameterValue(WorldContextObject: UObject *, Collection: UMaterialParameterCollection *, ParameterName: FName, ParameterValue: FLinearColor &) -> ENGINE_API void
```

Sets a vector parameter value on the material collection instance. Logs if ParameterName is invalid.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Collection` | `UMaterialParameterCollection *` | - |
| `ParameterName` | `FName` | - |
| `ParameterValue` | `FLinearColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GetScalarParameterValue`

```text
GetScalarParameterValue(WorldContextObject: UObject *, Collection: UMaterialParameterCollection *, ParameterName: FName) -> ENGINE_API float
```

Gets a scalar parameter value from the material collection instance. Logs if ParameterName is invalid.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Collection` | `UMaterialParameterCollection *` | - |
| `ParameterName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API float` | - |

### `GetVectorParameterValue`

```text
GetVectorParameterValue(WorldContextObject: UObject *, Collection: UMaterialParameterCollection *, ParameterName: FName) -> ENGINE_API FLinearColor
```

Gets a vector parameter value from the material collection instance. Logs if ParameterName is invalid.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Collection` | `UMaterialParameterCollection *` | - |
| `ParameterName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FLinearColor` | - |

### `CreateDynamicMaterialInstance`

```text
CreateDynamicMaterialInstance(WorldContextObject: UObject *, Parent: UMaterialInterface *) -> ENGINE_API class UMaterialInstanceDynamic *
```

Creates a Dynamic Material Instance which you can modify during gameplay.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Parent` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API class UMaterialInstanceDynamic *` | - |

## Language

`cpp`

