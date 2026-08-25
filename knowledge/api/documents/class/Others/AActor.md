---
id: "api:class:AActor"
title: "AActor"
source: "https://developer.gp.qq.com/api/class/detail/Others/AActor.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
