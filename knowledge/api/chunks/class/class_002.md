---
id: "api-chunk:class:2"
title: "Oasis API class chunk 2"
source: "https://developer.gp.qq.com/api/"
category: "API Wiki/class"
kind: "api_chunk"
---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UActorComponent.json -->

# UActorComponent

ActorComponent is the base class for components that define reusable behavior that can be added to different types of Actors.
  ActorComponents that have a transform are known as SceneComponents and those that can be rendered are PrimitiveComponents.
 
  @see USceneComponent
  @see UPrimitiveComponent

## Inheritance

`UObject` -> `IInterface_AssetUserData`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PrimaryComponentTick` | `FActorComponentTickFunction` | Main tick function for the Actor |
| `DSTickInterval` | `float` | The frequency in seconds at which this tick function will be executed on DS.  If less than or equal to 0 then it will tick every frame<br>	 If greater than 0 will cover PrimaryComponentTick.TickInterval<br>	 Add by zoranouyang |
| `ComponentTags` | `TArray < FName >` | Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting. |
| `NetUpdateFrequency` | `float` | - |
| `bAllowBPReceiveTickEvent` | `bool` | If true, bp tick will be called , otherwise skipped |
| `TickAdapterIntvlOverride` | `uint8` | - |
| `bSyncOwnerTickAdapter` | `uint8` | - |
| `bEnableTickAdapter` | `uint8` | - |
| `ScriptNetworkReplicatedPropertyWrapper` | `FScriptNetworkReplicatedPropertyWrapper` | - |
| `bSupportSuspendTick` | `uint8` | - |
| `bDestroyIfOnClientNoLocalControl` | `uint8` | - |
| `bReplicates` | `uint8` | Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first! |
| `bNetAddressable` | `uint8` | Is this component safe to ID over the network by name? |
| `bDeferedConstructComponent` | `uint8` | - |
| `bSkipNewDuplicateComponent` | `uint8` | - |
| `bNameStableForBackupRestore` | `uint8` | - |
| `bNeedBackupRestoreForCustomSerialize` | `uint8` | - |
| `bEnableTickWhenOutOfRegion` | `uint8` | If true, this component will Enale Tick when out of region. |
| `bAutoActivate` | `uint8` | Whether the component is activated at creation or must be explicitly activated. |
| `bIsActive` | `uint8` | Whether the component is currently active. |
| `bEditableWhenInherited` | `uint8` | - |
| `bCanEverAffectNavigation` | `uint8` | Whether this component can potentially influence navigation |
| `bIsEditorOnly` | `uint8` | If true, the component will be excluded from non-editor builds |
| `bNeedsLoadForClient` | `uint8` | If false, the component will be excluded from client builds |
| `bNeedsLoadForServer` | `uint8` | If false, the component will be excluded from server builds |
| `bAllowRenderDataUpdateLag` | `uint8` | - |
| `CreationMethod` | `EComponentCreationMethod` | - |
| `UCSModifiedProperties` | `TArray < FSimpleMemberReference >` | - |
| `AssetUserData` | `TArray < UAssetUserData * >` | Array of user data stored with the component |
| `bCreatedByConstructionScript_DEPRECATED` | `uint8` | True if this component was created by a construction script, and will be destroyed by DestroyConstructedComponents |
| `bInstanceComponent_DEPRECATED` | `uint8` | True if this component was created as an instance component |

## Functions

### `GetToString`

```text
GetToString() -> FString
```

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `ForceNetUpdate`

```text
ForceNetUpdate() -> void
```

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

### `IsBeingDestroyed`

```text
IsBeingDestroyed() -> bool
```

Returns whether the component is in the process of being destroyed.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `OnRep_Replicates`

```text
OnRep_Replicates() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_IsActive`

```text
OnRep_IsActive() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOwner`

```text
GetOwner() -> AActor *
```

Follow the Outer chain to get the  AActor  that 'Owns' this component

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `ComponentHasTag`

```text
ComponentHasTag(Tag: FName) -> bool
```

See if this component contains the supplied tag

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Tag` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Activate`

```text
Activate(bReset: bool) -> void
```

Activates the SceneComponent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bReset` | `bool` | - The value to assign to HiddenGame. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Deactivate`

```text
Deactivate() -> void
```

Deactivates the SceneComponent.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetActive`

```text
SetActive(bNewActive: bool, bReset: bool) -> void
```

Sets whether the component is active or not

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewActive` | `bool` | - The new active state of the component |
| `bReset` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ToggleActive`

```text
ToggleActive() -> void
```

Toggles the active state of the component

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsActive`

```text
IsActive() -> bool
```

Returns whether the component is active or not

**Returns**

| Type | Description |
|---|---|
| `bool` | - The active state of the component. |

### `SetAutoActivate`

```text
SetAutoActivate(bNewAutoActivate: bool) -> void
```

Sets whether the component should be auto activate or not. Only safe during construction scripts.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewAutoActivate` | `bool` | - The new auto activate state of the component |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTickableWhenPaused`

```text
SetTickableWhenPaused(bTickableWhenPaused: bool) -> void
```

Sets whether this component can tick when paused.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bTickableWhenPaused` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIsReplicated`

```text
SetIsReplicated(ShouldReplicate: bool) -> void
```

Enable or disable replication. This is the equivalent of RemoteRole for actors (only a bool is required for components)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ShouldReplicate` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveBeginPlay`

```text
ReceiveBeginPlay() -> void
```

Blueprint implementable event for when the component is beginning play, called before its Owner's BeginPlay on Actor BeginPlay
	  or when the component is dynamically created if the Actor has already BegunPlay.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveEndPlay`

```text
ReceiveEndPlay(EndPlayReason: EEndPlayReason :: Type) -> void
```

Blueprint implementable event for when the component ends play, generally via destruction or its Actor's EndPlay.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EndPlayReason` | `EEndPlayReason :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetComponentTickEnabled`

```text
SetComponentTickEnabled(bEnabled: bool) -> void
```

Set this component's tick functions to be enabled or disabled. Only has an effect if the function is registered

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnabled` | `bool` | - Whether it should be enabled or not |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsComponentTickEnabled`

```text
IsComponentTickEnabled() -> bool
```

Returns whether this component has tick enabled or not

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsComponentTickEnabledByExternal`

```text
IsComponentTickEnabledByExternal() -> bool
```

Returns whether this component has tick enabled or not,
	  Which set by External business

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetComponentTickInterval`

```text
SetComponentTickInterval(TickInterval: float) -> void
```

Sets the tick interval for this component's primary tick function. Does not enable the tick interval. Takes effect on next tick.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TickInterval` | `float` | The duration between ticks for this component's primary tick function |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetComponentTickInterval`

```text
GetComponentTickInterval() -> float
```

Returns whether this component has tick enabled or not

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `K2_DestroyComponent`

```text
K2_DestroyComponent(Object: UObject *) -> void
```

Unregister and mark for pending kill a component.  This may not be used to destroy a component that is owned by an actor unless the owning actor is calling the function.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTickGroup`

```text
SetTickGroup(NewTickGroup: ETickingGroup) -> void
```

Changes the ticking group for this component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTickGroup` | `ETickingGroup` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddTickPrerequisiteActor`

```text
AddTickPrerequisiteActor(PrerequisiteActor: AActor *) -> void
```

Make this component tick after PrerequisiteActor

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

Make this component tick after PrerequisiteComponent.

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

## Delegates

### `OnComponentActivated`

```text
OnComponentActivated(Component: UActorComponent*, bReset: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UActorComponent*` | - |
| `bReset` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnComponentDeactivated`

```text
OnComponentDeactivated(Component: UActorComponent*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UActorComponent*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAggregatedCollisionComponent.json -->

# UAggregatedCollisionComponent

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AggregatedCollisions` | `TArray < FAggregatedCollision >` | - |
| `SavedBodySetups` | `TArray < UBodySetup * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAIAsyncTaskBlueprintProxy.json -->

# UAIAsyncTaskBlueprintProxy

## Inheritance

`UObject`

## Functions

### `OnMoveCompleted`

```text
OnMoveCompleted(RequestID: FAIRequestID, MovementResult: EPathFollowingResult :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RequestID` | `FAIRequestID` | - |
| `MovementResult` | `EPathFollowingResult :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnSuccess`

```text
OnSuccess(MovementResult: EPathFollowingResult::Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MovementResult` | `EPathFollowingResult::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnFail`

```text
OnFail(MovementResult: EPathFollowingResult::Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MovementResult` | `EPathFollowingResult::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAIBlueprintHelperLibrary.json -->

# UAIBlueprintHelperLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `CreateMoveToProxyObject`

```text
CreateMoveToProxyObject(WorldContextObject: UObject *, Pawn: APawn *, Destination: FVector, TargetActor: AActor *, AcceptanceRadius: float, bStopOnOverlap: bool) -> UAIAsyncTaskBlueprintProxy *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Pawn` | `APawn *` | - |
| `Destination` | `FVector` | - |
| `TargetActor` | `AActor *` | - |
| `AcceptanceRadius` | `float` | - |
| `bStopOnOverlap` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `UAIAsyncTaskBlueprintProxy *` | - |

### `SendAIMessage`

```text
SendAIMessage(Target: APawn *, Message: FName, MessageSource: UObject *, bSuccess: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `APawn *` | - |
| `Message` | `FName` | - |
| `MessageSource` | `UObject *` | - |
| `bSuccess` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SpawnAIFromClass`

```text
SpawnAIFromClass(WorldContextObject: UObject *, PawnClass: TSubclassOf < APawn >, BehaviorTree: UBehaviorTree *, Location: FVector, Rotation: FRotator, bNoCollisionFail: bool) -> APawn *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PawnClass` | `TSubclassOf < APawn >` | - |
| `BehaviorTree` | `UBehaviorTree *` | - |
| `Location` | `FVector` | - |
| `Rotation` | `FRotator` | - |
| `bNoCollisionFail` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `APawn *` | - |

### `GetAIController`

```text
GetAIController(ControlledActor: AActor *) -> AAIController *
```

The way it works exactly is if the actor passed in is a pawn, then the function retrieves 
	 	pawn's controller cast to AIController. Otherwise the function returns actor cast to AIController.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ControlledActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `AAIController *` | - |

### `GetBlackboard`

```text
GetBlackboard(Target: AActor *) -> UBlackboardComponent *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `UBlackboardComponent *` | - |

### `LockAIResourcesWithAnimation`

```text
LockAIResourcesWithAnimation(AnimInstance: UAnimInstance *, bLockMovement: bool, LockAILogic: bool) -> void
```

locks indicated AI resources of animated pawn

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AnimInstance` | `UAnimInstance *` | - |
| `bLockMovement` | `bool` | - |
| `LockAILogic` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnlockAIResourcesWithAnimation`

```text
UnlockAIResourcesWithAnimation(AnimInstance: UAnimInstance *, bUnlockMovement: bool, UnlockAILogic: bool) -> void
```

unlocks indicated AI resources of animated pawn. Will unlock only animation-locked resources

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AnimInstance` | `UAnimInstance *` | - |
| `bUnlockMovement` | `bool` | - |
| `UnlockAILogic` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsValidAILocation`

```text
IsValidAILocation(Location: FVector) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Location` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsValidAIDirection`

```text
IsValidAIDirection(DirectionVector: FVector) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DirectionVector` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsValidAIRotation`

```text
IsValidAIRotation(Rotation: FRotator) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rotation` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetCurrentPath`

```text
GetCurrentPath(Controller: AController *) -> UNavigationPath *
```

Returns a copy of navigation path given controller is currently using. 
	 	The result being a copy means you won't be able to influence agent's pathfollowing 
	 	by manipulating received path

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Controller` | `AController *` | - |

**Returns**

| Type | Description |
|---|---|
| `UNavigationPath *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAIDataProvider_QueryParams.json -->

# UAIDataProvider_QueryParams

AIDataProvider_QueryParams is used with environment queries
 
  It allows defining simple parameters for running query,
  which are not tied to any specific pawn, but defined
  for every query execution.

## Inheritance

`UAIDataProvider`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParamName` | `FName` | Arbitrary name this query parameter will be exposed as to outside world (like BT nodes) |
| `FloatValue` | `float` | - |
| `IntValue` | `int32` | - |
| `BoolValue` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAIDataProvider_Random.json -->

# UAIDataProvider_Random

## Inheritance

`UAIDataProvider_QueryParams`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Min` | `float` | - |
| `Max` | `float` | - |
| `bInteger` | `uint8` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAIPerceptionComponent.json -->

# UAIPerceptionComponent

AIPerceptionComponent is used to register as stimuli listener in AIPerceptionSystem
 	and gathers registered stimuli. UpdatePerception is called when component gets new stimuli (batched)

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SensesConfig` | `TArray < UAISenseConfig * >` | - |
| `DominantSense` | `TSubclassOf < UAISense >` | Indicated sense that takes precedence over other senses when determining sensed actor's location. <br>	 	Should be set to one of the senses configured in SensesConfig, or None. |
| `AIOwner` | `AAIController *` | - |

## Functions

### `OnOwnerEndPlay`

```text
OnOwnerEndPlay(Actor: AActor *, EndPlayReason: EEndPlayReason :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |
| `EndPlayReason` | `EEndPlayReason :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RequestStimuliListenerUpdate`

```text
RequestStimuliListenerUpdate() -> void
```

Notifies AIPerceptionSystem to update properties for this "stimuli listener"

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPerceivedHostileActors`

```text
GetPerceivedHostileActors(OutActors: TArray < AActor * > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutActors` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCurrentlyPerceivedActors`

```text
GetCurrentlyPerceivedActors(SenseToUse: TSubclassOf < UAISense >, OutActors: TArray < AActor * > &) -> void
```

If SenseToUse is none all actors currently perceived in any way will get fetched

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SenseToUse` | `TSubclassOf < UAISense >` | - |
| `OutActors` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetKnownPerceivedActors`

```text
GetKnownPerceivedActors(SenseToUse: TSubclassOf < UAISense >, OutActors: TArray < AActor * > &) -> void
```

If SenseToUse is none all actors ever perceived in any way (and not forgotten yet) will get fetched

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SenseToUse` | `TSubclassOf < UAISense >` | - |
| `OutActors` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPerceivedActors`

```text
GetPerceivedActors(SenseToUse: TSubclassOf < UAISense >, OutActors: TArray < AActor * > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SenseToUse` | `TSubclassOf < UAISense >` | - |
| `OutActors` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetActorsPerception`

```text
GetActorsPerception(Actor: AActor *, Info: FActorPerceptionBlueprintInfo &) -> bool
```

Retrieves whatever has been sensed about given actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |
| `Info` | `FActorPerceptionBlueprintInfo &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetSenseEnabled`

```text
SetSenseEnabled(SenseClass: TSubclassOf < UAISense >, bEnable: bool) -> void
```

Note that this works only if given sense has been already configured for
	 	this component instance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SenseClass` | `TSubclassOf < UAISense >` | - |
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnPerceptionUpdated`

```text
OnPerceptionUpdated(UpdatedActors: TArray<AActor*>) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UpdatedActors` | `TArray` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTargetPerceptionUpdated`

```text
OnTargetPerceptionUpdated(Actor: AActor*, Stimulus: FAIStimulus) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor*` | - |
| `Stimulus` | `FAIStimulus` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAIPerceptionStimuliSourceComponent.json -->

# UAIPerceptionStimuliSourceComponent

Gives owning actor a way to auto-register as perception system's sense stimuli source

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bAutoRegisterAsSource` | `uint32` | - |
| `RegisterAsSourceForSenses` | `TArray < TSubclassOf < UAISense > >` | - |

## Functions

### `RegisterWithPerceptionSystem`

```text
RegisterWithPerceptionSystem() -> void
```

Registers owning actor as source of stimuli for senses specified in RegisterAsSourceForSenses. 
	 	Note that you don't have to do it if bAutoRegisterAsSource == true

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RegisterForSense`

```text
RegisterForSense(SenseClass: TSubclassOf < UAISense >) -> void
```

Registers owning actor as source for specified sense class

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SenseClass` | `TSubclassOf < UAISense >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnregisterFromPerceptionSystem`

```text
UnregisterFromPerceptionSystem() -> void
```

Unregister owning actor from being a source of sense stimuli

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnregisterFromSense`

```text
UnregisterFromSense(SenseClass: TSubclassOf < UAISense >) -> void
```

Unregisters owning actor from sources list of a specified sense class

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SenseClass` | `TSubclassOf < UAISense >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAIPerceptionSystem.json -->

# UAIPerceptionSystem

By design checks perception between hostile teams

## Inheritance

`UObject` -> `FTickableGameObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Senses` | `TArray < UAISense * >` | - |
| `PerceptionAgingRate` | `float` | - |

## Functions

### `ReportEvent`

```text
ReportEvent(PerceptionEvent: UAISenseEvent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PerceptionEvent` | `UAISenseEvent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReportPerceptionEvent`

```text
ReportPerceptionEvent(WorldContextObject: UObject *, PerceptionEvent: UAISenseEvent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PerceptionEvent` | `UAISenseEvent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RegisterPerceptionStimuliSource`

```text
RegisterPerceptionStimuliSource(WorldContextObject: UObject *, Sense: TSubclassOf < UAISense >, Target: AActor *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Sense` | `TSubclassOf < UAISense >` | - |
| `Target` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetSenseClassForStimulus`

```text
GetSenseClassForStimulus(WorldContextObject: UObject *, Stimulus: FAIStimulus &) -> TSubclassOf < UAISense >
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Stimulus` | `FAIStimulus &` | - |

**Returns**

| Type | Description |
|---|---|
| `TSubclassOf < UAISense >` | - |

### `OnPerceptionStimuliSourceEndPlay`

```text
OnPerceptionStimuliSourceEndPlay(Actor: AActor *, EndPlayReason: EEndPlayReason :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |
| `EndPlayReason` | `EEndPlayReason :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAISense.json -->

# UAISense

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultExpirationAge` | `float` | age past which stimulus of this sense are "forgotten" |
| `NotifyType` | `EAISenseNotifyType` | - |
| `bWantsNewPawnNotification` | `uint32` | whether this sense is interested in getting notified about new Pawns being spawned <br>	 	this can be used for example for automated sense sources registration |
| `bAutoRegisterAllPawnsAsSources` | `uint32` | If true all newly spawned pawns will get auto registered as source for this sense. |
| `PerceptionSystemInstance` | `UAIPerceptionSystem *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAISense_Blueprint.json -->

# UAISense_Blueprint

## Inheritance

`UAISense`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ListenerDataType` | `TSubclassOf < UUserDefinedStruct >` | - |
| `ListenerContainer` | `TArray < UAIPerceptionComponent * >` | - |
| `UnprocessedEvents` | `TArray < UAISenseEvent * >` | - |

## Functions

### `OnUpdate`

```text
OnUpdate(EventsToProcess: TArray < UAISenseEvent * > &) -> float
```

returns requested amount of time to pass until next frame. 
	 	Return 0 to get update every frame (WARNING: hits performance)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EventsToProcess` | `TArray < UAISenseEvent * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `OnListenerRegistered`

```text
OnListenerRegistered(ActorListener: AActor *, PerceptionComponent: UAIPerceptionComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActorListener` | `AActor *` | - |
| `PerceptionComponent` | `UAIPerceptionComponent *` | is ActorListener's AIPerceptionComponent instance |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnListenerUpdated`

```text
OnListenerUpdated(ActorListener: AActor *, PerceptionComponent: UAIPerceptionComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActorListener` | `AActor *` | - |
| `PerceptionComponent` | `UAIPerceptionComponent *` | is ActorListener's AIPerceptionComponent instance |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnListenerUnregistered`

```text
OnListenerUnregistered(ActorListener: AActor *, PerceptionComponent: UAIPerceptionComponent *) -> void
```

called when a listener unregistered from this sense. Most often this is called due to actor's death

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActorListener` | `AActor *` | - |
| `PerceptionComponent` | `UAIPerceptionComponent *` | is ActorListener's AIPerceptionComponent instance |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAllListenerActors`

```text
GetAllListenerActors(ListenerActors: TArray < AActor * > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ListenerActors` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAllListenerComponents`

```text
GetAllListenerComponents(ListenerComponents: TArray < UAIPerceptionComponent * > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ListenerComponents` | `TArray < UAIPerceptionComponent * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_OnNewPawn`

```text
K2_OnNewPawn(NewPawn: APawn *) -> void
```

called when sense's instance gets notified about new pawn that has just been spawned

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAISense_Damage.json -->

# UAISense_Damage

## Inheritance

`UAISense`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RegisteredEvents` | `TArray < FAIDamageEvent >` | - |

## Functions

### `ReportDamageEvent`

```text
ReportDamageEvent(WorldContextObject: UObject *, DamagedActor: AActor *, Instigator: AActor *, DamageAmount: float, EventLocation: FVector, HitLocation: FVector) -> void
```

EventLocation will be reported as Instigator's location at the moment of event happening

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `DamagedActor` | `AActor *` | - |
| `Instigator` | `AActor *` | - |
| `DamageAmount` | `float` | - |
| `EventLocation` | `FVector` | - |
| `HitLocation` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAISense_Hearing.json -->

# UAISense_Hearing

## Inheritance

`UAISense`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NoiseEvents` | `TArray < FAINoiseEvent >` | - |
| `SpeedOfSoundSq` | `float` | Defaults to 0 to have instant notification. Setting to > 0 will result in delaying <br>	 	when AI hears the sound based on the distance from the source |

## Functions

### `ReportNoiseEvent`

```text
ReportNoiseEvent(WorldContextObject: UObject *, NoiseLocation: FVector, Loudness: float, Instigator: AActor *, MaxRange: float, Tag: FName) -> void
```

Report a noise event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `NoiseLocation` | `FVector` | Location of the noise. |
| `Loudness` | `float` | Loudness of the noise. If MaxRange is non-zero, modifies MaxRange, otherwise modifies the squared distance of the sensor's range. |
| `Instigator` | `AActor *` | Actor that triggered the noise. |
| `MaxRange` | `float` | Max range at which the sound can be heard, multiplied by Loudness. Values <= 0 mean no limit (still limited by listener's range however). |
| `Tag` | `FName` | Identifier for the event. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAISense_Prediction.json -->

# UAISense_Prediction

## Inheritance

`UAISense`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RegisteredEvents` | `TArray < FAIPredictionEvent >` | - |

## Functions

### `RequestControllerPredictionEvent`

```text
RequestControllerPredictionEvent(Requestor: AAIController *, PredictedActor: AActor *, PredictionTime: float) -> void
```

Asks perception system to supply Requestor with PredictedActor's predicted location in PredictionTime seconds
	 	Location is being predicted based on PredicterActor's current location and velocity

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Requestor` | `AAIController *` | - |
| `PredictedActor` | `AActor *` | - |
| `PredictionTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RequestPawnPredictionEvent`

```text
RequestPawnPredictionEvent(Requestor: APawn *, PredictedActor: AActor *, PredictionTime: float) -> void
```

Asks perception system to supply Requestor with PredictedActor's predicted location in PredictionTime seconds
	 	Location is being predicted based on PredicterActor's current location and velocity

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Requestor` | `APawn *` | - |
| `PredictedActor` | `AActor *` | - |
| `PredictionTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAISense_Sight.json -->

# UAISense_Sight

## Inheritance

`UAISense`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaxTracesPerTick` | `int32` | - |
| `MinQueriesPerTimeSliceCheck` | `int32` | - |
| `MaxTimeSlicePerTick` | `double` | - |
| `HighImportanceQueryDistanceThreshold` | `float` | - |
| `MaxQueryImportance` | `float` | - |
| `SightLimitQueryImportance` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAISense_Team.json -->

# UAISense_Team

## Inheritance

`UAISense`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RegisteredEvents` | `TArray < FAITeamStimulusEvent >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAISense_Touch.json -->

# UAISense_Touch

## Inheritance

`UAISense`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RegisteredEvents` | `TArray < FAITouchEvent >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAISenseConfig.json -->

# UAISenseConfig

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DebugColor` | `FColor` | - |
| `MaxAge` | `float` | specifies age limit after stimuli generated by this sense become forgotten. 0 means "never" |
| `bStartsEnabled` | `uint32` | determines whether given sense starts in an enabled state |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAISenseConfig_Blueprint.json -->

# UAISenseConfig_Blueprint

## Inheritance

`UAISenseConfig`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Implementation` | `TSubclassOf < UAISense_Blueprint >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAISenseConfig_Damage.json -->

# UAISenseConfig_Damage

## Inheritance

`UAISenseConfig`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Implementation` | `TSubclassOf < UAISense_Damage >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAISenseConfig_Hearing.json -->

# UAISenseConfig_Hearing

## Inheritance

`UAISenseConfig`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Implementation` | `TSubclassOf < UAISense_Hearing >` | - |
| `HearingRange` | `float` | - |
| `LoSHearingRange` | `float` | - |
| `bUseLoSHearing` | `uint32` | Warning: has significant runtime cost |
| `DetectionByAffiliation` | `FAISenseAffiliationFilter` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAISenseConfig_Sight.json -->

# UAISenseConfig_Sight

## Inheritance

`UAISenseConfig`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Implementation` | `TSubclassOf < UAISense_Sight >` | - |
| `SightRadius` | `float` | Maximum sight distance to notice a target. |
| `LoseSightRadius` | `float` | Maximum sight distance to see target that has been already seen. |
| `PeripheralVisionAngleDegrees` | `float` | How far to the side AI can see, in degrees. Use SetPeripheralVisionAngle to change the value at runtime. <br>	 	The value represents the angle measured in relation to the forward vector, not the whole range. |
| `DetectionByAffiliation` | `FAISenseAffiliationFilter` | - |
| `AutoSuccessRangeFromLastSeenLocation` | `float` | If not an InvalidRange (which is the default), we will always be able to see the target that has already been seen if they are within this range of their last seen location. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAISenseEvent_Damage.json -->

# UAISenseEvent_Damage

## Inheritance

`UAISenseEvent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Event` | `FAIDamageEvent` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAISenseEvent_Hearing.json -->

# UAISenseEvent_Hearing

## Inheritance

`UAISenseEvent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Event` | `FAINoiseEvent` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAISystem.json -->

# UAISystem

## Inheritance

`UAISystemBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PerceptionSystemClassName` | `FSoftClassPath` | - |
| `HotSpotManagerClassName` | `FSoftClassPath` | - |
| `NavLocalGridManagerClassName` | `FSoftClassPath` | Class that will be used to spawn the hot spot manager, can be game-specific |
| `AcceptanceRadius` | `float` | Default AI movement's acceptance radius used to determine whether <br> 	  AI reached path's end |
| `PathfollowingRegularPathPointAcceptanceRadius` | `float` | Value used for pathfollowing's internal code to determine whether AI reached path's point. <br>	 	@note this value is not used for path's last point. @see AcceptanceRadius |
| `PathfollowingNavLinkAcceptanceRadius` | `float` | Similarly to PathfollowingRegularPathPointAcceptanceRadius used by pathfollowing's internals<br>	 	but gets applied only when next point on a path represents a begining of navigation link |
| `bFinishMoveOnGoalOverlap` | `bool` | - |
| `bAcceptPartialPaths` | `bool` | - |
| `bAllowStrafing` | `bool` | - |
| `bEnableBTAITasks` | `bool` | this property is just a transition-time flag - in the end we're going to switch over to Gameplay Tasks anyway, that's the goal. |
| `bAllowControllersAsEQSQuerier` | `bool` | if enable will make EQS not complaint about using Controllers as queriers. Default behavior (false) will <br>	 	in places automatically convert controllers to pawns, and complain if code user bypasses the conversion or uses<br>	 	pawn-less controller |
| `bEnableDebuggerPlugin` | `bool` | if set, GameplayDebuggerPlugin will be loaded on module's startup |
| `DefaultSightCollisionChannel` | `TEnumAsByte < ECollisionChannel >` | - |
| `BehaviorTreeManager` | `UBehaviorTreeManager *` | Behavior tree manager used by game |
| `EnvironmentQueryManager` | `UEnvQueryManager *` | Environment query manager used by game |
| `PerceptionSystem` | `UAIPerceptionSystem *` | - |
| `AllProxyObjects` | `TArray < UAIAsyncTaskBlueprintProxy * >` | - |
| `HotSpotManager` | `UAIHotSpotManager *` | - |
| `NavLocalGrids` | `UNavLocalGridManager *` | - |

## Functions

### `AIIgnorePlayers`

```text
AIIgnorePlayers() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AILoggingVerbose`

```text
AILoggingVerbose() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAISystemBase.json -->

# UAISystemBase

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AISystemClassName` | `FSoftClassPath` | - |
| `AISystemModuleName` | `FName` | - |
| `bInstantiateAISystemOnClient` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAITask.json -->

# UAITask

## Inheritance

`UGameplayTask`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAITask_MoveTo.json -->

# UAITask_MoveTo

## Inheritance

`UAITask`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OnRequestFailed` | `FGenericGameplayTaskDelegate` | - |
| `MoveRequest` | `FAIMoveRequest` | parameters of move request |

## Functions

### `AIMoveTo`

```text
AIMoveTo(Controller: AAIController *, GoalLocation: FVector, GoalActor: AActor *, AcceptanceRadius: float, StopOnOverlap: EAIOptionFlag :: Type, AcceptPartialPath: EAIOptionFlag :: Type, bUsePathfinding: bool, bLockAILogic: bool, bUseContinuosGoalTracking: bool) -> UAITask_MoveTo *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Controller` | `AAIController *` | - |
| `GoalLocation` | `FVector` | - |
| `GoalActor` | `AActor *` | - |
| `AcceptanceRadius` | `float` | - |
| `StopOnOverlap` | `EAIOptionFlag :: Type` | - |
| `AcceptPartialPath` | `EAIOptionFlag :: Type` | - |
| `bUsePathfinding` | `bool` | - |
| `bLockAILogic` | `bool` | - |
| `bUseContinuosGoalTracking` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `UAITask_MoveTo *` | - |

## Delegates

### `OnMoveFinished`

```text
OnMoveFinished(Result: TEnumAsByte<EPathFollowingResult::Type>, AIController: AAIController*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Result` | `TEnumAsByte` | - |
| `AIController` | `AAIController*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAITask_RunEQS.json -->

# UAITask_RunEQS

## Inheritance

`UAITask`

## Functions

### `RunEQS`

```text
RunEQS(Controller: AAIController *, QueryTemplate: UEnvQuery *) -> UAITask_RunEQS *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Controller` | `AAIController *` | - |
| `QueryTemplate` | `UEnvQuery *` | - |

**Returns**

| Type | Description |
|---|---|
| `UAITask_RunEQS *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimationAsset.json -->

# UAnimationAsset

## Inheritance

`UObject` -> `IInterface_AssetUserData`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AnimAssetUID` | `int32` | - |
| `Skeleton` | `USkeleton *` | Pointer to the Skeleton this asset can be played on . |
| `MetaData` | `TArray < UAnimMetaData * >` | Meta data that can be saved with the asset <br>	  <br>	  You can query by GetMetaData function |
| `AssetUserData` | `TArray < UAssetUserData * >` | Array of user data stored with the asset |
| `bUseBoneRetarget` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimationSettings.json -->

# UAnimationSettings

Default animation settings.

## Inheritance

`UDeveloperSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CompressCommandletVersion` | `int32` | - |
| `KeyEndEffectorsMatchNameArray` | `TArray < FString >` | - |
| `DefaultCompressionAlgorithm` | `TSubclassOf < UAnimCompress >` | - |
| `RotationCompressionFormat` | `TEnumAsByte < AnimationCompressionFormat >` | - |
| `TranslationCompressionFormat` | `TEnumAsByte < AnimationCompressionFormat >` | - |
| `MaxCurveError` | `float` | Max error for compression of curves using remove redundant keys |
| `AlternativeCompressionThreshold` | `float` | The alternate error threshold (0.0 means don't try anything other than the current  default scheme) <br>	 <br>	 Determines the current setting for world-space error tolerance in the animation compressor.<br>	 When requested, animation being compressed will also consider an alternative compression<br>	 method if the end result of that method produces less error than the AlternativeCompressionThreshold.<br>	 Also known as "Max End Effector Error" |
| `ForceRecompression` | `bool` | - |
| `bOnlyCheckForMissingSkeletalMeshes` | `bool` | - |
| `bForceBelowThreshold` | `bool` | If true and the existing compression error is greater than Alternative Compression Threshold, then any compression technique (even one that increases the size) with a lower error will be used until it falls below the threshold |
| `bFirstRecompressUsingCurrentOrDefault` | `bool` | If true, then the animation will be first recompressed with it's current compressor if non-NULL, or with the global default compressor (specified in the engine ini) <br>	 Also known as "Run Current Default Compressor" |
| `bRaiseMaxErrorToExisting` | `bool` | If true and the existing compression error is greater than Alternative Compression Threshold, then Alternative Compression Threshold will be effectively raised to the existing error level |
| `bTryFixedBitwiseCompression` | `bool` | If true, the uniform bitwise techniques will be tried |
| `bTryPerTrackBitwiseCompression` | `bool` | If true, the per-track compressor techniques will be tried |
| `bTryLinearKeyRemovalCompression` | `bool` | If true, the linear key removal techniques will be tried |
| `bTryIntervalKeyRemoval` | `bool` | If true, the resampling techniques will be tried |
| `bEnablePerformanceLog` | `bool` | - |
| `bStripAnimationDataOnDedicatedServer` | `bool` | If true, animation track data will be stripped from dedicated server cooked data |
| `AnimUpdateRateDistanceFactorThesholdsBelow60FPS` | `TArray < float >` | - |
| `AnimUpdateRateDistanceFactorThesholdsIn60FPS` | `TArray < float >` | - |
| `AnimUpdateRateDistanceFactorThesholdsIn90FPS` | `TArray < float >` | - |
| `AnimUpdateRateDistanceFactorThesholdsIn120FPS` | `TArray < float >` | - |
| `AnimUpdateRateDistanceFactorThesholdsInPC` | `TArray < float >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimBlueprint.json -->

# UAnimBlueprint

An Anim Blueprint is essentially a specialized Blueprint whose graphs control the animation of a Skeletal Mesh.
  It can perform blending of animations, directly control the bones of the skeleton, and output a final pose
  for a Skeletal Mesh each frame.

## Inheritance

`UBlueprint`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetSkeleton` | `USkeleton *` | The kind of skeleton that animation graphs compiled from the blueprint will animate |
| `Groups` | `TArray < FAnimGroupInfo >` | - |
| `bUseMultiThreadedAnimationUpdate` | `bool` | Allows this anim Blueprint to update its native update, blend tree, montages and asset players on<br>	  a worker thread. The compiler will attempt to pick up any issues that may occur with threaded update.<br>	  For updates to run in multiple threads both this flag and the project setting "Allow Multi Threaded <br>	  Animation Update" should be set. |
| `bWarnAboutBlueprintUsage` | `bool` | Selecting this option will cause the compiler to emit warnings whenever a call into Blueprint<br>	  is made from the animation graph. This can help track down optimizations that need to be made. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimBlueprintGeneratedClass.json -->

# UAnimBlueprintGeneratedClass

## Inheritance

`UBlueprintGeneratedClass` -> `IAnimClassInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BakedStateMachines` | `TArray < FBakedAnimationStateMachine >` | - |
| `TargetSkeleton` | `USkeleton *` | Target skeleton for this blueprint class |
| `AnimNotifies` | `TArray < FAnimNotifyEvent >` | A list of anim notifies that state machines (or anything else) may reference |
| `RootAnimNodeIndex` | `int32` | - |
| `OrderedSavedPoseIndices` | `TArray < int32 >` | - |
| `SyncGroupNames` | `TArray < FName >` | - |
| `bFMPrecomputeDone` | `bool` | 预计算标记：编辑器编译蓝图时（PostCompile）扫描并写入，打包后序列化到.uasset，<br>	   运行时加载后直接读取正确值，无需再次扫描。<br>	   编辑器未编译时为false，懒初始化逻辑会在首次CollectFunctionModule时兜底扫描。 |
| `bHasAnyFunctionModule` | `bool` | 预计算缓存：该动画蓝图类（含父类继承链）是否含有任何FunctionModule属性。<br>	   仅在bFMPrecomputeDone为true时有效。打包后序列化到.uasset，运行时直接使用。 |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimClassData.json -->

# UAnimClassData

## Inheritance

`UObject` -> `IAnimClassInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BakedStateMachines` | `TArray < FBakedAnimationStateMachine >` | - |
| `TargetSkeleton` | `USkeleton *` | Target skeleton for this blueprint class |
| `AnimNotifies` | `TArray < FAnimNotifyEvent >` | A list of anim notifies that state machines (or anything else) may reference |
| `RootAnimNodeIndex` | `int32` | - |
| `OrderedSavedPoseIndices` | `TArray < int32 >` | - |
| `RootAnimNodeProperty` | `UStructProperty *` | - |
| `AnimNodeProperties` | `TArray < UStructProperty * >` | - |
| `SyncGroupNames` | `TArray < FName >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimComposite.json -->

# UAnimComposite

## Inheritance

`UAnimCompositeBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AnimationTrack` | `FAnimTrack` | Serializable data that stores sectionanim pairing |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimCompress.json -->

# UAnimCompress

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Description` | `FString` | Name of Compression Scheme used for this asset |
| `bNeedsSkeleton` | `uint32` | Compression algorithms requiring a skeleton should set this value to true. |
| `TranslationCompressionFormat` | `TEnumAsByte < AnimationCompressionFormat >` | Format for bitwise compression of translation data. |
| `RotationCompressionFormat` | `TEnumAsByte < AnimationCompressionFormat >` | Format for bitwise compression of rotation data. |
| `ScaleCompressionFormat` | `TEnumAsByte < AnimationCompressionFormat >` | Format for bitwise compression of scale data. |
| `MaxCurveError` | `float` | Max error for compression of curves using remove redundant keys |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimCompress_Automatic.json -->

# UAnimCompress_Automatic

## Inheritance

`UAnimCompress`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaxEndEffectorError` | `float` | Maximum amount of error that a compression technique can introduce in an end effector <br>	 Determines the current setting for world - space error tolerance in the animation compressor.<br>	 When requested, animation being compressed will also consider an alternative compression<br>	 method if the end result of that method produces less error than the AlternativeCompressionThreshold.<br>	 Also known as "Alternative Compression Threshold" |
| `bTryFixedBitwiseCompression` | `uint32` | If true, the uniform bitwise techniques will be tried |
| `bTryPerTrackBitwiseCompression` | `uint32` | If true, the per-track compressor techniques will be tried |
| `bTryLinearKeyRemovalCompression` | `uint32` | If true, the linear key removal techniques will be tried |
| `bTryIntervalKeyRemoval` | `uint32` | If true, the resampling techniques will be tried |
| `bRunCurrentDefaultCompressor` | `uint32` | If true, then the animation will be first recompressed with it's current compressor if non-NULL, or with the global default compressor (specified in the engine ini)<br>	 Also known as "First Recompress Using Current Or Default" |
| `bAutoReplaceIfExistingErrorTooGreat` | `uint32` | If true and the existing compression error is greater than Max End Effector Error, then any compression technique (even one that increases the size) with a lower error will be used until it falls below the threshold<br>	 Also known as "force below threshold" |
| `bRaiseMaxErrorToExisting` | `uint32` | If true and the existing compression error is greater than Max End Effector Error, then Max End Effector Error will be effectively raised to the existing error level |
| `bTryPerTrackVarBitCompression` | `uint32` | If true, the per-track variable bit compressor techniques will be tried |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimCompress_PerTrackCompression.json -->

# UAnimCompress_PerTrackCompression

## Inheritance

`UAnimCompress_RemoveLinearKeys`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaxZeroingThreshold` | `float` | Maximum threshold to use when replacing a component with zero. Lower values retain more keys, but yield less compression. |
| `MaxPosDiffBitwise` | `float` | Maximum position difference to use when testing if an animation key may be removed. Lower values retain more keys, but yield less compression. |
| `MaxAngleDiffBitwise` | `float` | Maximum angle difference to use when testing if an animation key may be removed. Lower values retain more keys, but yield less compression. |
| `MaxScaleDiffBitwise` | `float` | Maximum position difference to use when testing if an animation key may be removed. Lower values retain more keys, but yield less compression. |
| `AllowedRotationFormats` | `TArray < TEnumAsByte < enum AnimationCompressionFormat > >` | Which encoding formats is the per-track compressor allowed to try on rotation keys |
| `AllowedTranslationFormats` | `TArray < TEnumAsByte < enum AnimationCompressionFormat > >` | Which encoding formats is the per-track compressor allowed to try on translation keys |
| `bResampleAnimation` | `uint32` | If true, resample the animation to ResampleFramerate frames per second |
| `AllowedScaleFormats` | `TArray < TEnumAsByte < enum AnimationCompressionFormat > >` | Which encoding formats is the per-track compressor allowed to try on scale keys |
| `ResampledFramerate` | `float` | When bResampleAnimation is true, this defines the desired framerate |
| `MinKeysForResampling` | `int32` | Animations with fewer keys than MinKeysForResampling will not be resampled. |
| `bUseAdaptiveError` | `uint32` | If true, adjust the error thresholds based on the 'height' within the skeleton |
| `bUseOverrideForEndEffectors` | `uint32` | If true, uses MinEffectorDiff as the threhsold for end effectors |
| `TrackHeightBias` | `int32` | A bias added to the track height before using it to calculate the adaptive error |
| `ParentingDivisor` | `float` | Reduces the error tolerance the further up the tree that a key occurs<br>	  EffectiveErrorTolerance = Max(BaseErrorTolerance  Power(ParentingDivisor, Max(Height+Bias,0)  ParentingDivisorExponent), ZeroingThreshold)<br>	  Only has an effect bUseAdaptiveError is true |
| `ParentingDivisorExponent` | `float` | Reduces the error tolerance the further up the tree that a key occurs<br>	  EffectiveErrorTolerance = Max(BaseErrorTolerance  Power(ParentingDivisor, Max(Height+Bias,0)  ParentingDivisorExponent), ZeroingThreshold)<br>	  Only has an effect bUseAdaptiveError is true |
| `bUseAdaptiveError2` | `uint32` | If true, the adaptive error system will determine how much error to allow for each track, based on the<br>	  error introduced in end effectors due to errors in the track. |
| `RotationErrorSourceRatio` | `float` | This ratio determines how much error in end effector rotation can come from a given track's rotation error or translation error.<br>	  If 1, all of it must come from rotation error, if 0.5, half can come from each, and if 0.0, all must come from translation error. |
| `TranslationErrorSourceRatio` | `float` | This ratio determines how much error in end effector translation can come from a given track's rotation error or translation error.<br>	  If 1, all of it must come from rotation error, if 0.5, half can come from each, and if 0.0, all must come from translation error. |
| `ScaleErrorSourceRatio` | `float` | This ratio determines how much error in end effector scale can come from a given track's rotation error or scale error.<br>	  If 1, all of it must come from rotation error, if 0.5, half can come from each, and if 0.0, all must come from scale error. |
| `MaxErrorPerTrackRatio` | `float` | A fraction that determines how much of the total error budget can be introduced by any particular track |
| `PerturbationProbeSize` | `float` | How big of a perturbation should be made when probing error propagation |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimCompress_PerTrackVariableBit.json -->

# UAnimCompress_PerTrackVariableBit

## Inheritance

`UAnimCompress_PerTrackCompression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CompressedTranslationBitRate` | `TArray < uint32 >` | - |
| `CompressedRotationBitRate` | `TArray < uint32 >` | - |
| `CompressedScaleBitRate` | `TArray < uint32 >` | - |
| `isCompressed` | `bool` | - |
| `UncompressBoneName` | `TArray < FName >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimCompress_RemoveEverySecondKey.json -->

# UAnimCompress_RemoveEverySecondKey

## Inheritance

`UAnimCompress`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MinKeys` | `int32` | Animations with fewer than MinKeys will not lose any keys. |
| `bStartAtSecondKey` | `uint32` | If bStartAtSecondKey is true, remove keys 1,3,5,etc.<br>	  If bStartAtSecondKey is false, remove keys 0,2,4,etc. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimCompress_RemoveLinearKeys.json -->

# UAnimCompress_RemoveLinearKeys

## Inheritance

`UAnimCompress`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaxPosDiff` | `float` | Maximum position difference to use when testing if an animation key may be removed. Lower values retain more keys, but yield less compression. |
| `MaxAngleDiff` | `float` | Maximum angle difference to use when testing if an animation key may be removed. Lower values retain more keys, but yield less compression. |
| `MaxScaleDiff` | `float` | Maximum Scale difference to use when testing if an animation key may be removed. Lower values retain more keys, but yield less compression. |
| `MaxEffectorDiff` | `float` | As keys are tested for removal, we monitor the effects all the way down to the end effectors. <br>	  If their position changes by more than this amount as a result of removing a key, the key will be retained.<br>	  This value is used for all bones except the end-effectors parent. |
| `MinEffectorDiff` | `float` | As keys are tested for removal, we monitor the effects all the way down to the end effectors. <br>	  If their position changes by more than this amount as a result of removing a key, the key will be retained.<br>	  This value is used for the end-effectors parent, allowing tighter restrictions near the end of a skeletal chain. |
| `EffectorDiffSocket` | `float` | Error threshold for End Effectors with Sockets attached to them.<br>	  Typically more important bone, where we want to be less aggressive with compression. |
| `ParentKeyScale` | `float` | A scale value which increases the likelihood that a bone will retain a key if it's parent also had a key at the same time position. <br>	  Higher values can remove shaking artifacts from the animation, at the cost of compression. |
| `bRetarget` | `uint32` | true = As the animation is compressed, adjust animated nodes to compensate for compression error.<br>	  false= Do not adjust animated nodes. |
| `bActuallyFilterLinearKeys` | `uint32` | Controls whether the final filtering step will occur, or only the retargetting after bitwise compression.<br>	   If both this and bRetarget are false, then the linear compressor will do no better than the underlying bitwise compressor, extremely slowly. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimCompress_RemoveTrivialKeys.json -->

# UAnimCompress_RemoveTrivialKeys

## Inheritance

`UAnimCompress`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaxPosDiff` | `float` | - |
| `MaxAngleDiff` | `float` | - |
| `MaxScaleDiff` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimFuntionBoneModifyLibrary.json -->

# UAnimFuntionBoneModifyLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `Prototype_BoneModifyFuntion`

```text
Prototype_BoneModifyFuntion(Context: FBPAnimComponentSpacePoseContext &, AdditionalPoseBPContext: TArray < FBPAnimComponentSpacePoseContext > &, OutBoneModifyData: TArray < FFunctionBoneModifyData > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FBPAnimComponentSpacePoseContext &` | - |
| `AdditionalPoseBPContext` | `TArray < FBPAnimComponentSpacePoseContext > &` | - |
| `OutBoneModifyData` | `TArray < FFunctionBoneModifyData > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBoneTransformLocalSpace`

```text
GetBoneTransformLocalSpace(Context: FBPAnimComponentSpacePoseContext &, BoneName: FName) -> FTransform
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FBPAnimComponentSpacePoseContext &` | - |
| `BoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `GetBoneTransformComponentSpace`

```text
GetBoneTransformComponentSpace(Context: FBPAnimComponentSpacePoseContext &, BoneName: FName) -> FTransform
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FBPAnimComponentSpacePoseContext &` | - |
| `BoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimInstance.json -->

# UAnimInstance

## Inheritance

`UObject` -> `IObjectPoolInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CurrentSkeleton` | `USkeleton *` | This is used to extract animation. If Mesh exists, this will be overwritten by Mesh->Skeleton |
| `RootMotionMode` | `TEnumAsByte < ERootMotionMode :: Type >` | - |
| `bRunUpdatesInWorkerThreads_DEPRECATED` | `bool` | DEPRECATED: No longer used.<br>	  Allows this anim instance to update its native update, blend tree, montages and asset players on<br>	  a worker thread. this requires certain conditions to be met:<br>	  - All access of variables in the blend tree should be a direct access of a member variable<br>	  - No BlueprintUpdateAnimation event should be used (i.e. the event graph should be empty). Only native update is permitted. |
| `bCanUseParallelUpdateAnimation_DEPRECATED` | `bool` | DEPRECATED: No longer used.<br>	  Whether we can use parallel updates for our animations.<br>	  Conditions affecting this include:<br>	  - Use of BlueprintUpdateAnimation<br>	  - Use of non 'fast-path' EvaluateGraphExposedInputs in the node graph |
| `bUseMultiThreadedAnimationUpdate` | `bool` | Allows this anim instance to update its native update, blend tree, montages and asset players on<br>	  a worker thread. This flag is propagated from the UAnimBlueprint to this instance by the compiler.<br>	  The compiler will attempt to pick up any issues that may occur with threaded update.<br>	  For updates to run in multiple threads both this flag and the project setting "Allow Multi Threaded<br>	  Animation Update" should be set. |
| `bWarnAboutBlueprintUsage_DEPRECATED` | `bool` | Selecting this option will cause the compiler to emit warnings whenever a call into Blueprint<br>	  is made from the animation graph. This can help track down optimizations that need to be made. |
| `bBlueprintSkipUpdate` | `bool` | - |
| `bUseBlueprintUpdateAnimation` | `uint8` | - |
| `bUseBlueprintPostEvaluateAnimation` | `uint8` | - |
| `AnimAssets_NoGCRef` | `TMap < int64 , UAnimationAsset * >` | - |
| `bQueueMontageEvents` | `bool` | True when Montages are being ticked, and Montage Events should be queued.<br>	  When Montage are being ticked, we queue AnimNotifies and Events. We trigger notifies first, then Montage events. |
| `ForbiddenPlayMontageSlot` | `TArray < FString >` | - |
| `ActiveAnimNotifyState` | `TArray < FAnimNotifyEvent >` | Currently Active AnimNotifyState, stored as a copy of the event as we need to<br>		is removed correctly. |
| `bNeedUpdateNotAttributeCurve` | `bool` | 此动画蓝图是否需要更新非Attribute的Curve数据 |
| `RefCachedSubAnimInstances` | `TArray < UAnimInstance * >` | - |
| `bIsOnlyMasterTriggerNotify` | `bool` | - |
| `bIsMaster` | `bool` | - |
| `bDynamicDisableBoneRetarget` | `bool` | - |
| `CopyPoseFromSkelComp` | `USkeletalMeshComponent *` | - |
| `BoneRetargetSource` | `FName` | - |
| `bUseBoneStateDirtyFeature` | `bool` | - |
| `bBoneStateDirty` | `bool` | - |
| `C_InverseRetargetIgnoreBoneList` | `TArray < int32 >` | - |
| `C_IgnoreRetargetBoneList` | `TArray < FName >` | - |
| `FollowedAnimInstance` | `UAnimInstance *` | 记录被跟随者的动画实例   当该指针为nullptr时，代表启用了自身 Proxy 的 Follow 轨道(即FollowGroupArrays开始记录) |
| `FollowerAnimInstances` | `TArray < TWeakObjectPtr < UAnimInstance > >` | - |
| `ParentAnimInstance` | `TWeakObjectPtr < UAnimInstance >` | - |
| `SubAnimInstances` | `TArray < TWeakObjectPtr < UAnimInstance > >` | - |
| `SubAnimInstancesTempRef` | `TArray < UAnimInstance * >` | - |
| `CachedSwitchNotifySequence` | `TArray < UAnimSequenceBase * >` | - |
| `CachedBoneTransformInfoIndex` | `int64` | - |
| `CachedBoneTransformMapAsync` | `TMap < FName , FCachedBoneTransformInfo >` | - |
| `CachedBoneTransformMapInGame` | `TMap < FName , FCachedBoneTransformInfo >` | - |
| `bIsInPoseUpdate` | `bool` | - |
| `bEnableBoneCacheInGameThread` | `bool` | - |
| `bEnableFastPathExposedNodeTree` | `bool` | - |
| `UpdateConditions` | `TArray < UAnimInstanceUpdateCondition * >` | - |
| `bCheckUpdateConditionResult` | `bool` | - |
| `bEnableAnimBlueprintSkeletonDifferFromMeshSkeleton` | `bool` | - |
| `bEnableFilterForceTriggerNotifyWhenMontageJumpTick` | `bool` | - |
| `MultiSubInstanceTransferDefaultPoseIndex` | `int32` | - |
| `bEnableTriggerAnimNotify` | `bool` | - |
| `InitNodeSourcePropertyLookupTable` | `TMap < FName , UProperty * >` | - |
| `bParentPoseOverride` | `bool` | - |
| `bAutoCopyPose` | `bool` | - |
| `bHasAvatarSlotEvent` | `bool` | - |
| `bRestoreSlotVar` | `bool` | - |
| `bSkipSlotRelevanceCheckForNotifies` | `bool` | - |
| `bEnableAsyncAnimInstance` | `bool` | - |
| `bCanCopyRequiredBones` | `bool` | - |
| `RecordFileName` | `FString` | 回放的录制文件名 |
| `TotalFrames` | `int32` | 总帧数 |
| `CurrentFrame` | `int32` | 当前帧号 |
| `bIsPaused` | `bool` | 暂停 |
| `bRestoreErrorPending` | `bool` | 是否有待游戏线程处理的回放错误（由 ParallelRestoreAnimation 在工作线程设置） |
| `PostCompileValidationClassName` | `FSoftClassPath` | Name of Class to do Post Compile Validation.<br>	 See Class UAnimBlueprintPostCompileValidation. |
| `BoneRetargetBaseRefMesh` | `USkeletalMesh *` | - |

## Functions

### `TryGetPawnOwner`

```text
TryGetPawnOwner() -> APawn *
```

**Returns**

| Type | Description |
|---|---|
| `APawn *` | - |

### `SavePoseSnapshot`

```text
SavePoseSnapshot(SnapshotName: FName) -> void
```

Takes a snapshot of the current skeletal mesh component pose & saves it internally.
	  This snapshot can then be retrieved by name in the animation blueprint for blending.
	  The snapshot is taken at the current LOD, so if for example you took the snapshot at LOD1 and then used it at LOD0 any bones not in LOD1 will use the reference pose

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SnapshotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SnapshotPose`

```text
SnapshotPose(Snapshot: FPoseSnapshot &) -> void
```

Takes a snapshot of the current skeletal mesh component pose and saves it to the specified snapshot.
	  The snapshot is taken at the current LOD, so if for example you took the snapshot at LOD1
	  and then used it at LOD0 any bones not in LOD1 will use the reference pose

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Snapshot` | `FPoseSnapshot &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOwningActor`

```text
GetOwningActor() -> AActor *
```

Returns the owning actor of this AnimInstance

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `GetOwningComponent`

```text
GetOwningComponent() -> USkeletalMeshComponent *
```

**Returns**

| Type | Description |
|---|---|
| `USkeletalMeshComponent *` | - |

### `BlueprintShouldSkipUpdateAnimation`

```text
BlueprintShouldSkipUpdateAnimation(DeltaTimeX: float) -> bool
```

Executed before the Animation is updated, Check custom condition, whether to skip update

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTimeX` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `BlueprintInitializeAnimation`

```text
BlueprintInitializeAnimation() -> void
```

Executed when the Animation is initialized

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BlueprintUnInitializeAnimation`

```text
BlueprintUnInitializeAnimation() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BlueprintUpdateAnimation`

```text
BlueprintUpdateAnimation(DeltaTimeX: float) -> void
```

Executed when the Animation is updated

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTimeX` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BlueprintPostEvaluateAnimation`

```text
BlueprintPostEvaluateAnimation() -> void
```

Executed after the Animation is evaluated

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BlueprintBeginPlay`

```text
BlueprintBeginPlay() -> void
```

Executed when begin play is called on the owning component

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlaySlotAnimation`

```text
PlaySlotAnimation(Asset: UAnimSequenceBase *, SlotNodeName: FName, BlendInTime: float, BlendOutTime: float, InPlayRate: float, LoopCount: int32) -> float
```

SlotAnimation
	 
	 DEPRECATED. Use PlaySlotAnimationAsDynamicMontage instead, it returns the UAnimMontage created instead of time, allowing more control 
	 Play normal animation asset on the slot node. You can only play one asset (whether montage or animsequence) at a time.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Asset` | `UAnimSequenceBase *` | - |
| `SlotNodeName` | `FName` | - |
| `BlendInTime` | `float` | - |
| `BlendOutTime` | `float` | - |
| `InPlayRate` | `float` | - |
| `LoopCount` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `PlaySlotAnimationAsDynamicMontage`

```text
PlaySlotAnimationAsDynamicMontage(Asset: UAnimSequenceBase *, SlotNodeName: FName, BlendInTime: float, BlendOutTime: float, InPlayRate: float, LoopCount: int32, BlendOutTriggerTime: float, InTimeToStartMontageAt: float) -> UAnimMontage *
```

Play normal animation asset on the slot node by creating a dynamic UAnimMontage. You can only play one asset (whether montage or animsequence) at a time per SlotGroup.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Asset` | `UAnimSequenceBase *` | - |
| `SlotNodeName` | `FName` | - |
| `BlendInTime` | `float` | - |
| `BlendOutTime` | `float` | - |
| `InPlayRate` | `float` | - |
| `LoopCount` | `int32` | - |
| `BlendOutTriggerTime` | `float` | - |
| `InTimeToStartMontageAt` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `UAnimMontage *` | - |

### `PlaySlotAnimationAsDynamicMontageCustom`

```text
PlaySlotAnimationAsDynamicMontageCustom(Asset: UAnimSequenceBase *, SlotNodeName: FName, Extra: FCustomMontageAnimInfo, BlendInTime: float, BlendOutTime: float, InPlayRate: float, LoopCount: int32, BlendOutTriggerTime: float, InTimeToStartMontageAt: float) -> UAnimMontage *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Asset` | `UAnimSequenceBase *` | - |
| `SlotNodeName` | `FName` | - |
| `Extra` | `FCustomMontageAnimInfo` | - |
| `BlendInTime` | `float` | - |
| `BlendOutTime` | `float` | - |
| `InPlayRate` | `float` | - |
| `LoopCount` | `int32` | - |
| `BlendOutTriggerTime` | `float` | - |
| `InTimeToStartMontageAt` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `UAnimMontage *` | - |

### `SetMatineeAnimPosition`

```text
SetMatineeAnimPosition(TargetMontage: UAnimMontage *, InPosition: float, Extra: FCustomMontageAnimInfo, Weight: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetMontage` | `UAnimMontage *` | - |
| `InPosition` | `float` | - |
| `Extra` | `FCustomMontageAnimInfo` | - |
| `Weight` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopSlotAnimation`

```text
StopSlotAnimation(InBlendOutTime: float, SlotNodeName: FName) -> void
```

Stops currently playing slot animation slot or all

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlendOutTime` | `float` | - |
| `SlotNodeName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsPlayingSlotAnimation`

```text
IsPlayingSlotAnimation(Asset: UAnimSequenceBase *, SlotNodeName: FName, bcheckTransientPackage: bool) -> bool
```

Return true if it's playing the slot animation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Asset` | `UAnimSequenceBase *` | - |
| `SlotNodeName` | `FName` | - |
| `bcheckTransientPackage` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ForceTriggerAnimEndedEvent`

```text
ForceTriggerAnimEndedEvent() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMontageCustomSectionsPlayInfo`

```text
SetMontageCustomSectionsPlayInfo(Montage: UAnimMontage *, InPlayInfo: TArray < FMontageSectionsPlayInfo > &) -> void
```

AnimMontage

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |
| `InPlayInfo` | `TArray < FMontageSectionsPlayInfo > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMontageCustomSectionsPlayInfo`

```text
ClearMontageCustomSectionsPlayInfo(Montage: UAnimMontage *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_Play`

```text
Montage_Play(MontageToPlay: UAnimMontage *, InPlayRate: float, ReturnValueType: EMontagePlayReturnType, InTimeToStartMontageAt: float) -> float
```

Plays an animation montage. Returns the length of the animation montage in seconds. Returns 0.f if failed to play.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MontageToPlay` | `UAnimMontage *` | - |
| `InPlayRate` | `float` | - |
| `ReturnValueType` | `EMontagePlayReturnType` | - |
| `InTimeToStartMontageAt` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Montage_CustomPlay`

```text
Montage_CustomPlay(MontageToPlay: UAnimMontage *, Extra: FCustomMontageAnimInfo, InPlayRate: float, ReturnValueType: EMontagePlayReturnType, InTimeToStartMontageAt: float) -> float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MontageToPlay` | `UAnimMontage *` | - |
| `Extra` | `FCustomMontageAnimInfo` | - |
| `InPlayRate` | `float` | - |
| `ReturnValueType` | `EMontagePlayReturnType` | - |
| `InTimeToStartMontageAt` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Montage_Stop`

```text
Montage_Stop(InBlendOutTime: float, Montage: UAnimMontage *) -> void
```

Stops the animation montage. If reference is NULL, it will stop ALL active montages.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlendOutTime` | `float` | - |
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_StopBySlot`

```text
Montage_StopBySlot(InBlendOutTime: float, SlotName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlendOutTime` | `float` | - |
| `SlotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_CustomStop`

```text
Montage_CustomStop(InBlendOutTime: float, Extra: FCustomMontageAnimInfo, Montage: UAnimMontage *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlendOutTime` | `float` | - |
| `Extra` | `FCustomMontageAnimInfo` | - |
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_Pause`

```text
Montage_Pause(Montage: UAnimMontage *) -> void
```

Pauses the animation montage. If reference is NULL, it will pause ALL active montages.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_Resume`

```text
Montage_Resume(Montage: UAnimMontage *) -> void
```

Resumes a paused animation montage. If reference is NULL, it will resume ALL active montages.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_JumpToSection`

```text
Montage_JumpToSection(SectionName: FName, Montage: UAnimMontage *) -> void
```

Makes a montage jump to a named section. If Montage reference is NULL, it will do that to all active montages.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SectionName` | `FName` | - |
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_JumpToSectionsEnd`

```text
Montage_JumpToSectionsEnd(SectionName: FName, Montage: UAnimMontage *) -> void
```

Makes a montage jump to the end of a named section. If Montage reference is NULL, it will do that to all active montages.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SectionName` | `FName` | - |
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_SetNextSection`

```text
Montage_SetNextSection(SectionNameToChange: FName, NextSection: FName, Montage: UAnimMontage *) -> void
```

Relink new next section AFTER SectionNameToChange in run-time
	 	You can link section order the way you like in editor, but in run-time if you'd like to change it dynamically,
	 	use this function to relink the next section
	 	For example, you can have Start->Loop->Loop->Loop.... but when you want it to end, you can relink
	 	next section of Loop to be End to finish the montage, in which case, it stops looping by Loop->End.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SectionNameToChange` | `FName` | : This should be the name of the Montage Section after which you want to insert a new next section |
| `NextSection` | `FName` | : new next section |
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_SetPlayRate`

```text
Montage_SetPlayRate(Montage: UAnimMontage *, NewPlayRate: float) -> void
```

Change AnimMontage play rate. NewPlayRate = 1.0 is the default playback rate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |
| `NewPlayRate` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_ReversePlayByAbsRateAndSlot`

```text
Montage_ReversePlayByAbsRateAndSlot(SlotName: FName, AbsPlayRate: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotName` | `FName` | - |
| `AbsPlayRate` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_SetDelayFrame`

```text
Montage_SetDelayFrame(Montage: UAnimMontage *, DelayFrame: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |
| `DelayFrame` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_IsActive`

```text
Montage_IsActive(Montage: UAnimMontage *) -> bool
```

Returns true if the animation montage is active. If the Montage reference is NULL, it will return true if any Montage is active.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Montage_IsPlaying`

```text
Montage_IsPlaying(Montage: UAnimMontage *) -> bool
```

Returns true if the animation montage is currently active and playing.
	If reference is NULL, it will return true is ANY montage is currently active and playing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Montage_IsExisting`

```text
Montage_IsExisting(Montage: UAnimMontage *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `MontageGroup_IsPlaying`

```text
MontageGroup_IsPlaying(GroupName: FName) -> bool
```

判断有无某个组下的蒙太奇正在播放

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GroupName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Montage_GetCurrentSection`

```text
Montage_GetCurrentSection(Montage: UAnimMontage *) -> FName
```

Returns the name of the current animation montage section.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `Montage_GetPosition`

```text
Montage_GetPosition(Montage: UAnimMontage *) -> float
```

Get Current Montage Position

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Montage_SetPosition`

```text
Montage_SetPosition(Montage: UAnimMontage *, NewPosition: float) -> void
```

Set position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |
| `NewPosition` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Montage_GetIsStopped`

```text
Montage_GetIsStopped(Montage: UAnimMontage *) -> bool
```

return true if Montage is not currently active. (not valid or blending out)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Montage_GetBlendTime`

```text
Montage_GetBlendTime(Montage: UAnimMontage *) -> float
```

Get the current blend time of the Montage.
	If Montage reference is NULL, it will return the current blend time on the first active Montage found.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Montage_GetPlayRate`

```text
Montage_GetPlayRate(Montage: UAnimMontage *) -> float
```

Get PlayRate for Montage.
	If Montage is not playing, 0 is returned.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `IsAnyMontagePlaying`

```text
IsAnyMontagePlaying() -> bool
```

Returns true if any montage is playing currently. Doesn't mean it's active though, it could be blending out.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetCurrentActiveMontage`

```text
GetCurrentActiveMontage() -> UAnimMontage *
```

Get a current Active Montage in this AnimInstance.
		Note that there might be multiple Active at the same time. This will only return the first active one it finds.

**Returns**

| Type | Description |
|---|---|
| `UAnimMontage *` | - |

### `GetCurrentActiveMontages`

```text
GetCurrentActiveMontages() -> TArray < FAnimMontageInstance >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < FAnimMontageInstance >` | - |

### `GetCurMontageBySlot`

```text
GetCurMontageBySlot(SlotName: FName) -> UAnimMontage *
```

Get the UAnimMontage currently running that matches this SlotName.  Will return NULL if no instance is found.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UAnimMontage *` | - |

### `Montage_GetNextSection`

```text
Montage_GetNextSection(Montage: UAnimMontage *, SectionName: FName) -> FName
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |
| `SectionName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `AddAnimAssetNoGCRef`

```text
AddAnimAssetNoGCRef(InAnimAsset: UAnimationAsset *) -> int64
```

添加动画资源到非GC引用列表，返回全局唯一ID

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimAsset` | `UAnimationAsset *` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `RemoveAnimAssetNoGCRef`

```text
RemoveAnimAssetNoGCRef(InAnimAssetNoGCID: int64) -> void
```

从非GC引用列表移除动画资源（通过ID）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimAssetNoGCID` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveAllAnimAssetNoGCRef`

```text
RemoveAllAnimAssetNoGCRef(InAnimAsset: UAnimationAsset *) -> void
```

从非GC引用列表移除所有动画资源（通过资源指针）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimAsset` | `UAnimationAsset *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearAnimAssetsNoGCReferences`

```text
ClearAnimAssetsNoGCReferences() -> void
```

清空非GC引用列表

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopAllMontages`

```text
StopAllMontages(BlendOut: float) -> void
```

Stop all montages that are active

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BlendOut` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearAllMontages`

```text
ClearAllMontages(BlendOut: float) -> void
```

Stop all montages that are active

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BlendOut` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearStoppedMontageInstances`

```text
ClearStoppedMontageInstances(bClearSubAnim: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bClearSubAnim` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetForbiddenPlayMontageSlot`

```text
GetForbiddenPlayMontageSlot() -> TArray < FString >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < FString >` | - |

### `SetForbiddenPlayMontageSlot`

```text
SetForbiddenPlayMontageSlot(bIsAdd: bool, SlotName: FString) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsAdd` | `bool` | - |
| `SlotName` | `FString` | should be GroupName + SlotName |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRootMotionMode`

```text
SetRootMotionMode(Value: TEnumAsByte < ERootMotionMode :: Type >) -> void
```

Set RootMotionMode

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `TEnumAsByte < ERootMotionMode :: Type >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetInstanceAssetPlayerLength`

```text
GetInstanceAssetPlayerLength(AssetPlayerIndex: int32) -> float
```

NOTE: Derived anim getters
	 
	  Anim getter functions can be defined for any instance deriving UAnimInstance.
	  To do this the function must be marked BlueprintPure, and have the AnimGetter metadata entry set to
	  "true". Following the instructions below, getters should appear correctly in the blueprint node context
	  menu for the derived classes
	 
	  A context string can be provided in the GetterContext metadata and can contain any (or none) of the
	  following entries separated by a pipe (|)
	  Transition  - Only available in a transition rule
	  AnimGraph   - Only available in an animgraph (also covers state anim graphs)
	  CustomBlend - Only available in a custom blend graph
	 
	  Anim getters support a number of automatic parameters that will be baked at compile time to be passed
	  to the functions. They will not appear as pins on the graph node. They are as follows:
	  AssetPlayerIndex - Index of an asset player node to operate on, one getter will be added to the blueprint action list per asset node available
	  MachineIndex     - Index of a state machine in the animation blueprint, one getter will be added to the blueprint action list per state machine
	  StateIndex       - Index of a state inside a state machine, also requires MachineIndex. One getter will be added to the blueprint action list per state
	  TransitionIndex  - Index of a transition inside a state machine, also requires MachineIndex. One getter will be added to the blueprint action list per transition
	 
	  Gets the length in seconds of the asset referenced in an asset player node

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetPlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInstanceAssetPlayerTime`

```text
GetInstanceAssetPlayerTime(AssetPlayerIndex: int32) -> float
```

Get the current accumulated time in seconds for an asset player node

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetPlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetInstanceAssetPlayerTime`

```text
SetInstanceAssetPlayerTime(AssetPlayerIndex: int32, time: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetPlayerIndex` | `int32` | - |
| `time` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetNodeIndexWithTag`

```text
GetNodeIndexWithTag(NodeTag: FName) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeTag` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetInstanceAssetPlayerTime_BP`

```text
GetInstanceAssetPlayerTime_BP(AssetPlayerIndex: int32) -> float
```

Get the current accumulated time in seconds for an asset player node

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetPlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetInstanceAssetPlayerTime_BP`

```text
SetInstanceAssetPlayerTime_BP(AssetPlayerIndex: int32, time: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetPlayerIndex` | `int32` | - |
| `time` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetInstanceAssetPlayerTimeFraction`

```text
GetInstanceAssetPlayerTimeFraction(AssetPlayerIndex: int32) -> float
```

Get the current accumulated time as a fraction for an asset player node

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetPlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInstanceAssetPlayerTimeFromEnd`

```text
GetInstanceAssetPlayerTimeFromEnd(AssetPlayerIndex: int32) -> float
```

Get the time in seconds from the end of an animation in an asset player node

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetPlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInstanceAssetPlayerTimeFromEndFraction`

```text
GetInstanceAssetPlayerTimeFromEndFraction(AssetPlayerIndex: int32) -> float
```

Get the time as a fraction of the asset length of an animation in an asset player node

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetPlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInstanceMachineWeight`

```text
GetInstanceMachineWeight(MachineIndex: int32) -> float
```

Get the blend weight of a specified state machine

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInstanceStateWeight`

```text
GetInstanceStateWeight(MachineIndex: int32, StateIndex: int32) -> float
```

Get the blend weight of a specified state

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |
| `StateIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInstanceCurrentStateElapsedTime`

```text
GetInstanceCurrentStateElapsedTime(MachineIndex: int32) -> float
```

Get the current elapsed time of a state within the specified state machine

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInstanceTransitionCrossfadeDuration`

```text
GetInstanceTransitionCrossfadeDuration(MachineIndex: int32, TransitionIndex: int32) -> float
```

Get the crossfade duration of a specified transition

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |
| `TransitionIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInstanceTransitionTimeElapsed`

```text
GetInstanceTransitionTimeElapsed(MachineIndex: int32, TransitionIndex: int32) -> float
```

Get the elapsed time in seconds of a specified transition

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |
| `TransitionIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInstanceTransitionTimeElapsedFraction`

```text
GetInstanceTransitionTimeElapsedFraction(MachineIndex: int32, TransitionIndex: int32) -> float
```

Get the elapsed time as a fraction of the crossfade duration of a specified transition

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |
| `TransitionIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetRelevantAnimTimeRemaining`

```text
GetRelevantAnimTimeRemaining(MachineIndex: int32, StateIndex: int32, NullAnimDefaultValue: float) -> float
```

Get the time remaining in seconds for the most relevant animation in the source state

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |
| `StateIndex` | `int32` | - |
| `NullAnimDefaultValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetRelevantAnimTimeRemainingFraction`

```text
GetRelevantAnimTimeRemainingFraction(MachineIndex: int32, StateIndex: int32, NullAnimDefaultValue: float) -> float
```

Get the time remaining as a fraction of the duration for the most relevant animation in the source state

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |
| `StateIndex` | `int32` | - |
| `NullAnimDefaultValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetRelevantAnimLength`

```text
GetRelevantAnimLength(MachineIndex: int32, StateIndex: int32, NullAnimDefaultValue: float) -> float
```

Get the length in seconds of the most relevant animation in the source state

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |
| `StateIndex` | `int32` | - |
| `NullAnimDefaultValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetRelevantAnimTime`

```text
GetRelevantAnimTime(MachineIndex: int32, StateIndex: int32, NullAnimDefaultValue: float) -> float
```

Get the current accumulated time in seconds for the most relevant animation in the source state

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |
| `StateIndex` | `int32` | - |
| `NullAnimDefaultValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetRelevantAnimTimeFraction`

```text
GetRelevantAnimTimeFraction(MachineIndex: int32, StateIndex: int32, NullAnimDefaultValue: float) -> float
```

Get the current accumulated time as a fraction of the length of the most relevant animation in the source state

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |
| `StateIndex` | `int32` | - |
| `NullAnimDefaultValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetCurveValue`

```text
GetCurveValue(CurveName: FName, Immediately: bool) -> float
```

Returns the value of a named curve.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CurveName` | `FName` | - |
| `Immediately` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetCurrentStateName`

```text
GetCurrentStateName(MachineIndex: int32) -> FName
```

Returns the name of a currently active state in a state machine.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MachineIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `SetMorphTarget`

```text
SetMorphTarget(MorphTargetName: FName, Value: float) -> void
```

Sets a morph target to a certain weight.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MorphTargetName` | `FName` | - |
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMorphTargets`

```text
ClearMorphTargets() -> void
```

Clears the current morph targets.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CalculateDirection`

```text
CalculateDirection(Velocity: FVector &, BaseRotation: FRotator &) -> float
```

Returns degree of the angle betwee velocity and Rotation forward vector
	  The range of return will be from [-180, 180], and this can be used to feed blendspace directional value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Velocity` | `FVector &` | - |
| `BaseRotation` | `FRotator &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `LockAIResources`

```text
LockAIResources(bLockMovement: bool, LockAILogic: bool) -> void
```

locks indicated AI resources of animated pawn
	 	DEPRECATED. Use LockAIResourcesWithAnimation instead

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bLockMovement` | `bool` | - |
| `LockAILogic` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnlockAIResources`

```text
UnlockAIResources(bUnlockMovement: bool, UnlockAILogic: bool) -> void
```

unlocks indicated AI resources of animated pawn. Will unlock only animation-locked resources.
	 	DEPRECATED. Use UnlockAIResourcesWithAnimation instead

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bUnlockMovement` | `bool` | - |
| `UnlockAILogic` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTimeToClosestMarker`

```text
GetTimeToClosestMarker(SyncGroup: FName, MarkerName: FName, OutMarkerTime: float &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SyncGroup` | `FName` | - |
| `MarkerName` | `FName` | - |
| `OutMarkerTime` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `HasMarkerBeenHitThisFrame`

```text
HasMarkerBeenHitThisFrame(SyncGroup: FName, MarkerName: FName) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SyncGroup` | `FName` | - |
| `MarkerName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsSyncGroupBetweenMarkers`

```text
IsSyncGroupBetweenMarkers(InSyncGroupName: FName, PreviousMarker: FName, NextMarker: FName, bRespectMarkerOrder: bool) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSyncGroupName` | `FName` | - |
| `PreviousMarker` | `FName` | - |
| `NextMarker` | `FName` | - |
| `bRespectMarkerOrder` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetSyncGroupPosition`

```text
GetSyncGroupPosition(InSyncGroupName: FName) -> FMarkerSyncAnimPosition
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSyncGroupName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FMarkerSyncAnimPosition` | - |

### `TriggerAllSequenceSwitchNotify`

```text
TriggerAllSequenceSwitchNotify() -> void
```

Trigger AnimNotifies

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CheckCanTriggerNotify_AnimIsolation_Outer`

```text
CheckCanTriggerNotify_AnimIsolation_Outer(InAnimNotifyEvent: FAnimNotifyEvent &, InNotify: UAnimNotify *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimNotifyEvent` | `FAnimNotifyEvent &` | - |
| `InNotify` | `UAnimNotify *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `CheckCanTriggerNotifyState_AnimIsolation_Outer`

```text
CheckCanTriggerNotifyState_AnimIsolation_Outer(InAnimNotifyEvent: FAnimNotifyEvent &, InNotifyState: UAnimNotifyState *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimNotifyEvent` | `FAnimNotifyEvent &` | - |
| `InNotifyState` | `UAnimNotifyState *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `CheckCanTriggerAnimNotifyFunction_AnimIsolation_Outer`

```text
CheckCanTriggerAnimNotifyFunction_AnimIsolation_Outer(InAnimNotifyEvent: FAnimNotifyEvent &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimNotifyEvent` | `FAnimNotifyEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ReplaceSubAnimNodeAnimClass`

```text
ReplaceSubAnimNodeAnimClass(SubInstanceSlotName: FName, NewAnimClass: TSubclassOf < UAnimInstance >, BlendTime: float, bEnableNoWaitParallelEvalTask: bool) -> UAnimInstance *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |
| `NewAnimClass` | `TSubclassOf < UAnimInstance >` | - |
| `BlendTime` | `float` | - |
| `bEnableNoWaitParallelEvalTask` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `UAnimInstance *` | - |

### `ReplaceSubAnimNodeAnimClass_EmptyClassDefaut`

```text
ReplaceSubAnimNodeAnimClass_EmptyClassDefaut(SubInstanceSlotName: FName, NewAnimClass: TSubclassOf < UAnimInstance >, BlendTime: float) -> UAnimInstance *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |
| `NewAnimClass` | `TSubclassOf < UAnimInstance >` | - |
| `BlendTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `UAnimInstance *` | - |

### `ResetSubAnimNodeAnimClass`

```text
ResetSubAnimNodeAnimClass(SubInstanceSlotName: FName, FilterAnimClass: TSubclassOf < UAnimInstance >, BlendTime: float, bEnableNoWaitParallelEvalTask: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |
| `FilterAnimClass` | `TSubclassOf < UAnimInstance >` | - |
| `BlendTime` | `float` | - |
| `bEnableNoWaitParallelEvalTask` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetSubAnimNodeAnimClass_EmptyClassDefaut`

```text
ResetSubAnimNodeAnimClass_EmptyClassDefaut(SubInstanceSlotName: FName, FilterAnimClass: TSubclassOf < UAnimInstance >, BlendTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |
| `FilterAnimClass` | `TSubclassOf < UAnimInstance >` | - |
| `BlendTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetAllSubAnimNode`

```text
ResetAllSubAnimNode() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearAllSubAnimBlendTime`

```text
ClearAllSubAnimBlendTime() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetAllSubAnimNodePosInertialization`

```text
ResetAllSubAnimNodePosInertialization() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSubAnimInstanceBySlot`

```text
GetSubAnimInstanceBySlot(SubInstanceSlotName: FName) -> UAnimInstance *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UAnimInstance *` | - |

### `IsUseSubAnimInstanceBySlot`

```text
IsUseSubAnimInstanceBySlot(SubInstanceSlotName: FName) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetSubAnimNodeEnableBlend`

```text
SetSubAnimNodeEnableBlend(SubInstanceSlotName: FName, bEnable: bool, NewSubAnimBlendTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |
| `bEnable` | `bool` | - |
| `NewSubAnimBlendTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddSubAnimNodeAnimClass`

```text
AddSubAnimNodeAnimClass(SubInstanceSlotName: FName, NewAnimClass: TSubclassOf < UAnimInstance >, Priority: int32, BlendTime: float) -> UAnimInstance *
```

同槽多子动画实例

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |
| `NewAnimClass` | `TSubclassOf < UAnimInstance >` | - |
| `Priority` | `int32` | - |
| `BlendTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `UAnimInstance *` | - |

### `RemoveSubAnimNodeAnimClass`

```text
RemoveSubAnimNodeAnimClass(SubInstanceSlotName: FName, FilterClass: TSubclassOf < UAnimInstance >, BlendTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |
| `FilterClass` | `TSubclassOf < UAnimInstance >` | - |
| `BlendTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetSubAnimNode_MultiInstanceClass`

```text
ResetSubAnimNode_MultiInstanceClass(SubInstanceSlotName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SubInstanceSlotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetAllSubAnimNode_MultiInstance`

```text
ResetAllSubAnimNode_MultiInstance() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddStopTickSubAnimInstance`

```text
AddStopTickSubAnimInstance(Instance: UAnimInstance *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Instance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveCachedStopTickSubAnimInstance`

```text
RemoveCachedStopTickSubAnimInstance(Instance: UAnimInstance *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Instance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearAllStopTickSubAnimInstance`

```text
ClearAllStopTickSubAnimInstance() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRecycleCachedSubAnimInstances`

```text
OnRecycleCachedSubAnimInstances(bToPersistentPool: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bToPersistentPool` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MarkBoneStateDirty`

```text
MarkBoneStateDirty(InIsDirty: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIsDirty` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsBoneStateDirty`

```text
IsBoneStateDirty() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsUseBoneStateDirtyFeature`

```text
IsUseBoneStateDirtyFeature() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `HasSlotNode`

```text
HasSlotNode(InSlotName: FName) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSlotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `UpdateAnimSlotRetargetInfo`

```text
UpdateAnimSlotRetargetInfo(InMontage: UAnimMontage *, InSlotNameRetargetInfo: TMap < FName , FName > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMontage` | `UAnimMontage *` | - |
| `InSlotNameRetargetInfo` | `TMap < FName , FName > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetInverseRetargetIgnoreBoneList`

```text
GetInverseRetargetIgnoreBoneList() -> const TArray < int32 > &
```

**Returns**

| Type | Description |
|---|---|
| `const TArray < int32 > &` | - |

### `SetFollowedAnimInstance`

```text
SetFollowedAnimInstance(InputFollowedInstance: UAnimInstance *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InputFollowedInstance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetFollowedAnimInstance`

```text
ResetFollowedAnimInstance() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsFollowing`

```text
IsFollowing(TargetFollowedInstance: UAnimInstance *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetFollowedInstance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetDelayPlay`

```text
SetDelayPlay(IsDelay: bool, InputDelayFrames: int) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsDelay` | `bool` | - |
| `InputDelayFrames` | `int` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetParentAnimInstance`

```text
GetParentAnimInstance() -> UAnimInstance *
```

**Returns**

| Type | Description |
|---|---|
| `UAnimInstance *` | - |

### `SetParentAnimInstance`

```text
SetParentAnimInstance(InParentAnimInstance: UAnimInstance *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InParentAnimInstance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSubAnimInstances`

```text
GetSubAnimInstances() -> TArray < UAnimInstance * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < UAnimInstance * >` | - |

### `GetAllSubAnimInstances`

```text
GetAllSubAnimInstances() -> TArray < UAnimInstance * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < UAnimInstance * >` | - |

### `SwapCachedBoneTransformMap`

```text
SwapCachedBoneTransformMap() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCachedBoneTransform`

```text
GetCachedBoneTransform(InBoneName: FName, OutTransform: FTransform &, forceSync: bool) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBoneName` | `FName` | - |
| `OutTransform` | `FTransform &` | - |
| `forceSync` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetCachedBoneTransformByFlag`

```text
GetCachedBoneTransformByFlag(InBoneName: FName, InCacheFlag: FName, OutTransform: FTransform &, NeedLastFrameCount: int32, forceSync: bool) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBoneName` | `FName` | - |
| `InCacheFlag` | `FName` | - |
| `OutTransform` | `FTransform &` | - |
| `NeedLastFrameCount` | `int32` | - |
| `forceSync` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `CompareCachedBoneTransformByFlag`

```text
CompareCachedBoneTransformByFlag(InBoneName0: FName, InCacheFlag0: FName, InBoneName1: FName, InCacheFlag1: FName) -> int64
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBoneName0` | `FName` | - |
| `InCacheFlag0` | `FName` | - |
| `InBoneName1` | `FName` | - |
| `InCacheFlag1` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `SetTriggerAnimNotify`

```text
SetTriggerAnimNotify(NeedTrigger: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NeedTrigger` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FilterForceTriggerNotifyWhenMontageJumpTick`

```text
FilterForceTriggerNotifyWhenMontageJumpTick(InMontage: UAnimMontage *, bPlayingBackwards: bool, CurrentTrackPos: float, CurrentDeltaSeconds: float, InAnimNotifies: TArray < FAnimNotifyEvent > &, OutForceTriggerAnimNotifies: TArray < FAnimNotifyEvent > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMontage` | `UAnimMontage *` | - |
| `bPlayingBackwards` | `bool` | - |
| `CurrentTrackPos` | `float` | - |
| `CurrentDeltaSeconds` | `float` | - |
| `InAnimNotifies` | `TArray < FAnimNotifyEvent > &` | - |
| `OutForceTriggerAnimNotifies` | `TArray < FAnimNotifyEvent > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLobbySeqIgnoreNotifyList`

```text
GetLobbySeqIgnoreNotifyList() -> TArray < FString >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < FString >` | - |

### `ResetNotifyQueue`

```text
ResetNotifyQueue() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestoreAnimation`

```text
RestoreAnimation(InRecordName: FString &) -> void
```

编辑器调用函数，根据录制文件名进行重放，播放第一帧后暂停

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRecordName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `LogPoseDebug`

```text
LogPoseDebug() -> void
```

输出当前Pose至Log界面

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PauseOrContinueRestore`

```text
PauseOrContinueRestore() -> void
```

暂停或者继续重放

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestoreNextFrame`

```text
RestoreNextFrame() -> void
```

重放下一帧

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `JumpToGivenFrame`

```text
JumpToGivenFrame() -> void
```

跳转至指定帧

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestoreClear`

```text
RestoreClear() -> void
```

清空当前回放信息

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestartAnimation`

```text
RestartAnimation() -> void
```

重新开始回放

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SeekToFrame`

```text
SeekToFrame(FrameIndex: int32) -> void
```

跳转到指定帧并恢复该帧状态（编辑器调用）
	   要求当前处于 RestoreWait 或 RestoreEnd 状态
	   内部设置 DataAr 位置到 RestoreHeader[FrameIndex-1]，
	   下一帧 ParallelRestoreAnimation 将恢复该帧并更新调试数据

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FrameIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SeekToTime`

```text
SeekToTime(TimeInSeconds: float) -> void
```

根据时间跳转到最近帧（编辑器调用）
	   使用估算帧率计算帧索引后调用 SeekToFrame

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimeInSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestorePreviousFrame`

```text
RestorePreviousFrame() -> void
```

回退到前一帧（编辑器调用）

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnMontageBlendingOut`

```text
OnMontageBlendingOut(Montage: UAnimMontage*, bInterrupted: bool) -> void
```

Called when a montage starts blending out, whether interrupted or finished

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage*` | - |
| `bInterrupted` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMontageStarted`

```text
OnMontageStarted(Montage: UAnimMontage*) -> void
```

Called when a montage has started

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMontageEnded`

```text
OnMontageEnded(Montage: UAnimMontage*, bInterrupted: bool) -> void
```

Called when a montage has ended, whether interrupted or finished

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage*` | - |
| `bInterrupted` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMontageRealEnded`

```text
OnMontageRealEnded(Montage: UAnimMontage*, bInterrupted: bool) -> void
```

Called when a montage real ended, whether interrupted or finished

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage*` | - |
| `bInterrupted` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAllMontageInstancesEnded`

```text
OnAllMontageInstancesEnded() -> void
```

Called when all Montage instances have ended.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimInstanceUpdateCondition.json -->

# UAnimInstanceUpdateCondition

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Enable` | `bool` | - |

## Functions

### `SetEnable`

```text
SetEnable(InEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CheckCondition`

```text
CheckCondition(AnimInstance: UAnimInstance *, DeltaTime: float) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AnimInstance` | `UAnimInstance *` | - |
| `DeltaTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NeedUpdate`

```text
NeedUpdate(AnimInstance: UAnimInstance *, DeltaTime: float) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AnimInstance` | `UAnimInstance *` | - |
| `DeltaTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NeedUpdate_Internal`

```text
NeedUpdate_Internal(AnimInstance: UAnimInstance *, DeltaTime: float) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AnimInstance` | `UAnimInstance *` | - |
| `DeltaTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimMontage.json -->

# UAnimMontage

Any property you're adding to AnimMontage and parent class has to be considered for Child Asset
 
  Child Asset is considered to be only asset mapping feature using everything else in the class
  For example, you can just use all parent's setting  for the montage, but only remap assets
  This isn't magic bullet unfortunately and it is consistent effort of keeping the data synced with parent
  If you add new property, please make sure those property has to be copied for children.
  If it does, please add the copy in the function RefreshParentAssetData

## Inheritance

`UAnimCompositeBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BlendIn` | `FAlphaBlend` | Blend in option. |
| `BlendInTime_DEPRECATED` | `float` | - |
| `BlendOut` | `FAlphaBlend` | Blend out option. This is only used when it blends out itself. If it's interrupted by other montages, it will use new montage's BlendIn option to blend out. |
| `BlendOutTime_DEPRECATED` | `float` | - |
| `BlendOutTriggerTime` | `float` | Time from Sequence End to trigger blend out.<br>	  <0 means using BlendOutTime, so BlendOut finishes as Montage ends.<br>	  >=0 means using 'SequenceEnd - BlendOutTriggerTime' to trigger blend out. |
| `FilteredBones` | `FInputBlendPose` | - |
| `bAccumulateCurveSlotWeight` | `bool` | - |
| `bCheckSlotNodeRelevant` | `bool` | - |
| `SyncGroup` | `FName` | If you're using marker based sync for this montage, make sure to add sync group name. For now we only support one group |
| `SyncSlotIndex` | `int32` | wip: until we have UI working |
| `MarkerData` | `FMarkerSyncData` | - |
| `CompositeSections` | `TArray < FCompositeSection >` | - |
| `SlotAnimTracks` | `TArray < struct FSlotAnimationTrack >` | - |
| `BranchingPoints_DEPRECATED` | `TArray < struct FBranchingPoint >` | - |
| `bEnableRootMotionTranslation` | `bool` | If this is on, it will allow extracting root motion translation. DEPRECATED in 4.5 root motion is controlled by anim sequences |
| `bEnableRootMotionRotation` | `bool` | If this is on, it will allow extracting root motion rotation. DEPRECATED in 4.5 root motion is controlled by anim sequences |
| `bIsFarFromRoot` | `bool` | - |
| `RootMotionRootLock` | `TEnumAsByte < ERootMotionRootLock :: Type >` | Root Bone will be locked to that position when extracting root motion. DEPRECATED in 4.5 root motion is controlled by anim sequences |
| `bEnableMontageRandomSectionJump` | `bool` | - |
| `bRandomLoopJump` | `bool` | - |
| `RandomSectionNum` | `int32` | - |
| `RandomJumpTimes` | `int32` | - |
| `RetargetSource` | `FName` | - |
| `BranchingPointMarkers` | `TArray < FBranchingPointMarker >` | Cached list of Branching Point markers |
| `CurveForRootPosition` | `UCurveVector *` | 当在对Montage 本身进行构造Root 位置曲线后才会被携带的三个曲线 |
| `CurveForRootRotation` | `UCurveVector *` | - |
| `CurveForRootScale` | `UCurveVector *` | - |
| `BranchingPointStateNotifyIndices` | `TArray < int32 >` | Keep track of which AnimNotify_State are marked as BranchingPoints, so we can update their state when the Montage is ticked |
| `IgnoreNotifyType` | `TArray < FString >` | Names of notifies should be ignore in Montage. |
| `TimeStretchCurve` | `FTimeStretchCurve` | - |
| `TimeStretchCurveName` | `FName` | Name of optional TimeStretchCurveName to look for in Montage. |
| `PreviewBasePose` | `UAnimSequence *` | Preview Base pose for additive BlendSpace |
| `BoneRetargetBaseMesh` | `USkeletalMesh *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimNotify.json -->

# UAnimNotify

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bCheckAnimIsolation` | `bool` | - |
| `bCheckAnimIsolation_OnlyNewFPP` | `bool` | - |
| `bCheckAnimIsolation_OnlyNewFPP_IgnoreOldAnimMode` | `bool` | - |

## Functions

### `GetNotifyName`

```text
GetNotifyName() -> FString
```

Implementable event to get a custom name for the notify

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Received_Notify`

```text
Received_Notify(MeshComp: USkeletalMeshComponent *, Animation: UAnimSequenceBase *, InvokeAnimInstance: UAnimInstance *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MeshComp` | `USkeletalMeshComponent *` | - |
| `Animation` | `UAnimSequenceBase *` | - |
| `InvokeAnimInstance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimNotify_PlayMontageNotify.json -->

# UAnimNotify_PlayMontageNotify

## Inheritance

`UAnimNotify`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NotifyName` | `FName` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimNotify_PlayMontageNotifyWindow.json -->

# UAnimNotify_PlayMontageNotifyWindow

## Inheritance

`UAnimNotifyState`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NotifyName` | `FName` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimNotify_PlayParticleEffect.json -->

# UAnimNotify_PlayParticleEffect

## Inheritance

`UAnimNotify`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PSTemplate` | `UParticleSystem *` | - |
| `LocationOffset` | `FVector` | - |
| `RotationOffset` | `FRotator` | - |
| `RotationOffsetDisable` | `uint32` | - |
| `ScaleDisable` | `uint32` | - |
| `Scale` | `FVector` | - |
| `bPlayOnce` | `bool` | - |
| `bDestroyAtEnd` | `bool` | - |
| `SimulatedActivationOfQualityLevel` | `int32` | - |
| `PSCInstace` | `TWeakObjectPtr < UParticleSystemComponent >` | - |
| `Attached` | `uint32` | - |
| `SocketName` | `FName` | - |
| `UpdateWithoutBone` | `uint32` | - |
| `bNotifyControlParticleVisible` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimNotify_PlaySound.json -->

# UAnimNotify_PlaySound

## Inheritance

`UAnimNotify`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sound` | `USoundBase *` | - |
| `VolumeMultiplier` | `float` | - |
| `PitchMultiplier` | `float` | - |
| `bFollow` | `uint32` | - |
| `AttachName` | `FName` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimNotifyState.json -->

# UAnimNotifyState

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InOldFPPAnimMode_ChangeToNewFPPMesh` | `bool` | - |
| `bEnableBoneRetargetAdaptFeature` | `bool` | - |
| `bCheckAnimIsolation` | `bool` | - |
| `bCheckAnimIsolation_OnlyNewFPP` | `bool` | - |
| `bCheckAnimIsolation_OnlyNewFPP_IgnoreOldAnimMode` | `bool` | - |
| `bCheckAnimIsolation_OnlyTPP` | `bool` | 仅在TPP（第三人称）下生效，开启后此NotifyState只会在TPP AnimInstance中触发 |

## Functions

### `GetNotifyName`

```text
GetNotifyName() -> FString
```

Implementable event to get a custom name for the notify

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Received_NotifyBegin`

```text
Received_NotifyBegin(MeshComp: USkeletalMeshComponent *, Animation: UAnimSequenceBase *, TotalDuration: float, InvokeAnimInstance: UAnimInstance *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MeshComp` | `USkeletalMeshComponent *` | - |
| `Animation` | `UAnimSequenceBase *` | - |
| `TotalDuration` | `float` | - |
| `InvokeAnimInstance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Received_NotifyTick`

```text
Received_NotifyTick(MeshComp: USkeletalMeshComponent *, Animation: UAnimSequenceBase *, FrameDeltaTime: float, InvokeAnimInstance: UAnimInstance *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MeshComp` | `USkeletalMeshComponent *` | - |
| `Animation` | `UAnimSequenceBase *` | - |
| `FrameDeltaTime` | `float` | - |
| `InvokeAnimInstance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Received_NotifyEnd`

```text
Received_NotifyEnd(MeshComp: USkeletalMeshComponent *, Animation: UAnimSequenceBase *, InvokeAnimInstance: UAnimInstance *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MeshComp` | `USkeletalMeshComponent *` | - |
| `Animation` | `UAnimSequenceBase *` | - |
| `InvokeAnimInstance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `TryGetNewFPPAdaptSkelMeshComp`

```text
TryGetNewFPPAdaptSkelMeshComp(InTargetSkelMeshComp: USkeletalMeshComponent *, InIsInitCall: bool, HasRetarget: bool, ForceGetFPPMesh: bool) -> USkeletalMeshComponent *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |
| `InIsInitCall` | `bool` | - |
| `HasRetarget` | `bool` | - |
| `ForceGetFPPMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `USkeletalMeshComponent *` | - |

### `TryGetBoneRetargetAdaptSkelMeshComp`

```text
TryGetBoneRetargetAdaptSkelMeshComp(InTargetSkelMeshComp: USkeletalMeshComponent *, InIsInitCall: bool) -> USkeletalMeshComponent *
```

For Bone Retarget Feature Start

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |
| `InIsInitCall` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `USkeletalMeshComponent *` | - |

### `ClearBoneRetargetAdaptState`

```text
ClearBoneRetargetAdaptState(InTargetSkelMeshComp: USkeletalMeshComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsBoneRetargetAdaptInitDone`

```text
IsBoneRetargetAdaptInitDone(InTargetSkelMeshComp: USkeletalMeshComponent *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsEnableBoneRetargetAdaptFeature`

```text
IsEnableBoneRetargetAdaptFeature(InTargetSkelMeshComp: USkeletalMeshComponent *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimNotifyState_TimedParticleEffect.json -->

# UAnimNotifyState_TimedParticleEffect

## Inheritance

`UAnimNotifyState`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PSTemplate` | `UParticleSystem *` | - |
| `bIsPlayInWorld` | `bool` | - |
| `bIsRelativeToMeshSocketInWorld` | `bool` | - |
| `SocketName` | `FName` | - |
| `LocationOffset` | `FVector` | - |
| `RotationOffset` | `FRotator` | - |
| `RotationOffsetDisable` | `uint32` | - |
| `ScaleDisable` | `uint32` | - |
| `ScaleMultiplier` | `FVector` | - |
| `bDestroyAtEnd` | `bool` | - |
| `bEnableAttachMeshChangeIgnoreSocketCheck` | `bool` | - |
| `bAdaptToNewFPP` | `bool` | - |
| `CacheAttachAdaptMeshComp` | `TWeakObjectPtr < USkeletalMeshComponent >` | - |
| `SimulatedActivationOfQualityLevel` | `int32` | - |
| `CurveParamList` | `TMap < FName , FCurveParams >` | - |
| `ParticleComp` | `UParticleSystemComponent *` | - |
| `bNotifyControlParticleVisible` | `bool` | - |
| `bEnableSpawnObjTrackFeature` | `bool` | - |
| `bAddAnotherBone_Z_Delta` | `bool` | - |
| `Z_Delta_BoneName` | `FName` | - |
| `ParticleTag` | `FName` | - |
| `SpawnedObjCacheMap` | `TMap < FName , TWeakObjectPtr < UObject > >` | - |
| `bSkipSocketNameCheck` | `bool` | - |
| `EnableDestoryByUniqueTagAtEnd` | `bool` | - |
| `PreviousPSTemplates` | `TArray < UParticleSystem * >` | - |
| `PreviousSocketNames` | `TArray < FName >` | - |
| `bInDebugMode` | `bool` | - |
| `CurrentLocationOffset` | `FVector` | - |
| `CurrentRotationOffset` | `FRotator` | - |
| `CurrentScaleMultiplier` | `FVector` | - |
| `CachedSpawnedParticleComponent` | `UParticleSystemComponent *` | - |

## Functions

### `IsEnableSpawnObjTrackFeature`

```text
IsEnableSpawnObjTrackFeature() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `TryMarkSpawnObjTracker`

```text
TryMarkSpawnObjTracker(InTargetSkelMeshComp: USkeletalMeshComponent *, InSpawnedObj: UObject *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |
| `InSpawnedObj` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `TryClearSpawnObjTracker`

```text
TryClearSpawnObjTracker(InTargetSkelMeshComp: USkeletalMeshComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsTrackingObj`

```text
IsTrackingObj(InTargetSkelMeshComp: USkeletalMeshComponent *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetOverrideParticleTemplate`

```text
GetOverrideParticleTemplate(InTargetSkelMeshComp: USkeletalMeshComponent *, InPSTemplate: UParticleSystem *) -> UParticleSystem *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |
| `InPSTemplate` | `UParticleSystem *` | - |

**Returns**

| Type | Description |
|---|---|
| `UParticleSystem *` | - |

### `GetOverrideParticleWorldTransform`

```text
GetOverrideParticleWorldTransform(InTargetSkelMeshComp: USkeletalMeshComponent *, TargetTransform: FTransform) -> FTransform
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |
| `TargetTransform` | `FTransform` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `InnerCheckParticleParentVisibility`

```text
InnerCheckParticleParentVisibility(skComp: USkeletalMeshComponent *, InPSC: UParticleSystemComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `skComp` | `USkeletalMeshComponent *` | - |
| `InPSC` | `UParticleSystemComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CheckParticleParentVisibility`

```text
CheckParticleParentVisibility(InComponent: USkeletalMeshComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InComponent` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsEnableSearchAllDescendants`

```text
IsEnableSearchAllDescendants(InTargetSkelMeshComp: USkeletalMeshComponent *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SearchChildrenParticleAndDestroy`

```text
SearchChildrenParticleAndDestroy(Children: TArray < USceneComponent * >, MeshComp: USkeletalMeshComponent *, AttachAdaptMeshComp: USkeletalMeshComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Children` | `TArray < USceneComponent * >` | - |
| `MeshComp` | `USkeletalMeshComponent *` | - |
| `AttachAdaptMeshComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimNotifyState_Trail.json -->

# UAnimNotifyState_Trail

## Inheritance

`UAnimNotifyState`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PSTemplate` | `UParticleSystem *` | The particle system to use for this trail. |
| `FirstSocketName` | `FName` | Name of the first socket defining this trail. |
| `SecondSocketName` | `FName` | Name of the second socket defining this trail. |
| `FirstSocketRelativeOffset` | `FTransform` | - |
| `SecondSocketRelativeOffset` | `FTransform` | - |
| `WidthScaleMode` | `TEnumAsByte < enum ETrailWidthMode >` | - |
| `WidthScaleCurve` | `FName` | Name of the curve to drive the width scale. |
| `bRecycleSpawnedSystems` | `uint32` | - |
| `bRenderGeometry` | `uint32` | If true, render the trail geometry (this should typically be on) |
| `bRenderSpawnPoints` | `uint32` | If true, render stars at each spawned particle point along the trail |
| `bRenderTangents` | `uint32` | If true, render a line showing the tangent at each spawned particle point along the trail |
| `bRenderTessellation` | `uint32` | If true, render the tessellated path between spawned particles |

## Functions

### `OverridePSTemplate`

```text
OverridePSTemplate(MeshComp: USkeletalMeshComponent *, Animation: UAnimSequenceBase *) -> UParticleSystem *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MeshComp` | `USkeletalMeshComponent *` | - |
| `Animation` | `UAnimSequenceBase *` | - |

**Returns**

| Type | Description |
|---|---|
| `UParticleSystem *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimNotifyStateBoneRetargetAdaptInfoObj.json -->

# UAnimNotifyStateBoneRetargetAdaptInfoObj

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AnimNotifyStateBoneRetargetAdaptInfoMap` | `TMap < UObject * , FAnimNotifyStateBoneRetargetAdaptInfo >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimSequence.json -->

# UAnimSequence

## Inheritance

`UAnimSequenceBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NumFrames` | `int32` | Number of raw frames in this sequence (not used by engine - just for informational purposes). |
| `TrackToSkeletonMapTable` | `TArray < struct FTrackToSkeletonMap >` | In the future, maybe keeping RawAnimSequenceTrack + TrackMap as one would be good idea to avoid inconsistent array size<br>	  TrackToSkeletonMapTable(i) should contains  track mapping data for RawAnimationData(i). |
| `OverrideChunkFreeTime` | `float` | - |
| `OverrideFollowingChunkSize` | `float` | - |
| `bIshugeAnim` | `uint8` | - |
| `bImmediateLoadChunk` | `uint8` | - |
| `bForceUseStreamable` | `uint8` | - |
| `bUseStreamable` | `uint8` | - |
| `StreamableAdvanceConfig` | `bool` | - |
| `StreamableFirstChunkSize` | `float` | - |
| `StreamableFollowingChunkSize` | `float` | - |
| `bIgnoreDirectoryLimit` | `bool` | - |
| `AdditiveAnimType` | `TEnumAsByte < enum EAdditiveAnimationType >` | Additive animation type. |
| `RefPoseType` | `TEnumAsByte < enum EAdditiveBasePoseType >` | Additive refrerence pose type. Refer above enum type |
| `RefPoseSeq` | `UAnimSequence *` | Additive reference animation if it's relevant - i.e. AnimScaled or AnimFrame |
| `RefFrameIndex` | `int32` | Additve reference frame if RefPoseType == AnimFrame |
| `EncodingPkgVersion` | `int32` | The version of the global encoding package used at the time of import |
| `RetargetSource` | `FName` | Base pose to use when retargeting |
| `Interpolation` | `EAnimInterpolationType` | This defines how values between keys are calculated |
| `bEnableRootMotion` | `bool` | If this is on, it will allow extracting of root motion |
| `RootMotionRootLock` | `TEnumAsByte < ERootMotionRootLock :: Type >` | Root Bone will be locked to that position when extracting root motion. |
| `bForceRootLock` | `bool` | Force Root Bone Lock even if Root Motion is not enabled |
| `bRootMotionSettingsCopiedFromMontage` | `bool` | Have we copied root motion settings from an owning montage |
| `AuthoredSyncMarkers` | `TArray < FAnimSyncMarker >` | Authored Sync markers |
| `CurveForRootPosition` | `UCurveVector *` | 当在对Sequence 本身进行构造Root 位置曲线后才会被携带的三个曲线和新的Sequence |
| `CurveForRootRotation` | `UCurveVector *` | - |
| `CurveForRootScale` | `UCurveVector *` | - |
| `CreatedSequenceForRoot` | `UAnimSequence *` | - |
| `CurveForPositionRootSingleAxis` | `TSoftObjectPtr < UCurveFloat >` | - |
| `CurveForOnlySinglePosition` | `TSoftObjectPtr < UCurveVector >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimSequenceBase.json -->

# UAnimSequenceBase

## Inheritance

`UAnimationAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Notifies` | `TArray < FAnimNotifyEvent >` | Animation notifies, sorted by time (earliest notification first). |
| `SequenceLength` | `float` | Length (in seconds) of this AnimSequence if played back with a speed of 1.0. |
| `RateScale` | `float` | Number for tweaking playback rate of this animation globally. |
| `bEnableExcludeNotifiesWhenPlayAsMontage` | `bool` | - |
| `RawCurveData` | `FRawCurveTracks` | Raw uncompressed float curve data |

## Functions

### `GetPlayLength`

```text
GetPlayLength() -> ENGINE_API virtual float
```

Returns the total play length of the montage, if played back with a speed of 1.0.

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API virtual float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimSequencerInstance.json -->

# UAnimSequencerInstance

## Inheritance

`UAnimCustomInstance`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RuntimeAsset` | `TArray < UObject * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimSet.json -->

# UAnimSet

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bAnimRotationOnly` | `uint32` | Indicates that only the rotation should be taken from the animation sequence and the translation should come from the USkeletalMesh ref pose. <br>	 	Note that the root bone always takes translation from the animation, even if this flag is set.<br>	 	You can use the UseTranslationBoneNames array to specify other bones that should use translation with this flag set. |
| `TrackBoneNames` | `TArray < FName >` | Bone name that each track relates to. TrackBoneName.Num() == Number of tracks. |
| `LinkupCache` | `TArray < struct FAnimSetMeshLinkup >` | Non-serialised cache of linkups between different skeletal meshes and this AnimSet. |
| `BoneUseAnimTranslation` | `TArray < uint8 >` | Array of booleans that indicate whether or not to read the translation of a bone from animation or ref skeleton.<br>	 	This is basically a cooked down version of UseTranslationBoneNames for speed.<br>	 	Size matches the number of tracks. |
| `ForceUseMeshTranslation` | `TArray < uint8 >` | Cooked down version of ForceMeshTranslationBoneNames |
| `UseTranslationBoneNames` | `TArray < FName >` | Names of bones that should use translation from the animation, if bAnimRotationOnly is set. |
| `ForceMeshTranslationBoneNames` | `TArray < FName >` | List of bones which are ALWAYS going to use their translation from the mesh and not the animation. |
| `PreviewSkelMeshName` | `FName` | In the AnimSetEditor, when you switch to this AnimSet, it sees if this skeletal mesh is loaded and if so switches to it. |
| `BestRatioSkelMeshName` | `FName` | Holds the name of the skeletal mesh whose reference skeleton best matches the TrackBoneName array. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAnimSingleNodeInstance.json -->

# UAnimSingleNodeInstance

## Inheritance

`UAnimInstance`

## Functions

### `SetLooping`

```text
SetLooping(bIsLooping: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsLooping` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPlayRate`

```text
SetPlayRate(InPlayRate: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPlayRate` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetReverse`

```text
SetReverse(bInReverse: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInReverse` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPosition`

```text
SetPosition(InPosition: float, bFireNotifies: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPosition` | `float` | - |
| `bFireNotifies` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPositionWithPreviousTime`

```text
SetPositionWithPreviousTime(InPosition: float, InPreviousTime: float, bFireNotifies: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPosition` | `float` | - |
| `InPreviousTime` | `float` | - |
| `bFireNotifies` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlendSpaceInput`

```text
SetBlendSpaceInput(InBlendInput: FVector &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlendInput` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPlaying`

```text
SetPlaying(bIsPlaying: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsPlaying` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLength`

```text
GetLength() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `PlayAnim`

```text
PlayAnim(bIsLooping: bool, InPlayRate: float, InStartPosition: float) -> void
```

For AnimSequence specific

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsLooping` | `bool` | - |
| `InPlayRate` | `float` | - |
| `InStartPosition` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopAnim`

```text
StopAnim() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAnimationAsset`

```text
SetAnimationAsset(NewAsset: UAnimationAsset *, bIsLooping: bool, InPlayRate: float) -> void
```

Set New Asset - calls InitializeAnimation, for now we need MeshComponent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAsset` | `UAnimationAsset *` | - |
| `bIsLooping` | `bool` | - |
| `InPlayRate` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAnimationAsset`

```text
GetAnimationAsset() -> UAnimationAsset *
```

Get the currently used asset

**Returns**

| Type | Description |
|---|---|
| `UAnimationAsset *` | - |

### `SetPreviewCurveOverride`

```text
SetPreviewCurveOverride(PoseName: FName &, Value: float, bRemoveIfZero: bool) -> void
```

Set pose value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PoseName` | `FName &` | - |
| `Value` | `float` | - |
| `bRemoveIfZero` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `PostEvaluateAnimEvent`

```text
PostEvaluateAnimEvent() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAnimSinglePlayAnim`

```text
OnAnimSinglePlayAnim(AnimAsset: UAnimationAsset*, bPlay: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AnimAsset` | `UAnimationAsset*` | - |
| `bPlay` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UApplicationLifecycleComponent.json -->

# UApplicationLifecycleComponent

Component to handle receiving notifications from the OS about application state (activated, suspended, termination, etc).

## Inheritance

`UActorComponent`

## Delegates

### `ApplicationWillDeactivateDelegate`

```text
ApplicationWillDeactivateDelegate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationHasReactivatedDelegate`

```text
ApplicationHasReactivatedDelegate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationWillEnterBackgroundDelegate`

```text
ApplicationWillEnterBackgroundDelegate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationHasEnteredForegroundDelegate`

```text
ApplicationHasEnteredForegroundDelegate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationWillTerminateDelegate`

```text
ApplicationWillTerminateDelegate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTemperatureChangeDelegate`

```text
OnTemperatureChangeDelegate(Severity: ETemperatureSeverityType) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Severity` | `ETemperatureSeverityType` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UArrowComponent.json -->

# UArrowComponent

A simple arrow rendered using lines. Useful for indicating which way an object is facing.

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ArrowColor` | `FColor` | - |
| `ArrowSize` | `float` | - |
| `bIsScreenSizeScaled` | `bool` | Set to limit the screen size of this arrow |
| `ScreenSize` | `float` | The size on screen to limit this arrow to (in screen space) |
| `bTreatAsASprite` | `uint32` | If true, don't show the arrow when EngineShowFlags.BillboardSprites is disabled. |

## Functions

### `SetArrowColor`

```text
SetArrowColor(NewColor: FLinearColor) -> void
```

Updates the arrow's colour, and tells it to refresh

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAssetManager.json -->

# UAssetManager

A singleton UObject that is responsible for loading and unloading PrimaryAssets, and maintaining game-specific asset references
  Games should override this class and change the class reference

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ObjectReferenceList` | `TArray < UObject * >` | List of UObjects that are being kept from being GCd, derived from the asset type map. Arrays are currently more efficient than Sets |
| `bIsGlobalAsyncScanEnvironment` | `bool` | True if we are running a build that is already scanning assets globally so we can perhaps avoid scanning paths synchronously |
| `bShouldGuessTypeAndName` | `bool` | True if PrimaryAssetTypeName will be implied for loading assets that don't have it saved on disk. Won't work for all projects |
| `bShouldUseSynchronousLoad` | `bool` | True if we should always use synchronous loads, this speeds up cooking |
| `bIsLoadingFromPakFiles` | `bool` | True if we are loading from pak files |
| `bShouldAcquireMissingChunksOnLoad` | `bool` | True if the chunk install interface should be queries before loading assets |
| `bOnlyCookProductionAssets` | `bool` | If true, DevelopmentCook assets will error when they are cooked |
| `bIsBulkScanning` | `bool` | True if we are currently in bulk scanning mode |
| `bIsPrimaryAssetDirectoryCurrent` | `bool` | True if asset data is current, if false it will need to rescan before PIE |
| `bIsManagementDatabaseCurrent` | `bool` | True if the asset management database is up to date |
| `bUpdateManagementDatabaseAfterScan` | `bool` | True if the asset management database should be updated after scan completes |
| `bIncludeOnlyOnDiskAssets` | `bool` | True if only on-disk assets should be searched by the asset registry |
| `NumberOfSpawnedNotifications` | `int32` | Number of notifications seen in this update |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAssetManagerSettings.json -->

# UAssetManagerSettings

Settings for the Asset Management framework, which can be used to discover, load, and audit game-specific asset types

## Inheritance

`UDeveloperSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PrimaryAssetTypesToScan` | `TArray < FPrimaryAssetTypeInfo >` | List of asset types to scan at startup |
| `DirectoriesToExclude` | `TArray < FDirectoryPath >` | List of directories to exclude from scanning for Primary Assets, useful to exclude test assets |
| `PrimaryAssetRules` | `TArray < FPrimaryAssetRulesOverride >` | List of specific asset rule overrides |
| `bOnlyCookProductionAssets` | `bool` | If true, DevelopmentCook assets will error when they are cooked |
| `bShouldGuessTypeAndNameInEditor` | `bool` | If true, PrimaryAsset TypeName will be implied for assets in the editor (cooked builds always must be explicit). This allows guessing for content that hasn't been resaved yet |
| `bShouldAcquireMissingChunksOnLoad` | `bool` | If true, this will query the platform chunk install interface to request missing chunks for any requested primary asset loads |
| `IndexOfUsingAutoChunkName` | `int32` | - |
| `PrimaryAssetIdRedirects` | `TArray < FAssetManagerRedirect >` | Redirect from Type:Name to Type:NameNew |
| `PrimaryAssetTypeRedirects` | `TArray < FAssetManagerRedirect >` | Redirect from Type to TypeNew |
| `AssetPathRedirects` | `TArray < FAssetManagerRedirect >` | Redirect from gameassetpath to gameassetpathnew |
| `MetaDataTagsForAssetRegistry` | `TSet < FName >` | The metadata tags to be transferred to the Asset Registry. |
| `bParsePAWhenDroped` | `bool` | Asset Audit解析拖拽的PA. |
| `DefaultChunkName` | `FString` | 默认Core包名. |
| `BlacklistFilePath` | `FFilePath` | 编辑器检查用黑名单文件路径. |
| `BlacklistForPackageFilePath` | `FFilePath` | 打包用黑名单文件路径. |
| `bAlwaysReloadCSVConfig` | `bool` | 是否每次检查都重新读取黑名单配置. |
| `bUseBlacklistMap` | `bool` | 构造所有黑名单文件夹的文件Map来查找. |
| `bEnableCheckBlacklist` | `bool` | Whether check the asset depend on blacklist asset in content browser. |
| `SearchingDepth` | `int32` | The depth of searching blacklist asset tree in content browser. |
| `ManagementRuleConfigPath` | `FString` | - |
| `bUseAllMetaDataTagsForAssetRegistry` | `bool` | - |
| `bEnableModelStage` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAssetMappingTable.json -->

# UAssetMappingTable

UAssetMappingTable : that has AssetMappingTableging data 
 		- used for retargeting
 		- support to share different animations

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MappedAssets` | `TArray < FAssetMapping >` | Mappin of asset between source and target |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAssetRegistryHelpers.json -->

# UAssetRegistryHelpers

## Inheritance

`UObject`

## Functions

### `GetAssetRegistry`

```text
GetAssetRegistry() -> TScriptInterface < IAssetRegistry >
```

**Returns**

| Type | Description |
|---|---|
| `TScriptInterface < IAssetRegistry >` | - |

### `CreateAssetData`

```text
CreateAssetData(InAsset: UObject *, bAllowBlueprintClass: bool) -> FAssetData
```

Creates asset data from a UObject.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAsset` | `UObject *` | The asset to create asset data for |
| `bAllowBlueprintClass` | `bool` | By default trying to create asset data for a blueprint class will create one for the UBlueprint instead |

**Returns**

| Type | Description |
|---|---|
| `FAssetData` | - |

### `IsValid`

```text
IsValid(InAssetData: FAssetData &) -> bool
```

Checks to see if this AssetData refers to an asset or is NULL

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsUAsset`

```text
IsUAsset(InAssetData: FAssetData &) -> bool
```

Returns true if this asset was found in a UAsset file

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsRedirector`

```text
IsRedirector(InAssetData: FAssetData &) -> bool
```

Returns true if the this asset is a redirector.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetFullName`

```text
GetFullName(InAssetData: FAssetData &) -> FString
```

Returns the full name for the asset in the form: Class ObjectPath

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `ToSoftObjectPath`

```text
ToSoftObjectPath(InAssetData: FAssetData &) -> FSoftObjectPath
```

Convert to a SoftObjectPath for loading

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | - |

### `GetClass`

```text
GetClass(InAssetData: FAssetData &) -> UClass *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `UClass *` | - |

### `GetAsset`

```text
GetAsset(InAssetData: FAssetData &) -> UObject *
```

Returns the asset UObject if it is loaded or loads the asset if it is unloaded then returns the result

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

### `IsAssetLoaded`

```text
IsAssetLoaded(InAssetData: FAssetData &) -> bool
```

Returns true if the asset is loaded

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetExportTextName`

```text
GetExportTextName(InAssetData: FAssetData &) -> FString
```

Returns the name for the asset in the form: Class'ObjectPath'

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetTagValue < FName >`

```text
GetTagValue < FName >(InAssetData: FAssetData &, InTagName: FName &, OutTagValue: FString &) -> bool
```

Gets the value associated with the given tag as a string

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |
| `InTagName` | `FName &` | - |
| `OutTagValue` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetFilterTagsAndValues`

```text
SetFilterTagsAndValues(InFilter: FARFilter &, InTagsAndValues: TArray < FTagAndValue > &) -> FARFilter
```

Populates the FARFilters tags and values map with the passed in tags and values

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFilter` | `FARFilter &` | - |
| `InTagsAndValues` | `TArray < FTagAndValue > &` | - |

**Returns**

| Type | Description |
|---|---|
| `FARFilter` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAsyncTaskDownloadImage.json -->

# UAsyncTaskDownloadImage

## Inheritance

`UBlueprintAsyncActionBase`

## Functions

### `DownloadImage`

```text
DownloadImage(URL: FString) -> UAsyncTaskDownloadImage *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `URL` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `UAsyncTaskDownloadImage *` | - |

## Delegates

### `OnSuccess`

```text
OnSuccess(Texture: UTexture2DDynamic*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Texture` | `UTexture2DDynamic*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnFail`

```text
OnFail(Texture: UTexture2DDynamic*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Texture` | `UTexture2DDynamic*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAtmosphericFogComponent.json -->

# UAtmosphericFogComponent

Used to create fogging effects such as clouds.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SunMultiplier` | `float` | Global scattering factor. |
| `FogMultiplier` | `float` | Scattering factor on object. |
| `DensityMultiplier` | `float` | Fog density control factor. |
| `DensityOffset` | `float` | Fog density offset to control opacity [-1.f ~ 1.f]. |
| `DistanceScale` | `float` | Distance scale. |
| `AltitudeScale` | `float` | Altitude scale (only Z scale). |
| `DistanceOffset` | `float` | Distance offset, in km (to handle large distance) |
| `GroundOffset` | `float` | Ground offset. |
| `StartDistance` | `float` | Start Distance. |
| `SunDiscScale` | `float` | Distance offset, in km (to handle large distance) |
| `DefaultBrightness` | `float` | Default light brightness. Used when there is no sunlight placed in the level. Unit is lumens |
| `DefaultLightColor` | `FColor` | Default light color. Used when there is no sunlight placed in the level. |
| `bDisableSunDisk` | `uint32` | Disable Sun Disk rendering. |
| `bDisableGroundScattering` | `uint32` | Disable Color scattering from ground. |
| `PrecomputeParams` | `FAtmospherePrecomputeParameters` | - |
| `TransmittanceTexture_DEPRECATED` | `UTexture2D *` | - |
| `IrradianceTexture_DEPRECATED` | `UTexture2D *` | - |

## Functions

### `SetDefaultBrightness`

```text
SetDefaultBrightness(NewBrightness: float) -> ENGINE_API void
```

Set brightness of the light

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewBrightness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetDefaultLightColor`

```text
SetDefaultLightColor(NewLightColor: FLinearColor) -> ENGINE_API void
```

Set color of the light

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetSunMultiplier`

```text
SetSunMultiplier(NewSunMultiplier: float) -> ENGINE_API void
```

Set SunMultiplier

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewSunMultiplier` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetFogMultiplier`

```text
SetFogMultiplier(NewFogMultiplier: float) -> ENGINE_API void
```

Set FogMultiplier

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewFogMultiplier` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetDensityMultiplier`

```text
SetDensityMultiplier(NewDensityMultiplier: float) -> ENGINE_API void
```

Set DensityMultiplier

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewDensityMultiplier` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetDensityOffset`

```text
SetDensityOffset(NewDensityOffset: float) -> ENGINE_API void
```

Set DensityOffset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewDensityOffset` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetDistanceScale`

```text
SetDistanceScale(NewDistanceScale: float) -> ENGINE_API void
```

Set DistanceScale

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewDistanceScale` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetAltitudeScale`

```text
SetAltitudeScale(NewAltitudeScale: float) -> ENGINE_API void
```

Set AltitudeScale

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAltitudeScale` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetStartDistance`

```text
SetStartDistance(NewStartDistance: float) -> ENGINE_API void
```

Set StartDistance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewStartDistance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetDistanceOffset`

```text
SetDistanceOffset(NewDistanceOffset: float) -> ENGINE_API void
```

Set DistanceOffset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewDistanceOffset` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `DisableSunDisk`

```text
DisableSunDisk(NewSunDisk: bool) -> ENGINE_API void
```

Set DisableSunDisk

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewSunDisk` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `DisableGroundScattering`

```text
DisableGroundScattering(NewGroundScattering: bool) -> ENGINE_API void
```

Set DisableGroundScattering

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewGroundScattering` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetPrecomputeParams`

```text
SetPrecomputeParams(DensityHeight: float, MaxScatteringOrder: int32, InscatterAltitudeSampleNum: int32) -> ENGINE_API void
```

Set PrecomputeParams, only valid in Editor mode

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DensityHeight` | `float` | - |
| `MaxScatteringOrder` | `int32` | - |
| `InscatterAltitudeSampleNum` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `StartPrecompute`

```text
StartPrecompute() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAtmosphericSkyBoxComponent.json -->

# UAtmosphericSkyBoxComponent

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RenderDynamicSky` | `bool` | - |
| `Material` | `UMaterialInterface *` | - |
| `NoiseTexture` | `UTexture2D *` | - |
| `StaticMesh` | `UStaticMesh *` | - |
| `RadiusScale` | `float` | - |
| `MeshRotation` | `FRotator` | - |
| `RainyDegree` | `float` | - |
| `Atmosphere` | `FTOD_AtmosphereParameters` | - |
| `Day` | `FTOD_DayParameters` | - |
| `Light` | `FTOD_LightParameters` | - |
| `CloudsPbr` | `FTOD_CloudPBRParameters` | - |
| `World` | `FTOD_WorldParameters` | - |
| `Cycle` | `FTOD_CycleParameters` | - |
| `TodTime` | `FTOD_Time` | - |
| `TodAnimation` | `FTOD_Animation` | - |
| `TodSunParams` | `FTOD_Sun` | - |
| `TodMoonParams` | `FTOD_Moon` | - |
| `TodSunAndMoonParams` | `FTOD_SunAndMoon` | - |
| `TodStarsParams` | `FTOD_Stars` | - |
| `TodSpecialSkyParams` | `FTOD_SpecialSky` | - |
| `SunActor` | `AActor *` | - |
| `MoonActor` | `AActor *` | - |
| `LightingChannels` | `FLightingChannels` | - |
| `MaterialInstancesDynamic` | `UMaterialInstanceDynamic *` | - |
| `bIsMaterialInstanceDirty` | `bool` | - |
| `FixedTimeOfDay` | `bool` | - |
| `FixedCurrTime` | `float` | - |
| `bNeedUpdate` | `bool` | - |

## Functions

### `SetFixedCurrTime`

```text
SetFixedCurrTime(time: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `time` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFixedTimeOfDay`

```text
SetFixedTimeOfDay(IsFiexd: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsFiexd` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNeedUpdate`

```text
SetNeedUpdate(NeedUpdate: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NeedUpdate` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMaterialInstancesDynamic`

```text
GetMaterialInstancesDynamic() -> UMaterialInstanceDynamic *
```

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAudioComponent.json -->

# UAudioComponent

AudioComponent is used to play a Sound
 
  @see USoundBase

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sound` | `USoundBase *` | The sound to be played |
| `InstanceParameters` | `TArray < struct FAudioComponentParam >` | Array of per-instance parameters for this AudioComponent. |
| `SoundClassOverride` | `USoundClass *` | Optional sound group this AudioComponent belongs to |
| `bAutoDestroy` | `uint8` | Auto destroy this component on completion |
| `bStopWhenOwnerDestroyed` | `uint8` | Stop sound when owner is destroyed |
| `bShouldRemainActiveIfDropped` | `uint8` | Whether the wave instances should remain active if they're dropped by the prioritization code. Useful for e.g. vehicle sounds that shouldn't cut out. |
| `bAllowSpatialization` | `uint8` | Overrides spatialization enablement in either the attenuation asset or on this audio component's attenuation settings override. |
| `bOverrideAttenuation` | `uint8` | Allows defining attenuation settings directly on this audio component without using an attenuation settings asset. |
| `bOverrideSubtitlePriority` | `uint32` | Whether or not to override the sound's subtitle priority. |
| `bIsUISound` | `uint8` | Whether or not this sound plays when the game is paused in the UI |
| `bEnableLowPassFilter` | `uint8` | Whether or not to apply a low-pass filter to the sound that plays in this audio component. |
| `bOverridePriority` | `uint8` | - |
| `bSuppressSubtitles` | `uint8` | If true, subtitles in the sound data will be ignored. |
| `AudioComponentUserID` | `FName` | Configurable, serialized ID for audio plugins |
| `PitchModulationMin` | `float` | The lower bound to use when randomly determining a pitch multiplier |
| `PitchModulationMax` | `float` | The upper bound to use when randomly determining a pitch multiplier |
| `VolumeModulationMin` | `float` | The lower bound to use when randomly determining a volume multiplier |
| `VolumeModulationMax` | `float` | The upper bound to use when randomly determining a volume multiplier |
| `VolumeMultiplier` | `float` | A volume multiplier to apply to sounds generated by this component |
| `Priority` | `float` | A priority value that is used for sounds that play on this component that scales against final output volume. |
| `SubtitlePriority` | `float` | Used by the subtitle manager to prioritize subtitles wave instances spawned by this component. |
| `VolumeWeightedPriorityScale_DEPRECATED` | `float` | - |
| `PitchMultiplier` | `float` | A pitch multiplier to apply to sounds generated by this component |
| `HighFrequencyGainMultiplier_DEPRECATED` | `float` | - |
| `LowPassFilterFrequency` | `float` | The frequency of the lowpass filter (in hertz) to apply to this voice. A frequency of 0.0 is the device sample rate and will bypass the filter. |
| `AttenuationSettings` | `USoundAttenuation *` | If bOverrideSettings is false, the asset to use to determine attenuation properties for sounds generated by this component |
| `AttenuationOverrides` | `FSoundAttenuationSettings` | If bOverrideSettings is true, the attenuation properties to use for sounds generated by this component |
| `ConcurrencySettings` | `USoundConcurrency *` | What sound concurrency to use for sounds generated by this audio component |

## Functions

### `SetSound`

```text
SetSound(NewSound: USoundBase *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewSound` | `USoundBase *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FadeIn`

```text
FadeIn(FadeInDuration: float, FadeVolumeLevel: float, StartTime: float) -> void
```

This can be used in place of "play" when it is desired to fade in the sound over time.
	 
	  If FadeTime is 0.0, the change in volume is instant.
	  If FadeTime is > 0.0, the multiplier will be increased from 0 to FadeVolumeLevel over FadeIn seconds.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FadeInDuration` | `float` | how long it should take to reach the FadeVolumeLevel |
| `FadeVolumeLevel` | `float` | the percentage of the AudioComponents's calculated volume to fade to |
| `StartTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FadeOut`

```text
FadeOut(FadeOutDuration: float, FadeVolumeLevel: float) -> void
```

This is used in place of "stop" when it is desired to fade the volume of the sound before stopping.
	 
	  If FadeTime is 0.0, this is the same as calling Stop().
	  If FadeTime is > 0.0, this will adjust the volume multiplier to FadeVolumeLevel over FadeInTime seconds
	  and then stop the sound.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FadeOutDuration` | `float` | how long it should take to reach the FadeVolumeLevel |
| `FadeVolumeLevel` | `float` | the percentage of the AudioComponents's calculated volume in which to fade to |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Play`

```text
Play(StartTime: float) -> void
```

Start a sound playing on an audio component

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

Stop an audio component playing its sound cue, issue any delegates if needed

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPaused`

```text
SetPaused(bPause: bool) -> void
```

Pause an audio component playing its sound cue, issue any delegates if needed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bPause` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsPlaying`

```text
IsPlaying() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if this component is currently playing a SoundCue. |

### `AdjustVolume`

```text
AdjustVolume(AdjustVolumeDuration: float, AdjustVolumeLevel: float) -> void
```

This will allow one to adjust the volume of an AudioComponent on the fly

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AdjustVolumeDuration` | `float` | - |
| `AdjustVolumeLevel` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFloatParameter`

```text
SetFloatParameter(InName: FName, InFloat: float) -> void
```

Set a float instance parameter for use in sound cues played by this audio component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InName` | `FName` | - |
| `InFloat` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWaveParameter`

```text
SetWaveParameter(InName: FName, InWave: USoundWave *) -> void
```

Set a sound wave instance parameter for use in sound cues played by this audio component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InName` | `FName` | - |
| `InWave` | `USoundWave *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBoolParameter`

```text
SetBoolParameter(InName: FName, InBool: bool) -> void
```

Set a boolean instance parameter for use in sound cues played by this audio component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InName` | `FName` | - |
| `InBool` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIntParameter`

```text
SetIntParameter(InName: FName, InInt: int32) -> void
```

Set an integer instance parameter for use in sound cues played by this audio component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InName` | `FName` | - |
| `InInt` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumeMultiplier`

```text
SetVolumeMultiplier(NewVolumeMultiplier: float) -> void
```

Set a new volume multiplier

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewVolumeMultiplier` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPitchMultiplier`

```text
SetPitchMultiplier(NewPitchMultiplier: float) -> void
```

Set a new pitch multiplier

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPitchMultiplier` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetUISound`

```text
SetUISound(bInUISound: bool) -> void
```

Set whether sounds generated by this audio component should be considered UI sounds

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInUISound` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AdjustAttenuation`

```text
AdjustAttenuation(InAttenuationSettings: FSoundAttenuationSettings &) -> void
```

Modify the attenuation settings of the audio component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAttenuationSettings` | `FSoundAttenuationSettings &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSubmixSend`

```text
SetSubmixSend(Submix: USoundSubmix *, SendLevel: float) -> void
```

Sets how much audio the sound should send to the given submix.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Submix` | `USoundSubmix *` | - |
| `SendLevel` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLowPassFilterEnabled`

```text
SetLowPassFilterEnabled(InLowPassFilterEnabled: bool) -> void
```

Sets whether or not the low pass filter is enabled on the audio component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InLowPassFilterEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLowPassFilterFrequency`

```text
SetLowPassFilterFrequency(InLowPassFilterFrequency: float) -> void
```

Sets lowpass filter frequency of the audio component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InLowPassFilterFrequency` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BP_GetAttenuationSettingsToApply`

```text
BP_GetAttenuationSettingsToApply(OutAttenuationSettings: FSoundAttenuationSettings &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutAttenuationSettings` | `FSoundAttenuationSettings &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Delegates

### `OnAudioFinished`

```text
OnAudioFinished() -> void
```

called when we finish playing audio, either because it played to completion or because a Stop() call turned it off early

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAudioPlaybackPercent`

```text
OnAudioPlaybackPercent(PlayingSoundWave: const class USoundWave*, PlaybackPercent: const float) -> void
```

Called as a sound plays on the audio component to allow BP to perform actions based on playback percentage.
	 Computed as samples played divided by total samples, taking into account pitch.
	 Not currently implemented on all platforms.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayingSoundWave` | `const class USoundWave*` | - |
| `PlaybackPercent` | `const float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnQueueSubtitles`

```text
OnQueueSubtitles(Subtitles: const TArray<struct FSubtitleCue>&, CueDuration: float) -> void
```

Called when subtitles are sent to the SubtitleManager.  Set this delegate if you want to hijack the subtitles for other purposes

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Subtitles` | `const TArray&` | - |
| `CueDuration` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAudioMixerBlueprintLibrary.json -->

# UAudioMixerBlueprintLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `AddMasterSubmixEffect`

```text
AddMasterSubmixEffect(WorldContextObject: UObject *, SubmixEffectPreset: USoundEffectSubmixPreset *) -> void
```

Adds a submix effect preset to the master submix.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `SubmixEffectPreset` | `USoundEffectSubmixPreset *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveMasterSubmixEffect`

```text
RemoveMasterSubmixEffect(WorldContextObject: UObject *, SubmixEffectPreset: USoundEffectSubmixPreset *) -> void
```

Removes a submix effect preset from the master submix.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `SubmixEffectPreset` | `USoundEffectSubmixPreset *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMasterSubmixEffects`

```text
ClearMasterSubmixEffects(WorldContextObject: UObject *) -> void
```

Clears all master submix effects.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddSourceEffectToPresetChain`

```text
AddSourceEffectToPresetChain(WorldContextObject: UObject *, PresetChain: USoundEffectSourcePresetChain *, Entry: FSourceEffectChainEntry) -> void
```

Adds source effect entry to preset chain. Only effects the instance of the preset chain

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PresetChain` | `USoundEffectSourcePresetChain *` | - |
| `Entry` | `FSourceEffectChainEntry` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveSourceEffectFromPresetChain`

```text
RemoveSourceEffectFromPresetChain(WorldContextObject: UObject *, PresetChain: USoundEffectSourcePresetChain *, EntryIndex: int32) -> void
```

Adds source effect entry to preset chain. Only affects the instance of preset chain.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PresetChain` | `USoundEffectSourcePresetChain *` | - |
| `EntryIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBypassSourceEffectChainEntry`

```text
SetBypassSourceEffectChainEntry(WorldContextObject: UObject *, PresetChain: USoundEffectSourcePresetChain *, EntryIndex: int32, bBypassed: bool) -> void
```

Set whether or not to bypass the effect at the source effect chain index.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PresetChain` | `USoundEffectSourcePresetChain *` | - |
| `EntryIndex` | `int32` | - |
| `bBypassed` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetNumberOfEntriesInSourceEffectChain`

```text
GetNumberOfEntriesInSourceEffectChain(WorldContextObject: UObject *, PresetChain: USoundEffectSourcePresetChain *) -> int32
```

Returns the number of effect chain entries in the given source effect chain.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PresetChain` | `USoundEffectSourcePresetChain *` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAudioSettings.json -->

# UAudioSettings

Audio settings.

## Inheritance

`UDeveloperSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultSoundClassName` | `FSoftObjectPath` | The SoundClass assigned to newly created sounds |
| `DefaultSoundConcurrencyName` | `FSoftObjectPath` | The SoundConcurrency assigned to newly created sounds |
| `DefaultBaseSoundMix` | `FSoftObjectPath` | The SoundMix to use as base when no other system has specified a Base SoundMix |
| `VoiPSoundClass` | `FSoftObjectPath` | Sound class to be used for the VOIP audio component |
| `DefaultReverbSendLevel` | `float` | The amount of audio to send to reverb submixes if no reverb send is setup for the source through attenuation settings. Only used in audio mixer. |
| `LowPassFilterResonance` | `float` | - |
| `MaximumConcurrentStreams` | `int32` | How many streaming sounds can be played at the same time (if more are played they will be sorted by priority) |
| `QualityLevels` | `TArray < FAudioQualitySettings >` | - |
| `bAllowVirtualizedSounds` | `uint32` | Allows sounds to play at 0 volume. |
| `bDisableMasterEQ` | `uint32` | Disables master EQ effect in the audio DSP graph. |
| `bDisableMasterReverb` | `uint32` | Disables master reverb effect in the audio DSP graph. |
| `bAllowCenterChannel3DPanning` | `uint32` | Enables the surround sound spatialization calculations to include the center channel. |
| `DialogueFilenameFormat` | `FString` | - |
| `AkEventCppNotifyClass` | `TSoftClassPtr < UAnimNotify >` | UAnimNotify_AkEventCpp is the subclass of UAnimNotify. |
| `TimedAkEventNotifyStateClass` | `TSoftClassPtr < UAnimNotifyState >` | UAnimNotifyState_TimedAkEvent is the subclass of UAnimNotifyState. |
| `AkAudioEventSearchDepth` | `uint8` | Search depth when trying to link commerce animation montage with its AkAudioEvent. |
| `bUsePreCachedMontageMap` | `bool` | Whether to use pre-cached map for AkAudio-Montages searching. |
| `bDynamicPreCachedMontageMap` | `bool` | Whether to dynamically update pre-cached map for AkAudio-Montages searching. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAutomatedLevelSequenceCapture.json -->

# UAutomatedLevelSequenceCapture

## Inheritance

`UMovieSceneCapture`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LevelSequenceAsset` | `FSoftObjectPath` | A level sequence asset to playback at runtime - used where the level sequence does not already exist in the world. |
| `bUseCustomStartFrame` | `bool` | When enabled, the StartFrame setting will override the default starting frame number |
| `StartFrame` | `int32` | Frame number to start capturing.  The frame number range depends on whether the bUseRelativeFrameNumbers option is enabled. |
| `bUseCustomEndFrame` | `bool` | When enabled, the EndFrame setting will override the default ending frame number |
| `EndFrame` | `int32` | Frame number to end capturing.  The frame number range depends on whether the bUseRelativeFrameNumbers option is enabled. |
| `WarmUpFrameCount` | `int32` | The number of extra frames to play before the sequence's start frame, to "warm up" the animation.  This is useful if your<br>	    animation contains particles or other runtime effects that are spawned into the scene earlier than your capture start frame |
| `DelayBeforeWarmUp` | `float` | The number of seconds to wait (in real-time) before we start playing back the warm up frames.  Useful for allowing post processing effects to settle down before capturing the animation. |
| `BurnInOptions` | `ULevelSequenceBurnInOptions *` | - |
| `bWriteEditDecisionList` | `bool` | Whether to write edit decision lists (EDLs) if the sequence contains shots |
| `LevelSequenceActor` | `TWeakObjectPtr < ALevelSequenceActor >` | The pre-existing level sequence actor to use for capture that specifies playback settings |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UAutomationTestSettings.json -->

# UAutomationTestSettings

Implements the Editor's user settings.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EngineTestModules` | `TArray < FString >` | Modules to load that have engine tests |
| `EditorTestModules` | `TArray < FString >` | Modules to load that have editor tests |
| `AutomationTestmap` | `FSoftObjectPath` | The automation test map to be used for several of the automation tests. |
| `EditorPerformanceTestMaps` | `TArray < FEditorMapPerformanceTestDefinition >` | The map to be used for the editor performance capture tool. |
| `AssetsToOpen` | `TArray < FSoftObjectPath >` | Asset to test for open in automation process |
| `BuildPromotionTest` | `FBuildPromotionTestSettings` | Editor build promotion test settings |
| `MaterialEditorPromotionTest` | `FMaterialEditorPromotionSettings` | Material editor promotion test settings |
| `ParticleEditorPromotionTest` | `FParticleEditorPromotionSettings` | Particle editor promotion test settings |
| `BlueprintEditorPromotionTest` | `FBlueprintEditorPromotionSettings` | Blueprint editor promotion test settings |
| `TestLevelFolders` | `TArray < FString >` | Folders containing levels to exclude from automated tests |
| `ExternalTools` | `TArray < FExternalToolDefinition >` | External executables and scripts to run as part of automation. |
| `ImportExportTestDefinitions` | `TArray < FEditorImportExportTestDefinition >` | Asset import  Export test settings |
| `LaunchOnSettings` | `TArray < FLaunchOnTestSettings >` | The map and device type to be used for the editor Launch On With Map Iterations test. |
| `DefaultScreenshotResolution` | `FIntPoint` | The default resolution to take all automation screenshots at. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBackgroundBlur.json -->

# UBackgroundBlur

A background blur is a container widget that can contain one child widget, providing an opportunity 
  to surround it with adjustable padding and apply a post-process Gaussian blur to all content beneath the widget.
 
   Single Child
   Blur Effect

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Padding` | `FMargin` | The padding area between the slot and the content it contains. |
| `HorizontalAlignment` | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the content horizontally. |
| `VerticalAlignment` | `TEnumAsByte < EVerticalAlignment >` | The alignment of the content vertically. |
| `bApplyAlphaToBlur` | `bool` | True to modulate the strength of the blur based on the widget alpha. |
| `BlurStrength` | `float` | How blurry the background is.  Larger numbers mean more blurry but will result in larger runtime cost on the gpu. |
| `bOverrideAutoRadiusCalculation` | `bool` | Whether or not the radius should be computed automatically or if it should use the radius |
| `BlurType` | `TEnumAsByte < EBlurType >` | Blur type |
| `BlurDirection` | `float` | Blur direction for directional blur |
| `BlurCenter` | `FVector2D` | Blur center for radial and rotate blur |
| `BlurRadius` | `int32` | This is the number of pixels which will be weighted in each direction from any given pixel when computing the blur<br>	  A larger value is more costly but allows for stronger blurs. |
| `BlurMask` | `UTexture *` | A blur mask texture |
| `LowQualityFallbackBrush` | `FSlateBrush` | An image to draw instead of applying a blur when low quality override mode is enabled. <br>	  You can enable low quality mode for background blurs by setting the cvar Slate.ForceBackgroundBlurLowQualityOverride to 1. <br>	  This is usually done in the project's scalability settings |
| `BlurMaskBrush` | `FSlateBrush` | - |

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

### `SetApplyAlphaToBlur`

```text
SetApplyAlphaToBlur(bInApplyAlphaToBlur: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInApplyAlphaToBlur` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlurRadius`

```text
SetBlurRadius(InBlurRadius: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlurRadius` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlurStrength`

```text
SetBlurStrength(InStrength: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStrength` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlurDirection`

```text
SetBlurDirection(InDirection: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDirection` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlurCenter`

```text
SetBlurCenter(InCenter: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCenter` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlurMask`

```text
SetBlurMask(InTexture: UTexture *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTexture` | `UTexture *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLowQualityFallbackBrush`

```text
SetLowQualityFallbackBrush(InBrush: FSlateBrush &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBrush` | `FSlateBrush &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBackgroundBlurSlot.json -->

# UBackgroundBlurSlot

The Slot for the UBackgroundBlurSlot, contains the widget displayed in a BackgroundBlur's single slot

## Inheritance

`UPanelSlot`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Padding` | `FMargin` | The padding area between the slot and the content it contains. |
| `HorizontalAlignment` | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the object horizontally. |
| `VerticalAlignment` | `TEnumAsByte < EVerticalAlignment >` | The alignment of the object vertically. |

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

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/%E8%83%8C%E5%8C%85%E7%BB%84%E4%BB%B6%E7%B1%BB/UBackpackComponent.json -->

# UBackpackComponent

背包组件

## Inheritance

`UActorComponent` -> `IItemContainerInterface` -> `IItemFactoryInterface` -> `ICommonBackpackInterface`

## Delegates

### `UGC_ItemOperationFailedDelegate`

```text
UGC_ItemOperationFailedDelegate(DefineID: const FItemDefineID&, OperationType: EBattleItemOperationType, OperationFailedReason: EBattleItemOperationFailedReason) -> void
```

Delegate
	  生效范围SC
	  物品操作失败时通知

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `const FItemDefineID&` | 物品DefineID |
| `OperationType` | `EBattleItemOperationType` | 操作类型 |
| `OperationFailedReason` | `EBattleItemOperationFailedReason` | 失败原因 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_ItemOperationDelegate`

```text
UGC_ItemOperationDelegate(DefineID: const FItemDefineID&, OperationType: EBattleItemOperationType, Reason: uint8) -> void
```

Delegate
	  生效范围SC
	  物品操作时通知

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `const FItemDefineID&` | 物品DefineID |
| `OperationType` | `EBattleItemOperationType` | 操作类型 |
| `Reason` | `uint8` | 操作原因 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_ItemBeforeRemovedDelegate`

```text
UGC_ItemBeforeRemovedDelegate(DefineID: const FItemDefineID&) -> void
```

Delegate
	  生效范围S
	  物品被移除前通知

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `const FItemDefineID&` | 物品DefineID |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_CapacityUpdatedDelegate`

```text
UGC_CapacityUpdatedDelegate() -> void
```

Delegate
	  生效范围SC
	  背包最大容量变化时通知

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBackpackComponentV2.json -->

# UBackpackComponentV2

V2背包内核组件

## Inheritance

`UCommonBackpackComponent` -> `IUGCItemContainerInterface` -> `IUGCItemEquipTargetInterface` -> `IUGCGamePartPlayerComponentInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Warehouse` | `UUGCItemWarehouse_Backpack *` | 仓库对象<br>	  基类：UUGCItemWarehouseBase |

## Functions

### `RemoveItemNewFlag`

```text
RemoveItemNewFlag(DefineID: FItemDefineID &) -> void
```

移除物品新标记
	  DS、Client 可调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `FItemDefineID &` | 物品实例ID |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableItemNewFlag`

```text
EnableItemNewFlag() -> void
```

激活物品新标记
	  DS、Client 可调用

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableItemNewFlag`

```text
DisableItemNewFlag(bForever: bool) -> void
```

失效物品新标记
	  DS、Client 可调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bForever` | `bool` | 是否永久失效 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetItemIsNew`

```text
GetItemIsNew(DefineID: FItemDefineID &) -> bool
```

获取物品是否新标记
	  Client 可调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `FItemDefineID &` | 物品实例ID |

**Returns**

| Type | Description |
|---|---|
| `bool` | 物品是否有新标记 |

### `CheckInitPersistCompleted`

```text
CheckInitPersistCompleted() -> bool
```

查询背包是否初始化完成，完成后才可以进行背包操作

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Events

### `CanAddItemV2`

```text
CanAddItemV2(ItemID: int32, Count: int32) -> int32
```

能否添加物品，能添加多少物品
	  可重载并自定义
	  DS 被调用
	  
	  能通过此事件，决定调用 AddItemV2 时，允许添加多少物品。
	  即使此事件允许添加物品，也可能因为其它限制因素导致物品添加数量减少或添加失败。
	  部分强制添加物品的情形，会跳过此事件。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `int32` | 物品ID |
| `Count` | `int32` | 需要添加的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `int32` | 允许添加的物品数量，如果等于 Count 表示允许添加所有需要的物品 |

### `CanAddItemByDefineIDV2`

```text
CanAddItemByDefineIDV2(DefineID: FItemDefineID &, Count: int32) -> int32
```

能否添加物品，能添加多少物品
	  可重载并自定义
	  DS 被调用
	  
	  能通过此事件，决定添加某个实例物品时，允许添加多少物品。
	  此接口针对具体实例，调用AddItemV2、调用AddItemByDefineIDV2、物品转移等情形都可能触发此事件。
	  单次调用 AddItemV2 可能触发多次针对不同实例的 CanAddItemByDefineIDV2 判断。
	  即使此事件允许添加物品，也可能因为其它限制因素导致物品添加数量减少或添加失败。
	  部分强制添加物品的情形，会跳过此事件。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `FItemDefineID &` | - |
| `Count` | `int32` | 需要添加的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `int32` | 允许添加的物品数量，如果等于 Count 表示允许添加所有需要的物品 |

### `OnAddItemV2`

```text
OnAddItemV2(ItemDefineID: FItemDefineID &, Count: int32) -> void
```

当添加物品实例后回调
	  可重载并自定义
	  DS 被调用
	  
	  当物品实例被成功添加时触发此事件。
	  单次 AddItemV2 可能触发多次针对不同实例的 OnAddItem 调用（生成多个堆叠的情况）。
	  如果物品触发了自动装备，可能装备相关事件会先于 OnAddItemV2 被触发。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID |
| `Count` | `int32` | 已添加的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanMergeItemV2`

```text
CanMergeItemV2(ItemDefineID: FItemDefineID &, CountNow: int32, MergeCount: int32) -> int32
```

能否合并物品(将新增的物品叠加到已有格子上)
	  可重载并自定义
	  DS 被调用
	  
	  能通过此事件，决定多少物品能堆叠到已有堆叠（ItemDefineID）上。
	  此接口针对具体实例，调用AddItemV2、调用AddItemByDefineIDV2、物品转移等情形都可能触发此事件。
	  单次 AddItemV2 可能触发多次针对不同实例的 CanMergeItem 判断（向多个堆叠合并时）。
	  即使此事件允许堆叠物品，也可能因为其它限制因素导致物品堆叠数量减少或堆叠失败。
	  部分情形下会跳过此事件。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID |
| `CountNow` | `int32` | 当前实例的物品数量 |
| `MergeCount` | `int32` | 即将合并到此实例，新增的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `int32` | 允许合并到格子的物品数量，如果等于 Count 表示允许合并所有需要的物品 |

### `OnMergeItemV2`

```text
OnMergeItemV2(ItemDefineID: FItemDefineID &, OldCount: int32, MergeCount: int32) -> void
```

当合并物品后回调(将新增的物品叠加到已有格子上)
	  可重载并自定义
	  DS 被调用
	  
	  此接口针对具体实例，调用AddItemV2、调用AddItemByDefineIDV2、物品转移等情形都可能触发此事件。
	  单次 AddItemV2 可能触发多次针对不同实例的 OnMergeItemV2 事件（向多个堆叠合并时）。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID |
| `OldCount` | `int32` | 合并前的物品数量 |
| `MergeCount` | `int32` | 此次合并操作新增的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanRemoveItemV2`

```text
CanRemoveItemV2(ItemDefineID: FItemDefineID &, Count: int32) -> int32
```

能否移除物品，能移除多少物品
	  可重载并自定义
	  DS、Client 被调用
	  
	  能通过此事件，决定多少物品能被移除。
	  此接口针对具体实例，调用RemoveItemV2、调用RemoveItemByDefineIDV2、物品转移等情形都可能触发此事件。
	  单次 RemoveItemV2 可能触发多次针对不同实例的 CanRemoveItemV2 判断（单个堆叠数量不足时）。
	  即使此事件允许移除物品，也可能因为其它限制因素导致移除数量减少或移除失败。
	  部分情形下会跳过此事件。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID |
| `Count` | `int32` | 需要移除的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `int32` | 允许移除的物品数量，如果等于 Count 表示允许移除所有需要的物品 |

### `OnRemoveItemV2`

```text
OnRemoveItemV2(ItemDefineID: FItemDefineID &, Count: int32) -> void
```

当移除物品后回调
	  可重载并自定义
	  DS 被调用
	  
	  此接口针对具体实例，调用RemoveItemV2、调用RemoveItemByDefineIDV2、物品转移等情形都可能触发此事件。
	  单次 RemoveItemV2 可能触发多次针对不同实例的 OnRemoveItemV2 事件（单个堆叠数量不足时）。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID，移除后可能已不存在于背包 |
| `Count` | `int32` | 已移除的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanDropItemV2`

```text
CanDropItemV2(ItemDefineID: FItemDefineID &, Count: int32) -> int32
```

能否丢弃物品，能丢弃多少物品
	  可重载并自定义
	  DS、Client 被调用
	  
	  能通过此事件，决定多少物品能被丢弃。
	  此接口针对具体实例，调用DropItemV2、调用DropItemByDefineIDV2等情形都可能触发此事件。
	  单次 调用 DropItemV2 可能触发多次针对不同实例的 CanDropItemV2 判断（单个堆叠数量不足时）。
	  即使此事件允许丢弃物品，也可能因为其它限制因素导致丢弃数量减少或丢弃失败。
	  部分情形下会跳过此事件。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID |
| `Count` | `int32` | 需要丢弃的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `int32` | 允许丢弃的物品数量，如果等于 Count 表示允许丢弃所有需要的物品 |

### `OnDropItemV2`

```text
OnDropItemV2(ItemDefineID: FItemDefineID &, Count: int32) -> void
```

当丢弃物品后回调
	  可重载并自定义
	  DS 被调用
	  
	  当物品被成功丢弃时，触发此事件。
	  此接口针对具体实例，调用DropItemV2、调用DropItemByDefineIDV2等情形都可能触发此事件。
	  单次 DropItemV2 可能触发多次针对不同实例的 OnDropItemV2 事件（单个堆叠数量不足时）。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID，丢弃后可能已不存在于背包 |
| `Count` | `int32` | 已丢弃的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanUseItemV2`

```text
CanUseItemV2(ItemDefineID: FItemDefineID &) -> bool
```

能否使用物品
	  可重载并自定义
	  DS、Client 被调用
	  
	  DS 触发使用物品时，会触发并判断能否使用。
	  即使此事件允许使用物品，也可能因为其它限制因素导致使用失败。
	  部分情形下会跳过此事件。
	  
	  Client 背包UI选中物品时，会触发并判断是否显示使用按钮。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID |

**Returns**

| Type | Description |
|---|---|
| `bool` | 物品是否能够被使用 |

### `OnUseItemV2`

```text
OnUseItemV2(ItemDefineID: FItemDefineID &) -> void
```

当物品触发使用后回调
	  可重载并自定义
	  DS 被调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnDisuseItemV2`

```text
OnDisuseItemV2(ItemDefineID: FItemDefineID &) -> void
```

当物品触发 DisUseItem 完成后回调
	  可重载并自定义
	  DS 被调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 物品DefineID |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanAttachToSlot_Implementation`

```text
CanAttachToSlot_Implementation(SlotName: FName &, ItemDefineID: FItemDefineID &) -> bool
```

其它物品是否能装备到此槽位
	  当物品尝试装备在背包槽位时触发
	  
	  DS 被调用
	  
	  开发者能通过此事件，决定调用 EquipItemV2 时，是否允许装备。
	  即使此事件允许装备物品，也可能因为其它限制因素导致物品装备失败。
	  部分强制装备物品的情形，会跳过此事件。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotName` | `FName &` | 槽位名称 |
| `ItemDefineID` | `FItemDefineID &` | 即将装备在此槽位的物品 |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `OnAttachToSlot_Implementation`

```text
OnAttachToSlot_Implementation(SlotName: FName &, ItemDefineID: FItemDefineID &) -> void
```

当其它物品装备到此槽位
	  当物品成功装备在背包槽位时触发
	  
	  DS 被调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotName` | `FName &` | 槽位名称 |
| `ItemDefineID` | `FItemDefineID &` | 已装备在此槽位的物品 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnDetachBySlot_Implementation`

```text
OnDetachBySlot_Implementation(SlotName: FName &, ItemDefineID: FItemDefineID &) -> void
```

当物品成功从背包槽位卸下时触发
	  
	  DS 被调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotName` | `FName &` | 槽位名称 |
| `ItemDefineID` | `FItemDefineID &` | 已从此槽位卸下的物品 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanAutoEquip`

```text
CanAutoEquip(ItemDefineID: FItemDefineID &) -> bool
```

物品能否自动装备
	  当配置了自动装备的物品尝试自动装备时触发
	 
	  DS 被调用
	 
	  开发者能通过此事件，阻止物品自动装备到背包或Attach到其它物品上。
	  手动装备或主动调用装备时，不受此函数影响。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 即将装备在此槽位的物品 |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `HandleExceedCellCapacity`

```text
HandleExceedCellCapacity(ItemDefineID: FItemDefineID &, Count: int32) -> void
```

处理超过格子容量的物品
	  普通情况下，背包内容量已满时，无法添加物品。
	  但存在特殊情况，背包满容量时依然成功添加物品、原本不占格子的物品变为占用格子、背包容量发生变化。
	  超容量物品会被直接移除，移除后在此函数处理保底逻辑
	  默认保底逻辑为丢弃到地上
	  重写此事件时，请不要将超容量物品在此处重新添加到背包里
	  
	  可重载并自定义
	  DS 被调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID &` | 超过容量的物品ID |
| `Count` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnCellCapacityChange`

```text
OnCellCapacityChange(NewCapacity: const int32&) -> void
```

当背包格子容量改变时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewCapacity` | `const int32&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMaxCellCapacityChange`

```text
OnMaxCellCapacityChange(NewCapacity: const int32&) -> void
```

当背包格子容量上限改变时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewCapacity` | `const int32&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWarehouseCellCapacityChange`

```text
OnWarehouseCellCapacityChange(NewCapacity: const int32&) -> void
```

当仓库格子容量改变时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewCapacity` | `const int32&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemUsingStateDelegateV2`

```text
ItemUsingStateDelegateV2(ItemDefineID: FItemDefineID, bUse: bool) -> void
```

背包物品使用状态变化时广播
	  广播范围: 服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `FItemDefineID` | 物品DefefineID |
| `bUse` | `bool` | true:开始使用,false:停止使用 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemChangeDelegateV2`

```text
ItemChangeDelegateV2(ChangeType: const EUGCItemChangeType&, DefineID: const FItemDefineID&) -> void
```

当物品实例数据发生改变时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ChangeType` | `const EUGCItemChangeType&` | - |
| `DefineID` | `const FItemDefineID&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemAddDelegateV2`

```text
ItemAddDelegateV2(DefineID: const FItemDefineID&) -> void
```

当新增物品实例时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `const FItemDefineID&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemUpdateDelegateV2`

```text
ItemUpdateDelegateV2(DefineID: const FItemDefineID&) -> void
```

当物品实例数据更新时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `const FItemDefineID&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemRemoveDelegateV2`

```text
ItemRemoveDelegateV2(DefineID: const FItemDefineID&) -> void
```

当移除物品实例时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `const FItemDefineID&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemInstanceDataChangeV2`

```text
ItemInstanceDataChangeV2() -> void
```

当背包物品实例化数据发生改变时广播
	  广播范围：客户端

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemAttachParentChangeDelegateV2`

```text
ItemAttachParentChangeDelegateV2(ItemDefineID: const FItemDefineID&, OldAttachItem: const FItemDefineID&, OldAttachSlotName: const FName&, NewAttachItem: const FItemDefineID&, NewAttachSlotName: const FName&) -> void
```

当物品附加的Parent发生改变时广播
	  广播范围：服务端 & 客户端
	  
	  ItemDefineID: 哪个物品的 Parent 发生了改变
	  OldAttachItem: 改变之前物品的 Parent
	  OldAttachSlotName: 改变之前物品所在的槽位
	  NewAttachItem: 改变之后物品的 Parent
	  NewAttachSlotName: 改变之后物品所在的槽位
	  如果物品是直接装备在背包上，AttachItem 将为空物品 ( TypeSpecificID 为 0 ) ，AttachSlotName 为背包槽位名称。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `const FItemDefineID&` | - |
| `OldAttachItem` | `const FItemDefineID&` | - |
| `OldAttachSlotName` | `const FName&` | - |
| `NewAttachItem` | `const FItemDefineID&` | - |
| `NewAttachSlotName` | `const FName&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemOperationInfoDelegateV2`

```text
ItemOperationInfoDelegateV2(ItemOperationInfo: FItemOperationInfoV2 const&) -> void
```

当对物品操作成功后广播
	  广播范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemOperationInfo` | `FItemOperationInfoV2 const&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBaseMediaSource.json -->

# UBaseMediaSource

Base class for concrete media sources.

## Inheritance

`UMediaSource`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PlayerName` | `FName` | Name of the desired native media player (Empty = find one automatically). |
| `PlatformPlayerNames` | `TMap < FString , FName >` | Override native media player plug-ins per platform (Empty = find one automatically). |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBasicOverlays.json -->

# UBasicOverlays

Implements an asset that contains a set of overlay data (which includes timing, text, and position) to be displayed for any
  given source (including, but not limited to, audio, dialog, and movies)

## Inheritance

`UOverlays`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Overlays` | `TArray < FOverlayItem >` | The overlay data held by this asset. Contains info on timing, position, and the subtitle to display |
| `AssetImportData` | `UAssetImportData *` | The import data used to make this overlays asset |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBehaviorTree.json -->

# UBehaviorTree

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RootNode` | `UBTCompositeNode *` | root node of loaded tree |
| `BlackboardAsset` | `UBlackboardData *` | blackboard asset for this tree |
| `RootDecorators` | `TArray < UBTDecorator * >` | root level decorators, used by subtrees |
| `RootDecoratorOps` | `TArray < FBTDecoratorLogic >` | logic operators for root level decorators, used by subtrees |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBehaviorTreeComponent.json -->

# UBehaviorTreeComponent

## Inheritance

`UBrainComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NodeInstances` | `TArray < UBTNode * >` | instanced nodes |

## Functions

### `GetTagCooldownEndTime`

```text
GetTagCooldownEndTime(CooldownTag: FGameplayTag) -> float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CooldownTag` | `FGameplayTag` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | the cooldown tag end time, 0.0f if CooldownTag is not found |

### `AddCooldownTagDuration`

```text
AddCooldownTagDuration(CooldownTag: FGameplayTag, CooldownDuration: float, bAddToExistingDuration: bool) -> void
```

add to the cooldown tag's duration

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CooldownTag` | `FGameplayTag` | - |
| `CooldownDuration` | `float` | - |
| `bAddToExistingDuration` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDynamicSubtree`

```text
SetDynamicSubtree(InjectTag: FGameplayTag, BehaviorAsset: UBehaviorTree *) -> void
```

assign subtree to RunBehaviorDynamic task specified by tag

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InjectTag` | `FGameplayTag` | - |
| `BehaviorAsset` | `UBehaviorTree *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetUGCMobBTDebugInfo`

```text
GetUGCMobBTDebugInfo(OutTreeInfo: FUGCMobBTDebugInfo &, OutBlackBoardInfo: TArray < FUGCMobBTBlackBoardInfo > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutTreeInfo` | `FUGCMobBTDebugInfo &` | - |
| `OutBlackBoardInfo` | `TArray < FUGCMobBTBlackBoardInfo > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBehaviorTreeManager.json -->

# UBehaviorTreeManager

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaxDebuggerSteps` | `int32` | limit for recording execution steps for debugger |
| `LoadedTemplates` | `TArray < FBehaviorTreeTemplateInfo >` | initialized tree templates |
| `ActiveComponents` | `TArray < UBehaviorTreeComponent * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBillboardComponent.json -->

# UBillboardComponent

A 2d texture that will be rendered always facing the camera.

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sprite` | `UTexture2D *` | - |
| `bIsScreenSizeScaled` | `uint32` | - |
| `ScreenSize` | `float` | - |
| `U` | `float` | - |
| `UL` | `float` | - |
| `V` | `float` | - |
| `VL` | `float` | - |
| `SpriteCategoryName_DEPRECATED` | `FName` | Sprite category that the component belongs to. Value serves as a key into the localization file. |
| `SpriteInfo` | `FSpriteCategoryInfo` | Sprite category information regarding the component |
| `bUseInEditorScaling` | `bool` | Whether to use in-editor arrow scaling (i.e. to be affected by the global arrow scale) |

## Functions

### `SetSprite`

```text
SetSprite(NewSprite: UTexture2D *) -> void
```

Change the sprite texture used by this component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewSprite` | `UTexture2D *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetUV`

```text
SetUV(NewU: int32, NewUL: int32, NewV: int32, NewVL: int32) -> void
```

Change the sprite's UVs

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewU` | `int32` | - |
| `NewUL` | `int32` | - |
| `NewV` | `int32` | - |
| `NewVL` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSpriteAndUV`

```text
SetSpriteAndUV(NewSprite: UTexture2D *, NewU: int32, NewUL: int32, NewV: int32, NewVL: int32) -> void
```

Change the sprite texture and the UV's used by this component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewSprite` | `UTexture2D *` | - |
| `NewU` | `int32` | - |
| `NewUL` | `int32` | - |
| `NewV` | `int32` | - |
| `NewVL` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlackboardComponent.json -->

# UBlackboardComponent

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BrainComp` | `UBrainComponent *` | cached behavior tree component |
| `BlackboardAsset` | `UBlackboardData *` | data asset defining entries |
| `KeyInstances` | `TArray < UBlackboardKeyType * >` | instanced keys with custom data allocations |

## Functions

### `GetValueAsObject`

```text
GetValueAsObject(KeyName: FName &) -> UObject *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

### `GetValueAsClass`

```text
GetValueAsClass(KeyName: FName &) -> UClass *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `UClass *` | - |

### `GetValueAsEnum`

```text
GetValueAsEnum(KeyName: FName &) -> uint8
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `uint8` | - |

### `GetValueAsInt`

```text
GetValueAsInt(KeyName: FName &) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetValueAsFloat`

```text
GetValueAsFloat(KeyName: FName &) -> float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetValueAsBool`

```text
GetValueAsBool(KeyName: FName &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetValueAsString`

```text
GetValueAsString(KeyName: FName &) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetValueAsName`

```text
GetValueAsName(KeyName: FName &) -> FName
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `GetValueAsVector`

```text
GetValueAsVector(KeyName: FName &) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetValueAsRotator`

```text
GetValueAsRotator(KeyName: FName &) -> FRotator
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `SetValueAsObject`

```text
SetValueAsObject(KeyName: FName &, ObjectValue: UObject *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `ObjectValue` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetValueAsClass`

```text
SetValueAsClass(KeyName: FName &, ClassValue: UClass *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `ClassValue` | `UClass *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetValueAsEnum`

```text
SetValueAsEnum(KeyName: FName &, EnumValue: uint8) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `EnumValue` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetValueAsInt`

```text
SetValueAsInt(KeyName: FName &, IntValue: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `IntValue` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetValueAsFloat`

```text
SetValueAsFloat(KeyName: FName &, FloatValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `FloatValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetValueAsBool`

```text
SetValueAsBool(KeyName: FName &, BoolValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `BoolValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetValueAsString`

```text
SetValueAsString(KeyName: FName &, StringValue: FString) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `StringValue` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetValueAsName`

```text
SetValueAsName(KeyName: FName &, NameValue: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `NameValue` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetValueAsVector`

```text
SetValueAsVector(KeyName: FName &, VectorValue: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `VectorValue` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetValueAsRotator`

```text
SetValueAsRotator(KeyName: FName &, VectorValue: FRotator) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `VectorValue` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsVectorValueSet`

```text
IsVectorValueSet(KeyName: FName &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetLocationFromEntry`

```text
GetLocationFromEntry(KeyName: FName &, ResultLocation: FVector &) -> bool
```

return false if call failed (most probably no such entry in BB)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `ResultLocation` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetRotationFromEntry`

```text
GetRotationFromEntry(KeyName: FName &, ResultRotation: FRotator &) -> bool
```

return false if call failed (most probably no such entry in BB)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `ResultRotation` | `FRotator &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ClearValue`

```text
ClearValue(KeyName: FName &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlackboardData.json -->

# UBlackboardData

## Inheritance

`UDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Parent` | `UBlackboardData *` | parent blackboard (keys can be overridden) |
| `Keys` | `TArray < FBlackboardEntry >` | blackboard keys |
| `bHasSynchronizedKeys` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlackboardKeyType_Class.json -->

# UBlackboardKeyType_Class

## Inheritance

`UBlackboardKeyType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BaseClass` | `UClass *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlackboardKeyType_Enum.json -->

# UBlackboardKeyType_Enum

## Inheritance

`UBlackboardKeyType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EnumType` | `UEnum *` | - |
| `EnumName` | `FString` | name of enum defined in c++ code, will take priority over asset from EnumType property |
| `bIsEnumNameValid` | `uint32` | set when EnumName override is valid and active |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlackboardKeyType_NativeEnum.json -->

# UBlackboardKeyType_NativeEnum

## Inheritance

`UBlackboardKeyType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EnumName` | `FString` | - |
| `EnumType` | `UEnum *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlackboardKeyType_Object.json -->

# UBlackboardKeyType_Object

## Inheritance

`UBlackboardKeyType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BaseClass` | `UClass *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlackboardKeyType_String.json -->

# UBlackboardKeyType_String

## Inheritance

`UBlackboardKeyType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StringValue` | `FString` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlendProfile.json -->

# UBlendProfile

A blend profile is a set of per-bone scales that can be used in transitions and blend lists
   to tweak the weights of specific bones. The scales are applied to the normal weight for that bone

## Inheritance

`UObject` -> `IInterpolationIndexProvider`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OwningSkeleton` | `USkeleton *` | - |
| `ProfileEntries` | `TArray < FBlendProfileBoneEntry >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlendSpace.json -->

# UBlendSpace

Contains a grid of data points with weights from sample points in the space

## Inheritance

`UBlendSpaceBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AxisToScaleAnimation` | `TEnumAsByte < EBlendSpaceAxis >` | If you have input interpolation, which axis to drive animation speed (scale) - i.e. for locomotion animation, speed axis will drive animation speed (thus scale) |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlendSpace1D.json -->

# UBlendSpace1D

## Inheritance

`UBlendSpaceBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bScaleAnimation` | `bool` | Drive animation speed by blend input position |
| `bDisplayEditorVertically_DEPRECATED` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlendSpaceBase.json -->

# UBlendSpaceBase

Allows multiple animations to be blended between based on input parameters

## Inheritance

`UAnimationAsset` -> `IInterpolationIndexProvider`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bRotationBlendInMeshSpace` | `bool` | When you use blend per bone, allows rotation to blend in mesh space. This only works if this does not contain additive animation samples<br>	 This is more performance intensive |
| `AnimLength` | `float` | This animation length changes based on current input (resulting in different blend time) |
| `InterpolationParam` | `FInterpolationParameter` | Input interpolation parameter for all 3 axis, for each axis input, decide how you'd like to interpolate input to |
| `TargetWeightInterpolationSpeedPerSec` | `float` | Target weight interpolation. When target samples are set, how fast you'd like to get to target. Improve target blending.<br>	 i.e. for locomotion, if you interpolate input, when you move from left to right rapidly, you'll interpolate through forward, but if you use target weight interpolation,<br>	 you'll skip forward, but interpolate between left to right |
| `NotifyTriggerMode` | `TEnumAsByte < ENotifyTriggerMode :: Type >` | The current mode used by the blendspace to decide which animation notifies to fire. Valid options are: |
| `PerBoneBlend` | `TArray < FPerBoneInterpolation >` | Define target weight interpolation per bone. This will blend in different speed per each bone setting |
| `SampleIndexWithMarkers` | `int32` | Track index to get marker data from. Samples are tested for the suitability of marker based sync<br>	    during load and if we can use marker based sync we cache an index to a representative sample here |
| `SampleData` | `TArray < struct FBlendSample >` | Sample animation data |
| `GridSamples` | `TArray < struct FEditorElement >` | Grid samples, indexing scheme imposed by subclass |
| `BlendParameters` | `FBlendParameter` | Blend Parameters for each axis. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlueprint.json -->

# UBlueprint

Blueprints are special assets that provide an intuitive, node-based interface that can be used to create new types of Actors
  and script level events; giving designers and gameplay programmers the tools to quickly create and iterate gameplay from
  within Unreal Editor without ever needing to write a line of code.

## Inheritance

`UBlueprintCore`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bRecompileOnLoad` | `uint32` | Whether or not this blueprint should recompile itself on load |
| `ParentClass` | `TSubclassOf < UObject >` | Pointer to the parent class that the generated class should derive from. This can be null under rare circumstances, |
| `PRIVATE_InnermostPreviousCDO` | `UObject *` | - |
| `bHasBeenRegenerated` | `uint32` | When the class generated by this blueprint is loaded, it will be recompiled the first time.  After that initial recompile, subsequent loads will skip the regeneration step |
| `bIsRegeneratingOnLoad` | `uint32` | State flag to indicate whether or not the Blueprint is currently being regenerated on load |
| `SimpleConstructionScript` | `USimpleConstructionScript *` | 'Simple' construction script - graph of components to instance |
| `ComponentTemplates` | `TArray < UActorComponent * >` | Array of component template objects, used by AddComponent function |
| `Timelines` | `TArray < UTimelineTemplate * >` | Array of templates for timelines that should be created |
| `InheritableComponentHandler` | `UInheritableComponentHandler *` | Stores data to override (in children classes) components (created by SCS) from parent classes |
| `BlueprintType` | `TEnumAsByte < enum EBlueprintType >` | The type of this blueprint |
| `BlueprintSystemVersion` | `int32` | The version of the blueprint system that was used to  create this blueprint |
| `bNativize_DEPRECATED` | `bool` | Deprecated properties. |
| `bIsNewlyCreated` | `uint32` | Whether or not this blueprint is newly created, and hasn't been opened in an editor yet |
| `bForceFullEditor` | `uint32` | Whether to force opening the full (non data-only) editor for this blueprint. |
| `bQueuedForCompilation` | `uint32` | - |
| `bRunConstructionScriptOnDrag` | `uint32` | whether or not you want to continuously rerun the construction script for an actor as you drag it in the editor, or only when the drag operation is complete |
| `bRunConstructionScriptInSequencer` | `uint32` | whether or not you want to continuously rerun the construction script for an actor in sequencer |
| `bGenerateConstClass` | `uint32` | Whether or not this blueprint's class is a const class or not.  Should set CLASS_Const in the KismetCompiler. |
| `bGenerateAbstractClass` | `uint32` | Whether or not this blueprint's class is a abstract class or not.  Should set CLASS_Abstract in the KismetCompiler. |
| `BlueprintDescription` | `FString` | shows up in the content browser when the blueprint is hovered |
| `BlueprintCategory` | `FString` | The category of the Blueprint, used to organize this Blueprint class when displayed in palette windows |
| `HideCategories` | `TArray < FString >` | Additional HideCategories. These are added to HideCategories from parent. |
| `NativizationFlag` | `EBlueprintNativizationFlag` | When exclusive nativization is enabled, then this asset will be nativized. All super classes must be also nativized. |
| `bDisplayCompilePIEWarning` | `bool` | TRUE to show a warning when attempting to start in PIE and there is a compiler error on this Blueprint |
| `SearchGuid` | `FGuid` | Guid key for finding searchable data for Blueprint in the DDC |
| `bDeprecate` | `bool` | Deprecates the Blueprint, marking the generated class with the CLASS_Deprecated flag |
| `CompileMode` | `EBlueprintCompileMode` | The mode that will be used when compiling this class. |
| `UbergraphPages` | `TArray < UEdGraph * >` | Set of pages that combine into a single uber-graph |
| `FunctionGraphs` | `TArray < UEdGraph * >` | Set of functions implemented for this class graphically |
| `DelegateSignatureGraphs` | `TArray < UEdGraph * >` | Graphs of signatures for delegates |
| `MacroGraphs` | `TArray < UEdGraph * >` | Set of macros implemented for this class |
| `IntermediateGeneratedGraphs` | `TArray < UEdGraph * >` | Set of functions actually compiled for this class |
| `EventGraphs` | `TArray < UEdGraph * >` | Set of functions actually compiled for this class |
| `PRIVATE_CachedMacroInfo` | `TMap < UEdGraph * , FBlueprintMacroCosmeticInfo >` | Cached cosmetic information about macro graphs, use GetCosmeticInfoForMacro() to access |
| `bDuplicatingReadOnly` | `bool` | Flag indicating that a read only duplicate of this blueprint is being created, used to disable logic in ::PostDuplicate,<br>	 <br>	  This flag needs to be copied on duplication (because it's the duplicated object that we're disabling on PostDuplicate),<br>	  but we don't need to serialize it for permanent objects.<br>	 <br>	  Without setting this flag a blueprint will be marked dirty when it is duplicated and if saved while in this dirty<br>	  state you will not be able to open the blueprint. More specifically, UClass::Rename (called by DestroyGeneratedClass)<br>	  sets a dirty flag on the package. Once saved the package will fail to open because some unnamed objects are present in<br>	  the pacakge.<br>	 <br>	  This flag can be used to avoid the package being marked as dirty in the first place. Ideally PostDuplicateObject<br>	  would not rename classes that are still in use by the original object. |
| `Status` | `TEnumAsByte < enum EBlueprintStatus >` | The current status of this blueprint |
| `NewVariables` | `TArray < struct FBPVariableDescription >` | Array of new variables to be added to generated class |
| `CategorySorting` | `TArray < FName >` | Array of user sorted categories |
| `ImplementedInterfaces` | `TArray < struct FBPInterfaceDescription >` | Array of info about the interfaces we implement in this blueprint |
| `LastEditedDocuments` | `TArray < struct FEditedDocumentInfo >` | Set of documents that were being edited in this blueprint, so we can open them right away |
| `Breakpoints` | `TArray < UBreakpoint * >` | Persistent debugging options |
| `WatchedPins` | `TArray < FEdGraphPinReference >` | - |
| `DeprecatedPinWatches` | `TArray < UEdGraphPin_Deprecated * >` | - |
| `ComponentTemplateNameIndex` | `TMap < FName , int32 >` | Index map for component template names |
| `OldToNewComponentTemplateNames` | `TMap < FName , FName >` | Maps old to new component template names |
| `Extensions` | `TArray < UBlueprintExtension * >` | Array of extensions for this blueprint |
| `ThumbnailInfo` | `UThumbnailInfo *` | Information for thumbnail rendering |
| `bBeingCompiled` | `uint32` | The blueprint is currently compiled |
| `CrcLastCompiledCDO` | `uint32` | CRC for CDO calculated right after the latest compilation used by Reinstancer to check if default values were changed |
| `CrcLastCompiledSignature` | `uint32` | - |
| `OriginalClass` | `UClass *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlueprintAsyncActionBase.json -->

# UBlueprintAsyncActionBase

## Inheritance

`UObject`

## Functions

### `Activate`

```text
Activate() -> void
```

Called to trigger the action once the delegates have been bound

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlueprintCore.json -->

# UBlueprintCore

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SkeletonGeneratedClass` | `TSubclassOf < UObject >` | Pointer to the skeleton class; this is regenerated any time a member variable or function is added but  <br>	is usually incomplete (no code or hidden autogenerated variables are added to it) |
| `GeneratedClass` | `TSubclassOf < UObject >` | Pointer to the 'most recent' fully generated class |
| `bLegacyNeedToPurgeSkelRefs` | `bool` | BackCompat:  Whether or not we need to purge references in this blueprint to the skeleton generated during compile-on-load |
| `bLegacyGeneratedClassIsAuthoritative` | `bool` | BackCompat: Whether or not this blueprint's authoritative CDO data has been migrated from the SkeletonGeneratedClass CDO to the GeneratedClass CDO |
| `BlueprintGuid` | `FGuid` | Blueprint Guid |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlueprintGameplayTagLibrary.json -->

# UBlueprintGameplayTagLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `MatchesTag`

```text
MatchesTag(TagOne: FGameplayTag, TagTwo: FGameplayTag, bExactMatch: bool) -> bool
```

Determine if TagOne matches against TagTwo

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagOne` | `FGameplayTag` | Tag to check for match |
| `TagTwo` | `FGameplayTag` | Tag to check match against |
| `bExactMatch` | `bool` | If true, the tag has to be exactly present, if false then TagOne will include it's parent tags while matching |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if TagOne matches TagTwo |

### `MatchesAnyTags`

```text
MatchesAnyTags(TagOne: FGameplayTag, OtherContainer: FGameplayTagContainer &, bExactMatch: bool) -> GAMEPLAYTAGS_API bool
```

Determine if TagOne matches against any tag in OtherContainer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagOne` | `FGameplayTag` | Tag to check for match |
| `OtherContainer` | `FGameplayTagContainer &` | Container to check against. |
| `bExactMatch` | `bool` | If true, the tag has to be exactly present, if false then TagOne will include it's parent tags while matching |

**Returns**

| Type | Description |
|---|---|
| `GAMEPLAYTAGS_API bool` | True if TagOne matches any tags explicitly present in OtherContainer |

### `EqualEqual_GameplayTag`

```text
EqualEqual_GameplayTag(A: FGameplayTag, B: FGameplayTag) -> bool
```

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FGameplayTag` | - |
| `B` | `FGameplayTag` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_GameplayTag`

```text
NotEqual_GameplayTag(A: FGameplayTag, B: FGameplayTag) -> bool
```

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FGameplayTag` | - |
| `B` | `FGameplayTag` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsGameplayTagValid`

```text
IsGameplayTagValid(GameplayTag: FGameplayTag) -> bool
```

Returns true if the passed in gameplay tag is non-null

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GameplayTag` | `FGameplayTag` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetTagName`

```text
GetTagName(GameplayTag: FGameplayTag &) -> FName
```

Returns FName of this tag

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GameplayTag` | `FGameplayTag &` | - |

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `MakeLiteralGameplayTag`

```text
MakeLiteralGameplayTag(Value: FGameplayTag) -> FGameplayTag
```

Creates a literal FGameplayTag

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FGameplayTag` | - |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTag` | - |

### `GetNumGameplayTagsInContainer`

```text
GetNumGameplayTagsInContainer(TagContainer: FGameplayTagContainer &) -> int32
```

Get the number of gameplay tags in the specified container

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer &` | Tag container to get the number of tags from |

**Returns**

| Type | Description |
|---|---|
| `int32` | The number of tags in the specified container |

### `HasTag`

```text
HasTag(TagContainer: FGameplayTagContainer &, Tag: FGameplayTag, bExactMatch: bool) -> bool
```

Check if the tag container has the specified tag

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer &` | Container to check for the tag |
| `Tag` | `FGameplayTag` | Tag to check for in the container |
| `bExactMatch` | `bool` | If true, the tag has to be exactly present, if false then TagContainer will include it's parent tags while matching |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the container has the specified tag, false if it does not |

### `HasAnyTags`

```text
HasAnyTags(TagContainer: FGameplayTagContainer &, OtherContainer: FGameplayTagContainer &, bExactMatch: bool) -> bool
```

Check if the specified tag container has ANY of the tags in the other container

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer &` | Container to check if it matches any of the tags in the other container |
| `OtherContainer` | `FGameplayTagContainer &` | Container to check against. |
| `bExactMatch` | `bool` | If true, the tag has to be exactly present, if false then TagContainer will include it's parent tags while matching |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the container has ANY of the tags in the other container |

### `HasAllTags`

```text
HasAllTags(TagContainer: FGameplayTagContainer &, OtherContainer: FGameplayTagContainer &, bExactMatch: bool) -> bool
```

Check if the specified tag container has ALL of the tags in the other container

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer &` | Container to check if it matches all of the tags in the other container |
| `OtherContainer` | `FGameplayTagContainer &` | Container to check against. If this is empty, the check will succeed |
| `bExactMatch` | `bool` | If true, the tag has to be exactly present, if false then TagContainer will include it's parent tags while matching |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the container has ALL of the tags in the other container |

### `DoesContainerMatchTagQuery`

```text
DoesContainerMatchTagQuery(TagContainer: FGameplayTagContainer &, TagQuery: FGameplayTagQuery &) -> bool
```

Check if the specified tag container matches the given Tag Query

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer &` | Container to check if it matches all of the tags in the other container |
| `TagQuery` | `FGameplayTagQuery &` | Query to match against |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the container matches the query, false otherwise. |

### `GetAllActorsOfClassMatchingTagQuery`

```text
GetAllActorsOfClassMatchingTagQuery(WorldContextObject: UObject *, ActorClass: TSubclassOf < AActor >, GameplayTagQuery: FGameplayTagQuery &, OutActors: TArray < AActor * > &) -> void
```

Get an array of all actors of a specific class (or subclass of that class) which match the specified gameplay tag query.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ActorClass` | `TSubclassOf < AActor >` | Class of actors to fetch |
| `GameplayTagQuery` | `FGameplayTagQuery &` | Query to match against |
| `OutActors` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddGameplayTag`

```text
AddGameplayTag(TagContainer: FGameplayTagContainer &, Tag: FGameplayTag) -> void
```

Adds a single tag to the passed in tag container

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer &` | - |
| `Tag` | `FGameplayTag` | The tag to add to the container |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveGameplayTag`

```text
RemoveGameplayTag(TagContainer: FGameplayTagContainer &, Tag: FGameplayTag) -> bool
```

Remove a single tag from the passed in tag container, returns true if found

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer &` | - |
| `Tag` | `FGameplayTag` | The tag to add to the container |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `AppendGameplayTagContainers`

```text
AppendGameplayTagContainers(InOutTagContainer: FGameplayTagContainer &, InTagContainer: FGameplayTagContainer &) -> void
```

Appends all tags in the InTagContainer to InOutTagContainer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOutTagContainer` | `FGameplayTagContainer &` | The container that will be appended too. |
| `InTagContainer` | `FGameplayTagContainer &` | The container to append. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EqualEqual_GameplayTagContainer`

```text
EqualEqual_GameplayTagContainer(A: FGameplayTagContainer &, B: FGameplayTagContainer &) -> bool
```

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FGameplayTagContainer &` | - |
| `B` | `FGameplayTagContainer &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_GameplayTagContainer`

```text
NotEqual_GameplayTagContainer(A: FGameplayTagContainer &, B: FGameplayTagContainer &) -> bool
```

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FGameplayTagContainer &` | - |
| `B` | `FGameplayTagContainer &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `MakeLiteralGameplayTagContainer`

```text
MakeLiteralGameplayTagContainer(Value: FGameplayTagContainer) -> FGameplayTagContainer
```

Creates a literal FGameplayTagContainer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FGameplayTagContainer` | - |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTagContainer` | - |

### `MakeGameplayTagContainerFromArray`

```text
MakeGameplayTagContainerFromArray(GameplayTags: TArray < FGameplayTag > &) -> FGameplayTagContainer
```

Creates a FGameplayTagContainer from the array of passed in tags

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GameplayTags` | `TArray < FGameplayTag > &` | - |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTagContainer` | - |

### `MakeGameplayTagContainerFromTag`

```text
MakeGameplayTagContainerFromTag(SingleTag: FGameplayTag) -> FGameplayTagContainer
```

Creates a FGameplayTagContainer containing a single tag

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SingleTag` | `FGameplayTag` | - |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTagContainer` | - |

### `BreakGameplayTagContainer`

```text
BreakGameplayTagContainer(GameplayTagContainer: FGameplayTagContainer &, GameplayTags: TArray < FGameplayTag > &) -> void
```

Breaks tag container into explicit array of tags

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GameplayTagContainer` | `FGameplayTagContainer &` | - |
| `GameplayTags` | `TArray < FGameplayTag > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MakeGameplayTagQuery`

```text
MakeGameplayTagQuery(TagQuery: FGameplayTagQuery) -> FGameplayTagQuery
```

Creates a literal FGameplayTagQuery

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagQuery` | `FGameplayTagQuery` | value to set the FGameplayTagQuery to |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTagQuery` | The literal FGameplayTagQuery |

### `HasAllMatchingGameplayTags`

```text
HasAllMatchingGameplayTags(TagContainerInterface: TScriptInterface < IGameplayTagAssetInterface >, OtherContainer: FGameplayTagContainer &) -> bool
```

Check Gameplay tags in the interface has all of the specified tags in the tag container (expands to include parents of asset tags)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainerInterface` | `TScriptInterface < IGameplayTagAssetInterface >` | An Interface to a tag container |
| `OtherContainer` | `FGameplayTagContainer &` | A Tag Container |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the tagcontainer in the interface has all the tags inside the container. |

### `DoesTagAssetInterfaceHaveTag`

```text
DoesTagAssetInterfaceHaveTag(TagContainerInterface: TScriptInterface < IGameplayTagAssetInterface >, Tag: FGameplayTag) -> bool
```

Check if the specified tag container has the specified tag, using the specified tag matching types

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainerInterface` | `TScriptInterface < IGameplayTagAssetInterface >` | An Interface to a tag container |
| `Tag` | `FGameplayTag` | Tag to check for in the container |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the container has the specified tag, false if it does not |

### `NotEqual_TagTag`

```text
NotEqual_TagTag(A: FGameplayTag, B: FString) -> bool
```

Checks if a gameplay tag's name and a string are not equal to one another

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FGameplayTag` | - |
| `B` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_TagContainerTagContainer`

```text
NotEqual_TagContainerTagContainer(A: FGameplayTagContainer, B: FString) -> bool
```

Checks if a gameplay tag containers's name and a string are not equal to one another

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FGameplayTagContainer` | - |
| `B` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetDebugStringFromGameplayTagContainer`

```text
GetDebugStringFromGameplayTagContainer(TagContainer: FGameplayTagContainer &) -> FString
```

Returns an FString listing all of the gameplay tags in the tag container for debugging purposes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer &` | The tag container to get the debug string from. |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetDebugStringFromGameplayTag`

```text
GetDebugStringFromGameplayTag(GameplayTag: FGameplayTag) -> FString
```

Returns an FString representation of a gameplay tag for debugging purposes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GameplayTag` | `FGameplayTag` | The tag to get the debug string from. |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlueprintMapLibrary.json -->

# UBlueprintMapLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `Map_Add`

```text
Map_Add(TargetMap: TMap < int32 , int32 > &, Key: int32 &, Value: int32 &) -> void
```

Adds a key and value to the map. If something already uses the provided key it will be overwritten with the new value.
	  After calling Key is guaranteed to be associated with Value until a subsequent mutation of the Map.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetMap` | `TMap < int32 , int32 > &` | The map to add the key and value to |
| `Key` | `int32 &` | The key that will be used to look the value up |
| `Value` | `int32 &` | The value to be retrieved later |

**Returns**

| Type | Description |
|---|---|
| `void` | True if a Value was added, or False if the Key was already present and has been overwritten |

### `Map_Remove`

```text
Map_Remove(TargetMap: TMap < int32 , int32 > &, Key: int32 &) -> bool
```

Removes a key and its associated value from the map.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetMap` | `TMap < int32 , int32 > &` | The map to remove the key and its associated value from |
| `Key` | `int32 &` | The key that will be used to look the value up |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if an item was removed (False indicates nothing in the map uses the provided key) |

### `Map_Find`

```text
Map_Find(TargetMap: TMap < int32 , int32 > &, Key: int32 &, Value: int32 &) -> bool
```

Finds the value associated with the provided Key

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetMap` | `TMap < int32 , int32 > &` | The map to perform the lookup on |
| `Key` | `int32 &` | The key that will be used to look the value up |
| `Value` | `int32 &` | The value associated with the key, default constructed if key was not found |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if an item was found (False indicates nothing in the map uses the provided key) |

### `Map_Contains`

```text
Map_Contains(TargetMap: TMap < int32 , int32 > &, Key: int32 &) -> bool
```

Checks whether key is in a provided Map

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetMap` | `TMap < int32 , int32 > &` | The map to perform the lookup on |
| `Key` | `int32 &` | The key that will be used to lookup |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if an item was found (False indicates nothing in the map uses the provided key) |

### `Map_Keys`

```text
Map_Keys(TargetMap: TMap < int32 , int32 > &, Keys: TArray < int32 > &) -> void
```

Outputs an array of all keys present in the map

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetMap` | `TMap < int32 , int32 > &` | The map to get the list of keys from |
| `Keys` | `TArray < int32 > &` | All keys present in the map |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Map_Values`

```text
Map_Values(TargetMap: TMap < int32 , int32 > &, Values: TArray < int32 > &) -> void
```

Outputs an array of all values present in the map

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetMap` | `TMap < int32 , int32 > &` | The map to get the list of values from |
| `Values` | `TArray < int32 > &` | All values present in the map |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Map_Length`

```text
Map_Length(TargetMap: TMap < int32 , int32 > &) -> int32
```

Determines the number of entries in a provided Map

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetMap` | `TMap < int32 , int32 > &` | The map in question |

**Returns**

| Type | Description |
|---|---|
| `int32` | The number of entries in the map |

### `Map_Clear`

```text
Map_Clear(TargetMap: TMap < int32 , int32 > &) -> void
```

Clears a map of all entries, resetting it to empty

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetMap` | `TMap < int32 , int32 > &` | The map to clear |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMapPropertyByName`

```text
SetMapPropertyByName(Object: UObject *, PropertyName: FName, Value: TMap < int32 , int32 > &) -> void
```

Not exposed to users. Supports setting a map property on an object by name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `TMap < int32 , int32 > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlueprintPlatformLibrary.json -->

# UBlueprintPlatformLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `ClearAllLocalNotifications`

```text
ClearAllLocalNotifications() -> void
```

Clear all pending local notifications. Typically this will be done before scheduling new notifications when going into the background

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ScheduleLocalNotificationAtTime`

```text
ScheduleLocalNotificationAtTime(FireDateTime: FDateTime &, LocalTime: bool, Title: FText &, Body: FText &, Action: FText &, ActivationEvent: FString &) -> void
```

Schedule a local notification at a specific time, inLocalTime specifies the current local time or if UTC time should be used

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FireDateTime` | `FDateTime &` | The time at which to fire the local notification |
| `LocalTime` | `bool` | If true the provided time is in the local timezone, if false it is in UTC |
| `Title` | `FText &` | The title of the notification |
| `Body` | `FText &` | The more detailed description of the notification |
| `Action` | `FText &` | The text to be displayed on the slider controller |
| `ActivationEvent` | `FString &` | A string that is passed in the delegate callback when the app is brought into the foreground from the user activating the notification |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ScheduleLocalNotificationFromNow`

```text
ScheduleLocalNotificationFromNow(inSecondsFromNow: int32, Title: FText &, Body: FText &, Action: FText &, ActivationEvent: FString &) -> void
```

Schedule a local notification to fire inSecondsFromNow from now

**Parameters**

| Name | Type | Description |
|---|---|---|
| `inSecondsFromNow` | `int32` | The seconds until the notification should fire |
| `Title` | `FText &` | The title of the notification |
| `Body` | `FText &` | The more detailed description of the notification |
| `Action` | `FText &` | The text to be displayed on the slider controller |
| `ActivationEvent` | `FString &` | A string that is passed in the delegate callback when the app is brought into the foreground from the user activating the notification |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ScheduleLocalNotificationBadgeAtTime`

```text
ScheduleLocalNotificationBadgeAtTime(FireDateTime: FDateTime &, LocalTime: bool, ActivationEvent: FString &) -> void
```

Schedule a local notification badge at a specific time, inLocalTime specifies the current local time or if UTC time should be used

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FireDateTime` | `FDateTime &` | The time at which to fire the local notification |
| `LocalTime` | `bool` | If true the provided time is in the local timezone, if false it is in UTC |
| `ActivationEvent` | `FString &` | A string that is passed in the delegate callback when the app is brought into the foreground from the user activating the notification |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ScheduleLocalNotificationBadgeFromNow`

```text
ScheduleLocalNotificationBadgeFromNow(inSecondsFromNow: int32, ActivationEvent: FString &) -> void
```

Schedule a local notification badge to fire inSecondsFromNow from now

**Parameters**

| Name | Type | Description |
|---|---|---|
| `inSecondsFromNow` | `int32` | The seconds until the notification should fire |
| `ActivationEvent` | `FString &` | A string that is passed in the delegate callback when the app is brought into the foreground from the user activating the notification |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CancelLocalNotification`

```text
CancelLocalNotification(ActivationEvent: FString &) -> void
```

Cancel a local notification given the ActivationEvent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActivationEvent` | `FString &` | The string passed into the Schedule call for the notification to be cancelled |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLaunchNotification`

```text
GetLaunchNotification(NotificationLaunchedApp: bool &, ActivationEvent: FString &, FireDate: int32 &) -> void
```

Get the local notification that was used to launch the app

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotificationLaunchedApp` | `bool &` | Return true if a notification was used to launch the app |
| `ActivationEvent` | `FString &` | Returns the name of the ActivationEvent if a notification was used to launch the app |
| `FireDate` | `int32 &` | Returns the time the notification was activated |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlueprintRuntimeSettings.json -->

# UBlueprintRuntimeSettings

Implements the settings for the BlueprintRuntime module

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WarningSettings` | `TArray < FBlueprintWarningSettings >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBlueprintSetLibrary.json -->

# UBlueprintSetLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `Set_Add`

```text
Set_Add(TargetSet: TSet < int32 > &, NewItem: int32 &) -> void
```

Adds item to set. Output value indicates whether the item was successfully added, meaning an 
	  output of False indicates the item was already in the Set.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetSet` | `TSet < int32 > &` | The set to add item to |
| `NewItem` | `int32 &` | The item to add to the set |

**Returns**

| Type | Description |
|---|---|
| `void` | True if NewItem was added to the set (False indicates an equivalent item was present) |

### `Set_AddItems`

```text
Set_AddItems(TargetSet: TSet < int32 > &, NewItems: TArray < int32 > &) -> void
```

Adds all elements from an Array to a Set

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetSet` | `TSet < int32 > &` | The set to search for the item |
| `NewItems` | `TArray < int32 > &` | The items to add to the set |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Set_Remove`

```text
Set_Remove(TargetSet: TSet < int32 > &, Item: int32 &) -> bool
```

Remove item from set. Output value indicates if something was actually removed. False
	  indicates no equivalent item was found.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetSet` | `TSet < int32 > &` | The set to remove from |
| `Item` | `int32 &` | The item to remove from the set |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if an item was removed (False indicates no equivalent item was present) |

### `Set_RemoveItems`

```text
Set_RemoveItems(TargetSet: TSet < int32 > &, Items: TArray < int32 > &) -> void
```

Removes all elements in an Array from a set.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetSet` | `TSet < int32 > &` | The set to remove from |
| `Items` | `TArray < int32 > &` | The items to remove from the set |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Set_ToArray`

```text
Set_ToArray(A: TSet < int32 > &, Result: TArray < int32 > &) -> void
```

Outputs an Array containing copies of the entries of a Set.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `TSet < int32 > &` | Set |
| `Result` | `TArray < int32 > &` | Array |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Set_Clear`

```text
Set_Clear(TargetSet: TSet < int32 > &) -> void
```

Clear a set, removes all content.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetSet` | `TSet < int32 > &` | The set to clear |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Set_Length`

```text
Set_Length(TargetSet: TSet < int32 > &) -> int32
```

Get the number of items in a set.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetSet` | `TSet < int32 > &` | The set to get the length of |

**Returns**

| Type | Description |
|---|---|
| `int32` | The length of the set |

### `Set_Contains`

```text
Set_Contains(TargetSet: TSet < int32 > &, ItemToFind: int32 &) -> bool
```

Returns true if the set contains the given item.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetSet` | `TSet < int32 > &` | The set to search for the item |
| `ItemToFind` | `int32 &` | The item to look for |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the item was found within the set |

### `Set_Intersection`

```text
Set_Intersection(A: TSet < int32 > &, B: TSet < int32 > &, Result: TSet < int32 > &) -> void
```

Assigns Result to the intersection of Set A and Set B. That is, Result will contain
	  all elements that are in both Set A and Set B. To intersect with the empty set use
	  Clear.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `TSet < int32 > &` | One set to intersect |
| `B` | `TSet < int32 > &` | Another set to intersect |
| `Result` | `TSet < int32 > &` | Set to store results in |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Set_Union`

```text
Set_Union(A: TSet < int32 > &, B: TSet < int32 > &, Result: TSet < int32 > &) -> void
```

Assigns Result to the union of two sets, A and B. That is, Result will contain
	  all elements that are in Set A and in addition all elements in Set B. Note that 
	  a Set is a collection of unique elements, so duplicates will be eliminated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `TSet < int32 > &` | One set to union |
| `B` | `TSet < int32 > &` | Another set to union |
| `Result` | `TSet < int32 > &` | Set to store results in |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Set_Difference`

```text
Set_Difference(A: TSet < int32 > &, B: TSet < int32 > &, Result: TSet < int32 > &) -> void
```

Assigns Result to the relative difference of two sets, A and B. That is, Result will 
	  contain  all elements that are in Set A but are not found in Set B. Note that the 
	  difference between two sets  is not commutative. The Set whose elements you wish to 
	  preserve should be the first (top) parameter. Also called the relative complement.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `TSet < int32 > &` | Starting set |
| `B` | `TSet < int32 > &` | Set of elements to remove from set A |
| `Result` | `TSet < int32 > &` | Set containing all elements in A that are not found in B |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSetPropertyByName`

```text
SetSetPropertyByName(Object: UObject *, PropertyName: FName, Value: TSet < int32 > &) -> void
```

Not exposed to users. Supports setting a set property on an object by name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `TSet < int32 > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBoneMaskFilter.json -->

# UBoneMaskFilter

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BlendPoses` | `TArray < FInputBlendPose >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBookMark.json -->

# UBookMark

A camera position the current level.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Location` | `FVector` | Camera position |
| `Rotation` | `FRotator` | Camera rotation |
| `HiddenLevels` | `TArray < FString >` | Array of levels that are hidden |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBookMark2D.json -->

# UBookMark2D

Simple class to store 2D camera information.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Zoom2D` | `float` | Zoom of the camera |
| `Location` | `FIntPoint` | Location of the camera |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBoolBinding.json -->

# UBoolBinding

## Inheritance

`UPropertyBinding`

## Functions

### `GetValue`

```text
GetValue() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBorder.json -->

# UBorder

A border is a container widget that can contain one child widget, providing an opportunity 
  to surround it with a background image and adjustable padding.
 
   Single Child
   Image

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `HorizontalAlignment` | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the content horizontally. |
| `VerticalAlignment` | `TEnumAsByte < EVerticalAlignment >` | The alignment of the content vertically. |
| `bShowEffectWhenDisabled` | `uint8` | Whether or not to show the disabled effect when this border is disabled |
| `ContentColorAndOpacity` | `FLinearColor` | Color and opacity multiplier of content in the border |
| `ContentColorAndOpacityDelegate` | `FGetLinearColor` | A bindable delegate for the ContentColorAndOpacity. |
| `ResetBlendColor` | `bool` | - |
| `Padding` | `FMargin` | The padding area between the slot and the content it contains. |
| `Background` | `FSlateBrush` | Brush to drag as the background |
| `BackgroundDelegate` | `FGetSlateBrush` | A bindable delegate for the Brush. |
| `BrushColor` | `FLinearColor` | Color and opacity of the actual border image |
| `BrushColorDelegate` | `FGetLinearColor` | A bindable delegate for the BrushColor. |
| `DesiredSizeScale` | `FVector2D` | Scales the computed desired size of this border and its contents. Useful<br>	  for making things that slide open without having to hard-code their size.<br>	  Note: if the parent widget is set up to ignore this widget's desired size,<br>	  then changing this value will have no effect. |
| `OnMouseButtonDownEvent` | `FOnPointerEvent` | - |
| `OnMouseButtonUpEvent` | `FOnPointerEvent` | - |
| `OnMouseMoveEvent` | `FOnPointerEvent` | - |
| `OnMouseDoubleClickEvent` | `FOnPointerEvent` | - |

## Functions

### `SetContentColorAndOpacity`

```text
SetContentColorAndOpacity(InContentColorAndOpacity: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InContentColorAndOpacity` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetResetBlendColor`

```text
SetResetBlendColor(bResetBlendColor: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bResetBlendColor` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

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

### `SetBrushColor`

```text
SetBrushColor(InBrushColor: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBrushColor` | `FLinearColor` | - |

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
SetBrushFromTexture(Texture: UTexture2D *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Texture` | `UTexture2D *` | - |

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

### `SetDesiredSizeScale`

```text
SetDesiredSizeScale(InScale: FVector2D) -> void
```

Sets the DesireSizeScale of this border.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InScale` | `FVector2D` | The X and Y multipliers for the desired size |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBorderSlot.json -->

# UBorderSlot

The Slot for the UBorderSlot, contains the widget displayed in a border's single slot

## Inheritance

`UPanelSlot`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Padding` | `FMargin` | The padding area between the slot and the content it contains. |
| `HorizontalAlignment` | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the object horizontally. |
| `VerticalAlignment` | `TEnumAsByte < EVerticalAlignment >` | The alignment of the object vertically. |

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

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBoxComponent.json -->

# UBoxComponent

A box generally used for simple collision. Bounds are rendered as lines in the editor.

## Inheritance

`UShapeComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoxExtent` | `FVector` | The extents (radii dimensions) of the box |
| `LineThickness` | `float` | Used to control the line thickness when rendering |

## Functions

### `SetBoxExtent`

```text
SetBoxExtent(InBoxExtent: FVector, bUpdateOverlaps: bool) -> void
```

Change the box extent size. This is the unscaled size, before component scale is applied.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBoxExtent` | `FVector` | - |
| `bUpdateOverlaps` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetScaledBoxExtent`

```text
GetScaledBoxExtent() -> FVector
```

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetUnscaledBoxExtent`

```text
GetUnscaledBoxExtent() -> FVector
```

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBoxReflectionCaptureComponent.json -->

# UBoxReflectionCaptureComponent

## Inheritance

`UReflectionCaptureComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoxTransitionDistance` | `float` | Adjust capture transition distance |
| `PerformShapeTestOnMobile` | `bool` | - |
| `PreviewInfluenceBox` | `UBoxComponent *` | - |
| `PreviewCaptureBox` | `UBoxComponent *` | - |
| `bShowPreviewVolumeBox` | `bool` | - |
| `PreviewVolumeBox` | `UStaticMeshComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBrainComponent.json -->

# UBrainComponent

## Inheritance

`UActorComponent` -> `IAIResourceInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BlackboardComp` | `UBlackboardComponent *` | blackboard component |
| `AIOwner` | `AAIController *` | - |

## Functions

### `RestartLogic`

```text
RestartLogic() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopLogic`

```text
StopLogic(Reason: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reason` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PauseLogic`

```text
PauseLogic(Reason: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reason` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResumeLogic`

```text
ResumeLogic(Reason: FString &) -> EAILogicResuming :: Type
```

MUST be called by child implementations!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reason` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `EAILogicResuming :: Type` | indicates whether child class' ResumeLogic should be called (true) or has it been |

### `IsRunning`

```text
IsRunning() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsPaused`

```text
IsPaused() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBreakpoint.json -->

# UBreakpoint

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnabled` | `uint32` | - |
| `Node` | `UEdGraphNode *` | - |
| `bStepOnce` | `uint32` | - |
| `bStepOnce_WasPreviouslyDisabled` | `uint32` | - |
| `bStepOnce_RemoveAfterHit` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBrushBinding.json -->

# UBrushBinding

## Inheritance

`UPropertyBinding`

## Functions

### `GetValue`

```text
GetValue() -> FSlateBrush
```

**Returns**

| Type | Description |
|---|---|
| `FSlateBrush` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBrushBuilder.json -->

# UBrushBuilder

Base class of UnrealEd brush builders.
 
 
  Tips for writing brush builders:
 
  - Always validate the user-specified and call BadParameters function
    if anything is wrong, instead of actually building geometry.
    If you build an invalid brush due to bad user parameters, you'll
    cause an extraordinary amount of pain for the poor user.
 
  - When generating polygons with more than 3 vertices, BE SURE all the
    polygon's vertices are coplanar!  Out-of-plane polygons will cause
    geometry to be corrupted.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BitmapFilename` | `FString` | - |
| `ToolTip` | `FString` | localized FString that will be displayed as the name of this brush builder in the editor |
| `NotifyBadParams` | `uint32` | If false, disabled the bad param notifications |
| `Vertices` | `TArray < FVector >` | - |
| `Polys` | `TArray < struct FBuilderPoly >` | - |
| `Layer` | `FName` | - |
| `MergeCoplanars` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBrushComponent.json -->

# UBrushComponent

A brush component defines a shape that can be modified within the editor. They are used both as part of BSP building, and for volumes.

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Brush` | `UModel *` | - |
| `BrushBodySetup` | `UBodySetup *` | Description of collision |
| `PrePivot_DEPRECATED` | `FVector` | Local space translation |
| `MeshCollisionProvider` | `UStaticMesh *` | - |

## Functions

### `SetMeshCollisionProvider`

```text
SetMeshCollisionProvider(Mesh: UStaticMesh *) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Mesh` | `UStaticMesh *` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTAttachment_LuaBase.json -->

# UBTAttachment_LuaBase

Base class for lua based Attachment nodes. Do NOT use it for creating native c++ classes!
 
   When Attachment receives Deactivation event, all latent actions associated this instance are being removed.
   This prevents from resuming activity started by Activation, but does not handle external events.
   Please use them safely (unregister at abort) and call IsAttachmentActive() when in doubt.

## Inheritance

`UBTService`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AIOwner` | `AAIController *` | Cached AIController owner of BehaviorTreeComponent. |

## Functions

### `ReceiveTickAI`

```text
ReceiveTickAI(OwnerController: AAIController *, ControlledPawn: APawn *, DeltaSeconds: float) -> void
```

tick function

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |
| `DeltaSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveSearchStartAI`

```text
ReceiveSearchStartAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

task search enters branch of tree

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveActivationAI`

```text
ReceiveActivationAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

attachment became active

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveDeactivationAI`

```text
ReceiveDeactivationAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

attachment became inactive

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsAttachmentActive`

```text
IsAttachmentActive() -> bool
```

check if attachment is currently being active

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTComposite_SimpleParallel.json -->

# UBTComposite_SimpleParallel

Simple Parallel composite node.
  Allows for running two children: one which must be a single task node (with optional decorators), and the other of which can be a complete subtree.

## Inheritance

`UBTCompositeNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FinishMode` | `TEnumAsByte < EBTParallelMode :: Type >` | how background tree should be handled when main task finishes execution |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTCompositeNode.json -->

# UBTCompositeNode

## Inheritance

`UBTNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Children` | `TArray < FBTCompositeChild >` | child nodes |
| `Services` | `TArray < UBTService * >` | service nodes |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTCondition_LuaBase.json -->

# UBTCondition_LuaBase

Base class for lua based condition nodes. Do NOT use it for creating native c++ classes!
 
   Unlike task and attachments, condition have two execution chains:
    ExecutionStart-ExecutionFinish and ObserverActivated-ObserverDeactivated
   which makes automatic latent action cleanup impossible. Keep in mind, that
   you HAVE TO verify is given chain is still active after resuming from any
   latent action (like Delay, Timelines, etc).
 
   Helper functions:
   - IsConditionExecutionActive (true after ExecutionStart, until ExecutionFinish)
   - IsConditionObserverActive (true after ObserverActivated, until ObserverDeactivated)

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AIOwner` | `AAIController *` | Cached AIController owner of BehaviorTreeComponent. |
| `ObservedKeyNames` | `TArray < FName >` | blackboard key names that should be observed |
| `bCheckConditionOnlyBlackBoardChanges` | `uint32` | Applies only if Condition has any FBlackboardKeySelector property and if condition is<br>	 	set to abort BT flow. Is set to true ReceiveConditionCheck will be called only on changes<br>	  	to observed BB keys. If false or no BB keys observed ReceiveConditionCheck will be called every tick |
| `bIsObservingBB` | `uint32` | gets set to true if condition declared BB keys it can potentially observe |

## Functions

### `ReceiveTickAI`

```text
ReceiveTickAI(OwnerController: AAIController *, ControlledPawn: APawn *, DeltaSeconds: float) -> void
```

tick function

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |
| `DeltaSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveExecutionStartAI`

```text
ReceiveExecutionStartAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

called on execution of underlying node

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveExecutionFinishAI`

```text
ReceiveExecutionFinishAI(OwnerController: AAIController *, ControlledPawn: APawn *, NodeResult: EBTNodeResult :: Type) -> void
```

called when execution of underlying node is finished

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |
| `NodeResult` | `EBTNodeResult :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveObserverActivatedAI`

```text
ReceiveObserverActivatedAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

called when observer is activated (flow controller)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveObserverDeactivatedAI`

```text
ReceiveObserverDeactivatedAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

called when observer is deactivated (flow controller)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PerformConditionCheckAI`

```text
PerformConditionCheckAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> bool
```

called when testing if underlying node can be executed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsConditionExecutionActive`

```text
IsConditionExecutionActive() -> bool
```

check if condition is part of currently active branch

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsConditionObserverActive`

```text
IsConditionObserverActive() -> bool
```

check if condition's observer is currently active

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator.json -->

# UBTDecorator

Decorators are supporting nodes placed on parent-child connection, that receive notification about execution flow and can be ticked
 
  Because some of them can be instanced for specific AI, following virtual functions are not marked as const:
   - OnNodeActivation
   - OnNodeDeactivation
   - OnNodeProcessed
   - OnBecomeRelevant (from UBTAuxiliaryNode)
   - OnCeaseRelevant (from UBTAuxiliaryNode)
   - TickNode (from UBTAuxiliaryNode)
 
  If your node is not being instanced (default behavior), DO NOT change any properties of object within those functions!
  Template nodes are shared across all behavior tree components using the same tree asset and must store
  their runtime properties in provided NodeMemory block (allocation size determined by GetInstanceMemorySize() )

## Inheritance

`UBTAuxiliaryNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bInverseCondition` | `uint32` | if set, condition check result will be inversed |
| `FlowAbortMode` | `TEnumAsByte < EBTFlowAbortMode :: Type >` | flow controller settings |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_Blackboard.json -->

# UBTDecorator_Blackboard

Blackboard decorator node.
  A decorator node that bases its condition on a Blackboard key.

## Inheritance

`UBTDecorator_BlackboardBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `IntValue` | `int32` | value for arithmetic operations |
| `FloatValue` | `float` | value for arithmetic operations |
| `StringValue` | `FString` | value for string operations |
| `CachedDescription` | `FString` | cached description |
| `OperationType` | `uint8` | operation type |
| `NotifyObserver` | `TEnumAsByte < EBTBlackboardRestart :: Type >` | when observer can try to request abort? |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_BlackboardBase.json -->

# UBTDecorator_BlackboardBase

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BlackboardKey` | `FBlackboardKeySelector` | blackboard key selector |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_BlueprintBase.json -->

# UBTDecorator_BlueprintBase

Base class for blueprint based decorator nodes. Do NOT use it for creating native c++ classes!
 
   Unlike task and services, decorator have two execution chains: 
    ExecutionStart-ExecutionFinish and ObserverActivated-ObserverDeactivated
   which makes automatic latent action cleanup impossible. Keep in mind, that
   you HAVE TO verify is given chain is still active after resuming from any
   latent action (like Delay, Timelines, etc).
 
   Helper functions:
   - IsDecoratorExecutionActive (true after ExecutionStart, until ExecutionFinish)
   - IsDecoratorObserverActive (true after ObserverActivated, until ObserverDeactivated)

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AIOwner` | `AAIController *` | Cached AIController owner of BehaviorTreeComponent. |
| `ActorOwner` | `AActor *` | Cached AIController owner of BehaviorTreeComponent. |
| `ObservedKeyNames` | `TArray < FName >` | blackboard key names that should be observed |
| `bShowPropertyDetails` | `uint32` | show detailed information about properties |
| `bCheckConditionOnlyBlackBoardChanges` | `uint32` | Applies only if Decorator has any FBlackboardKeySelector property and if decorator is <br>	 	set to abort BT flow. Is set to true ReceiveConditionCheck will be called only on changes <br>	  	to observed BB keys. If false or no BB keys observed ReceiveConditionCheck will be called every tick |
| `bIsObservingBB` | `uint32` | gets set to true if decorator declared BB keys it can potentially observe |

## Functions

### `ReceiveTick`

```text
ReceiveTick(OwnerActor: AActor *, DeltaSeconds: float) -> void
```

tick function

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |
| `DeltaSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveExecutionStart`

```text
ReceiveExecutionStart(OwnerActor: AActor *) -> void
```

called on execution of underlying node

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveExecutionFinish`

```text
ReceiveExecutionFinish(OwnerActor: AActor *, NodeResult: EBTNodeResult :: Type) -> void
```

called when execution of underlying node is finished

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |
| `NodeResult` | `EBTNodeResult :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveObserverActivated`

```text
ReceiveObserverActivated(OwnerActor: AActor *) -> void
```

called when observer is activated (flow controller)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveObserverDeactivated`

```text
ReceiveObserverDeactivated(OwnerActor: AActor *) -> void
```

called when observer is deactivated (flow controller)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PerformConditionCheck`

```text
PerformConditionCheck(OwnerActor: AActor *) -> bool
```

called when testing if underlying node can be executed, must call FinishConditionCheck

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ReceiveTickAI`

```text
ReceiveTickAI(OwnerController: AAIController *, ControlledPawn: APawn *, DeltaSeconds: float) -> void
```

Alternative AI version of ReceiveTick

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |
| `DeltaSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveExecutionStartAI`

```text
ReceiveExecutionStartAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

Alternative AI version of ReceiveExecutionStart

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveExecutionFinishAI`

```text
ReceiveExecutionFinishAI(OwnerController: AAIController *, ControlledPawn: APawn *, NodeResult: EBTNodeResult :: Type) -> void
```

Alternative AI version of ReceiveExecutionFinish

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |
| `NodeResult` | `EBTNodeResult :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveObserverActivatedAI`

```text
ReceiveObserverActivatedAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

Alternative AI version of ReceiveObserverActivated

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveObserverDeactivatedAI`

```text
ReceiveObserverDeactivatedAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

Alternative AI version of ReceiveObserverDeactivated

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PerformConditionCheckAI`

```text
PerformConditionCheckAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> bool
```

Alternative AI version of ReceiveConditionCheck

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsDecoratorExecutionActive`

```text
IsDecoratorExecutionActive() -> bool
```

check if decorator is part of currently active branch

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsDecoratorObserverActive`

```text
IsDecoratorObserverActive() -> bool
```

check if decorator's observer is currently active

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_CheckGameplayTagsOnActor.json -->

# UBTDecorator_CheckGameplayTagsOnActor

GameplayTag decorator node.
  A decorator node that bases its condition on whether the specified Actor (in the blackboard) has a Gameplay Tag or
  Tags specified.

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActorToCheck` | `FBlackboardKeySelector` | - |
| `TagsToMatch` | `EGameplayContainerMatchType` | - |
| `GameplayTags` | `FGameplayTagContainer` | - |
| `CachedDescription` | `FString` | cached description |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_CompareBBEntries.json -->

# UBTDecorator_CompareBBEntries

Blackboard comparison decorator node.
  A decorator node that bases its condition on a comparison between two Blackboard keys.

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Operator` | `TEnumAsByte < EBlackBoardEntryComparison :: Type >` | operation type |
| `BlackboardKeyA` | `FBlackboardKeySelector` | blackboard key selector |
| `BlackboardKeyB` | `FBlackboardKeySelector` | blackboard key selector |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_ConeCheck.json -->

# UBTDecorator_ConeCheck

Cone check decorator node.
  A decorator node that bases its condition on a cone check, using Blackboard entries to form the parameters of the check.

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConeHalfAngle` | `float` | Angle between cone direction and code cone edge, or a half of the total cone angle |
| `ConeOrigin` | `FBlackboardKeySelector` | blackboard key selector |
| `ConeDirection` | `FBlackboardKeySelector` | "None" means "use ConeOrigin's direction" |
| `Observed` | `FBlackboardKeySelector` | blackboard key selector |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_Cooldown.json -->

# UBTDecorator_Cooldown

Cooldown decorator node.
  A decorator node that bases its condition on whether a cooldown timer has expired.

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CoolDownTime` | `float` | max allowed time for execution of underlying node |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_DoesPathExist.json -->

# UBTDecorator_DoesPathExist

Cooldown decorator node.
  A decorator node that bases its condition on whether a path exists between two points from the Blackboard.

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BlackboardKeyA` | `FBlackboardKeySelector` | blackboard key selector |
| `BlackboardKeyB` | `FBlackboardKeySelector` | blackboard key selector |
| `bUseSelf` | `uint32` | - |
| `PathQueryType` | `TEnumAsByte < EPathExistanceQueryType :: Type >` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | "None" will result in default filter being used |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_IsAtLocation.json -->

# UBTDecorator_IsAtLocation

Is At Location decorator node.
  A decorator node that checks if AI controlled pawn is at given location.

## Inheritance

`UBTDecorator_BlackboardBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AcceptableRadius` | `float` | distance threshold to accept as being at location |
| `ParametrizedAcceptableRadius` | `FAIDataProviderFloatValue` | - |
| `GeometricDistanceType` | `FAIDistanceType` | - |
| `bUseParametrizedRadius` | `uint32` | - |
| `bUseNavAgentGoalLocation` | `uint32` | if moving to an actor and this actor is a nav agent, then we will move to their nav agent location |
| `bPathFindingBasedTest` | `uint32` | If true the result will be consistent with tests done while following paths.<br>	 	Set to false to use geometric distance as configured with DistanceType |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_IsBBEntryOfClass.json -->

# UBTDecorator_IsBBEntryOfClass

## Inheritance

`UBTDecorator_BlackboardBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TestClass` | `TSubclassOf < UObject >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_KeepInCone.json -->

# UBTDecorator_KeepInCone

Cooldown decorator node.
  A decorator node that bases its condition on whether the observed position is still inside a cone. The cone's direction is calculated when the node first becomes relevant.

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConeHalfAngle` | `float` | max allowed time for execution of underlying node |
| `ConeOrigin` | `FBlackboardKeySelector` | blackboard key selector |
| `Observed` | `FBlackboardKeySelector` | blackboard key selector |
| `bUseSelfAsOrigin` | `uint32` | - |
| `bUseSelfAsObserved` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_Loop.json -->

# UBTDecorator_Loop

Loop decorator node.
  A decorator node that bases its condition on whether its loop counter has been exceeded.

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NumLoops` | `int32` | number of executions |
| `bInfiniteLoop` | `bool` | infinite loop |
| `InfiniteLoopTimeoutTime` | `float` | timeout (when looping infinitely, when we finish a loop we will check whether we have spent this time looping, if we have we will stop looping). A negative value means loop forever. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_SetTagCooldown.json -->

# UBTDecorator_SetTagCooldown

Set tag cooldown decorator node.
  A decorator node that sets a gameplay tag cooldown.

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CooldownTag` | `FGameplayTag` | Gameplay tag that will be used for the cooldown. |
| `CooldownDuration` | `float` | Value we will add or set to the Cooldown tag when this task runs. |
| `bAddToExistingDuration` | `bool` | True if we are adding to any existing duration, false if we are setting the duration (potentially invalidating an existing end time). |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_TagCooldown.json -->

# UBTDecorator_TagCooldown

Cooldown decorator node.
  A decorator node that bases its condition on whether a cooldown timer based on a gameplay tag has expired.

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CooldownTag` | `FGameplayTag` | Gameplay tag that will be used for the cooldown. |
| `CooldownDuration` | `float` | Value we will add or set to the Cooldown tag when this node is deactivated. |
| `bAddToExistingDuration` | `bool` | True if we are adding to any existing duration, false if we are setting the duration (potentially invalidating an existing end time). |
| `bActivatesCooldown` | `bool` | Whether or not we are addingsetting to the cooldown tag's value when the decorator deactivates. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_TimeLimit.json -->

# UBTDecorator_TimeLimit

Time Limit decorator node.
  A decorator node that bases its condition on whether a timer has exceeded a specified value. The timer is reset each time the node becomes relevant.

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TimeLimit` | `float` | max allowed time for execution of underlying node |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTFunctionLibrary.json -->

# UBTFunctionLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `GetOwnersBlackboard`

```text
GetOwnersBlackboard(NodeOwner: UBTNode *) -> UBlackboardComponent *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |

**Returns**

| Type | Description |
|---|---|
| `UBlackboardComponent *` | - |

### `GetOwnerComponent`

```text
GetOwnerComponent(NodeOwner: UBTNode *) -> UBehaviorTreeComponent *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |

**Returns**

| Type | Description |
|---|---|
| `UBehaviorTreeComponent *` | - |

### `GetBlackboardValueAsObject`

```text
GetBlackboardValueAsObject(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> UObject *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

### `GetBlackboardValueAsActor`

```text
GetBlackboardValueAsActor(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> AActor *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `GetBlackboardValueAsClass`

```text
GetBlackboardValueAsClass(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> UClass *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `UClass *` | - |

### `GetBlackboardValueAsEnum`

```text
GetBlackboardValueAsEnum(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> uint8
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `uint8` | - |

### `GetBlackboardValueAsInt`

```text
GetBlackboardValueAsInt(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetBlackboardValueAsFloat`

```text
GetBlackboardValueAsFloat(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetBlackboardValueAsBool`

```text
GetBlackboardValueAsBool(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetBlackboardValueAsString`

```text
GetBlackboardValueAsString(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetBlackboardValueAsName`

```text
GetBlackboardValueAsName(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> FName
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `GetBlackboardValueAsVector`

```text
GetBlackboardValueAsVector(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetBlackboardValueAsRotator`

```text
GetBlackboardValueAsRotator(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> FRotator
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `SetBlackboardValueAsObject`

```text
SetBlackboardValueAsObject(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: UObject *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlackboardValueAsClass`

```text
SetBlackboardValueAsClass(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: UClass *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `UClass *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlackboardValueAsEnum`

```text
SetBlackboardValueAsEnum(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: uint8) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlackboardValueAsInt`

```text
SetBlackboardValueAsInt(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlackboardValueAsFloat`

```text
SetBlackboardValueAsFloat(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlackboardValueAsBool`

```text
SetBlackboardValueAsBool(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlackboardValueAsString`

```text
SetBlackboardValueAsString(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: FString) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlackboardValueAsName`

```text
SetBlackboardValueAsName(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlackboardValueAsVector`

```text
SetBlackboardValueAsVector(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearBlackboardValueAsVector`

```text
ClearBlackboardValueAsVector(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> void
```

(DEPRECATED) Use ClearBlackboardValue instead

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlackboardValueAsRotator`

```text
SetBlackboardValueAsRotator(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: FRotator) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearBlackboardValue`

```text
ClearBlackboardValue(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> void
```

Resets indicated value to "not set" value, based on values type

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StartUsingExternalEvent`

```text
StartUsingExternalEvent(NodeOwner: UBTNode *, OwningActor: AActor *) -> void
```

Initialize variables marked as "instance memory" and set owning actor for blackboard operations

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `OwningActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopUsingExternalEvent`

```text
StopUsingExternalEvent(NodeOwner: UBTNode *) -> void
```

Save variables marked as "instance memory" and clear owning actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTNode.json -->

# UBTNode

## Inheritance

`UObject` -> `IGameplayTaskOwnerInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NodeName` | `FString` | node name |
| `TreeAsset` | `UBehaviorTree *` | source asset |
| `ParentNode` | `UBTCompositeNode *` | parent node |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTService.json -->

# UBTService

Behavior Tree service nodes is designed to perform "background" tasks that update AI's knowledge.
 
   Services are being executed when underlying branch of behavior tree becomes active,
   but unlike tasks they don't return any results and can't directly affect execution flow.
 
   Usually they perform periodical checks (see TickNode) and often store results in blackboard.
   If any decorator node below requires results of check beforehand, use OnSearchStart function.
    Keep in mind that any checks performed there have to be instantaneous!
 	
   Other typical use case is creating a marker when specific branch is being executed
   (see OnBecomeRelevant, OnCeaseRelevant), by setting a flag in blackboard.
 
   Because some of them can be instanced for specific AI, following virtual functions are not marked as const:
    - OnBecomeRelevant (from UBTAuxiliaryNode)
    - OnCeaseRelevant (from UBTAuxiliaryNode)
    - TickNode (from UBTAuxiliaryNode)
    - OnSearchStart
 
   If your node is not being instanced (default behavior), DO NOT change any properties of object within those functions!
   Template nodes are shared across all behavior tree components using the same tree asset and must store
   their runtime properties in provided NodeMemory block (allocation size determined by GetInstanceMemorySize() )

## Inheritance

`UBTAuxiliaryNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Interval` | `float` | defines time span between subsequent ticks of the service |
| `RandomDeviation` | `float` | adds random range to service's Interval |
| `bCallTickOnSearchStart` | `uint32` | call Tick event when task search enters this node (SearchStart will be called as well) |
| `bRestartTimerOnEachActivation` | `uint32` | if set, next tick time will be always reset to service's interval when node is activated |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTService_BlackboardBase.json -->

# UBTService_BlackboardBase

## Inheritance

`UBTService`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BlackboardKey` | `FBlackboardKeySelector` | blackboard key selector |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTService_BlueprintBase.json -->

# UBTService_BlueprintBase

Base class for blueprint based service nodes. Do NOT use it for creating native c++ classes!
 
   When service receives Deactivation event, all latent actions associated this instance are being removed.
   This prevents from resuming activity started by Activation, but does not handle external events.
   Please use them safely (unregister at abort) and call IsServiceActive() when in doubt.

## Inheritance

`UBTService`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AIOwner` | `AAIController *` | Cached AIController owner of BehaviorTreeComponent. |
| `ActorOwner` | `AActor *` | Cached actor owner of BehaviorTreeComponent. |
| `bShowPropertyDetails` | `uint32` | show detailed information about properties |
| `bShowEventDetails` | `uint32` | show detailed information about implemented events |

## Functions

### `ReceiveTick`

```text
ReceiveTick(OwnerActor: AActor *, DeltaSeconds: float) -> void
```

tick function

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |
| `DeltaSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveSearchStart`

```text
ReceiveSearchStart(OwnerActor: AActor *) -> void
```

task search enters branch of tree

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveActivation`

```text
ReceiveActivation(OwnerActor: AActor *) -> void
```

service became active

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveDeactivation`

```text
ReceiveDeactivation(OwnerActor: AActor *) -> void
```

service became inactive

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveTickAI`

```text
ReceiveTickAI(OwnerController: AAIController *, ControlledPawn: APawn *, DeltaSeconds: float) -> void
```

Alternative AI version of ReceiveTick function.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |
| `DeltaSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveSearchStartAI`

```text
ReceiveSearchStartAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

Alternative AI version of ReceiveSearchStart function.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveActivationAI`

```text
ReceiveActivationAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

Alternative AI version of ReceiveActivation function.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveDeactivationAI`

```text
ReceiveDeactivationAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

Alternative AI version of ReceiveDeactivation function.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsServiceActive`

```text
IsServiceActive() -> bool
```

check if service is currently being active

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTService_DefaultFocus.json -->

# UBTService_DefaultFocus

Default Focus service node.
  A service node that automatically sets the AI controller's focus when it becomes active.

## Inheritance

`UBTService_BlackboardBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FocusPriority` | `uint8` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTService_RunEQS.json -->

# UBTService_RunEQS

## Inheritance

`UBTService_BlackboardBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EQSRequest` | `FEQSParametrizedQueryExecutionRequest` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_BlackboardBase.json -->

# UBTTask_BlackboardBase

## Inheritance

`UBTTaskNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BlackboardKey` | `FBlackboardKeySelector` | blackboard key selector |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_BlueprintBase.json -->

# UBTTask_BlueprintBase

Base class for blueprint based task nodes. Do NOT use it for creating native c++ classes!
 
   When task receives Abort event, all latent actions associated this instance are being removed.
   This prevents from resuming activity started by Execute, but does not handle external events.
   Please use them safely (unregister at abort) and call IsTaskExecuting() when in doubt.

## Inheritance

`UBTTaskNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AIOwner` | `AAIController *` | Cached AIController owner of BehaviorTreeComponent. |
| `ActorOwner` | `AActor *` | Cached actor owner of BehaviorTreeComponent. |
| `bShowPropertyDetails` | `uint32` | show detailed information about properties |

## Functions

### `ReceiveExecute`

```text
ReceiveExecute(OwnerActor: AActor *) -> void
```

entry point, task will stay active until FinishExecute is called.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveAbort`

```text
ReceiveAbort(OwnerActor: AActor *) -> void
```

if blueprint graph contains this event, task will stay active until FinishAbort is called

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveTick`

```text
ReceiveTick(OwnerActor: AActor *, DeltaSeconds: float) -> void
```

tick function

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |
| `DeltaSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveExecuteAI`

```text
ReceiveExecuteAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

Alternative AI version of ReceiveExecute

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveAbortAI`

```text
ReceiveAbortAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

Alternative AI version of ReceiveAbort

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveTickAI`

```text
ReceiveTickAI(OwnerController: AAIController *, ControlledPawn: APawn *, DeltaSeconds: float) -> void
```

Alternative AI version of tick function.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |
| `DeltaSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FinishExecute`

```text
FinishExecute(bSuccess: bool) -> void
```

finishes task execution with Success or Fail result

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bSuccess` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FinishAbort`

```text
FinishAbort() -> void
```

aborts task execution

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFinishOnMessage`

```text
SetFinishOnMessage(MessageName: FName) -> void
```

task execution will be finished (with result 'Success') after receiving specified message

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MessageName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFinishOnMessageWithId`

```text
SetFinishOnMessageWithId(MessageName: FName, RequestID: int32) -> void
```

task execution will be finished (with result 'Success') after receiving specified message with indicated ID

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MessageName` | `FName` | - |
| `RequestID` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsTaskExecuting`

```text
IsTaskExecuting() -> bool
```

check if task is currently being executed

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsTaskAborting`

```text
IsTaskAborting() -> bool
```

check if task is currently being aborted

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_GameplayTaskBase.json -->

# UBTTask_GameplayTaskBase

Base class for managing gameplay tasks
  Since AITask doesn't have any kind of successfailed results, default implemenation will only return EBTNode::Succeeded
 
  In your ExecuteTask:
  - use NewBTAITask() helper to create task
  - initialize task with values if needed
  - use StartGameplayTask() helper to execute and get node result

## Inheritance

`UBTTaskNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bWaitForGameplayTask` | `uint32` | if set, behavior tree task will wait until gameplay tasks finishes |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_LuaBase.json -->

# UBTTask_LuaBase

Base class for lua based task nodes. Do NOT use it for creating native c++ classes!
 
   When task receives Abort event, all latent actions associated this instance are being removed.
   This prevents from resuming activity started by Execute, but does not handle external events.
   Please use them safely (unregister at abort) and call IsTaskExecuting() when in doubt.

## Inheritance

`UBTTaskNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AIOwner` | `AAIController *` | Cached AIController owner of BehaviorTreeComponent. |
| `bShowPropertyDetails` | `uint32` | show detailed information about properties |

## Functions

### `ReceiveExecuteAI`

```text
ReceiveExecuteAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

entry point, task will stay active until FinishExecute is called.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveAbortAI`

```text
ReceiveAbortAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

if blueprint graph contains this event, task will stay active until FinishAbort is called

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveTickAI`

```text
ReceiveTickAI(OwnerController: AAIController *, ControlledPawn: APawn *, DeltaSeconds: float) -> void
```

tick function

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |
| `DeltaSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FinishExecute`

```text
FinishExecute(bSuccess: bool) -> void
```

finishes task execution with Success or Fail result

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bSuccess` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FinishAbort`

```text
FinishAbort() -> void
```

aborts task execution

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFinishOnMessage`

```text
SetFinishOnMessage(MessageName: FName) -> void
```

task execution will be finished (with result 'Success') after receiving specified message

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MessageName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFinishOnMessageWithId`

```text
SetFinishOnMessageWithId(MessageName: FName, RequestID: int32) -> void
```

task execution will be finished (with result 'Success') after receiving specified message with indicated ID

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MessageName` | `FName` | - |
| `RequestID` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsTaskExecuting`

```text
IsTaskExecuting() -> bool
```

check if task is currently being executed

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsTaskAborting`

```text
IsTaskAborting() -> bool
```

check if task is currently being aborted

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_MakeNoise.json -->

# UBTTask_MakeNoise

Make Noise task node.
  A task node that calls MakeNoise() on this Pawn when executed.

## Inheritance

`UBTTaskNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Loudnes` | `float` | Loudnes of generated noise |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_MoveDirectlyToward.json -->

# UBTTask_MoveDirectlyToward

Move Directly Toward task node.
  Moves the AI pawn toward the specified Actor or Location (Vector) blackboard entry in a straight line, without regard to any navigation system. If you need the AI to navigate, use the "Move To" node instead.

## Inheritance

`UBTTask_MoveTo`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bDisablePathUpdateOnGoalLocationChange` | `uint32` | - |
| `bProjectVectorGoalToNavigation` | `uint32` | - |
| `bUpdatedDeprecatedProperties` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_MoveTo.json -->

# UBTTask_MoveTo

Move To task node.
  Moves the AI pawn toward the specified Actor or Location blackboard entry using the navigation system.

## Inheritance

`UBTTask_BlackboardBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AcceptableRadius` | `float` | fixed distance added to threshold between AI and goal location in destination reach test |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | "None" will result in default filter being used |
| `ObservedBlackboardValueTolerance` | `float` | if task is expected to react to changes to location represented by BB key <br>	 	this property can be used to tweak sensitivity of the mechanism. Value is <br>	 	recommended to be less then AcceptableRadius |
| `bObserveBlackboardValue` | `uint32` | if move goal in BB changes the move will be redirected to new location |
| `bAllowStrafe` | `uint32` | - |
| `bAllowPartialPath` | `uint32` | if set, use incomplete path when goal can't be reached |
| `bTrackMovingGoal` | `uint32` | if set, path to goal actor will update itself when actor moves |
| `bProjectGoalLocation` | `uint32` | if set, goal location will be projected on navigation data (navmesh) before using |
| `bReachTestIncludesAgentRadius` | `uint32` | if set, radius of AI's capsule will be added to threshold between AI and goal location in destination reach test |
| `bReachTestIncludesGoalRadius` | `uint32` | if set, radius of goal's capsule will be added to threshold between AI and goal location in destination reach test |
| `bStopOnOverlap` | `uint32` | DEPRECATED, please use combination of bReachTestIncludesRadius instead |
| `bStopOnOverlapNeedsUpdate` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_PlayAnimation.json -->

# UBTTask_PlayAnimation

Play indicated AnimationAsset on Pawn controlled by BT 
 	Note that this node is generic and is handing multiple special cases,
 	If you want a more efficient solution you'll need to implement it yourself (or wait for our BTTask_PlayCharacterAnimation)

## Inheritance

`UBTTaskNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AnimationToPlay` | `UAnimationAsset *` | Animation asset to play. Note that it needs to match the skeleton of pawn this BT is controlling |
| `bLooping` | `uint32` | - |
| `bNonBlocking` | `uint32` | if true the task will just trigger the animation and instantly finish. Fire and Forget. |
| `MyOwnerComp` | `UBehaviorTreeComponent *` | - |
| `CachedSkelMesh` | `USkeletalMeshComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_PlaySound.json -->

# UBTTask_PlaySound

Play Sound task node.
  Plays the specified sound when executed.

## Inheritance

`UBTTaskNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SoundToPlay` | `USoundCue *` | CUE to play |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_PushPawnAction.json -->

# UBTTask_PushPawnAction

Action task node.
  Push pawn action to controller.

## Inheritance

`UBTTask_PawnActionBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Action` | `UPawnAction *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_RotateToFaceBBEntry.json -->

# UBTTask_RotateToFaceBBEntry

## Inheritance

`UBTTask_BlackboardBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Precision` | `float` | Success condition precision in degrees |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_RunBehavior.json -->

# UBTTask_RunBehavior

RunBehavior task allows pushing subtrees on execution stack.
  Subtree asset can't be changed in runtime! 
 
  This limitation is caused by support for subtree's root level decorators,
  which are injected into parent tree, and structure of running tree
  cannot be modified in runtime (see: BTNode: ExecutionIndex, MemoryOffset)
 
  Use RunBehaviorDynamic task for subtrees that need to be changed in runtime.

## Inheritance

`UBTTaskNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BehaviorAsset` | `UBehaviorTree *` | behavior to run |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_RunBehaviorDynamic.json -->

# UBTTask_RunBehaviorDynamic

RunBehaviorDynamic task allows pushing subtrees on execution stack.
  Subtree asset can be assigned at runtime with SetDynamicSubtree function of BehaviorTreeComponent.
 
  Does NOT support subtree's root level decorators!

## Inheritance

`UBTTaskNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InjectionTag` | `FGameplayTag` | Gameplay tag that will identify this task for subtree injection |
| `DefaultBehaviorAsset` | `UBehaviorTree *` | default behavior to run |
| `BehaviorAsset` | `UBehaviorTree *` | current subtree |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_RunEQSQuery.json -->

# UBTTask_RunEQSQuery

Run Environment Query System Query task node.
  Runs the specified environment query when executed.

## Inheritance

`UBTTask_BlackboardBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `QueryTemplate` | `UEnvQuery *` | query to run |
| `QueryParams` | `TArray < FEnvNamedValue >` | optional parameters for query |
| `QueryConfig` | `TArray < FAIDynamicParam >` | - |
| `RunMode` | `TEnumAsByte < EEnvQueryRunMode :: Type >` | determines which item will be stored (All = only first matching) |
| `EQSQueryBlackboardKey` | `FBlackboardKeySelector` | blackboard key storing an EQS query template |
| `bUseBBKey` | `bool` | - |
| `EQSRequest` | `FEQSParametrizedQueryExecutionRequest` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_SetTagCooldown.json -->

# UBTTask_SetTagCooldown

Cooldown task node.
  Sets a cooldown tag value.  Use with cooldown tag decorators to prevent behavior tree execution.

## Inheritance

`UBTTaskNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CooldownTag` | `FGameplayTag` | Gameplay tag that will be used for the cooldown. |
| `bAddToExistingDuration` | `bool` | True if we are adding to any existing duration, false if we are setting the duration (potentially invalidating an existing end time). |
| `CooldownDuration` | `float` | Value we will add or set to the Cooldown tag when this task runs. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_Wait.json -->

# UBTTask_Wait

Wait task node.
  Wait for the specified time when executed.

## Inheritance

`UBTTaskNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WaitTime` | `float` | wait time in seconds |
| `RandomDeviation` | `float` | allows adding random time to wait time |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTTask_WaitBlackboardTime.json -->

# UBTTask_WaitBlackboardTime

Wait task node.
  Wait for the time specified by a Blackboard key when executed.

## Inheritance

`UBTTask_Wait`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BlackboardKey` | `FBlackboardKeySelector` | blackboard key selector |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UBTTaskNode.json -->

# UBTTaskNode

Task are leaf nodes of behavior tree, which perform actual actions
 
  Because some of them can be instanced for specific AI, following virtual functions are not marked as const:
   - ExecuteTask
   - AbortTask
   - TickTask
   - OnMessage
 
  If your node is not being instanced (default behavior), DO NOT change any properties of object within those functions!
  Template nodes are shared across all behavior tree components using the same tree asset and must store
  their runtime properties in provided NodeMemory block (allocation size determined by GetInstanceMemorySize() )

## Inheritance

`UBTNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Services` | `TArray < UBTService * >` | service nodes |
| `bIgnoreRestartSelf` | `uint32` | if set, task search will be discarded when this task is selected to execute but is already running |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UButton.json -->

# UButton

The button is a click-able primitive widget to enable basic interaction, you
  can place any other widget inside a button to make a more complex and
  interesting click-able element in your UI.
 
   Single Child
   Clickable

## Inheritance

`UContentWidget` -> `IWidgetSkinInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Style_DEPRECATED` | `USlateWidgetStyleAsset *` | The template style asset, used to seed the mutable instance of the style. |
| `WidgetStyle` | `FButtonStyle` | The button style used at runtime |
| `ColorAndOpacity` | `FLinearColor` | The color multiplier for the button content |
| `BackgroundColor` | `FLinearColor` | The color multiplier for the button background |
| `ClickMethod` | `TEnumAsByte < EButtonClickMethod :: Type >` | The type of mouse action required by the user to trigger the buttons 'Click' |
| `TouchMethod` | `TEnumAsByte < EButtonTouchMethod :: Type >` | The type of touch action required by the user to trigger the buttons 'Click' |
| `ListenEscMethod` | `TEnumAsByte < EListenEscMethod :: Type >` | 通过命名识别关闭按钮，识别忽略大小写下划线，推荐命名(Button_Close,NewButton_Close...) |
| `ListenActions` | `TArray < FButtonListenAction >` | 通过监听Action，来统一模拟按键点击，扩展Esc模拟点击功能 |
| `IsTipsBgBtn` | `bool` | 是否为Tips背景按钮 |
| `IsFocusable` | `bool` | Sometimes a button should only be mouse-clickable and never keyboard focusable. |
| `IsPassMouseEvent` | `bool` | - |
| `IsImgAlphaBtn` | `bool` | - |
| `bUseCustomSettings` | `bool` | - |
| `CustomHitAreaTexture` | `UTexture2D *` | - |
| `CustomHitAreaAlpha` | `int` | - |
| `bIsShowHover` | `bool` | - |
| `bIsLayerPlus` | `bool` | - |
| `OnMouseButtonDownEvent` | `FOnPointerEvent` | - |
| `OnMouseButtonUpEvent` | `FOnPointerEvent` | - |
| `OnMouseMoveEvent` | `FOnPointerEvent` | - |
| `InputActionBindings` | `FButtonInputActionBindingsStruct` | - |
| `EscRespondSetting` | `FEscRespondSetting` | - |
| `IsThisFrameClicked` | `bool` | - |

## Functions

### `SetStyle`

```text
SetStyle(InStyle: FButtonStyle &) -> void
```

Sets the color multiplier for the button background

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStyle` | `FButtonStyle &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetColorAndOpacity`

```text
SetColorAndOpacity(InColorAndOpacity: FLinearColor) -> void
```

Sets the color multiplier for the button content

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColorAndOpacity` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBackgroundColor`

```text
SetBackgroundColor(InBackgroundColor: FLinearColor) -> void
```

Sets the color multiplier for the button background

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBackgroundColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsPressed`

```text
IsPressed() -> bool
```

Returns true if the user is actively pressing the button.  Do not use this for detecting 'Clicks', use the OnClicked event instead.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the user is actively pressing the button otherwise false. |

### `Release`

```text
Release() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetClickMethod`

```text
SetClickMethod(InClickMethod: EButtonClickMethod :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InClickMethod` | `EButtonClickMethod :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTouchMethod`

```text
SetTouchMethod(InTouchMethod: EButtonTouchMethod :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTouchMethod` | `EButtonTouchMethod :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetReleasedReason`

```text
GetReleasedReason() -> uint8
```

**Returns**

| Type | Description |
|---|---|
| `uint8` | - |

### `SetListenEscMethod`

```text
SetListenEscMethod(InListenEscMethod: EListenEscMethod :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InListenEscMethod` | `EListenEscMethod :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetListenEscMethod`

```text
GetListenEscMethod() -> EListenEscMethod :: Type
```

**Returns**

| Type | Description |
|---|---|
| `EListenEscMethod :: Type` | - |

### `SetShowHover`

```text
SetShowHover(InShowHover: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InShowHover` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddListenAction`

```text
AddListenAction(InActionName: FName, InType: EButtonListenActionEvent :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActionName` | `FName` | - |
| `InType` | `EButtonListenActionEvent :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveListenAction`

```text
RemoveListenAction(InActionName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActionName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearListenActions`

```text
ClearListenActions() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCacheLayerId`

```text
GetCacheLayerId() -> int32
```

return CacheLayerId only windows

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `RespondEscape`

```text
RespondEscape() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetButtonsFromAction`

```text
GetButtonsFromAction(OutButtons: TArray < UButton * > &, InAction: FName) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutButtons` | `TArray < UButton * > &` | - |
| `InAction` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ClearInvalidForListenActions`

```text
ClearInvalidForListenActions() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetButtonsFromTipsBg`

```text
GetButtonsFromTipsBg() -> TArray < UButton * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < UButton * >` | - |

### `SetButtonClickedGlobalEvent`

```text
SetButtonClickedGlobalEvent(InEvent: FOnButtonClickedGlobalEvent) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InEvent` | `FOnButtonClickedGlobalEvent` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearButtonClickedGlobalEvent`

```text
ClearButtonClickedGlobalEvent() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIsFocusable`

```text
SetIsFocusable(InFocusable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFocusable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnClicked`

```text
OnClicked() -> void
```

Called when the button is clicked

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPressed`

```text
OnPressed() -> void
```

Called when the button is pressed

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnReleased`

```text
OnReleased() -> void
```

Called when the button is released

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnHovered`

```text
OnHovered() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnUnhovered`

```text
OnUnhovered() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPressedParam`

```text
OnPressedParam(MyGeometry: FGeometry, MouseEvent: const FPointerEvent&) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | - |
| `MouseEvent` | `const FPointerEvent&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnReleasedParam`

```text
OnReleasedParam(MyGeometry: FGeometry, MouseEvent: const FPointerEvent&) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | - |
| `MouseEvent` | `const FPointerEvent&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnReplayRecordNotify`

```text
OnReplayRecordNotify(EventIndex: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EventIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UButtonSlot.json -->

# UButtonSlot

The Slot for the UButtonSlot, contains the widget displayed in a button's single slot

## Inheritance

`UPanelSlot`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Padding` | `FMargin` | The padding area between the slot and the content it contains. |
| `HorizontalAlignment` | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the object horizontally. |
| `VerticalAlignment` | `TEnumAsByte < EVerticalAlignment >` | The alignment of the object vertically. |

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

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UButtonStyleAsset.json -->

# UButtonStyleAsset

An asset describing a button's appearance.
  Just a wrapper for the struct with real data in it.style factory

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ButtonStyle` | `FButtonStyle` | The actual data describing the button's appearance. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UButtonWidgetStyle.json -->

# UButtonWidgetStyle

## Inheritance

`USlateWidgetStyleContainerBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ButtonStyle` | `FButtonStyle` | The actual data describing the button's appearance. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCameraAnim.json -->

# UCameraAnim

A predefined animation to be played on a camera

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CameraInterpGroup` | `UInterpGroup *` | The UInterpGroup that holds our actual interpolation data. |
| `AnimLength` | `float` | Length, in seconds. |
| `BoundingBox` | `FBox` | AABB in local space. |
| `bRelativeToInitialTransform` | `uint8` | If true, assume all transform keys are intended be offsets from the start of the animation. This allows the animation to be authored at any world location and be applied as a delta to the camera. <br>	  If false, assume all transform keys are authored relative to the world origin. Positions will be directly applied as deltas to the camera. |
| `bRelativeToInitialFOV` | `uint8` | If true, assume all FOV keys are intended be offsets from the start of the animation.<br>	 If false, assume all FOV keys are authored relative to the current FOV of the camera at the start of the animation. |
| `BaseFOV` | `float` | The base FOV that all FOV keys are relative to. |
| `BasePostProcessSettings` | `FPostProcessSettings` | Default PP settings to put on the animated camera. For modifying PP without keyframes. |
| `BasePostProcessBlendWeight` | `float` | Default PP blend weight to put on the animated camera. For modifying PP without keyframes. |
| `PreviewInterpGroup` | `UInterpGroup *` | This is to preview and they only exists in editor |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCameraAnimInst.json -->

# UCameraAnimInst

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CamAnim` | `UCameraAnim *` | which CameraAnim this is an instance of |
| `InterpGroupInst` | `UInterpGroupInst *` | the UInterpGroupInst used to do the interpolation |
| `PlayRate` | `float` | Multiplier for playback rate.  1.0 = normal. |
| `MoveTrack` | `UInterpTrackMove *` | cached movement track from the currently playing anim so we don't have to go find it every frame |
| `MoveInst` | `UInterpTrackInstMove *` | - |
| `PlaySpace` | `TEnumAsByte < ECameraAnimPlaySpace :: Type >` | - |

## Functions

### `SetCurrentTime`

```text
SetCurrentTime(NewTime: float) -> void
```

Jumps he camera anim to the given (unscaled) time.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Stop`

```text
Stop(bImmediate: bool) -> void
```

Stops this instance playing whatever animation it is playing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bImmediate` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDuration`

```text
SetDuration(NewDuration: float) -> void
```

Changes the running duration of this active anim, while maintaining playback position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewDuration` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetScale`

```text
SetScale(NewDuration: float) -> void
```

Changes the scale of the animation while playing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewDuration` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCameraComponent.json -->

# UCameraComponent

Represents a camera viewpoint and settings, such as projection type, field of view, and post-process overrides.
   The default behavior for an actor used as the camera view target is to look for an attached camera component and use its location, rotation, and settings.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FieldOfView` | `float` | The horizontal field of view (in degrees) in perspective mode (ignored in Orthographic mode) |
| `FirstPersonFieldOfView` | `float` | The horizontal field of view (in degrees) used for primitives tagged as "IsFirstPerson". |
| `FirstPersonScale` | `float` | The scale to apply to primitives tagged as "IsFirstPerson". This is used to scale down primitives towards the camera such that they are small enough not to intersect with the scene. |
| `FirstPersonScaleCurveNearValue` | `float` | - |
| `FirstPersonScaleMaxLength` | `float` | - |
| `FirstPersonScaleCurvePow` | `float` | - |
| `bEnableFirstPersonFieldOfView` | `uint8` | True if the first person field of view should be used for primitives tagged as "IsFirstPerson". |
| `bEnableFirstPersonScale` | `uint8` | True if the first person scale should be used for primitives tagged as "IsFirstPerson". |
| `OrthoWidth` | `float` | The desired width (in world units) of the orthographic view (ignored in Perspective mode) |
| `OrthoNearClipPlane` | `float` | The near plane distance of the orthographic view (in world units) |
| `OrthoFarClipPlane` | `float` | The far plane distance of the orthographic view (in world units) |
| `AspectRatio` | `float` | - |
| `WidthHeight` | `FVector2D` | - |
| `bConstrainAspectRatio` | `uint32` | - |
| `bUseFieldOfViewForLOD` | `uint32` | - |
| `bLockToHmd` | `uint32` | True if the camera's orientation and position should be locked to the HMD |
| `bUsePawnControlRotation` | `uint32` | If this camera component is placed on a pawn, should it use the viewcontrol rotation of the pawn where possible?<br>	  @see APawn::GetViewRotation() |
| `bEnableModifyAdditiveOffset` | `uint32` | - |
| `ProjectionMode` | `TEnumAsByte < ECameraProjectionMode :: Type >` | - |
| `PostProcessBlendWeight` | `float` | Indicates if PostProcessSettings should be used when using this Camera to view through. |
| `PostProcessSettings` | `FPostProcessSettings` | Post process settings to use for this camera. Don't forget to check the properties you want to override |
| `bUseControllerViewRotation_DEPRECATED` | `uint32` | DEPRECATED: use bUsePawnControlRotation instead |

## Functions

### `SetFieldOfView`

```text
SetFieldOfView(InFieldOfView: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFieldOfView` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFirstPersonFieldOfView`

```text
SetFirstPersonFieldOfView(InFirstPersonFieldOfView: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFirstPersonFieldOfView` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFirstPersonScale`

```text
SetFirstPersonScale(InFirstPersonScale: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFirstPersonScale` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFirstPersonScaleParams`

```text
SetFirstPersonScaleParams(InFirstPersonScale: float, InFPScaleCurveNearValue: float, InFPScaleMaxLen: float, InFPScaleCurvePow: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFirstPersonScale` | `float` | - |
| `InFPScaleCurveNearValue` | `float` | - |
| `InFPScaleMaxLen` | `float` | - |
| `InFPScaleCurvePow` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetEnableFirstPersonFieldOfView`

```text
SetEnableFirstPersonFieldOfView(bInEnableFirstPersonFieldOfView: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInEnableFirstPersonFieldOfView` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetEnableFirstPersonScale`

```text
SetEnableFirstPersonScale(bInEnableFirstPersonScale: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInEnableFirstPersonScale` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetActive`

```text
SetActive(bNewActive: bool, bReset: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewActive` | `bool` | - |
| `bReset` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplyDrawDistanceOffset`

```text
ApplyDrawDistanceOffset(InFieldOfView: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFieldOfView` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOrthoWidth`

```text
SetOrthoWidth(InOrthoWidth: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOrthoWidth` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOrthoNearClipPlane`

```text
SetOrthoNearClipPlane(InOrthoNearClipPlane: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOrthoNearClipPlane` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOrthoFarClipPlane`

```text
SetOrthoFarClipPlane(InOrthoFarClipPlane: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOrthoFarClipPlane` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAspectRatio`

```text
SetAspectRatio(InAspectRatio: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAspectRatio` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWidthHeight`

```text
SetWidthHeight(InWidthHeight: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InWidthHeight` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetConstraintAspectRatio`

```text
SetConstraintAspectRatio(bInConstrainAspectRatio: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInConstrainAspectRatio` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetUseFieldOfViewForLOD`

```text
SetUseFieldOfViewForLOD(bInUseFieldOfViewForLOD: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInUseFieldOfViewForLOD` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetProjectionMode`

```text
SetProjectionMode(InProjectionMode: ECameraProjectionMode :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InProjectionMode` | `ECameraProjectionMode :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPostProcessBlendWeight`

```text
SetPostProcessBlendWeight(InPostProcessBlendWeight: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPostProcessBlendWeight` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCameraView`

```text
GetCameraView(DeltaTime: float, DesiredView: FMinimalViewInfo &) -> void
```

Returns camera's Point of View.
	  Called by Camera class. Subclass and postprocess to add any effects.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTime` | `float` | - |
| `DesiredView` | `FMinimalViewInfo &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddOrUpdateBlendable`

```text
AddOrUpdateBlendable(InBlendableObject: TScriptInterface < IBlendableInterface >, InWeight: float) -> void
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
| `void` | - |

### `RemoveBlendable`

```text
RemoveBlendable(InBlendableObject: TScriptInterface < IBlendableInterface >) -> void
```

Removes a blendable.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlendableObject` | `TScriptInterface < IBlendableInterface >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetbEnableModifyAdditiveOffset`

```text
SetbEnableModifyAdditiveOffset(InEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetEnableModifyAdditiveOffset`

```text
GetEnableModifyAdditiveOffset() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `AddAdditiveOffset`

```text
AddAdditiveOffset(Transform: FTransform &, FOV: float) -> void
```

Applies the given additive offset, preserving any existing offset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Transform` | `FTransform &` | - |
| `FOV` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearAdditiveOffset`

```text
ClearAdditiveOffset() -> void
```

Removes any additive offset.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAddtiveInfo`

```text
GetAddtiveInfo(OutIsAddtive: bool &, OutAddtiveOffset: float &, OutAddtiveTrans: FTransform &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutIsAddtive` | `bool &` | - |
| `OutAddtiveOffset` | `float &` | - |
| `OutAddtiveTrans` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCameraModifier.json -->

# UCameraModifier

A CameraModifier is a base class for objects that may adjust the final camera properties after
  being computed by the APlayerCameraManager (@see ModifyCamera). A CameraModifier
  can be stateful, and is associated uniquely with a specific APlayerCameraManager.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bDebug` | `uint32` | If true, enables certain debug visualization features. |
| `bExclusive` | `uint32` | If true, no other modifiers of same priority allowed. |
| `Priority` | `uint8` | Priority value that determines the order in which modifiers are applied. 0 = highest priority, 255 = lowest. |
| `CameraOwner` | `APlayerCameraManager *` | Camera this object is associated with. |
| `AlphaInTime` | `float` | When blending in, alpha proceeds from 0 to 1 over this time |
| `AlphaOutTime` | `float` | When blending out, alpha proceeds from 1 to 0 over this time |
| `Alpha` | `float` | Current blend alpha. |

## Functions

### `BlueprintModifyCamera`

```text
BlueprintModifyCamera(DeltaTime: float, ViewLocation: FVector, ViewRotation: FRotator, FOV: float, NewViewLocation: FVector &, NewViewRotation: FRotator &, NewFOV: float &) -> void
```

Called per tick that the modifier is active to allow Blueprinted modifiers to modify the camera's transform. 
	  Scaling by Alpha happens after this in code, so no need to deal with that in the blueprint.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTime` | `float` | Change in time since last update |
| `ViewLocation` | `FVector` | The current camera location. |
| `ViewRotation` | `FRotator` | The current camera rotation. |
| `FOV` | `float` | The current camera fov. |
| `NewViewLocation` | `FVector &` | (out) The modified camera location. |
| `NewViewRotation` | `FRotator &` | (out) The modified camera rotation. |
| `NewFOV` | `float &` | (out) The modified camera FOV. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BlueprintModifyPostProcess`

```text
BlueprintModifyPostProcess(DeltaTime: float, PostProcessBlendWeight: float &, PostProcessSettings: FPostProcessSettings &) -> void
```

Called per tick that the modifier is active to allow Blueprinted modifiers to modify the camera's postprocess effects.
	  Scaling by Alpha happens after this in code, so no need to deal with that in the blueprint.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTime` | `float` | Change in time since last update |
| `PostProcessBlendWeight` | `float &` | (out) Blend weight applied to the entire postprocess structure. |
| `PostProcessSettings` | `FPostProcessSettings &` | (out) Post process structure defining what settings and values to override. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsDisabled`

```text
IsDisabled() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | Returns true if modifier is disabled, false otherwise. |

### `GetViewTarget`

```text
GetViewTarget() -> AActor *
```

**Returns**

| Type | Description |
|---|---|
| `AActor *` | Returns the actor the camera is currently viewing. |

### `DisableModifier`

```text
DisableModifier(bImmediate: bool) -> void
```

Disables this modifier.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bImmediate` | `bool` | - true to disable with no blend out, false (default) to allow blend out |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableModifier`

```text
EnableModifier() -> void
```

Enables this modifier.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCameraModifier_CameraShake.json -->

# UCameraModifier_CameraShake

A UCameraModifier_CameraShake is a camera modifier that can apply a UCameraShake to 
  the owning camera.

## Inheritance

`UCameraModifier`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActiveShakes` | `TArray < UCameraShake * >` | List of active CameraShake instances |
| `SplitScreenShakeScale` | `float` | Scaling factor applied to all camera shakes in when in splitscreen mode. Normally used to reduce shaking, since shakes feel more intense in a smaller viewport. |
| `CacheShakeInsMap` | `TMap < TSubclassOf < UCameraShake > , FCacheCameraShakeData >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCameraShake.json -->

# UCameraShake

A CameraShake is an asset that defines how to shake the camera in 
  a particular way. CameraShakes can be authored as either oscillating shakes, 
  animated shakes, or both.
 
  An oscillating shake will sinusoidally vibrate various camera parameters over time. Each location
  and rotation axis can be oscillated independently with different parameters to create complex and
  random-feeling shakes. These are easier to author and tweak, but can still feel mechanical and are
  limited to vibration-style shakes, such as earthquakes.
 
  Animated shakes play keyframed camera animations.  These can take more effort to author, but enable
  more natural-feeling results and things like directional shakes.  For instance, you can have an explosion
  to the camera's right push it primarily to the left.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bSingleInstance` | `uint32` | If true to only allow a single instance of this shake class to play at any given time.<br>	   Subsequent attempts to play this shake will simply restart the timer. |
| `OscillationDuration` | `float` | Duration in seconds of current screen shake. Less than 0 means indefinite, 0 means no oscillation. |
| `OscillationBlendInTime` | `float` | Duration of the blend-in, where the oscillation scales from 0 to 1. |
| `OscillationBlendOutTime` | `float` | Duration of the blend-out, where the oscillation scales from 1 to 0. |
| `RotOscillation` | `FROscillator` | Rotational oscillation |
| `LocOscillation` | `FVOscillator` | Positional oscillation |
| `FOVOscillation` | `FFOscillator` | FOV oscillation |
| `AnimPlayRate` | `float` | Parameters for defining CameraAnim-driven camera shakes<br>	 <br>	 Scalar defining how fast to play the anim. |
| `AnimScale` | `float` | Scalar defining how "intense" to play the anim. |
| `AnimBlendInTime` | `float` | Linear blend-in time. |
| `AnimBlendOutTime` | `float` | Linear blend-out time. |
| `RandomAnimSegmentDuration` | `float` | When bRandomAnimSegment is true, this defines how long the anim should play. |
| `Anim` | `UCameraAnim *` | Source camera animation to play. Can be null. |
| `Anims` | `TArray < UCameraAnim * >` | Source camera animations to play. Can be empty. |
| `bRandomAnimSegment` | `uint32` | If true, play a random snippet of the animation of length Duration.  Implies bLoop and bRandomStartTime = true for the CameraAnim.<br>	 If false, play the full anim once, non-looped. Useful for getting variety out of a single looped CameraAnim asset. |
| `RandomFinalIntenseScaleRange` | `FVector2D` | - |
| `RandomFinalIntenseScaleRange_X` | `FVector2D` | - |
| `RandomFinalIntenseScaleRange_Y` | `FVector2D` | - |
| `RandomFinalIntenseScaleRange_Z` | `FVector2D` | - |
| `RandomFinalIntenseScaleRange_Yaw` | `FVector2D` | - |
| `RandomFinalIntenseScaleRange_Pitch` | `FVector2D` | - |
| `RandomFinalIntenseScaleRange_Roll` | `FVector2D` | - |
| `CameraOwner` | `APlayerCameraManager *` | - |
| `ShakeScale` | `float` | Overall intensity scale for this shake instance. |
| `OscillatorTimeRemaining` | `float` | Time remaining for oscillation shakes. Less than 0.f means shake infinitely. |
| `AttenuationFloatCurve` | `UCurveFloat *` | Source camera curve to add. Can be null. |

## Functions

### `BlueprintUpdateCameraShake`

```text
BlueprintUpdateCameraShake(DeltaTime: float, Alpha: float, POV: FMinimalViewInfo &, ModifiedPOV: FMinimalViewInfo &) -> void
```

Called every tick to let the shake modify the point of view

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTime` | `float` | - |
| `Alpha` | `float` | - |
| `POV` | `FMinimalViewInfo &` | - |
| `ModifiedPOV` | `FMinimalViewInfo &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceivePlayShake`

```text
ReceivePlayShake(Scale: float) -> void
```

Called when the shake starts playing

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Scale` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveIsFinished`

```text
ReceiveIsFinished() -> bool
```

Called to allow a shake to decide when it's finished playing.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ReceiveStopShake`

```text
ReceiveStopShake(bImmediately: bool) -> void
```

Called when the shake is explicitly stopped.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bImmediately` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCanvas.json -->

# UCanvas

A drawing canvas.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OrgX` | `float` | - |
| `OrgY` | `float` | - |
| `ClipX` | `float` | - |
| `ClipY` | `float` | - |
| `DrawColor` | `FColor` | - |
| `bCenterX` | `uint32` | - |
| `bCenterY` | `uint32` | - |
| `bNoSmooth` | `uint32` | - |
| `SizeX` | `int32` | - |
| `SizeY` | `int32` | - |
| `ColorModulate` | `FPlane` | - |
| `DefaultTexture` | `UTexture2D *` | - |
| `GradientTexture0` | `UTexture2D *` | - |
| `ReporterGraph` | `UReporterGraph *` | Helper class to render 2d graphs on canvas |

## Functions

### `K2_DrawLine`

```text
K2_DrawLine(ScreenPositionA: FVector2D, ScreenPositionB: FVector2D, Thickness: float, RenderColor: FLinearColor) -> void
```

Draws a line on the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ScreenPositionA` | `FVector2D` | Starting position of the line in screen space. |
| `ScreenPositionB` | `FVector2D` | Ending position of the line in screen space. |
| `Thickness` | `float` | How many pixels thick this line should be. |
| `RenderColor` | `FLinearColor` | Color to render the line. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DrawTexture`

```text
K2_DrawTexture(RenderTexture: UTexture *, ScreenPosition: FVector2D, ScreenSize: FVector2D, CoordinatePosition: FVector2D, CoordinateSize: FVector2D, RenderColor: FLinearColor, BlendMode: EBlendMode, Rotation: float, PivotPoint: FVector2D) -> void
```

Draws a texture on the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RenderTexture` | `UTexture *` | Texture to use when rendering. If no texture is set then this will use the default white texture. |
| `ScreenPosition` | `FVector2D` | Screen space position to render the texture. |
| `ScreenSize` | `FVector2D` | Screen space size to render the texture. |
| `CoordinatePosition` | `FVector2D` | Normalized UV starting coordinate to use when rendering the texture. |
| `CoordinateSize` | `FVector2D` | Normalized UV size coordinate to use when rendering the texture. |
| `RenderColor` | `FLinearColor` | Color to use when rendering the texture. |
| `BlendMode` | `EBlendMode` | Blending mode to use when rendering the texture. |
| `Rotation` | `float` | Rotation, in degrees, to render the texture. |
| `PivotPoint` | `FVector2D` | Normalized pivot point to use when rotating the texture. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DrawMaterial`

```text
K2_DrawMaterial(RenderMaterial: UMaterialInterface *, ScreenPosition: FVector2D, ScreenSize: FVector2D, CoordinatePosition: FVector2D, CoordinateSize: FVector2D, Rotation: float, PivotPoint: FVector2D) -> void
```

Draws a material on the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RenderMaterial` | `UMaterialInterface *` | Material to use when rendering. Remember that only the emissive channel is able to be rendered as no lighting is performed when rendering to the Canvas. |
| `ScreenPosition` | `FVector2D` | Screen space position to render the texture. |
| `ScreenSize` | `FVector2D` | Screen space size to render the texture. |
| `CoordinatePosition` | `FVector2D` | Normalized UV starting coordinate to use when rendering the texture. |
| `CoordinateSize` | `FVector2D` | Normalized UV size coordinate to use when rendering the texture. |
| `Rotation` | `float` | Rotation, in degrees, to render the texture. |
| `PivotPoint` | `FVector2D` | Normalized pivot point to use when rotating the texture. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DrawText`

```text
K2_DrawText(RenderFont: UFont *, RenderText: FString &, ScreenPosition: FVector2D, RenderColor: FLinearColor, Kerning: float, ShadowColor: FLinearColor, ShadowOffset: FVector2D, bCentreX: bool, bCentreY: bool, bOutlined: bool, OutlineColor: FLinearColor) -> void
```

Draws text on the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RenderFont` | `UFont *` | Font to use when rendering the text. If this is null, then a default engine font is used. |
| `RenderText` | `FString &` | Text to render on the Canvas. |
| `ScreenPosition` | `FVector2D` | Screen space position to render the text. |
| `RenderColor` | `FLinearColor` | Color to render the text. |
| `Kerning` | `float` | Horizontal spacing adjustment to modify the spacing between each letter. |
| `ShadowColor` | `FLinearColor` | Color to render the shadow of the text. |
| `ShadowOffset` | `FVector2D` | Pixel offset relative to the screen space position to render the shadow of the text. |
| `bCentreX` | `bool` | If true, then interpret the screen space position X coordinate as the center of the rendered text. |
| `bCentreY` | `bool` | If true, then interpret the screen space position Y coordinate as the center of the rendered text. |
| `bOutlined` | `bool` | If true, then the text should be rendered with an outline. |
| `OutlineColor` | `FLinearColor` | Color to render the outline for the text. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DrawBorder`

```text
K2_DrawBorder(BorderTexture: UTexture *, BackgroundTexture: UTexture *, LeftBorderTexture: UTexture *, RightBorderTexture: UTexture *, TopBorderTexture: UTexture *, BottomBorderTexture: UTexture *, ScreenPosition: FVector2D, ScreenSize: FVector2D, CoordinatePosition: FVector2D, CoordinateSize: FVector2D, RenderColor: FLinearColor, BorderScale: FVector2D, BackgroundScale: FVector2D, Rotation: float, PivotPoint: FVector2D, CornerSize: FVector2D) -> void
```

Draws a 3x3 grid border with tiled frame and tiled interior on the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BorderTexture` | `UTexture *` | Texture to use for border. |
| `BackgroundTexture` | `UTexture *` | Texture to use for border background. |
| `LeftBorderTexture` | `UTexture *` | Texture to use for the tiling left border. |
| `RightBorderTexture` | `UTexture *` | Texture to use for the tiling right border. |
| `TopBorderTexture` | `UTexture *` | Texture to use for the tiling top border. |
| `BottomBorderTexture` | `UTexture *` | Texture to use for the tiling bottom border. |
| `ScreenPosition` | `FVector2D` | Screen space position to render the texture. |
| `ScreenSize` | `FVector2D` | Screen space size to render the texture. |
| `CoordinatePosition` | `FVector2D` | Normalized UV starting coordinate to use when rendering the border texture. |
| `CoordinateSize` | `FVector2D` | Normalized UV size coordinate to use when rendering the border texture. |
| `RenderColor` | `FLinearColor` | Color to tint the border. |
| `BorderScale` | `FVector2D` | Scale of the border. |
| `BackgroundScale` | `FVector2D` | Scale of the background. |
| `Rotation` | `float` | Rotation, in degrees, to render the texture. |
| `PivotPoint` | `FVector2D` | Normalized pivot point to use when rotating the texture. |
| `CornerSize` | `FVector2D` | Frame corner size in percent of frame texture (should be < 0.5f). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DrawBox`

```text
K2_DrawBox(ScreenPosition: FVector2D, ScreenSize: FVector2D, Thickness: float) -> void
```

Draws an unfilled box on the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ScreenPosition` | `FVector2D` | Screen space position to render the text. |
| `ScreenSize` | `FVector2D` | Screen space size to render the texture. |
| `Thickness` | `float` | How many pixels thick the box lines should be. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DrawTriangle`

```text
K2_DrawTriangle(RenderTexture: UTexture *, Triangles: TArray < FCanvasUVTri >) -> void
```

Draws a set of triangles on the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RenderTexture` | `UTexture *` | Texture to use when rendering the triangles. If no texture is set, then the default white texture is used. |
| `Triangles` | `TArray < FCanvasUVTri >` | Triangles to render. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DrawMaterialTriangle`

```text
K2_DrawMaterialTriangle(RenderMaterial: UMaterialInterface *, Triangles: TArray < FCanvasUVTri >) -> void
```

Draws a set of triangles on the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RenderMaterial` | `UMaterialInterface *` | Material to use when rendering. Remember that only the emissive channel is able to be rendered as no lighting is performed when rendering to the Canvas. |
| `Triangles` | `TArray < FCanvasUVTri >` | Triangles to render. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DrawPolygon`

```text
K2_DrawPolygon(RenderTexture: UTexture *, ScreenPosition: FVector2D, Radius: FVector2D, NumberOfSides: int32, RenderColor: FLinearColor) -> void
```

Draws a polygon on the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RenderTexture` | `UTexture *` | Texture to use when rendering the triangles. If no texture is set, then the default white texture is used. |
| `ScreenPosition` | `FVector2D` | Screen space position to render the text. |
| `Radius` | `FVector2D` | How large in pixels this polygon should be. |
| `NumberOfSides` | `int32` | How many sides this polygon should have. This should be above or equal to three. |
| `RenderColor` | `FLinearColor` | Color to tint the polygon. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_Project`

```text
K2_Project(WorldLocation: FVector) -> FVector
```

Performs a projection of a world space coordinates using the projection matrix set up for the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector` | World space location to project onto the Canvas rendering plane. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Returns a vector where X, Y defines a screen space position representing the world space location. |

### `K2_Deproject`

```text
K2_Deproject(ScreenPosition: FVector2D, WorldOrigin: FVector &, WorldDirection: FVector &) -> void
```

Performs a deprojection of a screen space coordinate using the projection matrix set up for the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ScreenPosition` | `FVector2D` | Screen space position to deproject to the World. |
| `WorldOrigin` | `FVector &` | Vector which is the world position of the screen space position. |
| `WorldDirection` | `FVector &` | Vector which can be used in a trace to determine what is "behind" the screen space position. Useful for object picking. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_StrLen`

```text
K2_StrLen(RenderFont: UFont *, RenderText: FString &) -> FVector2D
```

Returns the wrapped text size in screen space coordinates.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RenderFont` | `UFont *` | Font to use when determining the size of the text. If this is null, then a default engine font is used. |
| `RenderText` | `FString &` | Text to determine the size of. |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | Returns the screen space size of the text. |

### `K2_TextSize`

```text
K2_TextSize(RenderFont: UFont *, RenderText: FString &, Scale: FVector2D) -> FVector2D
```

Returns the clipped text size in screen space coordinates.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RenderFont` | `UFont *` | Font to use when determining the size of the text. If this is null, then a default engine font is used. |
| `RenderText` | `FString &` | Text to determine the size of. |
| `Scale` | `FVector2D` | Scale of the font to use when determining the size of the text. |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | Returns the screen space size of the text. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCanvasPanel.json -->

# UCanvasPanel

The canvas panel is a designer friendly panel that allows widgets to be laid out at arbitrary 
  locations, anchored and z-ordered with other children of the canvas.  The canvas is a great widget
  for manual layout, but bad when you want to procedurally just generate widgets and place them in a 
  container (unless you want absolute layout).
 
   Many Children
   Absolute Layout
   Anchors

## Inheritance

`UPanelWidget`

## Functions

### `AddChildToCanvas`

```text
AddChildToCanvas(Content: UWidget *) -> UCanvasPanelSlot *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UCanvasPanelSlot *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCanvasPanelSlot.json -->

# UCanvasPanelSlot

## Inheritance

`UPanelSlot`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LayoutData` | `FAnchorData` | The anchoring information for the slot |
| `bAutoSize` | `bool` | When AutoSize is true we use the widget's desired size |
| `ZOrder` | `int32` | The order priority this widget is rendered in.  Higher values are rendered last (and so they will appear to be on top). |
| `bAntiAdaptation` | `bool` | - |

## Functions

### `SetLayout`

```text
SetLayout(InLayoutData: FAnchorData &) -> void
```

Sets the layout data of the slot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InLayoutData` | `FAnchorData &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLayout`

```text
GetLayout() -> FAnchorData
```

Gets the layout data of the slot

**Returns**

| Type | Description |
|---|---|
| `FAnchorData` | - |

### `SetPosition`

```text
SetPosition(InPosition: FVector2D) -> void
```

Sets the position of the slot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPosition` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPosition`

```text
GetPosition() -> FVector2D
```

Gets the position of the slot

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetSize`

```text
SetSize(InSize: FVector2D) -> void
```

Sets the size of the slot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSize` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSize`

```text
GetSize() -> FVector2D
```

Gets the size of the slot

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetOffsets`

```text
SetOffsets(InOffset: FMargin) -> void
```

Sets the offset data of the slot, which could be position and size, or margins depending on the anchor points

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOffset` | `FMargin` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOffsets`

```text
GetOffsets() -> FMargin
```

Gets the offset data of the slot, which could be position and size, or margins depending on the anchor points

**Returns**

| Type | Description |
|---|---|
| `FMargin` | - |

### `SetAnchors`

```text
SetAnchors(InAnchors: FAnchors) -> void
```

Sets the anchors on the slot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnchors` | `FAnchors` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAnchors`

```text
GetAnchors() -> FAnchors
```

Gets the anchors on the slot

**Returns**

| Type | Description |
|---|---|
| `FAnchors` | - |

### `SetAlignment`

```text
SetAlignment(InAlignment: FVector2D) -> void
```

Sets the alignment on the slot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAlignment` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAlignment`

```text
GetAlignment() -> FVector2D
```

Gets the alignment on the slot

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetAutoSize`

```text
SetAutoSize(InbAutoSize: bool) -> void
```

Sets if the slot to be auto-sized

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InbAutoSize` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAutoSize`

```text
GetAutoSize() -> bool
```

Gets if the slot to be auto-sized

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetZOrder`

```text
SetZOrder(InZOrder: int32) -> void
```

Sets the z-order on the slot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InZOrder` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetZOrder`

```text
GetZOrder() -> int32
```

Gets the z-order on the slot

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetAntiAdaptation`

```text
SetAntiAdaptation(InbAntiAdaptation: bool) -> void
```

Sets the bAntiAdaptation on the slot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InbAntiAdaptation` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAntiAdaptation`

```text
GetAntiAdaptation() -> bool
```

Gets the bAntiAdaptation on the slot

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetMinimum`

```text
SetMinimum(InMinimumAnchors: FVector2D) -> void
```

Sets the anchors on the slot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMinimumAnchors` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMaximum`

```text
SetMaximum(InMaximumAnchors: FVector2D) -> void
```

Sets the anchors on the slot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMaximumAnchors` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAntiAdaptationOffsetsChange`

```text
OnAntiAdaptationOffsetsChange() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCanvasRenderTarget2D.json -->

# UCanvasRenderTarget2D

CanvasRenderTarget2D is 2D render target which exposes a Canvas interface to allow you to draw elements onto 
  it directly.  Use CreateCanvasRenderTarget2D() to create a render target texture by unique name, then
  bind a function to the OnCanvasRenderTargetUpdate delegate which will be called when the render target is
  updated.  If you need to repaint your canvas every single frame, simply call UpdateResource() on it from a Tick
  function.  Also, remember to hold onto your new canvas render target with a reference so that it doesn't get
  garbage collected.

## Inheritance

`UTextureRenderTarget2D`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `World` | `TWeakObjectPtr < UWorld >` | The world this render target will be used with |
| `bShouldClearRenderTargetOnReceiveUpdate` | `bool` | - |

## Functions

### `UpdateResource`

```text
UpdateResource() -> void
```

Updates the the canvas render target texture's resource. This is where the render target will create or 
	  find a canvas object to use.  It also calls UpdateResourceImmediate() to clear the render target texture 
	  from the deferred rendering list, to stop the texture from being cleared the next frame. From there it
	  will ask the rendering thread to set up the RHI viewport. The canvas is then set up for rendering and 
	  then the user's update delegate is called.  The canvas is then flushed and the RHI resolves the 
	  texture to make it available for rendering.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CreateCanvasRenderTarget2D`

```text
CreateCanvasRenderTarget2D(WorldContextObject: UObject *, CanvasRenderTarget2DClass: TSubclassOf < UCanvasRenderTarget2D >, Width: int32, Height: int32) -> UCanvasRenderTarget2D *
```

Creates a new canvas render target and initializes it to the specified dimensions

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | The world where this render target will be rendered for |
| `CanvasRenderTarget2DClass` | `TSubclassOf < UCanvasRenderTarget2D >` | Class of the render target. Unless you want to use a special sub-class, you can simply pass UCanvasRenderTarget2D::StaticClass() here. |
| `Width` | `int32` | Width of the render target. |
| `Height` | `int32` | Height of the render target. |

**Returns**

| Type | Description |
|---|---|
| `UCanvasRenderTarget2D *` | Returns the instanced render target. |

### `ReceiveUpdate`

```text
ReceiveUpdate(Canvas: UCanvas *, Width: int32, Height: int32) -> void
```

Allows a Blueprint to implement how this Canvas Render Target 2D should be updated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Canvas` | `UCanvas *` | Canvas object that can be used to paint to the render target |
| `Width` | `int32` | Width of the render target. |
| `Height` | `int32` | Height of the render target. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSize`

```text
GetSize(Width: int32 &, Height: int32 &) -> void
```

Gets a specific render target's size from the global map of canvas render targets.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Width` | `int32 &` | Output variable for the render target's width |
| `Height` | `int32 &` | Output variable for the render target's height |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnCanvasRenderTargetUpdate`

```text
OnCanvasRenderTargetUpdate(Canvas: UCanvas*, Width: int32, Height: int32) -> void
```

Called when this Canvas Render Target is asked to update its texture resource.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Canvas` | `UCanvas*` | - |
| `Width` | `int32` | - |
| `Height` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCapsuleComponent.json -->

# UCapsuleComponent

A capsule generally used for simple collision. Bounds are rendered as lines in the editor.

## Inheritance

`UShapeComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CapsuleHalfHeight` | `float` | Half-height, from center of capsule to the end of top or bottom hemisphere.  <br>	 	This cannot be less than CapsuleRadius. |
| `CapsuleRadius` | `float` | Radius of cap hemispheres and center cylinder. <br>	 	This cannot be more than CapsuleHalfHeight. |
| `UseDelayPhysicUpdated` | `int32` | - |
| `bTransformDataDirty` | `bool` | - |
| `CapsuleHeight_DEPRECATED` | `float` | - |

## Functions

### `SetCapsuleSize`

```text
SetCapsuleSize(InRadius: float, InHalfHeight: float, bUpdateOverlaps: bool) -> void
```

Change the capsule size. This is the unscaled size, before component scale is applied.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRadius` | `float` | : radius of end-cap hemispheres and center cylinder. |
| `InHalfHeight` | `float` | : half-height, from capsule center to end of top or bottom hemisphere. |
| `bUpdateOverlaps` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCapsuleRadius`

```text
SetCapsuleRadius(Radius: float, bUpdateOverlaps: bool) -> void
```

Set the capsule radius. This is the unscaled radius, before component scale is applied.
	  If this capsule collides, updates touching array for owner actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Radius` | `float` | : radius of end-cap hemispheres and center cylinder. |
| `bUpdateOverlaps` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCapsuleHalfHeight`

```text
SetCapsuleHalfHeight(HalfHeight: float, bUpdateOverlaps: bool) -> void
```

Set the capsule half-height. This is the unscaled half-height, before component scale is applied.
	  If this capsule collides, updates touching array for owner actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HalfHeight` | `float` | : half-height, from capsule center to end of top or bottom hemisphere. |
| `bUpdateOverlaps` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetScaledCapsuleRadius`

```text
GetScaledCapsuleRadius() -> float
```

Returns the capsule radius scaled by the component scale.

**Returns**

| Type | Description |
|---|---|
| `float` | The capsule radius scaled by the component scale. |

### `GetScaledCapsuleHalfHeight`

```text
GetScaledCapsuleHalfHeight() -> float
```

Returns the capsule half-height scaled by the component scale. This includes both the cylinder and hemisphere cap.

**Returns**

| Type | Description |
|---|---|
| `float` | The capsule half-height scaled by the component scale. |

### `GetScaledCapsuleHalfHeight_WithoutHemisphere`

```text
GetScaledCapsuleHalfHeight_WithoutHemisphere() -> float
```

Returns the capsule half-height minus radius (to exclude the hemisphere), scaled by the component scale.
	 From the center of the capsule this is the vertical distance along the straight cylindrical portion to the point just before the curve of top hemisphere begins.

**Returns**

| Type | Description |
|---|---|
| `float` | The capsule half-height minus radius, scaled by the component scale. |

### `GetScaledCapsuleSize`

```text
GetScaledCapsuleSize(OutRadius: float &, OutHalfHeight: float &) -> void
```

Returns the capsule radius and half-height scaled by the component scale. Half-height includes the hemisphere end cap.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutRadius` | `float &` | Radius of the capsule, scaled by the component scale. |
| `OutHalfHeight` | `float &` | Half-height of the capsule, scaled by the component scale. Includes the hemisphere end cap. |

**Returns**

| Type | Description |
|---|---|
| `void` | The capsule radius and half-height scaled by the component scale. |

### `GetScaledCapsuleSize_WithoutHemisphere`

```text
GetScaledCapsuleSize_WithoutHemisphere(OutRadius: float &, OutHalfHeightWithoutHemisphere: float &) -> void
```

Returns the capsule radius and half-height scaled by the component scale. Half-height excludes the hemisphere end cap.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutRadius` | `float &` | Radius of the capsule, ignoring component scaling. |
| `OutHalfHeightWithoutHemisphere` | `float &` | Half-height of the capsule, scaled by the component scale. Excludes the hemisphere end cap. |

**Returns**

| Type | Description |
|---|---|
| `void` | The capsule radius and half-height scaled by the component scale. |

### `GetUnscaledCapsuleRadius`

```text
GetUnscaledCapsuleRadius() -> float
```

Returns the capsule radius, ignoring component scaling.

**Returns**

| Type | Description |
|---|---|
| `float` | the capsule radius, ignoring component scaling. |

### `GetUnscaledCapsuleHalfHeight`

```text
GetUnscaledCapsuleHalfHeight() -> float
```

Returns the capsule half-height, ignoring component scaling. This includes the hemisphere end cap.

**Returns**

| Type | Description |
|---|---|
| `float` | The capsule radius, ignoring component scaling. |

### `GetUnscaledCapsuleHalfHeight_WithoutHemisphere`

```text
GetUnscaledCapsuleHalfHeight_WithoutHemisphere() -> float
```

Returns the capsule half-height minus radius (to exclude the hemisphere), ignoring component scaling. This excludes the hemisphere end cap.
	 From the center of the capsule this is the vertical distance along the straight cylindrical portion to the point just before the curve of top hemisphere begins.

**Returns**

| Type | Description |
|---|---|
| `float` | The capsule half-height minus radius, ignoring component scaling. |

### `GetUnscaledCapsuleSize`

```text
GetUnscaledCapsuleSize(OutRadius: float &, OutHalfHeight: float &) -> void
```

Returns the capsule radius and half-height scaled by the component scale. Half-height includes the hemisphere end cap.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutRadius` | `float &` | Radius of the capsule, scaled by the component scale. |
| `OutHalfHeight` | `float &` | Half-height of the capsule, scaled by the component scale. Includes the hemisphere end cap. |

**Returns**

| Type | Description |
|---|---|
| `void` | The capsule radius and half-height scaled by the component scale. |

### `GetUnscaledCapsuleSize_WithoutHemisphere`

```text
GetUnscaledCapsuleSize_WithoutHemisphere(OutRadius: float &, OutHalfHeightWithoutHemisphere: float &) -> void
```

Returns the capsule radius and half-height, ignoring component scaling. Half-height excludes the hemisphere end cap.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutRadius` | `float &` | Radius of the capsule, ignoring component scaling. |
| `OutHalfHeightWithoutHemisphere` | `float &` | Half-height of the capsule, scaled by the component scale. Excludes the hemisphere end cap. |

**Returns**

| Type | Description |
|---|---|
| `void` | The capsule radius and half-height (excluding hemisphere end cap), ignoring component scaling. |

### `GetShapeScale`

```text
GetShapeScale() -> float
```

Get the scale used by this shape. This is a uniform scale that is the minimum of any non-uniform scaling.

**Returns**

| Type | Description |
|---|---|
| `float` | the scale used by this shape. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCascadeDebuggerSystem.json -->

# UCascadeDebuggerSystem

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StatFont` | `UFont *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UChannel.json -->

# UChannel

Base class of communication channels.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Connection` | `UNetConnection *` | - |
| `OpenAcked` | `uint32` | - |
| `Closing` | `uint32` | - |
| `Dormant` | `uint32` | - |
| `bIsReplicationPaused` | `uint32` | - |
| `OpenTemporary` | `uint32` | - |
| `Broken` | `uint32` | - |
| `bTornOff` | `uint32` | - |
| `bPendingDormancy` | `uint32` | - |
| `bPausedUntilReliableACK` | `uint32` | - |
| `ChIndex` | `int32` | - |
| `OpenedLocally` | `int32` | - |
| `OpenPacketId` | `FPacketIdRange` | - |
| `ChType` | `EChannelType` | - |
| `NumInRec` | `int32` | - |
| `NumOutRec` | `int32` | - |
| `InRec` | `FInBunch *` | - |
| `OutRec` | `FOutBunch *` | - |
| `InPartialBunch` | `FInBunch *` | - |
| `bEnableSendBunchOpt` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCharacterMovementComponent.json -->

# UCharacterMovementComponent

CharacterMovementComponent handles movement logic for the associated Character owner.
  It supports various movement modes including: walking, falling, swimming, flying, custom.
 
  Movement is affected primarily by current Velocity and Acceleration. Acceleration is updated each frame
  based on the input vector accumulated thus far (see UPawnMovementComponent::GetPendingInputVector()).
 
  Networking is fully implemented, with server-client correction and prediction included.
 
  @see ACharacter, UPawnMovementComponent

## Inheritance

`UPawnMovementComponent` -> `IRVOAvoidanceInterface` -> `INetworkPredictionInterface` -> `IObjectPoolInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CharacterOwner` | `ACharacter *` | Character movement component belongs to |
| `bApplyGravityWhileJumping` | `uint32` | Apply gravity while the character is actively jumping (e.g. holding the jump key).<br>	 	Helps remove frame-rate dependent jump height, but may alter base jump height. |
| `GravityScale` | `float` | Custom gravity scale. Gravity is multiplied by this amount for the character. |
| `MaxStepHeight` | `float` | Maximum height character can step up |
| `JumpZVelocity` | `float` | Initial velocity (instantaneous vertical acceleration) when jumping. |
| `JumpOffJumpZFactor` | `float` | Fraction of JumpZVelocity to use when automatically "jumping off" of a base actor that's not allowed to be a base for a character. (For example, if you're not allowed to stand on other players.) |
| `WalkableFloorAngle` | `float` | Max angle in degrees of a walkable surface. Any greater than this and it is too steep to be walkable. |
| `WalkableFloorZ` | `float` | Minimum Z value for floor normal. If less, not a walkable surface. Computed from WalkableFloorAngle. |
| `MovementMode` | `TEnumAsByte < enum EMovementMode >` | Actor's current movement mode (walking, falling, etc).<br>	     - walking:  Walking on a surface, under the effects of friction, and able to "step up" barriers. Vertical velocity is zero.<br>	     - falling:  Falling under the effects of gravity, after jumping or walking off the edge of a surface.<br>	     - flying:   Flying, ignoring the effects of gravity.<br>	     - swimming: Swimming through a fluid volume, under the effects of gravity and buoyancy.<br>	     - custom:   User-defined custom movement mode, including many possible sub-modes.<br>	  This is automatically replicated through the Character owner and for client-server movement functions.<br>	  @see SetMovementMode(), CustomMovementMode |
| `CustomMovementMode` | `uint8` | Current custom sub-mode if MovementMode is set to Custom.<br>	  This is automatically replicated through the Character owner and for client-server movement functions.<br>	  @see SetMovementMode() |
| `OldBaseLocation` | `FVector` | Saved location of object we are standing on, for UpdateBasedMovement() to determine if base moved in the last frame, and therefore pawn needs an update. |
| `OldBaseQuat` | `FQuat` | Saved location of object we are standing on, for UpdateBasedMovement() to determine if base moved in the last frame, and therefore pawn needs an update. |
| `OldReplaySampleLocation` | `FVector` | - |
| `OldReplaySampleTime` | `float` | - |
| `GroundFriction` | `float` | Setting that affects movement control. Higher values allow faster changes in direction.<br>	  If bUseSeparateBrakingFriction is false, also affects the ability to stop more quickly when braking (whenever Acceleration is zero), where it is multiplied by BrakingFrictionFactor.<br>	  When braking, this property allows you to control how much friction is applied when moving across the ground, applying an opposing force that scales with current velocity.<br>	  This can be used to simulate slippery surfaces such as ice or oil by changing the value (possibly based on the material pawn is standing on).<br>	  @see BrakingDecelerationWalking, BrakingFriction, bUseSeparateBrakingFriction, BrakingFrictionFactor |
| `MaxWalkSpeed` | `float` | The maximum ground speed when walking. Also determines maximum lateral speed when falling. |
| `MaxWalkSpeedCrouched` | `float` | The maximum ground speed when walking and crouched. |
| `MaxSwimSpeed` | `float` | The maximum swimming speed. |
| `MaxFlySpeed` | `float` | The maximum flying speed. |
| `MaxCustomMovementSpeed` | `float` | The maximum speed when using Custom movement mode. |
| `MaxAcceleration` | `float` | Max Acceleration (rate of change of velocity) |
| `MinAnalogWalkSpeed` | `float` | The ground speed that we should accelerate up to when walking at minimum analog stick tilt |
| `BrakingFrictionFactor` | `float` | Factor used to multiply actual value of friction used when braking.<br>	  This applies to any friction value that is currently used, which may depend on bUseSeparateBrakingFriction.<br>	  @note This is 2 by default for historical reasons, a value of 1 gives the true drag equation.<br>	  @see bUseSeparateBrakingFriction, GroundFriction, BrakingFriction |
| `BrakingFriction` | `float` | Friction (drag) coefficient applied when braking (whenever Acceleration = 0, or if character is exceeding max speed); actual value used is this multiplied by BrakingFrictionFactor.<br>	  When braking, this property allows you to control how much friction is applied when moving across the ground, applying an opposing force that scales with current velocity.<br>	  Braking is composed of friction (velocity-dependent drag) and constant deceleration.<br>	  This is the current value, used in all movement modes; if this is not desired, override it or bUseSeparateBrakingFriction when movement mode changes.<br>	  @note Only used if bUseSeparateBrakingFriction setting is true, otherwise current friction such as GroundFriction is used.<br>	  @see bUseSeparateBrakingFriction, BrakingFrictionFactor, GroundFriction, BrakingDecelerationWalking |
| `bUseSeparateBrakingFriction` | `uint32` | If true, BrakingFriction will be used to slow the character to a stop (when there is no Acceleration).<br>	  If false, braking uses the same friction passed to CalcVelocity() (ie GroundFriction when walking), multiplied by BrakingFrictionFactor.<br>	  This setting applies to all movement modes; if only desired in certain modes, consider toggling it when movement modes change.<br>	  @see BrakingFriction |
| `BrakingDecelerationWalking` | `float` | Deceleration when walking and not applying acceleration. This is a constant opposing force that directly lowers velocity by a constant value.<br>	  @see GroundFriction, MaxAcceleration |
| `BrakingDecelerationFalling` | `float` | Lateral deceleration when falling and not applying acceleration.<br>	  @see MaxAcceleration |
| `BrakingDecelerationSwimming` | `float` | Deceleration when swimming and not applying acceleration.<br>	  @see MaxAcceleration |
| `BrakingDecelerationFlying` | `float` | Deceleration when flying and not applying acceleration.<br>	  @see MaxAcceleration |
| `AirControl` | `float` | When falling, amount of lateral movement control available to the character.<br>	  0 = no control, 1 = full control at max speed of MaxWalkSpeed. |
| `AirControlBoostMultiplier` | `float` | When falling, multiplier applied to AirControl when lateral velocity is less than AirControlBoostVelocityThreshold.<br>	  Setting this to zero will disable air control boosting. Final result is clamped at 1. |
| `AirControlBoostVelocityThreshold` | `float` | When falling, if lateral velocity magnitude is less than this value, AirControl is multiplied by AirControlBoostMultiplier.<br>	  Setting this to zero will disable air control boosting. |
| `FallingLateralFriction` | `float` | Friction to apply to lateral air movement when falling.<br>	  If bUseSeparateBrakingFriction is false, also affects the ability to stop more quickly when braking (whenever Acceleration is zero).<br>	  @see BrakingFriction, bUseSeparateBrakingFriction |
| `CrouchedHalfHeight` | `float` | Collision half-height when crouching (component scale is applied separately) |
| `Buoyancy` | `float` | Water buoyancy. A ratio (1.0 = neutral buoyancy, 0.0 = no buoyancy) |
| `PerchRadiusThreshold` | `float` | Don't allow the character to perch on the edge of a surface if the contact is this close to the edge of the capsule.<br>	  Note that characters will not fall off if they are within MaxStepHeight of a walkable surface below. |
| `PerchAdditionalHeight` | `float` | When perching on a ledge, add this additional distance to MaxStepHeight when determining how high above a walkable floor we can perch.<br>	  Note that we still enforce MaxStepHeight to start the step up; this just allows the character to hang off the edge or step slightly higher off the floor.<br>	  (@see PerchRadiusThreshold) |
| `RotationRate` | `FRotator` | Change in rotation per second, used when UseControllerDesiredRotation or OrientRotationToMovement are true. Set a negative value for infinite rotation rate and instant turns. |
| `bUseControllerDesiredRotation` | `uint32` | If true, smoothly rotate the Character toward the Controller's desired rotation (typically Controller->ControlRotation), using RotationRate as the rate of rotation change. Overridden by OrientRotationToMovement.<br>	  Normally you will want to make sure that other settings are cleared, such as bUseControllerRotationYaw on the Character. |
| `bOrientRotationToMovement` | `uint32` | If true, rotate the Character toward the direction of acceleration, using RotationRate as the rate of rotation change. Overrides UseControllerDesiredRotation.<br>	  Normally you will want to make sure that other settings are cleared, such as bUseControllerRotationYaw on the Character. |
| `bSweepWhileNavWalking` | `uint32` | Whether or not the character should sweep for collision geometry while walking.<br>	  @see USceneComponent::MoveComponent. |
| `bMovementInProgress` | `uint32` | True during movement update.<br>	  Used internally so that attempts to change CharacterOwner and UpdatedComponent are deferred until after an update.<br>	  @see IsMovementInProgress() |
| `bEnableScopedMovementUpdates` | `uint32` | If true, high-level movement updates will be wrapped in a movement scope that accumulates updates and defers a bulk of the work until the end.<br>	  When enabled, touch and hit events will not be triggered until the end of multiple moves within an update, which can improve performance.<br>	 <br>	  @see FScopedMovementUpdate |
| `bForceMaxAccel` | `uint32` | Ignores size of acceleration component, and forces max acceleration to drive character at full velocity. |
| `bRunPhysicsWithNoController` | `uint32` | If true, movement will be performed even if there is no Controller for the Character owner.<br>	  Normally without a Controller, movement will be aborted and velocity and acceleration are zeroed if the character is walking.<br>	  Characters that are spawned without a Controller but with this flag enabled will initialize the movement mode to DefaultLandMovementMode or DefaultWaterMovementMode appropriately.<br>	  @see DefaultLandMovementMode, DefaultWaterMovementMode |
| `bForceNextFloorCheck` | `uint32` | Force the Character in MOVE_Walking to do a check for a valid floor even if he hasn't moved. Cleared after next floor check.<br>	  Normally if bAlwaysCheckFloor is false we try to avoid the floor check unless some conditions are met, but this can be used to force the next check to always run. |
| `bShrinkProxyCapsule` | `uint32` | If true, the capsule needs to be shrunk on this simulated proxy, to avoid replication rounding putting us in geometry.<br>	   Whenever this is set to true, this will cause the capsule to be shrunk again on the next update, and then set to false. |
| `bCanWalkOffLedges` | `uint32` | If true, Character can walk off a ledge. |
| `bCanWalkOffLedgesWhenCrouching` | `uint32` | If true, Character can walk off a ledge when crouching. |
| `bNetworkSmoothingComplete` | `uint32` | Signals that smoothed positionrotation has reached target, and no more smoothing is necessary until a future update.<br>	  This is used as an optimization to skip calls to SmoothClientPosition() when true. SmoothCorrection() sets it false when a new network update is received.<br>	  SmoothClientPosition_Interpolate() sets this to true when the interpolation reaches the target, before one last call to SmoothClientPosition_UpdateVisuals().<br>	  If this is not desired, override SmoothClientPosition() to always set this to false to avoid this feature. |
| `bNetworkSkipProxyPredictionOnNetUpdate` | `uint32` | Whether we skip prediction on frames where a proxy receives a network update. This can avoid expensive prediction on those frames,<br>	 with the side-effect of predicting with a frame of additional latency. |
| `bForceNoSimulatePrediction` | `uint32` | Whether we skip prediction on simulate movement, only interpolate from server replicated movement |
| `bDeferUpdateMoveComponent` | `uint32` | true to update CharacterOwner and UpdatedComponent after movement ends |
| `DeferredUpdatedMoveComponent` | `USceneComponent *` | What to update CharacterOwner and UpdatedComponent after movement ends |
| `MaxOutOfWaterStepHeight` | `float` | Maximum step height for getting out of water |
| `OutofWaterZ` | `float` | Z velocity applied when pawn tries to get out of water |
| `Mass` | `float` | Mass of pawn (for when momentum is imparted to it). |
| `bEnablePhysicsInteraction` | `bool` | If enabled, the player will interact with physics objects when walking into them. |
| `bTouchForceScaledToMass` | `bool` | If enabled, the TouchForceFactor is applied per kg mass of the affected object. |
| `bPushForceScaledToMass` | `bool` | If enabled, the PushForceFactor is applied per kg mass of the affected object. |
| `bPushForceUsingZOffset` | `bool` | If enabled, the PushForce location is moved using PushForcePointZOffsetFactor. Otherwise simply use the impact point. |
| `bScalePushForceToVelocity` | `bool` | If enabled, the applied push force will try to get the physics object to the same velocity than the player, not faster. This will only<br>		scale the force down, it will never apply more force than defined by PushForceFactor. |
| `StandingDownwardForceScale` | `float` | Force applied to objects we stand on (due to Mass and Gravity) is scaled by this amount. |
| `InitialPushForceFactor` | `float` | Initial impulse force to apply when the player bounces into a blocking physics object. |
| `PushForceFactor` | `float` | Force to apply when the player collides with a blocking physics object. |
| `PushForcePointZOffsetFactor` | `float` | Z-Offset for the position the force is applied to. 0.0f is the center of the physics object, 1.0f is the top and -1.0f is the bottom of the object. |
| `TouchForceFactor` | `float` | Force to apply to physics objects that are touched by the player. |
| `MinTouchForce` | `float` | Minimum Force applied to touched physics objects. If < 0.0f, there is no minimum. |
| `MaxTouchForce` | `float` | Maximum force applied to touched physics objects. If < 0.0f, there is no maximum. |
| `RepulsionForce` | `float` | Force per kg applied constantly to all overlapping components. |
| `bForceBraking_DEPRECATED` | `uint32` | - |
| `CrouchedSpeedMultiplier_DEPRECATED` | `float` | Multiplier to max ground speed to use when crouched |
| `UpperImpactNormalScale_DEPRECATED` | `float` | - |
| `Acceleration` | `FVector` | Current acceleration vector (with magnitude).<br>	  This is calculated each update based on the input vector and the constraints of MaxAcceleration and the current movement mode. |
| `LastUpdateLocation` | `FVector` | Location after last PerformMovement or SimulateMovement update. Used internally to detect changes in position from outside character movement to try to validate the current floor. |
| `LastUpdateRotation` | `FQuat` | Rotation after last PerformMovement or SimulateMovement update. |
| `LastUpdateVelocity` | `FVector` | Velocity after last PerformMovement or SimulateMovement update. Used internally to detect changes in velocity from external sources. |
| `ServerLastTransformUpdateTimeStamp` | `float` | Timestamp when location or rotation last changed during an update. Only valid on the server. |
| `PendingImpulseToApply` | `FVector` | Accumulated impulse to be added next tick. |
| `PendingForceToApply` | `FVector` | Accumulated force to be added next tick. |
| `AnalogInputModifier` | `float` | Modifier to applied to values such as acceleration and max speed due to analog input. |
| `LastStuckWarningTime` | `float` | Used for throttling "stuck in geometry" logging. |
| `LastPrintApplyImpactPhysicsForcesLog` | `float` | - |
| `MaxSimulationTimeStep` | `float` | Max time delta for each discrete simulation step.<br>	  Used primarily in the the more advanced movement modes that break up larger time steps (usually those applying gravity such as falling and walking).<br>	  Lowering this value can address issues with fast-moving objects or complex collision scenarios, at the cost of performance.<br>	 <br>	  WARNING: if (MaxSimulationTimeStep  MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.<br>	  @see MaxSimulationIterations |
| `MaxSimulationIterations` | `int32` | Max number of iterations used for each discrete simulation step.<br>	  Used primarily in the the more advanced movement modes that break up larger time steps (usually those applying gravity such as falling and walking).<br>	  Increasing this value can address issues with fast-moving objects or complex collision scenarios, at the cost of performance.<br>	 <br>	  WARNING: if (MaxSimulationTimeStep  MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.<br>	  @see MaxSimulationTimeStep |
| `MaxDepenetrationWithGeometry` | `float` | Max distance we allow simulated proxies to depenetrate when moving out of anything but Pawns.<br>	 This is generally more tolerant than with Pawns, because other geometry is either not moving, or is moving predictably with a bit of delay compared to on the server.<br>	 @see MaxDepenetrationWithGeometryAsProxy, MaxDepenetrationWithPawn, MaxDepenetrationWithPawnAsProxy |
| `MaxDepenetrationWithGeometryAsProxy` | `float` | Max distance we allow simulated proxies to depenetrate when moving out of anything but Pawns.<br>	 This is generally more tolerant than with Pawns, because other geometry is either not moving, or is moving predictably with a bit of delay compared to on the server.<br>	 @see MaxDepenetrationWithGeometry, MaxDepenetrationWithPawn, MaxDepenetrationWithPawnAsProxy |
| `MaxDepenetrationWithPawn` | `float` | Max distance we are allowed to depenetrate when moving out of other Pawns.<br>	 @see MaxDepenetrationWithGeometry, MaxDepenetrationWithGeometryAsProxy, MaxDepenetrationWithPawnAsProxy |
| `MaxDepenetrationWithPawnAsProxy` | `float` | Max distance we allow simulated proxies to depenetrate when moving out of other Pawns.<br>	  Typically we don't want a large value, because we receive a server authoritative position that we should not then ignore by pushing them out of the local player.<br>	  @see MaxDepenetrationWithGeometry, MaxDepenetrationWithGeometryAsProxy, MaxDepenetrationWithPawn |
| `NetworkSimulatedSmoothLocationTime` | `float` | How long to take to smoothly interpolate from the old pawn position on the client to the corrected one sent by the server. Not used by Linear smoothing. |
| `NetworkSimulatedSmoothRotationTime` | `float` | How long to take to smoothly interpolate from the old pawn rotation on the client to the corrected one sent by the server. Not used by Linear smoothing. |
| `ListenServerNetworkSimulatedSmoothLocationTime` | `float` | Similar setting as NetworkSimulatedSmoothLocationTime but only used on Listen servers. |
| `ListenServerNetworkSimulatedSmoothRotationTime` | `float` | Similar setting as NetworkSimulatedSmoothRotationTime but only used on Listen servers. |
| `NetProxyShrinkRadius` | `float` | Shrink simulated proxy capsule radius by this amount, to account for network rounding that may cause encroachment. Changing during gameplay is not supported.<br>	  @see AdjustProxyCapsuleSize() |
| `NetProxyShrinkHalfHeight` | `float` | Shrink simulated proxy capsule half height by this amount, to account for network rounding that may cause encroachment. Changing during gameplay is not supported.<br>	  @see AdjustProxyCapsuleSize() |
| `NetworkMaxSmoothUpdateDistance` | `float` | Maximum distance character is allowed to lag behind server location when interpolating between updates. |
| `NetworkNoSmoothUpdateDistance` | `float` | Maximum distance beyond which character is teleported to the new server location without any smoothing. |
| `bReplaySmoothUseInterp` | `bool` | - |
| `NetworkSmoothingMode` | `ENetworkSmoothingMode` | Smoothing mode for simulated proxies in network game. |
| `LedgeCheckThreshold` | `float` | Used in determining if pawn is going off ledge.  If the ledge is "shorter" than this value then the pawn will be able to walk off it. |
| `JumpOutOfWaterPitch` | `float` | When exiting water, jump if control pitch angle is this high or above. |
| `CurrentFloor` | `FFindFloorResult` | Information about the floor the Character is standing on (updated only during walking movement). |
| `DefaultLandMovementMode` | `TEnumAsByte < enum EMovementMode >` | Default movement mode when not in water. Used at player startup or when teleported.<br>	  @see DefaultWaterMovementMode<br>	  @see bRunPhysicsWithNoController |
| `DefaultWaterMovementMode` | `TEnumAsByte < enum EMovementMode >` | Default movement mode when in water. Used at player startup or when teleported.<br>	  @see DefaultLandMovementMode<br>	  @see bRunPhysicsWithNoController |
| `GroundMovementMode` | `TEnumAsByte < enum EMovementMode >` | Ground movement mode to switch to after falling and resuming ground movement.<br>	  Only allowed values are: MOVE_Walking, MOVE_NavWalking.<br>	  @see SetGroundMovementMode(), GetGroundMovementMode() |
| `bMaintainHorizontalGroundVelocity` | `uint32` | If true, walking movement always maintains horizontal velocity when moving up ramps, which causes movement up ramps to be faster parallel to the ramp surface.<br>	  If false, then walking movement maintains velocity magnitude parallel to the ramp surface. |
| `bImpartBaseVelocityX` | `uint32` | If true, impart the base actor's X velocity when falling off it (which includes jumping) |
| `bImpartBaseVelocityY` | `uint32` | If true, impart the base actor's Y velocity when falling off it (which includes jumping) |
| `bImpartBaseVelocityZ` | `uint32` | If true, impart the base actor's Z velocity when falling off it (which includes jumping) |
| `bImpartBaseAngularVelocity` | `uint32` | If true, impart the base component's tangential components of angular velocity when jumping or falling off it.<br>	  Only those components of the velocity allowed by the separate component settings (bImpartBaseVelocityX etc) will be applied.<br>	  @see bImpartBaseVelocityX, bImpartBaseVelocityY, bImpartBaseVelocityZ |
| `bJustTeleported` | `uint32` | Used by movement code to determine if a change in position is based on normal movement or a teleport. If not a teleport, velocity can be recomputed based on the change in position. |
| `bNetworkUpdateReceived` | `uint32` | True when a network replication update is received for simulated proxies. |
| `bNetworkMovementModeChanged` | `uint32` | True when the networked movement mode has been replicated. |
| `bIgnoreClientMovementErrorChecksAndCorrection` | `uint32` | True when we should ignore server location difference checks for client error on this movement component<br>	  This can be useful when character is moving at extreme speeds for a duration and you need it to look<br>	  smooth on clients. Make sure to disable when done, as this would break this character's server-client<br>	  movement correction. |
| `bNotifyApex` | `uint32` | If true, event NotifyJumpApex() to CharacterOwner's controller when at apex of jump. Is cleared when event is triggered.<br>	  By default this is off, and if you want the event to fire you typically set it to true when movement mode changes to "Falling" from another mode (see OnMovementModeChanged). |
| `bCheatFlying` | `uint32` | Instantly stop when in flying mode and no acceleration is being applied. |
| `bWantsToCrouch` | `uint32` | If true, try to crouch (or keep crouching) on next update. If false, try to stop crouching on next update. |
| `bCrouchMaintainsBaseLocation` | `uint32` | If true, crouching should keep the base of the capsule in place by lowering the center of the shrunken capsule. If false, the base of the capsule moves up and the center stays in place.<br>	  The same behavior applies when the character uncrouches: if true, the base is kept in the same location and the center moves up. If false, the capsule grows and only moves up if the base impacts something.<br>	  By default this variable is set when the movement mode changes: set to true when walking and false otherwise. Feel free to override the behavior when the movement mode changes. |
| `bIgnoreBaseRotation` | `uint32` | Whether the character ignores changes in rotation of the base it is standing on.<br>	  If true, the character maintains current world rotation.<br>	  If false, the character rotates with the moving base. |
| `bFastAttachedMove` | `uint32` | Set this to true if riding on a moving base that you know is clear from non-moving world obstructions.<br>	  Optimization to avoid sweeps during based movement, use with care. |
| `bAlwaysCheckFloor` | `uint32` | Whether we always force floor checks for stationary Characters while walking.<br>	  Normally floor checks are avoided if possible when not moving, but this can be used to force them if there are use-cases where they are being skipped erroneously<br>	  (such as objects moving up into the character from below). |
| `bUseFlatBaseForFloorChecks` | `uint32` | Performs floor checks as if the character is using a shape with a flat base.<br>	  This avoids the situation where characters slowly lower off the side of a ledge (as their capsule 'balances' on the edge). |
| `bPerformingJumpOff` | `uint32` | Used to prevent reentry of JumpOff() |
| `bWantsToLeaveNavWalking` | `uint32` | Used to safely leave NavWalking movement mode |
| `bUseRVOAvoidance` | `uint32` | If set, component will use RVO avoidance. This only runs on the server. |
| `bRequestedMoveUseAcceleration` | `uint32` | Should use acceleration for path following?<br>	  If true, acceleration is applied when path following to reach the target velocity.<br>	  If false, path following velocity is set directly, disregarding acceleration. |
| `bIsNavWalkingOnServer` | `uint32` | Set on clients when server's movement mode is NavWalking |
| `bHasRequestedVelocity` | `uint32` | Was velocity requested by path following? |
| `bRequestedMoveWithMaxSpeed` | `uint32` | Was acceleration requested to be always max speed? |
| `bWasAvoidanceUpdated` | `uint32` | Was avoidance updated in this frame? |
| `bUseRVOPostProcess` | `uint32` | if set, PostProcessAvoidanceVelocity will be called |
| `bDeferUpdateBasedMovement` | `uint32` | Flag set in pre-physics update to indicate that based movement should be updated post-physics |
| `bProjectNavMeshWalking` | `uint32` | Whether to raycast to underlying geometry to better conform navmesh-walking characters |
| `bProjectNavMeshOnBothWorldChannels` | `uint32` | Use both WorldStatic and WorldDynamic channels for NavWalking geometry conforming |
| `AvoidanceLockVelocity` | `FVector` | forced avoidance velocity, used when AvoidanceLockTimer is > 0 |
| `AvoidanceLockTimer` | `float` | remaining time of avoidance velocity lock |
| `AvoidanceConsiderationRadius` | `float` | - |
| `RequestedVelocity` | `FVector` | Velocity requested by path following.<br>	  @see RequestDirectMove() |
| `AvoidanceUID` | `int32` | No default value, for now it's assumed to be valid if GetAvoidanceManager() returns non-NULL. |
| `AvoidanceGroup` | `FNavAvoidanceMask` | Moving actor's group mask |
| `GroupsToAvoid` | `FNavAvoidanceMask` | Will avoid other agents if they are in one of specified groups |
| `GroupsToIgnore` | `FNavAvoidanceMask` | Will NOT avoid other agents if they are in one of specified groups, higher priority than GroupsToAvoid |
| `AvoidanceWeight` | `float` | De facto default value 0.5 (due to that being the default in the avoidance registration function), indicates RVO behavior. |
| `PendingLaunchVelocity` | `FVector` | Temporarily holds launch velocity when pawn is to be launched so it happens at end of movement. |
| `CachedProjectedNavMeshHitResult` | `FHitResult` | Last valid projected hit result from raycast to geometry from navmesh |
| `NavMeshProjectionInterval` | `float` | How often we should raycast to project from navmesh to underlying geometry |
| `NavMeshProjectionTimer` | `float` | - |
| `NavMeshProjectionInterpSpeed` | `float` | Speed at which to interpolate agent navmesh offset between traces. 0: Instant (no interp) > 0: Interp speed") |
| `NavMeshProjectionHeightScaleUp` | `float` | Scale of the total capsule height to use for projection from navmesh to underlying geometry in the upward direction.<br>	  In other words, start the trace at [CapsuleHeight  NavMeshProjectionHeightScaleUp] above nav mesh. |
| `NavMeshProjectionHeightScaleDown` | `float` | Scale of the total capsule height to use for projection from navmesh to underlying geometry in the downward direction.<br>	  In other words, trace down to [CapsuleHeight  NavMeshProjectionHeightScaleDown] below nav mesh. |
| `NavWalkingFloorDistTolerance` | `float` | Ignore small differences in ground height between server and client data during NavWalking mode |
| `PostPhysicsTickFunction` | `FCharacterMovementComponentPostPhysicsTickFunction` | Post-physics tick function for this character |
| `MinTimeBetweenTimeStampResets` | `float` | Minimum time between client TimeStamp resets.<br>	 So we trigger a TimeStamp reset at regular intervals to maintain a high level of accuracy. |
| `CurrentRootMotion` | `FRootMotionSourceGroup` | Root Motion Group containing active root motion sources being applied to movement |
| `RootMotionParams` | `FRootMotionMovementParams` | Animation root motion (special case for now)<br>	<br>	 Root Motion movement params. Holds result of anim montage root motion during PerformMovement(), and is overridden<br>	   during autonomous move playback to force historical root motion for MoveAutonomous() calls |
| `AnimRootMotionVelocity` | `FVector` | Velocity extracted from RootMotionParams when there is anim root motion active. Invalid to use when HasAnimRootMotion() returns false. |
| `bWasSimulatingRootMotion` | `bool` | True when SimulatedProxies are simulating RootMotion |
| `bAllowPhysicsRotationDuringAnimRootMotion` | `uint32` | - |

## Functions

### `GetToString`

```text
GetToString() -> FString
```

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `SetAvoidanceGroup`

```text
SetAvoidanceGroup(GroupFlags: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GroupFlags` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAvoidanceGroupMask`

```text
SetAvoidanceGroupMask(GroupMask: FNavAvoidanceMask &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GroupMask` | `FNavAvoidanceMask &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetGroupsToAvoid`

```text
SetGroupsToAvoid(GroupFlags: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GroupFlags` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetGroupsToAvoidMask`

```text
SetGroupsToAvoidMask(GroupMask: FNavAvoidanceMask &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GroupMask` | `FNavAvoidanceMask &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetGroupsToIgnore`

```text
SetGroupsToIgnore(GroupFlags: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GroupFlags` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetGroupsToIgnoreMask`

```text
SetGroupsToIgnoreMask(GroupMask: FNavAvoidanceMask &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GroupMask` | `FNavAvoidanceMask &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAvoidanceEnabled`

```text
SetAvoidanceEnabled(bEnable: bool) -> void
```

Change avoidance state and registers in RVO manager if needed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCharacterOwner`

```text
GetCharacterOwner() -> ACharacter *
```

Get the Character that owns UpdatedComponent.

**Returns**

| Type | Description |
|---|---|
| `ACharacter *` | - |

### `SetMovementMode`

```text
SetMovementMode(NewMovementMode: EMovementMode, NewCustomMode: uint8) -> void
```

Change movement mode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewMovementMode` | `EMovementMode` | The new movement mode |
| `NewCustomMode` | `uint8` | The new custom sub-mode, only applicable if NewMovementMode is Custom. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetGroundMovementMode`

```text
SetGroundMovementMode(NewGroundMovementMode: EMovementMode) -> void
```

Set movement mode to use when returning to walking movement (either MOVE_Walking or MOVE_NavWalking).
	  If movement mode is currently one of Walking or NavWalking, this will also change the current movement mode (via SetMovementMode())
	  if the new mode is not the current ground mode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewGroundMovementMode` | `EMovementMode` | New ground movement mode. Must be either MOVE_Walking or MOVE_NavWalking, other values are ignored. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetGroundMovementMode`

```text
GetGroundMovementMode() -> EMovementMode
```

Get current GroundMovementMode value.

**Returns**

| Type | Description |
|---|---|
| `EMovementMode` | current GroundMovementMode |

### `PackNetworkMovementMode`

```text
PackNetworkMovementMode() -> uint8
```

**Returns**

| Type | Description |
|---|---|
| `uint8` | - |

### `UnpackNetworkMovementMode`

```text
UnpackNetworkMovementMode(ReceivedMode: uint8, OutMode: TEnumAsByte < EMovementMode > &, OutCustomMode: uint8 &, OutGroundMode: TEnumAsByte < EMovementMode > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ReceivedMode` | `uint8` | - |
| `OutMode` | `TEnumAsByte < EMovementMode > &` | - |
| `OutCustomMode` | `uint8 &` | - |
| `OutGroundMode` | `TEnumAsByte < EMovementMode > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplyNetworkMovementMode`

```text
ApplyNetworkMovementMode(ReceivedMode: uint8) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ReceivedMode` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CheckBaseIsMoveable`

```text
CheckBaseIsMoveable(MovementBase: USceneComponent *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MovementBase` | `USceneComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsWalking`

```text
IsWalking() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the character is in the 'Walking' movement mode. |

### `DisableMovement`

```text
DisableMovement() -> void
```

Make movement impossible (sets movement mode to MOVE_None).

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HasValidData`

```text
HasValidData() -> bool
```

Return true if we have a valid CharacterOwner and UpdatedComponent.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetMovementBase`

```text
GetMovementBase() -> UPrimitiveComponent *
```

Return PrimitiveComponent we are based on (standing and walking on).

**Returns**

| Type | Description |
|---|---|
| `UPrimitiveComponent *` | - |

### `MaybeUpdateBasedMovement`

```text
MaybeUpdateBasedMovement(DeltaSeconds: float) -> void
```

Update or defer updating of position based on Base movement

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MaybeSaveBaseLocation`

```text
MaybeSaveBaseLocation() -> void
```

Call SaveBaseLocation() if not deferring updates (bDeferUpdateBasedMovement is false).

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetImpartedMovementBaseVelocity`

```text
GetImpartedMovementBaseVelocity() -> FVector
```

If we have a movement base, get the velocity that should be imparted by that base, usually when jumping off of it.
	  Only applies the components of the velocity enabled by bImpartBaseVelocityX, bImpartBaseVelocityY, bImpartBaseVelocityZ.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `CalcVelocity`

```text
CalcVelocity(DeltaTime: float, Friction: float, bFluid: bool, BrakingDeceleration: float) -> void
```

Updates Velocity and Acceleration based on the current state, applying the effects of friction and acceleration or deceleration. Does not apply gravity.
	  This is used internally during movement updates. Normally you don't need to call this from outside code, but you might want to use it for custom movement modes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTime` | `float` | time elapsed since last frame. |
| `Friction` | `float` | coefficient of friction when not accelerating, or in the direction opposite acceleration. |
| `bFluid` | `bool` | true if moving through a fluid, causing Friction to always be applied regardless of acceleration. |
| `BrakingDeceleration` | `float` | deceleration applied when not accelerating, or when exceeding max velocity. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMaxJumpHeight`

```text
GetMaxJumpHeight() -> float
```

Compute the max jump height based on the JumpZVelocity velocity and gravity.
	 	This does not take into account the CharacterOwner's MaxJumpHoldTime.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetMaxJumpHeightWithJumpTime`

```text
GetMaxJumpHeightWithJumpTime() -> float
```

Compute the max jump height based on the JumpZVelocity velocity and gravity.
	 	This does take into account the CharacterOwner's MaxJumpHoldTime.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetMinAnalogSpeed`

```text
GetMinAnalogSpeed() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | Maximum acceleration for the current state. |

### `K2_GetModifiedMaxAcceleration`

```text
K2_GetModifiedMaxAcceleration() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | Maximum acceleration for the current state, based on MaxAcceleration and any additional modifiers. |

### `GetMaxAcceleration`

```text
GetMaxAcceleration() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | Maximum acceleration for the current state. |

### `GetMaxBrakingDeceleration`

```text
GetMaxBrakingDeceleration() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | Maximum deceleration for the current state when braking (ie when there is no acceleration). |

### `GetCurrentAcceleration`

```text
GetCurrentAcceleration() -> FVector
```

**Returns**

| Type | Description |
|---|---|
| `FVector` | Current acceleration, computed from input vector each update. |

### `GetAnalogInputModifier`

```text
GetAnalogInputModifier() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | Modifier [0..1] based on the magnitude of the last input vector, which is used to modify the acceleration and max speed during movement. |

### `CanStepUp`

```text
CanStepUp(Hit: FHitResult &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Hit` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if we can step up on the actor in the given FHitResult. |

### `SetBase`

```text
SetBase(NewBase: UPrimitiveComponent *, BoneName: FName, bNotifyActor: bool) -> void
```

Update the base of the character, which is the PrimitiveComponent we are standing on.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewBase` | `UPrimitiveComponent *` | - |
| `BoneName` | `FName` | - |
| `bNotifyActor` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBaseFromFloor`

```text
SetBaseFromFloor(FloorResult: FFindFloorResult &) -> void
```

Update the base of the character, using the given floor result if it is walkable, or null if not. Calls SetBase().

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FloorResult` | `FFindFloorResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearAccumulatedForces`

```text
ClearAccumulatedForces() -> void
```

Clears forces accumulated through AddImpulse() and AddForce(), and also pending launch velocity.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HasAccumulatedForcesOrLaunch`

```text
HasAccumulatedForcesOrLaunch() -> bool
```

Add by zoranouyang
	 Is there AddImpulse() or AddForce() or Launch()?

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `AddImpulse`

```text
AddImpulse(Impulse: FVector, bVelocityChange: bool) -> void
```

Add impulse to character. Impulses are accumulated each tick and applied together
	  so multiple calls to this function will accumulate.
	  An impulse is an instantaneous force, usually applied once. If you want to continually apply
	  forces each frame, use AddForce().
	  Note that changing the momentum of characters like this can change the movement mode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Impulse` | `FVector` | Impulse to apply. |
| `bVelocityChange` | `bool` | Whether or not the impulse is relative to mass. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddForce`

```text
AddForce(Force: FVector) -> void
```

Add force to character. Forces are accumulated each tick and applied together
	  so multiple calls to this function will accumulate.
	  Forces are scaled depending on timestep, so they can be applied each frame. If you want an
	  instantaneous force, use AddImpulse.
	  Adding a force always takes the actor's mass into account.
	  Note that changing the momentum of characters like this can change the movement mode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Force` | `FVector` | Force to apply. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPerchRadiusThreshold`

```text
GetPerchRadiusThreshold() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | The distance from the edge of the capsule within which we don't allow the character to perch on the edge of a surface. |

### `GetValidPerchRadius`

```text
GetValidPerchRadius() -> float
```

Returns the radius within which we can stand on the edge of a surface without falling (if this is a walkable surface).
	  Simply computed as the capsule radius minus the result of GetPerchRadiusThreshold().

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `IsWalkable`

```text
IsWalkable(Hit: FHitResult &) -> bool
```

Return true if the hit result should be considered a walkable surface for the character.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Hit` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `K2_GetWalkableFloorAngle`

```text
K2_GetWalkableFloorAngle() -> float
```

Get the max angle in degrees of a walkable surface for the character.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetWalkableFloorAngle`

```text
SetWalkableFloorAngle(InWalkableFloorAngle: float) -> void
```

Set the max angle in degrees of a walkable surface for the character. Also computes WalkableFloorZ.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InWalkableFloorAngle` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_GetWalkableFloorZ`

```text
K2_GetWalkableFloorZ() -> float
```

Get the Z component of the normal of the steepest walkable surface for the character. Any lower than this and it is not walkable.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetWalkableFloorZ`

```text
SetWalkableFloorZ(InWalkableFloorZ: float) -> void
```

Set the Z component of the normal of the steepest walkable surface for the character. Also computes WalkableFloorAngle.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InWalkableFloorZ` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_FindFloor`

```text
K2_FindFloor(CapsuleLocation: FVector, FloorResult: FFindFloorResult &) -> void
```

Sweeps a vertical trace to find the floor for the capsule at the given location. Will attempt to perch if ShouldComputePerchResult() returns true for the downward sweep result.
	 No floor will be found if collision is disabled on the capsule!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CapsuleLocation` | `FVector` | Location where the capsule sweep should originate |
| `FloorResult` | `FFindFloorResult &` | Result of the floor check |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_ComputeFloorDist`

```text
K2_ComputeFloorDist(CapsuleLocation: FVector, LineDistance: float, SweepDistance: float, SweepRadius: float, FloorResult: FFindFloorResult &) -> void
```

Compute distance to the floor from bottom sphere of capsule and store the result in FloorResult.
	 This distance is the swept distance of the capsule to the first point impacted by the lower hemisphere, or distance from the bottom of the capsule in the case of a line trace.
	 This function does not care if collision is disabled on the capsule (unlike FindFloor).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CapsuleLocation` | `FVector` | Location where the capsule sweep should originate |
| `LineDistance` | `float` | If non-zero, max distance to test for a simple line check from the capsule base. Used only if the sweep test fails to find a walkable floor, and only returns a valid result if the impact normal is a walkable normal. |
| `SweepDistance` | `float` | If non-zero, max distance to use when sweeping a capsule downwards for the test. MUST be greater than or equal to the line distance. |
| `SweepRadius` | `float` | The radius to use for sweep tests. Should be <= capsule radius. |
| `FloorResult` | `FFindFloorResult &` | Result of the floor check |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CapsuleTouched`

```text
CapsuleTouched(OverlappedComp: UPrimitiveComponent *, Other: AActor *, OtherComp: UPrimitiveComponent *, OtherBodyIndex: int32, bFromSweep: bool, SweepResult: FHitResult &) -> void
```

Called when the collision capsule touches another primitive component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OverlappedComp` | `UPrimitiveComponent *` | - |
| `Other` | `AActor *` | - |
| `OtherComp` | `UPrimitiveComponent *` | - |
| `OtherBodyIndex` | `int32` | - |
| `bFromSweep` | `bool` | - |
| `SweepResult` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetPredictionData_Client`

```text
ResetPredictionData_Client() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetPredictionData_Server`

```text
ResetPredictionData_Server() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSmoothNetUpdateRotationTimeTemporaty`

```text
GetSmoothNetUpdateRotationTimeTemporaty() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetSmoothNetUpdateRotationTimeTemporaty`

```text
SetSmoothNetUpdateRotationTimeTemporaty(InSmoothNetUpdateRotationTime: float) -> void
```

Add by zoranouyang
	 临时的SmoothNetUpdateRotationTime，用于部分情况下需要一段时间内修改一下模拟端Rotation插值速度
	 主要还是以NetworkSimulatedSmoothRotationTime配置为主
	 注意：本值要记得还原到-1，表示不生效

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSmoothNetUpdateRotationTime` | `float` | 模拟端的Rotation插值时间，默认值-1表示使用NetworkSimulatedSmoothRotationTime配置的值 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerMove`

```text
ServerMove(TimeStamp: float, InAccel: FVector_NetQuantize10, ClientLoc: FVector_NetQuantize100, CompressedMoveFlags: uint8, ClientRoll: uint8, View: uint32, ClientMovementBase: UPrimitiveComponent *, ClientBaseBoneName: FName, ClientMovementMode: uint8) -> void
```

Replicated function sent by client to server - contains client movement and view info.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimeStamp` | `float` | - |
| `InAccel` | `FVector_NetQuantize10` | - |
| `ClientLoc` | `FVector_NetQuantize100` | - |
| `CompressedMoveFlags` | `uint8` | - |
| `ClientRoll` | `uint8` | - |
| `View` | `uint32` | - |
| `ClientMovementBase` | `UPrimitiveComponent *` | - |
| `ClientBaseBoneName` | `FName` | - |
| `ClientMovementMode` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerMoveDual`

```text
ServerMoveDual(TimeStamp0: float, InAccel0: FVector_NetQuantize10, PendingFlags: uint8, View0: uint32, TimeStamp: float, InAccel: FVector_NetQuantize10, ClientLoc: FVector_NetQuantize100, NewFlags: uint8, ClientRoll: uint8, View: uint32, ClientMovementBase: UPrimitiveComponent *, ClientBaseBoneName: FName, ClientMovementMode: uint8) -> void
```

Replicated function sent by client to server - contains client movement and view info for two moves.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimeStamp0` | `float` | - |
| `InAccel0` | `FVector_NetQuantize10` | - |
| `PendingFlags` | `uint8` | - |
| `View0` | `uint32` | - |
| `TimeStamp` | `float` | - |
| `InAccel` | `FVector_NetQuantize10` | - |
| `ClientLoc` | `FVector_NetQuantize100` | - |
| `NewFlags` | `uint8` | - |
| `ClientRoll` | `uint8` | - |
| `View` | `uint32` | - |
| `ClientMovementBase` | `UPrimitiveComponent *` | - |
| `ClientBaseBoneName` | `FName` | - |
| `ClientMovementMode` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerMoveDualHybridRootMotion`

```text
ServerMoveDualHybridRootMotion(TimeStamp0: float, InAccel0: FVector_NetQuantize10, PendingFlags: uint8, View0: uint32, TimeStamp: float, InAccel: FVector_NetQuantize10, ClientLoc: FVector_NetQuantize100, NewFlags: uint8, ClientRoll: uint8, View: uint32, ClientMovementBase: UPrimitiveComponent *, ClientBaseBoneName: FName, ClientMovementMode: uint8) -> void
```

Replicated function sent by client to server - contains client movement and view info for two moves. First move is non root motion, second is root motion.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimeStamp0` | `float` | - |
| `InAccel0` | `FVector_NetQuantize10` | - |
| `PendingFlags` | `uint8` | - |
| `View0` | `uint32` | - |
| `TimeStamp` | `float` | - |
| `InAccel` | `FVector_NetQuantize10` | - |
| `ClientLoc` | `FVector_NetQuantize100` | - |
| `NewFlags` | `uint8` | - |
| `ClientRoll` | `uint8` | - |
| `View` | `uint32` | - |
| `ClientMovementBase` | `UPrimitiveComponent *` | - |
| `ClientBaseBoneName` | `FName` | - |
| `ClientMovementMode` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerMoveOld`

```text
ServerMoveOld(OldTimeStamp: float, OldAccel: FVector_NetQuantize10, OldMoveFlags: uint8) -> void
```

Resending an (important) old move. Process it if not already processed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldTimeStamp` | `float` | - |
| `OldAccel` | `FVector_NetQuantize10` | - |
| `OldMoveFlags` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientAckGoodMove`

```text
ClientAckGoodMove(TimeStamp: float) -> void
```

If no client adjustment is needed after processing received ServerMove(), ack the good move so client can remove it from SavedMoves

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimeStamp` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnGoodMoveAck`

```text
OnGoodMoveAck(TimeStamp: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimeStamp` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientAdjustPosition`

```text
ClientAdjustPosition(TimeStamp: float, NewLoc: FVector, NewVel: FVector, NewBase: UPrimitiveComponent *, NewBaseBoneName: FName, bHasBase: bool, bBaseRelativePosition: bool, ServerMovementMode: uint8) -> void
```

Replicate position correction to client, associated with a timestamped servermove.  Client will replay subsequent moves after applying adjustment.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimeStamp` | `float` | - |
| `NewLoc` | `FVector` | - |
| `NewVel` | `FVector` | - |
| `NewBase` | `UPrimitiveComponent *` | - |
| `NewBaseBoneName` | `FName` | - |
| `bHasBase` | `bool` | - |
| `bBaseRelativePosition` | `bool` | - |
| `ServerMovementMode` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientVeryShortAdjustPosition`

```text
ClientVeryShortAdjustPosition(TimeStamp: float, NewLoc: FVector, NewBase: UPrimitiveComponent *, NewBaseBoneName: FName, bHasBase: bool, bBaseRelativePosition: bool, ServerMovementMode: uint8) -> void
```

Bandwidth saving version, when velocity is zeroed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimeStamp` | `float` | - |
| `NewLoc` | `FVector` | - |
| `NewBase` | `UPrimitiveComponent *` | - |
| `NewBaseBoneName` | `FName` | - |
| `bHasBase` | `bool` | - |
| `bBaseRelativePosition` | `bool` | - |
| `ServerMovementMode` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientAdjustRootMotionPosition`

```text
ClientAdjustRootMotionPosition(TimeStamp: float, ServerMontageTrackPosition: float, ServerLoc: FVector, ServerRotation: FVector_NetQuantizeNormal, ServerVelZ: float, ServerBase: UPrimitiveComponent *, ServerBoneName: FName, bHasBase: bool, bBaseRelativePosition: bool, ServerMovementMode: uint8) -> void
```

Replicate position correction to client when using root motion for movement. (animation root motion specific)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimeStamp` | `float` | - |
| `ServerMontageTrackPosition` | `float` | - |
| `ServerLoc` | `FVector` | - |
| `ServerRotation` | `FVector_NetQuantizeNormal` | - |
| `ServerVelZ` | `float` | - |
| `ServerBase` | `UPrimitiveComponent *` | - |
| `ServerBoneName` | `FName` | - |
| `bHasBase` | `bool` | - |
| `bBaseRelativePosition` | `bool` | - |
| `ServerMovementMode` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClientAdjustRootMotionSourcePosition`

```text
ClientAdjustRootMotionSourcePosition(TimeStamp: float, ServerRootMotion: FRootMotionSourceGroup, bHasAnimRootMotion: bool, ServerMontageTrackPosition: float, ServerLoc: FVector, ServerRotation: FVector_NetQuantizeNormal, ServerVelZ: float, ServerBase: UPrimitiveComponent *, ServerBoneName: FName, bHasBase: bool, bBaseRelativePosition: bool, ServerMovementMode: uint8) -> void
```

Replicate root motion source correction to client when using root motion for movement.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimeStamp` | `float` | - |
| `ServerRootMotion` | `FRootMotionSourceGroup` | - |
| `bHasAnimRootMotion` | `bool` | - |
| `ServerMontageTrackPosition` | `float` | - |
| `ServerLoc` | `FVector` | - |
| `ServerRotation` | `FVector_NetQuantizeNormal` | - |
| `ServerVelZ` | `float` | - |
| `ServerBase` | `UPrimitiveComponent *` | - |
| `ServerBoneName` | `FName` | - |
| `bHasBase` | `bool` | - |
| `bBaseRelativePosition` | `bool` | - |
| `ServerMovementMode` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCheatManager.json -->

# UCheatManager

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DebugCameraControllerRef` | `ADebugCameraController *` | Debug camera - used to have independent camera without stopping gameplay |
| `DebugCameraControllerClass` | `TSubclassOf < ADebugCameraController >` | Debug camera - used to have independent camera without stopping gameplay |

## Functions

### `FreezeFrame`

```text
FreezeFrame(Delay: float) -> void
```

Pause the game for Delay seconds.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delay` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Teleport`

```text
Teleport() -> void
```

Teleport to surface player is looking at.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ChangeSize`

```text
ChangeSize(F: float) -> void
```

Scale the player's size to be F  default size.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `F` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Fly`

```text
Fly() -> void
```

Pawn can fly.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Walk`

```text
Walk() -> void
```

Return to walking movement mode from Fly or Ghost cheat.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Ghost`

```text
Ghost() -> void
```

Pawn no longer collides with the world, and can fly

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `God`

```text
God() -> void
```

Invulnerability cheat.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Slomo`

```text
Slomo(NewTimeDilation: float) -> void
```

Modify time dilation to change apparent speed of passage of time. e.g. "Slomo 0.1" makes everything move very slowly, while "Slomo 10" makes everything move very fast.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTimeDilation` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DamageTarget`

```text
DamageTarget(DamageAmount: float) -> void
```

Damage the actor you're looking at (sourced from the player).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DamageAmount` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DestroyTarget`

```text
DestroyTarget() -> void
```

Destroy the actor you're looking at.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DestroyAll`

```text
DestroyAll(aClass: TSubclassOf < AActor >) -> void
```

Destroy all actors of class aClass

**Parameters**

| Name | Type | Description |
|---|---|---|
| `aClass` | `TSubclassOf < AActor >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DestroyAllPawnsExceptTarget`

```text
DestroyAllPawnsExceptTarget() -> void
```

Destroy all pawns except for the (pawn) target.  If no (pawn) target is found we don't destroy anything.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DestroyPawns`

```text
DestroyPawns(aClass: TSubclassOf < APawn >) -> void
```

Destroys (by calling destroy directly) all non-player pawns of class aClass in the level

**Parameters**

| Name | Type | Description |
|---|---|---|
| `aClass` | `TSubclassOf < APawn >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Summon`

```text
Summon(ClassName: FString &) -> void
```

Load Classname and spawn an actor of that class

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ClassName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlayersOnly`

```text
PlayersOnly() -> void
```

Freeze everything in the level except for players.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ViewSelf`

```text
ViewSelf() -> void
```

Make controlled pawn the viewtarget again.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ViewPlayer`

```text
ViewPlayer(S: FString &) -> void
```

View from the point of view of player with PlayerName S.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `S` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ViewActor`

```text
ViewActor(ActorName: FName) -> void
```

View from the point of view of AActor with Name ActorName.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActorName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ViewClass`

```text
ViewClass(DesiredClass: TSubclassOf < AActor >) -> void
```

View from the point of view of an AActor of class DesiredClass.  Each subsequent ViewClass cycles through the list of actors of that class.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DesiredClass` | `TSubclassOf < AActor >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StreamLevelIn`

```text
StreamLevelIn(PackageName: FName) -> void
```

Stream in the given level.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PackageName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnlyLoadLevel`

```text
OnlyLoadLevel(PackageName: FName) -> void
```

Load the given level.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PackageName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StreamLevelOut`

```text
StreamLevelOut(PackageName: FName) -> void
```

Stream out the given level.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PackageName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ToggleDebugCamera`

```text
ToggleDebugCamera() -> void
```

Toggle between debug cameraplayer camera without locking gameplay and with locking local player controller input.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ToggleAILogging`

```text
ToggleAILogging() -> void
```

toggles AI logging

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ServerToggleAILogging`

```text
ServerToggleAILogging() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DebugCapsuleSweep`

```text
DebugCapsuleSweep() -> void
```

Toggle capsule trace debugging. Will trace a capsule from current view point and show where it hits the world

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DebugCapsuleSweepSize`

```text
DebugCapsuleSweepSize(HalfHeight: float, Radius: float) -> void
```

Change Trace capsule size

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HalfHeight` | `float` | - |
| `Radius` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DebugCapsuleSweepChannel`

```text
DebugCapsuleSweepChannel(Channel: ECollisionChannel) -> void
```

Change Trace Channel

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Channel` | `ECollisionChannel` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DebugCapsuleSweepComplex`

```text
DebugCapsuleSweepComplex(bTraceComplex: bool) -> void
```

Change Trace Complex setting

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bTraceComplex` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DebugCapsuleSweepCapture`

```text
DebugCapsuleSweepCapture() -> void
```

Capture current trace and add to persistent list

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DebugCapsuleSweepPawn`

```text
DebugCapsuleSweepPawn() -> void
```

Capture current local PC's pawn's location and add to persistent list

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DebugCapsuleSweepClear`

```text
DebugCapsuleSweepClear() -> void
```

Clear persistent list for trace capture

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `TestCollisionDistance`

```text
TestCollisionDistance() -> void
```

Test all volumes in the world to the player controller's view location

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RebuildNavigation`

```text
RebuildNavigation() -> void
```

Builds the navigation mesh (or rebuilds it).

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNavDrawDistance`

```text
SetNavDrawDistance(DrawDistance: float) -> void
```

Sets navigation drawing distance. Relevant only in non-editor modes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DrawDistance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DumpOnlineSessionState`

```text
DumpOnlineSessionState() -> void
```

Dump online session information

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DumpPartyState`

```text
DumpPartyState() -> void
```

Dump known party information

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DumpChatState`

```text
DumpChatState() -> void
```

Dump known chat information

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DumpVoiceMutingState`

```text
DumpVoiceMutingState() -> void
```

Dump current state of voice chat

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BugItGo`

```text
BugItGo(X: float, Y: float, Z: float, Pitch: float, Yaw: float, Roll: float) -> void
```

This will move the player and set their rotation to the passed in values.
	  We have this version of the BugIt family as it is easier to type in just raw numbers in the console.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `X` | `float` | - |
| `Y` | `float` | - |
| `Z` | `float` | - |
| `Pitch` | `float` | - |
| `Yaw` | `float` | - |
| `Roll` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BugIt`

```text
BugIt(ScreenShotDescription: FString &) -> void
```

This function is used to print out the BugIt location.  It prints out copy and paste versions for both IMing someone to type in
	 and also a gameinfo ?options version so that you can append it to your launching url and be taken to the correct place.
	 Additionally, it will take a screen shot so reporting bugs is a one command action!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ScreenShotDescription` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BugItStringCreator`

```text
BugItStringCreator(ViewLocation: FVector, ViewRotation: FRotator, GoString: FString &, LocString: FString &) -> void
```

This will create a BugItGo string for us.  Nice for calling form c++ where you just want the string and no Screenshots

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ViewLocation` | `FVector` | - |
| `ViewRotation` | `FRotator` | - |
| `GoString` | `FString &` | - |
| `LocString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FlushLog`

```text
FlushLog() -> void
```

This will force a flush of the output log to file

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `LogLoc`

```text
LogLoc() -> void
```

Logs the current location in bugit format without taking screenshot and further routing.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWorldOrigin`

```text
SetWorldOrigin() -> void
```

Translate world origin to this player position

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMouseSensitivityToDefault`

```text
SetMouseSensitivityToDefault() -> void
```

Exec function to return the mouse sensitivity to its default value

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InvertMouse`

```text
InvertMouse() -> void
```

Backwards compatibility exec function for people used to it instead of using InvertAxisKey

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CheatScript`

```text
CheatScript(ScriptName: FString) -> void
```

Executes commands listed in CheatScript.ScriptName ini section of DefaultGame.ini

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ScriptName` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveInitCheatManager`

```text
ReceiveInitCheatManager() -> void
```

BP implementable event for when CheatManager is created to allow any needed initialization.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveEndPlay`

```text
ReceiveEndPlay() -> void
```

This is the End Play event for the CheatManager

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableDebugCamera`

```text
EnableDebugCamera() -> void
```

Switch controller to debug camera without locking gameplay and with locking local player controller input

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableDebugCamera`

```text
DisableDebugCamera() -> void
```

Switch controller from debug camera back to normal controller

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCheckBox.json -->

# UCheckBox

The checkbox widget allows you to display a toggled state of 'unchecked', 'checked' and 
  'indeterminable.  You can use the checkbox for a classic checkbox, or as a toggle button,
  or as radio buttons.
  
   Single Child
   Toggle

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CheckedState` | `ECheckBoxState` | Whether the check box is currently in a checked state |
| `CheckedStateDelegate` | `FGetCheckBoxState` | A bindable delegate for the IsChecked. |
| `WidgetStyle` | `FCheckBoxStyle` | The checkbox bar style |
| `Style_DEPRECATED` | `USlateWidgetStyleAsset *` | Style of the check box |
| `UncheckedImage_DEPRECATED` | `USlateBrushAsset *` | Image to use when the checkbox is unchecked |
| `UncheckedHoveredImage_DEPRECATED` | `USlateBrushAsset *` | Image to use when the checkbox is unchecked and hovered |
| `UncheckedPressedImage_DEPRECATED` | `USlateBrushAsset *` | Image to use when the checkbox is unchecked and pressed |
| `CheckedImage_DEPRECATED` | `USlateBrushAsset *` | Image to use when the checkbox is checked |
| `CheckedHoveredImage_DEPRECATED` | `USlateBrushAsset *` | Image to use when the checkbox is checked and hovered |
| `CheckedPressedImage_DEPRECATED` | `USlateBrushAsset *` | Image to use when the checkbox is checked and pressed |
| `UndeterminedImage_DEPRECATED` | `USlateBrushAsset *` | Image to use when the checkbox is in an ambiguous state and hovered |
| `UndeterminedHoveredImage_DEPRECATED` | `USlateBrushAsset *` | Image to use when the checkbox is checked and hovered |
| `UndeterminedPressedImage_DEPRECATED` | `USlateBrushAsset *` | Image to use when the checkbox is in an ambiguous state and pressed |
| `HorizontalAlignment` | `TEnumAsByte < EHorizontalAlignment >` | How the content of the toggle button should align within the given space |
| `Padding_DEPRECATED` | `FMargin` | Spacing between the check box image and its content |
| `BorderBackgroundColor_DEPRECATED` | `FSlateColor` | The color of the background border |
| `IsFocusable` | `bool` | Sometimes a button should only be mouse-clickable and never keyboard focusable. |
| `ClickMethod` | `TEnumAsByte < EButtonClickMethod :: Type >` | The type of mouse action required by the user to trigger the buttons 'Click' |
| `TouchMethod` | `TEnumAsByte < EButtonTouchMethod :: Type >` | The type of touch action required by the user to trigger the buttons 'Click' |

## Functions

### `IsPressed`

```text
IsPressed() -> bool
```

Returns true if this button is currently pressed

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsChecked`

```text
IsChecked() -> bool
```

Returns true if the checkbox is currently checked

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetCheckedState`

```text
GetCheckedState() -> ECheckBoxState
```

**Returns**

| Type | Description |
|---|---|
| `ECheckBoxState` | the full current checked state. |

### `SetIsChecked`

```text
SetIsChecked(InIsChecked: bool) -> void
```

Sets the checked state.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIsChecked` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCheckedState`

```text
SetCheckedState(InCheckedState: ECheckBoxState) -> void
```

Sets the checked state.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCheckedState` | `ECheckBoxState` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetClickMethod`

```text
SetClickMethod(InClickMethod: EButtonClickMethod :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InClickMethod` | `EButtonClickMethod :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTouchMethod`

```text
SetTouchMethod(InTouchMethod: EButtonTouchMethod :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTouchMethod` | `EButtonTouchMethod :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnCheckStateChanged`

```text
OnCheckStateChanged(bIsChecked: bool) -> void
```

Called when the checked state has changed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsChecked` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCheckBoxStyleAsset.json -->

# UCheckBoxStyleAsset

An asset describing a CheckBox's appearance.
  Just a wrapper for the struct with real data in it.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CheckBoxStyle` | `FCheckBoxStyle` | The actual data describing the Check Box's appearance. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCheckBoxWidgetStyle.json -->

# UCheckBoxWidgetStyle

## Inheritance

`USlateWidgetStyleContainerBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CheckBoxStyle` | `FCheckBoxStyle` | The actual data describing the button's appearance. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCheckedStateBinding.json -->

# UCheckedStateBinding

## Inheritance

`UPropertyBinding`

## Functions

### `GetValue`

```text
GetValue() -> ECheckBoxState
```

**Returns**

| Type | Description |
|---|---|
| `ECheckBoxState` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UChildActorComponent.json -->

# UChildActorComponent

A component that spawns an Actor when registered, and destroys it when unregistered.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ChildActorClass` | `TSubclassOf < AActor >` | The class of Actor to spawn |
| `ChildActor` | `AActor *` | The actor that we spawned and own |
| `bAllowTemplateModification` | `bool` | - |
| `ChildActorTemplate` | `AActor *` | Property to point to the template child actor for details panel purposes |
| `IsDestoryChildActor` | `bool` | - |
| `bKeepChildActorComponet` | `bool` | - |
| `bEnableReplication` | `bool` | - |
| `bDumpChildActorLocation` | `bool` | - |
| `bRedirectComps` | `uint8` | - |
| `bPCOnlyComps` | `uint8` | - |

## Functions

### `SetChildActorClass`

```text
SetChildActorClass(InClass: TSubclassOf < AActor >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InClass` | `TSubclassOf < AActor >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_ChildActor`

```text
OnRep_ChildActor() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CreateChildActor`

```text
CreateChildActor() -> void
```

Create the child actor

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DestroyChildActor`

```text
DestroyChildActor(bNeedInstanceData: bool) -> void
```

Kill any currently present child actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNeedInstanceData` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnChildActorRep`

```text
OnChildActorRep() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UChildConnection.json -->

# UChildConnection

Represents a secondary split screen connection that reroutes calls to the parent connection.

## Inheritance

`UNetConnection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Parent` | `UNetConnection *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UChunkLabel.json -->

# UChunkLabel

## Inheritance

`UPrimaryDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Rules` | `FPrimaryAssetRules` | Management rules for this specific asset, if set it will override the type rules |
| `LogicChunkName` | `FString` | True to Label everything in this directory and sub directories |
| `FinalChunkName` | `FString` | - |
| `ChunkOutputPath` | `FString` | - |
| `bIsRuntimeLabel` | `uint32` | Set to true if the label asset itself should be cooked and available at runtime. This does not affect the assets that are labeled, they are set with cook rule |
| `Key` | `FString` | - |
| `IV` | `FString` | - |
| `ManagerRuleNames` | `TArray < FString >` | - |
| `bUpdateManagerRulesWhenSaved` | `bool` | - |
| `bForceReloadManagerRule` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCineCameraComponent.json -->

# UCineCameraComponent

A specialized version of a camera component, geared toward cinematic usage.

## Inheritance

`UCameraComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FilmbackSettings` | `FCameraFilmbackSettings` | Controls the filmback of the camera. |
| `LensSettings` | `FCameraLensSettings` | Controls the camera's lens. |
| `FocusSettings` | `FCameraFocusSettings` | Controls the camera's focus. |
| `CurrentFocalLength` | `float` | Current focal length of the camera (i.e. controls FoV, zoom) |
| `CurrentAperture` | `float` | Current aperture, in terms of f-stop (e.g. 2.8 for f2.8) |
| `CurrentFocusDistance` | `float` | Read-only. Control this value via FocusSettings. |
| `FilmbackPresets` | `TArray < FNamedFilmbackPreset >` | List of available filmback presets |
| `LensPresets` | `TArray < FNamedLensPreset >` | List of available lens presets |
| `DefaultFilmbackPresetName` | `FString` | Name of the default filmback preset |
| `DefaultLensPresetName` | `FString` | Name of the default lens preset |
| `DefaultLensFocalLength` | `float` | Default focal length (will be constrained by default lens) |
| `DefaultLensFStop` | `float` | Default aperture (will be constrained by default lens) |

## Functions

### `GetHorizontalFieldOfView`

```text
GetHorizontalFieldOfView() -> float
```

Returns the horizonal FOV of the camera with current settings.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetVerticalFieldOfView`

```text
GetVerticalFieldOfView() -> float
```

Returns the vertical FOV of the camera with current settings.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetFilmbackPresetName`

```text
GetFilmbackPresetName() -> FString
```

Returns the filmback name of the camera with the current settings.

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `SetFilmbackPresetByName`

```text
SetFilmbackPresetByName(InPresetName: FString &) -> void
```

Set the current preset settings by preset name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPresetName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLensPresetName`

```text
GetLensPresetName() -> FString
```

Returns the lens name of the camera with the current settings.

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `SetLensPresetByName`

```text
SetLensPresetByName(InPresetName: FString &) -> void
```

Set the current lens settings by preset name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPresetName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCircularThrobber.json -->

# UCircularThrobber

A throbber widget that orients images in a spinning circle.
  
   No Children
   Spinner Progress

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NumberOfPieces` | `int32` | How many pieces there are |
| `Period` | `float` | The amount of time for a full circle (in seconds) |
| `Radius` | `float` | The radius of the circle. If the throbber is a child of Canvas Panel, the 'Size to Content' option must be enabled in order to set Radius. |
| `PieceImage_DEPRECATED` | `USlateBrushAsset *` | Image to use for each segment of the throbber |
| `Image` | `FSlateBrush` | - |
| `bEnableRadius` | `bool` | - |

## Functions

### `SetNumberOfPieces`

```text
SetNumberOfPieces(InNumberOfPieces: int32) -> void
```

Sets how many pieces there are.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNumberOfPieces` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPeriod`

```text
SetPeriod(InPeriod: float) -> void
```

Sets the amount of time for a full circle (in seconds).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPeriod` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRadius`

```text
SetRadius(InRadius: float) -> void
```

Sets the radius of the circle.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRadius` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UClickActorComponentBase.json -->

# UClickActorComponentBase

一个提供给按钮使用的组件，用于实现靠近显示按钮的逻辑

## Inheritance

`UActorComponent` -> `IRegionObjectInterface` -> `IObjectPoolInterface` -> `IInteractorInterface`

## Functions

### `HandleEnable`

```text
HandleEnable() -> void
```

生效范围：S
	  激活组件功能

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HandleDisable`

```text
HandleDisable() -> void
```

生效范围：S
	  停止组件功能

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UClipmapGenerateConfig.json -->

# UClipmapGenerateConfig

## Inheritance

`UDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetTexture` | `UTexture2D *` | - |
| `TargetClipmapTexture` | `UClipmapTexture *` | - |
| `ClipmapWetnessConfig` | `FClipmapWetness` | - |
| `FoliageHealthAndAbsorptionConfig` | `FClipmapFoliageHealthAndAbsorption` | - |
| `LandscapeTintConfig` | `FClipmapLandscapeTint` | - |
| `BurshTintNum` | `int32` | - |
| `WeightBitsNum` | `int32` | - |
| `WeightMax` | `int32` | - |

## Functions

### `GenerateGChannel`

```text
GenerateGChannel() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GenerateBAChannel`

```text
GenerateBAChannel() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GenerateCustomMips`

```text
GenerateCustomMips() -> void
```

统一的Mip后处理入口：先让引擎生成标准Mip，再后处理R通道(Max降采样)，可选BA通道(众数)

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UClipmapTexture.json -->

# UClipmapTexture

Runtime virtual texture UObject

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bSkipOneMip` | `bool` | - |
| `DisFirstMip` | `float` | - |
| `bUsePointSample` | `bool` | - |
| `bUseBorder` | `bool` | - |
| `TileSize` | `int32` | - |
| `FirstMipImageSize` | `int32` | - |
| `NumTile` | `int32` | - |
| `bUseCompressType` | `bool` | - |
| `NormalSetting` | `FClipmapSetting` | - |
| `CompressSetting` | `TMap < FString , FClipmapSetting >` | - |
| `bsRGB` | `bool` | - |
| `FileDDCPath` | `FString` | - |
| `ClipmapInfos` | `FClipmapInfos` | - |
| `CompressInfos` | `TMap < FString , FClipmapInfos >` | - |
| `DebugName` | `FString` | - |
| `HashNum` | `uint32` | - |
| `Owner` | `UClipmapTextureComponent *` | - |
| `OriginTexture` | `UTexture2D *` | - |
| `TargetTexture` | `TSoftObjectPtr < UTexture2D >` | - |

## Functions

### `CreateClipmapTargetTexture`

```text
CreateClipmapTargetTexture() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UClipmapTextureComponent.json -->

# UClipmapTextureComponent

Component used to place a URuntimeVirtualTexture in the world.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ClipmapTexture` | `UClipmapTexture *` | - |
| `bUseForCDLODMatID` | `bool` | - |
| `BoundsSourceActor` | `AActor *` | Actor to copy the bounds from to set up the transform. |
| `MipToDis` | `TMap < int32 , float >` | - |
| `ClipmapInfo` | `FVector4` | - |

## Functions

### `SetTransformToBounds`

```text
SetTransformToBounds() -> void
```

Set this component transform to include the BoundsSourceActor bounds. Called by our UI details customization.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RefreshClipmapInfo`

```text
RefreshClipmapInfo() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UClothingAsset.json -->

# UClothingAsset

## Inheritance

`UClothingAssetBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PhysicsAsset` | `UPhysicsAsset *` | - |
| `ClothConfig` | `FClothConfig` | - |
| `LodData` | `TArray < FClothLODData >` | - |
| `LodMap` | `TArray < int32 >` | - |
| `UsedBoneNames` | `TArray < FName >` | - |
| `UsedBoneIndices` | `TArray < int32 >` | - |
| `ReferenceBoneIndex` | `int32` | - |
| `CustomData` | `UClothingAssetCustomData *` | Custom data applied by the importer depending on where the asset was imported from |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UClothingAssetBase.json -->

# UClothingAssetBase

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ImportedFilePath` | `FString` | - |
| `AssetGuid` | `FGuid` | Guid to identify this asset. Will be embedded into chunks that are created using this asset |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCloudStorageBase.json -->

# UCloudStorageBase

Base class for the various platform interface classes.

## Inheritance

`UPlatformInterfaceBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LocalCloudFiles` | `TArray < FString >` | When using local storage (aka "cloud emulation"), this maintains a list of the file paths. |
| `bSuppressDelegateCalls` | `uint32` | If true, delegate callbacks should be skipped. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCollisionProfile.json -->

# UCollisionProfile

Set up and modify collision settings.

## Inheritance

`UDeveloperSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Profiles` | `TArray < FCollisionResponseTemplate >` | - |
| `DefaultChannelResponses` | `TArray < FCustomChannelSetup >` | - |
| `EditProfiles` | `TArray < FCustomProfile >` | - |
| `ProfileRedirects` | `TArray < FRedirector >` | - |
| `CollisionChannelRedirects` | `TArray < FRedirector >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UColorBinding.json -->

# UColorBinding

## Inheritance

`UPropertyBinding`

## Functions

### `GetSlateValue`

```text
GetSlateValue() -> FSlateColor
```

**Returns**

| Type | Description |
|---|---|
| `FSlateColor` | - |

### `GetLinearValue`

```text
GetLinearValue() -> FLinearColor
```

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UColorGradient.json -->

# UColorGradient

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ColorRGBs` | `TArray < FColorGradientCellInfo >` | - |

## Functions

### `GetNum`

```text
GetNum() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetCellByIndex`

```text
GetCellByIndex(Idx: int, OutPercent: float &, OutColorRGB: FLinearColor &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Idx` | `int` | - |
| `OutPercent` | `float &` | - |
| `OutColorRGB` | `FLinearColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `FindIndexByPercent`

```text
FindIndexByPercent(InPercent: float) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPercent` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetDatas`

```text
SetDatas(datas: TArray < FColorGradientCellInfo > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `datas` | `TArray < FColorGradientCellInfo > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `ColorRGBsDelegate`

```text
ColorRGBsDelegate() -> TArray<FColorGradientCellInfo>
```

**Returns**

| Type | Description |
|---|---|
| `TArray` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UColorGradientSlider.json -->

# UColorGradientSlider

## Inheritance

`UColorGradient`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SliderStyle` | `FSliderStyle` | - |
| `BarFrameNormal` | `FSlateBrush` | - |
| `BarFrameSelect` | `FSlateBrush` | - |
| `DefaultSelectIndex` | `int32` | - |
| `CurSelectIndex` | `int32` | - |

## Functions

### `GetCurSelectIndex`

```text
GetCurSelectIndex() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetCurSelectIndex`

```text
SetCurSelectIndex(Idx: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Idx` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDatas`

```text
SetDatas(datas: TArray < FColorGradientCellInfo > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `datas` | `TArray < FColorGradientCellInfo > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnPercentChanged`

```text
OnPercentChanged(Idx: int32, InPercent: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Idx` | `int32` | - |
| `InPercent` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnChildSelected`

```text
OnChildSelected(Idx: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Idx` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`

