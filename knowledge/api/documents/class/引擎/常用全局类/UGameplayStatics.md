---
id: "api:class:UGameplayStatics"
title: "UGameplayStatics"
source: "https://developer.gp.qq.com/api/class/detail/%E5%BC%95%E6%93%8E/%E5%B8%B8%E7%94%A8%E5%85%A8%E5%B1%80%E7%B1%BB/UGameplayStatics.json"
category: "API Wiki/class/引擎/常用全局类"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGameplayStatics

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `SpawnObject`

```text
SpawnObject(ObjectClass: TSubclassOf < UObject >, Outer: UObject *) -> UObject *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ObjectClass` | `TSubclassOf < UObject >` | - |
| `Outer` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

### `BeginSpawningActorFromBlueprint`

```text
BeginSpawningActorFromBlueprint(WorldContextObject: UObject *, Blueprint: UBlueprint *, SpawnTransform: FTransform &, bNoCollisionFail: bool) -> AActor *
```

生成指定蓝图类的实例，但不自动执行构造函数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `Blueprint` | `UBlueprint *` | 蓝图类 |
| `SpawnTransform` | `FTransform &` | 生成Actor的Transform |
| `bNoCollisionFail` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | Actor实例 |

### `BeginSpawningActorFromClass`

```text
BeginSpawningActorFromClass(WorldContextObject: UObject *, ActorClass: TSubclassOf < AActor >, SpawnTransform: FTransform &, bNoCollisionFail: bool, Owner: AActor *) -> AActor *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ActorClass` | `TSubclassOf < AActor >` | - |
| `SpawnTransform` | `FTransform &` | - |
| `bNoCollisionFail` | `bool` | - |
| `Owner` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `BeginDeferredActorSpawnFromClass`

```text
BeginDeferredActorSpawnFromClass(WorldContextObject: UObject *, ActorClass: TSubclassOf < AActor >, SpawnTransform: FTransform &, CollisionHandlingOverride: ESpawnActorCollisionHandlingMethod, Owner: AActor *) -> AActor *
```

Spawns an instance of an actor class, but does not automatically run its construction script.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ActorClass` | `TSubclassOf < AActor >` | - |
| `SpawnTransform` | `FTransform &` | - |
| `CollisionHandlingOverride` | `ESpawnActorCollisionHandlingMethod` | - |
| `Owner` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `FinishSpawningActor`

```text
FinishSpawningActor(Actor: AActor *, SpawnTransform: FTransform &) -> AActor *
```

结束生成Actor，执行Actor的构造函数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | Actor实例 |
| `SpawnTransform` | `FTransform &` | 生成Actor的Transform |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | Actor实例 |

### `GetActorArrayAverageLocation`

```text
GetActorArrayAverageLocation(Actors: TArray < AActor * > &) -> FVector
```

Find the average location (centroid) of an array of Actors

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actors` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetActorArrayBounds`

```text
GetActorArrayBounds(Actors: TArray < AActor * > &, bOnlyCollidingComponents: bool, Center: FVector &, BoxExtent: FVector &) -> void
```

Bind the bounds of an array of Actors

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actors` | `TArray < AActor * > &` | - |
| `bOnlyCollidingComponents` | `bool` | - |
| `Center` | `FVector &` | - |
| `BoxExtent` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAllActorsOfClass`

```text
GetAllActorsOfClass(WorldContextObject: UObject *, ActorClass: TSubclassOf < AActor >, OutActors: TArray < AActor * > &) -> void
```

Find all Actors in the world of the specified class.
	 	This is a slow operation, use with caution e.g. do not use every frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ActorClass` | `TSubclassOf < AActor >` | Class of Actor to find. Must be specified or result array will be empty. |
| `OutActors` | `TArray < AActor * > &` | Output array of Actors of the specified class. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetFirstActorOfClass`

```text
GetFirstActorOfClass(WorldContextObject: UObject *, ActorClass: TSubclassOf < AActor >) -> AActor *
```

Find one Actor in the world of the specified class.
		This is a slow operation, use with caution e.g. do not use every frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ActorClass` | `TSubclassOf < AActor >` | Class of Actor to find. Must be specified or result array will be empty. |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `GetAllActorsWithInterface`

```text
GetAllActorsWithInterface(WorldContextObject: UObject *, Interface: TSubclassOf < UInterface >, OutActors: TArray < AActor * > &) -> void
```

Find all Actors in the world with the specified interface.
	 	This is a slow operation, use with caution e.g. do not use every frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Interface` | `TSubclassOf < UInterface >` | Interface to find. Must be specified or result array will be empty. |
| `OutActors` | `TArray < AActor * > &` | Output array of Actors of the specified interface. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAllActorsWithTag`

```text
GetAllActorsWithTag(WorldContextObject: UObject *, Tag: FName, OutActors: TArray < AActor * > &) -> void
```

获取拥有指定Tag的所有Actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `Tag` | `FName` | Tag名称 |
| `OutActors` | `TArray < AActor * > &` | 输出的Actor列表 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetGameInstance`

```text
GetGameInstance(WorldContextObject: UObject *) -> UGameInstance *
```

获取GameInstance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `UGameInstance *` | GameInstance |

### `GetCurrentGameInstance`

```text
GetCurrentGameInstance() -> UGameInstance *
```

**Returns**

| Type | Description |
|---|---|
| `UGameInstance *` | - |

### `GetPlayerController`

```text
GetPlayerController(WorldContextObject: UObject *, PlayerIndex: int32) -> APlayerController *
```

获取PlayerController

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `PlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `APlayerController *` | PlayerController |

### `GetPlayerPawn`

```text
GetPlayerPawn(WorldContextObject: UObject *, PlayerIndex: int32) -> APawn *
```

获取PlayerPawn

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `PlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `APawn *` | PlayerPawn |

### `GetPlayerCharacter`

```text
GetPlayerCharacter(WorldContextObject: UObject *, PlayerIndex: int32) -> ACharacter *
```

获取PlayerCharacter

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `PlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `ACharacter *` | PlayerCharacter |

### `GetPlayerCameraManager`

```text
GetPlayerCameraManager(WorldContextObject: UObject *, PlayerIndex: int32) -> APlayerCameraManager *
```

获取PlayerCameraManager

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `PlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `APlayerCameraManager *` | PlayerCameraManager |

### `CreatePlayer`

```text
CreatePlayer(WorldContextObject: UObject *, ControllerId: int32, bSpawnPawn: bool) -> APlayerController *
```

Create a new player for this game.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ControllerId` | `int32` | The ID of the controller that the should control the newly created player. A value of -1 specifies to use the next available ID |
| `bSpawnPawn` | `bool` | Whether a pawn should be spawned immediately. If false a pawn will not be created until transition to the next map. |

**Returns**

| Type | Description |
|---|---|
| `APlayerController *` | - |

### `RemovePlayer`

```text
RemovePlayer(Player: APlayerController *, bDestroyPawn: bool) -> void
```

Removes a player from this game.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `APlayerController *` | The player controller of the player to be removed |
| `bDestroyPawn` | `bool` | Whether the controlled pawn should be deleted as well |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPlayerControllerID`

```text
GetPlayerControllerID(Player: APlayerController *) -> int32
```

Gets what controller ID a Player is using

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `APlayerController *` | The player controller of the player to get the ID of |

**Returns**

| Type | Description |
|---|---|
| `int32` | The ID of the passed in player. -1 if there is no controller for the passed in player |

### `SetPlayerControllerID`

```text
SetPlayerControllerID(Player: APlayerController *, ControllerId: int32) -> void
```

Sets what controller ID a Player should be using

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `APlayerController *` | The player controller of the player to change the controller ID of |
| `ControllerId` | `int32` | The controller ID to assign to this player |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `LoadStreamLevel`

```text
LoadStreamLevel(WorldContextObject: UObject *, LevelName: FName, bMakeVisibleAfterLoad: bool, bShouldBlockOnLoad: bool, LatentInfo: FLatentActionInfo) -> void
```

加载子关卡

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `LevelName` | `FName` | 子关卡名称 |
| `bMakeVisibleAfterLoad` | `bool` | 加载后是否显示 |
| `bShouldBlockOnLoad` | `bool` | 加载时是否阻塞 |
| `LatentInfo` | `FLatentActionInfo` | 回调信息结构 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnloadStreamLevel`

```text
UnloadStreamLevel(WorldContextObject: UObject *, LevelName: FName, LatentInfo: FLatentActionInfo) -> void
```

加载子关卡

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `LevelName` | `FName` | 子关卡名称 |
| `LatentInfo` | `FLatentActionInfo` | 回调信息结构 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetStreamingLevel`

```text
GetStreamingLevel(WorldContextObject: UObject *, PackageName: FName) -> ULevelStreaming *
```

Returns level streaming object with specified level package name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PackageName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `ULevelStreaming *` | - |

### `FlushLevelStreaming`

```text
FlushLevelStreaming(WorldContextObject: UObject *) -> void
```

刷新关卡流，直到所有子关卡加载完毕时返回

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FlushLevelStreamingBasedOnCharacterLocation`

