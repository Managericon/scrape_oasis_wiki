---
id: "api-chunk:class:1"
title: "Oasis API class chunk 1"
source: "https://developer.gp.qq.com/api/"
category: "API Wiki/class"
kind: "api_chunk"
---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AActivityBaseActor.json -->

# AActivityBaseActor

可实现可交互物基础功能的Actor

## Inheritance

`AUAERegionActor` -> `IOwnBlackboardInterface` -> `IPlayerLogicInterface` -> `IRelativeMoveMgrInterface` -> `IDamageableInterface` -> `IActivityStateInterface` -> `IGameplayTaskOwnerInterface` -> `INetContainerterface` -> `IClientConditionInerterface` -> `IObjectPoolInterface` -> `IInteractorInterface` -> `IUnifiedInteractionInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OnActivityActorChangeState` | `FActivityChangeState` | 状态变化事件委托<br>	 @param LeaveState 离开的状态 名<br>	 @param EnterState 进入的状态名 |

## Functions

### `GetCurrentStateName`

```text
GetCurrentStateName() -> SHADOWTRACKEREXTRA_API FName
```

生效范围：SC
	  获取当前状态名

**Returns**

| Type | Description |
|---|---|
| `SHADOWTRACKEREXTRA_API FName` | 当前状态名 |

### `GetCurrentStateTime`

```text
GetCurrentStateTime() -> float
```

生效范围：SC
	  获取进入当前状态后所经过的时间

**Returns**

| Type | Description |
|---|---|
| `float` | 当前状态经过的时间 |

### `JumpToState`

```text
JumpToState(StateName: FName, EnterTime: float, bPause: bool) -> void
```

生效范围：S
	  跳转到指定状态

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StateName` | `FName` | 要跳转的状态名 |
| `EnterTime` | `float` | 进入状态的时间 |
| `bPause` | `bool` | 是否暂停 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Pause`

```text
Pause() -> void
```

生效范围：S
	  暂停当前状态的sequence的播放

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Resume`

```text
Resume() -> void
```

生效范围：S
	  恢复当前状态的sequence的播放

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CheckCurrentStateIsEntry`

```text
CheckCurrentStateIsEntry() -> bool
```

生效范围：SC
	  检查当前状态是否为状态机的入口状态

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否为入口状态 |

### `GetCurrentSequnceIsEnd`

```text
GetCurrentSequnceIsEnd() -> bool
```

生效范围：SC
	  检查当前sequence是否播放完毕

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否播放完毕 |

## Events

### `OnEnterState_BP`

```text
OnEnterState_BP(StateName: FName) -> void
```

进入某个状态触发

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StateName` | `FName` | 状态名 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPlayerAttachedToThisActor_BP`

```text
OnPlayerAttachedToThisActor_BP(Player: ASTExtraCharacter *) -> void
```

当角色Attach到这个Actor时触发

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `ASTExtraCharacter *` | Attach的角色 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPlayerBeforeAttachedToThisActor_BP`

```text
OnPlayerBeforeAttachedToThisActor_BP(Player: ASTExtraCharacter *) -> void
```

当角色Attach到这个Actor前触发

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `ASTExtraCharacter *` | Attach的角色 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPlayerDettachedToThisActor_BP`

```text
OnPlayerDettachedToThisActor_BP(Player: ASTExtraCharacter *) -> void
```

当角色从Actor上Detach时触发

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `ASTExtraCharacter *` | Detach的角色 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnPlayerAttachedDelegate`

```text
OnPlayerAttachedDelegate(Player: ASTExtraCharacter*) -> void
```

角色Attach事件委托

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `ASTExtraCharacter*` | Attach的角色 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPlayerDettachedDelegate`

```text
OnPlayerDettachedDelegate(Player: ASTExtraCharacter*) -> void
```

角色Detach事件委托

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `ASTExtraCharacter*` | Detach的角色 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AActor.json -->

# AActor

Actor is the base class for an Object that can be placed or spawned in a level.
  Actors may contain a collection of ActorComponents, which can be used to control how actors move, how they are rendered, etc.
  The other main function of an Actor is the replication of properties and function calls across the network during play.
 
  @see UActorComponent

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PrimaryActorTick` | `FActorTickFunction` | Primary Actor tick function, which calls TickActor().<br>	  Tick functions can be configured to control whether ticking is enabled, at what time during a frame the update occurs, and to set up tick dependencies.<br>	  @see AddTickPrerequisiteActor(), AddTickPrerequisiteComponent() |
| `CustomTimeDilation` | `float` | Allow each actor to run at a different time speed. The DeltaTime for a frame is multiplied by the global TimeDilation (in WorldSettings) and this CustomTimeDilation for this actor's tick. |
| `bAllowBPReceiveTickEvent` | `bool` | If true, bp tick will be called , otherwise skipped |
| `TickAdapterInterval` | `uint8` | - |
| `bTickAdapterRqrMainFrame` | `uint8` | - |
| `bEnableTickAdapter` | `uint8` | - |
| `bSupportSuspendTick` | `uint8` | - |
| `bEnableFirstTickGroup` | `uint8` | - |
| `bHidden` | `uint8` | Allows us to only see this Actor in the Editor, and not in the actual game.<br>	  @see SetActorHiddenInGame() |
| `bConsideredHidden` | `uint8` | - |
| `bNetTemporary` | `uint8` | If true, when the actor is spawned it will be sent to the client but receive no further replication updates from the server afterwards. |
| `bNetStartup` | `uint8` | If true, this actor was loaded directly from the map, and for networking purposes can be addressed by its full path name |
| `bOnlyRelevantToOwner` | `uint8` | If true, this actor is only relevant to its owner. If this flag is changed during play, all non-owner channels would need to be explicitly closed. |
| `bOwningSpecificNetConsideration` | `uint8` | If true, this actor is considered for replication in an owning-specific semantics. |
| `bRegionBasedNetConsideration` | `uint8` | If true, this actor is considered for replication in region-based semantics. |
| `bMRegionBasedNetConsideration` | `uint8` | If true, this actor is considered for replication in Mregion-based semantics. |
| `bMRegionStatic` | `uint8` | - |
| `bFastDistBasedNetRelevancy` | `uint8` | If true, this actor is checked for relevancy by fast distance-based calculation. |
| `bGroupBasedNetRelevancy` | `uint8` | If true, this actor is checked for relevancy by relevancy group first. |
| `bLazyNetReplication` | `uint8` | If true, this actor is only replicated by calling ForceNetUpdate. |
| `bClientSimulatedRelevancy` | `uint8` | NOTE: Mark "Client Simulated Relevancy" for ob  replay<br>	 @see SetActorSimulatedRelevancy()<br>	 @see OnActorSimulatedRelevant() |
| `bCheckAllRelyOnAttachment` | `uint8` | - |
| `bAlwaysRelevant` | `uint8` | Always relevant for network (overrides bOnlyRelevantToOwner). |
| `bForceOwnedMeshAlwaysRefreshBones` | `uint8` | - |
| `bTearOff` | `uint8` | If true, this actor is no longer replicated to new clients, and is "torn off" (becomes a ROLE_Authority) on clients to which it was being replicated.<br>	  @see TornOff() |
| `bExchangedRoles` | `uint8` | Whether we have already exchanged RoleRemoteRole on the client, as when removing then re-adding a streaming level.<br>	  Causes all initialization to be performed again even though the actor may not have actually been reloaded. |
| `bNetLoadOnClient` | `uint8` | This actor will be loaded on network clients during map load |
| `bNetUseOwnerRelevancy` | `uint8` | If actor has valid Owner, call Owner's IsNetRelevantFor and GetNetPriority |
| `bBlockInput` | `uint8` | If true, all input on the stack below this actor will not be considered |
| `bCanBeBaseForCharacter` | `uint8` | If true, all input on the stack below this actor will not be considered |
| `bAllowTickBeforeBeginPlay` | `uint8` | Whether we allow this Actor to tick before it receives the BeginPlay event.<br>	  Normally we don't tick actors until after BeginPlay; this setting allows this behavior to be overridden.<br>	  This Actor must be able to tick for this setting to be relevant. |
| `bCustomHandlingNetworkSubobjectDeletion` | `uint8` | - |
| `bReplicates` | `uint8` | If true, this actor will replicate to remote machines<br>	  @see SetReplicates() |
| `RemoteRole` | `TEnumAsByte < enum ENetRole >` | Describes how much control the remote machine has over the actor. |
| `Owner` | `AActor *` | Owner of this Actor, used primarily for replication (bNetUseOwnerRelevancy & bOnlyRelevantToOwner) and visibility (PrimitiveComponent bOwnerNoSee and bOnlyOwnerSee)<br>	  @see SetOwner(), GetOwner() |
| `bReplicateMovement` | `uint8` | If true, replicate movementlocation related properties.<br>	  Actor must also be set to replicate.<br>	  @see SetReplicates() |
| `bActorEnableCollision` | `uint8` | Enables any collision on this actor.<br>	  @see SetActorEnableCollision(), GetActorEnableCollision() |
| `bEnableDeferredConstructComponent` | `uint8` | - |
| `bUseSpawnReplicatedActorMaxFrameDelayFromConfig` | `uint8` | - |
| `PendingConstructComponents` | `TArray < FDeferedComponentUnit >` | - |
| `PreSCSComponentsBeforeDeferContruction` | `TArray < UActorComponent * >` | - |
| `AsyncReplicatedActorSpawnDistA` | `float` | - |
| `AsyncReplicatedActorSpawnDistB` | `float` | - |
| `SpawnReplicatedActorMaxFrameDelayFromConfig` | `int32` | - |
| `ScriptNetworkReplicatedPropertyWrapper` | `FScriptNetworkReplicatedPropertyWrapper` | - |
| `NetDriverName` | `FName` | Used to specify the net driver to replicate on (NAME_None \|\| NAME_GameNetDriver is the default net driver) |
| `ReplicatedMovement` | `FRepMovement` | Used for replication of our RootComponent's position and velocity |
| `InitialLifeSpan` | `float` | How long this Actor lives before dying, 0=forever. Note this is the INITIAL value and should not be modified once play has begun. |
| `AttachmentReplication` | `FRepAttachment` | Used for replicating attachment of this actor's RootComponent to another actor.<br>	  This is filled in via GatherCurrentMovement() when the RootComponent has an AttachParent. |
| `Role` | `TEnumAsByte < enum ENetRole >` | Describes how much control the local machine has over the actor. |
| `NetDormancy` | `TEnumAsByte < enum ENetDormancy >` | Dormancy setting for actor to take itself off of the replication list without being destroyed on clients. |
| `AutoReceiveInput` | `TEnumAsByte < EAutoReceiveInput :: Type >` | Automatically registers this actor to receive input from a player. |
| `InputPriority` | `int32` | The priority of this input component when pushed in to the stack. |
| `InputComponent` | `UInputComponent *` | Component that handles input for this actor, if input is enabled. |
| `NetCullDistanceSquared` | `float` | Square of the max distance from the client's viewpoint that this actor is relevant and will be replicated. |
| `NetCullFactorSquared` | `float` | NetCullDistanceSquared Factor for Connection |
| `OBRelevantFactor` | `float` | - |
| `NetTag` | `int32` | Internal - used by UWorld::ServerTickClients() |
| `NetConsiderFrequency` | `float` | How often (per second) this actor enters consider list, should be greater than or equal to NetUpdateFrequency |
| `NetUpdateFrequency` | `float` | How often (per second) this actor will be checked for replication, used to determine NetUpdateTime |
| `MinNetUpdateFrequency` | `float` | Used to determine what rate to throttle down to when replicated properties are changing infrequently |
| `NetUpdateJumpFrame` | `int32` | - |
| `NetPriority` | `float` | Priority for this actor when checking for replication in a low bandwidth or saturated situation, higher priority means it is more likely to replicate |
| `bAutoDestroyWhenFinished` | `uint8` | If true then destroy self when "finished", meaning all relevant components report that they are done and no timelines or timers are in flight. |
| `bCanBeDamaged` | `uint8` | Whether this actor can take damage. Must be true for damage events (e.g. ReceiveDamage()) to be called.<br>	  @see TakeDamage(), ReceiveDamage() |
| `bCanNotifyDamager` | `uint8` | Whether this actor can Notify damager. Must be true for notify damager events (PreDamageOther) to be called.<br>	  @see TakeDamage(), PreDamageOther() |
| `bRepParentUpdatePhx` | `uint8` | - |
| `bActorIsBeingDestroyed` | `uint8` | Set when actor is about to be deleted. |
| `bCollideWhenPlacing` | `uint8` | This actor collides with the world when placing in the editor, even if RootComponent collision is disabled. Does not affect spawning, @see SpawnCollisionHandlingMethod |
| `bFindCameraComponentWhenViewTarget` | `uint8` | If true, this actor should search for an owned camera component to view through when used as a view target. |
| `bRelevantForNetworkReplays` | `uint8` | If true, this actor will be replicated to network replays (default is true) |
| `bForcedRelevancyCheckForReplay` | `uint8` | - |
| `bLowUpdateRateForReplay` | `uint8` | - |
| `bGenerateOverlapEventsDuringLevelStreaming` | `uint8` | If true, this actor will generate overlap events when spawned as part of level streaming. You might enable this is in the case where a streaming level loads around an actor and you want overlaps to trigger. |
| `bCanCachedInWorldSpecialActorList` | `uint8` | - |
| `bShouldDumpCallstackWhenMovingfast` | `uint8` | - |
| `bCanBeInCluster` | `uint8` | If true, this actor can be put inside of a GC Cluster to improve Garbage Collection performance |
| `bAllowReceiveTickEventOnDedicatedServer` | `uint8` | If false, the Blueprint ReceiveTick() event will be disabled on dedicated servers.<br>	  @see AllowReceiveTickEventOnDedicatedServer() |
| `bActorSeamlessTraveled` | `uint8` | Indicates the actor was pulled through a seamless travel. |
| `bIgnoresOriginShifting` | `uint8` | Whether this actor should not be affected by world origin shifting. |
| `bEnableAutoLODGeneration` | `uint8` | If true, and if World setting has bEnableHierarchicalLOD equal to true, then it will generate LODActor from groups of clustered Actor |
| `SpawnCollisionHandlingMethod` | `ESpawnActorCollisionHandlingMethod` | Controls how to handle spawning this actor in a situation where it's colliding with something else. "Default" means AlwaysSpawn here. |
| `CollisionCheckMoveDisStep` | `float` | - |
| `CollisionCheckMoveDegreeStep` | `float` | - |
| `CollisionCheckCircleRadius` | `float` | - |
| `Instigator` | `APawn *` | Pawn responsible for damage caused by this actor. |
| `Children` | `TArray < AActor * >` | Array of Actors whose Owner is this actor |
| `RootComponent` | `USceneComponent *` | Collision primitive that defines the transform (location, rotation, scale) of this Actor. |
| `ControllingMatineeActors` | `TArray < AMatineeActor * >` | The matinee actors that control this actor. |
| `Layers` | `TArray < FName >` | Layer's the actor belongs to.  This is outside of the editoronly data to allow hiding of LD-specified layers at runtime for profiling. |
| `ParentComponent` | `TWeakObjectPtr < UChildActorComponent >` | The UChildActorComponent that owns this Actor. |
| `Tags` | `TArray < FName >` | Array of tags that can be used for grouping and categorizing. |
| `DynamicTags` | `TArray < FName >` | - |
| `BlueprintCreatedComponents` | `TArray < UActorComponent * >` | Array of ActorComponents that are created by blueprints and serialized per-instance. |
| `InstanceComponents` | `TArray < UActorComponent * >` | Array of ActorComponents that have been added by the user on a per-instance basis. |
| `BackupRestoreIdentifier` | `int64` | - |
| `NeedsBackupStates` | `uint8` | - |
| `bSkipNewDuplicateOwnedComponents` | `uint8` | If you call CreateComponentFromTemplate on an actor which already owns a component with the same name, problem comes out<br>	  Optimized version will return the existing component, but not duplicate a new one, in this case, setting this switch to true is necessary |
| `bCanBeNetContainer` | `uint8` | - |
| `bDonotAsSubActor` | `uint8` | - |
| `DeformEffectType` | `TEnumAsByte < enum EDeformEffectType >` | - |
| `bBlockLandscapeDeform` | `bool` | If this actor will block any overlap deform. |
| `bRemoveStaticChildActorComp` | `bool` | - |
| `InputConsumeOption_DEPRECATED` | `TEnumAsByte < enum EInputConsumeOptions >` | - |
| `ExportActorInLevel` | `bool` | 在编辑器获取level里面actor的位置和朝向, 通过命令行方式导出到一个lua表格. feishen, 20210406 |
| `PivotOffset` | `FVector` | Local space pivot offset for the actor |
| `ParentComponentActor_DEPRECATED` | `TWeakObjectPtr < AActor >` | The Actor that owns the UChildActorComponent that owns this Actor. |
| `GroupActor` | `AActor *` | The group this actor is a part of. |
| `SpriteScale` | `float` | The scale to apply to any billboard components in editor builds (happens in any WITH_EDITOR build, including non-cooked games). |
| `ActorLabel` | `FString` | The friendly name for this actor, displayed in the editor.  You should always use AActor::GetActorLabel() to access the actual label to display,<br>	  and call AActor::SetActorLabel() or FActorLabelUtilities::SetActorLabelUnique() to change the label.  Never set the label directly. |
| `FolderPath` | `FName` | The folder path of this actor in the world (empty=root,  separated) |
| `bActorLabelEditable` | `uint8` | - |
| `bHiddenEd` | `uint8` | Whether this actor is hidden within the editor viewport. |
| `bEditable` | `uint8` | Whether the actor can be manipulated by editor operations. |
| `bListedInSceneOutliner` | `uint8` | Whether this actor should be listed in the scene outliner. |
| `bIsEditorPreviewActor` | `uint8` | True if this actor is the preview actor dragged out of the content browser |
| `bHiddenEdLayer` | `uint8` | Whether this actor is hidden by the layer browser. |
| `bHiddenEdTemporary` | `uint8` | Whether this actor is temporarily hidden within the editor; used for showhideetc functionality wo dirtying the actor. |
| `bHiddenEdLevel` | `uint8` | Whether this actor is hidden by the level browser. |
| `bLockLocation` | `uint8` | If true, prevents the actor from being moved in the editor viewport. |
| `ReorganizationTags` | `FReorganizationTagsContainer` | Reorganization tags for Level Partition system |
| `HiddenEditorViews` | `uint64` | Bitflag to represent which views this actor is hidden in, via per-view layer visibility. |
| `bActorCoastline` | `uint8` | - |

## Functions

### `GetToString`

```text
GetToString() -> FString
```

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `SetForceOwnedMeshAlwaysRefreshBones`

```text
SetForceOwnedMeshAlwaysRefreshBones(bAlwaysRefreshBones: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bAlwaysRefreshBones` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_ReplicateMovement`

```text
OnRep_ReplicateMovement() -> void
```

Called on client when updated bReplicateMovement value is received for this actor.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `TearOff`

```text
TearOff() -> void
```

Networking - Server - TearOff this actor to stop replication to clients. Will set bTearOff to true.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_Role`

```text
OnRep_Role() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_RemoteRole`

```text
OnRep_RemoteRole() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_Hidden`

```text
OnRep_Hidden() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_TearOff`

```text
OnRep_TearOff() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_CanBeDamaged`

```text
OnRep_CanBeDamaged() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_Owner`

```text
OnRep_Owner() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `TickConstructComponentWithTime`

```text
TickConstructComponentWithTime(OneFrameConstructTimeMS: float, bCreateImmediately: bool) -> float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OneFrameConstructTimeMS` | `float` | - |
| `bCreateImmediately` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `CallSubObjectLuaOnRep`

```text
CallSubObjectLuaOnRep(InObject: UObject *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_ScriptNetworkReplicatedPropertyWrapper`

```text
OnRep_ScriptNetworkReplicatedPropertyWrapper() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerSendScriptNetworkRemoteContent`

```text
ServerSendScriptNetworkRemoteContent(Content: FScriptNetworkRemoteContent &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `FScriptNetworkRemoteContent &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerSendScriptNetworkRemoteContent_Unreliable`

```text
ServerSendScriptNetworkRemoteContent_Unreliable(Content: FScriptNetworkRemoteContent &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `FScriptNetworkRemoteContent &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientSendScriptNetworkRemoteContent`

```text
ClientSendScriptNetworkRemoteContent(Content: FScriptNetworkRemoteContent &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `FScriptNetworkRemoteContent &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientSendScriptNetworkRemoteContent_Unreliable`

```text
ClientSendScriptNetworkRemoteContent_Unreliable(Content: FScriptNetworkRemoteContent &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `FScriptNetworkRemoteContent &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveScriptNetworkRemoteContent`

```text
ReceiveScriptNetworkRemoteContent(Content: FScriptNetworkRemoteContent &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `FScriptNetworkRemoteContent &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetReplicates`

```text
SetReplicates(bInReplicates: bool) -> void
```

Set whether this actor replicates to network clients. When this actor is spawned on the server it will be sent to clients as well.
	  Properties flagged for replication will update on clients if they change on the server.
	  Internally changes the RemoteRole property and handles the cases where the actor needs to be added to the network actor list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInReplicates` | `bool` | Whether this Actor replicates to network clients. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetEncSceneActor`

```text
SetEncSceneActor(bInEncSceneActor: bool) -> void
```

Set whether this Actor is an encrypted scene Actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInEncSceneActor` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsEncSceneActor`

```text
IsEncSceneActor() -> bool
```

Get whether this Actor is an encrypted scene Actor

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetReplicateMovement`

```text
SetReplicateMovement(bInReplicateMovement: bool) -> void
```

Set whether this actor's movement replicates to network clients.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInReplicateMovement` | `bool` | Whether this Actor's movement replicates to clients. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLocalRole`

```text
GetLocalRole() -> ENetRole
```

Returns how much control the local machine has over this actor.

**Returns**

| Type | Description |
|---|---|
| `ENetRole` | - |

### `GetRemoteRole`

```text
GetRemoteRole() -> ENetRole
```

Returns how much control the remote machine has over this actor.

**Returns**

| Type | Description |
|---|---|
| `ENetRole` | - |

### `GetRole`

```text
GetRole() -> ENetRole
```

**Returns**

| Type | Description |
|---|---|
| `ENetRole` | - |

### `OnRep_AttachmentReplication`

```text
OnRep_AttachmentReplication() -> void
```

Called on client when updated AttachmentReplication value is received for this actor.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_Instigator`

```text
OnRep_Instigator() -> void
```

Called on clients when Instigator is replicated.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddDynamicTag`

```text
AddDynamicTag(Tag: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Tag` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveDynamicTag`

```text
RemoveDynamicTag(Tag: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Tag` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableInput`

```text
EnableInput(PlayerController: APlayerController *) -> void
```

Pushes this actor on to the stack of input being handled by a PlayerController.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `APlayerController *` | The PlayerController whose input events we want to receive. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableInput`

```text
DisableInput(PlayerController: APlayerController *) -> void
```

Removes this actor from the stack of input being handled by a PlayerController.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `APlayerController *` | The PlayerController whose input events we no longer want to receive. If null, this actor will stop receiving input from all PlayerControllers. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetInputAxisValue`

```text
GetInputAxisValue(InputAxisName: FName) -> float
```

Gets the value of the input axis if input is enabled for this actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InputAxisName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInputAxisKeyValue`

```text
GetInputAxisKeyValue(InputAxisKey: FKey) -> float
```

Gets the value of the input axis key if input is enabled for this actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InputAxisKey` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInputVectorAxisValue`

```text
GetInputVectorAxisValue(InputAxisKey: FKey) -> FVector
```

Gets the value of the input axis key if input is enabled for this actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InputAxisKey` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetInstigator`

```text
GetInstigator() -> APawn *
```

Returns the instigator for this actor, or NULL if there is none.

**Returns**

| Type | Description |
|---|---|
| `APawn *` | - |

### `GetInstigatorController`

```text
GetInstigatorController() -> AController *
```

Returns the instigator's controller for this actor, or NULL if there is none.

**Returns**

| Type | Description |
|---|---|
| `AController *` | - |

### `GetTransform`

```text
GetTransform() -> FTransform
```

Get the actor-to-world transform.

**Returns**

| Type | Description |
|---|---|
| `FTransform` | The transform that transforms from actor space to world space. |

### `K2_GetActorLocation`

```text
K2_GetActorLocation() -> FVector
```

Returns the location of the RootComponent of this Actor

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `K2_SetActorLocation`

```text
K2_SetActorLocation(NewLocation: FVector, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> bool
```

Move the Actor to the specified location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector` | The new location to move the Actor to. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | The hit result from the move if swept. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether the location was successfully set (if not swept), or whether movement occurred at all (if swept). |

### `K2_GetActorRotation`

```text
K2_GetActorRotation() -> FRotator
```

Returns rotation of the RootComponent of this Actor.

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `GetActorForwardVector`

```text
GetActorForwardVector() -> FVector
```

Get the forward (X) vector (length 1.0) from this Actor, in world space.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetActorUpVector`

```text
GetActorUpVector() -> FVector
```

Get the up (Z) vector (length 1.0) from this Actor, in world space.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetActorRightVector`

```text
GetActorRightVector() -> FVector
```

Get the right (Y) vector (length 1.0) from this Actor, in world space.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetActorBounds`

```text
GetActorBounds(bOnlyCollidingComponents: bool, Origin: FVector &, BoxExtent: FVector &) -> void
```

Returns the bounding box of all components that make up this Actor (excluding ChildActorComponents).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bOnlyCollidingComponents` | `bool` | If true, will only return the bounding box for components with collision enabled. |
| `Origin` | `FVector &` | - |
| `BoxExtent` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_GetRootComponent`

```text
K2_GetRootComponent() -> USceneComponent *
```

Returns the RootComponent of this Actor

**Returns**

| Type | Description |
|---|---|
| `USceneComponent *` | - |

### `GetVelocity`

```text
GetVelocity() -> FVector
```

Returns velocity (in cms (Unreal Unitssecond) of the rootcomponent if it is either using physics or has an associated MovementComponent

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `K2_SetActorRotation`

```text
K2_SetActorRotation(NewRotation: FRotator, bTeleportPhysics: bool) -> bool
```

Set the Actor's rotation instantly to the specified rotation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRotation` | `FRotator` | The new rotation for the Actor. |
| `bTeleportPhysics` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether the rotation was successfully set. |

### `K2_SetActorLocationAndRotation`

```text
K2_SetActorLocationAndRotation(NewLocation: FVector, NewRotation: FRotator, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> bool
```

Move the actor instantly to the specified location and rotation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector` | The new location to teleport the Actor to. |
| `NewRotation` | `FRotator` | The new rotation for the Actor. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | The hit result from the move if swept. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether the rotation was successfully set. |

### `SetActorScale3D`

```text
SetActorScale3D(NewScale3D: FVector) -> void
```

Set the Actor's world-space scale.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewScale3D` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetActorScale3D`

```text
GetActorScale3D() -> FVector
```

Returns the Actor's world-space scale.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetDistanceTo`

```text
GetDistanceTo(OtherActor: AActor *) -> float
```

Returns the distance from this Actor to OtherActor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OtherActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetSquaredDistanceTo`

```text
GetSquaredDistanceTo(OtherActor: AActor *) -> float
```

Returns the squared distance from this Actor to OtherActor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OtherActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetHorizontalDistanceTo`

```text
GetHorizontalDistanceTo(OtherActor: AActor *) -> float
```

Returns the distance from this Actor to OtherActor, ignoring Z.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OtherActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetVerticalDistanceTo`

```text
GetVerticalDistanceTo(OtherActor: AActor *) -> float
```

Returns the distance from this Actor to OtherActor, ignoring XY.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OtherActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetDotProductTo`

```text
GetDotProductTo(OtherActor: AActor *) -> float
```

Returns the dot product from this Actor to OtherActor. Returns -2.0 on failure. Returns 0.0 for coincidental actors.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OtherActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetHorizontalDotProductTo`

```text
GetHorizontalDotProductTo(OtherActor: AActor *) -> float
```

Returns the dot product from this Actor to OtherActor, ignoring Z. Returns -2.0 on failure. Returns 0.0 for coincidental actors.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OtherActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `K2_AddActorWorldOffset`

```text
K2_AddActorWorldOffset(DeltaLocation: FVector, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the location of this actor in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaLocation` | `FVector` | The change in location. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | The hit result from the move if swept. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddActorWorldRotation`

```text
K2_AddActorWorldRotation(DeltaRotation: FRotator, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the rotation of this actor in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaRotation` | `FRotator` | The change in rotation. |
| `bSweep` | `bool` | Whether to sweep to the target rotation (not currently supported for rotation). |
| `SweepHitResult` | `FHitResult &` | The hit result from the move if swept. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddActorWorldTransform`

```text
K2_AddActorWorldTransform(DeltaTransform: FTransform &, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the transform of this actor in world space. Scale is unchanged.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTransform` | `FTransform &` | - |
| `bSweep` | `bool` | - |
| `SweepHitResult` | `FHitResult &` | - |
| `bTeleport` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetActorTransform`

```text
K2_SetActorTransform(NewTransform: FTransform &, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> bool
```

Set the Actors transform to the specified one.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTransform` | `FTransform &` | The new transform. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | - |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `K2_AddActorLocalOffset`

```text
K2_AddActorLocalOffset(DeltaLocation: FVector, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the location of this component in its local reference frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaLocation` | `FVector` | - |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | - |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddActorLocalRotation`

```text
K2_AddActorLocalRotation(DeltaRotation: FRotator, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the rotation of this component in its local reference frame

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaRotation` | `FRotator` | The change in rotation in local space. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | - |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddActorLocalTransform`

```text
K2_AddActorLocalTransform(NewTransform: FTransform &, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the transform of this component in its local reference frame

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTransform` | `FTransform &` | The change in transform in local space. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | - |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetActorRelativeLocation`

```text
K2_SetActorRelativeLocation(NewRelativeLocation: FVector, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Set the actor's RootComponent to the specified relative location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRelativeLocation` | `FVector` | New relative location of the actor's root component |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | - |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetActorRelativeRotation`

```text
K2_SetActorRelativeRotation(NewRelativeRotation: FRotator, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Set the actor's RootComponent to the specified relative rotation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRelativeRotation` | `FRotator` | New relative rotation of the actor's root component |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | - |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetActorRelativeTransform`

```text
K2_SetActorRelativeTransform(NewRelativeTransform: FTransform &, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Set the actor's RootComponent to the specified relative transform

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRelativeTransform` | `FTransform &` | New relative transform of the actor's root component |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | - |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetActorRelativeScale3D`

```text
SetActorRelativeScale3D(NewRelativeScale: FVector) -> void
```

Set the actor's RootComponent to the specified relative scale 3d

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRelativeScale` | `FVector` | New scale to set the actor's RootComponent to |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetActorRelativeScale3D`

```text
GetActorRelativeScale3D() -> FVector
```

Return the actor's relative scale 3d

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SetActorHiddenInGame`

```text
SetActorHiddenInGame(bNewHidden: bool) -> void
```

Sets the actor to be hidden in the game

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewHidden` | `bool` | Whether or not to hide the actor and all its components |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetActorConsideredHidden`

```text
SetActorConsideredHidden(bNewHidden: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewHidden` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetActorSimulatedRelevancy`

```text
SetActorSimulatedRelevancy(bIsRelevant: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsRelevant` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnActorSimulatedRelevant`

```text
OnActorSimulatedRelevant(bIsRelevant: bool) -> void
```

NOTE : Callback of Check Actor Relevancy in Client for ob or replay

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsRelevant` | `bool` | : Whether or not relevant for replay view target |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetActorEnableCollision`

```text
SetActorEnableCollision(bNewActorEnableCollision: bool) -> void
```

Allows enablingdisabling collision for the whole actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewActorEnableCollision` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetActorEnableCollision`

```text
GetActorEnableCollision() -> bool
```

Get current state of collision for the whole actor

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `K2_DestroyActor`

```text
K2_DestroyActor() -> void
```

Destroy the actor

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HasAuthority`

```text
HasAuthority() -> bool
```

Returns whether this actor has network authority

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `AddComponent`

```text
AddComponent(TemplateName: FName, bManualAttachment: bool, RelativeTransform: FTransform &, ComponentTemplateContext: UObject *) -> UActorComponent *
```

Creates a new component and assigns ownership to the Actor this is
	  called for. Automatic attachment causes the first component created to
	  become the root, and all subsequent components to be attached under that
	  root. When bManualAttachment is set, automatic attachment is
	  skipped and it is up to the user to attach the resulting component (or
	  set it up as the root) themselves.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TemplateName` | `FName` | The name of the Component Template to use. |
| `bManualAttachment` | `bool` | Whether manual or automatic attachment is to be used |
| `RelativeTransform` | `FTransform &` | The relative transform between the new component and its attach parent (automatic only) |
| `ComponentTemplateContext` | `UObject *` | Optional UBlueprintGeneratedClass reference to use to find the template in. If null (or not a BPGC), component is sought in this Actor's class |

**Returns**

| Type | Description |
|---|---|
| `UActorComponent *` | - |

### `K2_DestroyComponent`

```text
K2_DestroyComponent(Component: UActorComponent *) -> void
```

DEPRECATED - Use Component::DestroyComponent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UActorComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AttachRootComponentTo`

```text
K2_AttachRootComponentTo(InParent: USceneComponent *, InSocketName: FName, AttachLocationType: EAttachLocation :: Type, bWeldSimulatedBodies: bool) -> void
```

Attaches the RootComponent of this Actor to the supplied component, optionally at a named socket. It is not valid to call this on components that are not Registered.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InParent` | `USceneComponent *` | - |
| `InSocketName` | `FName` | - |
| `AttachLocationType` | `EAttachLocation :: Type` | Type of attachment, AbsoluteWorld to keep its world position, RelativeOffset to keep the object's relative offset and SnapTo to snap to the new parent. |
| `bWeldSimulatedBodies` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AttachToComponent`

```text
K2_AttachToComponent(Parent: USceneComponent *, SocketName: FName, LocationRule: EAttachmentRule, RotationRule: EAttachmentRule, ScaleRule: EAttachmentRule, bWeldSimulatedBodies: bool) -> void
```

Attaches the RootComponent of this Actor to the supplied component, optionally at a named socket. It is not valid to call this on components that are not Registered.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Parent` | `USceneComponent *` | Parent to attach to. |
| `SocketName` | `FName` | Optional socket to attach to on the parent. |
| `LocationRule` | `EAttachmentRule` | - |
| `RotationRule` | `EAttachmentRule` | - |
| `ScaleRule` | `EAttachmentRule` | - |
| `bWeldSimulatedBodies` | `bool` | Whether to weld together simulated physics bodies. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AttachRootComponentToActor`

```text
K2_AttachRootComponentToActor(InParentActor: AActor *, InSocketName: FName, AttachLocationType: EAttachLocation :: Type, bWeldSimulatedBodies: bool) -> void
```

Attaches the RootComponent of this Actor to the supplied component, optionally at a named socket. It is not valid to call this on components that are not Registered.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InParentActor` | `AActor *` | - |
| `InSocketName` | `FName` | - |
| `AttachLocationType` | `EAttachLocation :: Type` | Type of attachment, AbsoluteWorld to keep its world position, RelativeOffset to keep the object's relative offset and SnapTo to snap to the new parent. |
| `bWeldSimulatedBodies` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AttachToActor`

```text
K2_AttachToActor(ParentActor: AActor *, SocketName: FName, LocationRule: EAttachmentRule, RotationRule: EAttachmentRule, ScaleRule: EAttachmentRule, bWeldSimulatedBodies: bool) -> void
```

Attaches the RootComponent of this Actor to the supplied component, optionally at a named socket. It is not valid to call this on components that are not Registered.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParentActor` | `AActor *` | Actor to attach this actor's RootComponent to |
| `SocketName` | `FName` | Socket name to attach to, if any |
| `LocationRule` | `EAttachmentRule` | How to handle translation when attaching. |
| `RotationRule` | `EAttachmentRule` | How to handle rotation when attaching. |
| `ScaleRule` | `EAttachmentRule` | How to handle scale when attaching. |
| `bWeldSimulatedBodies` | `bool` | Whether to weld together simulated physics bodies. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SnapRootComponentTo`

```text
SnapRootComponentTo(InParentActor: AActor *, InSocketName: FName) -> void
```

Snap the RootComponent of this Actor to the supplied Actor's root component, optionally at a named socket. It is not valid to call this on components that are not Registered.
	   If InSocketName == NAME_None, it will attach to origin of the InParentActor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InParentActor` | `AActor *` | - |
| `InSocketName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DetachRootComponentFromParent`

```text
DetachRootComponentFromParent(bMaintainWorldPosition: bool) -> void
```

Detaches the RootComponent of this Actor from any SceneComponent it is currently attached to.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bMaintainWorldPosition` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DetachFromActor`

```text
K2_DetachFromActor(LocationRule: EDetachmentRule, RotationRule: EDetachmentRule, ScaleRule: EDetachmentRule) -> void
```

Detaches the RootComponent of this Actor from any SceneComponent it is currently attached to.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LocationRule` | `EDetachmentRule` | How to handle translation when detaching. |
| `RotationRule` | `EDetachmentRule` | How to handle rotation when detaching. |
| `ScaleRule` | `EDetachmentRule` | How to handle scale when detaching. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ActorHasTag`

```text
ActorHasTag(Tag: FName) -> bool
```

See if this actor contains the supplied tag

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Tag` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetActorTimeDilation`

```text
GetActorTimeDilation() -> float
```

Get CustomTimeDilation - this can be used for input control or speed control for slomo.
	  We don't want to scale input globally because input can be used for UI, which do not care for TimeDilation.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `AddTickPrerequisiteActor`

```text
AddTickPrerequisiteActor(PrerequisiteActor: AActor *) -> void
```

Make this actor tick after PrerequisiteActor. This only applies to this actor's tick function; dependencies for owned components must be set up separately if desired.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PrerequisiteActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddTickPrerequisiteComponent`

```text
AddTickPrerequisiteComponent(PrerequisiteComponent: UActorComponent *) -> void
```

Make this actor tick after PrerequisiteComponent. This only applies to this actor's tick function; dependencies for owned components must be set up separately if desired.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PrerequisiteComponent` | `UActorComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveTickPrerequisiteActor`

```text
RemoveTickPrerequisiteActor(PrerequisiteActor: AActor *) -> void
```

Remove tick dependency on PrerequisiteActor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PrerequisiteActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTickableWhenPaused`

```text
GetTickableWhenPaused() -> bool
```

Gets whether this actor can tick when paused.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `RemoveTickPrerequisiteComponent`

```text
RemoveTickPrerequisiteComponent(PrerequisiteComponent: UActorComponent *) -> void
```

Remove tick dependency on PrerequisiteComponent.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PrerequisiteComponent` | `UActorComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTickableWhenPaused`

```text
SetTickableWhenPaused(bTickableWhenPaused: bool) -> void
```

Sets whether this actor can tick when paused.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bTickableWhenPaused` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MakeMIDForMaterial`

```text
MakeMIDForMaterial(Parent: UMaterialInterface *) -> UMaterialInstanceDynamic *
```

Allocate a MID for a given parent material.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Parent` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | - |

### `GetGameTimeSinceCreation`

```text
GetGameTimeSinceCreation() -> float
```

The number of seconds (in game time) since this Actor was created, relative to Get Game Time In Seconds.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `MakeNoise`

```text
MakeNoise(Loudness: float, NoiseInstigator: APawn *, NoiseLocation: FVector, MaxRange: float, Tag: FName) -> void
```

Trigger a noise caused by a given Pawn, at a given location.
	  Note that the NoiseInstigator Pawn MUST have a PawnNoiseEmitterComponent for the noise to be detected by a PawnSensingComponent.
	  Senders of MakeNoise should have an Instigator if they are not pawns, or pass a NoiseInstigator.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Loudness` | `float` | The relative loudness of this noise. Usual range is 0 (no noise) to 1 (full volume). If MaxRange is used, this scales the max range, otherwise it affects the hearing range specified by the sensor. |
| `NoiseInstigator` | `APawn *` | Pawn responsible for this noise. Uses the actor's Instigator if NoiseInstigator=NULL |
| `NoiseLocation` | `FVector` | Position of noise source. If zero vector, use the actor's location. |
| `MaxRange` | `float` | Max range at which the sound may be heard. A value of 0 indicates no max range (though perception may have its own range). Loudness scales the range. (Note: not supported for legacy PawnSensingComponent, only for AIPerception) |
| `Tag` | `FName` | Identifier for the noise. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveBeginPlay`

```text
ReceiveBeginPlay() -> void
```

Event when play begins for this actor.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveReInitForReplay`

```text
ReceiveReInitForReplay() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveFastForwardFinishedForReplay`

```text
ReceiveFastForwardFinishedForReplay() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveActorSimulatedRelevant`

```text
ReceiveActorSimulatedRelevant(bIsRelevant: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsRelevant` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsActorBeingDestroyed`

```text
IsActorBeingDestroyed() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ReceiveAnyDamage`

```text
ReceiveAnyDamage(Damage: float, DamageType: UDamageType *, InstigatedBy: AController *, DamageCauser: AActor *) -> void
```

Event when this actor takes ANY damage

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Damage` | `float` | - |
| `DamageType` | `UDamageType *` | - |
| `InstigatedBy` | `AController *` | - |
| `DamageCauser` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveRadialDamage`

```text
ReceiveRadialDamage(DamageReceived: float, DamageType: UDamageType *, Origin: FVector, HitInfo: FHitResult &, InstigatedBy: AController *, DamageCauser: AActor *) -> void
```

Event when this actor takes RADIAL damage

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DamageReceived` | `float` | - |
| `DamageType` | `UDamageType *` | - |
| `Origin` | `FVector` | - |
| `HitInfo` | `FHitResult &` | - |
| `InstigatedBy` | `AController *` | - |
| `DamageCauser` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceivePointDamage`

```text
ReceivePointDamage(Damage: float, DamageType: UDamageType *, HitLocation: FVector, HitNormal: FVector, HitComponent: UPrimitiveComponent *, BoneName: FName, ShotFromDirection: FVector, InstigatedBy: AController *, DamageCauser: AActor *, HitInfo: FHitResult &) -> void
```

Event when this actor takes POINT damage

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Damage` | `float` | - |
| `DamageType` | `UDamageType *` | - |
| `HitLocation` | `FVector` | - |
| `HitNormal` | `FVector` | - |
| `HitComponent` | `UPrimitiveComponent *` | - |
| `BoneName` | `FName` | - |
| `ShotFromDirection` | `FVector` | - |
| `InstigatedBy` | `AController *` | - |
| `DamageCauser` | `AActor *` | - |
| `HitInfo` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveTick`

```text
ReceiveTick(DeltaSeconds: float) -> void
```

Event called every frame

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveActorBeginOverlap`

```text
ReceiveActorBeginOverlap(OtherActor: AActor *) -> void
```

Event when this actor overlaps another actor, for example a player walking into a trigger.
	 	For events when objects have a blocking collision, for example a player hitting a wall, see 'Hit' events.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OtherActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveActorEndOverlap`

```text
ReceiveActorEndOverlap(OtherActor: AActor *) -> void
```

Event when an actor no longer overlaps another actor, and they have separated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OtherActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveActorBeginCursorOver`

```text
ReceiveActorBeginCursorOver() -> void
```

Event when this actor has the mouse moved over it with the clickable interface.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveActorEndCursorOver`

```text
ReceiveActorEndCursorOver() -> void
```

Event when this actor has the mouse moved off of it with the clickable interface.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveActorOnClicked`

```text
ReceiveActorOnClicked(ButtonPressed: FKey) -> void
```

Event when this actor is clicked by the mouse when using the clickable interface.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ButtonPressed` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveActorOnReleased`

```text
ReceiveActorOnReleased(ButtonReleased: FKey) -> void
```

Event when this actor is under the mouse when left mouse button is released while using the clickable interface.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ButtonReleased` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveActorOnInputTouchBegin`

```text
ReceiveActorOnInputTouchBegin(FingerIndex: ETouchIndex :: Type) -> void
```

Event when this actor is touched when click events are enabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveActorOnInputTouchEnd`

```text
ReceiveActorOnInputTouchEnd(FingerIndex: ETouchIndex :: Type) -> void
```

Event when this actor is under the finger when untouched when click events are enabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveActorOnInputTouchEnter`

```text
ReceiveActorOnInputTouchEnter(FingerIndex: ETouchIndex :: Type) -> void
```

Event when this actor has a finger moved over it with the clickable interface.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveActorOnInputTouchLeave`

```text
ReceiveActorOnInputTouchLeave(FingerIndex: ETouchIndex :: Type) -> void
```

Event when this actor has a finger moved off of it with the clickable interface.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOverlappingActors`

```text
GetOverlappingActors(OverlappingActors: TArray < AActor * > &, ClassFilter: TSubclassOf < AActor >) -> void
```

Returns list of actors this actor is overlapping (any component overlapping any component). Does not return itself.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OverlappingActors` | `TArray < AActor * > &` | [out] Returned list of overlapping actors |
| `ClassFilter` | `TSubclassOf < AActor >` | [optional] If set, only returns actors of this class or subclasses |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOverlappingComponents`

```text
GetOverlappingComponents(OverlappingComponents: TArray < UPrimitiveComponent * > &) -> void
```

Returns list of components this actor is overlapping.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OverlappingComponents` | `TArray < UPrimitiveComponent * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveHit`

```text
ReceiveHit(MyComp: UPrimitiveComponent *, Other: AActor *, OtherComp: UPrimitiveComponent *, bSelfMoved: bool, HitLocation: FVector, HitNormal: FVector, NormalImpulse: FVector, Hit: FHitResult &) -> void
```

Event when this actor bumps into a blocking object, or blocks another actor that bumps into it.
	  This could happen due to things like Character movement, using Set Location with 'sweep' enabled, or physics simulation.
	  For events when objects overlap (e.g. walking into a trigger) see the 'Overlap' event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyComp` | `UPrimitiveComponent *` | - |
| `Other` | `AActor *` | - |
| `OtherComp` | `UPrimitiveComponent *` | - |
| `bSelfMoved` | `bool` | - |
| `HitLocation` | `FVector` | - |
| `HitNormal` | `FVector` | - |
| `NormalImpulse` | `FVector` | - |
| `Hit` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLifeSpan`

```text
SetLifeSpan(InLifespan: float) -> void
```

Set the lifespan of this actor. When it expires the object will be destroyed. If requested lifespan is 0, the timer is cleared and the actor will not be destroyed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InLifespan` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLifeSpan`

```text
GetLifeSpan() -> float
```

Get the remaining lifespan of this actor. If zero is returned the actor lives forever.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `UserConstructionScript`

```text
UserConstructionScript() -> void
```

Construction script, the place to spawn components and do other setup.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveDestroyed`

```text
ReceiveDestroyed() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveEndPlay`

```text
ReceiveEndPlay(EndPlayReason: EEndPlayReason :: Type) -> void
```

Event to notify blueprints this actor is about to be deleted.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EndPlayReason` | `EEndPlayReason :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetActorTickEnabled`

```text
SetActorTickEnabled(bEnabled: bool) -> void
```

Set this actor's tick functions to be enabled or disabled. Only has an effect if the function is registered
	  This only modifies the tick function on actor itself

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnabled` | `bool` | Whether it should be enabled or not |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsActorTickEnabled`

```text
IsActorTickEnabled() -> bool
```

Returns whether this actor has tick enabled or not

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetActorTickInterval`

```text
SetActorTickInterval(TickInterval: float) -> void
```

Sets the tick interval of this actor's primary tick function. Will not enable a disabled tick function. Takes effect on next tick.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TickInterval` | `float` | The rate at which this actor should be ticking |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetActorTickInterval`

```text
GetActorTickInterval() -> float
```

Returns the tick interval of this actor's primary tick function

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `OnRep_ReplicatedMovement`

```text
OnRep_ReplicatedMovement() -> void
```

ReplicatedMovement struct replication event

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOwner`

```text
SetOwner(NewOwner: AActor *) -> void
```

Set the owner of this Actor, used primarily for network replication.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewOwner` | `AActor *` | The Actor whom takes over ownership of this Actor |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOwner`

```text
GetOwner() -> AActor *
```

Get the owner of this Actor, used primarily for network replication.

**Returns**

| Type | Description |
|---|---|
| `AActor *` | Actor that owns this Actor |

### `IsOverlappingActor`

```text
IsOverlappingActor(Other: AActor *) -> bool
```

Check whether any component of this Actor is overlapping any component of another Actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Other` | `AActor *` | The other Actor to test against |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether any component of this Actor is overlapping any component of another Actor. |

### `SetNetDormancy`

```text
SetNetDormancy(NewDormancy: ENetDormancy) -> void
```

Puts actor in dormant networking state

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewDormancy` | `ENetDormancy` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FlushNetDormancy`

```text
FlushNetDormancy() -> void
```

Forces dormant actor to replicate but doesn't change NetDormancy state (i.e., they will go dormant again if left dormant)

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsChildActor`

```text
IsChildActor() -> bool
```

Returns whether this Actor was spawned by a child actor component

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetAllChildActors`

```text
GetAllChildActors(ChildActors: TArray < AActor * > &, bIncludeDescendants: bool) -> void
```

Returns a list of all child actors, including children of children

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ChildActors` | `TArray < AActor * > &` | - |
| `bIncludeDescendants` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetParentComponent`

```text
GetParentComponent() -> UChildActorComponent *
```

If this Actor was created by a Child Actor Component returns that Child Actor Component

**Returns**

| Type | Description |
|---|---|
| `UChildActorComponent *` | - |

### `GetParentActor`

```text
GetParentActor() -> AActor *
```

If this Actor was created by a Child Actor Component returns the Actor that owns that Child Actor Component

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `K2_TeleportTo`

```text
K2_TeleportTo(DestLocation: FVector, DestRotation: FRotator) -> bool
```

Teleport this actor to a new location. If the actor doesn't fit exactly at the location specified, tries to slightly move it out of walls and such.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DestLocation` | `FVector` | The target destination point |
| `DestRotation` | `FRotator` | The target rotation at the destination |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the actor has been successfully moved, or false if it couldn't fit. |

### `GetLevelName`

```text
GetLevelName() -> FString
```

Return the ULevel name that this Actor is part of.

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetAttachParentActor`

```text
GetAttachParentActor() -> AActor *
```

Walk up the attachment chain from RootComponent until we encounter a different actor, and return it. If we are not attached to a component in a different actor, returns NULL

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `GetAttachParentSocketName`

```text
GetAttachParentSocketName() -> FName
```

Walk up the attachment chain from RootComponent until we encounter a different actor, and return the socket name in the component. If we are not attached to a component in a different actor, returns NAME_None

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `GetAttachedActors`

```text
GetAttachedActors(OutActors: TArray < AActor * > &) -> void
```

Find all Actors which are attached directly to a component in this actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutActors` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTickGroup`

```text
SetTickGroup(NewTickGroup: ETickingGroup) -> void
```

Sets the ticking group for this actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTickGroup` | `ETickingGroup` | the new value to assign |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanBeBaseForCharacter`

```text
CanBeBaseForCharacter(Pawn: APawn *) -> bool
```

Return true if the given Pawn can be "based" on this actor (ie walk on it).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Pawn` | `APawn *` | - The pawn that wants to be based on this actor |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetAnimNotifyStateBoneRetargetAdaptInfoObj`

```text
GetAnimNotifyStateBoneRetargetAdaptInfoObj() -> UAnimNotifyStateBoneRetargetAdaptInfoObj *
```

**Returns**

| Type | Description |
|---|---|
| `UAnimNotifyStateBoneRetargetAdaptInfoObj *` | - |

### `TryGetBoneRetargetObj`

```text
TryGetBoneRetargetObj(InSourceObj: UObject *) -> UObject *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSourceObj` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

### `TryGetBoneRetargetObjForNotifyState`

```text
TryGetBoneRetargetObjForNotifyState(InTargetNotifyState: UObject *) -> UObject *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetNotifyState` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

### `InitAnimNotifyStateBoneRetargetInfo`

```text
InitAnimNotifyStateBoneRetargetInfo(InTargetNotifyState: UObject *, InBoneRetargetObj: UObject *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetNotifyState` | `UObject *` | - |
| `InBoneRetargetObj` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearAnimNotifyStateBoneRetargetAdaptState`

```text
ClearAnimNotifyStateBoneRetargetAdaptState(InTargetNotifyState: UObject *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetNotifyState` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsAnimNotifyStateBoneRetargetAdaptInitDone`

```text
IsAnimNotifyStateBoneRetargetAdaptInitDone(InTargetNotifyState: UObject *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetNotifyState` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `OverrideNotifyAttachMesh`

```text
OverrideNotifyAttachMesh(InTargetNotifyState: UObject *, InTargetSkelMeshComp: USkeletalMeshComponent *, HasRetarget: bool, IgnoreNewFPPState: bool) -> USkeletalMeshComponent *
```

For Bone Retarget Feature End

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetNotifyState` | `UObject *` | - |
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |
| `HasRetarget` | `bool` | - |
| `IgnoreNewFPPState` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `USkeletalMeshComponent *` | - |

### `K2_OnBecomeViewTarget`

```text
K2_OnBecomeViewTarget(PC: APlayerController *) -> void
```

Event called when this Actor becomes the view target for the given PlayerController.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PC` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_OnEndViewTarget`

```text
K2_OnEndViewTarget(PC: APlayerController *) -> void
```

Event called when this Actor is no longer the view target for the given PlayerController.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PC` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_OnReset`

```text
K2_OnReset() -> void
```

Event called when this Actor is reset to its initial state - used when restarting level without reloading.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `WasRecentlyRendered`

```text
WasRecentlyRendered(Tolerance: float) -> bool
```

Returns true if this actor has been rendered "recently", with a tolerance in seconds to define what "recent" means.
	  e.g.: If a tolerance of 0.1 is used, this function will return true only if the actor was rendered in the last 0.1 seconds of game time.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Tolerance` | `float` | How many seconds ago the actor last render time can be and still count as having been "recently" rendered. |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether this actor was recently rendered. |

### `ForceNetRelevant`

```text
ForceNetRelevant() -> void
```

Forces this actor to be net relevant if it is not already by default

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ForceNetConsider`

```text
ForceNetConsider() -> void
```

Force actor enter consider list

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ForceNetComponentUpdate`

```text
ForceNetComponentUpdate(InComponent: UActorComponent *) -> void
```

Force actor's component to be updated to client

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InComponent` | `UActorComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ForceNetUpdate`

```text
ForceNetUpdate() -> void
```

Force actor to be updated to clients

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PrestreamTextures`

```text
PrestreamTextures(Seconds: float, bEnableStreaming: bool, CinematicTextureGroups: int32) -> void
```

Calls PrestreamTextures() for all the actor's meshcomponents.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Seconds` | `float` | - Number of seconds to force all mip-levels to be resident |
| `bEnableStreaming` | `bool` | - Whether to start (true) or stop (false) streaming |
| `CinematicTextureGroups` | `int32` | - Bitfield indicating which texture groups that use extra high-resolution mips |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTextureForceResidentFlag`

```text
SetTextureForceResidentFlag(bForceMiplevelsToBeResident: bool) -> void
```

Calls SetTextureForceResidentFlag() for all the actor's meshcomponents.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bForceMiplevelsToBeResident` | `bool` | Whether textures should be forced to be resident or not. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetActorEyesViewPoint`

```text
GetActorEyesViewPoint(OutLocation: FVector &, OutRotation: FRotator &) -> void
```

Returns the point of view of the actor.
	  Note that this doesn't mean the camera, but the 'eyes' of the actor.
	  For example, for a Pawn, this would define the eye height location,
	  and view rotation (which is different from the pawn rotation which has a zeroed pitch component).
	  A camera first person view will typically use this view point. Most traces (weapon, AI) will be done from this view point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutLocation` | `FVector &` | - location of view point |
| `OutRotation` | `FRotator &` | - view rotation of actor. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetComponentByClass`

```text
GetComponentByClass(ComponentClass: TSubclassOf < UActorComponent >) -> UActorComponent *
```

Script exposed version of FindComponentByClass

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ComponentClass` | `TSubclassOf < UActorComponent >` | - |

**Returns**

| Type | Description |
|---|---|
| `UActorComponent *` | - |

### `GetComponentsByClass`

```text
GetComponentsByClass(ComponentClass: TSubclassOf < UActorComponent >) -> TArray < UActorComponent * >
```

Gets all the components that inherit from the given class.
	Currently returns an array of UActorComponent which must be cast to the correct type.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ComponentClass` | `TSubclassOf < UActorComponent >` | - |

**Returns**

| Type | Description |
|---|---|
| `TArray < UActorComponent * >` | - |

### `GetComponentsByTag`

```text
GetComponentsByTag(ComponentClass: TSubclassOf < UActorComponent >, Tag: FName) -> TArray < UActorComponent * >
```

Gets all the components that inherit from the given class with a given tag.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ComponentClass` | `TSubclassOf < UActorComponent >` | - |
| `Tag` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `TArray < UActorComponent * >` | - |

### `SetGeneralCampID`

```text
SetGeneralCampID(InCampID: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCampID` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetGeneralCampID`

```text
GetGeneralCampID() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetGeneralCampName`

```text
GetGeneralCampName() -> FString
```

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetGeneralCampRelationWithCampID`

```text
GetGeneralCampRelationWithCampID(CampID: int32) -> ECampRelation
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CampID` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `ECampRelation` | - |

### `GetGeneralCampRelationWithActor`

```text
GetGeneralCampRelationWithActor(Actor: AActor *) -> ECampRelation
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `ECampRelation` | - |

### `AllowTriggerDeformEffect`

```text
AllowTriggerDeformEffect(Origin: FVector &, EffectRange: float) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Origin` | `FVector &` | - |
| `EffectRange` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `TriggerDeformEffect`

```text
TriggerDeformEffect(Origin: FVector &, EffectRange: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Origin` | `FVector &` | - |
| `EffectRange` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableDeformEffect`

```text
DisableDeformEffect() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MarkSubObjectDeleteDirty`

```text
MarkSubObjectDeleteDirty(SubObject: UObject *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsHiddenEdAtStartup`

```text
IsHiddenEdAtStartup() -> bool
```

Simple accessor to check if the actor is hidden upon editor startup

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the actor is hidden upon editor startup; false if it is not |

### `IsHiddenEd`

```text
IsHiddenEd() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetIsTemporarilyHiddenInEditor`

```text
SetIsTemporarilyHiddenInEditor(bIsHidden: bool) -> void
```

Sets whether or not this actor is hidden in the editor for the duration of the current editor session

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsHidden` | `bool` | True if the actor is hidden |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsTemporarilyHiddenInEditor`

```text
IsTemporarilyHiddenInEditor(bIncludeParent: bool) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIncludeParent` | `bool` | - Whether to recurse up child actor hierarchy or not |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether or not this actor is hidden in the editor for the duration of the current editor session |

### `IsEditable`

```text
IsEditable() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | Returns true if this actor is allowed to be displayed, selected and manipulated by the editor. |

### `IsSelectable`

```text
IsSelectable() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | Returns true if this actor can EVER be selected in a level in the editor.  Can be overridden by specific actors to make them unselectable. |

## Delegates

### `OnTakeAnyDamage`

```text
OnTakeAnyDamage(DamagedActor: AActor*, Damage: float, DamageType: const class UDamageType*, InstigatedBy: AController*, DamageCauser: AActor*) -> void
```

Called when the actor is damaged in any way.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DamagedActor` | `AActor*` | - |
| `Damage` | `float` | - |
| `DamageType` | `const class UDamageType*` | - |
| `InstigatedBy` | `AController*` | - |
| `DamageCauser` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTakePointDamage`

```text
OnTakePointDamage(DamagedActor: AActor*, Damage: float, InstigatedBy: AController*, HitLocation: FVector, FHitComponent: UPrimitiveComponent*, BoneName: FName, ShotFromDirection: FVector, DamageType: const class UDamageType*, DamageCauser: AActor*) -> void
```

Called when the actor is damaged by point damage.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DamagedActor` | `AActor*` | - |
| `Damage` | `float` | - |
| `InstigatedBy` | `AController*` | - |
| `HitLocation` | `FVector` | - |
| `FHitComponent` | `UPrimitiveComponent*` | - |
| `BoneName` | `FName` | - |
| `ShotFromDirection` | `FVector` | - |
| `DamageType` | `const class UDamageType*` | - |
| `DamageCauser` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnActorBeginOverlap`

```text
OnActorBeginOverlap(OverlappedActor: AActor*, OtherActor: AActor*) -> void
```

Called when another actor begins to overlap this actor, for example a player walking into a trigger.
	 	For events when objects have a blocking collision, for example a player hitting a wall, see 'Hit' events.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OverlappedActor` | `AActor*` | - |
| `OtherActor` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnActorEndOverlap`

```text
OnActorEndOverlap(OverlappedActor: AActor*, OtherActor: AActor*) -> void
```

Called when another actor stops overlapping this actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OverlappedActor` | `AActor*` | - |
| `OtherActor` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnBeginCursorOver`

```text
OnBeginCursorOver(TouchedActor: AActor*) -> void
```

Called when the mouse cursor is moved over this actor if mouse over events are enabled in the player controller.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TouchedActor` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnEndCursorOver`

```text
OnEndCursorOver(TouchedActor: AActor*) -> void
```

Called when the mouse cursor is moved off this actor if mouse over events are enabled in the player controller.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TouchedActor` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnClicked`

```text
OnClicked(TouchedActor: AActor*, ButtonPressed: FKey) -> void
```

Called when the left mouse button is clicked while the mouse is over this actor and click events are enabled in the player controller.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TouchedActor` | `AActor*` | - |
| `ButtonPressed` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnReleased`

```text
OnReleased(TouchedActor: AActor*, ButtonReleased: FKey) -> void
```

Called when the left mouse button is released while the mouse is over this actor and click events are enabled in the player controller.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TouchedActor` | `AActor*` | - |
| `ButtonReleased` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInputTouchBegin`

```text
OnInputTouchBegin(FingerIndex: ETouchIndex::Type, TouchedActor: AActor*) -> void
```

Called when a touch input is received over this actor when touch events are enabled in the player controller.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex::Type` | - |
| `TouchedActor` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInputTouchEnd`

```text
OnInputTouchEnd(FingerIndex: ETouchIndex::Type, TouchedActor: AActor*) -> void
```

Called when a touch input is received over this component when touch events are enabled in the player controller.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex::Type` | - |
| `TouchedActor` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInputTouchEnter`

```text
OnInputTouchEnter(FingerIndex: ETouchIndex::Type, TouchedActor: AActor*) -> void
```

Called when a finger is moved over this actor when touch over events are enabled in the player controller.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex::Type` | - |
| `TouchedActor` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInputTouchLeave`

```text
OnInputTouchLeave(FingerIndex: ETouchIndex::Type, TouchedActor: AActor*) -> void
```

Called when a finger is moved off this actor when touch over events are enabled in the player controller.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex::Type` | - |
| `TouchedActor` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnActorHit`

```text
OnActorHit(SelfActor: AActor*, OtherActor: AActor*, NormalImpulse: FVector, Hit: const FHitResult&) -> void
```

Called when this Actor hits (or is hit by) something solid. This could happen due to things like Character movement, using Set Location with 'sweep' enabled, or physics simulation.
	 	For events when objects overlap (e.g. walking into a trigger) see the 'Overlap' event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelfActor` | `AActor*` | - |
| `OtherActor` | `AActor*` | - |
| `NormalImpulse` | `FVector` | - |
| `Hit` | `const FHitResult&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnActorHitNew`

```text
OnActorHitNew(SelfActor: AActor*, OtherActor: AActor*, NormalImpulse: FVector, Hit: const FHitResult&) -> void
```

same as OnActorHit, but will Recivie StartPenetrating Hits

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelfActor` | `AActor*` | - |
| `OtherActor` | `AActor*` | - |
| `NormalImpulse` | `FVector` | - |
| `Hit` | `const FHitResult&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnDestroyed`

```text
OnDestroyed(DestroyedActor: AActor*) -> void
```

Event triggered when the actor is destroyed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DestroyedActor` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnEndPlay`

```text
OnEndPlay(Actor: AActor*, EndPlayReason: EEndPlayReason::Type) -> void
```

Event triggered when the actor is being removed from a level.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor*` | - |
| `EndPlayReason` | `EEndPlayReason::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnBecomeViewTargetEvent`

```text
OnBecomeViewTargetEvent(PC: APlayerController*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PC` | `APlayerController*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnEndViewTargetEvent`

```text
OnEndViewTargetEvent(PC: APlayerController*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PC` | `APlayerController*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnEndBlendViewTargetEvent`

```text
OnEndBlendViewTargetEvent(PC: APlayerController*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PC` | `APlayerController*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ActorOnVaultEvent`

```text
ActorOnVaultEvent(Character: AActor*, HitLocation: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `AActor*` | - |
| `HitLocation` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AAggregatedCollisionActor.json -->

# AAggregatedCollisionActor

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AggregatedCollisionComponent` | `UAggregatedCollisionComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AAIController.json -->

# AAIController

AIController is the base class of controllers for AI-controlled Pawns.
  
  Controllers are non-physical actors that can be attached to a pawn to control its actions.
  AIControllers manage the artificial intelligence for the pawns they control.
  In networked games, they only exist on the server.

## Inheritance

`AController` -> `IAIPerceptionListenerInterface` -> `IGameplayTaskOwnerInterface` -> `IGenericTeamAgentInterface` -> `IVisualLoggerDebugSnapshotInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bStopAILogicOnUnposses` | `uint32` | By default AI's logic gets stopped when controlled Pawn is unpossesed. Setting this flag to false<br>	 	will make AI logic persist past loosing controll over a pawn |
| `bSkipExtraLOSChecks` | `uint32` | Skip extra line of sight traces to extremities of target being checked. |
| `bAllowStrafe` | `uint32` | Is strafing allowed during movement? |
| `bWantsPlayerState` | `uint32` | Specifies if this AI wants its own PlayerState. |
| `bSetControlRotationFromPawnOrientation` | `uint32` | Copy Pawn rotation to ControlRotation, if there is no focus point. |
| `PathFollowingComponent` | `UPathFollowingComponent *` | Component used for moving along a path. |
| `BrainComponent` | `UBrainComponent *` | Component responsible for behaviors. |
| `PerceptionComponent` | `UAIPerceptionComponent *` | - |
| `ActionsComp` | `UPawnActionsComponent *` | - |
| `Blackboard` | `UBlackboardComponent *` | blackboard |
| `CachedGameplayTasksComponent` | `UGameplayTasksComponent *` | - |
| `DefaultNavigationFilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |

## Functions

### `OnPossess`

```text
OnPossess(PossessedPawn: APawn *) -> void
```

Event called when PossessedPawn is possessed by this controller.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PossessedPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnUnpossess`

```text
OnUnpossess(UnpossessedPawn: APawn *) -> void
```

Gets triggered after given pawn has been unpossesed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UnpossessedPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MoveToActor`

```text
MoveToActor(Goal: AActor *, AcceptanceRadius: float, bStopOnOverlap: bool, bUsePathfinding: bool, bCanStrafe: bool, FilterClass: TSubclassOf < UNavigationQueryFilter >, bAllowPartialPath: bool) -> EPathFollowingRequestResult :: Type
```

Makes AI go toward specified Goal actor (destination will be continuously updated), aborts any active path following

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Goal` | `AActor *` | - |
| `AcceptanceRadius` | `float` | - finish move if pawn gets close enough |
| `bStopOnOverlap` | `bool` | - add pawn's radius to AcceptanceRadius |
| `bUsePathfinding` | `bool` | - use navigation data to calculate path (otherwise it will go in straight line) |
| `bCanStrafe` | `bool` | - set focus related flag: bAllowStrafe |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - navigation filter for pathfinding adjustments. If none specified DefaultNavigationFilterClass will be used |
| `bAllowPartialPath` | `bool` | - use incomplete path when goal can't be reached |

**Returns**

| Type | Description |
|---|---|
| `EPathFollowingRequestResult :: Type` | - |

### `MoveToLocation`

```text
MoveToLocation(Dest: FVector &, AcceptanceRadius: float, bStopOnOverlap: bool, bUsePathfinding: bool, bProjectDestinationToNavigation: bool, bCanStrafe: bool, FilterClass: TSubclassOf < UNavigationQueryFilter >, bAllowPartialPath: bool, bUseNavLink: bool) -> EPathFollowingRequestResult :: Type
```

Makes AI go toward specified Dest location, aborts any active path following

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Dest` | `FVector &` | - |
| `AcceptanceRadius` | `float` | - finish move if pawn gets close enough |
| `bStopOnOverlap` | `bool` | - add pawn's radius to AcceptanceRadius |
| `bUsePathfinding` | `bool` | - use navigation data to calculate path (otherwise it will go in straight line) |
| `bProjectDestinationToNavigation` | `bool` | - project location on navigation data before using it |
| `bCanStrafe` | `bool` | - set focus related flag: bAllowStrafe |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - navigation filter for pathfinding adjustments. If none specified DefaultNavigationFilterClass will be used |
| `bAllowPartialPath` | `bool` | - use incomplete path when goal can't be reached |
| `bUseNavLink` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `EPathFollowingRequestResult :: Type` | - |

### `GetMoveStatus`

```text
GetMoveStatus() -> EPathFollowingStatus :: Type
```

Returns status of path following

**Returns**

| Type | Description |
|---|---|
| `EPathFollowingStatus :: Type` | - |

### `HasPartialPath`

```text
HasPartialPath() -> bool
```

Returns true if the current PathFollowingComponent's path is partial (does not reach desired destination).

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetImmediateMoveDestination`

```text
GetImmediateMoveDestination() -> FVector
```

Returns position of current path segment's end.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SetMoveBlockDetection`

```text
SetMoveBlockDetection(bEnable: bool) -> void
```

Updates state of movement block detection.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RunBehaviorTree`

```text
RunBehaviorTree(BTAsset: UBehaviorTree *) -> bool
```

Starts executing behavior tree.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BTAsset` | `UBehaviorTree *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `UseBlackboard`

```text
UseBlackboard(BlackboardAsset: UBlackboardData *, BlackboardComponent: UBlackboardComponent * &) -> bool
```

Makes AI use the specified Blackboard asset & creates a Blackboard Component if one does not already exist.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BlackboardAsset` | `UBlackboardData *` | The Blackboard asset to use. |
| `BlackboardComponent` | `UBlackboardComponent * &` | The Blackboard component that was used or created to work with the passed-in Blackboard Asset. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if we successfully linked the blackboard asset to the blackboard component. |

### `ClaimTaskResource`

```text
ClaimTaskResource(ResourceClass: TSubclassOf < UGameplayTaskResource >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ResourceClass` | `TSubclassOf < UGameplayTaskResource >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnclaimTaskResource`

```text
UnclaimTaskResource(ResourceClass: TSubclassOf < UGameplayTaskResource >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ResourceClass` | `TSubclassOf < UGameplayTaskResource >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnUsingBlackBoard`

```text
OnUsingBlackBoard(BlackboardComp: UBlackboardComponent *, BlackboardAsset: UBlackboardData *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BlackboardComp` | `UBlackboardComponent *` | - |
| `BlackboardAsset` | `UBlackboardData *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetFocalPoint`

```text
GetFocalPoint() -> FVector
```

Retrieve the final position that controller should be looking at.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetFocalPointOnActor`

```text
GetFocalPointOnActor(Actor: AActor *) -> FVector
```

Retrieve the focal point this controller should focus to on given actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `K2_SetFocalPoint`

```text
K2_SetFocalPoint(FP: FVector) -> void
```

Set the position that controller should be looking at.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FP` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetFocus`

```text
K2_SetFocus(NewFocus: AActor *) -> void
```

Set Focus for actor, will set FocalPoint as a result.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewFocus` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetFocusActor`

```text
GetFocusActor() -> AActor *
```

Get the focused actor.

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `K2_ClearFocus`

```text
K2_ClearFocus() -> void
```

Clears Focus, will also clear FocalPoint as a result

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnGameplayTaskResourcesClaimed`

```text
OnGameplayTaskResourcesClaimed(NewlyClaimed: FGameplayResourceSet, FreshlyReleased: FGameplayResourceSet) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewlyClaimed` | `FGameplayResourceSet` | - |
| `FreshlyReleased` | `FGameplayResourceSet` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPathFollowingComponent`

```text
GetPathFollowingComponent() -> UPathFollowingComponent *
```

Returns PathFollowingComponent subobject

**Returns**

| Type | Description |
|---|---|
| `UPathFollowingComponent *` | - |

### `GetAIPerceptionComponent`

```text
GetAIPerceptionComponent() -> UAIPerceptionComponent *
```

**Returns**

| Type | Description |
|---|---|
| `UAIPerceptionComponent *` | - |

## Delegates

### `ReceiveMoveCompleted`

```text
ReceiveMoveCompleted(RequestID: FAIRequestID, Result: EPathFollowingResult::Type) -> void
```

Blueprint notification that we've completed the current movement request

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RequestID` | `FAIRequestID` | - |
| `Result` | `EPathFollowingResult::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AAmbientSound.json -->

# AAmbientSound

A sound actor that can be placed in a level

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AudioComponent` | `UAudioComponent *` | Audio component that handles sound playing |

## Functions

### `FadeIn`

```text
FadeIn(FadeInDuration: float, FadeVolumeLevel: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FadeInDuration` | `float` | - |
| `FadeVolumeLevel` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FadeOut`

```text
FadeOut(FadeOutDuration: float, FadeVolumeLevel: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FadeOutDuration` | `float` | - |
| `FadeVolumeLevel` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AdjustVolume`

```text
AdjustVolume(AdjustVolumeDuration: float, AdjustVolumeLevel: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AdjustVolumeDuration` | `float` | - |
| `AdjustVolumeLevel` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Play`

```text
Play(StartTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Stop`

```text
Stop() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AAtmosphericFog.json -->

# AAtmosphericFog

A placeable fog actor that simulates atmospheric light scattering

## Inheritance

`AInfo`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AtmosphericFogComponent` | `UAtmosphericFogComponent *` | Main fog component |
| `ArrowComponent` | `UArrowComponent *` | Arrow component to indicate default sun rotation |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AAtmosphericSkyBoxActor.json -->

# AAtmosphericSkyBoxActor

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Component` | `UAtmosphericSkyBoxComponent *` | - |
| `bEnabled` | `uint32` | replicated copy of ExponentialHeightFogComponent's bEnabled property |

## Functions

### `OnRep_bEnabled`

```text
OnRep_bEnabled() -> void
```

Replication Notification Callbacks

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AAudioVolume.json -->

# AAudioVolume

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Priority` | `float` | Priority of this volume. In the case of overlapping volumes the one with the highest priority<br>	  is chosen. The order is undefined if two or more overlapping volumes have the same priority. |
| `bEnabled` | `uint32` | whether this volume is currently enabled and able to affect sounds |
| `Settings` | `FReverbSettings` | Reverb settings to use for this volume. |
| `AmbientZoneSettings` | `FInteriorSettings` | Interior settings used for this volume |

## Functions

### `SetPriority`

```text
SetPriority(NewPriority: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPriority` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetEnabled`

```text
SetEnabled(bNewEnabled: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetReverbSettings`

```text
SetReverbSettings(NewReverbSettings: FReverbSettings &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewReverbSettings` | `FReverbSettings &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInteriorSettings`

```text
SetInteriorSettings(NewInteriorSettings: FInteriorSettings &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewInteriorSettings` | `FInteriorSettings &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_bEnabled`

```text
OnRep_bEnabled() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ABoxGIVolume.json -->

# ABoxGIVolume

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VolumeComponent` | `UGIBoxVolumeComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ABrush.json -->

# ABrush

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BrushType` | `TEnumAsByte < enum EBrushType >` | Type of brush |
| `BrushColor` | `FColor` | - |
| `PolyFlags` | `int32` | - |
| `bColored` | `uint32` | - |
| `bSolidWhenSelected` | `uint32` | - |
| `bPlaceableFromClassBrowser` | `uint32` | If true, this brush class can be placed using the class browser like other simple class types |
| `bNotForClientOrServer` | `uint32` | If true, this brush is a builder or otherwise does not need to be loaded into the game |
| `Brush` | `UModel *` | - |
| `BrushComponent` | `UBrushComponent *` | - |
| `bInManipulation` | `uint32` | Flag set when we are in a manipulation (scaling, translation, brush builder param change etc.) |
| `SavedSelections` | `TArray < struct FGeomSelection >` | Stores selection information from geometry mode.  This is the only information that we can't<br>	  regenerate by looking at the source brushes following an undo operation. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ACameraActor.json -->

# ACameraActor

A CameraActor is a camera viewpoint that can be placed in a level.

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AutoActivateForPlayer` | `TEnumAsByte < EAutoReceiveInput :: Type >` | Specifies which player controller, if any, should automatically use this Camera when the controller is active. |
| `CameraComponent` | `UCameraComponent *` | The camera component for this camera |
| `SceneComponent` | `USceneComponent *` | - |
| `bConstrainAspectRatio_DEPRECATED` | `uint32` | - |
| `AspectRatio_DEPRECATED` | `float` | - |
| `FOVAngle_DEPRECATED` | `float` | - |
| `PostProcessBlendWeight_DEPRECATED` | `float` | - |
| `PostProcessSettings_DEPRECATED` | `FPostProcessSettings` | - |

## Functions

### `GetAutoActivatePlayerIndex`

```text
GetAutoActivatePlayerIndex() -> int32
```

Returns index of the player for whom we auto-activate, or INDEX_NONE (-1) if disabled.

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ACameraRig_Crane.json -->

# ACameraRig_Crane

A simple rig for simulating crane-like camera movements.

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CranePitch` | `float` | Controls the pitch of the crane arm. |
| `CraneYaw` | `float` | Controls the yaw of the crane arm. |
| `CraneArmLength` | `float` | Controls the length of the crane arm. |
| `bLockMountPitch` | `bool` | Lock the mount pitch so that an attached camera is locked and pitched in the direction of the crane arm |
| `bLockMountYaw` | `bool` | Lock the mount yaw so that an attached camera is locked and oriented in the direction of the crane arm |
| `TransformComponent` | `USceneComponent *` | Root component to give the whole actor a transform. |
| `CraneYawControl` | `USceneComponent *` | Component to control Yaw. |
| `CranePitchControl` | `USceneComponent *` | Component to control Pitch. |
| `CraneCameraMount` | `USceneComponent *` | Component to define the attach point for cameras. |
| `PreviewMesh_CraneArm` | `UStaticMeshComponent *` | Preview meshes for visualization |
| `PreviewMesh_CraneBase` | `UStaticMeshComponent *` | - |
| `PreviewMesh_CraneMount` | `UStaticMeshComponent *` | - |
| `PreviewMesh_CraneCounterWeight` | `UStaticMeshComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ACameraRig_Rail.json -->

# ACameraRig_Rail

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CurrentPositionOnRail` | `float` | Defines current position of the mount point along the rail, in terms of normalized distance from the beginning of the rail. |
| `TransformComponent` | `USceneComponent *` | Root component to give the whole actor a transform. |
| `RailSplineComponent` | `USplineComponent *` | Spline component to define the rail path. |
| `RailCameraMount` | `USceneComponent *` | Component to define the attach point for cameras. Moves along the rail. |
| `PreviewMesh_Rail` | `USplineMeshComponent *` | Preview meshes for visualization |
| `PreviewRailMeshSegments` | `TArray < USplineMeshComponent * >` | - |
| `PreviewRailStaticMesh` | `UStaticMesh *` | - |
| `PreviewMesh_Mount` | `UStaticMeshComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ACharacter.json -->

# ACharacter

Characters are Pawns that have a mesh, collision, and built-in movement logic.
  They are responsible for all physical interaction between the player or AI and the world, and also implement basic networking and input models.
  They are designed for a vertically-oriented player representation that can walk, jump, fly, and swim through the world using CharacterMovementComponent.
 
  @see APawn, UCharacterMovementComponent

## Inheritance

`APawn`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Mesh` | `USkeletalMeshComponent *` | The main skeletal mesh associated with this Character (optional sub-object). |
| `CharacterMovement` | `UCharacterMovementComponent *` | Movement component used for movement logic in various movement modes (walking, falling, etc), containing relevant settings and functions to control movement. |
| `CapsuleComponent` | `UCapsuleComponent *` | The CapsuleComponent being used for movement collision (by CharacterMovement). Always treated as being vertically aligned in simple collision check functions. |
| `BasedMovement` | `FBasedMovementInfo` | Info about our current movement base (object we are standing on). |
| `ReplicatedBasedMovement` | `FBasedMovementInfo` | Replicated version of relative movement. Read-only on simulated proxies! |
| `AnimRootMotionTranslationScale` | `float` | Scale to apply to root motion translation on this Character |
| `NetworkPredictionInterface` | `TScriptInterface < INetworkPredictionInterface >` | - |
| `BaseTranslationOffset` | `FVector` | Saved translation offset of mesh. |
| `BaseRotationOffset` | `FQuat` | Saved rotation offset of mesh. |
| `ReplicatedServerLastTransformUpdateTimeStamp` | `float` | CharacterMovement ServerLastTransformUpdateTimeStamp value, replicated to simulated proxies. |
| `ReplicatedMovementMode` | `uint8` | Flag that we are receiving replication of the based movement. |
| `bInBaseReplication` | `bool` | Flag that we are receiving replication of the based movement. |
| `CrouchedEyeHeight` | `float` | Default crouched eye height |
| `bIsCrouched` | `uint32` | Set by character movement to specify that this Character is currently crouched. |
| `bPressedJump` | `uint32` | When true, player wants to jump |
| `bClientUpdating` | `uint32` | When true, applying updates to network client (replaying saved moves for a locally controlled character) |
| `bClientWasFalling` | `uint32` | True if Pawn was initially falling when started to replay network moves. |
| `bClientResimulateRootMotion` | `uint32` | If server disagrees with root motion track position, client has to resimulate root motion from last AckedMove. |
| `bClientResimulateRootMotionSources` | `uint32` | If server disagrees with root motion state, client has to resimulate root motion from last AckedMove. |
| `bSimGravityDisabled` | `uint32` | Disable simulated gravity (set when character encroaches geometry on client, to keep him from falling through floors) |
| `bClientCheckEncroachmentOnNetUpdate` | `uint32` | - |
| `bServerMoveIgnoreRootMotion` | `uint32` | Disable root motion on the server. When receiving a DualServerMove, where the first move is not root motion and the second is. |
| `JumpKeyHoldTime` | `float` | Jump key Held Time.<br>	  This is the time that the player has held the jump key, in seconds. |
| `JumpMaxHoldTime` | `float` | The max time the jump key can be held.<br>	  Note that if StopJumping() is not called before the max jump hold time is reached,<br>	  then the character will carry on receiving vertical velocity. Therefore it is usually<br>	  best to call StopJumping() when jump input has ceased (such as a button up event). |
| `JumpMaxCount` | `int32` | The max number of jumps the character can perform.<br>      Note that if JumpMaxHoldTime is non zero and StopJumping is not called, the player<br>      may be able to perform and unlimited number of jumps. Therefore it is usually<br>      best to call StopJumping() when jump input has ceased (such as a button up event). |
| `JumpCurrentCount` | `int32` | Tracks the current number of jumps performed.<br>      This is incremented in CheckJumpInput, used in CanJump_Implementation, and reset in OnMovementModeChanged.<br>      When providing overrides for these methods, it's recommended to either manually<br>      increment  reset this value, or call the Super:: method. |
| `bWasJumping` | `uint32` | - |
| `bUseReplaySampleRot` | `uint32` | - |
| `SavedRootMotion` | `FRootMotionSourceGroup` | For LocallyControlled Autonomous clients.<br>	   During a PerformMovement() after root motion is prepared, we save it off into this and<br>	   then record it into our SavedMoves.<br>	   During SavedMove playback we use it as our "Previous Move" SavedRootMotion which includes<br>	   last received root motion from the Server |
| `ClientRootMotionParams` | `FRootMotionMovementParams` | For LocallyControlled Autonomous clients. Saved root motion data to be used by SavedMoves. |
| `RootMotionRepMoves` | `TArray < FSimulatedRootMotionReplicatedMove >` | Array of previously received root motion moves from the server. |
| `RepRootMotion` | `FRepRootMotionMontage` | Replicated Root Motion montage |
| `bReplicateBasedMovement` | `uint8` | - |
| `DisableParticleNames` | `TArray < FString >` | - |
| `GeneralCampID` | `int32` | - |
| `EnableApplyMomentumInRadialDamage` | `bool` | - |
| `bEnableAsyncAnimInstance` | `bool` | - |
| `bAsyncNewAnimInstance` | `bool` | - |
| `AsyncAnimInstances` | `TMap < UAnimInstance * , bool >` | - |
| `bMarkScopeIn` | `bool` | - |
| `ArrowComponent` | `UArrowComponent *` | - |

## Functions

### `CacheInitialMeshOffset`

```text
CacheInitialMeshOffset(MeshRelativeLocation: FVector, MeshRelativeRotation: FRotator) -> void
```

Cache mesh offset from capsule. This is used as the target for network smoothing interpolation, when the mesh is offset with lagged smoothing.
	  This is automatically called during initialization; call this at runtime if you intend to change the default mesh offset from the capsule.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MeshRelativeLocation` | `FVector` | - |
| `MeshRelativeRotation` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_ReplicatedBasedMovement`

```text
OnRep_ReplicatedBasedMovement() -> void
```

Rep notify for ReplicatedBasedMovement

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetReplicateMovement`

```text
SetReplicateMovement(bInReplicateMovement: bool) -> void
```

Set whether this actor's movement replicates to network clients.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInReplicateMovement` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_ReplicatedMovementMode`

```text
OnRep_ReplicatedMovementMode(LastReplicatedMovementMode: uint8) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LastReplicatedMovementMode` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetReplicatedMovementMode`

```text
GetReplicatedMovementMode() -> uint8
```

Returns ReplicatedMovementMode

**Returns**

| Type | Description |
|---|---|
| `uint8` | - |

### `GetBaseTranslationOffset`

```text
GetBaseTranslationOffset() -> FVector
```

Get the saved translation offset of mesh. This is how much extra offset is applied from the center of the capsule.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetBaseRotationOffsetRotator`

```text
GetBaseRotationOffsetRotator() -> FRotator
```

Get the saved rotation offset of mesh. This is how much extra rotation is applied from the capsule rotation.

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `OnRep_IsCrouched`

```text
OnRep_IsCrouched() -> void
```

Handle Crouching replicated from server

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMovementBase`

```text
GetMovementBase() -> UPrimitiveComponent *
```

**Returns**

| Type | Description |
|---|---|
| `UPrimitiveComponent *` | - |

### `GetReplicatedMovementBase`

```text
GetReplicatedMovementBase() -> UPrimitiveComponent *
```

**Returns**

| Type | Description |
|---|---|
| `UPrimitiveComponent *` | - |

### `Jump`

```text
Jump() -> void
```

Make the character jump on the next update.
	  If you want your character to jump according to the time that the jump key is held,
	  then you can set JumpKeyHoldTime to some non-zero value. Make sure in this case to
	  call StopJumping() when you want the jump's z-velocity to stop being applied (such
	  as on a button up event), otherwise the character will carry on receiving the
	  velocity until JumpKeyHoldTime is reached.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopJumping`

```text
StopJumping() -> void
```

Stop the character from jumping on the next update.
	  Call this from an input event (such as a button 'up' event) to cease applying
	  jump Z-velocity. If this is not called, then jump z-velocity will be applied
	  until JumpMaxHoldTime is reached.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanJump`

```text
CanJump() -> bool
```

Check if the character can jump in the current state.
	 
	  The default implementation may be overridden or extended by implementing the custom CanJump event in Blueprints.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `CanJumpInternal`

```text
CanJumpInternal() -> bool
```

Customizable event to check if the character can jump in the current state.
	  Default implementation returns true if the character is on the ground and not crouching,
	  has a valid CharacterMovementComponent and CanEverJump() returns true.
	  Default implementation also allows for 'hold to jump higher' functionality:
	  As well as returning true when on the ground, it also returns true when GetMaxJumpTime is more
	  than zero and IsJumping returns true.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsJumpProvidingForce`

```text
IsJumpProvidingForce() -> bool
```

True if jump is actively providing a force, such as when the jump key is held and the time it has been held is less than JumpMaxHoldTime.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `PlayAnimMontage`

```text
PlayAnimMontage(AnimMontage: UAnimMontage *, InPlayRate: float, StartSectionName: FName, TPP: bool, FPP: bool, NewFPP: bool) -> float
```

Play Animation Montage on the character mesh

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AnimMontage` | `UAnimMontage *` | - |
| `InPlayRate` | `float` | - |
| `StartSectionName` | `FName` | - |
| `TPP` | `bool` | - |
| `FPP` | `bool` | - |
| `NewFPP` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `StopAnimMontage`

```text
StopAnimMontage(AnimMontage: UAnimMontage *) -> void
```

Stop Animation Montage. If NULL, it will stop what's currently active. The Blend Out Time is taken from the montage asset that is being stopped.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AnimMontage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCurrentMontage`

```text
GetCurrentMontage() -> UAnimMontage *
```

Return current playing Montage

**Returns**

| Type | Description |
|---|---|
| `UAnimMontage *` | - |

### `IsVelocitySimulated`

```text
IsVelocitySimulated() -> bool
```

是否正在速度场模拟中(实际生效)

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetAdditiveVelocity`

```text
GetAdditiveVelocity() -> FVector
```

获取速度场的叠加速度

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetSimulatedVelocity`

```text
GetSimulatedVelocity() -> FVector
```

获取速度场中的模拟速度(原有速度+叠加速度)

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `LaunchCharacter`

```text
LaunchCharacter(LaunchVelocity: FVector &, bXYOverride: bool, bZOverride: bool) -> void
```

Set a pending launch velocity on the Character. This velocity will be processed on the next CharacterMovementComponent tick,
	   and will set it to the "falling" state. Triggers the OnLaunched event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LaunchVelocity` | `FVector &` | - |
| `bXYOverride` | `bool` | - |
| `bZOverride` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnLaunched`

```text
OnLaunched(LaunchVelocity: FVector &, bXYOverride: bool, bZOverride: bool) -> void
```

Let blueprint know that we were launched

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LaunchVelocity` | `FVector &` | - |
| `bXYOverride` | `bool` | - |
| `bZOverride` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnJumped`

```text
OnJumped() -> void
```

Event fired when the character has just started jumping

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnLanded`

```text
OnLanded(Hit: FHitResult &) -> void
```

Called upon landing when falling, to perform actions based on the Hit result.
	 Note that movement mode is still "Falling" during this event. Current Velocity value is the velocity at the time of landing.
	 Consider OnMovementModeChanged() as well, as that can be used once the movement mode changes to the new mode (most likely Walking).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Hit` | `FHitResult &` | Result describing the landing that resulted in a valid landing spot. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWalkingOffLedge`

```text
OnWalkingOffLedge(PreviousFloorImpactNormal: FVector &, PreviousFloorContactNormal: FVector &, PreviousLocation: FVector &, TimeDelta: float) -> void
```

Event fired when the Character is walking off a surface and is about to fall because CharacterMovement->CurrentFloor became unwalkable.
	  If CharacterMovement->MovementMode does not change during this event then the character will automatically start falling afterwards.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PreviousFloorImpactNormal` | `FVector &` | Normal of the previous walkable floor. |
| `PreviousFloorContactNormal` | `FVector &` | Normal of the contact with the previous walkable floor. |
| `PreviousLocation` | `FVector &` | Previous character location before movement off the ledge. |
| `TimeDelta` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Crouch`

```text
Crouch(bClientSimulation: bool) -> void
```

Request the character to start crouching. The request is processed on the next update of the CharacterMovementComponent.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bClientSimulation` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnCrouch`

```text
UnCrouch(bClientSimulation: bool) -> void
```

Request the character to stop crouching. The request is processed on the next update of the CharacterMovementComponent.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bClientSimulation` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_OnEndCrouch`

```text
K2_OnEndCrouch(HalfHeightAdjust: float, ScaledHalfHeightAdjust: float) -> void
```

Event when Character stops crouching.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HalfHeightAdjust` | `float` | difference between default collision half-height, and actual crouched capsule half-height. |
| `ScaledHalfHeightAdjust` | `float` | difference after component scale is taken in to account. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_OnStartCrouch`

```text
K2_OnStartCrouch(HalfHeightAdjust: float, ScaledHalfHeightAdjust: float) -> void
```

Event when Character crouches.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HalfHeightAdjust` | `float` | difference between default collision half-height, and actual crouched capsule half-height. |
| `ScaledHalfHeightAdjust` | `float` | difference after component scale is taken in to account. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_OnMovementModeChanged`

```text
K2_OnMovementModeChanged(PrevMovementMode: EMovementMode, NewMovementMode: EMovementMode, PrevCustomMode: uint8, NewCustomMode: uint8) -> void
```

Called from CharacterMovementComponent to notify the character that the movement mode has changed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PrevMovementMode` | `EMovementMode` | Movement mode before the change |
| `NewMovementMode` | `EMovementMode` | New movement mode |
| `PrevCustomMode` | `uint8` | Custom mode before the change (applicable if PrevMovementMode is Custom) |
| `NewCustomMode` | `uint8` | New custom mode (applicable if NewMovementMode is Custom) |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_UpdateCustomMovement`

```text
K2_UpdateCustomMovement(DeltaTime: float) -> void
```

Event for implementing custom character movement mode. Called by CharacterMovement if MovementMode is set to Custom.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientCheatWalk`

```text
ClientCheatWalk() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientCheatFly`

```text
ClientCheatFly() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientCheatGhost`

```text
ClientCheatGhost() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RootMotionDebugClientPrintOnScreen`

```text
RootMotionDebugClientPrintOnScreen(InString: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_RootMotion`

```text
OnRep_RootMotion() -> void
```

Handles replicated root motion properties on simulated proxies and position correction.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsPlayingRootMotion`

```text
IsPlayingRootMotion() -> bool
```

true if we are playing Root Motion right now

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsPlayingNetworkedRootMotionMontage`

```text
IsPlayingNetworkedRootMotionMontage() -> bool
```

true if we are playing Root Motion right now, through a Montage with RootMotionMode == ERootMotionMode::RootMotionFromMontagesOnly.
	  This means code path for networked root motion is enabled.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetAnimRootMotionTranslationScale`

```text
GetAnimRootMotionTranslationScale() -> float
```

Returns current value of AnimRootMotionScale

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetReplicateBasedMovement`

```text
SetReplicateBasedMovement(bInReplicateBasedMovement: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInReplicateBasedMovement` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_GeneralCampID`

```text
OnRep_GeneralCampID() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnReachedJumpApex`

```text
OnReachedJumpApex() -> void
```

Broadcast when Character's jump reaches its apex. Needs CharacterMovement->bNotifyApex = true

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MovementModeChangedDelegate`

```text
MovementModeChangedDelegate(Character: ACharacter*, PrevMovementMode: EMovementMode, PreviousCustomMode: uint8) -> void
```

Multicast delegate for MovementMode changing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `ACharacter*` | - |
| `PrevMovementMode` | `EMovementMode` | - |
| `PreviousCustomMode` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnCharacterMovementUpdated`

```text
OnCharacterMovementUpdated(DeltaSeconds: float, OldLocation: FVector, OldVelocity: FVector) -> void
```

Event triggered at the end of a CharacterMovementComponent movement update.
	  This is the preferred event to use rather than the Tick event when performing custom updates to CharacterMovement properties based on the current state.
	  This is mainly due to the nature of network updates, where client corrections in position from the server can cause multiple iterations of a movement update,
	  which allows this event to update as well, while a Tick event would not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaSeconds` | `float` | Delta time in seconds for this update |
| `OldLocation` | `FVector` | - |
| `OldVelocity` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ACineCameraActor.json -->

# ACineCameraActor

A CineCameraActor is a CameraActor specialized to work like a cinematic camera.

## Inheritance

`ACameraActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LookatTrackingSettings` | `FCameraLookatTrackingSettings` | - |

## Functions

### `GetCineCameraComponent`

```text
GetCineCameraComponent() -> UCineCameraComponent *
```

Returns the CineCameraComponent of this CineCamera

**Returns**

| Type | Description |
|---|---|
| `UCineCameraComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AClipmapTextureVolume.json -->

# AClipmapTextureVolume

Actor used to place a URuntimeVirtualTexture in the world.

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ClipmapTextureComponent` | `UClipmapTextureComponent *` | Component that owns the runtime virtual texture. |
| `Box` | `UBoxComponent *` | Box for visualizing virtual texture extents. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AConsoleCMDVolume.json -->

# AConsoleCMDVolume

ConsoleCMDVolume is a volume used to automatically change console variables

 @see ModifyConsoleVariable

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConsoleVariables` | `TArray < FString >` | Array of tags that can be used for grouping and categorizing. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AController.json -->

# AController

Controllers are non-physical actors that can possess a Pawn to control
  its actions.  PlayerControllers are used by human players to control pawns, while
  AIControllers implement the artificial intelligence for the pawns they control.
  Controllers take control of a pawn using their Possess() method, and relinquish
  control of the pawn by calling UnPossess().
 
  Controllers receive notifications for many of the events occurring for the Pawn they
  are controlling.  This gives the controller the opportunity to implement the behavior
  in response to this event, intercepting the event and superseding the Pawn's default
  behavior.
 
  ControlRotation (accessed via GetControlRotation()), determines the viewingaiming
  direction of the controlled Pawn and is affected by input such as from a mouse or gamepad.

## Inheritance

`AActor` -> `INavAgentInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Pawn` | `APawn *` | Pawn currently being controlled by this controller.  Use Pawn.Possess() to take control of a pawn |
| `Character` | `ACharacter *` | Character currently being controlled by this controller.  Value is same as Pawn if the controlled pawn is a character, otherwise NULL |
| `PlayerState` | `APlayerState *` | PlayerState containing replicated information about the player using this controller (only exists for players, not NPCs). |
| `IgnoreMoveInputChnage` | `FString` | ShadowVar.  Use for debug |
| `IgnoreLookInputChnage` | `FString` | ShadowVar.  Use for debug |
| `TransformComponent` | `USceneComponent *` | Component to give controllers a transform and enable attachment if desired. |
| `ControlRotation` | `FRotator` | The control rotation of the Controller. See GetControlRotation. |
| `bAttachToPawn` | `uint32` | If true, the controller location will match the possessed Pawn's location. If false, it will not be updated. Rotation will match ControlRotation in either case.<br>	  Since a Controller's location is normally inaccessible, this is intended mainly for purposes of being able to attach<br>	  an Actor that follows the possessed Pawn location, but that still has the full aim rotation (since a Pawn might<br>	  update only some components of the rotation). |
| `bIsPlayerController` | `uint32` | Whether this controller is a PlayerController. |
| `IgnoreMoveInput` | `uint8` | Ignores movement input. Stacked state storage, Use accessor function IgnoreMoveInput() |
| `IgnoreLookInput` | `uint8` | Ignores look input. Stacked state storage, use accessor function IgnoreLookInput(). |
| `StateName` | `FName` | - |

## Functions

### `GetControlRotation`

```text
GetControlRotation() -> FRotator
```

Get the control rotation. This is the full aim rotation, which may be different than a camera orientation (for example in a third person view),
	   and may differ from the rotation of the controlled Pawn (which may choose not to visually pitch or roll, for example).

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `SetControlRotation`

```text
SetControlRotation(NewRotation: FRotator &) -> void
```

Set the control rotation. The RootComponent's rotation will also be updated to match it if RootComponent->bAbsoluteRotation is true.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRotation` | `FRotator &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInitialLocationAndRotation`

```text
SetInitialLocationAndRotation(NewLocation: FVector &, NewRotation: FRotator &) -> void
```

Set the initial location and rotation of the controller, as well as the control rotation. Typically used when the controller is first created.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector &` | - |
| `NewRotation` | `FRotator &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetStartSpot`

```text
SetStartSpot(InActor: AActor *) -> void
```

Set the StartSpot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearStartSpot`

```text
ClearStartSpot() -> void
```

Clear the StartSpot

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetStartSpot`

```text
GetStartSpot() -> AActor *
```

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `LineOfSightTo`

```text
LineOfSightTo(Other: AActor *, ViewPoint: FVector, bAlternateChecks: bool) -> bool
```

Checks line to center and top of other actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Other` | `AActor *` | is the actor whose visibility is being checked. |
| `ViewPoint` | `FVector` | is eye position visibility is being checked from. If vect(0,0,0) passed in, uses current viewtarget's eye position. |
| `bAlternateChecks` | `bool` | used only in AIController implementation |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if controller's pawn can see Other actor. |

### `OnRep_Pawn`

```text
OnRep_Pawn() -> void
```

Replication Notification Callbacks

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_PlayerState`

```text
OnRep_PlayerState() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CastToPlayerController`

```text
CastToPlayerController() -> APlayerController *
```

DEPRECATED! Use the standard "Cast To" node instead. Casts this Controller to a Player Controller, if possible.

**Returns**

| Type | Description |
|---|---|
| `APlayerController *` | - |

### `ClientSetLocation`

```text
ClientSetLocation(NewLocation: FVector, NewRotation: FRotator) -> void
```

Replicated function to set the pawn location and rotation, allowing server to force (ex. teleports).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector` | - |
| `NewRotation` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientSetRotation`

```text
ClientSetRotation(NewRotation: FRotator, bResetCamera: bool) -> void
```

Replicated function to set the pawn rotation, allowing the server to force.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRotation` | `FRotator` | - |
| `bResetCamera` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_GetPawn`

```text
K2_GetPawn() -> APawn *
```

Return the Pawn that is currently 'controlled' by this PlayerController

**Returns**

| Type | Description |
|---|---|
| `APawn *` | - |

### `GetViewTarget`

```text
GetViewTarget() -> AActor *
```

Get the actor the controller is looking at

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `GetDesiredRotation`

```text
GetDesiredRotation() -> FRotator
```

Get the desired pawn target rotation

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `IsPlayerController`

```text
IsPlayerController() -> bool
```

Returns whether this Controller is a PlayerController.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsLocalPlayerController`

```text
IsLocalPlayerController() -> bool
```

Returns whether this Controller is a locally controlled PlayerController.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsLocalController`

```text
IsLocalController() -> bool
```

Returns whether this Controller is a local controller.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Possess`

```text
Possess(InPawn: APawn *) -> void
```

Handles attaching this controller to the specified pawn.
	  Only runs on the network authority (where HasAuthority() returns true).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPawn` | `APawn *` | The Pawn to be possessed. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnPossess`

```text
UnPossess() -> void
```

Called to unpossess our pawn for any reason that is not the pawn being destroyed (destruction handled by PawnDestroyed()).

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopMovement`

```text
StopMovement() -> void
```

Aborts the move the controller is currently performing

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIgnoreMoveInput`

```text
SetIgnoreMoveInput(bNewMoveInput: bool) -> void
```

Locks or unlocks movement input, consecutive calls stack up and require the same amount of calls to undo, or can all be undone using ResetIgnoreMoveInput.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewMoveInput` | `bool` | If true, move input is ignored. If false, input is not ignored. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetIgnoreMoveInput`

```text
ResetIgnoreMoveInput() -> void
```

Stops ignoring move input by resetting the ignore move input state.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsMoveInputIgnored`

```text
IsMoveInputIgnored() -> bool
```

Returns true if movement input is ignored.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetIgnoreLookInput`

```text
SetIgnoreLookInput(bNewLookInput: bool) -> void
```

Locks or unlocks look input, consecutive calls stack up and require the same amount of calls to undo, or can all be undone using ResetIgnoreLookInput.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewLookInput` | `bool` | If true, look input is ignored. If false, input is not ignored. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetIgnoreLookInput`

```text
ResetIgnoreLookInput() -> void
```

Stops ignoring look input by resetting the ignore look input state.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsLookInputIgnored`

```text
IsLookInputIgnored() -> bool
```

Returns true if look input is ignored.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ResetIgnoreInputFlags`

```text
ResetIgnoreInputFlags() -> void
```

Reset move and look input ignore flags.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveInstigatedAnyDamage`

```text
ReceiveInstigatedAnyDamage(Damage: float, DamageType: UDamageType *, DamagedActor: AActor *, DamageCauser: AActor *) -> void
```

Event when this controller instigates ANY damage

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Damage` | `float` | - |
| `DamageType` | `UDamageType *` | - |
| `DamagedActor` | `AActor *` | - |
| `DamageCauser` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnInstigatedAnyDamage`

```text
OnInstigatedAnyDamage(Damage: float, DamageType: const class UDamageType*, DamagedActor: AActor*, DamageCauser: AActor*) -> void
```

Called when the controller has instigated damage in any way

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Damage` | `float` | - |
| `DamageType` | `const class UDamageType*` | - |
| `DamagedActor` | `AActor*` | - |
| `DamageCauser` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ACullDistanceVolume.json -->

# ACullDistanceVolume

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CullDistances` | `TArray < struct FCullDistanceSizePair >` | Array of size and cull distance pairs. The code will calculate the sphere diameter of a primitive's BB and look for a best<br>	  fit in this array to determine which cull distance to use. |
| `bEnabled` | `uint32` | Whether the volume is currently enabled or not. |
| `bEnabledDeviceScale` | `uint32` | - |
| `VeryLowScale` | `float` | - |
| `LowScale` | `float` | - |
| `MidScale` | `float` | - |
| `HighScale` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ADebugCameraController.json -->

# ADebugCameraController

Camera controller that allows you to fly around a level mostly unrestricted by normal movement rules.

 To turn it on, please press Alt+C or both (left and right) analogs on XBox pad,
 or use the "ToggleDebugCamera" console command. Check the debug camera bindings
 in DefaultPawn.cpp for the camera controls.

## Inheritance

`APlayerController`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bShowSelectedInfo` | `uint32` | Whether to show information about the selected actor on the debug camera HUD. |
| `bIsFrozenRendering` | `uint32` | @todo document |
| `DrawFrustum` | `UDrawFrustumComponent *` | @todo document |
| `SpeedScale` | `float` | Allows control over the speed of the spectator pawn. This scales the speed based on the InitialMaxSpeed. Use Set Pawn Movement Speed Scale during runtime |
| `InitialMaxSpeed` | `float` | Initial max speed of the spectator pawn when we start possession. |
| `InitialAccel` | `float` | Initial acceleration of the spectator pawn when we start possession. |
| `InitialDecel` | `float` | Initial deceleration of the spectator pawn when we start possession. |

## Functions

### `ShowDebugSelectedInfo`

```text
ShowDebugSelectedInfo() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ToggleDisplay`

```text
ToggleDisplay() -> void
```

Toggles the display of debug info and input commands for the Debug Camera.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSelectedActor`

```text
GetSelectedActor() -> AActor *
```

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `SetPawnMovementSpeedScale`

```text
SetPawnMovementSpeedScale(NewSpeedScale: float) -> void
```

Sets the pawn movement speed scale.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewSpeedScale` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveOnActivate`

```text
ReceiveOnActivate(OriginalPC: APlayerController *) -> void
```

Function called on activation of debug camera controller.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OriginalPC` | `APlayerController *` | The active player controller before this debug camera controller was possessed by the player. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveOnDeactivate`

```text
ReceiveOnDeactivate(RestoredPC: APlayerController *) -> void
```

Function called on deactivation of debug camera controller.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RestoredPC` | `APlayerController *` | The Player Controller that the player input is being returned to. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveOnActorSelected`

```text
ReceiveOnActorSelected(NewSelectedActor: AActor *, SelectHitLocation: FVector &, SelectHitNormal: FVector &, Hit: FHitResult &) -> void
```

Called when an actor has been selected with the primary key (e.g. left mouse button).
	 
	  The selection trace starts from the center of the debug camera's view.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewSelectedActor` | `AActor *` | - |
| `SelectHitLocation` | `FVector &` | The exact world-space location where the selection trace hit the New Selected Actor. |
| `SelectHitNormal` | `FVector &` | The world-space surface normal of the New Selected Actor at the hit location. |
| `Hit` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ADecalActor.json -->

# ADecalActor

DecalActor contains a DecalComponent which can be used to render material modifications on top of existing geometry.

 @see UDecalComponent

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Decal` | `UDecalComponent *` | The decal component for this decal actor |
| `ArrowComponent` | `UArrowComponent *` | Reference to the editor only arrow visualization component |
| `SpriteComponent` | `UBillboardComponent *` | Reference to the billboard component |
| `BoxComponent_DEPRECATED` | `UBoxComponent *` | - |

## Functions

### `SetDecalMaterial`

```text
SetDecalMaterial(NewDecalMaterial: UMaterialInterface *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewDecalMaterial` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDecalMaterial`

```text
GetDecalMaterial() -> UMaterialInterface *
```

**Returns**

| Type | Description |
|---|---|
| `UMaterialInterface *` | - |

### `CreateDynamicMaterialInstance`

```text
CreateDynamicMaterialInstance() -> UMaterialInstanceDynamic *
```

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ADecalBakingParameterActor.json -->

# ADecalBakingParameterActor

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DecalBakingParam` | `UDecalBakingParameterComponent *` | The decal component for this decal actor |
| `ArrowComponent` | `UArrowComponent *` | Reference to the editor only arrow visualization component |
| `SpriteComponent` | `UBillboardComponent *` | Reference to the billboard component |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ADecalMergeSubVolume.json -->

# ADecalMergeSubVolume

Decal Merge SubVolume
  美术在 ADecalPickupVolume 内手摆的「子体积」，用于在父 Volume 范围内精细控制
  合并 Mesh 的颗粒度。一个 SubVolume = 一个独立合并颗粒度（其内部所有普通 Decal
  合成 1～N 个 Mesh Actor，按 SkyBucket 分桶）。
 
  关键约束：
  - Atlas 颗粒度不变：仍由父 Volume 统一聚合（一 Volume 一 Atlas）；
    SubVolume 不触发独立 Atlas 构建。
  - 共存兜底：未被任何 SubVolume 覆盖的 Decal 沿用父 Volume 的现有逻辑
    （Grid 或整 Volume）。
  - 完全 EditorOnly：本 Actor 仅服务于编辑器内的合并颗粒度划分，没有任何运行时意义。
    通过重写 IsEditorOnly() = true，Cook 流程会整体跳过该 Actor，不写入 cooked .umap，
    打包后的版本里完全不存在该 Actor（含 DummyRoot）。
    编辑器中正常加载、正常显示、正常保存到 .umap 的 Editor-only 段。

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DummyRoot` | `USceneComponent *` | 运行时根组件（空 SceneComponent，无渲染开销） |
| `VolumeBox` | `UBoxComponent *` | Box 组件：定义 SubVolume 的范围，美术可在编辑器中拖拽调整大小 |
| `Priority` | `int32` | 优先级：用于 Decal 同时落入多个 SubVolume 时的归属仲裁。<br>	  数值越大优先级越高；相同则按 Actor Name 字典序兜底。 |
| `OverrideParentVolume` | `TWeakObjectPtr < ADecalPickupVolume >` | 可选：父 Volume 显式绑定。留空时按「SubVolume Pivot 落入哪个 DecalPickupVolume」自动推导。<br>	  显式绑定可解决跨 Volume 边界场景下的归属歧义。 |
| `SpriteComponent` | `UBillboardComponent *` | 编辑器 3D 图标（Billboard Sprite），在 Actor Pivot 位置显示，始终面向摄像机 |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ADecalPickupVolume.json -->

# ADecalPickupVolume

Decal Pickup Volume
  用于标定贴花合并颗粒度的 Volume Actor。
  同一个 Volume 内的所有 DecalActor 会被统一拾取为一批，合出来的图集（Atlas）是一套。
  支持 Grid 划分以控制合成 Mesh 的粒度（用于视锥剔除和遮挡剔除）。
 
  运行时轻量模式（非 EditorOnly）：
  - Volume 进入包体作为生成 Mesh 的 ParentActor（层级组织）
  - 编辑器专用组件（BoxComponent、GridLineComponent）通过 WITH_EDITORONLY_DATA 在 Cook 时剥离
  - 运行时仅剩空壳 AActor（无渲染、无 Tick、无碰撞，~200 bytes）

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DummyRoot` | `USceneComponent *` | 运行时根组件（空 SceneComponent，无渲染开销） |
| `VolumeBox` | `UBoxComponent *` | Box 组件：定义 Volume 的范围，美术可在编辑器中拖拽调整大小 <br>	 仅编辑器下存在，Cook 时由 WITH_EDITORONLY_DATA 保证剥离，无需 Transient |
| `bEnableGridSubdivision` | `bool` | 是否启用 Grid 划分（仅 XY 维度，不划分 Z） |
| `GridCellSize` | `float` | 单个 Grid Cell 的世界空间大小（cm），仅 XY 维度 |
| `SpriteComponent` | `UBillboardComponent *` | 编辑器 3D 图标（Billboard Sprite），在 Actor Pivot 位置显示，始终面向摄像机 |
| `GridLineComponent` | `ULineBatchComponent *` | Grid 线可视化组件 |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ADefaultPawn.json -->

# ADefaultPawn

DefaultPawn implements a simple Pawn with spherical collision and built-in flying movement.
  @see UFloatingPawnMovement

## Inheritance

`APawn`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BaseTurnRate` | `float` | Base turn rate, in degsec. Other scaling may affect final turn rate. |
| `BaseLookUpRate` | `float` | Base lookup rate, in degsec. Other scaling may affect final lookup rate. |
| `MovementComponent` | `UPawnMovementComponent *` | DefaultPawn movement component |
| `CollisionComponent` | `USphereComponent *` | DefaultPawn collision component |
| `MeshComponent` | `UStaticMeshComponent *` | The mesh associated with this Pawn. |
| `bAddDefaultMovementBindings` | `uint32` | If true, adds default input bindings for movement and camera look. |

## Functions

### `MoveForward`

```text
MoveForward(Val: float) -> void
```

Input callback to move forward in local space (or backward if Val is negative).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Val` | `float` | Amount of movement in the forward direction (or backward if negative). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MoveRight`

```text
MoveRight(Val: float) -> void
```

Input callback to strafe right in local space (or left if Val is negative).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Val` | `float` | Amount of movement in the right direction (or left if negative). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MoveUp_World`

```text
MoveUp_World(Val: float) -> void
```

Input callback to move up in world space (or down if Val is negative).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Val` | `float` | Amount of movement in the world up direction (or down if negative). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `TurnAtRate`

```text
TurnAtRate(Rate: float) -> void
```

Called via input to turn at a given rate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rate` | `float` | This is a normalized rate, i.e. 1.0 means 100% of desired turn rate |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `LookUpAtRate`

```text
LookUpAtRate(Rate: float) -> void
```

Called via input to look up at a given rate (or down if Rate is negative).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rate` | `float` | This is a normalized rate, i.e. 1.0 means 100% of desired turn rate |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ADocumentationActor.json -->

# ADocumentationActor

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DocumentLink` | `FString` | Link to a help document. |
| `Billboard` | `UMaterialBillboardComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AEliteProjectile.json -->

# AEliteProjectile

投掷物

## Inheritance

`AActor` -> `IRegionObjectInterface`

## Functions

### `AddOnProjectileDestroyedHandler`

```text
AddOnProjectileDestroyedHandler(InDelegate: FSimpleProjectileDelegate) -> void
```

生效范围SC
	  添加销毁事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDelegate` | `FSimpleProjectileDelegate` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveOnProjectileDestroyedHandler`

```text
RemoveOnProjectileDestroyedHandler(InDelegate: FSimpleProjectileDelegate) -> void
```

生效范围SC
	  移除销毁事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDelegate` | `FSimpleProjectileDelegate` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveProjectileExplodedEvent`

```text
ReceiveProjectileExplodedEvent(Impact: FHitResult &) -> void
```

生效范围SC
	  爆炸事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Impact` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveProjectileHit`

```text
ReceiveProjectileHit(Hit: FHitResult &) -> void
```

生效范围SC
	  击中事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Hit` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveProjectileBouncedEvent`

```text
ReceiveProjectileBouncedEvent(ImpactResult: FHitResult &, ImpactVelocity: FVector &) -> void
```

生效范围SC
	  弹射事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `FHitResult &` | - |
| `ImpactVelocity` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveProjectileStoppedEvent`

```text
ReceiveProjectileStoppedEvent(HitResult: FHitResult &) -> void
```

生效范围SC
	  停止事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HitResult` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AEmitter.json -->

# AEmitter

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParticleSystemComponent` | `UParticleSystemComponent *` | - |
| `bDestroyOnSystemFinish` | `uint32` | - |
| `bPostUpdateTickGroup` | `uint32` | - |
| `bCurrentlyActive` | `uint32` | used to update status of toggleable level placed emitters on clients |

## Functions

### `OnParticleSystemFinished`

```text
OnParticleSystemFinished(FinishedComponent: UParticleSystemComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FinishedComponent` | `UParticleSystemComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_bCurrentlyActive`

```text
OnRep_bCurrentlyActive() -> void
```

Replication Notification Callbacks

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Activate`

```text
Activate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Deactivate`

```text
Deactivate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ToggleActive`

```text
ToggleActive() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsActive`

```text
IsActive() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetTemplate`

```text
SetTemplate(NewTemplate: UParticleSystem *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTemplate` | `UParticleSystem *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFloatParameter`

```text
SetFloatParameter(ParameterName: FName, Param: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVectorParameter`

```text
SetVectorParameter(ParameterName: FName, Param: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetColorParameter`

```text
SetColorParameter(ParameterName: FName, Param: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetActorParameter`

```text
SetActorParameter(ParameterName: FName, Param: AActor *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMaterialParameter`

```text
SetMaterialParameter(ParameterName: FName, Param: UMaterialInterface *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnParticleSpawn`

```text
OnParticleSpawn(EventName: FName, EmitterTime: float, Location: FVector, Velocity: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EventName` | `FName` | - |
| `EmitterTime` | `float` | - |
| `Location` | `FVector` | - |
| `Velocity` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnParticleBurst`

```text
OnParticleBurst(EventName: FName, EmitterTime: float, ParticleCount: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EventName` | `FName` | - |
| `EmitterTime` | `float` | - |
| `ParticleCount` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnParticleDeath`

```text
OnParticleDeath(EventName: FName, EmitterTime: float, ParticleTime: int32, Location: FVector, Velocity: FVector, Direction: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EventName` | `FName` | - |
| `EmitterTime` | `float` | - |
| `ParticleTime` | `int32` | - |
| `Location` | `FVector` | - |
| `Velocity` | `FVector` | - |
| `Direction` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnParticleCollide`

```text
OnParticleCollide(EventName: FName, EmitterTime: float, ParticleTime: int32, Location: FVector, Velocity: FVector, Direction: FVector, Normal: FVector, BoneName: FName, PhysMat: UPhysicalMaterial*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EventName` | `FName` | - |
| `EmitterTime` | `float` | - |
| `ParticleTime` | `int32` | - |
| `Location` | `FVector` | - |
| `Velocity` | `FVector` | - |
| `Direction` | `FVector` | - |
| `Normal` | `FVector` | - |
| `BoneName` | `FName` | - |
| `PhysMat` | `UPhysicalMaterial*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AEmitterCameraLensEffectBase.json -->

# AEmitterCameraLensEffectBase

## Inheritance

`AEmitter`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PS_CameraEffect` | `UParticleSystem *` | Particle System to use |
| `PS_CameraEffectNonExtremeContent_DEPRECATED` | `UParticleSystem *` | The effect to use for non extreme content |
| `BaseCamera` | `APlayerCameraManager *` | Camera this emitter is attached to, will be notified when emitter is destroyed |
| `RelativeTransform` | `FTransform` | Effect-to-camera transform to allow arbitrary placement of the particle system .<br>	  Note the X component of the location will be scaled with camera fov to keep the lens effect the same apparent size. |
| `BaseFOV` | `float` | This is the assumed FOV for which the effect was authored. The code will make automatic adjustments to make it look the same at different FOVs |
| `bAllowMultipleInstances` | `uint8` | true if multiple instances of this emitter can exist simultaneously, false otherwise. |
| `bResetWhenRetriggered` | `uint8` | If bAllowMultipleInstances is true and this effect is retriggered, the particle system will be reset if this is true |
| `EmittersToTreatAsSame` | `TArray < TSubclassOf < AEmitterCameraLensEffectBase > >` | If an emitter class in this array is currently playing, do not play this effect.<br>	   Useful for preventing multiple similar or expensive camera effects from playing simultaneously. |
| `DistFromCamera_DEPRECATED` | `float` | DEPRECATED(4.11) |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AEQSTestingPawn.json -->

# AEQSTestingPawn

this class is abstract even though it's perfectly functional on its own.
 	The reason is to stop it from showing as valid player pawn type when configuring 
 	project's game mode.

## Inheritance

`ACharacter` -> `IEQSQueryResultSourceInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `QueryTemplate` | `UEnvQuery *` | - |
| `QueryParams` | `TArray < FEnvNamedValue >` | optional parameters for query |
| `QueryConfig` | `TArray < FAIDynamicParam >` | - |
| `TimeLimitPerStep` | `float` | - |
| `StepToDebugDraw` | `int32` | - |
| `HighlightMode` | `EEnvQueryHightlightMode` | - |
| `bDrawLabels` | `uint32` | - |
| `bDrawFailedItems` | `uint32` | - |
| `bReRunQueryOnlyOnFinishedMove` | `uint32` | - |
| `bShouldBeVisibleInGame` | `uint32` | - |
| `bTickDuringGame` | `uint32` | - |
| `QueryingMode` | `TEnumAsByte < EEnvQueryRunMode :: Type >` | - |
| `EdRenderComp` | `UEQSRenderingComponent *` | Editor Preview |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AExponentialHeightFog.json -->

# AExponentialHeightFog

Implements an Actor for exponential height fog.

## Inheritance

`AInfo`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Component` | `UExponentialHeightFogComponent *` | @todo document |
| `bEnabled` | `uint32` | replicated copy of ExponentialHeightFogComponent's bEnabled property |

## Functions

### `OnRep_bEnabled`

```text
OnRep_bEnabled() -> void
```

Replication Notification Callbacks

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AGameMode.json -->

# AGameMode

GameMode is a subclass of GameModeBase that behaves like a multiplayer match-based game.
  It has default behavior for picking spawn points and match state.
  If you want a simpler base, inherit from GameModeBase instead.

## Inheritance

`AGameModeBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MatchState` | `FName` | What match state we are currently in |
| `bDelayedStart` | `uint32` | Whether the game should immediately start when the first player logs in. Affects the default behavior of ReadyToStartMatch |
| `NumSpectators` | `int32` | Current number of spectators. |
| `NumPlayers` | `int32` | Current number of human players. |
| `NumBots` | `int32` | number of non-human players (AI controlled but participating as a player). |
| `MinRespawnDelay` | `float` | Minimum time before player can respawn after dying. |
| `NumTravellingPlayers` | `int32` | Number of players that are still traveling from a previous map |
| `EngineMessageClass` | `TSubclassOf < ULocalMessage >` | Contains strings describing localized game agnostic messages. |
| `InactivePlayerArray` | `TArray < APlayerState * >` | PlayerStates of players who have disconnected from the server (saved in case they reconnect) |
| `bEnabelPawnPool` | `bool` | Weather to enable Gamemode Pawn Pool |
| `InactivePlayerStateLifeSpan` | `float` | Time a playerstate will stick around in an inactive state after a player logout |
| `bHandleDedicatedServerReplays` | `bool` | If true, dedicated servers will record replays when HandleMatchHasStartedHandleMatchHasStopped is called |

## Functions

### `GetMatchState`

```text
GetMatchState() -> FName
```

Returns the current match state, this is an accessor to protect the state machine flow

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `IsMatchInProgress`

```text
IsMatchInProgress() -> bool
```

Returns true if the match state is InProgress or other gameplay state

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `HasMatchEnded`

```text
HasMatchEnded() -> bool
```

Returns true if the match state is WaitingPostMatch or later

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `StartMatch`

```text
StartMatch() -> void
```

Transition from WaitingToStart to InProgress. You can call this manually, will also get called if ReadyToStartMatch returns true

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EndMatch`

```text
EndMatch() -> void
```

Transition from InProgress to WaitingPostMatch. You can call this manually, will also get called if ReadyToEndMatch returns true

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestartGame`

```text
RestartGame() -> void
```

Restart the game, by default travel to the current map

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AbortMatch`

```text
AbortMatch() -> void
```

Report that a match has failed due to unrecoverable error

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_OnSetMatchState`

```text
K2_OnSetMatchState(NewState: FName) -> void
```

Implementable event to respond to match state changes

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewState` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReadyToStartMatch`

```text
ReadyToStartMatch() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | True if ready to Start Match. Games should override this |

### `ReadyToEndMatch`

```text
ReadyToEndMatch() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if ready to End Match. Games should override this |

### `Say`

```text
Say(Msg: FString &) -> void
```

Exec command to broadcast a string to all players

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Msg` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBandwidthLimit`

```text
SetBandwidthLimit(AsyncIOBandwidthLimit: float) -> void
```

Alters the synthetic bandwidth limit for a running game.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AsyncIOBandwidthLimit` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AGameModeBase.json -->

# AGameModeBase

The GameModeBase defines the game being played. It governs the game rules, scoring, what actors
  are allowed to exist in this game type, and who may enter the game.
 
  It is only instanced on the server and will never exist on the client. 
 
  A GameModeBase actor is instantiated when the level is initialized for gameplay in
  C++ UGameEngine::LoadMap().  
  
  The class of this GameMode actor is determined by (in order) either the URL ?game=xxx, 
  the GameMode Override value set in the World Settings, or the DefaultGameMode entry set 
  in the game's Project Settings.

## Inheritance

`AInfo` -> `IVirtualParallelWorld`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OptionsString` | `FString` | Save options string and parse it when needed |
| `GameSessionClass` | `TSubclassOf < AGameSession >` | Class of GameSession, which handles login approval and online game interface |
| `GameStateClass` | `TSubclassOf < AGameStateBase >` | Class of GameState associated with this GameMode. |
| `PlayerControllerClass` | `TSubclassOf < APlayerController >` | The class of PlayerController to spawn for players logging in. |
| `PlayerStateClass` | `TSubclassOf < APlayerState >` | A PlayerState of this class will be associated with every player to replicate relevant player information to all clients. |
| `HUDClass` | `TSubclassOf < AHUD >` | HUD class this game uses. |
| `DefaultPawnClass` | `TSubclassOf < APawn >` | The default pawn class used by players. |
| `SpectatorClass` | `TSubclassOf < ASpectatorPawn >` | The pawn class used by the PlayerController for players when spectating. |
| `ReplaySpectatorPlayerControllerClass` | `TSubclassOf < APlayerController >` | The PlayerController class used when spectating a network replay. |
| `GameSession` | `AGameSession *` | Game Session handles login approval, arbitration, online game interface |
| `GameState` | `AGameStateBase *` | GameState is used to replicate game state relevant properties to all clients. |
| `DefaultPlayerName` | `FText` | The default player name assigned to players that join with no name specified. |
| `bUseSeamlessTravel` | `uint32` | Whether the game perform map travels using SeamlessTravel() which loads in the background and doesn't disconnect clients |
| `bUnlimitedRegionZ` | `uint32` | - |
| `bStartPlayersAsSpectators` | `uint32` | Whether players should immediately spawn when logging in, or stay as spectators until they manually spawn |
| `bPauseable` | `uint32` | Whether the game is pauseable. |

## Functions

### `GetDefaultPawnClassForController`

```text
GetDefaultPawnClassForController(InController: AController *) -> UClass *
```

Returns default pawn class for given controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InController` | `AController *` | - |

**Returns**

| Type | Description |
|---|---|
| `UClass *` | - |

### `GetNumPlayers`

```text
GetNumPlayers() -> int32
```

Returns number of active human players, excluding spectators

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetNumSpectators`

```text
GetNumSpectators() -> int32
```

Returns number of human players currently spectating

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `StartPlay`

```text
StartPlay() -> void
```

Transitions to calls BeginPlay on actors.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HasMatchStarted`

```text
HasMatchStarted() -> bool
```

Returns true if the match start callbacks have been called

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ShouldReset`

```text
ShouldReset(ActorToReset: AActor *) -> bool
```

Overridable function to determine whether an Actor should have Reset called when the game has Reset called on it.
	  Default implementation returns true

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActorToReset` | `AActor *` | The actor to make a determination for |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if ActorToReset should have Reset() called on it while restarting the game, |

### `ResetLevel`

```text
ResetLevel() -> void
```

Overridable function called when resetting level. This is used to reset the game state while staying in the same map
	  Default implementation calls Reset() on all actors except GameMode and Controllers

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReturnToMainMenuHost`

```text
ReturnToMainMenuHost() -> void
```

Return to main menu, and disconnect any players

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_PostLogin`

```text
K2_PostLogin(NewPlayer: APlayerController *) -> void
```

Notification that a player has successfully logged in, and has been given a player controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayer` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_OnLogout`

```text
K2_OnLogout(ExitingController: AController *) -> void
```

Implementable event when a Controller with a PlayerState leaves the game.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ExitingController` | `AController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HandleStartingNewPlayer`

```text
HandleStartingNewPlayer(NewPlayer: APlayerController *) -> void
```

Signals that a player is ready to enter the game, which may start it up

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayer` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MustSpectate`

```text
MustSpectate(NewPlayerController: APlayerController *) -> bool
```

Returns true if NewPlayerController may only join the server as a spectator.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayerController` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `CanSpectate`

```text
CanSpectate(Viewer: APlayerController *, ViewTarget: APlayerState *) -> bool
```

Return whether Viewer is allowed to spectate from the point of view of ViewTarget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Viewer` | `APlayerController *` | - |
| `ViewTarget` | `APlayerState *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ChangeName`

```text
ChangeName(Controller: AController *, NewName: FString &, bNameChange: bool) -> void
```

Sets the name for a controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Controller` | `AController *` | The controller of the player to change the name of |
| `NewName` | `FString &` | The name to set the player to |
| `bNameChange` | `bool` | Whether the name is changing or if this is the first time it has been set |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_OnChangeName`

```text
K2_OnChangeName(Other: AController *, NewName: FString &, bNameChange: bool) -> void
```

Overridable event for GameMode blueprint to respond to a change name call

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Other` | `AController *` | - |
| `NewName` | `FString &` | The name to set the player to |
| `bNameChange` | `bool` | Whether the name is changing or if this is the first time it has been set |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ChoosePlayerStart`

```text
ChoosePlayerStart(Player: AController *) -> AActor *
```

Return the 'best' player start for this player to spawn from
	  Default implementation looks for a random unoccupied spot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `AController *` | is the controller for whom we are choosing a playerstart |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | AActor chosen as player start (usually a PlayerStart) |

### `FindPlayerStart`

```text
FindPlayerStart(Player: AController *, IncomingName: FString &) -> AActor *
```

Return the specific player start actor that should be used for the next spawn
	  This will either use a previously saved startactor, or calls ChoosePlayerStart

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `AController *` | The AController for whom we are choosing a Player Start |
| `IncomingName` | `FString &` | Specifies the tag of a Player Start to use |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | Actor chosen as player start (usually a PlayerStart) |

### `K2_FindPlayerStart`

```text
K2_FindPlayerStart(Player: AController *, IncomingName: FString &) -> AActor *
```

Return the specific player start actor that should be used for the next spawn
	  This will either use a previously saved startactor, or calls ChoosePlayerStart

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `AController *` | The AController for whom we are choosing a Player Start |
| `IncomingName` | `FString &` | Specifies the tag of a Player Start to use |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | Actor chosen as player start (usually a PlayerStart) |

### `PlayerCanRestart`

```text
PlayerCanRestart(Player: APlayerController *) -> bool
```

Returns true if it's valid to call RestartPlayer. By default will call Player->CanRestartPlayer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `RestartPlayer`

```text
RestartPlayer(NewPlayer: AController *) -> void
```

Tries to spawn the player's pawn, at the location returned by FindPlayerStart

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayer` | `AController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestartPlayerAtPlayerStart`

```text
RestartPlayerAtPlayerStart(NewPlayer: AController *, StartSpot: AActor *) -> void
```

Tries to spawn the player's pawn at the specified actor's location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayer` | `AController *` | - |
| `StartSpot` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestartPlayerAtTransform`

```text
RestartPlayerAtTransform(NewPlayer: AController *, SpawnTransform: FTransform &) -> void
```

Tries to spawn the player's pawn at a specific location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayer` | `AController *` | - |
| `SpawnTransform` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SpawnDefaultPawnFor`

```text
SpawnDefaultPawnFor(NewPlayer: AController *, StartSpot: AActor *) -> APawn *
```

Called during RestartPlayer to actually spawn the player's pawn, when using a start spot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayer` | `AController *` | - Controller for whom this pawn is spawned |
| `StartSpot` | `AActor *` | - Actor at which to spawn pawn |

**Returns**

| Type | Description |
|---|---|
| `APawn *` | a pawn of the default pawn class |

### `SpawnDefaultPawnAtTransform`

```text
SpawnDefaultPawnAtTransform(NewPlayer: AController *, SpawnTransform: FTransform &) -> APawn *
```

Called during RestartPlayer to actually spawn the player's pawn, when using a transform

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayer` | `AController *` | - Controller for whom this pawn is spawned |
| `SpawnTransform` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `APawn *` | a pawn of the default pawn class |

### `InitStartSpot`

```text
InitStartSpot(StartSpot: AActor *, NewPlayer: AController *) -> void
```

Called from RestartPlayerAtPlayerStart, can be used to initialize the start spawn actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartSpot` | `AActor *` | - |
| `NewPlayer` | `AController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_OnRestartPlayer`

```text
K2_OnRestartPlayer(NewPlayer: AController *) -> void
```

Implementable event called at the end of RestartPlayer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayer` | `AController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InitializeHUDForPlayer`

```text
InitializeHUDForPlayer(NewPlayer: APlayerController *) -> void
```

Initialize the AHUD object for a player. Games can override this to do something different

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayer` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_OnSwapPlayerControllers`

```text
K2_OnSwapPlayerControllers(OldPC: APlayerController *, NewPC: APlayerController *) -> void
```

Called when a PlayerController is swapped to a new one during seamless travel

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldPC` | `APlayerController *` | - |
| `NewPC` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AGameNetworkManager.json -->

# AGameNetworkManager

Handles game-specific networking management (cheat detection, bandwidth management, etc.).

## Inheritance

`AInfo`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AdjustedNetSpeed` | `int32` | Current adjusted net speed - Used for dynamically managing netspeed for listen servers |
| `LastNetSpeedUpdateTime` | `float` | Last time netspeed was updated for server (by client entering or leaving) |
| `TotalNetBandwidth` | `int32` | Total available bandwidth for listen server, split dynamically across net connections |
| `MinDynamicBandwidth` | `int32` | Minimum bandwidth dynamically set per connection |
| `MaxDynamicBandwidth` | `int32` | Maximum bandwidth dynamically set per connection |
| `bIsStandbyCheckingEnabled` | `uint32` | Used to determine if checking for standby cheats should occur |
| `bHasStandbyCheatTriggered` | `uint32` | Used to determine whether we've already caught a cheat or not |
| `StandbyRxCheatTime` | `float` | The amount of time without packets before triggering the cheat code |
| `StandbyTxCheatTime` | `float` | The amount of time without packets before triggering the cheat code |
| `BadPingThreshold` | `int32` | The point we determine the server is either delaying packets or has bad upstream |
| `PercentMissingForRxStandby` | `float` | The percentage of clients missing RX data before triggering the standby code |
| `PercentMissingForTxStandby` | `float` | The percentage of clients missing TX data before triggering the standby code |
| `PercentForBadPing` | `float` | The percentage of clients with bad ping before triggering the standby code |
| `JoinInProgressStandbyWaitTime` | `float` | The amount of time to wait before checking a connection for standby issues |
| `MoveRepSize` | `float` | Average size of replicated move packet (ServerMove() packet size) from player |
| `MAXPOSITIONERRORSQUARED` | `float` | MAXPOSITIONERRORSQUARED is the square of the max position error that is accepted (not corrected) in net play |
| `MAXNEARZEROVELOCITYSQUARED` | `float` | MAXNEARZEROVELOCITYSQUARED is the square of the max velocity that is considered zero (not corrected) in net play |
| `CLIENTADJUSTUPDATECOST` | `float` | CLIENTADJUSTUPDATECOST is the bandwidth cost in bytes of sending a client adjustment update. 180 is greater than the actual cost, but represents a tweaked value reserving enough bandwidth for<br>	other updates sent to the client.  Increase this value to reduce client adjustment update frequency, or if the amount of data sent in the clientadjustment() call increases |
| `MAXCLIENTUPDATEINTERVAL` | `float` | MAXCLIENTUPDATEINTERVAL is the maximum time between movement updates from the client before the server forces an update. |
| `MaxMoveDeltaTime` | `float` | MaxMoveDeltaTime is the default maximum time delta of CharacterMovement ServerMoves. Should be less than or equal to MAXCLIENTUPDATEINTERVAL, otherwise server will interfere by forcing position updates. |
| `ClientNetSendMoveDeltaTime` | `float` | ClientNetSendMoveDeltaTime is the default minimum time delta of CharacterMovement client moves to the server. When updates occur more frequently, they may be combined to save bandwidth.<br>	  This value is not used when player count is over ClientNetSendMoveThrottleOverPlayerCount or player net speed is <= ClientNetSendMoveThrottleAtNetSpeed (see ClientNetSendMoveDeltaTimeThrottled). |
| `ClientNetSendMoveDeltaTimeThrottled` | `float` | ClientNetSendMoveDeltaTimeThrottled is used in place of ClientNetSendMoveDeltaTime when player count is high or net speed is low. See ClientNetSendMoveDeltaTime for more info. |
| `ClientNetSendMoveDeltaTimeStationary` | `float` | ClientNetSendMoveDeltaTimeStationary is used when players are determined to not be moving or changing their view. See ClientNetSendMoveDeltaTime for more info. |
| `ClientNetSendMoveThrottleAtNetSpeed` | `int32` | When player net speed (CurrentNetSpeed, based on ConfiguredInternetSpeed or ConfiguredLanSpeed) is less than or equal to this amount, ClientNetSendMoveDeltaTimeThrottled is used instead of ClientNetSendMoveDeltaTime. |
| `ClientNetSendMoveThrottleOverPlayerCount` | `int32` | When player count is greater than this amount, ClientNetSendMoveDeltaTimeThrottled is used instead of ClientNetSendMoveDeltaTime. |
| `ClientAuthorativePosition` | `bool` | If client update is within MAXPOSITIONERRORSQUARED then he is authorative on his final position |
| `ClientErrorUpdateRateLimit` | `float` | Minimum delay between the server sending error corrections to a client, in seconds. |
| `bMovementTimeDiscrepancyDetection` | `bool` | Whether movement time discrepancy detection is enabled. |
| `bMovementTimeDiscrepancyResolution` | `bool` | Whether movement time discrepancy resolution is enabled (when detected, make client movement "pay back" excessive time discrepancies) |
| `MovementTimeDiscrepancyMaxTimeMargin` | `float` | Maximum time client can be ahead before triggering movement time discrepancy detectionresolution (if enabled). |
| `MovementTimeDiscrepancyMinTimeMargin` | `float` | Maximum time client can be behind. |
| `MovementTimeDiscrepancyResolutionRate` | `float` | During time discrepancy resolution, we "pay back" the time discrepancy at this rate for future moves until total error is zero.<br>	  1.0 = 100% resolution rate, meaning the next X ServerMoves from the client are fully paying back the time, <br>	  0.5 = 50% resolution rate, meaning future ServerMoves will spend 50% of tick continuing to move the character and 50% paying back.<br>	  Lowering from 100% could be used to produce less severenoticeable corrections, although typically we would want to correct<br>	  the client as quickly as possible. |
| `MovementTimeDiscrepancyDriftAllowance` | `float` | Accepted drift in clocks between client and server as a percent per second allowed. <br>	 <br>	  0.0 is "no forgiveness" and all logic would run on raw values, no tampering on the server side.<br>	  0.02 would be a 2% per second difference "forgiven" - if the time discrepancy in a given second was less than 2%,<br>	  the error handlingdetection code effectively ignores it.<br>	  <br>	  Increasing this value above 0% lessens the chance of false positives on time discrepancy (burst packet loss, performance<br>	  hitches), but also means anyone tampering with their client time below that percent will not be detected and no resolution<br>	  action will be taken, and anyone above that threshold will still gain the advantage of this % of time boost (if running at <br>	  10% speed-up and this value is 0.05 or 5% allowance, they would only be resolved down to a 5% speed boost).<br>	 <br>	  Time discrepancy detection code DOES keep track of LifetimeRawTimeDiscrepancy, which is unaffected by this drift allowance,<br>	  so cheating below DriftAllowance percent could be tracked and acted on outside of an individual game. For example, if DriftAllowance<br>	  was 0.05 (meaning we're not going to actively prevent any cheating below 5% boosts to ensure less false positives for normal players),<br>	  we could still post-process analytics of the game showing that Player X regularly runs at 4% speed boost and take action. |
| `bMovementTimeDiscrepancyForceCorrectionsDuringResolution` | `bool` | Whether client moves should be force corrected during time discrepancy resolution, useful for projects that have lenient <br>	  move error toleranceClientAuthorativePosition enabled. |
| `bUseDistanceBasedRelevancy` | `bool` | If true, actor network relevancy is constrained by whether they are within their NetCullDistanceSquared from the client's view point. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AGameSession.json -->

# AGameSession

## Inheritance

`AInfo`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaxSpectators` | `int32` | Maximum number of spectators allowed by this server. |
| `MaxPlayers` | `int32` | Maximum number of players allowed by this server. |
| `MaxPartySize` | `int32` | Restrictions on the largest party that can join together |
| `MaxSplitscreensPerConnection` | `uint8` | Maximum number of splitscreen players to allow from one connection |
| `bRequiresPushToTalk` | `bool` | Is voice enabled always or via a push to talk keybinding |
| `SessionName` | `FName` | SessionName local copy from PlayerState class.  should really be define in this class, but need to address replication issues |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AGameState.json -->

# AGameState

GameState is a subclass of GameStateBase that behaves like a multiplayer match-based game.
  It is tied to functionality in GameMode.

## Inheritance

`AGameStateBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MatchState` | `FName` | What match state we are currently in |
| `PreviousMatchState` | `FName` | Previous map state, used to handle if multiple transitions happen per frame |
| `ElapsedTime` | `int32` | Elapsed game time since match has started. |

## Functions

### `OnRep_MatchState`

```text
OnRep_MatchState() -> void
```

Match state has changed

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_ElapsedTime`

```text
OnRep_ElapsedTime() -> void
```

Gives clients the chance to do something when time gets updates

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetGeneralCampNameByCampID`

```text
GetGeneralCampNameByCampID(CampID: int32) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CampID` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetGeneralCampRelation`

```text
GetGeneralCampRelation(CampAID: int32, CampBID: int32) -> ECampRelation
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CampAID` | `int32` | - |
| `CampBID` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `ECampRelation` | - |

### `GetGameModeGeneralDataAsset`

```text
GetGameModeGeneralDataAsset() -> UGameModeGeneralDataAsset *
```

**Returns**

| Type | Description |
|---|---|
| `UGameModeGeneralDataAsset *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AGameStateBase.json -->

# AGameStateBase

GameStateBase is a class that manages the game's global state, and is spawned by GameModeBase.
  It exists on both the client and the server and is fully replicated.

## Inheritance

`AInfo`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GameModeClass` | `TSubclassOf < AGameModeBase >` | Class of the server's game mode, assigned by GameModeBase. |
| `AuthorityGameMode` | `AGameModeBase *` | Instance of the current game mode, exists only on the server. For non-authority clients, this will be NULL. |
| `SpectatorClass` | `TSubclassOf < ASpectatorPawn >` | Class used by spectators, assigned by GameModeBase. |
| `PlayerArray` | `TArray < APlayerState * >` | Array of all PlayerStates, maintained on both server and clients (PlayerStates are always relevant) |
| `bReplicatedHasBegunPlay` | `bool` | Replicated when GameModeBase->StartPlay has been called so the client will also start play |
| `ReplicatedWorldTimeSeconds` | `float` | Server TimeSeconds. Useful for syncing up animation and gameplay. |
| `ServerWorldTimeSecondsDelta` | `float` | The difference from the local world's TimeSeconds and the server world's TimeSeconds. |
| `ServerWorldTimeSecondsUpdateFrequency` | `float` | Frequency that the server updates the replicated TimeSeconds from the world. Set to zero to disable periodic updates. |
| `bRecordControllerReplay` | `bool` | If use rec ctrl in replay |
| `PauseInfo` | `bool` | - |

## Functions

### `GetServerWorldTimeSeconds`

```text
GetServerWorldTimeSeconds() -> float
```

Returns the simulated TimeSeconds on the server, will be synchronized on client and server

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetServerWorldTimeSecondsForReplay`

```text
GetServerWorldTimeSecondsForReplay() -> float
```

Returns the simulated TimeSeconds on the server while playing replay, with fastforward skipped time considered

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `HasBegunPlay`

```text
HasBegunPlay() -> bool
```

Returns true if the world has started play (called BeginPlay on actors)

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `HasMatchStarted`

```text
HasMatchStarted() -> bool
```

Returns true if the world has started match (called MatchStarted callbacks)

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetPlayerStartTime`

```text
GetPlayerStartTime(Controller: AController *) -> float
```

Returns the time that should be used as when a player started

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Controller` | `AController *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetPlayerRespawnDelay`

```text
GetPlayerRespawnDelay(Controller: AController *) -> float
```

Returns how much time needs to be spent before a player can respawn

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Controller` | `AController *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `OnRep_GameModeClass`

```text
OnRep_GameModeClass() -> void
```

GameModeBase class notification callback.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_SpectatorClass`

```text
OnRep_SpectatorClass() -> void
```

Callback when we receive the spectator class

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_ReplicatedHasBegunPlay`

```text
OnRep_ReplicatedHasBegunPlay() -> void
```

By default calls BeginPlay and StartMatch

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_ReplicatedWorldTimeSeconds`

```text
OnRep_ReplicatedWorldTimeSeconds(OldValue: float &) -> void
```

Allows clients to calculate ServerWorldTimeSecondsDelta

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldValue` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_RecordControllerReplay`

```text
OnRep_RecordControllerReplay() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_PauseInfo`

```text
OnRep_PauseInfo() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnPauseState`

```text
OnPauseState(bIsPause: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsPause` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AInfo.json -->

# AInfo

Info is the base class of an Actor that isn't meant to have a physical representation in the world, used primarily
  for "manager" type classes that hold settings data about the world, but might need to be an Actor for replication purposes.

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SpriteComponent` | `UBillboardComponent *` | Billboard Component displayed in editor |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AInteractiveFoliageActor.json -->

# AInteractiveFoliageActor

## Inheritance

`AStaticMeshActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CapsuleComponent` | `UCapsuleComponent *` | Collision cylinder |
| `TouchingActorEntryPosition` | `FVector` | Position of the last actor to enter the collision cylinder.<br>	  This currently does not handle multiple actors affecting the foliage simultaneously. |
| `FoliageVelocity` | `FVector` | Simulated physics state |
| `FoliageForce` | `FVector` | @todo document |
| `FoliagePosition` | `FVector` | @todo document |
| `FoliageDamageImpulseScale` | `float` | Scales forces applied from damage events. |
| `FoliageTouchImpulseScale` | `float` | Scales forces applied from touch events. |
| `FoliageStiffness` | `float` | Determines how strong the force that pushes toward the spring's center will be. |
| `FoliageStiffnessQuadratic` | `float` | Same as FoliageStiffness, but the strength of this force increases with the square of the distance to the spring's center.<br>	  This force is used to prevent the spring from extending past a certain point due to touch and damage forces. |
| `FoliageDamping` | `float` | Determines the amount of energy lost by the spring as it oscillates.<br>	  This force is similar to air friction. |
| `MaxDamageImpulse` | `float` | Clamps the magnitude of each damage force applied. |
| `MaxTouchImpulse` | `float` | Clamps the magnitude of each touch force applied. |
| `MaxForce` | `float` | Clamps the magnitude of combined forces applied each update. |
| `Mass` | `float` | - |

## Functions

### `CapsuleTouched`

```text
CapsuleTouched(OverlappedComp: UPrimitiveComponent *, Other: AActor *, OtherComp: UPrimitiveComponent *, OtherBodyIndex: int32, bFromSweep: bool, OverlapInfo: FHitResult &) -> void
```

Called when capsule is touched

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OverlappedComp` | `UPrimitiveComponent *` | - |
| `Other` | `AActor *` | - |
| `OtherComp` | `UPrimitiveComponent *` | - |
| `OtherBodyIndex` | `int32` | - |
| `bFromSweep` | `bool` | - |
| `OverlapInfo` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ALandscape.json -->

# ALandscape

## Inheritance

`ALandscapeProxy`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaterialIdUserSettings` | `FMaterialIdUserSettings` | - |
| `UseFarLandNormalDistance` | `float` | - |
| `BlendFarLandNormalDistance` | `float` | - |
| `FarLandVertexColorThreshold` | `float` | - |
| `FarLandVertexColorBlendThreshold` | `float` | - |
| `bUseLandscapeDeform` | `bool` | - |
| `bCanUseMaterialIdShading` | `bool` | - |
| `CurrentBiomesIndex` | `int32` | Current selected biomes info |
| `bTextureArrayDirty` | `bool` | - |
| `PaintingCustomWeightLayerIndex` | `int32` | - |
| `MatIdLayerVisibility` | `TArray < bool >` | - |
| `FarLandDiffuseTexture` | `UTexture2D *` | - |
| `FarLandNormalTexture` | `UTexture2D *` | - |
| `FarLandInfoDebug` | `TMap < ULandscapeComponent * , FFarLandInfo >` | - |
| `ExportSplatmapTexture` | `UTexture2D *` | - |
| `Platform` | `EMyLandscapePlatfromConfiguration` | - |
| `PCConfig` | `FMyLandscapeConfigurationParams` | - |
| `MobileConfig` | `FMyLandscapeConfigurationParams` | - |

## Functions

### `EnumerateLandscapePaintMatIDLayers`

```text
EnumerateLandscapePaintMatIDLayers(Landscape: ALandscapeProxy *) -> LANDSCAPE_API TArray < FName >
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Landscape` | `ALandscapeProxy *` | - |

**Returns**

| Type | Description |
|---|---|
| `LANDSCAPE_API TArray < FName >` | - |

### `IsMaterialIDLandscape`

```text
IsMaterialIDLandscape(Landscape: ALandscapeProxy *) -> LANDSCAPE_API bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Landscape` | `ALandscapeProxy *` | - |

**Returns**

| Type | Description |
|---|---|
| `LANDSCAPE_API bool` | - |

### `SetLandscapeCorner`

```text
SetLandscapeCorner() -> LANDSCAPE_API void
```

**Returns**

| Type | Description |
|---|---|
| `LANDSCAPE_API void` | - |

### `SplitFarLandTextureForComponent`

```text
SplitFarLandTextureForComponent() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetFarLandTextureInfo`

```text
GetFarLandTextureInfo() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GenerateSplatmapMip`

```text
GenerateSplatmapMip() -> LANDSCAPE_API void
```

**Returns**

| Type | Description |
|---|---|
| `LANDSCAPE_API void` | - |

### `ExportWeightAsSplatmapMipEditor`

```text
ExportWeightAsSplatmapMipEditor() -> LANDSCAPE_API void
```

**Returns**

| Type | Description |
|---|---|
| `LANDSCAPE_API void` | - |

### `BuildLandscapeStaticMesh`

```text
BuildLandscapeStaticMesh() -> void
```

UFUNCTION(CallInEditor, Category = "Build Static Mesh", meta = (CallInEditor = "true"))

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ALandscapeMeshProxyActor.json -->

# ALandscapeMeshProxyActor

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LandscapeMeshProxyComponent` | `ULandscapeMeshProxyComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ALandscapeProxy.json -->

# ALandscapeProxy

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SplineComponent` | `ULandscapeSplinesComponent *` | - |
| `LandscapeGuid` | `FGuid` | - |
| `BoundingGuid` | `FGuid` | - |
| `bUseMaterialId` | `bool` | Cached value of bUseMaterialId, should be equal to bUseMaterialId in ALandscape |
| `MatIDFallbackMaterial` | `UMaterialInterface *` | - |
| `MatIDFallbackHoleMaterial` | `UMaterialInterface *` | - |
| `LandscapeSectionOffset` | `FIntPoint` | Offset in quads from global components grid origin (in quads) |
| `MaxLODLevel` | `int32` | Max LOD level to use when rendering, -1 means the max available |
| `MaxLODLevel_PC` | `int32` | Combined material used to render the landscape |
| `LODDistanceFactor_PC` | `float` | - |
| `LODStartDistance_PC` | `float` | - |
| `LODFalloff_PC` | `TEnumAsByte < ELandscapeLODFalloff :: Type >` | - |
| `LODDistanceFactor` | `float` | - |
| `LODFalloff` | `TEnumAsByte < ELandscapeLODFalloff :: Type >` | - |
| `bUseScreenSizeLOD` | `bool` | - |
| `LOD0DistributionSetting` | `float` | The distribution setting used to change the LOD 0 generation, 1.75 is the normal distribution, numbers influence directly the LOD0 proportion on screen. |
| `LODDistributionSetting` | `float` | The distribution setting used to change the LOD generation, 2 is the normal distribution, small number mean you want your last LODs to take more screen space and big number mean you want your first LODs to take more screen space. |
| `NearMaxLOD_Baked` | `uint8` | - |
| `NearFactor_Baked` | `float` | - |
| `NearExtent_Baked` | `float` | - |
| `FarFactor_Baked` | `float` | - |
| `LandscapeRoughness` | `float` | - |
| `EnableImproveLOD` | `bool` | - |
| `ImproveLODValues` | `TArray < float >` | LOD Values |
| `NearMaxLOD` | `uint8` | - |
| `NearFactor` | `float` | - |
| `NearExtent` | `float` | - |
| `FarFactor` | `float` | - |
| `StaticLightingLOD` | `int32` | LOD level to use when running lightmass (increase to 1 or 2 for large landscapes to stop lightmass crashing) |
| `DefaultPhysMaterial` | `UPhysicalMaterial *` | Default physical material, used when no per-layer values physical materials |
| `StreamingDistanceMultiplier` | `float` | Allows artists to adjust the distance where textures using UV 0 are streamed inout.<br>	  1.0 is the default, whereas a higher value increases the streamed-in resolution.<br>	  Value can be < 0 (from legcay content, or code changes) |
| `bCacheHeightData` | `uint32` | - |
| `LandscapeMaterial` | `UMaterialInterface *` | Combined material used to render the landscape |
| `LandscapeHoleMaterial` | `UMaterialInterface *` | Material used to render landscape components with holes. If not set, LandscapeMaterial will be used (blend mode will be overridden to Masked if it is set to Opaque) |
| `LandscapeMaterial_ForPC` | `UMaterialInterface *` | - |
| `LandscapeHoleMaterial_ForPC` | `UMaterialInterface *` | Material used to render landscape components with holes. If not set, LandscapeMaterial will be used (blend mode will be overridden to Masked if it is set to Opaque) |
| `bOverrideGrassTypes_ForPC` | `uint8` | - |
| `GrassTypes_ForPC` | `TArray < ULandscapeGrassType * >` | - |
| `OtherMaterials` | `TMap < FName , UMaterialInterface * >` | Other materials allow LandscapeComponent to change its material in runtime |
| `bOverrideGrassTypes` | `uint8` | - |
| `GrassTypes` | `TArray < ULandscapeGrassType * >` | - |
| `MinGrassWeightThreshold` | `float` | Minimal weight threshold to generate landscape grass |
| `NegativeZBoundsExtension` | `float` | Allows overriding the landscape bounds. This is useful if you distort the landscape with world-position-offset, for example<br>	   Extension value in the negative Z axis, positive value increases bound size<br>	   Note that this can also be overridden per-component when the component is selected with the component select tool |
| `PositiveZBoundsExtension` | `float` | Allows overriding the landscape bounds. This is useful if you distort the landscape with world-position-offset, for example<br>	   Extension value in the positive Z axis, positive value increases bound size<br>	   Note that this can also be overridden per-component when the component is selected with the component select tool |
| `GrassColor_WorldMaskNoiseTexture` | `UTexture2D *` | Texture used to render grass color |
| `GrassColor_UVScale_WorldMaskNoise` | `FVector2D` | - |
| `GrassColor_Center_WorldMaskNoise` | `FVector2D` | - |
| `LandscapeComponents` | `TArray < ULandscapeComponent * >` | The array of LandscapeComponent that are used by the landscape |
| `LandscapeAOTextureDataAsset` | `ULandscapeAOTextureDataAsset *` | - |
| `CollisionComponents` | `TArray < ULandscapeHeightfieldCollisionComponent * >` | Array of LandscapeHeightfieldCollisionComponent |
| `FoliageComponents` | `TArray < UHierarchicalInstancedStaticMeshComponent * >` | - |
| `StillUsed` | `TSet < UHierarchicalInstancedStaticMeshComponent * >` | - |
| `bHasLandscapeGrass` | `bool` | - |
| `StaticLightingResolution` | `float` | The resolution to cache lighting at, in texelsquad in one axis<br>	   Total resolution would be changed by StaticLightingResolutionStaticLightingResolution<br>	 	Automatically calculate proper value for removing seams |
| `bCastStaticShadow` | `uint32` | - |
| `bCastShadowAsTwoSided` | `uint32` | Whether this primitive should cast dynamic shadows as if it were a two sided material. |
| `bCastFarShadow` | `uint32` | Whether this primitive should cast shadows in the far shadow cascades. |
| `LightingChannels` | `FLightingChannels` | Channels that this Landscape should be in.  Lights with matching channels will affect the Landscape.<br>	 These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing. |
| `bUseMaterialPositionOffsetInStaticLighting` | `uint32` | Whether to use the landscape material's vertical world position offset when calculating static lighting.<br>		Does not work correctly with an XY offset map (mesh collision) |
| `bRenderCustomDepth` | `uint32` | If true, the Landscape will be rendered in the CustomDepth pass (usually used for outlines) |
| `CustomDepthStencilValue` | `int32` | Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3) |
| `LightmassSettings` | `FLightmassPrimitiveSettings` | The Lightmass settings for this object. |
| `CollisionMipLevel` | `int32` | - |
| `SimpleCollisionMipLevel` | `int32` | - |
| `CollisionThickness` | `float` | Thickness of the collision surface, in unreal units |
| `BodyInstance` | `FBodyInstance` | Collision profile settings for this landscape |
| `bGenerateOverlapEvents` | `uint32` | If true, Landscape will generate overlap events when other components are overlapping it (eg Begin Overlap).<br>	  Both the Landscape and the other component must have this flag enabled for overlap events to occur.<br>	 <br>	  @see UpdateOverlaps(), BeginComponentOverlap(), EndComponentOverlap() |
| `bBakeMaterialPositionOffsetIntoCollision` | `uint32` | Whether to bake the landscape material's vertical world position offset into the collision heightfield.<br>		Does not work with an XY offset map (mesh collision) |
| `bUseHoleConsistent` | `uint32` | Set to true before digging, making the physical data consistent with the rendered data, added by huiwenjiang |
| `ComponentSizeQuads` | `int32` | Data set at creation time |
| `SubsectionSizeQuads` | `int32` | Data set at creation time |
| `NumSubsections` | `int32` | Data set at creation time |
| `bUsedForNavigation` | `uint32` | Data set at creation time <br>	 Hints navigation system whether this landscape will ever be navigated on. true by default, but make sure to set it to false for faraway, background landscapes |
| `bMobileMultiLayers` | `uint32` | - |
| `NavigationGeometryGatheringMode` | `ENavDataGatheringMode` | - |
| `bUseLandscapeForCullingInvisibleHLODVertices` | `bool` | Flag whether or not this Landscape's surface can be used for culling hidden triangles |
| `DeformComponentMap` | `TMap < FIntPoint , int32 >` | - |
| `DeformWeightTileMap` | `TArray < uint32 >` | - |
| `DeformWeightData` | `TArray < uint8 >` | - |
| `ExportLOD` | `int32` | LOD level to use when exporting the landscape to obj or FBX |
| `TargetDisplayOrderList` | `TArray < FName >` | Display Order of the targets |
| `TargetDisplayOrder` | `ELandscapeLayerDisplayMode` | Display Order mode for the targets |
| `bUsePCMaterialToGenerateCollision` | `bool` | Combined material used to render the landscape |
| `bIsMovingToLevel` | `uint32` | - |
| `EditorCachedLayerInfos_DEPRECATED` | `TArray < ULandscapeLayerInfoObject * >` | - |
| `ReimportHeightmapFilePath` | `FString` | - |
| `EditorLayerSettings` | `TArray < FLandscapeEditorLayerSettings >` | - |
| `ExtraHeightmapNumber` | `int32` | - |
| `NoWeightBlendMaskNumber` | `int32` | - |
| `HeightmapNameSet` | `TSet < FString >` | - |
| `MaskNameSet` | `TSet < FString >` | - |
| `VisibleHeightmapNameSet` | `TSet < FString >` | - |
| `NoWeightBlendMaskNameSet` | `TSet < FString >` | - |
| `LockedHeightmapNameSet` | `TSet < FString >` | - |
| `ColorMaskList` | `TArray < FLandscapeColorMask >` | - |
| `VisibilityLayerNameSet` | `TSet < FString >` | All Visibility Layer names |
| `MaxPaintedLayersPerComponent` | `int32` | - |
| `LayerTextureParameterMapping` | `TMap < FName , UTexture * >` | - |
| `DeformWeightMsg` | `FString` | - |

## Functions

### `ChangebUseScreenSizeLOD`

```text
ChangebUseScreenSizeLOD(InbUseScreenSizeLOD: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InbUseScreenSizeLOD` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ChangeLODDistanceFactor`

```text
ChangeLODDistanceFactor(InLODDistanceFactor: float) -> void
```

Change the Level of Detail distance factor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InLODDistanceFactor` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ChangeLOD0DistributionSettingConsoleVariable`

```text
ChangeLOD0DistributionSettingConsoleVariable() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ChangeLODDistributionSettingConsoleVariable`

```text
ChangeLODDistributionSettingConsoleVariable() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EditorApplySpline`

```text
EditorApplySpline(InSplineComponent: USplineComponent *, StartWidth: float, EndWidth: float, StartSideFalloff: float, EndSideFalloff: float, StartRoll: float, EndRoll: float, NumSubdivisions: int32, bRaiseHeights: bool, bLowerHeights: bool, PaintLayer: ULandscapeLayerInfoObject *) -> void
```

Deform landscape using a given spline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSplineComponent` | `USplineComponent *` | - |
| `StartWidth` | `float` | - Width of the spline at the start node, in Spline Component local space |
| `EndWidth` | `float` | - Width of the spline at the end node, in Spline Component local space |
| `StartSideFalloff` | `float` | - Width of the falloff at either side of the spline at the start node, in Spline Component local space |
| `EndSideFalloff` | `float` | - Width of the falloff at either side of the spline at the end node, in Spline Component local space |
| `StartRoll` | `float` | - Roll applied to the spline at the start node, in degrees. 0 is flat |
| `EndRoll` | `float` | - Roll applied to the spline at the end node, in degrees. 0 is flat |
| `NumSubdivisions` | `int32` | - Number of triangles to place along the spline when applying it to the landscape. Higher numbers give better results, but setting it too high will be slow and may cause artifacts |
| `bRaiseHeights` | `bool` | - Allow the landscape to be raised up to the level of the spline. If both bRaiseHeights and bLowerHeights are false, no height modification of the landscape will be performed |
| `bLowerHeights` | `bool` | - Allow the landscape to be lowered down to the level of the spline. If both bRaiseHeights and bLowerHeights are false, no height modification of the landscape will be performed |
| `PaintLayer` | `ULandscapeLayerInfoObject *` | - LayerInfo to paint, or none to skip painting. The landscape must be configured with the same layer info in one of its layers or this will do nothing! |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BakeLandscape`

```text
BakeLandscape() -> void
```

UFUNCTION(BlueprintNativeEvent, BlueprintNativeEvent, CallInEditor, Category = "Improve LOD")

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DebugViewLandscapeCollision`

```text
DebugViewLandscapeCollision() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearCollisionDebugDraw`

```text
ClearCollisionDebugDraw() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FixPCOnlyWeightmapData`

```text
FixPCOnlyWeightmapData() -> LANDSCAPE_API void
```

**Returns**

| Type | Description |
|---|---|
| `LANDSCAPE_API void` | - |

### `FixPCOnlyWeightmap`

```text
FixPCOnlyWeightmap() -> LANDSCAPE_API void
```

**Returns**

| Type | Description |
|---|---|
| `LANDSCAPE_API void` | - |

### `ChangeShowWeightmap`

```text
ChangeShowWeightmap() -> LANDSCAPE_API void
```

**Returns**

| Type | Description |
|---|---|
| `LANDSCAPE_API void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ALandscapeStreamingProxy.json -->

# ALandscapeStreamingProxy

## Inheritance

`ALandscapeProxy`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LandscapeActor` | `TLazyObjectPtr < ALandscape >` | - |
| `MatIDSettings` | `FMaterialIdUserSettings` | - |
| `LandscapeAOTexture` | `UTexture2D *` | Texture used to render grass color |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ALevelBounds.json -->

# ALevelBounds

Defines level bounds
  Updates bounding box automatically based on actors transformation changes or holds fixed user defined bounding box
  Uses only actors where AActor::IsLevelBoundsRelevant() == true

## Inheritance

`AActor` -> `FEditorTickableLevelBounds`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bAutoUpdateBounds` | `bool` | Whether to automatically update actor bounds based on all relevant actors bounds belonging to the same level |
| `bCalWithoutLandscapeSpline` | `bool` | - |

## Functions

### `SaveLevelBoudns`

```text
SaveLevelBoudns() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CaculateFoliageLevelBounds`

```text
CaculateFoliageLevelBounds() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CaculateLandscapeLevelBounds`

```text
CaculateLandscapeLevelBounds() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ALevelScriptActor.json -->

# ALevelScriptActor

ALevelScriptActor is the base class for classes generated by 
  ULevelScriptBlueprints. ALevelScriptActor instances are hidden actors that 
  exist within a level, and can execute level-wide logic (operating on specific
  actor instances within the level). The level-script's functionality is defined
  inside the ULevelScriptBlueprint itself (using the blueprint's node-based 
  interface).
 
  @see AActor
  @see ULevelScriptBlueprint
  @see UBlueprint

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bInputEnabled` | `uint32` | - |

## Functions

### `RemoteEvent`

```text
RemoteEvent(EventName: FName) -> bool
```

Tries to find an event named "EventName" on all other levels, and calls it

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EventName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetCinematicMode`

```text
SetCinematicMode(bCinematicMode: bool, bHidePlayer: bool, bAffectsHUD: bool, bAffectsMovement: bool, bAffectsTurning: bool) -> void
```

Sets the cinematic mode on all PlayerControllers

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bCinematicMode` | `bool` | - |
| `bHidePlayer` | `bool` | specify true to hide the player's pawn (only relevant if bInCinematicMode is true) |
| `bAffectsHUD` | `bool` | specify true if we should showhide the HUD to match the value of bCinematicMode |
| `bAffectsMovement` | `bool` | specify true to disable movement in cinematic mode, enable it when leaving |
| `bAffectsTurning` | `bool` | specify true to disable turning in cinematic mode or enable it when leaving |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `LevelReset`

```text
LevelReset() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `WorldOriginLocationChanged`

```text
WorldOriginLocationChanged(OldOriginLocation: FIntVector, NewOriginLocation: FIntVector) -> void
```

Event called on world origin location changes

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldOriginLocation` | `FIntVector` | Previous world origin location |
| `NewOriginLocation` | `FIntVector` | New world origin location |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ALevelSequenceActor.json -->

# ALevelSequenceActor

Actor responsible for controlling a specific level sequence in the world.

## Inheritance

`AActor` -> `IMovieSceneBindingOwnerInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bAutoPlay` | `bool` | - |
| `PlaybackSettings` | `FMovieSceneSequencePlaybackSettings` | - |
| `SequencePlayer` | `ULevelSequencePlayer *` | - |
| `LevelSequence` | `FSoftObjectPath` | - |
| `TempLevelSequence` | `ULevelSequence *` | - |
| `AdditionalEventReceivers` | `TArray < AActor * >` | - |
| `BurnInOptions` | `ULevelSequenceBurnInOptions *` | - |
| `BindingOverrides` | `UMovieSceneBindingOverrides *` | Mapping of actors to override the sequence bindings with |
| `bReduceFrequency` | `bool` | - |
| `ReduceFrameCount` | `int32` | - |
| `IgnoreFrameTolerance` | `float` | - |
| `bOverrideInstanceData` | `uint8` | Enable specification of dynamic instance data to be supplied to the sequence during playback |
| `DefaultInstanceData` | `UObject *` | Instance data that can be used to dynamically control sequence evaluation at runtime |
| `BurnInInstance` | `ULevelSequenceBurnIn *` | Burn-in widget |
| `OwnCharacter` | `AActor *` | 所属玩家, feishen, 20210623 |

## Functions

### `GetSequence`

```text
GetSequence(bLoad: bool, bInitializePlayer: bool) -> ULevelSequence *
```

Get the level sequence being played by this actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bLoad` | `bool` | Whether to load the sequence object if it is not already in memory. |
| `bInitializePlayer` | `bool` | Whether to initialize the player when the sequence has been loaded. |

**Returns**

| Type | Description |
|---|---|
| `ULevelSequence *` | Level sequence, or nullptr if not assigned or if it cannot be loaded. |

### `SetSequence`

```text
SetSequence(InSequence: ULevelSequence *) -> void
```

Set the level sequence being played by this actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSequence` | `ULevelSequence *` | The sequence object to set. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetEventReceivers`

```text
SetEventReceivers(AdditionalReceivers: TArray < AActor * >) -> void
```

Set an array of additional actors that will receive events triggerd from this sequence actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AdditionalReceivers` | `TArray < AActor * >` | An array of actors to receive events |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBinding`

```text
SetBinding(Binding: FMovieSceneObjectBindingID, Actors: TArray < AActor * > &, bAllowBindingsFromAsset: bool) -> void
```

Overrides the specified binding with the specified actors, optionally still allowing the bindings defined in the Level Sequence asset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Binding` | `FMovieSceneObjectBindingID` | - |
| `Actors` | `TArray < AActor * > &` | - |
| `bAllowBindingsFromAsset` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddBinding`

```text
AddBinding(Binding: FMovieSceneObjectBindingID, Actor: AActor *, bAllowBindingsFromAsset: bool) -> void
```

Adds the specified actor to the overridden bindings for the specified binding ID, optionally still allowing the bindings defined in the Level Sequence asset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Binding` | `FMovieSceneObjectBindingID` | - |
| `Actor` | `AActor *` | - |
| `bAllowBindingsFromAsset` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveBinding`

```text
RemoveBinding(Binding: FMovieSceneObjectBindingID, Actor: AActor *) -> void
```

Removes the specified actor from the specified binding's actor array

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Binding` | `FMovieSceneObjectBindingID` | - |
| `Actor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetBinding`

```text
ResetBinding(Binding: FMovieSceneObjectBindingID) -> void
```

Resets the specified binding back to the defaults defined by the Level Sequence asset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Binding` | `FMovieSceneObjectBindingID` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetBindings`

```text
ResetBindings() -> void
```

Resets all overridden bindings back to the defaults defined by the Level Sequence asset

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGCAddBinding`

```text
UGCAddBinding(Actor: AActor *, TrackName: FString) -> FMovieSceneObjectBindingID
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |
| `TrackName` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `FMovieSceneObjectBindingID` | - |

### `UGCRemoveBinding`

```text
UGCRemoveBinding(Actor: AActor *, TrackName: FString) -> FMovieSceneObjectBindingID
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |
| `TrackName` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `FMovieSceneObjectBindingID` | - |

### `ReceiveInitailizePlayer`

```text
ReceiveInitailizePlayer() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOwnCharacter`

```text
SetOwnCharacter(Actor: AActor *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ALevelStreamingVolume.json -->

# ALevelStreamingVolume

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StreamingLevelNames` | `TArray < FName >` | Levels names affected by this level streaming volume. |
| `bEditorPreVisOnly` | `uint32` | If true, this streaming volume should only be used for editor streaming level previs. |
| `bDisabled` | `uint32` | If true, this streaming volume is ignored by the streaming volume code.  Used to either<br>	  disable a level streaming volume without disassociating it from the level, or to toggle<br>	  the control of a level's streaming between Kismet and volume streaming. |
| `StreamingUsage` | `TEnumAsByte < enum EStreamingVolumeUsage >` | Determines what this volume is used for, e.g. whether to control loading, loading and visibility or just visibilty (blocking on load) |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ALight.json -->

# ALight

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LightComponent` | `ULightComponent *` | @todo document |
| `bEnabled` | `uint32` | replicated copy of LightComponent's bEnabled property |

## Functions

### `OnRep_bEnabled`

```text
OnRep_bEnabled() -> void
```

Replication Notification Callbacks

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetEnabled`

```text
SetEnabled(bSetEnabled: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bSetEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsEnabled`

```text
IsEnabled() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ToggleEnabled`

```text
ToggleEnabled() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrightness`

```text
SetBrightness(NewBrightness: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewBrightness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBrightness`

```text
GetBrightness() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetLightColor`

```text
SetLightColor(NewLightColor: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLightColor`

```text
GetLightColor() -> FLinearColor
```

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `SetLightFunctionMaterial`

```text
SetLightFunctionMaterial(NewLightFunctionMaterial: UMaterialInterface *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightFunctionMaterial` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLightFunctionScale`

```text
SetLightFunctionScale(NewLightFunctionScale: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightFunctionScale` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLightFunctionFadeDistance`

```text
SetLightFunctionFadeDistance(NewLightFunctionFadeDistance: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightFunctionFadeDistance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCastShadows`

```text
SetCastShadows(bNewValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAffectTranslucentLighting`

```text
SetAffectTranslucentLighting(bNewValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ALightmassPortal.json -->

# ALightmassPortal

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PortalComponent` | `ULightmassPortalComponent *` | - |
| `SpriteComponent` | `UBillboardComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ALODActor.json -->

# ALODActor

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StaticMeshComponent` | `UStaticMeshComponent *` | - |
| `Proxy` | `UHLODProxy *` | The mesh proxy used to display this LOD |
| `Key` | `FName` | The key used to validate this actor against the proxy |
| `LODDrawDistance` | `float` | what distance do you want this to show up instead of SubActors |
| `SubActors` | `TArray < AActor * >` | - |
| `ClusterRefs` | `TArray < FHLODClusterRef >` | - |
| `bIsClusterBasedHLOD` | `bool` | - |
| `HLODGroupName` | `FName` | 该 LODActor 所属的 HLOD Group 名称（来自 WorldSettings HLODSetup[L].HLODGroups[i].GroupName）。<br>	  NAME_None  = Default 重组通道产物，使用关卡默认 BaseMaterial 与默认 DrawDistanceScale。<br>	  非空       = 由 Group 通道产物，烘焙时按此名反查 ProxyBaseMaterial，运行时反查 LODDrawDistanceScale。 |
| `DebugHighlightDuration` | `float` | 调试包围盒持续时间（秒） |
| `DebugHighlightThickness` | `float` | 调试包围盒线宽 |
| `DebugHighlightColor` | `FColor` | 调试包围盒颜色 |
| `bDebugPrintNodeIndex` | `bool` | 是否在 Cluster 节点中心打印 RefNode 索引文本（用于诊断哪个 Node 跑偏） |
| `DebugHighlightRefIndices` | `TArray < int32 >` | 仅高亮指定索引的 ClusterRef（针对 ClusterRefs 数组下标）。<br>	  留空 = 高亮全部 ClusterRefs；填了任意值 = 只高亮命中数组中的 RefIndex。<br>	  例：[0, 2] 表示仅高亮 ClusterRefs[0] 与 ClusterRefs[2]。 |
| `LODLevel` | `int32` | The hierarchy level of this actor; the first tier of HLOD is level 1, the second tier is level 2 and so on. |
| `bCookStripProxyMesh` | `bool` | If true, during Cook the proxy StaticMesh and Proxy reference will be stripped (set to nullptr).<br>	   The mesh asset path is saved to CachedProxyMeshPath for runtime async reload on demand.<br>	   This prevents the HLOD mesh and its textures from being loaded into memory at level load time. |
| `CachedProxyMeshPath` | `FSoftObjectPath` | Soft path to the original static mesh, used to reload after Cook strip or runtime unloading.<br>	   UPROPERTY so it is serialized into the cooked package for runtime async reload.<br>	   FSoftObjectPath is a soft reference (path string only) and does NOT prevent GC. |
| `CachedNumHLODLevels` | `uint8` | - |
| `HLODActorDebugDynamicMaterialInstance` | `UMaterialInstanceDynamic *` | - |
| `SubActorsDebugDynamicMaterialInstance` | `UMaterialInstanceDynamic *` | - |
| `NumTrianglesInSubActors` | `uint32` | Cached number of triangles contained in the SubActors |
| `NumTrianglesInMergedMesh` | `uint32` | Cached number of triangles contained in the SubActors |
| `bOverrideMaterialMergeSettings` | `bool` | Flag whether or not to use the override MaterialSettings when creating the proxy mesh |
| `MaterialSettings` | `FMaterialProxySettings` | Override Material Settings, used when creating the proxy mesh |
| `bOverrideTransitionScreenSize` | `bool` | Flag whether or not to use the override TransitionScreenSize for this proxy mesh |
| `TransitionScreenSize` | `float` | Override transition screen size value, determines the screen size at which the proxy is visible<br>	  The screen size is based around the projected diameter of the bounding<br>	  sphere of the model. i.e. 0.5 means half the screen's maximum dimension. |
| `bOverrideScreenSize` | `bool` | Flag whether or not to use the override ScreenSize when creating the proxy mesh |
| `ScreenSize` | `int32` | Override screen size value used in mesh reduction, when creating the proxy mesh |

## Functions

### `DebugHighlightOwnedClusters`

```text
DebugHighlightOwnedClusters() -> void
```

编辑器调试：高亮本 LODActor 管辖的所有 HISM Cluster 节点包围盒。
	  仅纯 Cluster LODActor 有效。绘制时长由 DebugHighlightDuration 控制，运行时永不调用。

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AMaterialInstanceActor.json -->

# AMaterialInstanceActor

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetActors` | `TArray < AActor * >` | Pointer to actors that we want to control paramters of using Matinee. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AMatineeActor.json -->

# AMatineeActor

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MatineeData` | `UInterpData *` | The matinee data used by this actor |
| `MatineeControllerName` | `FName` | Name of controller node in level script, used to know what function to try and find for events |
| `PlayRate` | `float` | Time multiplier for playback. |
| `bPlayOnLevelLoad` | `uint32` | If true, the matinee will play when the level is loaded. |
| `bForceStartPos` | `uint32` | Lets you force the sequence to always start at ForceStartPosition |
| `ForceStartPosition` | `float` | Time position to always start at if bForceStartPos is set to true. |
| `bLooping` | `uint32` | If sequence should pop back to beginning when finished.<br>	 	Note, if true, will never get CompletedReversed events - sequence must be explicitly Stopped. |
| `bRewindOnPlay` | `uint32` | If true, sequence will rewind itself back to the start each time the Play input is activated. |
| `bNoResetOnRewind` | `uint32` | If true, when rewinding this interpolation, reset the 'initial positions' of any RelateToInitial movements to the current location.<br>	 	This allows the next loop of movement to proceed from the current locations. |
| `bRewindIfAlreadyPlaying` | `uint32` | Only used if bRewindOnPlay if true. Defines what should happen if the Play input is activated while currently playing.<br>	 	If true, hitting Play while currently playing will pop the position back to the start and begin playback over again.<br>	 	If false, hitting Play while currently playing will do nothing. |
| `bDisableRadioFilter` | `uint32` | If true, disables the realtime radio effect |
| `bClientSideOnly` | `uint32` | Indicates that this interpolation does not affect gameplay. This means that:<br>	  -it is not replicated via MatineeActor<br>	  -it is not ticked if no affected Actors are visible<br>	  -on dedicated servers, it is completely ignored |
| `bSkipUpdateIfNotVisible` | `uint32` | if bClientSideOnly is true, whether this matinee should be completely skipped if none of the affected Actors are visible |
| `bIsSkippable` | `uint32` | Lets you skip the matinee with the CANCELMATINEE exec command. Triggers all events to the end along the way. |
| `PreferredSplitScreenNum` | `int32` | Preferred local viewport number (when split screen is active) the director track should associate with, or zero for 'all'. |
| `bDisableMovementInput` | `uint32` | Disable Input from player during play |
| `bDisableLookAtInput` | `uint32` | Disable LookAt Input from player during play |
| `bHidePlayer` | `uint32` | Hide Player Pawn during play |
| `bHideHud` | `uint32` | Hide HUD during play |
| `GroupActorInfos` | `TArray < struct FInterpGroupActorInfo >` | @todo UE4 matinee - shouldnt be directly editable.  Needs a nice interface in matinee |
| `bShouldShowGore` | `uint32` | Cached value that indicates whether or not gore was enabled when the sequence was started |
| `GroupInst` | `TArray < UInterpGroupInst * >` | Instance data for interp groups. One for each variablegroup combination. |
| `CameraCuts` | `TArray < struct FCameraCutInfo >` | Contains the camera world-position for each camera cut in the cinematic. |
| `bIsPlaying` | `uint32` | properties that may change on InterpAction that we need to notify clients about, since the object's properties will not be replicated |
| `bReversePlayback` | `uint32` | - |
| `bPaused` | `uint32` | - |
| `bPendingStop` | `uint32` | - |
| `InterpPosition` | `float` | - |
| `ReplicationForceIsPlaying` | `uint8` | Counter to indicate that play count has changed. Used to work around single frames that go from play-stop-play where bIsPlaying won't get replicated. |

## Functions

### `Play`

```text
Play() -> void
```

Begin playback of the matinee. Only called in game.
	  Will then advance Position by (PlayRate  Deltatime) each time the matinee is ticked.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Stop`

```text
Stop() -> void
```

Stops playback at the current position

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Reverse`

```text
Reverse() -> void
```

Similar to play, but the playback will go backwards until the beginning of the sequence is reached.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Pause`

```text
Pause() -> void
```

Hold playback at its current position. Calling Pause again will continue playback in its current direction.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPosition`

```text
SetPosition(NewPosition: float, bJump: bool) -> void
```

Set the position of the interpolation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPosition` | `float` | the new position to set the interpolation to |
| `bJump` | `bool` | if true, teleport to the new position (don't trigger any events between the old and new positions, etc) |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ChangePlaybackDirection`

```text
ChangePlaybackDirection() -> void
```

Changes the direction of playback (go in reverse if it was going forward, or vice versa)

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLoopingState`

```text
SetLoopingState(bNewLooping: bool) -> void
```

Change the looping behaviour of this matinee

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewLooping` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableGroupByName`

```text
EnableGroupByName(GroupName: FString, bEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GroupName` | `FString` | - |
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnPlay`

```text
OnPlay() -> void
```

Event triggered when the matinee is played for whatever reason

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnStop`

```text
OnStop() -> void
```

Event triggered when the matinee is stopped for whatever reason

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPause`

```text
OnPause() -> void
```

Event triggered when the matinee is paused for whatever reason

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AMatineeActorCameraAnim.json -->

# AMatineeActorCameraAnim

Actor used to control temporary matinees for camera anims that only exist in the editor

## Inheritance

`AMatineeActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CameraAnim` | `UCameraAnim *` | The camera anim we are editing |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ANavigationData.json -->

# ANavigationData

Represents abstract Navigation Data (sub-classed as NavMesh, NavGraph, etc)
 	Used as a common interface for all navigation types handled by NavigationSystem

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RenderingComp` | `UPrimitiveComponent *` | - |
| `NavDataConfig` | `FNavDataConfig` | - |
| `bEnableDrawing` | `uint32` | if set to true then this navigation data will be drawing itself when requested as part of "show navigation" |
| `bForceRebuildOnLoad` | `uint32` | By default navigation will skip the first update after being successfully loaded<br>	  setting bForceRebuildOnLoad to false can override this behavior |
| `bCanBeMainNavData` | `uint32` | If set, navigation data can act as default one in navigation system's queries |
| `bCanSpawnOnRebuild` | `uint32` | If set, navigation data will be spawned in persistent level during rebuild if actor doesn't exist |
| `bRebuildAtRuntime_DEPRECATED` | `uint32` | If true, the NavMesh can be dynamically rebuilt at runtime. |
| `RuntimeGeneration` | `ERuntimeGenerationType` | Navigation data runtime generation options |
| `ObservedPathsTickInterval` | `float` | all observed paths will be processed every ObservedPathsTickInterval seconds |
| `AgentType` | `int32` | AgentType for quick match |
| `DataVersion` | `uint32` | Navigation data versioning. |
| `SupportedAreas` | `TArray < FSupportedAreaData >` | serialized area class - ID mapping |

## Delegates

### `BuildTileSortSeedLocationDelegate`

```text
BuildTileSortSeedLocationDelegate() -> TArray<FVector2D>
```

**Returns**

| Type | Description |
|---|---|
| `TArray` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ANavigationObjectBase.json -->

# ANavigationObjectBase

## Inheritance

`AActor` -> `INavAgentInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CapsuleComponent` | `UCapsuleComponent *` | - |
| `GoodSprite` | `UBillboardComponent *` | Normal editor sprite. |
| `BadSprite` | `UBillboardComponent *` | Used to draw bad collision intersection in editor. |
| `bIsPIEPlayerStart` | `uint32` | True if this nav point was spawned to be a PIE player start. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ANavigationTestingActor.json -->

# ANavigationTestingActor

## Inheritance

`AActor` -> `INavAgentInterface` -> `INavPathObserverInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CapsuleComponent` | `UCapsuleComponent *` | - |
| `InvokerComponent` | `UNavigationInvokerComponent *` | - |
| `bActAsNavigationInvoker` | `uint32` | - |
| `NavAgentProps` | `FNavAgentProperties` | @todo document |
| `QueryingExtent` | `FVector` | - |
| `MyNavData` | `ANavigationData *` | - |
| `ProjectedLocation` | `FVector` | - |
| `ProjectedTile` | `FIntVector` | - |
| `ProjectedPloyId` | `int32` | - |
| `bProjectedLocationValid` | `uint32` | - |
| `bSearchStart` | `uint32` | - |
| `bUseHierarchicalPathfinding` | `uint32` | - |
| `bGatherDetailedInfo` | `uint32` | if set, all steps of A algorithm will be accessible for debugging |
| `bDrawDistanceToWall` | `uint32` | - |
| `bShowNodePool` | `uint32` | show polys from open (orange) and closed (yellow) sets |
| `bShowBestPath` | `uint32` | show current best path |
| `bShowDiffWithPreviousStep` | `uint32` | show which nodes were modified in current A step |
| `bShouldBeVisibleInGame` | `uint32` | - |
| `CostDisplayMode` | `TEnumAsByte < ENavCostDisplay :: Type >` | determines which cost will be shown |
| `TextCanvasOffset` | `FVector2D` | text canvas offset to apply |
| `bPathExist` | `uint32` | - |
| `bPathIsPartial` | `uint32` | - |
| `bPathSearchOutOfNodes` | `uint32` | - |
| `PathfindingTime` | `float` | Time in micro seconds |
| `PathCost` | `float` | - |
| `PathfindingSteps` | `int32` | - |
| `OtherActor` | `ANavigationTestingActor *` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | "None" will result in default filter being used |
| `ShowStepIndex` | `int32` | - |
| `OffsetFromCornersDistance` | `float` | - |
| `EdRenderComp` | `UNavTestRenderingComponent *` | Editor Preview |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ANavLinkProxy.json -->

# ANavLinkProxy

## Inheritance

`AActor` -> `INavLinkHostInterface` -> `INavRelevantInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PointLinks` | `TArray < FNavigationLink >` | Navigation links (point to point) added to navigation data |
| `SegmentLinks` | `TArray < FNavigationSegmentLink >` | Navigation links (segment to segment) added to navigation data<br>		@todo hidden from use until we fix segment links. Not really working now |
| `SmartLinkComp` | `UNavLinkCustomComponent *` | Smart link: can affect path following |
| `bSmartLinkIsRelevant` | `bool` | Smart link: toggle relevancy |
| `EdRenderComp` | `UNavLinkRenderingComponent *` | Editor Preview |
| `SpriteComponent` | `UBillboardComponent *` | - |

## Functions

### `ReceiveSmartLinkReached`

```text
ReceiveSmartLinkReached(Agent: AActor *, Destination: FVector &) -> void
```

called when agent reaches smart link during path following, use ResumePathFollowing() to give control back

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Agent` | `AActor *` | - |
| `Destination` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResumePathFollowing`

```text
ResumePathFollowing(Agent: AActor *) -> void
```

resume normal path following

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Agent` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsSmartLinkEnabled`

```text
IsSmartLinkEnabled() -> bool
```

check if smart link is enabled

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetSmartLinkEnabled`

```text
SetSmartLinkEnabled(bEnabled: bool) -> void
```

change state of smart link

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HasMovingAgents`

```text
HasMovingAgents() -> bool
```

check if any agent is moving through smart link right now

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Delegates

### `OnSmartLinkReached`

```text
OnSmartLinkReached(MovingActor: AActor*, DestinationPoint: const FVector&) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MovingActor` | `AActor*` | - |
| `DestinationPoint` | `const FVector&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ANavMeshBoundsVolume.json -->

# ANavMeshBoundsVolume

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SupportedAgents` | `FNavAgentSelector` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ANavModifierVolume.json -->

# ANavModifierVolume

Allows applying selected AreaClass to navmesh, using Volume's shape

## Inheritance

`AVolume` -> `INavRelevantInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AreaClass` | `TSubclassOf < UNavArea >` | - |

## Functions

### `SetAreaClass`

```text
SetAreaClass(NewAreaClass: TSubclassOf < UNavArea >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAreaClass` | `TSubclassOf < UNavArea >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ANote.json -->

# ANote

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Text` | `FString` | - |
| `SpriteComponent` | `UBillboardComponent *` | - |
| `ArrowComponent` | `UArrowComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AOcean.json -->

# AOcean

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OceanFFTComponent` | `UOceanFFTComponent *` | - |
| `OceanGerstnerComponent` | `UOceanGerstnerComponent *` | UPROPERTY(Category = Rendering, VisibleAnywhere, BlueprintReadOnly, meta = (AllowPrivateAccess = "true"))<br>	class UOceanMeshComponent OceanMeshComponent; |
| `OceanCDLODMeshComponent` | `UOceanCDLODMeshComponent *` | - |
| `Disfield` | `UTexture2D *` | - |
| `IndirectMap` | `UTexture2D *` | - |
| `DFResolutionUintNum` | `FVector2D` | baking information's(collected coastline informations) resolution is multiple of 126, texture is multiple of 128,this para record the multiples |
| `DistanceFieldParas` | `FVector4` | - |
| `bDistanceFieldinfoBaked` | `bool` | UPROPERTY(Category = DistanceField, EditAnywhere, BlueprintReadOnly, meta = (AllowPrivateAccess = "true"))<br>	float DistanceFieldBlurStep; |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APainCausingVolume.json -->

# APainCausingVolume

Volume that causes damage over time to any Actor that overlaps its collision.

## Inheritance

`APhysicsVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bPainCausing` | `uint32` | Whether volume currently causes damage. |
| `DamagePerSec` | `float` | Damage done per second to actors in this volume when bPainCausing=true |
| `DamageType` | `TSubclassOf < UDamageType >` | Type of damage done |
| `PainInterval` | `float` | If pain causing, time between damage applications. |
| `bEntryPain` | `uint32` | if bPainCausing, cause pain when something enters the volume in addition to damage each second |
| `BACKUP_bPainCausing` | `uint32` | Checkpointed bPainCausing value |
| `DamageInstigator` | `AController *` | Controller that gets credit for any damage caused by this volume |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APaperCharacter.json -->

# APaperCharacter

## Inheritance

`ACharacter`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sprite` | `UPaperFlipbookComponent *` | The main skeletal mesh associated with this Character (optional sub-object). |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APaperFlipbookActor.json -->

# APaperFlipbookActor

An instance of a UPaperFlipbook in a level.
 
  This actor is created when you drag a flipbook asset from the content browser into the level, and
  it is just a thin wrapper around a UPaperFlipbookComponent that actually references the asset.

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RenderComponent` | `UPaperFlipbookComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APaperGroupedSpriteActor.json -->

# APaperGroupedSpriteActor

A group of sprites that will be rendered and culled as a single unit
 
  This actor is created when you Merge several sprite components together.
  it is just a thin wrapper around a UPaperGroupedSpriteComponent.

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RenderComponent` | `UPaperGroupedSpriteComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APaperSpriteActor.json -->

# APaperSpriteActor

An instance of a UPaperSprite in a level.
 
  This actor is created when you drag a sprite asset from the content browser into the level, and
  it is just a thin wrapper around a UPaperSpriteComponent that actually references the asset.

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RenderComponent` | `UPaperSpriteComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APaperTerrainActor.json -->

# APaperTerrainActor

An instance of a piece of 2D terrain in the level

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DummyRoot` | `USceneComponent *` | - |
| `SplineComponent` | `UPaperTerrainSplineComponent *` | - |
| `RenderComponent` | `UPaperTerrainComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APaperTileMapActor.json -->

# APaperTileMapActor

An instance of a UPaperTileMap in a level.
 
  This actor is created when you drag a tile map asset from the content browser into the level, and
  it is just a thin wrapper around a UPaperTileMapComponent that actually references the asset.

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RenderComponent` | `UPaperTileMapComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APawn.json -->

# APawn

Pawn is the base class of all actors that can be possessed by players or AI.
  They are the physical representations of players and creatures in a level.

## Inheritance

`AActor` -> `INavAgentInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bUseControllerRotationPitch` | `bool` | If true, this Pawn's pitch will be updated to match the Controller's ControlRotation pitch, if controlled by a PlayerController. |
| `bUseControllerRotationYaw` | `bool` | If true, this Pawn's yaw will be updated to match the Controller's ControlRotation yaw, if controlled by a PlayerController. |
| `bUseControllerRotationRoll` | `bool` | If true, this Pawn's roll will be updated to match the Controller's ControlRotation roll, if controlled by a PlayerController. |
| `bCanAffectNavigationGeneration` | `uint32` | If set to false (default) given pawn instance will never affect navigation generation. <br>	 	Setting it to true will result in using regular AActor's navigation relevancy <br>	 	calculation to check if this pawn instance should affect navigation generation<br>	 	Use SetCanAffectNavigationGeneration to change this value at runtime.<br>	 	Note that modifying this value at runtime will result in any navigation change only if runtime navigation generation is enabled. |
| `bUseViewTranslatedTransform` | `uint8` | - |
| `BaseEyeHeight` | `float` | Base eye height above collision center. |
| `AutoPossessPlayer` | `TEnumAsByte < EAutoReceiveInput :: Type >` | Determines which PlayerController, if any, should automatically possess the pawn when the level starts or when the pawn is spawned.<br>	  @see AutoPossessAI |
| `AutoPossessAI` | `EAutoPossessAI` | Determines when the Pawn creates and is possessed by an AI Controller (on level start, when spawned, etc).<br>	  Only possible if AIControllerClass is set, and ignored if AutoPossessPlayer is enabled.<br>	  @see AutoPossessPlayer |
| `AIControllerClass` | `TSubclassOf < AController >` | Default class to use when pawn is controlled by AI. |
| `PlayerState` | `APlayerState *` | If Pawn is possessed by a player, points to his playerstate.  Needed for network play as controllers are not replicated to clients. |
| `RemoteViewPitch` | `uint8` | Replicated so we can see where remote clients are looking. |
| `LastHitBy` | `AController *` | Controller of the last Actor that caused us damage. |
| `Controller` | `AController *` | Controller currently possessing this Actor |
| `ControlInputVector` | `FVector` | Accumulated control input vector, stored in world space. This is the pending input, which is cleared (zeroed) once consumed.<br>	  @see GetPendingMovementInputVector(), AddMovementInput() |
| `LastControlInputVector` | `FVector` | The last control input vector that was processed by ConsumeMovementInputVector().<br>	  @see GetLastMovementInputVector() |

## Functions

### `GetMovementComponent`

```text
GetMovementComponent() -> UPawnMovementComponent *
```

Return our PawnMovementComponent, if we have one. By default, returns the first PawnMovementComponent found. Native classes that create their own movement component should override this method for more efficiency.

**Returns**

| Type | Description |
|---|---|
| `UPawnMovementComponent *` | - |

### `GetMeshComponent`

```text
GetMeshComponent() -> UMeshComponent *
```

Return our Mesh, if we have one. By default, returns the first MeshComponent found. Native classes that create their own mesh component should override this method for more efficiency.

**Returns**

| Type | Description |
|---|---|
| `UMeshComponent *` | - |

### `SetUseViewTranslatedTransform`

```text
SetUseViewTranslatedTransform(bNewUseViewTranslatedTransform: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewUseViewTranslatedTransform` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PawnMakeNoise`

```text
PawnMakeNoise(Loudness: float, NoiseLocation: FVector, bUseNoiseMakerLocation: bool, NoiseMaker: AActor *) -> void
```

Inform AIControllers that you've made a noise they might hear (they are sent a HearNoise message if they have bHearNoises==true)
	  The instigator of this sound is the pawn which is used to call MakeNoise.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Loudness` | `float` | - is the relative loudness of this noise (range 0.0 to 1.0). Directly affects the hearing range specified by the AI's HearingThreshold. |
| `NoiseLocation` | `FVector` | - Position of noise source. If zero vector, use the actor's location. |
| `bUseNoiseMakerLocation` | `bool` | - If true, use the location of the NoiseMaker rather than NoiseLocation. If false, use NoiseLocation. |
| `NoiseMaker` | `AActor *` | - Which actor is the source of the noise. Not to be confused with the Noise Instigator, which is responsible for the noise (and is the pawn on which this function is called). If not specified, the pawn instigating the noise will be used as the NoiseMaker |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMovementBaseActor`

```text
GetMovementBaseActor(Pawn: APawn *) -> AActor *
```

Gets the owning actor of the Movement Base Component on which the pawn is standing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Pawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `IsControlled`

```text
IsControlled() -> bool
```

See if this actor is currently being controlled

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetController`

```text
GetController() -> AController *
```

Returns controller for this actor.

**Returns**

| Type | Description |
|---|---|
| `AController *` | - |

### `GetControlRotation`

```text
GetControlRotation() -> FRotator
```

Get the rotation of the Controller, often the 'view' rotation of this Pawn.

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `OnRep_Controller`

```text
OnRep_Controller() -> void
```

Called when Controller is replicated

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UseControllerRotationYaw`

```text
UseControllerRotationYaw() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `OnRep_PlayerState`

```text
OnRep_PlayerState() -> void
```

PlayerState Replication Notification Callback

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCanAffectNavigationGeneration`

```text
SetCanAffectNavigationGeneration(bNewValue: bool, bForceUpdate: bool) -> void
```

Use SetCanAffectNavigationGeneration to change this value at runtime.
	 	Note that calling this function at runtime will result in any navigation change only if runtime navigation generation is enabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |
| `bForceUpdate` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetNavAgentLocation`

```text
GetNavAgentLocation() -> FVector
```

Basically retrieved pawn's location on navmesh

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `ReceivePossessed`

```text
ReceivePossessed(NewController: AController *) -> void
```

Event called when the Pawn is possessed by a Controller (normally only occurs on the serverstandalone).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewController` | `AController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveUnpossessed`

```text
ReceiveUnpossessed(OldController: AController *) -> void
```

Event called when the Pawn is no longer possessed by a Controller.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldController` | `AController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsLocallyControlled`

```text
IsLocallyControlled() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if controlled by a local (not network) Controller. |

### `IsPlayerControlled`

```text
IsPlayerControlled() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if controlled by a human player (possessed by a PlayerController). |

### `GetBaseAimRotation`

```text
GetBaseAimRotation() -> FRotator
```

Return the aim rotation for the Pawn.
	  If we have a controller, by default we aim at the player's 'eyes' direction
	  that is by default the Pawn rotation for AI, and camera (crosshair) rotation for human players.

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `DetachFromControllerPendingDestroy`

```text
DetachFromControllerPendingDestroy() -> void
```

Call this function to detach safely pawn from its controller, knowing that we will be destroyed soon.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SpawnDefaultController`

```text
SpawnDefaultController() -> void
```

Spawn default controller for this Pawn, and get possessed by it.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddMovementInput`

```text
AddMovementInput(WorldDirection: FVector, ScaleValue: float, bForce: bool) -> void
```

Add movement input along the given world direction vector (usually normalized) scaled by 'ScaleValue'. If ScaleValue < 0, movement will be in the opposite direction.
	  Base Pawn classes won't automatically apply movement, it's up to the user to do so in a Tick event. Subclasses such as Character and DefaultPawn automatically handle this input and move.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldDirection` | `FVector` | Direction in world space to apply input |
| `ScaleValue` | `float` | Scale to apply to input. This can be used for analog input, ie a value of 0.5 applies half the normal value, while -1.0 would reverse the direction. |
| `bForce` | `bool` | If true always add the input, ignoring the result of IsMoveInputIgnored(). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPendingMovementInputVector`

```text
GetPendingMovementInputVector() -> FVector
```

Return the pending input vector in world space. This is the most up-to-date value of the input vector, pending ConsumeMovementInputVector() which clears it,
	  Usually only a PawnMovementComponent will want to read this value, or the Pawn itself if it is responsible for movement.

**Returns**

| Type | Description |
|---|---|
| `FVector` | The pending input vector in world space. |

### `GetLastMovementInputVector`

```text
GetLastMovementInputVector() -> FVector
```

Return the last input vector in world space that was processed by ConsumeMovementInputVector(), which is usually done by the Pawn or PawnMovementComponent.
	  Any user that needs to know about the input that last affected movement should use this function.
	  For example an animation update would want to use this, since by default the order of updates in a frame is:
	  PlayerController (device input) -> MovementComponent -> Pawn -> Mesh (animations)

**Returns**

| Type | Description |
|---|---|
| `FVector` | The last input vector in world space that was processed by ConsumeMovementInputVector(). |

### `ConsumeMovementInputVector`

```text
ConsumeMovementInputVector() -> FVector
```

Returns the pending input vector and resets it to zero.
	  This should be used during a movement update (by the Pawn or PawnMovementComponent) to prevent accumulation of control input between frames.
	  Copies the pending input vector to the saved input vector (GetLastMovementInputVector()).

**Returns**

| Type | Description |
|---|---|
| `FVector` | The pending input vector. |

### `AddControllerPitchInput`

```text
AddControllerPitchInput(Val: float) -> void
```

Add input (affecting Pitch) to the Controller's ControlRotation, if it is a local PlayerController.
	  This value is multiplied by the PlayerController's InputPitchScale value.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Val` | `float` | Amount to add to Pitch. This value is multiplied by the PlayerController's InputPitchScale value. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddControllerYawInput`

```text
AddControllerYawInput(Val: float) -> void
```

Add input (affecting Yaw) to the Controller's ControlRotation, if it is a local PlayerController.
	  This value is multiplied by the PlayerController's InputYawScale value.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Val` | `float` | Amount to add to Yaw. This value is multiplied by the PlayerController's InputYawScale value. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddControllerRollInput`

```text
AddControllerRollInput(Val: float) -> void
```

Add input (affecting Roll) to the Controller's ControlRotation, if it is a local PlayerController.
	  This value is multiplied by the PlayerController's InputRollScale value.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Val` | `float` | Amount to add to Roll. This value is multiplied by the PlayerController's InputRollScale value. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsMoveInputIgnored`

```text
IsMoveInputIgnored() -> bool
```

Helper to see if move input is ignored. If our controller is a PlayerController, checks Controller->IsMoveInputIgnored().

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `LaunchPawn`

```text
LaunchPawn(LaunchVelocity: FVector, bXYOverride: bool, bZOverride: bool) -> void
```

(Deprecated) Launch Character with LaunchVelocity

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LaunchVelocity` | `FVector` | - |
| `bXYOverride` | `bool` | - |
| `bZOverride` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_GetMovementInputVector`

```text
K2_GetMovementInputVector() -> FVector
```

(Deprecated) Return the input vector in world space.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

## Delegates

### `OnControllerArrived`

```text
OnControllerArrived() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPawnClientRestart`

```text
OnPawnClientRestart() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APESkillProjectileBase.json -->

# APESkillProjectileBase

通用抛体V2

## Inheritance

`AUniversalProjectileCore`

## Events

### `ReceiveOnImpactBP`

```text
ReceiveOnImpactBP(ImpactResult: FHitResult &, TargetData: FPESkillTargetData &) -> void
```

碰撞时处理Action前的额外接口
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `FHitResult &` | - |
| `TargetData` | `FPESkillTargetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PostReceiveOnImpactBP`

```text
PostReceiveOnImpactBP(ImpactResult: FHitResult &, TargetData: FPESkillTargetData &) -> void
```

碰撞处理Action结束后的额外接口
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `FHitResult &` | - |
| `TargetData` | `FPESkillTargetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveStoppedBP`

```text
ReceiveStoppedBP(LastHitResult: FHitResult &) -> void
```

完全停止后的额外接口
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LastHitResult` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SearchTargetActorByPriorityBP`

```text
SearchTargetActorByPriorityBP(InActors: TArray < AActor * > &, CurrentTarget: AActor *) -> AActor *
```

弹射轨迹的自定义优先级算法
	 生效范围：S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActors` | `TArray < AActor * > &` | 传入的Actor数组 |
| `CurrentTarget` | `AActor *` | 当前碰撞对象 |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | AActor 最后返回的结果对象 |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APhysicsConstraintActor.json -->

# APhysicsConstraintActor

## Inheritance

`ARigidBodyBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConstraintComp` | `UPhysicsConstraintComponent *` | - |
| `ConstraintActor1_DEPRECATED` | `AActor *` | - |
| `ConstraintActor2_DEPRECATED` | `AActor *` | - |
| `bDisableCollision_DEPRECATED` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APhysicsThruster.json -->

# APhysicsThruster

Attach one of these on an object using physics simulation and it will apply a force down the negative-X direction
 	ie. point X in the direction you want the thrust in.

## Inheritance

`ARigidBodyBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ThrusterComponent` | `UPhysicsThrusterComponent *` | Thruster component |
| `ArrowComponent` | `UArrowComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APhysicsVolume.json -->

# APhysicsVolume

PhysicsVolume: A bounding volume which affects actor physics.
  Each AActor is affected at any time by one PhysicsVolume.

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TerminalVelocity` | `float` | Terminal velocity of pawns using CharacterMovement when falling. |
| `Priority` | `int32` | Determines which PhysicsVolume takes precedence if they overlap (higher number = higher priority). |
| `FluidFriction` | `float` | This property controls the amount of friction applied by the volume as pawns using CharacterMovement move through it. The higher this value, the harder it will feel to move through |
| `bWaterVolume` | `uint32` | True if this volume contains a fluid like water |
| `bPhysicsOnContact` | `uint32` | By default, the origin of an AActor must be inside a PhysicsVolume for it to affect the actor. However if this flag is true, the other actor only has to touch the volume to be affected by it. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/%E5%9C%B0%E9%9D%A2%E5%8F%AF%E6%8B%BE%E5%8F%96%E7%89%A9%E7%B1%BB/APickUpWrapperActor.json -->

# APickUpWrapperActor

地面可拾取物类

## Inheritance

`AUAENetActor` -> `IGeneratorActorInterface` -> `IPickupInterface` -> `IPickupCustomInterface` -> `IObjectPoolInterface` -> `IManagedActorInterface` -> `IDropActorCurveInterface` -> `IDropItemPerformanceInterface` -> `ILuaInterface` -> `IInteractorInterface` -> `IScopeInteractionInterface`

## Delegates

### `UGC_PickUpWrapperHideDelegate`

```text
UGC_PickUpWrapperHideDelegate(InRefreshTimeStamp: float) -> void
```

生效范围:SC
	 可拾取道具隐藏事件委托

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRefreshTimeStamp` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_PickUpWrapperShowDelegate`

```text
UGC_PickUpWrapperShowDelegate() -> void
```

生效范围:S
	 可拾取道具显示事件委托

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_PickUpWrapperDestroyDelegate`

```text
UGC_PickUpWrapperDestroyDelegate() -> void
```

生效范围:SC
	 可拾取道具销毁事件委托

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APixelProjectedReflection.json -->

# APixelProjectedReflection

## Inheritance

`ASceneCapture`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PixelProjectedReflectionComponent` | `UPixelProjectedReflectionComponent *` | Planar reflection component. |
| `bShowPreviewPlane` | `bool` | - |
| `SpriteComponent` | `UBillboardComponent *` | - |

## Functions

### `OnInterpToggle`

```text
OnInterpToggle(bEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APixelProjectedReflectionHeightAdjustmentVolume.json -->

# APixelProjectedReflectionHeightAdjustmentVolume

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DestinationHeight` | `float` | - |
| `FadeTime` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APixelProjectedReflectionVisibilityVolume.json -->

# APixelProjectedReflectionVisibilityVolume

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaxDrawDistance` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APlanarReflection.json -->

# APlanarReflection

## Inheritance

`ASceneCapture`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PlanarReflectionComponent` | `UPlanarReflectionComponent *` | Planar reflection component. |
| `bShowPreviewPlane` | `bool` | - |
| `SpriteComponent` | `UBillboardComponent *` | - |

## Functions

### `OnInterpToggle`

```text
OnInterpToggle(bEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APlayerCameraManager.json -->

# APlayerCameraManager

A PlayerCameraManager is responsible for managing the camera for a particular
  player. It defines the final view properties used by other systems (e.g. the renderer),
  meaning you can think of it as your virtual eyeball in the world. It can compute the 
  final camera properties directly, or it can arbitrateblend between other objects or 
  actors that influence the camera (e.g. blending from one CameraActor to another).
  
  The PlayerCameraManagers primary external responsibility is to reliably respond to
  various Get() functions, such as GetCameraViewPoint. Most everything else is
  implementation detail and overrideable by user projects.
  
  By default, a PlayerCameraManager maintains a "view target", which is the primary actor
  the camera is associated with. It can also apply various "post" effects to the final 
  view state, such as camera animations, shakes, post-process effects or special 
  effects such as dirt on the lens.

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PCOwner` | `APlayerController *` | PlayerController that owns this Camera actor |
| `TransformComponent` | `USceneComponent *` | Dummy component we can use to attach things to the camera. |
| `DefaultFOV` | `float` | FOV to use by default. |
| `DefaultOrthoWidth` | `float` | The default desired width (in world units) of the orthographic view (ignored in Perspective mode) |
| `DefaultAspectRatio` | `float` | Default aspect ratio (used when a view target override the aspect ratio and bConstrainAspectRatio is set; most of the time the value from a camera component will be used instead) |
| `CameraCache` | `FCameraCacheEntry` | Cached camera properties. |
| `LastFrameCameraCache` | `FCameraCacheEntry` | Cached camera properties, one frame old. |
| `ViewTarget` | `FTViewTarget` | Current ViewTarget |
| `PendingViewTarget` | `FTViewTarget` | Pending view target for blending |
| `CachedViewPOV` | `FMinimalViewInfo` | If This POV is not null, Use this Value to Blend Target |
| `ModifierList` | `TArray < UCameraModifier * >` | List of active camera modifier instances that have a chance to update the final camera POV |
| `DefaultModifiers` | `TArray < TSubclassOf < UCameraModifier > >` | List of modifiers to create by default for this camera |
| `FreeCamDistance` | `float` | Distance to place free camera from view target (used in certain CameraStyles) |
| `FreeCamOffset` | `FVector` | Offset to Z free camera position (used in certain CameraStyles) |
| `ViewTargetOffset` | `FVector` | Offset to view target (used in certain CameraStyles) |
| `CameraLensEffects` | `TArray < AEmitterCameraLensEffectBase * >` | CameraBlood emitter attached to this camera |
| `CachedCameraShakeMod` | `UCameraModifier_CameraShake *` | Cached ref to modifier for code-driven screen shakes |
| `AnimInstPool` | `UCameraAnimInst *` | Internal pool of camera anim instance objects available for playing camera animations. Defines the max number of camera anims that can play simultaneously. |
| `PostProcessBlendCache` | `TArray < struct FPostProcessSettings >` | Internal pool of camera anim instance objects available for playing camera animations. Defines the max number of camera anims that can play simultaneously. <br>	class UCameraAnimInst AnimInstPool[8];    MAX_ACTIVE_CAMERA_ANIMS @fixme constant <br>	 Internal list of active post process effects. Parallel array to PostProcessBlendCacheWeights. |
| `ActiveAnims` | `TArray < UCameraAnimInst * >` | Array of camera anim instances that are currently playing and in-use |
| `FreeAnims` | `TArray < UCameraAnimInst * >` | Array of camera anim instances that are not playing and available to be used. |
| `AnimCameraActor` | `ACameraActor *` | Internal. Receives the output of individual camera animations. |
| `bIsOrthographic` | `uint32` | True when this camera should use an orthographic perspective instead of FOV |
| `bDefaultConstrainAspectRatio` | `uint32` | True if black bars should be added if the destination view has a different aspect ratio (only used when a view target doesn't specify whether or not to constrain the aspect ratio; most of the time the value from a camera component is used instead) |
| `bUseClientSideCameraUpdates` | `uint32` | True if server will use camera positions replicated from the client instead of calculating them locally. |
| `bGameCameraCutThisFrame` | `uint32` | True if we did a camera cut this frame. Automatically reset to false every frame.<br>	  This flag affects various things in the renderer (such as whether to use the occlusion queries from last frame, and motion blur). |
| `SendServerUpdateCameraInterval` | `float` | - |
| `ViewPitchMin` | `float` | Minimum view pitch, in degrees. |
| `ViewPitchMax` | `float` | Maximum view pitch, in degrees. |
| `ViewYawMin` | `float` | Minimum view yaw, in degrees. |
| `ViewYawMax` | `float` | Maximum view yaw, in degrees. |
| `ViewRollMin` | `float` | Minimum view roll, in degrees. |
| `ViewRollMax` | `float` | Maximum view roll, in degrees. |
| `BaseCamAnimTrans` | `FTransform` | - |
| `NotifyCameraActor` | `ACameraActor *` | - |

## Functions

### `SetViewPitchMin`

```text
SetViewPitchMin(InViewPitchMin: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InViewPitchMin` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetViewPitchMin`

```text
GetViewPitchMin() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetViewPitchMax`

```text
SetViewPitchMax(InViewPitchMax: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InViewPitchMax` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetViewPitchMax`

```text
GetViewPitchMax() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `PhotographyCameraModify`

```text
PhotographyCameraModify(NewCameraLocation: FVector, PreviousCameraLocation: FVector, OriginalCameraLocation: FVector, ResultCameraLocation: FVector &) -> void
```

Implementable blueprint hook to allow a PlayerCameraManager subclass to
	 constrain or otherwise modify the camera during free-camera photography.
	 For example, a blueprint may wish to limit the distance from the camera's
	 original point, or forbid the camera from passing through walls.
	 NewCameraLocation contains the proposed new camera location.
	 PreviousCameraLocation contains the camera location in the previous frame.
	 OriginalCameraLocation contains the camera location before the game was put
	 into photography mode.
	 Return ResultCameraLocation as modified according to your constraints.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewCameraLocation` | `FVector` | - |
| `PreviousCameraLocation` | `FVector` | - |
| `OriginalCameraLocation` | `FVector` | - |
| `ResultCameraLocation` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPhotographySessionStart`

```text
OnPhotographySessionStart() -> void
```

Event triggered upon entering Photography mode (before pausing, if
	 r.Photography.AutoPause is 1).

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPhotographySessionEnd`

```text
OnPhotographySessionEnd() -> void
```

Event triggered upon leaving Photography mode (after unpausing, if
	 r.Photography.AutoPause is 1).

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPhotographyMultiPartCaptureStart`

```text
OnPhotographyMultiPartCaptureStart() -> void
```

Event triggered upon the start of a multi-part photograph capture (i.e. a
	 stereoscopic or 360-degree shot).  This is an ideal time to turn off
	 rendering effects that tile badly (UI, subtitles, vignette, very aggressive
	 bloom, etc; most of these are automatically disabled when
	 r.Photography.AutoPostprocess is 1).

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPhotographyMultiPartCaptureEnd`

```text
OnPhotographyMultiPartCaptureEnd() -> void
```

Event triggered upon the end of a multi-part photograph capture, when manual
	 free-roaming photographic camera control is about to be returned to the user.
	 Here you may re-enable whatever was turned off within
	 OnPhotographyMultiPartCaptureStart.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BlueprintUpdateCamera`

```text
BlueprintUpdateCamera(CameraTarget: AActor *, NewCameraLocation: FVector &, NewCameraRotation: FRotator &, NewCameraFOV: float &) -> bool
```

Blueprint hook to allow blueprints to override existing camera behavior or implement custom cameras.
	  If this function returns true, we will use the given returned values and skip further calculations to determine
	  final camera POV.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CameraTarget` | `AActor *` | - |
| `NewCameraLocation` | `FVector &` | - |
| `NewCameraRotation` | `FRotator &` | - |
| `NewCameraFOV` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetOwningPlayerController`

```text
GetOwningPlayerController() -> APlayerController *
```

Returns the PlayerController that owns this camera.

**Returns**

| Type | Description |
|---|---|
| `APlayerController *` | - |

### `SetCachedViewPOV`

```text
SetCachedViewPOV(Setup: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Setup` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetViewTarget`

```text
GetViewTarget() -> AActor *
```

**Returns**

| Type | Description |
|---|---|
| `AActor *` | the current ViewTarget. |

### `AddNewCameraModifier`

```text
AddNewCameraModifier(ModifierClass: TSubclassOf < UCameraModifier >) -> UCameraModifier *
```

Creates and initializes a new camera modifier of the specified class.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ModifierClass` | `TSubclassOf < UCameraModifier >` | - The class of camera modifier to create. |

**Returns**

| Type | Description |
|---|---|
| `UCameraModifier *` | Returns the newly created camera modifier. |

### `FindCameraModifierByClass`

```text
FindCameraModifierByClass(ModifierClass: TSubclassOf < UCameraModifier >, bIncludeSuper: bool) -> UCameraModifier *
```

Returns camera modifier for this camera of the given class, if it exists. 
	  Exact class match only. If there are multiple modifiers of the same class, the first one is returned.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ModifierClass` | `TSubclassOf < UCameraModifier >` | - |
| `bIncludeSuper` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `UCameraModifier *` | - |

### `RemoveCameraModifier`

```text
RemoveCameraModifier(ModifierToRemove: UCameraModifier *) -> bool
```

Removes the given camera modifier from this camera (if it's on the camera in the first place) and discards it.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ModifierToRemove` | `UCameraModifier *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if successfully removed, false otherwise. |

### `GetFOVAngle`

```text
GetFOVAngle() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | Returns the camera's current full FOV angle, in degrees. |

### `SetFOV`

```text
SetFOV(NewFOV: float) -> void
```

Locks the FOV to the given value.  Unlock with UnlockFOV.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewFOV` | `float` | - New full FOV angle to use, in degrees. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnlockFOV`

```text
UnlockFOV() -> void
```

Unlocks the FOV.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCameraRotation`

```text
GetCameraRotation() -> FRotator
```

**Returns**

| Type | Description |
|---|---|
| `FRotator` | Returns camera's current rotation. |

### `GetCameraLocation`

```text
GetCameraLocation() -> FVector
```

**Returns**

| Type | Description |
|---|---|
| `FVector` | Returns camera's current location. |

### `AddCameraLensEffect`

```text
AddCameraLensEffect(LensEffectEmitterClass: TSubclassOf < AEmitterCameraLensEffectBase >) -> AEmitterCameraLensEffectBase *
```

Creates a camera lens effect of the given class on this camera.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LensEffectEmitterClass` | `TSubclassOf < AEmitterCameraLensEffectBase >` | - Class of lens effect emitter to create. |

**Returns**

| Type | Description |
|---|---|
| `AEmitterCameraLensEffectBase *` | Returns the new emitter actor. |

### `RemoveCameraLensEffect`

```text
RemoveCameraLensEffect(Emitter: AEmitterCameraLensEffectBase *) -> void
```

Removes the given lens effect from the camera.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Emitter` | `AEmitterCameraLensEffectBase *` | - the emitter actor to remove from the camera |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearCameraLensEffects`

```text
ClearCameraLensEffects() -> void
```

Removes all camera lens effects.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlayCameraShake`

```text
PlayCameraShake(ShakeClass: TSubclassOf < UCameraShake >, Scale: float, PlaySpace: ECameraAnimPlaySpace :: Type, UserPlaySpaceRot: FRotator) -> UCameraShake *
```

Plays a camera shake on this camera.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ShakeClass` | `TSubclassOf < UCameraShake >` | - |
| `Scale` | `float` | - Scalar defining how "intense" to play the shake. 1.0 is normal (as authored). |
| `PlaySpace` | `ECameraAnimPlaySpace :: Type` | - Which coordinate system to play the shake in (affects oscillations and camera anims) |
| `UserPlaySpaceRot` | `FRotator` | - Coordinate system to play shake when PlaySpace == CAPS_UserDefined. |

**Returns**

| Type | Description |
|---|---|
| `UCameraShake *` | - |

### `PlayCameraShakeWithWorldLocation`

```text
PlayCameraShakeWithWorldLocation(ShakeClass: TSubclassOf < UCameraShake >, WorldLocation: FVector, Scale: float, PlaySpace: ECameraAnimPlaySpace :: Type, UserPlaySpaceRot: FRotator) -> UCameraShake *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ShakeClass` | `TSubclassOf < UCameraShake >` | - |
| `WorldLocation` | `FVector` | - |
| `Scale` | `float` | - |
| `PlaySpace` | `ECameraAnimPlaySpace :: Type` | - |
| `UserPlaySpaceRot` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `UCameraShake *` | - |

### `StopCameraShake`

```text
StopCameraShake(ShakeInstance: UCameraShake *, bImmediately: bool) -> void
```

Immediately stops the given shake instance and invalidates it.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ShakeInstance` | `UCameraShake *` | - |
| `bImmediately` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopAllInstancesOfCameraShake`

```text
StopAllInstancesOfCameraShake(Shake: TSubclassOf < UCameraShake >, bImmediately: bool) -> void
```

Stops playing CameraShake of the given class.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Shake` | `TSubclassOf < UCameraShake >` | - |
| `bImmediately` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopAllCameraShakes`

```text
StopAllCameraShakes(bImmediately: bool) -> void
```

Stops all active camera shakes on this camera.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bImmediately` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StartCameraFade`

```text
StartCameraFade(FromAlpha: float, ToAlpha: float, Duration: float, Color: FLinearColor, bShouldFadeAudio: bool, bHoldWhenFinished: bool) -> void
```

Does a camera fade tofrom a solid color.  Animates automatically.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FromAlpha` | `float` | - Alpha at which to begin the fade. Range [0..1], where 0 is fully transparent and 1 is fully opaque solid color. |
| `ToAlpha` | `float` | - Alpha at which to finish the fade. |
| `Duration` | `float` | - How long the fade should take, in seconds. |
| `Color` | `FLinearColor` | - Color to fade tofrom. |
| `bShouldFadeAudio` | `bool` | - True to fade audio volume along with the alpha of the solid color. |
| `bHoldWhenFinished` | `bool` | - True for fade to hold at the ToAlpha until explicitly stopped (e.g. with StopCameraFade) |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopCameraFade`

```text
StopCameraFade() -> void
```

Stops camera fading.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetManualCameraFade`

```text
SetManualCameraFade(InFadeAmount: float, Color: FLinearColor, bInFadeAudio: bool) -> void
```

Turns on camera fading at the given opacity. Does not auto-animate, allowing user to animate themselves.
	  Call StopCameraFade to turn fading back off.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFadeAmount` | `float` | - |
| `Color` | `FLinearColor` | - |
| `bInFadeAudio` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlayCameraAnim`

```text
PlayCameraAnim(Anim: UCameraAnim *, Rate: float, Scale: float, BlendInTime: float, BlendOutTime: float, bLoop: bool, bRandomStartTime: bool, Duration: float, PlaySpace: ECameraAnimPlaySpace :: Type, UserPlaySpaceRot: FRotator) -> UCameraAnimInst *
```

Play the indicated CameraAnim on this camera.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Anim` | `UCameraAnim *` | The animation that should play on this instance. |
| `Rate` | `float` | How fast to play the animation. 1.0 is normal. |
| `Scale` | `float` | How "intense" to play the animation. 1.0 is normal. |
| `BlendInTime` | `float` | Time to linearly ramp in. |
| `BlendOutTime` | `float` | Time to linearly ramp out. |
| `bLoop` | `bool` | True to loop the animation if it hits the end. |
| `bRandomStartTime` | `bool` | Whether or not to choose a random time to start playing. Useful with bLoop=true and a duration to randomize things like shakes. |
| `Duration` | `float` | Optional total playtime for this animation, including blends. 0 means to use animations natural duration, or infinite if looping. |
| `PlaySpace` | `ECameraAnimPlaySpace :: Type` | Which space to play the animation in. |
| `UserPlaySpaceRot` | `FRotator` | Custom play space, used when PlaySpace is UserDefined. |

**Returns**

| Type | Description |
|---|---|
| `UCameraAnimInst *` | The CameraAnim instance, which can be stored to manipulatestop the anim after the fact. |

### `StopAllInstancesOfCameraAnim`

```text
StopAllInstancesOfCameraAnim(Anim: UCameraAnim *, bImmediate: bool) -> void
```

Stop playing all instances of the indicated CameraAnim.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Anim` | `UCameraAnim *` | - |
| `bImmediate` | `bool` | True to stop it right now and ignore blend out, false to let it blend out as indicated. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopCameraAnimInst`

```text
StopCameraAnimInst(AnimInst: UCameraAnimInst *, bImmediate: bool) -> void
```

Stops the given CameraAnimInst from playing.  The given pointer should be considered invalid after this.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AnimInst` | `UCameraAnimInst *` | - |
| `bImmediate` | `bool` | True to stop it right now and ignore blend out, false to let it blend out as indicated. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopAllCameraAnims`

```text
StopAllCameraAnims(bImmediate: bool) -> void
```

Stop playing all CameraAnims on this CameraManager.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bImmediate` | `bool` | True to stop it right now and ignore blend out, false to let it blend out as indicated. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `PostViewPitchMinChangedDelegate`

```text
PostViewPitchMinChangedDelegate(OldViewPitchMin: float, NewViewPitchMin: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldViewPitchMin` | `float` | - |
| `NewViewPitchMin` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PostViewPitchMaxChangedDelegate`

```text
PostViewPitchMaxChangedDelegate(OldViewPitchMax: float, NewViewPitchMax: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldViewPitchMax` | `float` | - |
| `NewViewPitchMax` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APlayerController.json -->

# APlayerController

PlayerControllers are used by human players to control Pawns.
 
  ControlRotation (accessed via GetControlRotation()), determines the aiming
  orientation of the controlled Pawn.
 
  In networked games, PlayerControllers exist on the server for every player-controlled pawn,
  and also on the controlling client's machine. They do NOT exist on a client's
  machine for pawns controlled by remote players elsewhere on the network.

## Inheritance

`AController`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Player` | `UPlayer *` | UPlayer associated with this PlayerController.  Could be a local player or a net connection. |
| `AcknowledgedPawn` | `APawn *` | Used in net games so client can acknowledge it possessed a specific pawn. |
| `ControllingDirTrackInst` | `UInterpTrackInstDirector *` | Director track that's currently possessing this player controller, or none if not possessed. |
| `MyHUD` | `AHUD *` | Heads up display associated with this PlayerController. |
| `PlayerCameraManager` | `APlayerCameraManager *` | Camera manager associated with this Player Controller. |
| `PlayerCameraManagerClass` | `TSubclassOf < APlayerCameraManager >` | PlayerCamera class should be set for each game, otherwise Engine.PlayerCameraManager is used |
| `bAutoManageActiveCameraTarget` | `bool` | True to allow this player controller to manage the camera target for you,<br>	  typically by using the possessed pawn as the camera target. Set to false<br>	  if you want to manually control the camera target. |
| `SmoothTargetViewRotationSpeed` | `float` | Interp speed for blending remote view rotation for smoother client updates |
| `HiddenActors` | `TArray < AActor * >` | The actors which the camera shouldn't see - e.g. used to hide actors which the camera penetrates |
| `HiddenPrimitiveComponents` | `TArray < TWeakObjectPtr < UPrimitiveComponent > >` | Explicit components the camera shouldn't see (helpful for external systems to hide a component from a single player) |
| `LastSpectatorStateSynchTime` | `float` | Used to make sure the client is kept synchronized when in a spectator state |
| `LastSpectatorSyncLocation` | `FVector` | Last location synced on the server for a spectator. |
| `LastSpectatorSyncRotation` | `FRotator` | Last rotation synced on the server for a spectator. |
| `ClientCap` | `int32` | Cap set by server on bandwidth from client to server in bytessec (only has impact if >=2600) |
| `CheatManager` | `UCheatManager *` | Object that manages "cheat" commands.  Not instantiated in shipping builds. |
| `CheatClass` | `TSoftClassPtr < UCheatManager >` | Class of my CheatManager.  The Cheat Manager is not created in shipping builds |
| `CheatManagerExtras` | `TArray < UCheatManager * >` | Object that manages "cheat" commands.  Not instantiated in shipping builds. |
| `CheatClassExtras` | `TArray < TSoftClassPtr < UCheatManager > >` | Class of my CheatManager.  The Cheat Manager is not created in shipping builds |
| `PlayerInput` | `UPlayerInput *` | Object that manages player input. |
| `ActiveForceFeedbackEffects` | `TArray < FActiveForceFeedbackEffect >` | - |
| `bPlayerIsWaiting` | `uint32` | True if PlayerController is currently waiting for the match to start or to respawn. Only valid in Spectating state. |
| `NetPlayerIndex` | `uint8` | index identifying players using the same base connection (splitscreen clients)<br>	  Used by netcode to match replicated PlayerControllers to the correct splitscreen viewport and child connection<br>	  replicated via special internal code, not through normal variable replication |
| `PendingSwapConnection` | `UNetConnection *` | this is set on the OLD PlayerController when performing a swap over a network connection<br>	  so we know what connection we're waiting on acknowledgment from to finish destroying this PC<br>	  (or when the connection is closed)<br>	  @see GameModeBase::SwapPlayerControllers() |
| `NetConnection` | `UNetConnection *` | The net connection this controller is communicating on, NULL for local players on server |
| `RotationInput` | `FRotator` | - |
| `InputYawScale` | `float` | Yaw input speed scaling |
| `InputPitchScale` | `float` | Pitch input speed scaling |
| `InputRollScale` | `float` | Roll input speed scaling |
| `bShowMouseCursor` | `uint32` | Whether the mouse cursor should be displayed. |
| `bEnableClickEvents` | `uint32` | Whether actorcomponent click events should be generated. |
| `bEnableTouchEvents` | `uint32` | Whether actorcomponent touch events should be generated. |
| `bEnableMouseOverEvents` | `uint32` | Whether actorcomponent mouse over events should be generated. |
| `bEnableTouchOverEvents` | `uint32` | Whether actorcomponent touch over events should be generated. |
| `bForceFeedbackEnabled` | `uint32` | - |
| `ForceFeedbackScale` | `float` | Scale applied to force feedback values |
| `ClickEventKeys` | `TArray < FKey >` | - |
| `DefaultMouseCursor` | `TEnumAsByte < EMouseCursor :: Type >` | - |
| `CurrentMouseCursor` | `TEnumAsByte < EMouseCursor :: Type >` | - |
| `DefaultClickTraceChannel` | `TEnumAsByte < ECollisionChannel >` | Default trace channel used for determining what world object was clicked on. |
| `CurrentClickTraceChannel` | `TEnumAsByte < ECollisionChannel >` | Trace channel currently being used for determining what world object was clicked on. |
| `HitResultTraceDistance` | `float` | - |
| `bPauseUpdateStreamingState` | `uint32` | - |
| `bActiveReplayViewer` | `uint8` | true means this controller is active now as a replay viewer |
| `bEnableReplayRecord` | `uint8` | true means this controller is enable to record for replay |
| `IsBlockingInput` | `bool` | - |
| `InputWhiteListWhenBlocked` | `TSet < FName >` | - |
| `InputBlackList` | `TSet < FName >` | - |
| `PriorityActionSet` | `TSet < FName >` | - |
| `PriorityActionClusters` | `TArray < FActionCluster >` | - |
| `ActionExecuteState` | `int32` | - |
| `InactiveStateInputComponent` | `UInputComponent *` | InputComponent we use when player is in Inactive state. |
| `bShouldPerformFullTickWhenPaused` | `uint32` | Whether we fully tick when the game is paused, if our tick function is allowed to do so. If false, we do a minimal update during the tick. |
| `CurrentTouchInterface` | `UTouchInterface *` | The currently set touch interface |
| `SpectatorPawn` | `ASpectatorPawn *` | The pawn used when spectating (NULL if not spectating). |
| `SpawnLocation` | `FVector` | The location used internally when there is no pawn or spectator, to know where to spawn the spectator or focus the camera on death. |
| `bIsActorChannelOpen` | `bool` | - |
| `bIsDemoViewController` | `bool` | - |
| `bIsLocalPlayerController` | `bool` | Set during SpawnActor once and never again to indicate the intent of this controller instance (SERVER ONLY) |
| `SeamlessTravelCount` | `uint16` | Counter for this players seamless travels (used along with the below value, to restrict ServerNotifyLoadedWorld) |
| `LastCompletedSeamlessTravelCount` | `uint16` | The value of SeamlessTravelCount, upon the last call to GameModeBase::HandleSeamlessTravelPlayer; used to detect seamless travel |
| `bNeedResetCameraOnPossess` | `bool` | Restart Player by plane do not reset camera!  Engine Modification by czcheng, 2021.6.8 |
| `bNeedResetControlRotator` | `bool` | - |
| `LevelVisibilityInfoList` | `TArray < FLevelVisibilityInfo >` | - |
| `bClientRetryClientRestartFailedProcess` | `bool` | - |

## Functions

### `ServerSetSpectatorWaiting`

```text
ServerSetSpectatorWaiting(bWaiting: bool) -> void
```

Indicate that the Spectator is waiting to joinrespawn.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bWaiting` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientSetSpectatorWaiting`

```text
ClientSetSpectatorWaiting(bWaiting: bool) -> void
```

Indicate that the Spectator is waiting to joinrespawn.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bWaiting` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetActionExecuteState`

```text
SetActionExecuteState(bSuccess: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bSuccess` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetActionExecuteState`

```text
GetActionExecuteState() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `EnableCheats`

```text
EnableCheats() -> void
```

Enables cheats within the game

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FOV`

```text
FOV(NewFOV: float) -> void
```

Set the field of view to NewFOV

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewFOV` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestartLevel`

```text
RestartLevel() -> void
```

Restarts the current level

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `LocalTravel`

```text
LocalTravel(URL: FString &) -> void
```

Causes the client to travel to the given URL

**Parameters**

| Name | Type | Description |
|---|---|---|
| `URL` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientReturnToMainMenu`

```text
ClientReturnToMainMenu(ReturnReason: FString &) -> void
```

Return the client to the main menu gracefully

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ReturnReason` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientRepObjRef`

```text
ClientRepObjRef(Object: UObject *) -> void
```

Development RPC for testing object reference replication

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Pause`

```text
Pause() -> void
```

Command to try to pause the game.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPauseByBlueprint`

```text
SetPauseByBlueprint(bPaused: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bPaused` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetName`

```text
SetName(S: FString &) -> void
```

Trys to set the player's name to the given name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `S` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SwitchLevel`

```text
SwitchLevel(URL: FString &) -> void
```

SwitchLevel to the given MapURL.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `URL` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetHitResultUnderCursor`

```text
GetHitResultUnderCursor(TraceChannel: ECollisionChannel, bTraceComplex: bool, HitResult: FHitResult &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TraceChannel` | `ECollisionChannel` | - |
| `bTraceComplex` | `bool` | - |
| `HitResult` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetHitResultUnderCursorByChannel`

```text
GetHitResultUnderCursorByChannel(TraceChannel: ETraceTypeQuery, bTraceComplex: bool, HitResult: FHitResult &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TraceChannel` | `ETraceTypeQuery` | - |
| `bTraceComplex` | `bool` | - |
| `HitResult` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetHitResultUnderCursorForObjects`

```text
GetHitResultUnderCursorForObjects(ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, bTraceComplex: bool, HitResult: FHitResult &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | - |
| `bTraceComplex` | `bool` | - |
| `HitResult` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetHitResultUnderFinger`

```text
GetHitResultUnderFinger(FingerIndex: ETouchIndex :: Type, TraceChannel: ECollisionChannel, bTraceComplex: bool, HitResult: FHitResult &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex :: Type` | - |
| `TraceChannel` | `ECollisionChannel` | - |
| `bTraceComplex` | `bool` | - |
| `HitResult` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetHitResultUnderFingerByChannel`

```text
GetHitResultUnderFingerByChannel(FingerIndex: ETouchIndex :: Type, TraceChannel: ETraceTypeQuery, bTraceComplex: bool, HitResult: FHitResult &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex :: Type` | - |
| `TraceChannel` | `ETraceTypeQuery` | - |
| `bTraceComplex` | `bool` | - |
| `HitResult` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetHitResultUnderFingerForObjects`

```text
GetHitResultUnderFingerForObjects(FingerIndex: ETouchIndex :: Type, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, bTraceComplex: bool, HitResult: FHitResult &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex :: Type` | - |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | - |
| `bTraceComplex` | `bool` | - |
| `HitResult` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `DeprojectMousePositionToWorld`

```text
DeprojectMousePositionToWorld(WorldLocation: FVector &, WorldDirection: FVector &) -> bool
```

Convert current mouse 2D position to World Space 3D position and direction. Returns false if unable to determine value.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |
| `WorldDirection` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `DeprojectScreenPositionToWorld`

```text
DeprojectScreenPositionToWorld(ScreenX: float, ScreenY: float, WorldLocation: FVector &, WorldDirection: FVector &) -> bool
```

Convert 2D screen position to World Space 3D position and direction. Returns false if unable to determine value.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ScreenX` | `float` | - |
| `ScreenY` | `float` | - |
| `WorldLocation` | `FVector &` | - |
| `WorldDirection` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ProjectWorldLocationToScreen`

```text
ProjectWorldLocationToScreen(WorldLocation: FVector, ScreenLocation: FVector2D &, bPlayerViewportRelative: bool) -> bool
```

Convert a World Space 3D position into a 2D Screen Space position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector` | - |
| `ScreenLocation` | `FVector2D &` | - |
| `bPlayerViewportRelative` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the world coordinate was successfully projected to the screen. |

### `SetMouseLocation`

```text
SetMouseLocation(X: int, Y: int) -> void
```

Positions the mouse cursor in screen space, in pixels.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `X` | `int` | - |
| `Y` | `int` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StartFire`

```text
StartFire(FireModeNum: uint8) -> void
```

Fire the player's currently selected weapon with the optional fire mode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FireModeNum` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientEnableNetworkVoice`

```text
ClientEnableNetworkVoice(bEnable: bool) -> void
```

Tell the client to enable or disable voice chat (not muting)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | enable or disable voice chat |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ToggleSpeaking`

```text
ToggleSpeaking(bInSpeaking: bool) -> void
```

Toggle voice chat on and off

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInSpeaking` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientVoiceHandshakeComplete`

```text
ClientVoiceHandshakeComplete() -> void
```

Tells the client that the server has all the information it needs and that it
	  is ok to start sending voice packets. The server will already send voice packets
	  when this function is called, since it is set server side and then forwarded
	 
	  NOTE: This is done as an RPC instead of variable replication because ordering matters

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerMutePlayer`

```text
ServerMutePlayer(PlayerId: FUniqueNetIdRepl) -> void
```

Tell the server to mute a player for this controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerId` | `FUniqueNetIdRepl` | player id to mute |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerUnmutePlayer`

```text
ServerUnmutePlayer(PlayerId: FUniqueNetIdRepl) -> void
```

Tell the server to unmute a player for this controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerId` | `FUniqueNetIdRepl` | player id to unmute |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientMutePlayer`

```text
ClientMutePlayer(PlayerId: FUniqueNetIdRepl) -> void
```

Tell the client to mute a player for this controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerId` | `FUniqueNetIdRepl` | player id to mute |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientUnmutePlayer`

```text
ClientUnmutePlayer(PlayerId: FUniqueNetIdRepl) -> void
```

Tell the client to unmute a player for this controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerId` | `FUniqueNetIdRepl` | player id to unmute |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ConsoleKey`

```text
ConsoleKey(Key: FKey) -> void
```

Console control commands, useful when remote debugging so you can't touch the console the normal way

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SendToConsole`

```text
SendToConsole(Command: FString &) -> void
```

Sends a command to the console to execute if not shipping version

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Command` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientAddTextureStreamingLoc`

```text
ClientAddTextureStreamingLoc(InLoc: FVector, Duration: float, bOverrideLocation: bool) -> void
```

Adds a location to the texture streaming system for the specified duration.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InLoc` | `FVector` | - |
| `Duration` | `float` | - |
| `bOverrideLocation` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientCancelPendingMapChange`

```text
ClientCancelPendingMapChange() -> void
```

Tells client to cancel any pending map change.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientCapBandwidth`

```text
ClientCapBandwidth(Cap: int32) -> void
```

Set CurrentNetSpeed to the lower of its current value and Cap.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Cap` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientCommitMapChange`

```text
ClientCommitMapChange() -> void
```

Actually performs the level transition prepared by PrepareMapChange().

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientFlushLevelStreaming`

```text
ClientFlushLevelStreaming() -> void
```

Tells the client to block until all pending level streaming actions are complete
	  happens at the end of the tick
	  primarily used to force update the client ASAP at join time

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientForceGarbageCollection`

```text
ClientForceGarbageCollection() -> void
```

Forces GC at the end of the tick on the client

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientGameEnded`

```text
ClientGameEnded(EndGameFocus: AActor *, bIsWinner: bool) -> void
```

Replicated function called by GameHasEnded().

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EndGameFocus` | `AActor *` | - actor to view with camera |
| `bIsWinner` | `bool` | - true if this controller is on winning team |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientGotoState`

```text
ClientGotoState(NewState: FName) -> void
```

Server uses this to force client into NewState .

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewState` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientIgnoreLookInput`

```text
ClientIgnoreLookInput(bIgnore: bool) -> void
```

calls IgnoreLookInput on client

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIgnore` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientIgnoreMoveInput`

```text
ClientIgnoreMoveInput(bIgnore: bool) -> void
```

calls IgnoreMoveInput on client

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIgnore` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientMessage`

```text
ClientMessage(S: FString &, Type: FName, MsgLifeTime: float) -> void
```

Outputs a message to HUD

**Parameters**

| Name | Type | Description |
|---|---|---|
| `S` | `FString &` | - message to display |
| `Type` | `FName` | - @todo document |
| `MsgLifeTime` | `float` | - Optional length of time to display 0 = default time |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientPlayCameraAnim`

```text
ClientPlayCameraAnim(AnimToPlay: UCameraAnim *, Scale: float, Rate: float, BlendInTime: float, BlendOutTime: float, bLoop: bool, bRandomStartTime: bool, Space: ECameraAnimPlaySpace :: Type, CustomPlaySpace: FRotator) -> void
```

Play the indicated CameraAnim on this camera.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AnimToPlay` | `UCameraAnim *` | - Camera animation to play |
| `Scale` | `float` | - "Intensity" scalar. This is the scale at which the anim was first played. |
| `Rate` | `float` | - Multiplier for playback rate. 1.0 = normal. |
| `BlendInTime` | `float` | - Time to interpolate in from zero, for smooth starts |
| `BlendOutTime` | `float` | - Time to interpolate out to zero, for smooth finishes |
| `bLoop` | `bool` | - True if the animation should loop, false otherwise |
| `bRandomStartTime` | `bool` | - Whether or not to choose a random time to start playing. Only really makes sense for bLoop = true |
| `Space` | `ECameraAnimPlaySpace :: Type` | - Animation play area |
| `CustomPlaySpace` | `FRotator` | - Matrix used when Space = CAPS_UserDefined |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientPlayCameraShake`

```text
ClientPlayCameraShake(Shake: TSubclassOf < UCameraShake >, Scale: float, PlaySpace: ECameraAnimPlaySpace :: Type, UserPlaySpaceRot: FRotator) -> void
```

Play Camera Shake

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Shake` | `TSubclassOf < UCameraShake >` | - Camera shake animation to play |
| `Scale` | `float` | - Scalar defining how "intense" to play the anim |
| `PlaySpace` | `ECameraAnimPlaySpace :: Type` | - Which coordinate system to play the shake in (used for CameraAnims within the shake). |
| `UserPlaySpaceRot` | `FRotator` | - Matrix used when PlaySpace = CAPS_UserDefined |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientPlayCameraShakeWithWorldLocation`

```text
ClientPlayCameraShakeWithWorldLocation(Shake: TSubclassOf < UCameraShake >, WorldLocation: FVector, Scale: float, PlaySpace: ECameraAnimPlaySpace :: Type, UserPlaySpaceRot: FRotator) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Shake` | `TSubclassOf < UCameraShake >` | - |
| `WorldLocation` | `FVector` | - |
| `Scale` | `float` | - |
| `PlaySpace` | `ECameraAnimPlaySpace :: Type` | - |
| `UserPlaySpaceRot` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientPlaySound`

```text
ClientPlaySound(Sound: USoundBase *, VolumeMultiplier: float, PitchMultiplier: float) -> void
```

Play sound client-side (so only the client will hear it)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Sound` | `USoundBase *` | - Sound to play |
| `VolumeMultiplier` | `float` | - Volume multiplier to apply to the sound |
| `PitchMultiplier` | `float` | - Pitch multiplier to apply to the sound |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientPlaySoundAtLocation`

```text
ClientPlaySoundAtLocation(Sound: USoundBase *, Location: FVector, VolumeMultiplier: float, PitchMultiplier: float) -> void
```

Play sound client-side at the specified location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Sound` | `USoundBase *` | - Sound to play |
| `Location` | `FVector` | - Location to play the sound at |
| `VolumeMultiplier` | `float` | - Volume multiplier to apply to the sound |
| `PitchMultiplier` | `float` | - Pitch multiplier to apply to the sound |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientPrepareMapChange`

```text
ClientPrepareMapChange(LevelName: FName, bFirst: bool, bLast: bool) -> void
```

Asynchronously loads the given level in preparation for a streaming map transition.
	  the server sends one function per level name since dynamic arrays can't be replicated

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LevelName` | `FName` | - |
| `bFirst` | `bool` | - whether this is the first item in the list (so clear the list first) |
| `bLast` | `bool` | - whether this is the last item in the list (so start preparing the change after receiving it) |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientPrestreamTextures`

```text
ClientPrestreamTextures(ForcedActor: AActor *, ForceDuration: float, bEnableStreaming: bool, CinematicTextureGroups: int32) -> void
```

Forces the streaming system to disregard the normal logic for the specified duration and
	  instead always load all mip-levels for all textures used by the specified actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ForcedActor` | `AActor *` | - The actor whose textures should be forced into memory. |
| `ForceDuration` | `float` | - Number of seconds to keep all mip-levels in memory, disregarding the normal priority logic. |
| `bEnableStreaming` | `bool` | - Whether to start (true) or stop (false) streaming |
| `CinematicTextureGroups` | `int32` | - Bitfield indicating which texture groups that use extra high-resolution mips |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientReset`

```text
ClientReset() -> void
```

Tell client to reset the PlayerController

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientRestart`

```text
ClientRestart(NewPawn: APawn *) -> void
```

Tell client to restart the level

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientSetBlockOnAsyncLoading`

```text
ClientSetBlockOnAsyncLoading() -> void
```

Tells the client to block until all pending level streaming actions are complete.
	  Happens at the end of the tick primarily used to force update the client ASAP at join time.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientSetCameraFade`

```text
ClientSetCameraFade(bEnableFading: bool, FadeColor: FColor, FadeAlpha: FVector2D, FadeTime: float, bFadeAudio: bool) -> void
```

Tell client to fade camera

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableFading` | `bool` | - |
| `FadeColor` | `FColor` | - |
| `FadeAlpha` | `FVector2D` | - |
| `FadeTime` | `float` | - |
| `bFadeAudio` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientSetCameraMode`

```text
ClientSetCameraMode(NewCamMode: FName) -> void
```

Replicated function to set camera style on client

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewCamMode` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientSetCinematicMode`

```text
ClientSetCinematicMode(bInCinematicMode: bool, bAffectsMovement: bool, bAffectsTurning: bool, bAffectsHUD: bool) -> void
```

Called by the server to synchronize cinematic transitions with the client

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInCinematicMode` | `bool` | - |
| `bAffectsMovement` | `bool` | - |
| `bAffectsTurning` | `bool` | - |
| `bAffectsHUD` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientSetForceMipLevelsToBeResident`

```text
ClientSetForceMipLevelsToBeResident(Material: UMaterialInterface *, ForceDuration: float, CinematicTextureGroups: int32) -> void
```

Forces the streaming system to disregard the normal logic for the specified duration and
	  instead always load all mip-levels for all textures used by the specified material.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Material` | `UMaterialInterface *` | - The material whose textures should be forced into memory. |
| `ForceDuration` | `float` | - Number of seconds to keep all mip-levels in memory, disregarding the normal priority logic. |
| `CinematicTextureGroups` | `int32` | - Bitfield indicating which texture groups that use extra high-resolution mips |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientSetHUD`

```text
ClientSetHUD(NewHUDClass: TSubclassOf < AHUD >) -> void
```

Set the client's class of HUD and spawns a new instance of it. If there was already a HUD active, it is destroyed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewHUDClass` | `TSubclassOf < AHUD >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetViewportSize`

```text
GetViewportSize(SizeX: int32 &, SizeY: int32 &) -> void
```

Helper to get the size of the HUD canvas for this player controller.  Returns 0 if there is no HUD

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SizeX` | `int32 &` | - |
| `SizeY` | `int32 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetHUD`

```text
GetHUD() -> AHUD *
```

Gets the HUD currently being used by this player controller

**Returns**

| Type | Description |
|---|---|
| `AHUD *` | - |

### `SetMouseCursorWidget`

```text
SetMouseCursorWidget(Cursor: EMouseCursor :: Type, CursorWidget: UUserWidget *) -> void
```

Sets the Widget for the Mouse Cursor to display

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Cursor` | `EMouseCursor :: Type` | - the cursor to set the widget for |
| `CursorWidget` | `UUserWidget *` | - the widget to set the cursor to |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientSetViewTarget`

```text
ClientSetViewTarget(A: AActor *, TransitionParams: FViewTargetTransitionParams) -> void
```

Set the view target

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `AActor *` | - new actor to set as view target |
| `TransitionParams` | `FViewTargetTransitionParams` | - parameters to use for controlling the transition |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientSpawnCameraLensEffect`

```text
ClientSpawnCameraLensEffect(LensEffectEmitterClass: TSubclassOf < AEmitterCameraLensEffectBase >) -> void
```

Spawn a camera lens effect (e.g. blood).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LensEffectEmitterClass` | `TSubclassOf < AEmitterCameraLensEffectBase >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientClearCameraLensEffects`

```text
ClientClearCameraLensEffects() -> void
```

Removes all Camera Lens Effects.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientStopCameraAnim`

```text
ClientStopCameraAnim(AnimToStop: UCameraAnim *) -> void
```

Stop camera animation on client.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AnimToStop` | `UCameraAnim *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientStopCameraShake`

```text
ClientStopCameraShake(Shake: TSubclassOf < UCameraShake >, bImmediately: bool) -> void
```

Stop camera shake on client.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Shake` | `TSubclassOf < UCameraShake >` | - |
| `bImmediately` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientPlayForceFeedback`

```text
ClientPlayForceFeedback(ForceFeedbackEffect: UForceFeedbackEffect *, bLooping: bool, bIgnoreTimeDilation: bool, Tag: FName) -> void
```

Play a force feedback pattern on the player's controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ForceFeedbackEffect` | `UForceFeedbackEffect *` | The force feedback pattern to play |
| `bLooping` | `bool` | Whether the pattern should be played repeatedly or be a single one shot |
| `bIgnoreTimeDilation` | `bool` | Whether the pattern should ignore time dilation |
| `Tag` | `FName` | A tag that allows stopping of an effect. If another effect with this Tag is playing, it will be stopped and replaced |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientStopForceFeedback`

```text
ClientStopForceFeedback(ForceFeedbackEffect: UForceFeedbackEffect *, Tag: FName) -> void
```

Stops a playing force feedback pattern

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ForceFeedbackEffect` | `UForceFeedbackEffect *` | If set only patterns from that effect will be stopped |
| `Tag` | `FName` | If not none only the pattern with this tag will be stopped |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlayDynamicForceFeedback`

```text
PlayDynamicForceFeedback(Intensity: float, Duration: float, bAffectsLeftLarge: bool, bAffectsLeftSmall: bool, bAffectsRightLarge: bool, bAffectsRightSmall: bool, Action: TEnumAsByte < EDynamicForceFeedbackAction :: Type >, LatentInfo: FLatentActionInfo) -> void
```

Latent action that controls the playing of force feedback
	  Begins playing when Start is called.  Calling Update or Stop if the feedback is not active will have no effect.
	  Completed will execute when Stop is called or the duration ends.
	  When Update is called the Intensity, Duration, and affect values will be updated with the current inputs

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Intensity` | `float` | How strong the feedback should be. Valid values are between 0.0 and 1.0 |
| `Duration` | `float` | How long the feedback should play for. If the value is negative it will play until stopped |
| `bAffectsLeftLarge` | `bool` | - |
| `bAffectsLeftSmall` | `bool` | - |
| `bAffectsRightLarge` | `bool` | - |
| `bAffectsRightSmall` | `bool` | - |
| `Action` | `TEnumAsByte < EDynamicForceFeedbackAction :: Type >` | - |
| `LatentInfo` | `FLatentActionInfo` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlayHapticEffect`

```text
PlayHapticEffect(HapticEffect: UHapticFeedbackEffect_Base *, Hand: EControllerHand, Scale: float, bLoop: bool) -> void
```

Play a haptic feedback curve on the player's controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HapticEffect` | `UHapticFeedbackEffect_Base *` | The haptic effect to play |
| `Hand` | `EControllerHand` | Which hand to play the effect on |
| `Scale` | `float` | Scale between 0.0 and 1.0 on the intensity of playback |
| `bLoop` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopHapticEffect`

```text
StopHapticEffect(Hand: EControllerHand) -> void
```

Stops a playing haptic feedback curve

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Hand` | `EControllerHand` | Which hand to stop the effect for |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHapticsByValue`

```text
SetHapticsByValue(Frequency: float, Amplitude: float, Hand: EControllerHand) -> void
```

Sets the value of the haptics for the specified hand directly, using frequency and amplitude.  NOTE:  If a curve is already
	 playing for this hand, it will be cancelled in favour of the specified values.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Frequency` | `float` | The normalized frequency [0.0, 1.0] to play through the haptics system |
| `Amplitude` | `float` | The normalized amplitude [0.0, 1.0] to set the haptic feedback to |
| `Hand` | `EControllerHand` | Which hand to play the effect on |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetControllerLightColor`

```text
SetControllerLightColor(Color: FColor) -> void
```

Sets the light color of the player's controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Color` | `FColor` | The color for the light to be |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientTravel`

```text
ClientTravel(URL: FString &, TravelType: ETravelType, bSeamless: bool, MapPackageGuid: FGuid) -> void
```

Travel to a different map or IP address. Calls the PreClientTravel event before doing anything.
	  NOTE: This is implemented as a locally executed wrapper for ClientTravelInternal, to avoid API compatability breakage

**Parameters**

| Name | Type | Description |
|---|---|---|
| `URL` | `FString &` | A string containing the mapname (or IP address) to travel to, along with option keyvalue pairs |
| `TravelType` | `ETravelType` | specifies whether the client should append URL options used in previous travels; if true is specified |
| `bSeamless` | `bool` | Indicates whether to use seamless travel (requires TravelType of TRAVEL_Relative) |
| `MapPackageGuid` | `FGuid` | The GUID of the map package to travel to - this is used to find the file when it has been autodownloaded, |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientTravelInternal`

```text
ClientTravelInternal(URL: FString &, TravelType: ETravelType, bSeamless: bool, MapPackageGuid: FGuid) -> void
```

Internal clientside implementation of ClientTravel - use ClientTravel to call this

**Parameters**

| Name | Type | Description |
|---|---|---|
| `URL` | `FString &` | A string containing the mapname (or IP address) to travel to, along with option keyvalue pairs |
| `TravelType` | `ETravelType` | specifies whether the client should append URL options used in previous travels; if true is specified |
| `bSeamless` | `bool` | Indicates whether to use seamless travel (requires TravelType of TRAVEL_Relative) |
| `MapPackageGuid` | `FGuid` | The GUID of the map package to travel to - this is used to find the file when it has been autodownloaded, |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientUpdateLevelStreamingStatus`

```text
ClientUpdateLevelStreamingStatus(PackageName: FName, bNewShouldBeLoaded: bool, bNewShouldBeVisible: bool, bNewShouldBlockOnLoad: bool, LODIndex: int32) -> void
```

Replicated Update streaming status

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PackageName` | `FName` | - Name of the level package name used for loading. |
| `bNewShouldBeLoaded` | `bool` | - Whether the level should be loaded |
| `bNewShouldBeVisible` | `bool` | - Whether the level should be visible if it is loaded |
| `bNewShouldBlockOnLoad` | `bool` | - Whether we want to force a blocking load |
| `LODIndex` | `int32` | - Current LOD index for a streaming level |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientWasKicked`

```text
ClientWasKicked(KickReason: FText &) -> void
```

Notify client they were kicked from the server

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KickReason` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientStartOnlineSession`

```text
ClientStartOnlineSession() -> void
```

Notify client that the session is starting

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientEndOnlineSession`

```text
ClientEndOnlineSession() -> void
```

Notify client that the session is about to start

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientRetryClientRestart`

```text
ClientRetryClientRestart(NewPawn: APawn *) -> void
```

Assign Pawn to player, but avoid calling ClientRestart if we have already accepted this pawn

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientReceiveLocalizedMessage`

```text
ClientReceiveLocalizedMessage(Message: TSubclassOf < ULocalMessage >, Switch: int32, RelatedPlayerState_1: APlayerState *, RelatedPlayerState_2: APlayerState *, OptionalObject: UObject *) -> void
```

send client localized message id

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Message` | `TSubclassOf < ULocalMessage >` | - |
| `Switch` | `int32` | - |
| `RelatedPlayerState_1` | `APlayerState *` | - |
| `RelatedPlayerState_2` | `APlayerState *` | - |
| `OptionalObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerAcknowledgePossession`

```text
ServerAcknowledgePossession(P: APawn *) -> void
```

acknowledge possession of pawn

**Parameters**

| Name | Type | Description |
|---|---|---|
| `P` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerCamera`

```text
ServerCamera(NewMode: FName) -> void
```

change mode of camera

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewMode` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerChangeName`

```text
ServerChangeName(S: FString &) -> void
```

Change name of server

**Parameters**

| Name | Type | Description |
|---|---|---|
| `S` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerNotifyLoadedWorld`

```text
ServerNotifyLoadedWorld(WorldPackageName: FName) -> void
```

Called to notify the server when the client has loaded a new world via seamless traveling

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldPackageName` | `FName` | the name of the world package that was loaded |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerNotifyStreamLevelDisFactor`

```text
ServerNotifyStreamLevelDisFactor(InFactor: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFactor` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerPause`

```text
ServerPause() -> void
```

Replicate pause request to the server

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerRestartPlayer`

```text
ServerRestartPlayer() -> void
```

Attempts to restart this player, generally called from the client upon respawn request.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerSetSpectatorLocation`

```text
ServerSetSpectatorLocation(NewLoc: FVector, NewRot: FRotator) -> void
```

When spectating, updates spectator locationrotation and pings the server to make sure spectating should continue.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLoc` | `FVector` | - |
| `NewRot` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerCheckClientPossession`

```text
ServerCheckClientPossession() -> void
```

Tells the server to make sure the possessed pawn is in sync with the client.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerCheckClientPossessionReliable`

```text
ServerCheckClientPossessionReliable() -> void
```

Reliable version of ServerCheckClientPossession to be used when there is no likely danger of spamming the network.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerShortTimeout`

```text
ServerShortTimeout() -> void
```

Notifies the server that the client has ticked gameplay code, and should no longer get the extended "still loading" timeout grace period

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerUpdateCamera`

```text
ServerUpdateCamera(CamLoc: FVector_NetQuantize, CamPitchAndYaw: int32) -> void
```

If PlayerCamera.bUseClientSideCameraUpdates is set, client will replicate camera positions to the server.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CamLoc` | `FVector_NetQuantize` | - |
| `CamPitchAndYaw` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerUpdateCameraLocation`

```text
ServerUpdateCameraLocation(CamLoc: FVector_NetQuantize) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CamLoc` | `FVector_NetQuantize` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerUpdateLevelVisibility`

```text
ServerUpdateLevelVisibility(PackageName: FName, bIsVisible: bool) -> void
```

Called when the client addsremoves a streamed level
	  the server will only replicate references to Actors in visible levels so that it's impossible to send references to
	  Actors the client has not initialized

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PackageName` | `FName` | the name of the package for the level whose status changed |
| `bIsVisible` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerUpdateLevelListVisibility`

```text
ServerUpdateLevelListVisibility(PackageNames: TArray < FName > &, bIsVisible: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PackageNames` | `TArray < FName > &` | - |
| `bIsVisible` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerUpdateLevelListPackageVisibility`

```text
ServerUpdateLevelListPackageVisibility(PackageInfo: TArray < FLevelVisibilityInfo > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PackageInfo` | `TArray < FLevelVisibilityInfo > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerUpdateLevelIndexListPackageVisibility`

```text
ServerUpdateLevelIndexListPackageVisibility(PackageInfo: TArray < FLevelIndexVisibilityInfo > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PackageInfo` | `TArray < FLevelIndexVisibilityInfo > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerVerifyViewTarget`

```text
ServerVerifyViewTarget() -> void
```

Used by client to request server to confirm current viewtarget (server will respond with ClientSetViewTarget() ).

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerViewNextPlayer`

```text
ServerViewNextPlayer() -> void
```

Move camera to next player on round ended or spectating

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerViewPrevPlayer`

```text
ServerViewPrevPlayer() -> void
```

Move camera to previous player on round ended or spectating

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerViewSelf`

```text
ServerViewSelf(TransitionParams: FViewTargetTransitionParams) -> void
```

Move camera to current user

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TransitionParams` | `FViewTargetTransitionParams` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientTeamMessage`

```text
ClientTeamMessage(SenderPlayerState: APlayerState *, S: FString &, Type: FName, MsgLifeTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SenderPlayerState` | `APlayerState *` | - |
| `S` | `FString &` | - |
| `Type` | `FName` | - |
| `MsgLifeTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerToggleAILogging`

```text
ServerToggleAILogging() -> void
```

Used by UGameplayDebuggingControllerComponent to replicate messages for AI debugging in network games.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddPitchInput`

```text
AddPitchInput(Val: float) -> void
```

Add Pitch (look up) input. This value is multiplied by InputPitchScale.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Val` | `float` | Amount to add to Pitch. This value is multiplied by InputPitchScale. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddYawInput`

```text
AddYawInput(Val: float) -> void
```

Add Yaw (turn) input. This value is multiplied by InputYawScale.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Val` | `float` | Amount to add to Yaw. This value is multiplied by InputYawScale. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddRollInput`

```text
AddRollInput(Val: float) -> void
```

Add Roll input. This value is multiplied by InputRollScale.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Val` | `float` | Amount to add to Roll. This value is multiplied by InputRollScale. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsInputKeyDown`

```text
IsInputKeyDown(Key: FKey) -> bool
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

### `WasInputKeyJustPressed`

```text
WasInputKeyJustPressed(Key: FKey) -> bool
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

### `WasInputKeyJustReleased`

```text
WasInputKeyJustReleased(Key: FKey) -> bool
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

### `GetInputAnalogKeyState`

```text
GetInputAnalogKeyState(Key: FKey) -> float
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

### `GetInputVectorKeyState`

```text
GetInputVectorKeyState(Key: FKey) -> FVector
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

### `GetInputTouchState`

```text
GetInputTouchState(FingerIndex: ETouchIndex :: Type, LocationX: float &, LocationY: float &, bIsCurrentlyPressed: bool &) -> void
```

Retrieves the X and Y screen coordinates of the specified touch key. Returns false if the touch index is not down

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex :: Type` | - |
| `LocationX` | `float &` | - |
| `LocationY` | `float &` | - |
| `bIsCurrentlyPressed` | `bool &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetInputMotionState`

```text
GetInputMotionState(Tilt: FVector &, RotationRate: FVector &, Gravity: FVector &, Acceleration: FVector &) -> void
```

Retrieves the current motion state of the player's input device

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Tilt` | `FVector &` | - |
| `RotationRate` | `FVector &` | - |
| `Gravity` | `FVector &` | - |
| `Acceleration` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMousePosition`

```text
GetMousePosition(LocationX: float &, LocationY: float &) -> bool
```

Retrieves the X and Y screen coordinates of the mouse cursor. Returns false if there is no associated mouse device

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LocationX` | `float &` | - |
| `LocationY` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetInputKeyTimeDown`

```text
GetInputKeyTimeDown(Key: FKey) -> float
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

### `GetInputMouseDelta`

```text
GetInputMouseDelta(DeltaX: float &, DeltaY: float &) -> void
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

### `GetInputAnalogStickState`

```text
GetInputAnalogStickState(WhichStick: EControllerAnalogStick :: Type, StickX: float &, StickY: float &) -> void
```

Retrieves the X and Y displacement of the given analog stick.

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

### `ActivateTouchInterface`

```text
ActivateTouchInterface(NewTouchInterface: UTouchInterface *) -> void
```

Activates a new touch interface for this player controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTouchInterface` | `UTouchInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVirtualJoystickVisibility`

```text
SetVirtualJoystickVisibility(bVisible: bool) -> void
```

Set the virtual joystick visibility.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bVisible` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FadeInVirtualJoystick`

```text
FadeInVirtualJoystick(FadeDuration: float) -> void
```

Fade in the virtual joystick.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FadeDuration` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FadeOutVirtualJoystick`

```text
FadeOutVirtualJoystick(FadeDuration: float) -> void
```

Fade out the virtual joystick.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FadeDuration` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InitVirtualJoystickBySetting`

```text
InitVirtualJoystickBySetting() -> void
```

Set the virtual joystick visibility.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetViewportCacheGeometryScale`

```text
GetViewportCacheGeometryScale() -> float
```

获取Viewport的缓存几何缩放

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Camera`

```text
Camera(NewMode: FName) -> void
```

Change Camera mode

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewMode` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetViewTargetWithBlend`

```text
SetViewTargetWithBlend(NewViewTarget: AActor *, BlendTime: float, BlendFunc: EViewTargetBlendFunction, BlendExp: float, bLockOutgoing: bool) -> void
```

Set the view target blending with variable control

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewViewTarget` | `AActor *` | - new actor to set as view target |
| `BlendTime` | `float` | - time taken to blend |
| `BlendFunc` | `EViewTargetBlendFunction` | - Cubic, Linear etc functions for blending |
| `BlendExp` | `float` | - Exponent, used by certain blend functions to control the shape of the curve. |
| `bLockOutgoing` | `bool` | - If true, lock outgoing viewtarget to last frame's camera position for the remainder of the blend. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FlushPressedKeys`

```text
FlushPressedKeys() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FlushPressedKeysImmediate`

```text
FlushPressedKeysImmediate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FlushPressedMouseKeys`

```text
FlushPressedMouseKeys() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAudioListenerOverride`

```text
SetAudioListenerOverride(AttachToComponent: USceneComponent *, Location: FVector, Rotation: FRotator) -> void
```

Used to override the default positioning of the audio listener

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttachToComponent` | `USceneComponent *` | Optional component to attach the audio listener to |
| `Location` | `FVector` | Depending on whether Component is attached this is either an offset from its location or an absolute position |
| `Rotation` | `FRotator` | Depending on whether Component is attached this is either an offset from its rotation or an absolute rotation |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearAudioListenerOverride`

```text
ClearAudioListenerOverride() -> void
```

Clear any overrides that have been applied to audio listener

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ConsumeResidualNonAxisInput`

```text
ConsumeResidualNonAxisInput() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCinematicMode`

```text
SetCinematicMode(bInCinematicMode: bool, bHidePlayer: bool, bAffectsHUD: bool, bAffectsMovement: bool, bAffectsTurning: bool) -> void
```

ServerSP only function for changing whether the player is in cinematic mode.  Updates values of various state variables, then replicates the call to the client
	  to sync the current cinematic mode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInCinematicMode` | `bool` | specify true if the player is entering cinematic mode; false if the player is leaving cinematic mode. |
| `bHidePlayer` | `bool` | specify true to hide the player's pawn (only relevant if bInCinematicMode is true) |
| `bAffectsHUD` | `bool` | specify true if we should showhide the HUD to match the value of bCinematicMode |
| `bAffectsMovement` | `bool` | specify true to disable movement in cinematic mode, enable it when leaving |
| `bAffectsTurning` | `bool` | specify true to disable turning in cinematic mode or enable it when leaving |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnServerStartedVisualLogger`

```text
OnServerStartedVisualLogger(bIsLogging: bool) -> void
```

Notify from server that Visual Logger is recording, to show that information on client about possible performance issues

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsLogging` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSpectatorPawn`

```text
GetSpectatorPawn() -> ASpectatorPawn *
```

Get the Pawn used when spectating. NULL when not spectating.

**Returns**

| Type | Description |
|---|---|
| `ASpectatorPawn *` | - |

### `GetFocalLocation`

```text
GetFocalLocation() -> FVector
```

Returns the location the PlayerController is focused on.
	   If there is a possessed Pawn, returns the Pawn's location.
	   If there is a spectator Pawn, returns that Pawn's location.
	   Otherwise, returns the PlayerController's spawn location (usually the last known Pawn location after it has died).

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `StartTouchEventRecord`

```text
StartTouchEventRecord(RecordFileName: FString &) -> bool
```

开始记录Touch事件，将信息保存在TouchEventRecordData中，给定一个文件名存盘

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RecordFileName` | `FString &` | 记录保存到的文件名 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否一切正常 |

### `StopTouchEventRecord`

```text
StopTouchEventRecord() -> bool
```

停止记录Touch事件，将TouchEventRecordData中的数据保存到文件

**Returns**

| Type | Description |
|---|---|
| `bool` | 保存是否成功 |

### `ReplayTouchEventRecord`

```text
ReplayTouchEventRecord(RecordFileName: FString &) -> bool
```

从文件中加载Touch事件，并进行重放

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RecordFileName` | `FString &` | 记录文件名 |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetTouchRecordStartAndEndRotation`

```text
GetTouchRecordStartAndEndRotation(StartRotation: FRotator &, EndRotation: FRotator &) -> void
```

获取Touch记录中保存的起始和终止旋转角

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartRotation` | `FRotator &` | 起始旋转角，引用，在函数内赋值 |
| `EndRotation` | `FRotator &` | 终止旋转角，引用，在函数内赋值 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APlayerStart.json -->

# APlayerStart

This class indicates a location where a player can spawn when the game begins

## Inheritance

`ANavigationObjectBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PlayerStartTag` | `FName` | ~ To take more control over PlayerStart selection, you can override the virtual AGameModeBase::FindPlayerStart and AGameModeBase::ChoosePlayerStart functions. <br>	 Used when searching for which playerstart to use. |
| `ArrowComponent` | `UArrowComponent *` | Arrow component to indicate forward direction of start |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APlayerState.json -->

# APlayerState

A PlayerState is created for every player on a server (or in a standalone game).
  PlayerStates are replicated to all clients, and contain network game relevant information about the player, such as playername, score, etc.

## Inheritance

`AInfo`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Score` | `float` | Player's current score. |
| `Ping` | `uint8` | Replicated compressed ping for this player (holds ping in msec divided by 4) |
| `PlayerName` | `FString` | Player name, or blank if none. |
| `PlayerId` | `int32` | Unique net id number. Actual value varies based on current online subsystem, use it only as a guaranteed unique number per player. |
| `bIsSpectator` | `uint32` | Whether this player is currently a spectator |
| `bOnlySpectator` | `uint32` | Whether this player can only ever be a spectator |
| `bIsABot` | `uint32` | True if this PlayerState is associated with an AIController |
| `bIsInactive` | `uint32` | Means this PlayerState came from the GameMode's InactivePlayerArray |
| `bFromPreviousLevel` | `uint32` | indicates this is a PlayerState from the previous level of a seamless travel,<br>	  waiting for the player to finish the transition before creating a new one<br>	  this is used to avoid preserving the PlayerState in the InactivePlayerArray if the player leaves |
| `StartTime` | `int32` | Elapsed time on server when this PlayerState was first created. |
| `EngineMessageClass` | `TSubclassOf < ULocalMessage >` | This is used for sending game agnostic messages that can be localized |
| `SavedNetworkAddress` | `FString` | Used to match up InactivePlayerState with rejoining playercontroller. |
| `UniqueId` | `FUniqueNetIdRepl` | The id used by the network to uniquely identify a player.<br>	  NOTE: the internals of this property should never be exposed to the player as it's transient<br>	  and opaque in meaning (ie it might mean datetime followed by something else).<br>	  It is OK to use and pass around this property, though. |
| `PingBucketSize` | `int32` | - |

## Functions

### `OnRep_Score`

```text
OnRep_Score() -> void
```

Replication Notification Callbacks

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_PlayerName`

```text
OnRep_PlayerName() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_bIsInactive`

```text
OnRep_bIsInactive() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_UniqueId`

```text
OnRep_UniqueId() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveOverrideWith`

```text
ReceiveOverrideWith(OldPlayerState: APlayerState *) -> void
```

Can be implemented in Blueprint Child to move more properties from old to new PlayerState when reconnecting

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldPlayerState` | `APlayerState *` | Old PlayerState, which we use to fill the new one with |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveCopyProperties`

```text
ReceiveCopyProperties(NewPlayerState: APlayerState *) -> void
```

Can be implemented in Blueprint Child to move more properties from old to new PlayerState when traveling to a new level

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayerState` | `APlayerState *` | New PlayerState, which we fill with the current properties |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APointLight.json -->

# APointLight

## Inheritance

`ALight`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PointLightComponent` | `UPointLightComponent *` | - |

## Functions

### `SetRadius`

```text
SetRadius(NewRadius: float) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRadius` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetLightFalloffExponent`

```text
SetLightFalloffExponent(NewLightFalloffExponent: float) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightFalloffExponent` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APostProcessVolume.json -->

# APostProcessVolume

## Inheritance

`AVolume` -> `IInterface_PostProcessVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Settings` | `FPostProcessSettings` | Post process settings to use for this volume. |
| `Priority` | `float` | Priority of this volume. In the case of overlapping volumes the one with the highest priority<br>	  overrides the lower priority ones. The order is undefined if two or more overlapping volumes have the same priority. |
| `BlendRadius` | `float` | World space radius around the volume that is used for blending (only if not unbound). |
| `BlendWeight` | `float` | 0:no effect, 1:full effect |
| `bEnabled` | `uint32` | Whether this volume is enabled or not. |
| `bUnbound` | `uint32` | Whether this volume covers the whole world, or just the area inside its bounds. |

## Functions

### `AddOrUpdateBlendable`

```text
AddOrUpdateBlendable(InBlendableObject: TScriptInterface < IBlendableInterface >, InWeight: float) -> ENGINE_API void
```

Adds an Blendable (implements IBlendableInterface) to the array of Blendables (if it doesn't exist) and update the weight

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlendableObject` | `TScriptInterface < IBlendableInterface >` | - |
| `InWeight` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `ClearCustomGIFallbackSH`

```text
ClearCustomGIFallbackSH() -> ENGINE_API void
```

Clear all Custom GI Fallback SH coefficients (reset to zero)

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GenerateCustomGIFallbackSH`

```text
GenerateCustomGIFallbackSH() -> ENGINE_API void
```

Generate Spherical Harmonics coefficients from Custom GI Fallback directional colors

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GenerateCustomGIFallbackSHFromCubeMap`

```text
GenerateCustomGIFallbackSHFromCubeMap() -> ENGINE_API void
```

Generate Spherical Harmonics coefficients from CubeMap texture using Monte Carlo sampling

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APrecomputedVisibilityItemPoolVolume.json -->

# APrecomputedVisibilityItemPoolVolume

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bExternalVisibility` | `bool` | - |
| `bGroupOnlyUesdInDS` | `bool` | - |
| `PVSMode` | `EPVSMode` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APrecomputedVisibilityOverrideVolume.json -->

# APrecomputedVisibilityOverrideVolume

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OverrideVisibleActors` | `TArray < AActor * >` | Array of actors that will always be considered visible by Precomputed Visibility when viewed from inside this volume. |
| `OverrideInvisibleActors` | `TArray < AActor * >` | Array of actors that will always be considered invisible by Precomputed Visibility when viewed from inside this volume. |
| `OverrideInvisibleLevels` | `TArray < FName >` | Array of level names whose actors will always be considered invisible by Precomputed Visibility when viewed from inside this volume. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APrecomputedVisibilityVolume.json -->

# APrecomputedVisibilityVolume

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bOnlyInteriorComputed` | `bool` | - |
| `bOnlyUesdInDS` | `bool` | - |
| `PVSMode` | `EPVSMode` | - |
| `bAutoRCR` | `bool` | - |
| `AutoRCRMaxSize` | `float` | - |
| `SaveNewFolderName` | `FName` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AProceduralFoliageBlockingVolume.json -->

# AProceduralFoliageBlockingVolume

An invisible volume used to block ProceduralFoliage instances from being spawned.

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ProceduralFoliageVolume` | `AProceduralFoliageVolume *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AProceduralFoliageVolume.json -->

# AProceduralFoliageVolume

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ProceduralComponent` | `UProceduralFoliageComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/APVSExtraVisibilityActor.json -->

# APVSExtraVisibilityActor

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ExtraVisibilityInfo` | `TMap < int32 , FExtraPVSInfo >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ARadialForceActor.json -->

# ARadialForceActor

## Inheritance

`ARigidBodyBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ForceComponent` | `URadialForceComponent *` | Force component |
| `SpriteComponent` | `UBillboardComponent *` | - |

## Functions

### `FireImpulse`

```text
FireImpulse() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableForce`

```text
EnableForce() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableForce`

```text
DisableForce() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ToggleForce`

```text
ToggleForce() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ARecastNavMesh.json -->

# ARecastNavMesh

## Inheritance

`ANavigationData`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `navMeshFileName` | `FString` | - |
| `bDrawTriangleEdges` | `uint32` | should we draw edges of every navmesh's triangle |
| `bDrawPolyEdges` | `uint32` | should we draw edges of every poly (i.e. not only border-edges) |
| `bDrawFilledPolys` | `uint32` | if disabled skips filling drawn navmesh polygons |
| `bDrawNavMeshEdges` | `uint32` | should we draw border-edges |
| `bDrawTileBounds` | `uint32` | should we draw the tile boundaries |
| `bDrawPathCollidingGeometry` | `uint32` | Draw input geometry passed to the navmesh generator.  Recommend disabling other geometry rendering via viewport showflags in editor. |
| `bDrawTileLabels` | `uint32` | - |
| `bDrawPolygonLabels` | `uint32` | - |
| `bDrawDefaultPolygonCost` | `uint32` | - |
| `bDrawLabelsOnPathNodes` | `uint32` | - |
| `bDrawNavLinks` | `uint32` | - |
| `bDrawFailedNavLinks` | `uint32` | - |
| `bDrawClusters` | `uint32` | - |
| `bDrawOctree` | `uint32` | should we draw edges of every navmesh's triangle |
| `bDistinctlyDrawTilesBeingBuilt` | `uint32` | - |
| `bDrawNavMesh` | `uint32` | - |
| `DrawOffset` | `float` | vertical offset added to navmesh's debug representation for better readability |
| `bFixedTilePoolSize` | `uint32` | if true, the NavMesh will allocate fixed size pool for tiles, should be enabled to support streaming |
| `TilePoolSize` | `int32` | maximum number of tiles NavMesh can hold |
| `TileSizeUU` | `float` | size of single tile, expressed in uu |
| `CellSize` | `float` | horizontal size of voxelization cell |
| `CellHeight` | `float` | vertical size of voxelization cell |
| `AgentRadius` | `float` | Radius of smallest agent to traverse this navmesh |
| `AgentHeight` | `float` | - |
| `AgentMaxHeight` | `float` | Size of the tallest agent that will path with this navmesh. |
| `AgentMaxSlope` | `float` | The maximum slope (angle) that the agent can move on. |
| `AgentMaxStepHeight` | `float` | - |
| `MinRegionArea` | `float` | The minimum dimension of area. Areas smaller than this will be discarded |
| `MergeRegionSize` | `float` | The size limit of regions to be merged with bigger regions (watershed partitioning only) |
| `MaxSimplificationError` | `float` | How much navigable shapes can get simplified - the higher the value the more freedom |
| `MaxSimultaneousTileGenerationJobsCount` | `int32` | - |
| `TileNumberHardLimit` | `int32` | Absolute hard limit to number of navmesh tiles. Be very, very careful while modifying it while<br>	 	having big maps with navmesh. A single, empty tile takes 176 bytes and empty tiles are<br>	 	allocated up front (subject to change, but that's where it's at now)<br>	 	@note TileNumberHardLimit is always rounded up to the closest power of 2 |
| `PolyRefTileBits` | `int32` | - |
| `PolyRefNavPolyBits` | `int32` | - |
| `PolyRefSaltBits` | `int32` | - |
| `DefaultDrawDistance` | `float` | navmesh draw distance in game (always visible in editor) |
| `DefaultMaxSearchNodes` | `float` | specifes default limit to A nodes used when performing navigation queries. <br>	 	Can be overridden by passing custom FNavigationQueryFilter |
| `DefaultMaxHierarchicalSearchNodes` | `float` | specifes default limit to A nodes used when performing hierarchical navigation queries. |
| `bWithoutLayerCache` | `bool` | creating navmesh polys without layer cache |
| `WithoutLayerCachePartitioning` | `TEnumAsByte < ERecastWithoutLayerCachePartitioning :: Type >` | partitioning method for creating navmesh polys when not use layer cache |
| `RegionPartitioning` | `TEnumAsByte < ERecastPartitioning :: Type >` | partitioning method for creating navmesh polys |
| `LayerPartitioning` | `TEnumAsByte < ERecastPartitioning :: Type >` | partitioning method for creating tile layers |
| `RegionChunkSplits` | `int32` | number of chunk splits (along single axis) used for region's partitioning: ChunkyMonotone |
| `LayerChunkSplits` | `int32` | number of chunk splits (along single axis) used for layer's partitioning: ChunkyMonotone |
| `bSortNavigationAreasByCost` | `uint32` | Controls whether Navigation Areas will be sorted by cost before application <br>	 	to navmesh during navmesh generation. This is relevant then there are<br>	 	areas overlapping and we want to have area cost express area relevancy<br>	 	as well. Setting it to true will result in having area sorted by cost,<br>	 	but it will also increase navmesh generation cost a bit |
| `bPerformVoxelFiltering` | `uint32` | controls whether voxel filterring will be applied (via FRecastTileGenerator::ApplyVoxelFilter). <br>	 	Results in generated navemesh better fitting navigation bounds, but hits (a bit) generation performance |
| `bMarkLowHeightAreas` | `uint32` | mark areas with insufficient free height above instead of cutting them out |
| `bDoFullyAsyncNavDataGathering` | `uint32` | - |
| `bUseBetterOffsetsFromCorners` | `uint32` | TODO: switch to disable new code from OffsetFromCorners if necessary - remove it later |
| `bStoreEmptyTileLayers` | `uint32` | If set, tiles generated without any navmesh data will be marked to distinguish them from not generated  streamed out ones. Defaults to false. |
| `bUseVirtualFilters` | `uint32` | Indicates whether default navigation filters will use virtual functions. Defaults to true. |
| `bAllowNavLinkAsPathEnd` | `uint32` | If set, paths can end at navlink poly (not the ground one!) |
| `bOnlySavedOnDS` | `bool` | - |
| `PolyMeshSubvision` | `USubvisionMethodBase *` | - |
| `bAllowedDynamicNavAffectors` | `bool` | - |
| `DynamicAffectorUpdateInterval` | `float` | Minimal time, in seconds, between active tiles set update |
| `DynamicAffectorUpdateMode` | `EDynamicNavAffectorUpdateMode` | - |
| `bAllowedDynamicObstacle` | `bool` | - |
| `bUseVoxelCache` | `uint32` | Cache rasterized voxels instead of just collision verticesindices in navigation octree |
| `TileSetUpdateInterval` | `float` | indicates how often we will sort navigation tiles to mach players position |
| `HeuristicScale` | `float` | Euclidean distance heuristic scale used while pathfinding |
| `VerticalDeviationFromGroundCompensation` | `float` | Value added to each search height to compensate for error between navmesh polys and walkable geometry |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AReflectionCapture.json -->

# AReflectionCapture

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CaptureComponent` | `UReflectionCaptureComponent *` | Reflection capture component. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ASceneCapture.json -->

# ASceneCapture

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MeshComp` | `UStaticMeshComponent *` | To display the 3d camera in the editor. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ASceneCapture2D.json -->

# ASceneCapture2D

## Inheritance

`ASceneCapture`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CaptureComponent2D` | `USceneCaptureComponent2D *` | Scene capture component. |
| `DrawFrustum` | `UDrawFrustumComponent *` | To allow drawing the camera frustum in the editor. |

## Functions

### `OnInterpToggle`

```text
OnInterpToggle(bEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ASceneCaptureCube.json -->

# ASceneCaptureCube

## Inheritance

`ASceneCapture`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CaptureComponentCube` | `USceneCaptureComponentCube *` | Scene capture component. |
| `DrawFrustum` | `UDrawFrustumComponent *` | To allow drawing the camera frustum in the editor. |

## Functions

### `OnInterpToggle`

```text
OnInterpToggle(bEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ASkeletalMeshActor.json -->

# ASkeletalMeshActor

SkeletalMeshActor is an instance of a USkeletalMesh in the world.
  Skeletal meshes are deformable meshes that can be animated and change their geometry at run-time.
  Skeletal meshes dragged into the level from the Content Browser are automatically converted to StaticMeshActors.
  
  @see USkeletalMesh

## Inheritance

`AActor` -> `IMatineeAnimInterface` -> `IObjectPoolInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bShouldDoAnimNotifies` | `uint32` | Whether or not this actor should respond to anim notifies - CURRENTLY ONLY AFFECTS PlayParticleEffect NOTIFIES |
| `bWakeOnLevelStart_DEPRECATED` | `uint32` | - |
| `bSupportObjectPool` | `uint32` | - |
| `SkeletalMeshComponent` | `USkeletalMeshComponent *` | - |
| `ReplicatedMesh` | `USkeletalMesh *` | Used to replicate mesh to clients |
| `ReplicatedPhysAsset` | `UPhysicsAsset *` | Used to replicate physics asset to clients |
| `ReplicatedMaterial0` | `UMaterialInterface *` | used to replicate the material in index 0 |
| `ReplicatedMaterial1` | `UMaterialInterface *` | - |

## Functions

### `OnRep_ReplicatedMesh`

```text
OnRep_ReplicatedMesh() -> void
```

Replication Notification Callbacks

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_ReplicatedPhysAsset`

```text
OnRep_ReplicatedPhysAsset() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_ReplicatedMaterial0`

```text
OnRep_ReplicatedMaterial0() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_ReplicatedMaterial1`

```text
OnRep_ReplicatedMaterial1() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ASkyLight.json -->

# ASkyLight

## Inheritance

`AInfo`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LightComponent` | `USkyLightComponent *` | @todo document |
| `bEnabled` | `uint32` | replicated copy of LightComponent's bEnabled property |

## Functions

### `OnRep_bEnabled`

```text
OnRep_bEnabled() -> void
```

Replication Notification Callbacks

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ASkyLightZoneVolume.json -->

# ASkyLightZoneVolume

ASkyLightZoneVolume - 天光区域Volume Actor
  
  放置在场景中覆盖一个区域，区域内的组件根据自身 ReorganizationTags 的 isInterior 分组
  被设置不同的 SkyLightIntensityScale 值。
  
  isInterior 分组说明：
    有 Interior tag = 室内（应用室内参数）
    None (未勾选)   = 室外（应用室外参数）
    无 isInterior 分组 = 不处理

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `IndoorSkyLightIntensityScale` | `float` | 室内组件的 SkyLightIntensityScale 目标值（天光强度缩放） |
| `IndoorMinSkyVisibility` | `float` | 室内组件的 MinSkyVisibility 目标值（最小天空可见度） |
| `OutdoorSkyLightIntensityScale` | `float` | 室外组件的 SkyLightIntensityScale 目标值（天光强度缩放） |
| `OutdoorMinSkyVisibility` | `float` | 室外组件的 MinSkyVisibility 目标值（最小天空可见度） |
| `Priority` | `int32` | 优先级，重叠区域时高优先级覆盖低优先级 |
| `bShowAffectedActors` | `bool` | 是否在编辑器中显示受影响Actor的高亮边界框<br>	  使用 LineBatcher 绘制，不受G键（ShowFlags）影响<br>	  颜色说明：蓝色=室内，橙色=室外，绿色=同时室内外，灰色=未分类 |
| `InfoTextComponent` | `UTextRenderComponent *` | 编辑器中显示的文本标注组件（显示当前参数信息） |

## Functions

### `ApplyToOverlappingComponents`

```text
ApplyToOverlappingComponents() -> ENGINE_API void
```

一键应用：将此Volume的参数设置到区域内所有组件
	  根据组件的 ReorganizationTags isInterior 分组决定应用室内还是室外参数

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ASphereReflectionCapture.json -->

# ASphereReflectionCapture

Actor used to capture the scene for reflection in a sphere shape.

## Inheritance

`AReflectionCapture`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DrawCaptureRadius` | `UDrawSphereComponent *` | Sphere component used to visualize the capture radius |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ASplineMeshActor.json -->

# ASplineMeshActor

SplineMeshActor is an actor with a SplineMeshComponent.
 
  @see USplineMeshComponent

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SplineMeshComponent` | `USplineMeshComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ASpotLight.json -->

# ASpotLight

## Inheritance

`ALight`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SpotLightComponent` | `USpotLightComponent *` | - |

## Functions

### `SetInnerConeAngle`

```text
SetInnerConeAngle(NewInnerConeAngle: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewInnerConeAngle` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOuterConeAngle`

```text
SetOuterConeAngle(NewOuterConeAngle: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewOuterConeAngle` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AStaticMeshActor.json -->

# AStaticMeshActor

StaticMeshActor is an instance of a UStaticMesh in the world.
  Static meshes are geometry that do not animate or otherwise deform, and are more efficient to render than other types of geometry.
  Static meshes dragged into the level from the Content Browser are automatically converted to StaticMeshActors.
 
  @see UStaticMesh

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StaticMeshComponent` | `UStaticMeshComponent *` | - |
| `bStaticMeshReplicateMovement` | `bool` | This static mesh should replicate movement. Automatically sets the RemoteRole and bReplicateMovement flags. Meant to be edited on placed actors (those other two properties are not) |
| `NavigationGeometryGatheringMode` | `ENavDataGatheringMode` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AStaticMeshIndoorVolume.json -->

# AStaticMeshIndoorVolume

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VolumeComponent` | `UStaticMeshIndoorVolumeComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/%E4%B8%BB%E8%A7%92%E7%B1%BB%EF%BC%88PlayerPawn%EF%BC%89/ASTExtraBaseCharacter.json -->

# ASTExtraBaseCharacter

主角类（PlayerPawn）

## Inheritance

`ASTExtraCharacter` -> `ISTExtraInputInterface` -> `IPickupProxyFactory` -> `ISTExtraBaseCharacter_UGCEventInterface` -> `IGISPlayerInterface` -> `IGenericAbilityCarrierInterface` -> `IItemSkillV2RecevierInterface` -> `IInteractorInterface` -> `IDamageNumberInterface` -> `IMeleeAttackOwnerInterface`

## Functions

### `DSTeleportToLocationOrRotation`

```text
DSTeleportToLocationOrRotation(location: FVector, rotation: FRotator, setLoc: bool, setRot: bool, ResetVelocity: bool, bRecordTeleportInfo: bool) -> void
```

生效范围：服务器
	  传送主角，只有服务器上调用生效，客户端调用无效

**Parameters**

| Name | Type | Description |
|---|---|---|
| `location` | `FVector` | 位置 |
| `rotation` | `FRotator` | 旋转 |
| `setLoc` | `bool` | 是否修改位置 |
| `setRot` | `bool` | 是否修改旋转 |
| `ResetVelocity` | `bool` | 是否重置速度 |
| `bRecordTeleportInfo` | `bool` | 是否记录传送时间用于射击校验，如无特殊需求保持默认配置 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Events

### `UGC_WeaponShootBulletEvent`

```text
UGC_WeaponShootBulletEvent(ShootWeapon: ASTExtraShootWeapon *, Bullet: ASTExtraShootWeaponBulletBase *) -> void
```

发射子弹事件
	 生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ShootWeapon` | `ASTExtraShootWeapon *` | 射击武器 |
| `Bullet` | `ASTExtraShootWeaponBulletBase *` | 子弹 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_WeaponBulletHitEvent`

```text
UGC_WeaponBulletHitEvent(ShootWeapon: ASTExtraShootWeapon *, Bullet: ASTExtraShootWeaponBulletBase *, HitInfo: FHitResult) -> void
```

子弹命中事件
	 生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ShootWeapon` | `ASTExtraShootWeapon *` | 射击武器 |
| `Bullet` | `ASTExtraShootWeaponBulletBase *` | 子弹 |
| `HitInfo` | `FHitResult` | 命中信息 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_ChangeCurrentUsingWeaponEvent`

```text
UGC_ChangeCurrentUsingWeaponEvent(UsingWeaponSlot: ESurviveWeaponPropSlot, LastSlot: ESurviveWeaponPropSlot) -> void
```

当前武器变化事件
	 生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UsingWeaponSlot` | `ESurviveWeaponPropSlot` | 当前武器插槽 |
| `LastSlot` | `ESurviveWeaponPropSlot` | 上次武器插槽 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_EquipWeaponEvent`

```text
UGC_EquipWeaponEvent(Slot: ESurviveWeaponPropSlot) -> void
```

装备武器事件，仅装备在身上，非当前手持武器
	 生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Slot` | `ESurviveWeaponPropSlot` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_WeaponStartFireEvent`

```text
UGC_WeaponStartFireEvent(isAuto: ESTEWeaponShootType :: type) -> void
```

开火调用事件，仅在按下开火时调用一次
	 生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `isAuto` | `ESTEWeaponShootType :: type` | 是否自动开火 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_WeaponStopFireEvent`

```text
UGC_WeaponStopFireEvent() -> void
```

停火调用事件
	 生效范围SC

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_WeaponSwitchEvent`

```text
UGC_WeaponSwitchEvent() -> void
```

切换武器事件
	 生效范围C

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_ReloadStartEvent`

```text
UGC_ReloadStartEvent() -> void
```

开始换弹事件
	 生效范围SC

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_ReloadEndEvent`

```text
UGC_ReloadEndEvent() -> void
```

换弹结束事件
	 生效范围SC

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_OpenScopeEvent`

```text
UGC_OpenScopeEvent() -> void
```

开镜事件
	 生效范围C

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_CloseScopeEvent`

```text
UGC_CloseScopeEvent() -> void
```

开镜结束事件
	 生效范围C

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_EnterPawnStateEvent`

```text
UGC_EnterPawnStateEvent(PawnState: EPawnState) -> void
```

进入某个PawnState事件
	 生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PawnState` | `EPawnState` | 进入的PawnState |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_LeavePawnStateEvent`

```text
UGC_LeavePawnStateEvent(PawnState: EPawnState) -> void
```

离开某个PawnState事件
	 生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PawnState` | `EPawnState` | 离开的PawnState |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_PlayerPickUpEvent`

```text
UGC_PlayerPickUpEvent() -> void
```

玩家拾取事件
	 生效范围SC

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_PlayerDeadEvent`

```text
UGC_PlayerDeadEvent(Killer: AController *, DamageType: EDamageType :: DamageType) -> void
```

玩家死亡事件
	 生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Killer` | `AController *` | 把该角色淘汰的玩家 |
| `DamageType` | `EDamageType :: DamageType` | 伤害类型 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_TakeDamageOverrideEvent`

```text
UGC_TakeDamageOverrideEvent(Damage: float, DamageType: EDamageType :: DamageType, EventInstigator: AController *, DamageCauser: AActor *, Hit: FHitResult) -> float
```

重载伤害事件，返回值为修改后的伤害
	 生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Damage` | `float` | 伤害类型 |
| `DamageType` | `EDamageType :: DamageType` | 造成伤害的玩家 |
| `EventInstigator` | `AController *` | 造成伤害的玩家 |
| `DamageCauser` | `AActor *` | 把该角色淘汰的玩家 |
| `Hit` | `FHitResult` | 伤害命中信息 |

**Returns**

| Type | Description |
|---|---|
| `float` | 修改后伤害值 |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/%E8%A7%92%E8%89%B2%E7%B1%BB%EF%BC%88Pawn%EF%BC%89/ASTExtraCharacter.json -->

# ASTExtraCharacter

角色类

## Inheritance

`AUAECharacter` -> `IUAESkillInterface` -> `ISTBaseBuffCarrierInterface` -> `IDamageableInterface` -> `IWeaponOwnerInterface` -> `IWeaponOwnerProxyFactory` -> `IAttrModifyInterface` -> `IItemGenerateInterface` -> `IObjectPoolInterface` -> `IActorHiddenInterface` -> `ILaserSeekAndLockOwnerInterface` -> `IBulletHitInterface` -> `IGameAttributeCarrierInterface` -> `IPickerEffectInterface` -> `ICustomMovementInterface` -> `IGenericCharacterInterface` -> `ITargetFilterInfoProviderInterface` -> `IStateAbilityInterface` -> `IOwnershipChainInterface` -> `IFieldApplyInterface` -> `ICharacterTypeInterface`

## Events

### `UGC_GetDamageNumberConfigIndex`

```text
UGC_GetDamageNumberConfigIndex(Damage: float, bHeadShot: bool, EventInstigator: AController *, DamageCauser: AActor *, DamageTypeID: int32) -> int32
```

获取伤害数字配置索引
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Damage` | `float` | 伤害数值 |
| `bHeadShot` | `bool` | 是否爆头 |
| `EventInstigator` | `AController *` | 伤害来源Controller |
| `DamageCauser` | `AActor *` | 伤害来源物体 |
| `DamageTypeID` | `int32` | 伤害类型 |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `UGC_PreTakeDamageEvent`

```text
UGC_PreTakeDamageEvent(Damage: float, EventInstigator: AController *, DamageEvent: FDamageEvent, DamageCauser: AActor *) -> float
```

受到伤害前，返回值可以修改伤害值
	 生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Damage` | `float` | 当前伤害值， |
| `EventInstigator` | `AController *` | - |
| `DamageEvent` | `FDamageEvent` | 伤害类型 |
| `DamageCauser` | `AActor *` | 把该角色淘汰的玩家 |

**Returns**

| Type | Description |
|---|---|
| `float` | 修改后伤害值 |

## Delegates

### `UGC_OnHPChangedDelegate`

```text
UGC_OnHPChangedDelegate(HP: float, HPChanged: float) -> void
```

Delegate
	 生效范围SC
	 怪物血量变化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HP` | `float` | 当前血量 |
| `HPChanged` | `float` | 血量变化值 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_OnTakeDamageDelegate`

```text
UGC_OnTakeDamageDelegate(Damage: float, EventInstigator: AController*, DamageEvent: FDamageEvent, DamageCauser: AActor*) -> void
```

Delegate
	 生效范围S
	 受到伤害后

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Damage` | `float` | 当前伤害值， |
| `EventInstigator` | `AController*` | - |
| `DamageEvent` | `FDamageEvent` | 伤害类型 |
| `DamageCauser` | `AActor*` | 把该角色淘汰的玩家 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ASTExtraGameStateBase.json -->

# ASTExtraGameStateBase

游戏状态基类

## Inheritance

`AUAEGameState` -> `IUAELevelEventCenterInterface` -> `IImmediateUIInterface`

## Delegates

### `UGCPickupUsefulDelegate`

```text
UGCPickupUsefulDelegate(defineID: FItemDefineID) -> FUGCItemUsefulType
```

推荐拾取处理委托

**Parameters**

| Name | Type | Description |
|---|---|---|
| `defineID` | `FItemDefineID` | - |

**Returns**

| Type | Description |
|---|---|
| `FUGCItemUsefulType` | - |

### `UGCAutoPickupItemDelegate`

```text
UGCAutoPickupItemDelegate(defineID: FItemDefineID) -> FUGCAutoPickType
```

自动拾取处理委托

**Parameters**

| Name | Type | Description |
|---|---|---|
| `defineID` | `FItemDefineID` | - |

**Returns**

| Type | Description |
|---|---|
| `FUGCAutoPickType` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/%E8%A7%92%E8%89%B2%E6%8E%A7%E5%88%B6%E7%B1%BB%EF%BC%88PlayerController%EF%BC%89/ASTExtraPlayerController.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ASTExtraShootWeapon.json -->

# ASTExtraShootWeapon

射击武器类

## Inheritance

`ASTExtraWeapon`

## Delegates

### `OnShootWeaponAutoReloadDel`

```text
OnShootWeaponAutoReloadDel() -> void
```

Delegate
	  生效范围C
	  自动换弹事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnCurBulletChange`

```text
OnCurBulletChange() -> void
```

Delegate
	  生效范围SC
	  弹药数量变化事件。注：手动修改会触发开火消耗子弹不触发

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnCurBarrelBulletChangeDelegate`

```text
OnCurBarrelBulletChangeDelegate() -> void
```

Delegate
	  生效范围C
	  膛内弹药数量变化代理

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnStartFireDelegate`

```text
OnStartFireDelegate() -> void
```

Delegate
	  生效范围SC
	  开火事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnStopFireDelegate`

```text
OnStopFireDelegate() -> void
```

Delegate
	  生效范围SC
	  停火事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWeaponShootDelegate`

```text
OnWeaponShootDelegate() -> void
```

Delegate
	  生效范围C
	  射击事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWeaponReloadStartDelegate`

```text
OnWeaponReloadStartDelegate() -> void
```

Delegate
	  生效范围SC
	  开始换弹事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWeaponReloadEndDelegage`

```text
OnWeaponReloadEndDelegage() -> void
```

Delegate
	  生效范围SC
	  结束换弹事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWeaponEquipDelegate`

```text
OnWeaponEquipDelegate() -> void
```

Delegate
	  生效范围SC
	  武器装备事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWeaponUnEquipDelegate`

```text
OnWeaponUnEquipDelegate() -> void
```

Delegate
	  生效范围SC
	  武器卸载事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnLeftLastBulletWhenReloadOneByOneDelegate`

```text
OnLeftLastBulletWhenReloadOneByOneDelegate(RemainNum: int32) -> void
```

Delegate
	  生效范围SC
	  最后一发换弹通知事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RemainNum` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnBulletHitDelegate`

```text
OnBulletHitDelegate(InHitActor: AActor*, ImpactPosDistanceToWeapon: float, Player: APawn*) -> void
```

Delegate
	  生效范围S
	  射击武器命中事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InHitActor` | `AActor*` | - |
| `ImpactPosDistanceToWeapon` | `float` | - |
| `Player` | `APawn*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnShootIntervalModeChangeDelegate`

```text
OnShootIntervalModeChangeDelegate() -> void
```

Delegate
	  生效范围SC
	  改变射速模式事件（指的是改变了武器拥有的射速模式）

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnChangeAmmoDelegate`

```text
OnChangeAmmoDelegate(AmmoDefineID: FItemDefineID) -> void
```

Delegate
	  生效范围SC
	  切换武器弹药种类事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AmmoDefineID` | `FItemDefineID` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnClipAmmoDataChangeDelegate`

```text
OnClipAmmoDataChangeDelegate() -> void
```

Delegate
	  生效范围SC
	  武器弹夹内弹药数据发生变化事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnExplosionProjectileBulletExplodeDelegate`

```text
OnExplosionProjectileBulletExplodeDelegate(Bullet: AActor*) -> void
```

Delegate
	  生效范围SC
	  炮弹爆炸事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Bullet` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnScopeIn`

```text
OnScopeIn() -> void
```

Delegate
	  生效范围C
	  开镜事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnScopeOut`

```text
OnScopeOut() -> void
```

Delegate
	  生效范围C
	  关镜事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMaxBulletChange`

```text
OnMaxBulletChange() -> void
```

Delegate
	  生效范围SC
	  最大弹药数量变化事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnBulletPreShootDelegate`

```text
OnBulletPreShootDelegate(Bullet: ASTExtraShootWeaponBulletBase*) -> void
```

Delegate
	  生效范围C
	  子弹射出预处理事件，带有子弹参数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Bullet` | `ASTExtraShootWeaponBulletBase*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnBulletBeforeShootDelegate`

```text
OnBulletBeforeShootDelegate(Bullet: ASTExtraShootWeaponBulletBase*) -> void
```

Delegate
	  生效范围C
	  子弹射出事件，带有子弹参数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Bullet` | `ASTExtraShootWeaponBulletBase*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnBulletPostShootDelegate`

```text
OnBulletPostShootDelegate(Bullet: ASTExtraShootWeaponBulletBase*) -> void
```

Delegate
	  生效范围C
	  子弹射出后理事件，带有子弹参数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Bullet` | `ASTExtraShootWeaponBulletBase*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/%E8%BD%BD%E5%85%B7%E5%9F%BA%E7%B1%BB/ASTExtraVehicleBase.json -->

# ASTExtraVehicleBase

载具基类

## Inheritance

`APawn` -> `IGeneratorVehicleInterface` -> `IRegionObjectInterface` -> `IDamageableInterface` -> `ISeekAndLockOwnerInterface` -> `IActorHiddenInterface` -> `IFastRemoteReplicationTargetInterface` -> `IRelativeMoveMgrInterface` -> `IInteractorInterface` -> `IAttrModifyInterface` -> `ITargetFilterInfoProviderInterface`

## Events

### `UGC_OnVehicleEnterEvent`

```text
UGC_OnVehicleEnterEvent(IsSucc: bool, Character: ASTExtraPlayerCharacter *, SeatType: ESTExtraVehicleSeatType) -> void
```

玩家进入载具事件
	 生效范围CS

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsSucc` | `bool` | 上车是否成功 |
| `Character` | `ASTExtraPlayerCharacter *` | 乘客 |
| `SeatType` | `ESTExtraVehicleSeatType` | 座位类型 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_OnVehicleExitEvent`

```text
UGC_OnVehicleExitEvent(Character: ASTExtraPlayerCharacter *) -> void
```

玩家离开载具事件
	 生效范围CS

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `ASTExtraPlayerCharacter *` | 乘客 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `UGC_OnVehicleHealthStateChangedDelegate`

```text
UGC_OnVehicleHealthStateChangedDelegate(InVehicleHealthState: ESTExtraVehicleHealthState) -> void
```

载具健康状态变化	 
	  生效范围 CS

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVehicleHealthState` | `ESTExtraVehicleHealthState` | 变化后的健康状态 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_OnVehicleExplosionDelegate`

```text
UGC_OnVehicleExplosionDelegate() -> void
```

生效范围S
	 载具爆炸事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/%E6%AD%A6%E5%99%A8/ASTExtraWeapon.json -->

# ASTExtraWeapon

武器基类

## Inheritance

`AActor` -> `IOwnerRelevancyDependencyInterface` -> `IRegionObjectInterface` -> `IActorHiddenInterface` -> `IAttrModifyInterface` -> `IActorFeedbackInterface` -> `IGenericAbilityCarrierInterface` -> `IGameAttributeCarrierInterface` -> `ILogicEffectInterface` -> `IUAESharedModuleInterface` -> `IOwnershipChainInterface`

## Events

### `OnWeaponMeshLoadFinished`

```text
OnWeaponMeshLoadFinished(SlotID: int32, IsEquipped: bool) -> void
```

武器加载模型完毕的接口，之后可以获取武器的MeshComponent
	 生效范围：C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotID` | `int32` | - |
| `IsEquipped` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnWeaponDrawHUDDelegate`

```text
OnWeaponDrawHUDDelegate(WeaponHudWidget: UHUDWidgetBase*, Canvas: UCanvas*) -> void
```

Delegate
	  生效范围C
	  武器绘制HUD事件，传入武器的HUDWidiget， Canvas

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WeaponHudWidget` | `UHUDWidgetBase*` | - |
| `Canvas` | `UCanvas*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPressingWeaponFuncBtnDelegate`

```text
OnPressingWeaponFuncBtnDelegate(DeltaTime: float) -> void
```

Delegate
	  生效范围C
	  持续按键事件，有DeltaTime传入

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_AttachmentChangeDelegate`

```text
UGC_AttachmentChangeDelegate(AttachHandleID: int32, IsEquip: bool) -> void
```

武器配件装卸委托
	 
	  生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttachHandleID` | `int32` | 配件ID |
| `IsEquip` | `bool` | 是否是装备配件 |

**Returns**

| Type | Description |
|---|---|
| `void` | void |

### `OnWeaponTriggerEventDelegate`

```text
OnWeaponTriggerEventDelegate(Event: EWeaponTriggerEvent, EventData: const FString&) -> void
```

Delegate
	  生效范围C
	  武器按键事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Event` | `EWeaponTriggerEvent` | - |
| `EventData` | `const FString&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWeaponAttachToBackpackDelegate`

```text
OnWeaponAttachToBackpackDelegate() -> void
```

Delegate
	  生效范围SC
	  武器挂背事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ATargetPoint.json -->

# ATargetPoint

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SpriteComponent` | `UBillboardComponent *` | - |
| `ArrowComponent` | `UArrowComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ATextRenderActor.json -->

# ATextRenderActor

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TextRender` | `UTextRenderComponent *` | Component to render a text in 3d with a font |
| `SpriteComponent` | `UBillboardComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ATriggerBase.json -->

# ATriggerBase

An actor used to generate collision events (beginend overlap) in the level.

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CollisionComponent` | `UShapeComponent *` | Shape component used for collision |
| `SpriteComponent` | `UBillboardComponent *` | Billboard used to see the trigger in the editor |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/%E6%B8%B8%E6%88%8F%E6%A8%A1%E5%BC%8F%E7%B1%BB%EF%BC%88GameMode%EF%BC%89/AUGCGameModeBase.json -->

# AUGCGameModeBase

游戏模式类

## Inheritance

`ASTExtraGameFramework` -> `IUGCGetDynamicConfigInterface` -> `IUGCGraphicScriptInterface`

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AUGCGameModeTDM.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AUGCGenericCharacter.json -->

# AUGCGenericCharacter

怪物角色类

## Inheritance

`AGenericCharacter`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `HealthBarWidgetClass` | `TSoftClassPtr < UUGCGenericCharacterPositionWidget >` | 血条控件蓝图路径 |
| `bHealthBarShowWhenOcclusionHide` | `bool` | 被遮挡后血条是否仍显示 |
| `HealthBarMaxShowDistance` | `float` | 血条实时显示最大距离，单位厘米 |
| `HealthBarLocOffset` | `FVector` | 血条位置偏移 |
| `bHealthBarUseSocket` | `bool` | 血条是否附着到特定部位 |
| `HealthBarSocketName` | `FName` | 血条附着的部位名 |
| `bHealthBarShowWhenTakeDamage` | `bool` | 怪物受伤时显示血条 |
| `bHealthBarShowWhenLockPlayer` | `bool` | 当怪物将玩家作为当前目标时显示血条 |
| `bHealthBarShowWhenBeAimAt` | `bool` | 当玩家瞄准怪物时显示血条 |
| `HealthBarConditionShowDistance` | `float` | 能触发瞄准显示的最大距离 |
| `HealthBarShowDuration` | `float` | 血条显示条件触发后显示时间 |
| `HealthBarCampFilter` | `int32` | 阵营过滤 |
| `HealthBarDamageFilter` | `EShowHPBarDamageType` | 伤害来源过滤 |
| `bEnableDistanceBasedNetworkOptimization` | `bool` | 网络同步距离分档优化开关<br>	  只在客户端生效，控制是否根据与玩家的距离动态调整网络同步参数 |
| `NetworkOptimizationLevels` | `TArray < FUGCNetworkOptimizationLevelConfig >` | 距离分档配置数组<br>	  按 DistanceThreshold 从小到大排序配置，遍历找到第一个满足距离 <= 阈值的档位<br>	  如果距离超过所有阈值，则使用数组最后一个配置 |
| `DistanceCheckInterval` | `float` | 检测玩家距离的间隔时间 |
| `CurrentDistanceLevel` | `int32` | 当前档位索引 (-1表示未初始化) |

## Functions

### `GetBlackBoardComponent`

```text
GetBlackBoardComponent() -> UBlackboardComponent *
```

获取黑板组件
	  生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `UBlackboardComponent *` | - |

### `SetForceHatredTarget`

```text
SetForceHatredTarget(NewTarget: AActor *) -> void
```

设置当前强制仇恨目标
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTarget` | `AActor *` | 仇恨目标 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveForceHatredTarget`

```text
RemoveForceHatredTarget() -> void
```

清除强制仇恨目标
	  生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddTargetHatredValue`

```text
AddTargetHatredValue(Target: AActor *, HatredValue: float) -> void
```

增加目标仇恨值
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `AActor *` | 目标 |
| `HatredValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Events

### `OnEnterTagState_BP`

```text
OnEnterTagState_BP(DynamicState: FGameplayTag) -> void
```

状态进入事件
	  生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DynamicState` | `FGameplayTag` | 进入状态 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnLeaveTagState_BP`

```text
OnLeaveTagState_BP(DynamicState: FGameplayTag) -> void
```

状态退出事件
	  生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DynamicState` | `FGameplayTag` | 退出状态 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInterruptTagState_BP`

```text
OnInterruptTagState_BP(DynamicState: FGameplayTag) -> void
```

状态打断事件
	  生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DynamicState` | `FGameplayTag` | 打断状态 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnBehaviorNotify_BP`

```text
OnBehaviorNotify_BP(NotifyMsg: FString &) -> void
```

行为树消息
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotifyMsg` | `FString &` | 消息 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnArriveWaypoint_BP`

```text
OnArriveWaypoint_BP(WaypointIndex: int32 &) -> void
```

行为树消息
      生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WaypointIndex` | `int32 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnCreateHealthWidget`

```text
OnCreateHealthWidget(HealthWidget: UUGCGenericCharacterPositionWidget*) -> void
```

血条创建成功事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HealthWidget` | `UUGCGenericCharacterPositionWidget*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AUGCItemSpawner.json -->

# AUGCItemSpawner

物资刷新系统：物资刷新器

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ItemConfig` | `FUGCItemSpawnerItemConfig` | 配置刷出的物资类别和数量 |
| `bNeedSpawnerManager` | `bool` | 物资刷新点是否能独立运作，还是依赖于物资刷新管理器 |
| `bLoopSpawn` | `bool` | 独立运作模式时，物资被拾取后是否会自动生成 |
| `SpawnCD` | `float` | 开启循环生成后，物资被拾取后间隔重新刷新 |
| `bTraceGround` | `bool` | 物资是否一定刷新在地面上 |
| `bRandomRotator` | `bool` | 物资方向是否随机 |
| `StartRadius` | `int32` | 物资刷新位置到刷新点的最小距离 |
| `EndRadius` | `int32` | 物资刷新位置到刷新点的最大距离 |

## Functions

### `SpawnItem`

```text
SpawnItem(ItemID: int32, ItemCount: int32) -> AActor *
```

生效范围 服务器
	  刷物资

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `int32` | 物资ID |
| `ItemCount` | `int32` | 物资数量 |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | 刷出的物资 |

### `SetItemConfig`

```text
SetItemConfig(InItemConfig: FUGCItemSpawnerItemConfig) -> void
```

生效范围 服务器
	  修改物资刷新配置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InItemConfig` | `FUGCItemSpawnerItemConfig` | 新的物资刷新配置 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CleanItems`

```text
CleanItems() -> void
```

生效范围 服务器
	  清除刷出的物资

**Returns**

| Type | Description |
|---|---|
| `void` | 刷出的物资 |

## Events

### `OnItemsSpawn`

```text
OnItemsSpawn(Items: TArray < AActor * > &) -> void
```

生效范围 服务器
	  物资刷出事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Items` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAllItemsArePick`

```text
OnAllItemsArePick() -> void
```

生效范围 服务器
	  所有物资都被拾取

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CustomSpawnItem`

```text
CustomSpawnItem(CustomParam: TMap < FString , FString > &) -> TArray < AActor * >
```

生效范围 服务器
	  覆写该事件来自定义物资刷出流程

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CustomParam` | `TMap < FString , FString > &` | 自定义参数列表 |

**Returns**

| Type | Description |
|---|---|
| `TArray < AActor * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81%E4%B8%8E%E8%83%8C%E5%8C%85/AUGCItemSpawnerManager.json -->

# AUGCItemSpawnerManager

生成系统：物资生成管理器

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartCondition` | `EUGCItemSpawnerManagerStartCondition` | 管理器的启动方式 |
| `EventName` | `FString` | 启动方式选择事件触发时，监听的GMP事件名 |
| `ItemSpawners` | `TArray < FUGCItemSpawnerInfo >` | 配置刷新点 |
| `MaxWaveInternalTime` | `float` | 配置两次刷新之间的最大时间间隔 |
| `MinWaveInternalTime` | `float` | 配置两次刷新之间的最小时间间隔 |
| `MaxSpawnerNumPerWave` | `int32` | 配置同一时间有物资刷出的刷新点的最大数量 |
| `MinSpawnerNumPerWave` | `int32` | 配置同一时间有物资刷出的刷新点的最小数量 |
| `TotalSpawnWaveCount` | `int32` | 物资刷新的总轮数，设为-1则无限刷新 |
| `bOverrideItemConfig` | `bool` | 是否覆盖所有刷新点上的物资配置 |
| `ItemConfig` | `FUGCItemSpawnerItemConfig` | 配置所有刷新点上的物资配置 |

## Functions

### `StartSpawnerManager`

```text
StartSpawnerManager() -> void
```

生效范围 服务器
	  启动管理器

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetSpawnerManager`

```text
ResetSpawnerManager() -> void
```

生效范围 服务器
	  重置管理器

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CleanAllItem`

```text
CleanAllItem() -> void
```

生效范围 服务器
	  清理刷出的物资

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PauseSpawnerManager`

```text
PauseSpawnerManager() -> void
```

生效范围 服务器
	  暂停物资刷新管理器

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResumeSpawnerManager`

```text
ResumeSpawnerManager() -> void
```

生效范围 服务器
	  恢复物资刷新管理器

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetItemConfigOverrideForSpawner`

```text
SetItemConfigOverrideForSpawner(InItemConfig: FUGCItemSpawnerItemConfig, SpawnerIndex: int32) -> void
```

生效范围 服务器
	  修改特定刷新点的物资配置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InItemConfig` | `FUGCItemSpawnerItemConfig` | 新的物资刷新配置 |
| `SpawnerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetItemConfigOverride`

```text
SetItemConfigOverride(InItemConfig: FUGCItemSpawnerItemConfig) -> void
```

生效范围 服务器
	  修改所有刷新点的物资配置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InItemConfig` | `FUGCItemSpawnerItemConfig` | 新的物资刷新配置 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CleanAllItemConfigOverride`

```text
CleanAllItemConfigOverride() -> void
```

生效范围 服务器
	  清除刷新点的物资配置设置，调用后将使用刷新点本身的配置

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Events

### `OnItemsSpawn`

```text
OnItemsSpawn(Items: TArray < AActor * > &) -> void
```

生效范围 服务器
	  物品刷新

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Items` | `TArray < AActor * > &` | 本轮刷新的物品 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AUGCMobCharacter.json -->

# AUGCMobCharacter

怪物角色类

## Inheritance

`ACharacter` -> `IObjectPoolInterface` -> `IDamageableInterface` -> `IAttrModifyInterface` -> `IGameAttributeCarrierInterface` -> `IRegionObjectInterface` -> `IBulletEffectInterface` -> `IBulletHitInterface` -> `IUGCCharacterAnimPlayInterfaceBase` -> `ICommonAIInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Health` | `float` | 当前生命值 |
| `HealthAddScale` | `float` | 加血速率 |
| `HealthMax` | `float` | 最大生命值 |
| `bInvincible` | `int` | 是否无敌 |
| `SkillCDRecoverRate` | `FGameAttributeProperty` | 技能急速，值越大技能冷却越快结束 |
| `IsShowDamageNum` | `bool` | 是否显示伤害数字 |
| `HealthBarWidget` | `UUGCCharacterPositionWidget *` | 血条的蓝图类 |
| `bIsShowHealthBar` | `bool` | 是否显示血条 |
| `ShowName` | `FName` | 血条上显示的名字 |
| `PlayBeHitedAnimTimeInterval` | `float` | 受击动画播放最小间隔，小于受击动画长度时无效 |
| `bNeedDestroyOnDeath` | `bool` | 是否启用尸体消失后延迟销毁 |
| `DisappearOnDeathLifeSpan` | `float` | 尸体消失后延迟多久销毁 |
| `DelayRemoveDeadBody` | `float` | 死亡后尸体存在时间 |
| `BornTime` | `float` | 出生状态持续时间 |
| `StunDuration` | `float` | 硬直状态持续时间 |
| `UGCGeneralMoveSpeedScale` | `float` | 移动速度倍率 |
| `AttackMeActorRemainTime` | `float` | 活动范围，处于活动范围外时索敌无效，仇恨随时间消失<br>	 <br>	 UGC<br>	  处于活动范围外时仇恨持续时间 |
| `SpawnLoc` | `FVector` | 出生地点 |
| `bOutOfActivityRange` | `bool` | 是否在活动范围外 |

## Functions

### `IsAlive`

```text
IsAlive() -> bool
```

是否存活

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsInvincible`

```text
IsInvincible() -> FORCEINLINE int
```

是否无敌

**Returns**

| Type | Description |
|---|---|
| `FORCEINLINE int` | - |

### `ForceDie`

```text
ForceDie() -> void
```

生效范围 服务器
	  强制杀死怪物

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCurrentSpeed`

```text
GetCurrentSpeed() -> float
```

生效范围 服务器&客户端
	  获取当前速度值

**Returns**

| Type | Description |
|---|---|
| `float` | float 当前速度值 |

### `GetVelocity`

```text
GetVelocity() -> FVector
```

生效范围 服务器&客户端
	  获取当前速度向量

**Returns**

| Type | Description |
|---|---|
| `FVector` | FVector 当前速度向量 |

## Events

### `PreTakeDamageEvent`

```text
PreTakeDamageEvent(DamageCauser: AActor *, EventInstigator: AController *, Damage: float, DamageContext: FGameMagnitudeContext &) -> void
```

生效范围 服务器
	  小怪即将受到伤害前事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DamageCauser` | `AActor *` | 伤害来源 |
| `EventInstigator` | `AController *` | 伤害来源的Controller |
| `Damage` | `float` | - |
| `DamageContext` | `FGameMagnitudeContext &` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PostTakeDamageEvent`

```text
PostTakeDamageEvent(DamageCauser: AActor *, EventInstigator: AController *, Damage: float, DamageContext: FGameMagnitudeContext &) -> void
```

生效范围 服务器
	  受到伤害后事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DamageCauser` | `AActor *` | 伤害来源 |
| `EventInstigator` | `AController *` | 伤害来源的Controller |
| `Damage` | `float` | - |
| `DamageContext` | `FGameMagnitudeContext &` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PreOverrideDamageValue`

```text
PreOverrideDamageValue(Damage: float, DamageType: int32, EventInstigator: AController *, DamageCauser: AActor *, Hit: FHitResult &) -> float
```

生效范围 服务器
	  伤害值覆盖事件,在全局伤害公式前

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Damage` | `float` | - |
| `DamageType` | `int32` | 伤害类型 |
| `EventInstigator` | `AController *` | 伤害来源的Controller |
| `DamageCauser` | `AActor *` | 伤害来源 |
| `Hit` | `FHitResult &` | 命中信息 |

**Returns**

| Type | Description |
|---|---|
| `float` | 覆盖后的伤害值 |

### `PostOverrideDamageValue`

```text
PostOverrideDamageValue(Damage: float, DamageType: int32, EventInstigator: AController *, DamageCauser: AActor *, Hit: FHitResult &) -> float
```

生效范围 服务器
	  伤害值覆盖事件,在全局伤害公式后

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Damage` | `float` | - |
| `DamageType` | `int32` | 伤害类型 |
| `EventInstigator` | `AController *` | 伤害来源的Controller |
| `DamageCauser` | `AActor *` | 伤害来源 |
| `Hit` | `FHitResult &` | 命中信息 |

**Returns**

| Type | Description |
|---|---|
| `float` | 覆盖后的伤害值 |

### `MobPawnDeadEvent`

```text
MobPawnDeadEvent(Killer: AController *, DamageCauser: AActor *, KillingHitDamageType: EDamageType :: DamageType) -> void
```

生效范围 服务器&客户端
	  怪物死亡事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Killer` | `AController *` | 把该小怪杀死的角色的Controller |
| `DamageCauser` | `AActor *` | 杀死该小怪的角色 |
| `KillingHitDamageType` | `EDamageType :: DamageType` | 最后一击的伤害类型 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StateChangeEvent`

```text
StateChangeEvent(OldState: EUGCMobState, NewState: EUGCMobState) -> void
```

生效范围 服务器&客户端
	  状态变化事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldState` | `EUGCMobState` | 变化前状态 |
| `NewState` | `EUGCMobState` | 变化后状态 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AUGCMobSpawner.json -->

# AUGCMobSpawner

刷怪系统：刷怪器

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bNeedSpawnerManager` | `bool` | 是否刷怪点是否能独立运行，还是必须依赖刷怪管理器. 废弃, 请使用SpawnerContrMode |
| `SpawnerContrMode` | `EUGCMobSpawnerContrMode` | 刷怪器控制模式. |
| `MobConfig` | `FUGCMobSpawnerMobConfig` | 配置刷出的怪物 |
| `bUseNavMesh` | `bool` | 是否优先在有移动网格的地面上刷新 |
| `Range` | `float` | 配置怪物的生成范围的半径 |
| `Height` | `float` | 配置刷新点位置与实际生成位置的最大高度差 |
| `RandomRotYaw` | `bool` | 怪物的出生面向是否随机，否则使用刷新点的朝向 |
| `MinSpawnCount` | `int32` | 配置总的最小刷怪数量 |
| `MaxSpawnCount` | `int32` | 配置总的最大刷怪数量 |
| `SpawnCD` | `float` | 配置两次刷怪之间的时间间隔 |
| `MobCountPerSpawn` | `int32` | 配置单次刷怪的数量 |
| `bTraceGround` | `bool` | 是否保证怪物刷到地面上 |

## Functions

### `SpawnMob`

```text
SpawnMob(MobClass: UClass *) -> AActor *
```

生效范围 服务器
	  刷出指定怪物

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MobClass` | `UClass *` | 怪物的类 |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `SetMobConfig`

```text
SetMobConfig(InMobConfig: FUGCMobSpawnerMobConfig) -> void
```

生效范围 服务器
	  修改怪物刷新配置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMobConfig` | `FUGCMobSpawnerMobConfig` | 修改后的刷新配置 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ModifyMinMaxSpawnCount`

```text
ModifyMinMaxSpawnCount(InMinSpawnCount: int32, InMaxSpawnCount: int32) -> void
```

生效范围 服务器
	  修改最小最大刷怪数量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMinSpawnCount` | `int32` | 修改后的最小刷怪数量 |
| `InMaxSpawnCount` | `int32` | 修改后的最大刷怪数量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Events

### `OnMobSpawn`

```text
OnMobSpawn(Mob: AActor *) -> void
```

生效范围 服务器
	  怪物刷出事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Mob` | `AActor *` | 输出的怪物 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CustomSpawnMob`

```text
CustomSpawnMob(CustomParam: TMap < FString , FString > &) -> AActor *
```

生效范围 服务器
	  覆写该事件可实现自定义怪物刷出流程

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CustomParam` | `TMap < FString , FString > &` | 自定义参数列表 |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%80%AA%E7%89%A9%E7%B3%BB%E7%BB%9F/AUGCMobSpawnerManager.json -->

# AUGCMobSpawnerManager

刷怪系统：刷怪管理器

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartCondition` | `EUGCMobSpawnerManagerStartCondition` | 配置刷怪管理器的启动方式 |
| `EventName` | `FString` | 启动方式使用事件触发时，监听的GMP名 |
| `MaxSpawnPerFrame` | `int32` | 配置刷怪管理器每帧刷怪的上限 |
| `AliveMobsCheckDeltaTime` | `float` | 配置刷怪管理器检查当前怪物存活情况的间隔 |
| `SpawnWaves` | `TArray < FUGCSpawnWave >` | 配置刷怪的波次 |

## Functions

### `StartSpawnerManager`

```text
StartSpawnerManager() -> void
```

生效范围 服务器
	  启动刷怪管理器

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetSpawnerManager`

```text
ResetSpawnerManager(bDeleteAllMobs: bool) -> void
```

生效范围 服务器
	  重置刷怪管理器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bDeleteAllMobs` | `bool` | 是否清除所有刷出的怪物 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CleanAllMobs`

```text
CleanAllMobs(bDelete: bool) -> void
```

生效范围 服务器
	  清理对刷出怪物的引用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bDelete` | `bool` | 是否清除怪物 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PauseSpawnerManager`

```text
PauseSpawnerManager() -> void
```

生效范围 服务器
	  暂停刷怪管理器

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResumeSpawnerManager`

```text
ResumeSpawnerManager() -> void
```

生效范围 服务器
	  恢复刷怪管理器

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSpawner`

```text
GetSpawner(WaveIndex: int32, SpawnerIndex: int32) -> AUGCMobSpawner *
```

生效范围 服务器
	  获取波次中特定编号的刷怪点

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WaveIndex` | `int32` | 波次编号 |
| `SpawnerIndex` | `int32` | 刷新点编号 |

**Returns**

| Type | Description |
|---|---|
| `AUGCMobSpawner *` | 怪物刷新点 |

### `GetCurrentWaveIndex`

```text
GetCurrentWaveIndex() -> int32
```

生效范围 服务器
	  获取当前波的波次编号

**Returns**

| Type | Description |
|---|---|
| `int32` | 当前波次编号 |

### `GetWaveSpawnerNum`

```text
GetWaveSpawnerNum(WaveIndex: int32) -> int32
```

生效范围 服务器
	  获取对应波次的刷新点数量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WaveIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | 刷新点数量 |

### `GetWaveNum`

```text
GetWaveNum() -> int32
```

生效范围 服务器
	  获取波次的数量

**Returns**

| Type | Description |
|---|---|
| `int32` | 波次数量 |

### `SetMobConfigOverrideForSpawner`

```text
SetMobConfigOverrideForSpawner(InMobConfig: FUGCMobSpawnerMobConfig, WaveIndex: int32, SpawnerIndex: int32) -> void
```

生效范围 服务器
	  修改特定波次中特定刷新点的怪物配置覆盖

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMobConfig` | `FUGCMobSpawnerMobConfig` | 新的怪物配置 |
| `WaveIndex` | `int32` | 波次编号 |
| `SpawnerIndex` | `int32` | 刷新点编号 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMobConfigOverrideForWave`

```text
SetMobConfigOverrideForWave(InMobConfig: FUGCMobSpawnerMobConfig, WaveIndex: int32) -> void
```

生效范围 服务器
	  修改特定波次中所有刷新点的怪物配置覆盖

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMobConfig` | `FUGCMobSpawnerMobConfig` | 新的怪物配置 |
| `WaveIndex` | `int32` | 波次编号 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMobConfigOverride`

```text
SetMobConfigOverride(InMobConfig: FUGCMobSpawnerMobConfig) -> void
```

生效范围 服务器
	  修改所有波次的怪物配置覆盖

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMobConfig` | `FUGCMobSpawnerMobConfig` | 新的怪物配置 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CleanAllMobConfigOverride`

```text
CleanAllMobConfigOverride() -> void
```

生效范围 服务器
	  清除管理器所有的怪物配置覆盖

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `JumpToWave`

```text
JumpToWave(WaveIndex: int32) -> void
```

生效范围 服务器
	  跳转到指定波次

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WaveIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Events

### `OnMobSpawn`

```text
OnMobSpawn(Mob: AActor *) -> void
```

生效范围 服务器
	  怪物刷出事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Mob` | `AActor *` | 刷出的怪物 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWaveStart`

```text
OnWaveStart(WaveIndex: int32) -> void
```

生效范围 服务器
	  刷怪波次开始事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WaveIndex` | `int32` | 波次编号 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWaveEnd`

```text
OnWaveEnd(WaveIndex: int32) -> void
```

生效范围 服务器
	  刷怪波次结束事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WaveIndex` | `int32` | 波次编号 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAllWaveEnd`

```text
OnAllWaveEnd() -> void
```

生效范围 服务器
	  所有波次结束事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAllMobDie`

```text
OnAllMobDie() -> void
```

生效范围 服务器
	  所以波次怪物都已刷新并死亡事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AUGCPickUpWrapperActor.json -->

# AUGCPickUpWrapperActor

地面拾取物Actor

## Inheritance

`APickUpWrapperActor`

## Functions

### `OnRep_DefineID_BP`

```text
OnRep_DefineID_BP() -> void
```

拾取物DefineID更改时触发
	  生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDefineID`

```text
GetDefineID() -> FItemDefineID
```

获取拾取物物品的实例ID
	  DS & 客户端 可调用

**Returns**

| Type | Description |
|---|---|
| `FItemDefineID` | 实例ID |

### `GetItemCount`

```text
GetItemCount() -> int32
```

获取拾取物物品的物品数量
	  DS & 客户端 可调用

**Returns**

| Type | Description |
|---|---|
| `int32` | 物品数量 |

## Events

### `OnInitPickupWrapper`

```text
OnInitPickupWrapper() -> void
```

当地面拾取物初始化后回调
	  可重载并自定义
	  DS & 客户端 被调用
	 
	  能通过此事件，实现自定义的初始化逻辑

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnItemPickup`

```text
OnItemPickup(PickupCharacter: ASTExtraBaseCharacter *, PickupCount: int32, NewItemCount: int32) -> void
```

当地面拾取物被拾取后回调
	  可重载并自定义
	  DS 被调用
	 
	  能通过此事件，实现自定义的被拾取后处理逻辑

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PickupCharacter` | `ASTExtraBaseCharacter *` | 拾取物品的角色 |
| `PickupCount` | `int32` | 拾取数量 |
| `NewItemCount` | `int32` | 拾取后的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnItemCountChange`

```text
OnItemCountChange(OldItemCount: int32, NewItemCount: int32) -> void
```

当地面拾取物物品数量改变时回调(拾取物销毁时也会有回调)
	  如果是拾取导致的改变，时机略晚于 OnItemPickup
	  可重载并自定义
	  DS & 客户端 被调用
	 
	  能通过此事件，实现自定义的物品数量改变处理逻辑

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldItemCount` | `int32` | 改变前的物品数量 |
| `NewItemCount` | `int32` | 改变后的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnUnInitPickupWrapper`

```text
OnUnInitPickupWrapper() -> void
```

当地面拾取物销毁前回调
	  可重载并自定义
	  DS & 客户端 被调用
	 
	  能通过此事件，实现自定义的反初始化逻辑

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AUniversalProjectileBase.json -->

# AUniversalProjectileBase

通用抛体

## Inheritance

`AUniversalProjectileCore`

## Functions

### `ReceiveCustomFilter`

```text
ReceiveCustomFilter(InActor: AActor *) -> bool
```

自定义的过滤器接口
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ReceivePlayExplosionEffectToAllTarget`

```text
ReceivePlayExplosionEffectToAllTarget(FoundTargets: TArray < FHitResult > &) -> void
```

自定义爆炸范围内筛选过后所有碰撞结果接口
	 生效范围：S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FoundTargets` | `TArray < FHitResult > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceivePlayExplosionEffect`

```text
ReceivePlayExplosionEffect(ExplosionTarget: FHitResult &) -> void
```

自定义爆炸范围内筛选过后碰撞接口
	 生效范围：S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ExplosionTarget` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveBeginExplodeTimer`

```text
ReceiveBeginExplodeTimer() -> void
```

爆炸开始计时的额外接口（如果有延时爆炸）
	 生效范围：S

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveEndExplodeTimer`

```text
ReceiveEndExplodeTimer() -> void
```

爆炸停止计时的额外接口（如果有延时爆炸）
	 生效范围：S

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AUniversalProjectileCore.json -->

# AUniversalProjectileCore

通用抛体基类

## Inheritance

`AActor` -> `IObjectPoolInterface` -> `IOwnershipChainInterface`

## Events

### `ReceiveOnBounce`

```text
ReceiveOnBounce(ImpactResult: FHitResult &, ImpactVelocity: FVector &) -> void
```

弹跳时的额外接口
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `FHitResult &` | - |
| `ImpactVelocity` | `FVector &` | 碰撞速度 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveLaunchBullet`

```text
ReceiveLaunchBullet() -> void
```

发射时的额外接口
	 生效范围：S

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTarget`

```text
SetTarget(TargetPawn: APawn *) -> void
```

修改Target的接口，能触发对应目标修改接口
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveOnProjectileDestroyed`

```text
ReceiveOnProjectileDestroyed() -> void
```

销毁时的额外接口
	 生效范围：SC

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnBulletHitDelegate`

```text
OnBulletHitDelegate(ImpactResult: const FHitResult&) -> void
```

Delegate
	  生效范围S
	  通用抛体命中事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `const FHitResult&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnLaunchBulletDelegate`

```text
OnLaunchBulletDelegate() -> void
```

Delegate
	  生效范围S
	  抛体发射事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AUtilityTickActor.json -->

# AUtilityTickActor

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CheckData` | `TArray < FPHXCheckData >` | - |

## Functions

### `AddCheckData`

```text
AddCheckData(InCheckData: FPHXCheckData &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCheckData` | `FPHXCheckData &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CheckComponentPHXError`

```text
CheckComponentPHXError(InComponent: UPrimitiveComponent *, InErrorTag: FString &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InComponent` | `UPrimitiveComponent *` | - |
| `InErrorTag` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AVectorFieldVolume.json -->

# AVectorFieldVolume

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VectorFieldComponent` | `UVectorFieldComponent *` | - |
| `SpriteComponent` | `UBillboardComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AVolume.json -->

# AVolume

An editable 3D volume placed in a level. Different types of volumes perform different functions

## Inheritance

`ABrush`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bSimpleTestWithBounds` | `uint32` | - |
| `EditBrushColor` | `FColor` | - |
| `bEditColored` | `uint32` | - |
| `bEditSolidWhenSelected` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AWindDirectionalSource.json -->

# AWindDirectionalSource

Actor that provides a directional wind source. Only affects SpeedTree assets.

## Inheritance

`AInfo`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Component` | `UWindDirectionalSourceComponent *` | - |
| `ArrowComponent` | `UArrowComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/AWorldSettings.json -->

# AWorldSettings

Actor containing all script accessible world properties.

## Inheritance

`AInfo` -> `IInterface_AssetUserData`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BlueprintContainer` | `TSubclassOf < AActor >` | - |
| `SaveLocOffset` | `FVector` | - |
| `bEnableFOVDistanceCulling` | `uint32` | FOV Distance Culling |
| `FOVCulling` | `TArray < FVector2D >` | - |
| `bEnableWorldBoundsChecks` | `uint32` | DEFAULT BASIC PHYSICS SETTINGS <br>	 If true, enables CheckStillInWorld checks |
| `bEnableNavigationSystem` | `uint32` | if set to false navigation system will not get created (and all navigation functionality won't be accessible) |
| `bEnableAISystem` | `uint32` | if set to false AI system will not get created. Use it to disable all AI-related activity on a map |
| `bEnalbeLevelLoadConditionControl` | `uint32` | - |
| `bEnableWorldComposition` | `uint32` | Enables tools for composing a tiled world.<br>	  Level has to be saved and all sub-levels removed before enabling this option. |
| `bWorldCompositionPIESupportLevelRotation` | `uint32` | - |
| `bPIECloseFixupLazyPointers` | `uint32` | - |
| `bEnableRescanRestriction` | `uint32` | - |
| `bOnlyIncludeWhiteList` | `uint32` | - |
| `bAlwaysExcludeBlackList` | `uint32` | - |
| `WhiteListRescanFolders` | `TArray < FString >` | - |
| `WhiteListRescanLevelPaths` | `TArray < FString >` | - |
| `BlackListRescanFolders` | `TArray < FString >` | - |
| `BlackListRescanLevelPaths` | `TArray < FString >` | - |
| `bEnableAdditionalRescanRoots` | `uint32` | Master switch for cross-folder sub-levels. When enabled, AdditionalRescanRoots is<br>	  consumed by UWorldComposition::Rescan() to scan extra mounted content roots in<br>	  addition to the persistent map's own folder.<br>	 <br>	  Orthogonal to bEnableRescanRestriction (WhiteListBlackList): both can be combined. |
| `AdditionalRescanRoots` | `TArray < FAdditionalRescanRootEntry >` | Per-root scan and filter configuration. See FAdditionalRescanRootEntry.<br>	 <br>	  Example:<br>	    [0] RootPath     = GameCommonSharedTiles<br>	        IncludeTiles = ["Forest", "PlainTile_X0_Y0"]<br>	        ExcludeTiles = ["ForestDebug_Tile"]<br>	    [1] RootPath     = GameCommonSharedBuildings<br>	        ExcludeTiles = ["Office_LowPoly"]<br>	 <br>	  Notes:<br>	    - LOD tiles (_LOD1.._LOD4) must still sit next to their owning tile.<br>	    - Filters in this struct are independent of the global WhiteListBlackList Rescan settings. |
| `bUseClientSideLevelStreamingVolumes` | `uint32` | Enables client-side streaming volumes instead of server-side.<br>	  Expected usage scenario: server has all streaming levels always loaded, clients independently stream levels inout based on streaming volumes. |
| `bEnableWorldOriginRebasing` | `uint32` | World origin will shift to a camera position when camera goes far away from current origin |
| `bWorldGravitySet` | `uint32` | if set to true, when we call GetGravityZ we assume WorldGravityZ has already been initialized and skip the lookup of DefaultGravityZ and GlobalGravityZ |
| `bGlobalGravitySet` | `uint32` | If set to true we will use GlobalGravityZ instead of project setting DefaultGravityZ |
| `KillZ` | `float` | - |
| `KillZDamageType` | `TSubclassOf < UDamageType >` | - |
| `WorldGravityZ` | `float` | - |
| `GlobalGravityZ` | `float` | - |
| `DefaultPhysicsVolumeClass` | `TSubclassOf < ADefaultPhysicsVolume >` | - |
| `PhysicsCollisionHandlerClass` | `TSubclassOf < UPhysicsCollisionHandler >` | - |
| `DefaultGameMode` | `TSubclassOf < AGameModeBase >` | GAMEMODE SETTINGS <br>	 The default GameMode to use when starting this map in the game. If this value is NULL, the INI setting for default game type is used. |
| `GameNetworkManagerClass` | `TSubclassOf < AGameNetworkManager >` | Class of GameNetworkManager to spawn for network games |
| `StreamVolumeExManagerClass` | `TSubclassOf < AStreamVolumeExManager >` | - |
| `PackedLightAndShadowMapTextureSize` | `int32` | RENDERING SETTINGS <br>	 Maximum size of textures for packed light and shadow maps |
| `bMinimizeBSPSections` | `uint32` | Causes the BSP build to generate as few sections as possible.<br>	  This is useful when you need to reduce draw calls but can reduce texture streaming efficiency and effective lightmap resolution.<br>	  Note - changes require a rebuild to propagate.  Also, be sure to select all surfaces and make sure they all have the same flags to minimize section count. |
| `DefaultColorScale` | `FVector` | Default color scale for the level |
| `DefaultMaxDistanceFieldOcclusionDistance` | `float` | Max occlusion distance used by mesh distance fields, overridden if there is a movable skylight. |
| `GlobalDistanceFieldViewDistance` | `float` | Distance from the camera that the global distance field should cover. |
| `bEnableUpdateTransformViewTranslated` | `uint32` | - |
| `bEnableWorldComposition2DLoading` | `uint32` | - |
| `MaxWorldSize` | `float` | - |
| `RegionSizeNear` | `int32` | - |
| `RegionSizeFar` | `int32` | - |
| `RegionXAdd` | `bool` | - |
| `RegionYAdd` | `bool` | - |
| `UnlimitedRegionZ` | `bool` | - |
| `Graduation` | `int32` | - |
| `CompositionSize` | `int32` | - |
| `DynamicIndirectShadowsSelfShadowingIntensity` | `float` | Controls the intensity of self-shadowing from capsule indirect shadows.<br>	  These types of shadows use approximate occluder representations, so reducing self-shadowing intensity can hide those artifacts. |
| `bPrecomputeVisibility` | `uint32` | PRECOMPUTED VISIBILITY SETTINGS <br>	<br>	  Whether to place visibility cells inside Precomputed Visibility Volumes and along camera tracks in this level.<br>	  Precomputing visibility reduces rendering thread time at the cost of some runtime memory and somewhat increased lighting build times. |
| `bPlaceCellsOnlyAlongCameraTracks` | `uint32` | Whether to place visibility cells only along camera tracks or only above shadow casting surfaces. |
| `VisibilityCellSize` | `int32` | World space size of precomputed visibility cells in x and y.<br>	  Smaller sizes produce more effective occlusion culling at the cost of increased runtime memory usage and lighting build times. |
| `PlayAreaHeight` | `float` | Play Area Height ( Cell Z |
| `DynamicCellSize` | `FVector2D` | Dynamic Cell Size ( Dynamic Cell XY, Z |
| `PrecomputedVisibilitySettings` | `FLightmassPrecomputedVisibilitySettings` | - |
| `VisibilityAggressiveness` | `TEnumAsByte < enum EVisibilityAggressiveness >` | Determines how aggressive precomputed visibility should be.<br>	  More aggressive settings cull more objects but also cause more visibility errors like popping. |
| `bForceNoPrecomputedLighting` | `uint32` | LIGHTMASS RELATED SETTINGS <br>	<br>	  Whether to force lightmaps and other precomputed lighting to not be created even when the engine thinks they are needed.<br>	  This is useful for improving iteration in levels with fully dynamic lighting and shadowing.<br>	  Note that any lighting and shadowing interactions that are usually precomputed will be lost if this is enabled. |
| `bUseTieredBuildData` | `uint32` | - |
| `LightmassSettings` | `FLightmassWorldInfoSettings` | - |
| `LightmassSettingsHigh` | `FLightmassWorldInfoSettings` | - |
| `LightmassSettingsHighPlus` | `FLightmassWorldInfoSettings` | - |
| `IdeaBakingSettings` | `FIdeaBakingWorldInfoSettings` | - |
| `SurfelRayTracingSettings` | `FSurfelRayTracingSettings` | - |
| `DefaultReverbSettings` | `FReverbSettings` | AUDIO SETTINGS <br>	 Default reverb settings used by audio volumes. |
| `DefaultAmbientZoneSettings` | `FInteriorSettings` | Default interior settings used by audio volumes. |
| `DefaultBaseSoundMix` | `USoundMix *` | Default Base SoundMix. |
| `WorldToMeters` | `float` | DEFAULT SETTINGS <br>	 scale of 1uu to 1m in real world measurements, for HMD and other physically tracked devices (e.g. 1uu = 1cm would be 100.0) |
| `MonoCullingDistance` | `float` | Distance from the player after which content will be rendered in mono if monoscopic far field rendering is activated |
| `BookMarks` | `UBookMark *` | EDITOR ONLY SETTINGS <br>	 Level Bookmarks: 10 should be MAX_BOOKMARK_NUMBER @fixmeconst |
| `TimeDilation` | `float` | Normally 1 - scales real time passage.<br>	  Warning - most use cases should use GetEffectiveTimeDilation() instead of reading from this directly |
| `MatineeTimeDilation` | `float` | - |
| `DemoPlayTimeDilation` | `float` | - |
| `MinGlobalTimeDilation` | `float` | Lowest acceptable global time dilation. |
| `MaxGlobalTimeDilation` | `float` | Highest acceptable global time dilation. |
| `MinUndilatedFrameTime` | `float` | Smallest possible frametime, not considering dilation. Equiv to 1FastestFPS. |
| `MaxUndilatedFrameTime` | `float` | Largest possible frametime, not considering dilation. Equiv to 1SlowestFPS. |
| `Pauser` | `APlayerState *` | - |
| `bHighPriorityLoading` | `uint32` | when this flag is set, more time is allocated to background loading (replicated) |
| `bHighPriorityLoadingLocal` | `uint32` | copy of bHighPriorityLoading that is not replicated, for clientside-only loading operations |
| `ReplicationViewers` | `TArray < struct FNetViewer >` | valid only during replication - information about the player(s) being replicated to<br>	  (there could be more than one in the case of a splitscreen client) |
| `AssetUserData` | `TArray < UAssetUserData * >` | Array of user data stored with the asset |
| `LODRelativeDistances` | `TArray < float >` | - |
| `bEnablestreamingLevelLOD` | `bool` | - |
| `WorldCompositionNums` | `int32` | - |
| `CompositionBlockLength` | `int32` | - |
| `OriginOfTheRegion` | `FVector` | - |
| `bEnableObjectPool` | `bool` | - |
| `LevelReorganizationData` | `UDataAsset *` | - |
| `bEnableHierarchicalLODSystem` | `uint32` | if set to true, hierarchical LODs will be built, which will create hierarchical LODActors |
| `HLODSetupAsset` | `TSoftClassPtr < UHierarchicalLODSetup >` | If set overrides the level settings and global project settings |
| `OverrideBaseMaterial` | `TSoftObjectPtr < UMaterialInterface >` | If set overrides the project-wide base material used for Proxy Materials |
| `HierarchicalLODSetup` | `TArray < struct FHierarchicalSimplification >` | Hierarchical LOD Setup |
| `NumHLODLevels` | `int32` | - |
| `bGenerateSingleClusterForLevel` | `uint32` | if set to true, all eligible actors in this level will be added to a single cluster representing the entire level (used for small sublevels) |

## Functions

### `SaveEntireWorld`

```text
SaveEntireWorld() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_WorldGravityZ`

```text
OnRep_WorldGravityZ() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/BackpackUIComponent.json -->

# BackpackUIComponent

UGC V2背包UI组件

需启用及配合新背包系统使用，具体参见https://developer.gp.qq.com/wikieditor/#/catalog/20104

## Functions

### `GetBackpackDragDropWidget`

```text
GetBackpackDragDropWidget() -> FSoftClassPath|nil
```

获取背包拖拽控件类
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `FSoftClassPath\|nil` | 拖拽控件类，未配置则返回nil |

### `CloseLobbyPanel`

```text
CloseLobbyPanel()
```

关闭大厅背包界面(已废弃)
生效范围：客户端

### `OpenLobbyBackpackMainUI`

```text
OpenLobbyBackpackMainUI(Mode: number)
```

打开大厅背包界面(已废弃)
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Mode` | `number` | 1:背包+装备栏 2:背包+仓库 3:背包+装备栏+仓库 |

### `OnOpenBattleMainPanel`

```text
OnOpenBattleMainPanel(Panel: UUserWidget)
```

背包UI打开后执行

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Panel` | `UUserWidget` | 背包主界面控件 |

### `OnCloseBattleMainPanel`

```text
OnCloseBattleMainPanel(Panel: UUserWidget)
```

背包UI关闭后执行

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Panel` | `UUserWidget` | 背包主界面控件 |

### `OnOpenDeletePanel`

```text
OnOpenDeletePanel(Panel: UUserWidget)
```

当打开删除弹窗时调用（仅作为通知钩子，内核已用AddToSlot挂载，此处不处理AddToViewport）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Panel` | `UUserWidget` | 面板控件 |

### `OnOpenSavePanel`

```text
OnOpenSavePanel(Panel: UUserWidget)
```

当打开存入仓库确认弹窗时调用（仅作为通知钩子，内核已用AddToSlot挂载，此处不处理AddToViewport）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Panel` | `UUserWidget` | 面板控件 |

### `OnOpenTakeOutPanel`

```text
OnOpenTakeOutPanel(Panel: UUserWidget)
```

当打开存入背包确认弹窗时调用（仅作为通知钩子，内核已用AddToSlot挂载，此处不处理AddToViewport）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Panel` | `UUserWidget` | 面板控件 |

### `ClickLockBackpackItem`

```text
ClickLockBackpackItem(type: number) -> UUserWidget
```

点击上锁格子的响应函数
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `type` | `number` | 类型 [0:背包数据, 1:仓库数据] |

**Returns**

| Type | Description |
|---|---|
| `UUserWidget` | 弹窗控件 |

### `OnClickLockBackpackItem`

```text
OnClickLockBackpackItem(Panel: UUserWidget)
```

点击上锁格子后回调(重写ClickLockBackpackItem后不会执行)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Panel` | `UUserWidget` | 弹窗面板，取自ClickLockBackpackItem返回值，可能为nil |

### `IsDiscardAreaVisible`

```text
IsDiscardAreaVisible() -> boolean
```

是否显示丢弃区域
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否显示丢弃区域 |

### `OnOpenSaveOrWithDrawPanel`

```text
OnOpenSaveOrWithDrawPanel(Panel: UUserWidget)
```

当打开存入取出代币时调用（仅作为通知钩子，内核已用AddToSlot挂载，此处不处理AddToViewport）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Panel` | `UUserWidget` | 面板控件 |

### `OnOpenDropItemPanel`

```text
OnOpenDropItemPanel(Panel: UUserWidget)
```

当打开丢弃物品弹窗时调用（仅作为通知钩子，内核已用AddToSlot挂载，此处不处理AddToViewport）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Panel` | `UUserWidget` | 面板控件 |

### `GetUGCAvailableServerRPCs`

```text
GetUGCAvailableServerRPCs() -> table
```

获取RPC列表 (注意不要使用GetAvailableServerRPCs)

**Returns**

| Type | Description |
|---|---|
| `table` | RPC函数名列表 |

### `CompareQuality`

```text
CompareQuality(Data1: table, Data2: table) -> boolean
```

默认排序函数
生效范围: 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Data1` | `table` | 物品数据1 {DefineID:物品DefineID, Idx:格子索引} |
| `Data2` | `table` | 物品数据2 {DefineID:物品DefineID, Idx:格子索引} |

**Returns**

| Type | Description |
|---|---|
| `boolean` | true:物品1在前, false:物品2在前 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/BP_UGCPickUpListComponent.json -->

# BP_UGCPickUpListComponent

UGC物品拾取组件

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BP_UGCPickUpListComponent.RefreshInterval` | `-` | - |
| `BP_UGCPickUpListComponent.bCanAutoPickC` | `-` | - |
| `BP_UGCPickUpListComponent.HideForAimC` | `-` | - |
| `BP_UGCPickUpListComponent.bNeedRefresh` | `-` | - |
| `BP_UGCPickUpListComponent.LastItemCount` | `-` | - |
| `BP_UGCPickUpListComponent.LastCheckSum` | `-` | - |
| `BP_UGCPickUpListComponent.LastRefreshTime` | `-` | - |
| `BP_UGCPickUpListComponent.ItemUsefulCache` | `-` | - |
| `BP_UGCPickUpListComponent.PickupItemListCache` | `-` | - |
| `BP_UGCPickUpListComponent.TomBoxItemListCache` | `-` | - |
| `BP_UGCPickUpListComponent.PickupItemListCacheChange` | `-` | - |
| `BP_UGCPickUpListComponent.TomBoxItemListCacheChange` | `-` | - |
| `BP_UGCPickUpListComponent.bUpDateListDataChange` | `-` | - |

## Functions

### `IsWeaponItem`

```text
IsWeaponItem()
```

判断物品是否为武器（射击武器，排除近战和弩）
 仅使用V2标签系统
 @param ItemID number 物品ID
 @return boolean, boolean 是否为武器, 是否为手枪

### `GetHeldWeaponSlotName`

```text
GetHeldWeaponSlotName()
```

获取当前手持武器的装备槽位名
 通过 WeaponManager 获取当前武器槽位 ESurviveWeaponPropSlot，映射到背包槽位名
 @return string|nil 装备槽位名

### `FindBestEquipSlot`

```text
FindBestEquipSlot()
```

查找最佳装备槽位（仅V2标签）
 返回值说明：
   bestSlot=nil, bMatchAnySlot=false → 不匹配装备槽（背包物品）
   bestSlot=nil, bMatchAnySlot=true  → 装备类但无可用槽位（非武器槽满）
   bestSlot=string, bMatchAnySlot=true → 有可用槽位（引擎通过AddAndEquip自动处理空槽/替换）
 @param ItemID number 物品ID
 @param bIsWeapon boolean 是否为武器
 @return string|nil 最佳槽位名, boolean 物品是否匹配到装备槽

### `CheckEquipSlot`

```text
CheckEquipSlot()
```

检查物品的装备槽位信息（纯检查，不执行拾取）
 供主面板调用，根据检查结果决定拾取方式
 @param ItemID number 物品ID
 @return string|nil bestSlot 最佳槽位名
 @return boolean bMatchAnySlot 物品是否匹配到装备槽
 @return boolean bIsWeapon 是否为武器

### `SortItems`

```text
SortItems()
```

物品排序比较函数：按有用性、规则优先级、自动拾取标记、OrderWeight排序
 @param a table 物品数据A
 @param b table 物品数据B
 @return boolean a是否应该排在b前面

### `InitPickupRules`

```text
InitPickupRules() -> void
```

【工具函数】初始化拾取规则链
 功能：从蓝图变量PickupRulesCollection读取规则配置，构建规则链PickupRuleChain
 依赖：self.PickupRulesCollection（蓝图变量，Struct_PickUpRules结构体）

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CreateRuleResult`

```text
CreateRuleResult(match: boolean, score: number, count: number, autoPick: boolean)
```

【工具函数】创建规则评估结果
 功能：创建规则评估结果的统一格式，供规则函数返回

**Parameters**

| Name | Type | Description |
|---|---|---|
| `match` | `boolean` | 是否命中该规则 |
| `score` | `number` | 评分（越高排序越靠前） |
| `count` | `number` | 需要拾取的数量 |
| `autoPick` | `boolean` | 是否自动拾取 |

### `GetBackpackComponent`

```text
GetBackpackComponent() -> UBackpackComponent|nil
```

【工具函数】获取背包组件
 功能：从PlayerController获取背包组件
 依赖：STExtraBlueprintFunctionLibrary.GetBackpackComponentFromController(PC)

**Returns**

| Type | Description |
|---|---|
| `UBackpackComponent\|nil` | 背包组件 |

### `GetWeaponManagerComponent`

```text
GetWeaponManagerComponent() -> UWeaponManagerComponent|nil
```

【工具函数】获取武器管理组件
 功能：从Pawn获取武器管理组件
 依赖：self:GetPawn()、BC:GetWeaponManager()

**Returns**

| Type | Description |
|---|---|
| `UWeaponManagerComponent\|nil` | 武器管理组件 |

### `GetBackpackItemCount`

```text
GetBackpackItemCount(ItemDefineID: FItemDefineID) -> number
```

【工具函数】获取背包中指定物品的数量（含已装备的）
 功能：统计背包和装备槽中指定物品的总数量
 依赖：self:GetBackpackComponent()

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品定义ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 数量（默认0） |

### `GetTotalItemCountByID`

```text
GetTotalItemCountByID(ItemID: number) -> number
```

【工具函数】获取指定ItemID的持有总量（背包 + 已装备武器槽）
 功能：获取物品在背包和装备槽中的总数量，用于武器类物品的RecommendPickCount判断
 依赖：UGCBackpackSystemV2.GetItemDefineIDsByIDV2(PC, ItemID)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品TypeSpecificID |

**Returns**

| Type | Description |
|---|---|
| `number` | 持有总量（默认0） |

### `GetItemHandle`

```text
GetItemHandle(ItemID: number) -> table|nil
```

【工具函数】获取物品配置Handle
 功能：从UGCItemSystemV2获取物品配置Handle，包含OrderWeight、RecommendPickCount等配置
 依赖：UGCItemSystemV2.GetConfigItemHandle(ItemID)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `table\|nil` | 物品Handle（包含配置信息） |

### `GetRecommendPickCount`

```text
GetRecommendPickCount(ItemID: number) -> number|nil
```

【工具函数】获取物品推荐拾取数量
 功能：从物品配置Handle中获取推荐拾取数量，nil表示不拾取
 依赖：self:GetItemHandle(ItemID)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `number\|nil` | 推荐数量（nil 表示不拾取，默认1） |

### `GetItemOrderWeight`

```text
GetItemOrderWeight(ItemID: number) -> number
```

【工具函数】获取物品排序权重
 功能：从物品配置Handle中获取排序权重，用于同类物品比较
 依赖：self:GetItemHandle(ItemID)、ItemUtils.GetItemWeightForOrder(ItemID)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 权重值（默认0） |

### `GetItemQuality`

```text
GetItemQuality(ItemID: number) -> number
```

【工具函数】获取物品品质等级
 功能：获取物品品质等级（0-5），用于排序和替换判断
 依赖：UGCItemSystemV2.GetItemQualityV2(ItemID)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 品质等级（0-5，默认0） |

### `GetItemLevel`

```text
GetItemLevel(ItemID: number) -> number
```

【工具函数】获取物品等级
 功能：获取物品等级（适用于背包、防具、头盔等装备，如一级/二级/三级）
 依赖：UGCItemSystemV2.GetItemLevelV2(ItemID)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 等级（0表示无等级，默认0） |

### `HasTag`

```text
HasTag(ItemID: number, TagName: string) -> boolean
```

【工具函数】检查物品是否具有指定标签
 功能：使用V2标签系统检查物品是否具有指定标签
 依赖：UGCItemSystemV2.ItemHasTagV2(ItemID, TagName)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |
| `TagName` | `string` | 标签名 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否具有该标签 |

### `GetSwitcherConfig`

```text
GetSwitcherConfig(configName: string) -> boolean
```

【工具函数】获取背包开关配置
 功能：获取背包系统的开关配置（如自动拾取手枪等）
 依赖：self:GetBackpackComponent()、BackpackComp:GetSwitcherCfgList(configName)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `configName` | `string` | 配置名（如"AutoPickUpPistol"） |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 配置值（默认false） |

### `RuleWeapon`

```text
RuleWeapon()
```

武器规则：排除近战/弩 → 检查槽位（空槽位优先，无空槽位可替换）
 手枪: 当前无手枪+长枪没满+开启"自动拾取手枪" → 自动拾取；可替换槽位 → 自动拾取(低优先)
 长枪: 不足两把 → 自动拾取；可替换槽位 → 自动拾取(低优先)
 @param ItemDefineID FItemDefineID 物品定义ID
 @param Count number 物品数量
 @return table RuleResult

### `RuleAttachment`

```text
RuleAttachment()
```

配件规则：遍历所有武器检查配件适配性
 有空位 → 拾取；比同槽位配件更好(OrderWeight/品质) → 替换拾取
 快扩(Tag=Item.Attachments.Magazine)最高优先级：品质优先，OrderWeight次之
 普通配件：OrderWeight优先，品质次之
 @param ItemDefineID FItemDefineID 物品定义ID
 @param Count number 物品数量
 @return table RuleResult

### `RuleAmmo`

```text
RuleAmmo()
```

弹药规则：遍历所有武器检查是否使用此弹药
 需求总量 = RecommendPickCount(配表默认弹药量) * 使用该弹药的武器数
 背包总弹量低于需求总量 → 拾取差值
 @param ItemDefineID FItemDefineID 物品定义ID
 @param Count number 物品数量
 @return table RuleResult

### `RuleMedicine`

```text
RuleMedicine()
```

药品规则：每种药品单独配置拾取数量(RecommendPickCount)
 背包数量低于推荐值 → 拾取差值
 @param ItemDefineID FItemDefineID 物品定义ID
 @param Count number 物品数量
 @return table RuleResult

### `RuleThrowable`

```text
RuleThrowable()
```

投掷物规则：背包数量低于RecommendPickCount → 拾取差值
 @param ItemDefineID FItemDefineID 物品定义ID
 @param Count number 物品数量
 @return table RuleResult

### `GetItemDurabilityRatio`

```text
GetItemDurabilityRatio()
```

获取物品耐久度比例（当前耐久度/最大耐久度）
 无耐久度词条或满耐久返回1
 @param ItemID number 物品ID
 @param ItemDefineID FItemDefineID|nil 物品DefineID
 @return number 耐久度比例（0~1）

### `ShouldPickupBetterEquipment`

```text
ShouldPickupBetterEquipment()
```

比较两件装备，返回是否应该拾取新装备
 比较优先级：等级 > 品质 > 权重 > 耐久度（仅AvatarEquipment）
 耐久度阈值逻辑：当等级/品质差距在1级以内，耐久度差距超过阈值时，优先考虑耐久度
 @param NewItemID number 新物品ID
 @param OldItemID number 旧物品ID
 @param bIsAttchement boolean 是否为配件
 @param NewItemDefineID FItemDefineID|nil 新物品DefineID
 @param OldItemDefineID FItemDefineID|nil 旧物品DefineID
 @return boolean, number bShouldPickup, score

### `RuleArmorBackpack`

```text
RuleArmorBackpack()
```

防具背包规则：检查装备槽位，比较装备品质
 有空槽位 → 拾取（检查RecommendPickCount）
 槽位全满 → 使用ShouldPickupBetterEquipment比较装备品质，更好的装备 → 替换拾取
 同时检查 RecommendPickCount 控制拾取数量
 @param ItemDefineID FItemDefineID 物品定义ID
 @param Count number 物品数量
 @return table RuleResult

### `RuleGeneralOrder`

```text
RuleGeneralOrder()
```

通用排序规则(所有物品)：score = Handle.OrderWeight * 100 + 品质
 用于兜底排序，不触发自动拾取
 @param ItemDefineID FItemDefineID 物品定义ID
 @param Count number 物品数量
 @return table RuleResult

### `Server_SetEquipReason`

```text
Server_SetEquipReason()
```

服务器端 RPC：设置指定物品的装备Reason（为客户端预测拾取做准备）
 @param PlayerController UserData 玩家控制器（系统自动传入）
 @param ItemDefineID table 物品DefineID

### `Server_ResetEquipReason`

```text
Server_ResetEquipReason()
```

服务器端 RPC：重置指定物品的装备Reason
 @param PlayerController UserData 玩家控制器（系统自动传入）
 @param ItemDefineID table 物品DefineID

### `GetUGCAvailableServerRPCs`

```text
GetUGCAvailableServerRPCs() -> table
```

获取RPC列表 (注意不要使用GetAvailableServerRPCs)

**Returns**

| Type | Description |
|---|---|
| `table` | RPC函数名列表 |

### `CheckItemIsEquipped`

```text
CheckItemIsEquipped()
```

检查指定物品实例是否已装备到任何槽位
 @param PlayerController UserData 玩家控制器
 @param ItemDefineID table 物品实例的 DefineID（通过 totable(MainItemData.ID) 获得）
 @return boolean 该特定物品实例是否已装备

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/BP_UGCVehicleRefresherTool.json -->

# BP_UGCVehicleRefresherTool

载具刷新器工具，用于管理载具的自动刷新和生成

## Functions

### `AddVehicleEventListener`

```text
AddVehicleEventListener(callback: function, context: any)
```

添加载具生成事件监听器，外部代码调用此方法注册载具生成事件监听
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `callback` | `function` | 回调函数，参数为(Vehicle) |
| `context` | `any` | 上下文对象（可选） |

### `AddVehicleDriveAwayEventListener`

```text
AddVehicleDriveAwayEventListener(callback: function, context: any)
```

添加载具开走事件监听器，外部代码调用此方法注册载具开走事件监听
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `callback` | `function` | 回调函数，参数为(Vehicle) |
| `context` | `any` | 上下文对象（可选） |

### `RemoveVehicleEventListener`

```text
RemoveVehicleEventListener(callback: function, context: any)
```

移除载具生成事件监听器
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `callback` | `function` | 回调函数 |
| `context` | `any` | 上下文对象 |

### `RemoveVehicleDriveAwayEventListener`

```text
RemoveVehicleDriveAwayEventListener(callback: function, context: any)
```

移除载具开走事件监听器
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `callback` | `function` | 回调函数 |
| `context` | `any` | 上下文对象 |

### `GenerateVehicle`

```text
GenerateVehicle() -> boolean
```

根据权重配置随机生成载具
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `boolean` | true-生成成功, false-生成失败 |

### `GenerateCustomizeVehicle`

```text
GenerateCustomizeVehicle(VehiclePath: string) -> boolean
```

生成指定的载具蓝图
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `VehiclePath` | `string` | 载具蓝图路径，如"/Game/Arts_PlayerBluePrints/Vehicle/VH_Buggy/BP_VH_Buggy.BP_VH_Buggy_C" |

**Returns**

| Type | Description |
|---|---|
| `boolean` | true-生成成功, false-生成失败 |

### `DestroyCurrentVehicle`

```text
DestroyCurrentVehicle() -> boolean
```

销毁当前刷新点管理的载具
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `boolean` | true-销毁成功, false-销毁失败 |

### `ResetVehicleRespawnPoint`

```text
ResetVehicleRespawnPoint() -> boolean
```

重置载具刷新点，如果载具还在原地，先销毁再重新刷新
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `boolean` | true-重置成功, false-重置失败 |

### `GetVehicleRespawnPointConfig`

```text
GetVehicleRespawnPointConfig() -> table
```

获取配置的载具列表信息
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `table` | 载具配置列表，包含index、path、weight字段 |

### `GetVehicleStatusConfig`

```text
GetVehicleStatusConfig() -> table
```

获取当前车辆的实时状态信息
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `table` | 当前车辆信息（包含isValid、location、healthState、hasDriver等字段），如无车辆返回false |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/CommodityOperationManager.json -->

# CommodityOperationManager

UGC商业化购买流程全局管理器

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CommodityOperationManager.BuyProductResultDelegate` | `-` | 生效范围：客户端&&服务端<br>发起购买商品后触发<br>@param Result BuyProductResult @购买结果 |
| `CommodityOperationManager.LimitProductUpdateDelegate` | `-` | 生效范围：客户端&&服务端<br>限购商品购买次数发生变化时触发 |
| `CommodityOperationManager.PurchasedProductListUpdateDelegate` | `-` | 生效范围：客户端&&服务端<br>商品购买次数发生变化时触发 |

## Functions

### `BuyProduct`

```text
BuyProduct(ProductID: number, Num: number, CurrentPrice: number, bCheckPrivilege: boolean) -> PromiseFuture
```

发起商品购买
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProductID` | `number` | 商品的ID |
| `Num` | `number` | 购买商品数量 |
| `CurrentPrice` | `number` | 发起购买时的价格，用于校验 |
| `bCheckPrivilege` | `boolean` | 是否检查玩家特权（即当前商品为仅特权可购买），默认false |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 绿洲币购买UI界面的PromiseFuture实例，非绿洲币商品则返回nil |

### `ServerBuyProduct`

```text
ServerBuyProduct(PlayerKey: number, ProductID: number, Num: number, CurrentPrice: number, bCheckPrivilege: boolean)
```

发起自定义货币商品购买
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 发起购买者的 PlayerKey |
| `ProductID` | `number` | 商品的ID |
| `Num` | `number` | 购买商品数量 |
| `CurrentPrice` | `number` | 发起购买时的价格，用于校验 |
| `bCheckPrivilege` | `boolean` | 是否检查玩家特权（即当前商品为仅特权可购买），默认false |

### `CanAfford`

```text
CanAfford(ProductID: number, Num: number, PlayerController: UUGCPlayerController) -> boolean
```

检查是否买得起指定数量的商品
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProductID` | `number` | 商品的ID |
| `Num` | `number` | 购买的商品数量 |
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端可以不传 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetLimitPurchasedTimes`

```text
GetLimitPurchasedTimes(ProductID: number, PlayerController: UUGCPlayerController) -> number
```

获得限购商品的购买次数
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProductID` | `number` | 商品的ID |
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端可以不传 |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetAllLimitPurchasedProducts`

```text
GetAllLimitPurchasedProducts(PlayerController: UUGCPlayerController) -> table
```

获取所有已购买的限购商品
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端可以不传 |

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `GetPurchasedTimes`

```text
GetPurchasedTimes(ProductID: number, PlayerController: UUGCPlayerController) -> number
```

获得商品的累计购买次数
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProductID` | `number` | 商品的ID |
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端可以不传 |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetAllPurchasedProducts`

```text
GetAllPurchasedProducts(PlayerController: UUGCPlayerController) -> table
```

获取所有已购买的商品
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端可以不传 |

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `GetAllProductData`

```text
GetAllProductData() -> table
```

获取所有商品信息
生效范围：客户端&&服务器

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `GetProductData`

```text
GetProductData(ProductID: number) -> table
```

获取指定商品信息
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProductID` | `number` | 商品的ID |

**Returns**

| Type | Description |
|---|---|
| `table` | - |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9F%BA%E7%A1%80%E5%8A%9F%E8%83%BD/Delegate.json -->

# Delegate

Lua代理

Lua代理
- 使用 Add(callable, obj) 绑定可调用对象
- 使用 Remove(callable, obj) 解绑可调用对象
- 使用 Broadcast(...) 触发委托

## Functions

### `Add`

```text
Add()
```

绑定可调用对象
第一个参数为可调用对象（函数），第二个参数为定义了对应函数的表实例
例：Delegate:Add(self.foo, self)
生效范围：服务器&客户端

### `Remove`

```text
Remove() -> nil
```

移除可调用对象
第一个参数为可调用对象（函数），第二个参数为定义了对应函数的表实例
例：Delegate:Remove(self.foo, self)
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `nil` | - |

### `RemoveAll`

```text
RemoveAll(Callable: function)
```

移除可调用对象（函数）上绑定的所有监听函数
例：Delegate:RemoveAll()
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Callable` | `function` | 【可选】可调用对象（函数） |

### `Broadcast`

```text
Broadcast()
```

广播调用监听此委托的所有函数
例：Delegate:Broadcast(param1, param2 ...)
生效范围：服务器&客户端

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/PlayerListManager.json -->

# PlayerListManager

玩家列表全局管理器

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PlayerListManager.PlayerListUpdateDelegate` | `-` | 玩家列表数据更新委托<br>生效范围：客户端<br>@param PlayerListData FPlayerListEntry[] @排序后的玩家列表 |

## Functions

### `UpdatePlayerSortValue`

```text
UpdatePlayerSortValue(PlayerController: BP_UGCPlayerController_C, UID: number, SortValue: number) -> boolean
```

更新排序属性值
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `BP_UGCPlayerController_C` | 玩家控制器 |
| `UID` | `number` | 玩家UID |
| `SortValue` | `number` | 排序数值 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否更新成功 |

### `UpdatePlayerDisplayValue`

```text
UpdatePlayerDisplayValue(PlayerController: BP_UGCPlayerController_C, UID: number, DisplayValue: number) -> boolean
```

更新展示属性值
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `BP_UGCPlayerController_C` | 玩家控制器 |
| `UID` | `number` | 玩家UID |
| `DisplayValue` | `number` | 展示数值 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否更新成功 |

### `GetPlayerListData`

```text
GetPlayerListData() -> FPlayerListEntry[]
```

获取排序后的玩家列表
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `FPlayerListEntry[]` | 排序后的玩家列表 |

### `GetPlayerListConfig`

```text
GetPlayerListConfig() -> FPlayerListConfig
```

获取玩家列表配置
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `FPlayerListConfig` | - |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/PromiseFuture.json -->

# PromiseFuture

提供处理异步操作的类，支持链式调用和状态管理

说明：
- 创建实例: 使用 PromiseFuture.New() 创建新的 PromiseFuture 实例。
- 设置回调: 使用 Then 和 Else 方法设置成功和失败的回调函数。
- 执行逻辑: 使用 Set 方法定义 PromiseFuture 的执行逻辑，可以在其中使用 Yield 暂停执行。
- 前置条件: 可以将其他 PromiseFuture 实例作为前置条件，确保在执行当前 PromiseFuture 之前，所有前置条件都已完成。
- 自动恢复: 可以设置自动恢复功能，监控对象的状态并在需要时自动恢复执行。

## Functions

### `Resume`

```text
Resume(...: any) -> boolean
```

手动恢复 PromiseFuture 的执行

**Parameters**

| Name | Type | Description |
|---|---|---|
| `...` | `any` | 可选的参数，将传递给恢复的协程 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当 IsPrerequisitesEstablished() && IsEstablished() 时返回 true，否则返回 false |

### `IsPrerequisitesEstablished`

```text
IsPrerequisitesEstablished() -> boolean
```

检查所有先决条件是否已建立

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果所有先决条件都已建立则返回 true，否则返回 false |

### `IsAnyPrerequisiteCancellationRequested`

```text
IsAnyPrerequisiteCancellationRequested() -> boolean
```

检查任意先决条件是否已被取消

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果任意先决条件已被取消则返回 true，否则返回 false |

### `IsEstablished`

```text
IsEstablished() -> boolean
```

检查当前 PromiseFuture 是否已建立

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果已建立则返回 true，否则返回 false |

### `WaitForPrerequisites`

```text
WaitForPrerequisites() -> PromiseFuture
```

等待所有前置条件变为已建立状态
如果前置条件未完成，则会自动 Yield
只能在 Set 回调函数中使用

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 当前 PromiseFuture 实例，以支持链式调用 |

### `AddPrerequisites`

```text
AddPrerequisites(Prerequisite: PromiseFuture) -> PromiseFuture
```

添加前置条件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Prerequisite` | `PromiseFuture` | 前置条件 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 当前 PromiseFuture 实例，以支持链式调用 |

### `IsCancellationRequested`

```text
IsCancellationRequested() -> boolean
```

检查当前 PromiseFuture 是否已被取消

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果已被取消则返回 true，否则返回 false |

### `GetError`

```text
GetError() -> any
```

获取协程异常时保存的原始错误对象
主动 Cancel 时返回 nil；协程内业务异常时返回 error 值
可与 IsCancellationRequested 配合区分失败原因：
  IsCancellationRequested()==true 且 GetError()==nil  → 主动 Cancel
  IsCancellationRequested()==true 且 GetError()~=nil  → 协程内抛出的业务异常

**Returns**

| Type | Description |
|---|---|
| `any` | 错误对象，或 nil |

### `Cancel`

```text
Cancel() -> PromiseFuture
```

取消当前 PromiseFuture 的执行

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 当前 PromiseFuture 实例，以支持链式调用 |

### `CancelAll`

```text
CancelAll() -> PromiseFuture
```

取消当前 PromiseFuture 及其所有前置条件的执行

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 当前 PromiseFuture 实例，以支持链式调用 |

### `Get`

```text
Get() -> any
```

获取 Set 回调函数的返回值
只能在 Set、Then 回调函数中使用

**Returns**

| Type | Description |
|---|---|
| `any` | 返回 Set 回调函数的所有返回值 |

### `Then`

```text
Then(Callable: function, ...: any) -> PromiseFuture
```

设置成功回调函数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Callable` | `function` | 回调函数 |
| `...` | `any` | 可选的参数，将传递给回调函数 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 当前 PromiseFuture 实例，以支持链式调用 |

### `Else`

```text
Else(Callable: function, ...: any) -> PromiseFuture
```

设置失败回调函数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Callable` | `function` | 回调函数 |
| `...` | `any` | 可选的参数，将传递给回调函数 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 当前 PromiseFuture 实例，以支持链式调用 |

### `Set`

```text
Set(Setter: function, SetterValue: any, ...: any) -> PromiseFuture
```

设置执行逻辑

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Setter` | `function` | 回调函数 |
| `SetterValue` | `any` | - |
| `...` | `any` | 其他可选参数 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 当前 PromiseFuture 实例，以支持链式调用 |

### `Yield`

```text
Yield(...: any) -> PromiseFuture
```

暂停当前 PromiseFuture 的执行
只能在 Set 回调函数中使用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `...` | `any` | 可选的参数，将传递给 yield(...) 方法 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 当前 PromiseFuture 实例，以支持链式调用 |

### `AutoResume`

```text
AutoResume(WatchedObject: UObject, Interval: number, Timeout: number) -> PromiseFuture
```

设置自动恢复功能

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WatchedObject` | `UObject` | 监控的对象，如果对象被销毁则停止自动恢复 |
| `Interval` | `number` | 自动恢复的间隔，单位为秒 |
| `Timeout` | `number` | 自动恢复的超时时间，单位为秒 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 当前 PromiseFuture 实例，以支持链式调用 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/RankingListManager.json -->

# RankingListManager

UGC排行榜系统全局管理器

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RankingListManager.ShowRankDataChangeDelegate` | `-` | 生效范围：客户端<br>排行榜数据变更回调<br>@param RankID number @榜单ID<br>@param RankingCycles number @榜单周期 |
| `RankingListManager.PlayerRankDataChangeDelegate` | `-` | 生效范围：客户端<br>玩家排名数据变更回调<br>@param RankID number @榜单ID<br>@param RankingCycles number @榜单周期<br>@param UID number @玩家UID |
| `RankingListManager.ProfileDataChangeDelegate` | `-` | 生效范围：客户端<br>玩家信息数据变更回调<br>@param RankID number @榜单ID |
| `RankingListManager.ClaimRankListAwardDelegate` | `-` | 生效范围：客户端&服务端<br>领取奖励回调<br>@param RankID number @榜单ID<br>@param Result boolean @领奖是否成功<br>@param UID number @玩家UID |

## Functions

### `UpdateScore`

```text
UpdateScore(PlayerController: BP_UGCPlayerController_C, UID: number, RankID: number, Score: number, IsIncremental: boolean)
```

更新排行榜分数
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `BP_UGCPlayerController_C` | 玩家控制器 |
| `UID` | `number` | 玩家UID |
| `RankID` | `number` | 排行榜ID |
| `Score` | `number` | 更新分数 |
| `IsIncremental` | `boolean` | 是否增量更新 |

### `GetProfileData`

```text
GetProfileData(RankID: number, UID: number) -> RankListProfileData
```

获取玩家信息，使用前需要调用对应榜单的GetRankListData接口
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RankID` | `number` | 排行榜ID |
| `UID` | `number` | 玩家UID |

**Returns**

| Type | Description |
|---|---|
| `RankListProfileData` | - |

### `ClaimRankListAward`

```text
ClaimRankListAward(PlayerController: BP_UGCPlayerController_C, RankID: number)
```

领取排行榜奖励
生效范围：客户端&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `BP_UGCPlayerController_C` | 玩家控制器 |
| `RankID` | `number` | 排行榜ID |

### `CanClaimRankListAward`

```text
CanClaimRankListAward(PlayerController: BP_UGCPlayerController_C, RankID: number) -> UGCRankListAwardState
```

判断是否可以领取奖励
生效范围：客户端&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `BP_UGCPlayerController_C` | 玩家控制器 |
| `RankID` | `number` | 排行榜ID |

**Returns**

| Type | Description |
|---|---|
| `UGCRankListAwardState` | - |

### `GetPlayerRankData`

```text
GetPlayerRankData(UID: number, RankID: number, RankingCycles: number) -> PlayerRankData
```

获取当前DS内玩家排行榜数据(调用后如果当前缓存数据的获取时间超过RequestInterval或者榜单跨越了结算时间, DS会向后台重新请求一次，刷新缓存数据，但当次调用的返回结果还是旧缓存数据)
生效范围：客户端&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家UID |
| `RankID` | `number` | 排行榜ID |
| `RankingCycles` | `number` | 排行榜周期，0为当期，1为上期 |

**Returns**

| Type | Description |
|---|---|
| `PlayerRankData` | 玩家排行榜数据 |

### `GetRankListData`

```text
GetRankListData(RankID: number, RankingCycles: number) -> RankListData>,
```

获取排行榜数据(调用后如果当前缓存数据的获取时间超过RequestInterval或者榜单跨越了结算时间, DS会向后台重新请求一次，刷新缓存数据，但当次调用的返回结果还是旧缓存数据)
生效范围：客户端&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RankID` | `number` | 排行榜ID |
| `RankingCycles` | `number` | 排行榜周期，0为当期，1为上期 |

**Returns**

| Type | Description |
|---|---|
| `RankListData>,` | boolean |

### `GetShowRankData`

```text
GetShowRankData() -> table
```

获取全部排行榜数据
生效范围：客户端&服务端

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `OpenReportUI`

```text
OpenReportUI(UID: number, PlayerName: string, RankID: number, ShowUID: boolean)
```

打开举报界面
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 举报玩家UID |
| `PlayerName` | `string` | 举报玩家姓名 |
| `RankID` | `number` | 排行榜ID |
| `ShowUID` | `boolean` | 是否显示UID |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/RankingListPlayerComponent.json -->

# RankingListPlayerComponent

UGC排行榜系统组件

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/TaskManager.json -->

# TaskManager

UGC任务系统全局管理器

## Functions

### `GetTaskLineConfig`

```text
GetTaskLineConfig(TaskLineName: string) -> FUGCTaskLineConfig
```

获取任务线配置
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |

**Returns**

| Type | Description |
|---|---|
| `FUGCTaskLineConfig` | - |

### `GetTaskConfig`

```text
GetTaskConfig(TaskID: number) -> FUGCTaskConfig
```

获取任务配置
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `FUGCTaskConfig` | - |

### `GetTaskType`

```text
GetTaskType(TaskID: number) -> number
```

获取任务类型
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetTaskDesc`

```text
GetTaskDesc(TaskID: number) -> string
```

获取任务目标进度
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `string` | - |

### `GetTaskTarget`

```text
GetTaskTarget(TaskID: number) -> number
```

获取任务目标进度
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `UpdateTaskProgress`

```text
UpdateTaskProgress(TaskIndex: FUGCTaskIndex, PlayerController: Controller, Progress: number, IsIncremental: boolean)
```

通用更新任务进度
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskIndex` | `FUGCTaskIndex` | - |
| `PlayerController` | `Controller` | - |
| `Progress` | `number` | - |
| `IsIncremental` | `boolean` | - |

### `GetPercentTaskPercent`

```text
GetPercentTaskPercent(TaskLineName: string, TaskID: number) -> number
```

获取活跃任务完成后获得的活跃度数量
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `TaskID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/TaskPlayerComponent.json -->

# TaskPlayerComponent

UGC任务系统玩家组件

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TaskPlayerComponent.OnTaskLineAwardInfoChangeDelegate` | `-` | 生效范围：客户端<br>任务线奖励状态变更回调<br>@param TaskLineName string @任务线名称<br>@param Index number @奖励索引 |
| `TaskPlayerComponent.OnTaskInfoChangeDelegate` | `-` | 生效范围：客户端<br>任务数据变更回调<br>@param Index UGCTaskIndex @榜单周期 |
| `TaskPlayerComponent.OnTaskLineProgressChangeDelegate` | `-` | 生效范围：客户端&服务端<br>任务线进度变更回调<br>@param TaskLineName string @任务线名称 |

## Functions

### `ResetPercentTaskLine`

```text
ResetPercentTaskLine(TaskLineName: string)
```

重置活跃任务线
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |

### `ClaimLevelTaskAward`

```text
ClaimLevelTaskAward(TaskLineName: string, LevelIndex: number, TaskIndex: number)
```

领取成长任务奖励
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `LevelIndex` | `number` | - |
| `TaskIndex` | `number` | - |

### `ClaimPercentTaskAward`

```text
ClaimPercentTaskAward(TaskLineName: string, TaskIndex: number)
```

领取活跃任务奖励
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `TaskIndex` | `number` | - |

### `GetTaskLineProgress`

```text
GetTaskLineProgress(TaskLineName: string) -> number
```

获取任务线进度
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetLevelTaskInfoList`

```text
GetLevelTaskInfoList(TaskLineName: string) -> FUGCLevelTaskPlayerData[]
```

获取成长任务线的任务信息列表
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |

**Returns**

| Type | Description |
|---|---|
| `FUGCLevelTaskPlayerData[]` | - |

### `GetPercentTaskInfoList`

```text
GetPercentTaskInfoList(TaskLineName: string) -> FUGCTaskInfo[]
```

获取活跃任务线的任务信息列表
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |

**Returns**

| Type | Description |
|---|---|
| `FUGCTaskInfo[]` | - |

### `GetPercentTaskLineAwardStateList`

```text
GetPercentTaskLineAwardStateList(TaskLineName: string) -> table
```

获取活跃任务线的奖励状态列表
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `GetTaskLineAwardState`

```text
GetTaskLineAwardState(TaskLineName: string, Index: number) -> EUGCTaskLineAwardState
```

获取任务线奖励状态
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `Index` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `EUGCTaskLineAwardState` | - |

### `ClaimAllAward`

```text
ClaimAllAward(TaskLineName: string)
```

领取任务线的全部奖励
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |

### `ClaimTaskLineAward`

```text
ClaimTaskLineAward(TaskLineName: string, Index: number)
```

领取任务线奖励
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `Index` | `number` | - |

### `SetTaskLineProgress`

```text
SetTaskLineProgress(TaskLineName: string, Progress: number)
```

设置任务线进度
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `Progress` | `number` | - |

### `GetPercentTaskProgress`

```text
GetPercentTaskProgress(TaskLineName: string, Index: number) -> number
```

获取活跃任务进度
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `Index` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetPercentTaskState`

```text
GetPercentTaskState(TaskLineName: string, Index: number) -> EUGCTaskState
```

获取活跃任务状态
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `Index` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `EUGCTaskState` | - |

### `GetLevelTaskProgress`

```text
GetLevelTaskProgress(TaskLineName: string, LevelIndex: number, TaskIndex: number) -> number
```

获取成长任务进度
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `LevelIndex` | `number` | - |
| `TaskIndex` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetLevelTaskState`

```text
GetLevelTaskState(TaskLineName: string, LevelIndex: number, TaskIndex: number) -> EUGCTaskState
```

获取成长任务状态
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `LevelIndex` | `number` | - |
| `TaskIndex` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `EUGCTaskState` | - |

### `GetTaskManager`

```text
GetTaskManager() -> TaskManager
```

**Returns**

| Type | Description |
|---|---|
| `TaskManager` | - |

### `SetTaskLineTime`

```text
SetTaskLineTime(TaskLineName: string, BeginTime: number, EndTime: number)
```

设置任务线和任务线下所有任务的开始/结束时间
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskLineName` | `string` | - |
| `BeginTime` | `number` | - |
| `EndTime` | `number` | - |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UActivityFakePossessComponent.json -->

# UActivityFakePossessComponent

能够将这个Actor的控制权传递给玩家的组件

## Inheritance

`UActorComponent` -> `IFakePossessInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OnPossess` | `FFakePossesserChangeDelegate` | 获取控制权事件事件委托<br>	 @param PC 获取到这个Actor控制权的PC |
| `OnUnPossess` | `FFakePossesserChangeDelegate` | 解除控制权事件委托<br>	 @param PC 解除这个Actor控制权的PC |
| `OnUnPossessWithReason` | `FFakeUnPossessDelegate` | 解除控制权事件委托<br>	 @param PC 解除这个Actor控制权的PC<br>	 @param Reason 解除控制权的原因 |

## Functions

### `FakePossess`

```text
FakePossess(PC: AController *) -> bool
```

生效范围：S
	  让一个PlayerController控制这个Actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PC` | `AController *` | 获得控制权的PlayerController |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `FakeUnPossess`

```text
FakeUnPossess(Reason: EUnPossessReason) -> void
```

生效范围：S
	  解除这个Actor上的PC的控制权

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reason` | `EUnPossessReason` | 解除控制权的原因 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FakePossessWithAttach`

```text
FakePossessWithAttach(PC: AController *, AttachScene: USceneComponent *, SocketName: FName, bMulticastToClient: bool) -> bool
```

生效范围：S
	  让一个PlayerController控制这个Actor，并将当前控制的角色Attach到这个Actor上

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PC` | `AController *` | 获得控制权的PlayerController |
| `AttachScene` | `USceneComponent *` | Attach到的组件 |
| `SocketName` | `FName` | Attach到的Socket |
| `bMulticastToClient` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `FakeUnPossessWithDettach`

```text
FakeUnPossessWithDettach(Reason: EUnPossessReason) -> void
```

生效范围：S
	  解除这个Actor上的PC的控制权，并将角色从这个Actor上Detach

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reason` | `EUnPossessReason` | 解除控制权的原因 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanBePossess`

```text
CanBePossess(Character: ASTExtraBaseCharacter *) -> bool
```

生效范围：S
	  获取是否可以由这个Character控制当前Actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `ASTExtraBaseCharacter *` | 要检查的Character |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UActorChannel.json -->

# UActorChannel

A channel for exchanging actor and its subobject's properties and RPCs. ActorChannel manages the creation and lifetime of a replicated actor. Actual replication of properties and RPCs actually happens in FObjectReplicator now (see DataReplication.h). An ActorChannel bunch looks like this: |----------------------|---------------------------------------------------------------------------| | SpawnInfo | (Spawn Info) Initial bunch only | | -Actor Class | -Created by ActorChannel | | -Spawn LocRot | | | NetGUID assigns | | | -Actor NetGUID | | | -Component NetGUIDs | | |----------------------|---------------------------------------------------------------------------| | | | |----------------------|---------------------------------------------------------------------------| | NetGUID ObjRef | (Content chunks) x number of replicating objects (Actor + any components) | | | -Each chunk created by its own FObjectReplicator instance. | |----------------------|---------------------------------------------------------------------------| | | | | Properties... | | | | | | RPCs... | | | | | |----------------------|---------------------------------------------------------------------------| |  | | |----------------------|---------------------------------------------------------------------------|

## Inheritance

`UChannel`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Actor` | `AActor *` | - |
| `ActorName` | `FName` | - |
| `ActorStaticTag` | `uint64` | - |
| `bPausedUntilSubObjectReliableACK` | `bool` | - |
| `ServerScondsSinceWhenPauseReplicateForSubObjectAddOrRemove` | `float` | - |
| `ServerScondsFirstReplicateSinceWhenPauseReplicateForSubObjectAddOrRemove` | `float` | - |
| `LastWarningTimeForPauseTooLong_SinceWhenPauseReplicateForSubObjectAddOrRemove` | `float` | - |

## Language

`cpp`

