---
id: "api:class:UActorComponent"
title: "UActorComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UActorComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