```text
FlushLevelStreamingBasedOnCharacterLocation(WorldContextObject: UObject *, CharacterLocation: FVector) -> void
```

更新玩家的位置，触发LevelBounds，然后加载所有关卡

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `CharacterLocation` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FlushAllStreamingResource`

```text
FlushAllStreamingResource(WorldContextObject: UObject *) -> void
```

触发TextureStreaming， 将贴图全部加载完毕

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CancelAsyncLoading`

```text
CancelAsyncLoading() -> void
```

Cancels all currently queued streaming packages

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OpenLevel`

```text
OpenLevel(WorldContextObject: UObject *, LevelName: FName, bAbsolute: bool, Options: FString) -> void
```

Travel to another level

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `LevelName` | `FName` | the level to open |
| `bAbsolute` | `bool` | if true options are reset, if false options are carried over from current level |
| `Options` | `FString` | a string of options to use for the travel URL |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OpenShaderLibrary`

```text
OpenShaderLibrary(Name: FString &, VersionNum: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Name` | `FString &` | - |
| `VersionNum` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CloseShaderLibrary`

```text
CloseShaderLibrary(Name: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Name` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableShaderGroup`

```text
EnableShaderGroup(GroupName: FString &, ShaderPlatform: int32) -> void
```

Enable a new ShaderGroup for all opened ShaderCodeLibrary

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GroupName` | `FString &` | - |
| `ShaderPlatform` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableShaderLevel`

```text
EnableShaderLevel(ShaderLevelName: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ShaderLevelName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableShaderPak`

```text
EnableShaderPak(ShaderPakName: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ShaderPakName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableShaderLevel`

```text
DisableShaderLevel(ShaderLevelName: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ShaderLevelName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableShaderPak`

```text
DisableShaderPak(ShaderPakName: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ShaderPakName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestartShaderPrecompile`

```text
RestartShaderPrecompile() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OpenShaderCodeLibrary`

```text
OpenShaderCodeLibrary(Version: FString &, bUseContentShaders: bool) -> void
```

OpenShaderCodeLibrary in Saved Folder

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Version` | `FString &` | - |
| `bUseContentShaders` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCurrentLevelName`

```text
GetCurrentLevelName(WorldContextObject: UObject *, bRemovePrefixString: bool) -> FString
```

获得当前关卡名称

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `bRemovePrefixString` | `bool` | 是否移除prefix的字符串 |

**Returns**

| Type | Description |
|---|---|
| `FString` | 关卡名称 |

### `GetGameMode`

```text
GetGameMode(WorldContextObject: UObject *) -> AGameModeBase *
```

获得当前GameMode

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `AGameModeBase *` | 当前GameMode |

### `GetGameState`

```text
GetGameState(WorldContextObject: UObject *) -> AGameStateBase *
```

获得当前GameState

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `AGameStateBase *` | 当前GameState |

### `GetGameStateByWorldContext`

```text
GetGameStateByWorldContext(WorldContextObject: UObject *) -> AGameStateBase *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `AGameStateBase *` | - |

### `GetObjectClass`

```text
GetObjectClass(Object: UObject *) -> UClass *
```

获得对象的类型

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | 指定对象 |

**Returns**

| Type | Description |
|---|---|
| `UClass *` | 对象的类型 |

### `GetGlobalTimeDilation`

```text
GetGlobalTimeDilation(WorldContextObject: UObject *) -> float
```

获得当前时间膨胀

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `float` | Current time dilation. |

### `SetGlobalTimeDilation`

```text
SetGlobalTimeDilation(WorldContextObject: UObject *, TimeDilation: float) -> void
```

设置时间膨胀

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `TimeDilation` | `float` | 世界的时间膨胀 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetGamePaused`

```text
SetGamePaused(WorldContextObject: UObject *, bPaused: bool) -> bool
```

设置游戏是否暂停

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `bPaused` | `bool` | 是否暂停 |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether the game was successfully pausedunpaused |

### `IsGamePaused`

```text
IsGamePaused(WorldContextObject: UObject *) -> bool
```

判断游戏是否暂停

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether the game is currently paused or not |

### `ApplyRadialDamage`

```text
ApplyRadialDamage(WorldContextObject: UObject *, BaseDamage: float, Origin: FVector &, DamageRadius: float, DamageTypeClass: TSubclassOf < UDamageType >, IgnoreActors: TArray < AActor * > &, DamageCauser: AActor *, InstigatedByController: AController *, bDoFullDamage: bool, DamagePreventionChannel: ECollisionChannel, DamageTag: int32) -> bool
```

Hurt locally authoritative actors within the radius. Will only hit components that block the Visibility channel.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `BaseDamage` | `float` | - The base damage to apply, i.e. the damage at the origin. |
| `Origin` | `FVector &` | - Epicenter of the damage area. |
| `DamageRadius` | `float` | - Radius of the damage area, from Origin |
| `DamageTypeClass` | `TSubclassOf < UDamageType >` | - Class that describes the damage that was done. |
| `IgnoreActors` | `TArray < AActor * > &` | - |
| `DamageCauser` | `AActor *` | - Actor that actually caused the damage (e.g. the grenade that exploded). This actor will not be damaged and it will not block damage. |
| `InstigatedByController` | `AController *` | - Controller that was responsible for causing this damage (e.g. player who threw the grenade) |
| `bDoFullDamage` | `bool` | - |
| `DamagePreventionChannel` | `ECollisionChannel` | - Damage will not be applied to victim if there is something between the origin and the victim which blocks traces on this channel |
| `DamageTag` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if damage was applied to at least one actor. |

### `ApplyRadialDamageWithFalloff`

```text
ApplyRadialDamageWithFalloff(WorldContextObject: UObject *, BaseDamage: float, MinimumDamage: float, Origin: FVector &, DamageInnerRadius: float, DamageOuterRadius: float, DamageFalloff: float, DamageTypeClass: TSubclassOf < UDamageType >, IgnoreActors: TArray < AActor * > &, DamageCauser: AActor *, InstigatedByController: AController *, DamagePreventionChannel: ECollisionChannel, DamageTag: int32) -> bool
```

Hurt locally authoritative actors within the radius. Will only hit components that block the Visibility channel.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `BaseDamage` | `float` | - The base damage to apply, i.e. the damage at the origin. |
| `MinimumDamage` | `float` | - |
| `Origin` | `FVector &` | - Epicenter of the damage area. |
| `DamageInnerRadius` | `float` | - Radius of the full damage area, from Origin |
| `DamageOuterRadius` | `float` | - Radius of the minimum damage area, from Origin |
| `DamageFalloff` | `float` | - Falloff exponent of damage from DamageInnerRadius to DamageOuterRadius |
| `DamageTypeClass` | `TSubclassOf < UDamageType >` | - Class that describes the damage that was done. |
| `IgnoreActors` | `TArray < AActor * > &` | - |
| `DamageCauser` | `AActor *` | - Actor that actually caused the damage (e.g. the grenade that exploded) |
| `InstigatedByController` | `AController *` | - Controller that was responsible for causing this damage (e.g. player who threw the grenade) |
| `DamagePreventionChannel` | `ECollisionChannel` | - Damage will not be applied to victim if there is something between the origin and the victim which blocks traces on this channel |
| `DamageTag` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if damage was applied to at least one actor. |

### `ApplyPointDamage`

```text
ApplyPointDamage(DamagedActor: AActor *, BaseDamage: float, HitFromDirection: FVector &, HitInfo: FHitResult &, EventInstigator: AController *, DamageCauser: AActor *, DamageTypeClass: TSubclassOf < UDamageType >, DamageTag: int32) -> float
```

Hurts the specified actor with the specified impact.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DamagedActor` | `AActor *` | - Actor that will be damaged. |
| `BaseDamage` | `float` | - The base damage to apply. |
| `HitFromDirection` | `FVector &` | - Direction the hit came FROM |
| `HitInfo` | `FHitResult &` | - Collision or trace result that describes the hit |
| `EventInstigator` | `AController *` | - Controller that was responsible for causing this damage (e.g. player who shot the weapon) |
| `DamageCauser` | `AActor *` | - Actor that actually caused the damage (e.g. the grenade that exploded) |
| `DamageTypeClass` | `TSubclassOf < UDamageType >` | - Class that describes the damage that was done. |
| `DamageTag` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | Actual damage the ended up being applied to the actor. |

### `ApplyDamage`

```text
ApplyDamage(DamagedActor: AActor *, BaseDamage: float, EventInstigator: AController *, DamageCauser: AActor *, DamageTypeClass: TSubclassOf < UDamageType >, DamageTag: int32) -> float
```

Hurts the specified actor with generic damage.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DamagedActor` | `AActor *` | - Actor that will be damaged. |
| `BaseDamage` | `float` | - The base damage to apply. |
| `EventInstigator` | `AController *` | - Controller that was responsible for causing this damage (e.g. player who shot the weapon) |
| `DamageCauser` | `AActor *` | - Actor that actually caused the damage (e.g. the grenade that exploded) |
| `DamageTypeClass` | `TSubclassOf < UDamageType >` | - Class that describes the damage that was done. |
| `DamageTag` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | Actual damage the ended up being applied to the actor. |

### `PlayWorldCameraShake`

```text
PlayWorldCameraShake(WorldContextObject: UObject *, Shake: TSubclassOf < UCameraShake >, Epicenter: FVector, InnerRadius: float, OuterRadius: float, Falloff: float, bOrientShakeTowardsEpicenter: bool) -> void
```

Plays an in-world camera shake that affects all nearby local players, with distance-based attenuation. Does not replicate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - Object that we can obtain a world context from |
| `Shake` | `TSubclassOf < UCameraShake >` | - Camera shake asset to use |
| `Epicenter` | `FVector` | - location to place the effect in world space |
| `InnerRadius` | `float` | - Cameras inside this radius are ignored |
| `OuterRadius` | `float` | - Cameras outside of InnerRadius and inside this are effected |
| `Falloff` | `float` | - Affects falloff of effect as it nears OuterRadius |
| `bOrientShakeTowardsEpicenter` | `bool` | - Changes the rotation of shake to point towards epicenter instead of forward |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SpawnEmitterAtLocation`

```text
SpawnEmitterAtLocation(WorldContextObject: UObject *, EmitterTemplate: UParticleSystem *, Location: FVector, Rotation: FRotator, Scale: FVector, bAutoDestroy: bool) -> UParticleSystemComponent *
```

Plays the specified effect at the given location and rotation, fire and forget. The system will go away when the effect is complete. Does not replicate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - Object that we can obtain a world context from |
| `EmitterTemplate` | `UParticleSystem *` | - particle system to create |
| `Location` | `FVector` | - location to place the effect in world space |
| `Rotation` | `FRotator` | - rotation to place the effect in world space |
| `Scale` | `FVector` | - scale to create the effect at |
| `bAutoDestroy` | `bool` | - Whether the component will automatically be destroyed when the particle system completes playing or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UParticleSystemComponent *` | - |

### `SpawnEmitterAttached`

```text
SpawnEmitterAttached(EmitterTemplate: UParticleSystem *, AttachToComponent: USceneComponent *, AttachPointName: FName, Location: FVector, Rotation: FRotator, Scale: FVector, LocationType: EAttachLocation :: Type, bAutoDestroy: bool) -> UParticleSystemComponent *
```

Plays the specified effect attached to and following the specified component. The system will go away when the effect is complete. Does not replicate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterTemplate` | `UParticleSystem *` | - particle system to create |
| `AttachToComponent` | `USceneComponent *` | - |
| `AttachPointName` | `FName` | - Optional named point within the AttachComponent to spawn the emitter at |
| `Location` | `FVector` | - Depending on the value of LocationType this is either a relative offset from the attach componentpoint or an absolute world location that will be translated to a relative offset (if LocationType is KeepWorldPosition). |
| `Rotation` | `FRotator` | - Depending on the value of LocationType this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a relative offset (if LocationType is KeepWorldPosition). |
| `Scale` | `FVector` | - Depending on the value of LocationType this is either a relative scale from the attach component or an absolute world scale that will be translated to a relative scale (if LocationType is KeepWorldPosition). |
| `LocationType` | `EAttachLocation :: Type` | - Specifies whether Location is a relative offset or an absolute world position |
| `bAutoDestroy` | `bool` | - Whether the component will automatically be destroyed when the particle system completes playing or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UParticleSystemComponent *` | - |

### `SpawnEmitterAttachedToActor`

```text
SpawnEmitterAttachedToActor(EmitterTemplate: UParticleSystem *, AttachToComponent: USceneComponent *, AttachPointName: FName, Location: FVector, Rotation: FRotator, Scale: FVector, LocationType: EAttachLocation :: Type, bAutoDestroy: bool) -> UParticleSystemComponent *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterTemplate` | `UParticleSystem *` | - |
| `AttachToComponent` | `USceneComponent *` | - |
| `AttachPointName` | `FName` | - |
| `Location` | `FVector` | - |
| `Rotation` | `FRotator` | - |
| `Scale` | `FVector` | - |
| `LocationType` | `EAttachLocation :: Type` | - |
| `bAutoDestroy` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `UParticleSystemComponent *` | - |

### `AreAnyListenersWithinRange`

```text
AreAnyListenersWithinRange(WorldContextObject: UObject *, Location: FVector, MaximumRange: float) -> bool
```

Determines if any audio listeners are within range of the specified location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Location` | `FVector` | The location to potentially play a sound at |
| `MaximumRange` | `float` | The maximum distance away from Location that a listener can be |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetGlobalPitchModulation`

```text
SetGlobalPitchModulation(WorldContextObject: UObject *, PitchModulation: float, TimeSec: float) -> void
```

Sets a global pitch modulation scalar that will apply to all non-UI sounds
	
	  Fire and Forget.
	  Not Replicated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PitchModulation` | `float` | - A pitch modulation value to globally set. |
| `TimeSec` | `float` | - A time value to linearly interpolate the global modulation pitch over from it's current value. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetGlobalListenerFocusParameters`

```text
SetGlobalListenerFocusParameters(WorldContextObject: UObject *, FocusAzimuthScale: float, NonFocusAzimuthScale: float, FocusDistanceScale: float, NonFocusDistanceScale: float, FocusVolumeScale: float, NonFocusVolumeScale: float, FocusPriorityScale: float, NonFocusPriorityScale: float) -> void
```

Sets the global listener focus parameters which will scale focus behavior of sounds based on their focus azimuth settings in their attenuation settings.
	
	  Fire and Forget.
	  Not Replicated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `FocusAzimuthScale` | `float` | - An angle scale value used to scale the azimuth angle that defines where sounds are in-focus. |
| `NonFocusAzimuthScale` | `float` | - |
| `FocusDistanceScale` | `float` | - A distance scale value to use for sounds which are in-focus. Values < 1.0 will reduce perceived distance to sounds, values > 1.0 will increase perceived distance to in-focus sounds. |
| `NonFocusDistanceScale` | `float` | - A distance scale value to use for sounds which are out-of-focus. Values < 1.0 will reduce perceived distance to sounds, values > 1.0 will increase perceived distance to in-focus sounds. |
| `FocusVolumeScale` | `float` | - |
| `NonFocusVolumeScale` | `float` | - |
| `FocusPriorityScale` | `float` | - A priority scale value (> 0.0) to use for sounds which are in-focus. Values < 1.0 will reduce the priority of in-focus sounds, values > 1.0 will increase the priority of in-focus sounds. |
| `NonFocusPriorityScale` | `float` | - A priority scale value (> 0.0) to use for sounds which are out-of-focus. Values < 1.0 will reduce the priority of sounds out-of-focus sounds, values > 1.0 will increase the priority of out-of-focus sounds. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlaySound2D`

```text
PlaySound2D(WorldContextObject: UObject *, Sound: USoundBase *, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, ConcurrencySettings: USoundConcurrency *, OwningActor: AActor *) -> void
```

Plays a sound directly with no attenuation, perfect for UI sounds.
	 
	   Fire and Forget.
	   Not Replicated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Sound` | `USoundBase *` | - Sound to play. |
| `VolumeMultiplier` | `float` | - Multiplied with the volume to make the sound louder or softer. |
| `PitchMultiplier` | `float` | - Multiplies the pitch. |
| `StartTime` | `float` | - How far in to the sound to begin playback at |
| `ConcurrencySettings` | `USoundConcurrency *` | - Override concurrency settings package to play sound with |
| `OwningActor` | `AActor *` | - The actor to use as the "owner" for concurrency settings purposes. Allows PlaySound calls to do a concurrency limit per owner. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SpawnSound2D`

```text
SpawnSound2D(WorldContextObject: UObject *, Sound: USoundBase *, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, ConcurrencySettings: USoundConcurrency *, bPersistAcrossLevelTransition: bool, bAutoDestroy: bool) -> UAudioComponent *
```

Spawns a sound with no attenuation, perfect for UI sounds.
	 
	   Not Replicated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Sound` | `USoundBase *` | - Sound to play. |
| `VolumeMultiplier` | `float` | - Multiplied with the volume to make the sound louder or softer. |
| `PitchMultiplier` | `float` | - Multiplies the pitch. |
| `StartTime` | `float` | - How far in to the sound to begin playback at |
| `ConcurrencySettings` | `USoundConcurrency *` | - Override concurrency settings package to play sound with |
| `bPersistAcrossLevelTransition` | `bool` | - |
| `bAutoDestroy` | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UAudioComponent *` | An audio component to manipulate the spawned sound |

### `CreateSound2D`

```text
CreateSound2D(WorldContextObject: UObject *, Sound: USoundBase *, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, ConcurrencySettings: USoundConcurrency *, bPersistAcrossLevelTransition: bool, bAutoDestroy: bool) -> UAudioComponent *
```

Creates a sound with no attenuation, perfect for UI sounds. This does NOT play the sound
	 
	   Not Replicated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Sound` | `USoundBase *` | - Sound to create. |
| `VolumeMultiplier` | `float` | - Multiplied with the volume to make the sound louder or softer. |
| `PitchMultiplier` | `float` | - Multiplies the pitch. |
| `StartTime` | `float` | - How far in to the sound to begin playback at |
| `ConcurrencySettings` | `USoundConcurrency *` | - Override concurrency settings package to play sound with |
| `bPersistAcrossLevelTransition` | `bool` | - |
| `bAutoDestroy` | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UAudioComponent *` | An audio component to manipulate the created sound |

### `PlaySoundAtLocation`

```text
PlaySoundAtLocation(WorldContextObject: UObject *, Sound: USoundBase *, Location: FVector, Rotation: FRotator, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, AttenuationSettings: USoundAttenuation *, ConcurrencySettings: USoundConcurrency *, OwningActor: AActor *) -> void
```

Plays a sound at the given location. This is a fire and forget sound and does not travel with any actor. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Sound` | `USoundBase *` | - sound to play |
| `Location` | `FVector` | - World position to play sound at |
| `Rotation` | `FRotator` | - World rotation to play sound at |
| `VolumeMultiplier` | `float` | - Volume multiplier |
| `PitchMultiplier` | `float` | - PitchMultiplier |
| `StartTime` | `float` | - How far in to the sound to begin playback at |
| `AttenuationSettings` | `USoundAttenuation *` | - Override attenuation settings package to play sound with |
| `ConcurrencySettings` | `USoundConcurrency *` | - Override concurrency settings package to play sound with |
| `OwningActor` | `AActor *` | - The actor to use as the "owner" for concurrency settings purposes. Allows PlaySound calls to do a concurrency limit per owner. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SpawnSoundAtLocation`

```text
SpawnSoundAtLocation(WorldContextObject: UObject *, Sound: USoundBase *, Location: FVector, Rotation: FRotator, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, AttenuationSettings: USoundAttenuation *, ConcurrencySettings: USoundConcurrency *, bAutoDestroy: bool) -> UAudioComponent *
```

Spawns a sound at the given location. This does not travel with any actor. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Sound` | `USoundBase *` | - sound to play |
| `Location` | `FVector` | - World position to play sound at |
| `Rotation` | `FRotator` | - World rotation to play sound at |
| `VolumeMultiplier` | `float` | - Volume multiplier |
| `PitchMultiplier` | `float` | - PitchMultiplier |
| `StartTime` | `float` | - How far in to the sound to begin playback at |
| `AttenuationSettings` | `USoundAttenuation *` | - Override attenuation settings package to play sound with |
| `ConcurrencySettings` | `USoundConcurrency *` | - Override concurrency settings package to play sound with |
| `bAutoDestroy` | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UAudioComponent *` | An audio component to manipulate the spawned sound |

### `SpawnSoundAttached`

```text
SpawnSoundAttached(Sound: USoundBase *, AttachToComponent: USceneComponent *, AttachPointName: FName, Location: FVector, Rotation: FRotator, LocationType: EAttachLocation :: Type, bStopWhenAttachedToDestroyed: bool, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, AttenuationSettings: USoundAttenuation *, ConcurrencySettings: USoundConcurrency *, bAutoDestroy: bool) -> UAudioComponent *
```

Plays a sound attached to and following the specified component. This is a fire and forget sound. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Sound` | `USoundBase *` | - sound to play |
| `AttachToComponent` | `USceneComponent *` | - |
| `AttachPointName` | `FName` | - Optional named point within the AttachComponent to play the sound at |
| `Location` | `FVector` | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world position that will be translated to a relative offset |
| `Rotation` | `FRotator` | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a relative offset |
| `LocationType` | `EAttachLocation :: Type` | - Specifies whether Location is a relative offset or an absolute world position |
| `bStopWhenAttachedToDestroyed` | `bool` | - Specifies whether the sound should stop playing when the owner of the attach to component is destroyed. |
| `VolumeMultiplier` | `float` | - Volume multiplier |
| `PitchMultiplier` | `float` | - PitchMultiplier |
| `StartTime` | `float` | - How far in to the sound to begin playback at |
| `AttenuationSettings` | `USoundAttenuation *` | - Override attenuation settings package to play sound with |
| `ConcurrencySettings` | `USoundConcurrency *` | - Override concurrency settings package to play sound with |
| `bAutoDestroy` | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UAudioComponent *` | An audio component to manipulate the spawned sound |

### `PlayDialogue2D`

```text
PlayDialogue2D(WorldContextObject: UObject *, Dialogue: UDialogueWave *, Context: FDialogueContext &, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float) -> void
```

Plays a dialogue directly with no attenuation, perfect for UI.
	 
	   Fire and Forget.
	   Not Replicated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Dialogue` | `UDialogueWave *` | - dialogue to play |
| `Context` | `FDialogueContext &` | - context the dialogue is to play in |
| `VolumeMultiplier` | `float` | - Multiplied with the volume to make the sound louder or softer. |
| `PitchMultiplier` | `float` | - Multiplies the pitch. |
| `StartTime` | `float` | - How far in to the dialogue to begin playback at |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SpawnDialogue2D`

```text
SpawnDialogue2D(WorldContextObject: UObject *, Dialogue: UDialogueWave *, Context: FDialogueContext &, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, bAutoDestroy: bool) -> UAudioComponent *
```

Spawns a dialogue with no attenuation, perfect for UI.
	 
	   Not Replicated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Dialogue` | `UDialogueWave *` | - dialogue to play |
| `Context` | `FDialogueContext &` | - context the dialogue is to play in |
| `VolumeMultiplier` | `float` | - Multiplied with the volume to make the sound louder or softer. |
| `PitchMultiplier` | `float` | - Multiplies the pitch. |
| `StartTime` | `float` | - How far in to the dialogue to begin playback at |
| `bAutoDestroy` | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UAudioComponent *` | An audio component to manipulate the spawned sound |

### `PlayDialogueAtLocation`

```text
PlayDialogueAtLocation(WorldContextObject: UObject *, Dialogue: UDialogueWave *, Context: FDialogueContext &, Location: FVector, Rotation: FRotator, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, AttenuationSettings: USoundAttenuation *) -> void
```

Plays a dialogue at the given location. This is a fire and forget sound and does not travel with any actor. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Dialogue` | `UDialogueWave *` | - dialogue to play |
| `Context` | `FDialogueContext &` | - context the dialogue is to play in |
| `Location` | `FVector` | - World position to play dialogue at |
| `Rotation` | `FRotator` | - World rotation to play dialogue at |
| `VolumeMultiplier` | `float` | - Volume multiplier |
| `PitchMultiplier` | `float` | - Pitch multiplier |
| `StartTime` | `float` | - How far in to the dialogue to begin playback at |
| `AttenuationSettings` | `USoundAttenuation *` | - Override attenuation settings package to play sound with |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SpawnDialogueAtLocation`

```text
SpawnDialogueAtLocation(WorldContextObject: UObject *, Dialogue: UDialogueWave *, Context: FDialogueContext &, Location: FVector, Rotation: FRotator, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, AttenuationSettings: USoundAttenuation *, bAutoDestroy: bool) -> UAudioComponent *
```

Plays a dialogue at the given location. This is a fire and forget sound and does not travel with any actor. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Dialogue` | `UDialogueWave *` | - dialogue to play |
| `Context` | `FDialogueContext &` | - context the dialogue is to play in |
| `Location` | `FVector` | - World position to play dialogue at |
| `Rotation` | `FRotator` | - World rotation to play dialogue at |
| `VolumeMultiplier` | `float` | - Volume multiplier |
| `PitchMultiplier` | `float` | - PitchMultiplier |
| `StartTime` | `float` | - How far in to the dialogue to begin playback at |
| `AttenuationSettings` | `USoundAttenuation *` | - Override attenuation settings package to play sound with |
| `bAutoDestroy` | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UAudioComponent *` | Audio Component to manipulate the playing dialogue with |

### `SpawnDialogueAttached`

```text
SpawnDialogueAttached(Dialogue: UDialogueWave *, Context: FDialogueContext &, AttachToComponent: USceneComponent *, AttachPointName: FName, Location: FVector, Rotation: FRotator, LocationType: EAttachLocation :: Type, bStopWhenAttachedToDestroyed: bool, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, AttenuationSettings: USoundAttenuation *, bAutoDestroy: bool) -> UAudioComponent *
```

Spawns a dialogue attached to and following the specified component. This is a fire and forget sound. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Dialogue` | `UDialogueWave *` | - dialogue to play |
| `Context` | `FDialogueContext &` | - context the dialogue is to play in |
| `AttachToComponent` | `USceneComponent *` | - |
| `AttachPointName` | `FName` | - Optional named point within the AttachComponent to play the sound at |
| `Location` | `FVector` | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world position that will be translated to a relative offset |
| `Rotation` | `FRotator` | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a relative offset |
| `LocationType` | `EAttachLocation :: Type` | - Specifies whether Location is a relative offset or an absolute world position |
| `bStopWhenAttachedToDestroyed` | `bool` | - Specifies whether the sound should stop playing when the owner of the attach to component is destroyed. |
| `VolumeMultiplier` | `float` | - Volume multiplier |
| `PitchMultiplier` | `float` | - PitchMultiplier |
| `StartTime` | `float` | - How far in to the dialogue to begin playback at |
| `AttenuationSettings` | `USoundAttenuation *` | - Override attenuation settings package to play sound with |
| `bAutoDestroy` | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UAudioComponent *` | Audio Component to manipulate the playing dialogue with |

### `SpawnForceFeedbackAtLocation`

```text
SpawnForceFeedbackAtLocation(WorldContextObject: UObject *, ForceFeedbackEffect: UForceFeedbackEffect *, Location: FVector, Rotation: FRotator, bLooping: bool, IntensityMultiplier: float, StartTime: float, AttenuationSettings: UForceFeedbackAttenuation *, bAutoDestroy: bool) -> UForceFeedbackComponent *
```

Plays a force feedback effect at the given location. This is a fire and forget effect and does not travel with any actor. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ForceFeedbackEffect` | `UForceFeedbackEffect *` | - effect to play |
| `Location` | `FVector` | - World position to center the effect at |
| `Rotation` | `FRotator` | - World rotation to center the effect at |
| `bLooping` | `bool` | - |
| `IntensityMultiplier` | `float` | - Intensity multiplier |
| `StartTime` | `float` | - How far in to the feedback effect to begin playback at |
| `AttenuationSettings` | `UForceFeedbackAttenuation *` | - Override attenuation settings package to play effect with |
| `bAutoDestroy` | `bool` | - Whether the returned force feedback component will be automatically cleaned up when the feedback patern finishes (by completing or stopping) or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UForceFeedbackComponent *` | Force Feedback Component to manipulate the playing feedback effect with |

### `SpawnForceFeedbackAttached`

```text
SpawnForceFeedbackAttached(ForceFeedbackEffect: UForceFeedbackEffect *, AttachToComponent: USceneComponent *, AttachPointName: FName, Location: FVector, Rotation: FRotator, LocationType: EAttachLocation :: Type, bStopWhenAttachedToDestroyed: bool, bLooping: bool, IntensityMultiplier: float, StartTime: float, AttenuationSettings: UForceFeedbackAttenuation *, bAutoDestroy: bool) -> UForceFeedbackComponent *
```

Plays a force feedback effect attached to and following the specified component. This is a fire and forget effect. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ForceFeedbackEffect` | `UForceFeedbackEffect *` | - effect to play |
| `AttachToComponent` | `USceneComponent *` | - |
| `AttachPointName` | `FName` | - Optional named point within the AttachComponent to attach to |
| `Location` | `FVector` | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world position that will be translated to a relative offset |
| `Rotation` | `FRotator` | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a relative offset |
| `LocationType` | `EAttachLocation :: Type` | - Specifies whether Location is a relative offset or an absolute world position |
| `bStopWhenAttachedToDestroyed` | `bool` | - Specifies whether the feedback effect should stop playing when the owner of the attach to component is destroyed. |
| `bLooping` | `bool` | - |
| `IntensityMultiplier` | `float` | - Intensity multiplier |
| `StartTime` | `float` | - How far in to the feedback effect to begin playback at |
| `AttenuationSettings` | `UForceFeedbackAttenuation *` | - Override attenuation settings package to play effect with |
| `bAutoDestroy` | `bool` | - Whether the returned force feedback component will be automatically cleaned up when the feedback patern finishes (by completing or stopping) or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UForceFeedbackComponent *` | Force Feedback Component to manipulate the playing feedback effect with |

### `SetSubtitlesEnabled`

```text
SetSubtitlesEnabled(bEnabled: bool) -> void
```

Will set subtitles to be enabled or disabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnabled` | `bool` | will enable subtitle drawing if true, disable if false. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AreSubtitlesEnabled`

```text
AreSubtitlesEnabled() -> bool
```

Returns whether or not subtitles are currently enabled.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if subtitles are enabled. |

### `SetBaseSoundMix`

```text
SetBaseSoundMix(WorldContextObject: UObject *, InSoundMix: USoundMix *) -> void
```

Set the sound mix of the audio system for special EQing

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `InSoundMix` | `USoundMix *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSoundMixClassOverride`

```text
SetSoundMixClassOverride(WorldContextObject: UObject *, InSoundMixModifier: USoundMix *, InSoundClass: USoundClass *, Volume: float, Pitch: float, FadeInTime: float, bApplyToChildren: bool) -> void
```

Overrides the sound class adjuster in the given sound mix. If the sound class does not exist in the input sound mix, the sound class adjustment will be added to the sound mix.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `InSoundMixModifier` | `USoundMix *` | The sound mix to modify. |
| `InSoundClass` | `USoundClass *` | The sound class to override (or add) in the sound mix. |
| `Volume` | `float` | The volume scale to set the sound class adjuster to. |
| `Pitch` | `float` | The pitch scale to set the sound class adjuster to. |
| `FadeInTime` | `float` | The interpolation time to use to go from the current sound class adjuster values to the new values. |
| `bApplyToChildren` | `bool` | Whether or not to apply this override to the sound class' children or to just the specified sound class. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearSoundMixClassOverride`

```text
ClearSoundMixClassOverride(WorldContextObject: UObject *, InSoundMixModifier: USoundMix *, InSoundClass: USoundClass *, FadeOutTime: float) -> void
```

Clears the override of the sound class adjuster in the given sound mix. If the override did not exist in the sound mix, this will do nothing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `InSoundMixModifier` | `USoundMix *` | The sound mix to modify. |
| `InSoundClass` | `USoundClass *` | The sound class to override (or add) in the sound mix. |
| `FadeOutTime` | `float` | The interpolation time to use to go from the current sound class adjuster override values to the non-override values. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PushSoundMixModifier`

```text
PushSoundMixModifier(WorldContextObject: UObject *, InSoundMixModifier: USoundMix *) -> void
```

Push a sound mix modifier onto the audio system

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `InSoundMixModifier` | `USoundMix *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PopSoundMixModifier`

```text
PopSoundMixModifier(WorldContextObject: UObject *, InSoundMixModifier: USoundMix *) -> void
```

Pop a sound mix modifier from the audio system

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `InSoundMixModifier` | `USoundMix *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearSoundMixModifiers`

```text
ClearSoundMixModifiers(WorldContextObject: UObject *) -> void
```

Clear all sound mix modifiers from the audio system

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ActivateReverbEffect`

```text
ActivateReverbEffect(WorldContextObject: UObject *, ReverbEffect: UReverbEffect *, TagName: FName, Priority: float, Volume: float, FadeTime: float) -> void
```

Activates a Reverb Effect without the need for a volume

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ReverbEffect` | `UReverbEffect *` | Reverb Effect to use |
| `TagName` | `FName` | Tag to associate with Reverb Effect |
| `Priority` | `float` | Priority of the Reverb Effect |
| `Volume` | `float` | Volume level of Reverb Effect |
| `FadeTime` | `float` | Time before Reverb Effect is fully active |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DeactivateReverbEffect`

```text
DeactivateReverbEffect(WorldContextObject: UObject *, TagName: FName) -> void
```

Deactivates a Reverb Effect not applied by a volume

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `TagName` | `FName` | Tag associated with Reverb Effect to remove |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCurrentReverbEffect`

```text
GetCurrentReverbEffect(WorldContextObject: UObject *) -> UReverbEffect *
```

Returns the highest priority reverb settings currently active from any source (volumes or manual setting).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `UReverbEffect *` | - |

### `SpawnDecalAtLocation`

```text
SpawnDecalAtLocation(WorldContextObject: UObject *, DecalMaterial: UMaterialInterface *, DecalSize: FVector, Location: FVector, Rotation: FRotator, LifeSpan: float) -> UDecalComponent *
```

Spawns a decal at the given location and rotation, fire and forget. Does not replicate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `DecalMaterial` | `UMaterialInterface *` | - decal's material |
| `DecalSize` | `FVector` | - size of decal |
| `Location` | `FVector` | - location to place the decal in world space |
| `Rotation` | `FRotator` | - rotation to place the decal in world space |
| `LifeSpan` | `float` | - destroy decal component after time runs out (0 = infinite) |

**Returns**

| Type | Description |
|---|---|
| `UDecalComponent *` | - |

### `SpawnDecalAttached`

```text
SpawnDecalAttached(DecalMaterial: UMaterialInterface *, DecalSize: FVector, AttachToComponent: USceneComponent *, AttachPointName: FName, Location: FVector, Rotation: FRotator, LocationType: EAttachLocation :: Type, LifeSpan: float) -> UDecalComponent *
```

Spawns a decal attached to and following the specified component. Does not replicate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DecalMaterial` | `UMaterialInterface *` | - decal's material |
| `DecalSize` | `FVector` | - size of decal |
| `AttachToComponent` | `USceneComponent *` | - |
| `AttachPointName` | `FName` | - Optional named point within the AttachComponent to spawn the emitter at |
| `Location` | `FVector` | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world position that will be translated to a relative offset |
| `Rotation` | `FRotator` | - Depending on the value of LocationType this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a realative offset |
| `LocationType` | `EAttachLocation :: Type` | - Specifies whether Location is a relative offset or an absolute world position |
| `LifeSpan` | `float` | - destroy decal component after time runs out (0 = infinite) |

**Returns**

| Type | Description |
|---|---|
| `UDecalComponent *` | - |

### `BreakHitResult`

```text
BreakHitResult(Hit: FHitResult &, bBlockingHit: bool &, bInitialOverlap: bool &, Time: float &, Distance: float &, Location: FVector &, ImpactPoint: FVector &, Normal: FVector &, ImpactNormal: FVector &, PhysMat: UPhysicalMaterial * &, HitActor: AActor * &, HitComponent: UPrimitiveComponent * &, HitBoneName: FName &, HitItem: int32 &, FaceIndex: int32 &, TraceStart: FVector &, TraceEnd: FVector &) -> void
```

Extracts data from a HitResult.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Hit` | `FHitResult &` | The source HitResult. |
| `bBlockingHit` | `bool &` | True if there was a blocking hit, false otherwise. |
| `bInitialOverlap` | `bool &` | True if the hit started in an initial overlap. In this case some other values should be interpreted differently. Time will be 0, ImpactPoint will equal Location, and normals will be equal and indicate a depenetration vector. |
| `Time` | `float &` | 'Time' of impact along trace direction ranging from [0.0 to 1.0) if there is a hit, indicating time between start and end. Equals 1.0 if there is no hit. |
| `Distance` | `float &` | The distance from the TraceStart to the Location in world space. This value is 0 if there was an initial overlap (trace started inside another colliding object). |
| `Location` | `FVector &` | Location of the hit in world space. If this was a swept shape test, this is the location where we can place the shape in the world where it will not penetrate. |
| `ImpactPoint` | `FVector &` | Location of the actual contact point of the trace shape with the surface of the hit object. Equal to Location in the case of an initial overlap. |
| `Normal` | `FVector &` | Normal of the hit in world space, for the object that was swept (e.g. for a sphere trace this points towards the sphere's center). Equal to ImpactNormal for line tests. |
| `ImpactNormal` | `FVector &` | Normal of the hit in world space, for the object that was hit by the sweep. |
| `PhysMat` | `UPhysicalMaterial * &` | Physical material that was hit. Must set bReturnPhysicalMaterial to true in the query params for this to be returned. |
| `HitActor` | `AActor * &` | Actor hit by the trace. |
| `HitComponent` | `UPrimitiveComponent * &` | PrimitiveComponent hit by the trace. |
| `HitBoneName` | `FName &` | Name of the bone hit (valid only if we hit a skeletal mesh). |
| `HitItem` | `int32 &` | Primitive-specific data recording which item in the primitive was hit |
| `FaceIndex` | `int32 &` | If colliding with trimesh or landscape, index of face that was hit. |
| `TraceStart` | `FVector &` | - |
| `TraceEnd` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MakeHitResult`

```text
MakeHitResult(bBlockingHit: bool, bInitialOverlap: bool, Time: float, Distance: float, Location: FVector, ImpactPoint: FVector, Normal: FVector, ImpactNormal: FVector, PhysMat: UPhysicalMaterial *, HitActor: AActor *, HitComponent: UPrimitiveComponent *, HitBoneName: FName, HitItem: int32, FaceIndex: int32, TraceStart: FVector, TraceEnd: FVector) -> FHitResult
```

Create a HitResult struct

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bBlockingHit` | `bool` | True if there was a blocking hit, false otherwise. |
| `bInitialOverlap` | `bool` | True if the hit started in an initial overlap. In this case some other values should be interpreted differently. Time will be 0, ImpactPoint will equal Location, and normals will be equal and indicate a depenetration vector. |
| `Time` | `float` | 'Time' of impact along trace direction ranging from [0.0 to 1.0) if there is a hit, indicating time between start and end. Equals 1.0 if there is no hit. |
| `Distance` | `float` | The distance from the TraceStart to the Location in world space. This value is 0 if there was an initial overlap (trace started inside another colliding object). |
| `Location` | `FVector` | Location of the hit in world space. If this was a swept shape test, this is the location where we can place the shape in the world where it will not penetrate. |
| `ImpactPoint` | `FVector` | Location of the actual contact point of the trace shape with the surface of the hit object. Equal to Location in the case of an initial overlap. |
| `Normal` | `FVector` | Normal of the hit in world space, for the object that was swept (e.g. for a sphere trace this points towards the sphere's center). Equal to ImpactNormal for line tests. |
| `ImpactNormal` | `FVector` | Normal of the hit in world space, for the object that was hit by the sweep. |
| `PhysMat` | `UPhysicalMaterial *` | Physical material that was hit. Must set bReturnPhysicalMaterial to true in the query params for this to be returned. |
| `HitActor` | `AActor *` | Actor hit by the trace. |
| `HitComponent` | `UPrimitiveComponent *` | PrimitiveComponent hit by the trace. |
| `HitBoneName` | `FName` | Name of the bone hit (valid only if we hit a skeletal mesh). |
| `HitItem` | `int32` | Primitive-specific data recording which item in the primitive was hit |
| `FaceIndex` | `int32` | If colliding with trimesh or landscape, index of face that was hit. |
| `TraceStart` | `FVector` | - |
| `TraceEnd` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FHitResult` | - |

### `GetSurfaceType`

```text
GetSurfaceType(Hit: FHitResult &) -> EPhysicalSurface
```

Returns the EPhysicalSurface type of the given Hit.
	  To edit surface type for your project, use ProjectSettingsPhysicsPhysicalSurface section

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Hit` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `EPhysicalSurface` | - |

### `FindCollisionUV`

```text
FindCollisionUV(Hit: FHitResult &, UVChannel: int32, UV: FVector2D &) -> bool
```

Try and find the UV for a collision impact. Note this ONLY works if 'Support UV From Hit Results' is enabled in Physics Settings.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Hit` | `FHitResult &` | - |
| `UVChannel` | `int32` | - |
| `UV` | `FVector2D &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `CreateSaveGameObject`

```text
CreateSaveGameObject(SaveGameClass: TSubclassOf < USaveGame >) -> USaveGame *
```

Create a new, empty SaveGame object to set data on and then pass to SaveGameToSlot.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SaveGameClass` | `TSubclassOf < USaveGame >` | Class of SaveGame to create |

**Returns**

| Type | Description |
|---|---|
| `USaveGame *` | New SaveGame object to write data to |

### `CreateSaveGameObjectFromBlueprint`

```text
CreateSaveGameObjectFromBlueprint(SaveGameBlueprint: UBlueprint *) -> USaveGame *
```

Create a new, empty SaveGame object to set data on and then pass to SaveGameToSlot.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SaveGameBlueprint` | `UBlueprint *` | Blueprint of SaveGame to create |

**Returns**

| Type | Description |
|---|---|
| `USaveGame *` | New SaveGame object to write data to |

### `SaveGameToSlot`

```text
SaveGameToSlot(SaveGameObject: USaveGame *, SlotName: FString &, UserIndex: int32) -> bool
```

Save the contents of the SaveGameObject to a slot.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SaveGameObject` | `USaveGame *` | Object that contains data about the save game that we want to write out |
| `SlotName` | `FString &` | Name of save game slot to save to. |
| `UserIndex` | `int32` | For some platforms, master user index to identify the user doing the saving. |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether we successfully saved this information |

### `DoesSaveGameExist`

```text
DoesSaveGameExist(SlotName: FString &, UserIndex: int32) -> bool
```

See if a save game exists with the specified name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotName` | `FString &` | Name of save game slot. |
| `UserIndex` | `int32` | For some platforms, master user index to identify the user doing the saving. |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `BindLoadGameGuardEntranceCheckDelegate`

```text
BindLoadGameGuardEntranceCheckDelegate(Obj: UObject *, FuncName: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Obj` | `UObject *` | - |
| `FuncName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BindLoadGameGuardExitCheckDelegate`

```text
BindLoadGameGuardExitCheckDelegate(Obj: UObject *, FuncName: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Obj` | `UObject *` | - |
| `FuncName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `LoadGameFromSlot`

```text
LoadGameFromSlot(SlotName: FString &, UserIndex: int32) -> USaveGame *
```

Load the contents from a given slot.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotName` | `FString &` | Name of the save game slot to load from. |
| `UserIndex` | `int32` | For some platforms, master user index to identify the user doing the loading. |

**Returns**

| Type | Description |
|---|---|
| `USaveGame *` | SaveGameObject	Object containing loaded game state (NULL if load fails) |

### `LoadGameFromSlotWithSizeLimit`

```text
LoadGameFromSlotWithSizeLimit(SlotName: FString &, UserIndex: int32, MaxSerSize: int32) -> USaveGame *
```

Load the contents from a given slot.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotName` | `FString &` | Name of the save game slot to load from. |
| `UserIndex` | `int32` | For some platforms, master user index to identify the user doing the loading. |
| `MaxSerSize` | `int32` | Specify the maxserializesize of archive, just working for fstring. |

**Returns**

| Type | Description |
|---|---|
| `USaveGame *` | SaveGameObject	Object containing loaded game state (NULL if load fails) |

### `LoadGameFromMemory`

```text
LoadGameFromMemory(ObjectBytes: TArray < uint8 > &, MaxSerSize: int32) -> USaveGame *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ObjectBytes` | `TArray < uint8 > &` | - |
| `MaxSerSize` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `USaveGame *` | - |

### `LoadGameFromMemoryWithSizeLimit`

```text
LoadGameFromMemoryWithSizeLimit(ObjectBytes: TArray < uint8 > &, MaxSerSize: int32) -> USaveGame *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ObjectBytes` | `TArray < uint8 > &` | - |
| `MaxSerSize` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `USaveGame *` | - |

### `DeleteGameInSlot`

```text
DeleteGameInSlot(SlotName: FString &, UserIndex: int32) -> bool
```

Delete a save game in a particular slot.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotName` | `FString &` | Name of save game slot to delete. |
| `UserIndex` | `int32` | For some platforms, master user index to identify the user doing the deletion. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if a file was actually able to be deleted. use DoesSaveGameExist to distinguish between delete failures and failure due to file not existing. |

### `GetWorldDeltaSeconds`

```text
GetWorldDeltaSeconds(WorldContextObject: UObject *) -> float
```

获得当前每帧的delta time，单位秒

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `float` | 每帧的delta time |

### `GetTimeSeconds`

```text
GetTimeSeconds(WorldContextObject: UObject *) -> float
```

获得当前游戏开始之后的时间，单位秒，受时间膨胀和游戏暂停影响

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `float` | 游戏时间 |

### `GetUnpausedTimeSeconds`

```text
GetUnpausedTimeSeconds(WorldContextObject: UObject *) -> float
```

获得当前游戏开始之后的时间，单位秒，受时间膨胀影响，但不受游戏暂停影响

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `float` | 游戏时间 |

### `GetRealTimeSeconds`

```text
GetRealTimeSeconds(WorldContextObject: UObject *) -> float
```

获得当前游戏开始之后的真实时间，单位秒，不受时间膨胀和游戏暂停影响

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `float` | 游戏时间 |

### `GetAudioTimeSeconds`

```text
GetAudioTimeSeconds(WorldContextObject: UObject *) -> float
```

获得当前游戏开始之后的时间，单位秒，不受时间膨胀影响，但受时间暂停影响

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `float` | 游戏时间 |

### `GetAccurateRealTime`

```text
GetAccurateRealTime(WorldContextObject: UObject *, Seconds: int32 &, PartialSeconds: float &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Seconds` | `int32 &` | - |
| `PartialSeconds` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableLiveStreaming`

```text
EnableLiveStreaming(Enable: bool) -> void
```

~ DVRStreaming API 
	
	  Toggle live DVR streaming.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Enable` | `bool` | If true enable streaming, otherwise disable. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPlatformName`

```text
GetPlatformName() -> FString
```

Returns the string name of the current platform, to perform different behavior based on platform.
	  (Platform names include Windows, Mac, IOS, Android, PS4, XboxOne, HTML5, Linux)

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `BlueprintSuggestProjectileVelocity`

```text
BlueprintSuggestProjectileVelocity(WorldContextObject: UObject *, TossVelocity: FVector &, StartLocation: FVector, EndLocation: FVector, LaunchSpeed: float, OverrideGravityZ: float, TraceOption: ESuggestProjVelocityTraceOption :: Type, CollisionRadius: float, bFavorHighArc: bool, bDrawDebug: bool) -> bool
```

Calculates an launch velocity for a projectile to hit a specified point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `TossVelocity` | `FVector &` | (output) Result launch velocity. |
| `StartLocation` | `FVector` | Intended launch location |
| `EndLocation` | `FVector` | Desired landing location |
| `LaunchSpeed` | `float` | Desired launch speed |
| `OverrideGravityZ` | `float` | Optional gravity override. 0 means "do not override". |
| `TraceOption` | `ESuggestProjVelocityTraceOption :: Type` | Controls whether or not to validate a clear path by tracing along the calculated arc |
| `CollisionRadius` | `float` | Radius of the projectile (assumed spherical), used when tracing |
| `bFavorHighArc` | `bool` | If true and there are 2 valid solutions, will return the higher arc. If false, will favor the lower arc. |
| `bDrawDebug` | `bool` | When true, a debug arc is drawn (red for an invalid arc, green for a valid arc) |

**Returns**

| Type | Description |
|---|---|
| `bool` | Returns false if there is no valid solution or the valid solutions are blocked.  Returns true otherwise. |

### `Blueprint_PredictProjectilePath_ByObjectType`

```text
Blueprint_PredictProjectilePath_ByObjectType(WorldContextObject: UObject *, OutHit: FHitResult &, OutPathPositions: TArray < FVector > &, OutLastTraceDestination: FVector &, StartPos: FVector, LaunchVelocity: FVector, bTracePath: bool, ProjectileRadius: float, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, DrawDebugTime: float, SimFrequency: float, MaxSimTime: float, OverrideGravityZ: float) -> bool
```

Predict the arc of a virtual projectile affected by gravity with collision checks along the arc. Returns a list of positions of the simulated arc and the destination reached by the simulation.
	 Returns true if it hit something.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `OutHit` | `FHitResult &` | Predicted hit result, if the projectile will hit something |
| `OutPathPositions` | `TArray < FVector > &` | Predicted projectile path. Ordered series of positions from StartPos to the end. Includes location at point of impact if it hit something. |
| `OutLastTraceDestination` | `FVector &` | Goal position of the final trace it did. Will not be in the path if there is a hit. |
| `StartPos` | `FVector` | First start trace location |
| `LaunchVelocity` | `FVector` | Velocity the "virtual projectile" is launched at |
| `bTracePath` | `bool` | Trace along the entire path to look for blocking hits |
| `ProjectileRadius` | `float` | Radius of the virtual projectile to sweep against the environment |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | ObjectTypes to trace against, if bTracePath is true. |
| `bTraceComplex` | `bool` | Use TraceComplex (trace against triangles not primitives) |
| `ActorsToIgnore` | `TArray < AActor * > &` | Actors to exclude from the traces |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | Debug type (one-frame, duration, persistent) |
| `DrawDebugTime` | `float` | Duration of debug lines (only relevant for DrawDebugType::Duration) |
| `SimFrequency` | `float` | Determines size of each sub-step in the simulation (chopping up MaxSimTime) |
| `MaxSimTime` | `float` | Maximum simulation time for the virtual projectile. |
| `OverrideGravityZ` | `float` | Optional override of Gravity (if 0, uses WorldGravityZ) |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if hit something along the path if tracing for collision. |

### `Blueprint_PredictProjectilePath_ByTraceChannel`

```text
Blueprint_PredictProjectilePath_ByTraceChannel(WorldContextObject: UObject *, OutHit: FHitResult &, OutPathPositions: TArray < FVector > &, OutLastTraceDestination: FVector &, StartPos: FVector, LaunchVelocity: FVector, bTracePath: bool, ProjectileRadius: float, TraceChannel: TEnumAsByte < ECollisionChannel >, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, DrawDebugTime: float, SimFrequency: float, MaxSimTime: float, OverrideGravityZ: float) -> bool
```

Predict the arc of a virtual projectile affected by gravity with collision checks along the arc. Returns a list of positions of the simulated arc and the destination reached by the simulation.
	 Returns true if it hit something (if tracing with collision).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `OutHit` | `FHitResult &` | Predicted hit result, if the projectile will hit something |
| `OutPathPositions` | `TArray < FVector > &` | Predicted projectile path. Ordered series of positions from StartPos to the end. Includes location at point of impact if it hit something. |
| `OutLastTraceDestination` | `FVector &` | Goal position of the final trace it did. Will not be in the path if there is a hit. |
| `StartPos` | `FVector` | First start trace location |
| `LaunchVelocity` | `FVector` | Velocity the "virtual projectile" is launched at |
| `bTracePath` | `bool` | Trace along the entire path to look for blocking hits |
| `ProjectileRadius` | `float` | Radius of the virtual projectile to sweep against the environment |
| `TraceChannel` | `TEnumAsByte < ECollisionChannel >` | TraceChannel to trace against, if bTracePath is true. |
| `bTraceComplex` | `bool` | Use TraceComplex (trace against triangles not primitives) |
| `ActorsToIgnore` | `TArray < AActor * > &` | Actors to exclude from the traces |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | Debug type (one-frame, duration, persistent) |
| `DrawDebugTime` | `float` | Duration of debug lines (only relevant for DrawDebugType::Duration) |
| `SimFrequency` | `float` | Determines size of each sub-step in the simulation (chopping up MaxSimTime) |
| `MaxSimTime` | `float` | Maximum simulation time for the virtual projectile. |
| `OverrideGravityZ` | `float` | Optional override of Gravity (if 0, uses WorldGravityZ) |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if hit something along the path (if tracing with collision). |

### `Blueprint_PredictProjectilePath_Advanced`

```text
Blueprint_PredictProjectilePath_Advanced(WorldContextObject: UObject *, PredictParams: FPredictProjectilePathParams &, PredictResult: FPredictProjectilePathResult &) -> bool
```

Predict the arc of a virtual projectile affected by gravity with collision checks along the arc.
	 Returns true if it hit something.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PredictParams` | `FPredictProjectilePathParams &` | Input params to the trace (start location, velocity, time to simulate, etc). |
| `PredictResult` | `FPredictProjectilePathResult &` | Output result of the trace (Hit result, array of locationvelocitytimes for each trace step, etc). |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if hit something along the path (if tracing with collision). |

### `SuggestProjectileVelocity_CustomArc`

```text
SuggestProjectileVelocity_CustomArc(WorldContextObject: UObject *, OutLaunchVelocity: FVector &, StartPos: FVector, EndPos: FVector, OverrideGravityZ: float, ArcParam: float) -> bool
```

Returns the launch velocity needed for a projectile at rest at StartPos to land on EndPos.
	 Assumes a medium arc (e.g. 45 deg on level ground). Projectile velocity is variable and unconstrained.
	 Does no tracing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `OutLaunchVelocity` | `FVector &` | Returns the launch velocity required to reach the EndPos |
| `StartPos` | `FVector` | Start position of the simulation |
| `EndPos` | `FVector` | Desired end location for the simulation |
| `OverrideGravityZ` | `float` | Optional override of WorldGravityZ |
| `ArcParam` | `float` | Change height of arc between 0.0-1.0 where 0.5 is the default medium arc |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetWorldOriginLocation`

```text
GetWorldOriginLocation(WorldContextObject: UObject *) -> FIntVector
```

获取世界原点位置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `FIntVector` | 世界原点 |

### `SetWorldOriginLocation`

```text
SetWorldOriginLocation(WorldContextObject: UObject *, NewLocation: FIntVector) -> void
```

设置世界原点位置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `NewLocation` | `FIntVector` | 世界原点 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWorldOriginLocationByLua`

```text
SetWorldOriginLocationByLua(WorldContextObject: UObject *, X: int32, Y: int32, Z: int32) -> void
```

设置世界原点位置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `X` | `int32` | - |
| `Y` | `int32` | - |
| `Z` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SyncSetNewWorldOrigin`

```text
SyncSetNewWorldOrigin(WorldContextObject: UObject *, X: int32, Y: int32, Z: int32) -> void
```

同步设置世界原点位置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `X` | `int32` | - |
| `Y` | `int32` | - |
| `Z` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RebaseLocalOriginOntoZero`

```text
RebaseLocalOriginOntoZero(WorldContextObject: UObject *, WorldLocation: FVector) -> FVector
```

返回基于原点坐标的local坐标

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `WorldLocation` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | origin based position |

### `RebaseZeroOriginOntoLocal`

```text
RebaseZeroOriginOntoLocal(WorldContextObject: UObject *, WorldLocation: FVector) -> FVector
```

返回local坐标基于原点的坐标

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `WorldLocation` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | local location |

### `GrassOverlappingSphereCount`

```text
GrassOverlappingSphereCount(WorldContextObject: UObject *, StaticMesh: UStaticMesh *, CenterPosition: FVector, Radius: float) -> int32
```

Counts how many grass foliage instances overlap a given sphere.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `StaticMesh` | `UStaticMesh *` | - |
| `CenterPosition` | `FVector` | The center position of the sphere. |
| `Radius` | `float` | The radius of the sphere. |

**Returns**

| Type | Description |
|---|---|
| `int32` | Number of foliage instances with their mesh set to Mesh that overlap the sphere. |

### `DeprojectScreenToWorld`

```text
DeprojectScreenToWorld(Player: APlayerController *, ScreenPosition: FVector2D &, WorldPosition: FVector &, WorldDirection: FVector &) -> bool
```

获取给定2D屏幕空间中的坐标投影到3D世界空间中的坐标

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `APlayerController *` | 玩家的PlayerController |
| `ScreenPosition` | `FVector2D &` | 屏幕空间中的坐标 |
| `WorldPosition` | `FVector &` | 输出的世界空间坐标 |
| `WorldDirection` | `FVector &` | 输出的方向向量，世界空间中，给定点远离相机方向的方向向量 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否转换成功 |

### `ProjectWorldToScreen`

```text
ProjectWorldToScreen(Player: APlayerController *, WorldPosition: FVector &, ScreenPosition: FVector2D &, bPlayerViewportRelative: bool) -> bool
```

获取给定3D世界空间中的坐标投影到2D屏幕空间中的坐标

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `APlayerController *` | 玩家的PlayerController |
| `WorldPosition` | `FVector &` | 世界空间中的坐标 |
| `ScreenPosition` | `FVector2D &` | 输出的屏幕空间坐标 |
| `bPlayerViewportRelative` | `bool` | 是否与玩家视口相关 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否转换成功 |

### `MarkNetPropertyDirtyFromName`

```text
MarkNetPropertyDirtyFromName(Object: UObject *, PropertyName: FName, LifetimeCondition: ELifetimeCondition) -> bool
```

Mark a particular net property of an UObject as dirty (for networking), thus it will be take into consideration in next replication

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | UObject to be marked dirty |
| `PropertyName` | `FName` | Name of the particular net property to be marked dirty |
| `LifetimeCondition` | `ELifetimeCondition` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetKeyValue`

```text
GetKeyValue(Pair: FString &, Key: FString &, Value: FString &) -> void
```

Break up a key=value pair into its key and value.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Pair` | `FString &` | The string containing a pair to split apart. |
| `Key` | `FString &` | (out) Key portion of Pair. If no = in string will be the same as Pair. |
| `Value` | `FString &` | (out) Value portion of Pair. If no = in string will be empty. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ParseOption`

```text
ParseOption(Options: FString, Key: FString &) -> FString
```

Find an option in the options string and return it.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Options` | `FString` | The string containing the options. |
| `Key` | `FString &` | The key to find the value of in Options. |

**Returns**

| Type | Description |
|---|---|
| `FString` | The value associated with Key if Key found in Options string. |

### `HasOption`

```text
HasOption(Options: FString, InKey: FString &) -> bool
```

Returns whether a key exists in an options string.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Options` | `FString` | The string containing the options. |
| `InKey` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether Key was found in Options. |

### `GetIntOption`

```text
GetIntOption(Options: FString &, Key: FString &, DefaultValue: int32) -> int32
```

Find an option in the options string and return it as an integer.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Options` | `FString &` | The string containing the options. |
| `Key` | `FString &` | The key to find the value of in Options. |
| `DefaultValue` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | The value associated with Key as an integer if Key found in Options string, otherwise DefaultValue. |

### `HasLaunchOption`

```text
HasLaunchOption(OptionToCheck: FString &) -> bool
```

Checks the commandline to see if the desired option was specified on the commandline (e.g. -demobuild)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OptionToCheck` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the launch option was specified on the commandline, false otherwise |

### `GetDeviceQualityLevel`

```text
GetDeviceQualityLevel() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetDeviceTCQualityGrade`

```text
GetDeviceTCQualityGrade() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetDeviceMemoryLevel`

```text
GetDeviceMemoryLevel() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetDeviceMemorySize`

```text
GetDeviceMemorySize() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `EnableObjArrayAutoResize`

```text
EnableObjArrayAutoResize(bEnabled: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetConsoleIntVariable`

```text
SetConsoleIntVariable(Name: FString &, Value: int32) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Name` | `FString &` | - |
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `UpdateComponentToWorld`

```text
UpdateComponentToWorld(ActorComponent: UActorComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActorComponent` | `UActorComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsLongScreen`

```text
IsLongScreen(WorldContextObject: UObject *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsWinReleaseBuild`

```text
IsWinReleaseBuild() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `RecordDSLaunchState`

```text
RecordDSLaunchState(state: int32) -> void
```

record ds launch state, collect for ds shutdown error report, add by czcheng

**Parameters**

| Name | Type | Description |
|---|---|---|
| `state` | `int32` | launch state, see details in EDSLaunchState |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RecordDSShutdownErrorInfo`

```text
RecordDSShutdownErrorInfo(ErrorCode: int32, ErrMsg: FString &) -> void
```

record ds shutdown error info, collect for ds shutdown error report, add by czcheng

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ErrorCode` | `int32` | shutdown error code, see details in EDSShutdownErrorCode |
| `ErrMsg` | `FString &` | error message |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
