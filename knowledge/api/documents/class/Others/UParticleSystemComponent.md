---
id: "api:class:UParticleSystemComponent"
title: "UParticleSystemComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UParticleSystemComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UParticleSystemComponent

A particle emitter.

## Inheritance

`UPrimitiveComponent` -> `IWTACAggregateInterface` -> `IObjectPoolInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TemplateBindingType` | `EParticleTemplateBindingType` | - |
| `Template` | `UParticleSystem *` | - |
| `SoftTemplate` | `TSoftObjectPtr < UParticleSystem >` | - |
| `EmitterMaterials` | `TArray < UMaterialInterface * >` | - |
| `SkelMeshComponents` | `TArray < USkeletalMeshComponent * >` | The skeletal mesh components used with the socket location module.<br>	 	This is to prevent them from being garbage collected. |
| `bResetOnDetach` | `uint8` | - |
| `bUpdateOnDedicatedServer` | `uint8` | whether to update the particle system on dedicated servers |
| `bAllowRecycling` | `uint8` | If true, this Particle System will be available for recycling after it has completed. Auto-destroyed systems cannot be recycled.<br>	  Some systems (currently particle trail effects) can recycle components to avoid respawning them to play new effects.<br>	  This is only an optimization and does not change particle system behavior, aside from not triggering normal component initialization events more than once. |
| `bAutoManageAttachment` | `uint8` | True if we should automatically attach to AutoAttachParent when activated, and detach from our parent when completed.<br>	  This overrides any current attachment that may be present at the time of activation (deferring initial attachment until activation, if AutoAttachParent is null).<br>	  When enabled, detachment occurs regardless of whether AutoAttachParent is assigned, and the relative transform from the time of activation is restored.<br>	  This also disables attachment on dedicated servers, where we don't actually activate even if bAutoActivate is true.<br>	  @see AutoAttachParent, AutoAttachSocketName, AutoAttachLocationType |
| `bWarmingUp` | `uint8` | - |
| `bOverrideLODMethod` | `uint8` | indicates that the component's LODMethod overrides the Template's |
| `bSkipUpdateDynamicDataDuringTick` | `uint8` | Flag indicating that dynamic updating of render data should NOT occur during Tick.<br>	 	This is used primarily to allow for warming up and simulated effects to a certain state. |
| `LODMethod` | `TEnumAsByte < enum ParticleSystemLODMethod >` | The method of LOD level determination to utilize for this particle system |
| `RequiredSignificance` | `EParticleSignificanceLevel` | The significance this component requires of it's emitters for them to be enabled. |
| `bShouldUseTagGetSkeletalMesh` | `bool` | Array holding name instance parameters for this ParticleSystemComponent.<br>	 	Parameters can be used in Cascade using DistributionFloatVectorParticleParameters. |
| `SkeletalMeshTagName` | `FName` | - |
| `InstanceParameters` | `TArray < FParticleSysParam >` | - |
| `OnParticleSpawn` | `FParticleSpawnSignature` | - |
| `OnParticleBurst` | `FParticleBurstSignature` | - |
| `OnParticleDeath` | `FParticleDeathSignature` | - |
| `OnParticleCollide` | `FParticleCollisionSignature` | - |
| `OldPosition` | `FVector` | - |
| `PartSysVelocity` | `FVector` | - |
| `WarmupTime` | `float` | - |
| `WarmupTickRate` | `float` | - |
| `OverrideEmitterMeshDataMap` | `TMap < FName , UStaticMesh * >` | - |
| `SecondsBeforeInactive` | `float` | Number of seconds of emitter not being rendered that need to pass before it<br>	  no longer gets ticked becomes inactive. |
| `MaxTimeBeforeForceUpdateTransform` | `float` | Time between forced UpdateTransforms for systems that use dynamically calculated bounds,<br>	  Which is effectively how often the bounds are shrunk. |
| `ReplayClips` | `TArray < UParticleSystemReplay * >` | Array of replay clips for this particle system component.  These are serialized to disk.  You really should never add anything to this in the editor.  It's exposed so that you can delete clips if you need to, but be careful when doing so! |
| `CustomTimeDilation` | `float` | Scales DeltaTime in UParticleSystemComponent::Tick(...) |
| `bIsPCPlatformResource` | `bool` | Is PC Redirect Particle Resource |
| `AutoAttachParent` | `TWeakObjectPtr < USceneComponent >` | Component we automatically attach to when activated, if bAutoManageAttachment is true.<br>	  If null during registration, we assign the existing AttachParent and defer attachment until we activate.<br>	  @see bAutoManageAttachment |
| `AutoAttachSocketName` | `FName` | Socket we automatically attach to on the AutoAttachParent, if bAutoManageAttachment is true.<br>	  @see bAutoManageAttachment |
| `AutoAttachLocationRule` | `EAttachmentRule` | Options for how we handle our location when we attach to the AutoAttachParent, if bAutoManageAttachment is true.<br>	  @see bAutoManageAttachment, EAttachmentRule |
| `AutoAttachRotationRule` | `EAttachmentRule` | Options for how we handle our rotation when we attach to the AutoAttachParent, if bAutoManageAttachment is true.<br>	  @see bAutoManageAttachment, EAttachmentRule |
| `AutoAttachScaleRule` | `EAttachmentRule` | Options for how we handle our scale when we attach to the AutoAttachParent, if bAutoManageAttachment is true.<br>	  @see bAutoManageAttachment, EAttachmentRule |
| `bForceNoAsync` | `bool` | - |
| `SystemFixedWorldBounds` | `FBox` | - |
| `SystemFixedLocalBounds` | `FBox` | - |
| `CollisionIgnoreActorList` | `TArray < AActor * >` | - |
| `CollisionIgnoreComponentList` | `TArray < UPrimitiveComponent * >` | - |
| `CollisionIgnoreInfoLastClearTime` | `float` | - |
| `EditorLODLevel` | `int32` | INTERNAL. Used by the editor to set the LODLevel |
| `EditorDetailMode` | `int32` | Used for applying Cascade's detail mode setting to in-level particle systems |
| `AutoAttachLocationType_DEPRECATED` | `TEnumAsByte < EAttachLocation :: Type >` | DEPRECATED: Options for how we handle our location when we attach to the AutoAttachParent, if bAutoManageAttachment is true.<br>	  @see bAutoManageAttachment, EAttachLocation::Type |

## Functions

### `GetDuration`

```text
GetDuration() -> float
```

Returns duration

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetSystemFixedWorldBounds`

```text
SetSystemFixedWorldBounds(WorldBounds: FBox) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldBounds` | `FBox` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSystemFixedLocalBounds`

```text
SetSystemFixedLocalBounds(LocalBounds: FBox) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LocalBounds` | `FBox` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearSystemFixedBounds`

```text
ClearSystemFixedBounds() -> void
```

Clear any previously set fixed bounds for the system instance.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWarmUp`

```text
SetWarmUp(WarmUpTime: float, WarmUpRate: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WarmUpTime` | `float` | - |
| `WarmUpRate` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAutoAttachParams`

```text
SetAutoAttachParams(Parent: USceneComponent *, SocketName: FName, LocationType: EAttachLocation :: Type) -> void
```

DEPRECATED: Set AutoAttachParent, AutoAttachSocketName, AutoAttachLocationType to the specified parameters. Does not change bAutoManageAttachment; that must be set separately.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Parent` | `USceneComponent *` | Component to attach to. |
| `SocketName` | `FName` | Socket on Parent to attach to. |
| `LocationType` | `EAttachLocation :: Type` | Option for how we handle our location when we attach to Parent. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAutoAttachmentParameters`

```text
SetAutoAttachmentParameters(Parent: USceneComponent *, SocketName: FName, LocationRule: EAttachmentRule, RotationRule: EAttachmentRule, ScaleRule: EAttachmentRule) -> void
```

Set AutoAttachParent, AutoAttachSocketName, AutoAttachLocationRule, AutoAttachRotationRule, AutoAttachScaleRule to the specified parameters. Does not change bAutoManageAttachment; that must be set separately.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Parent` | `USceneComponent *` | Component to attach to. |
| `SocketName` | `FName` | Socket on Parent to attach to. |
| `LocationRule` | `EAttachmentRule` | Option for how we handle our location when we attach to Parent. |
| `RotationRule` | `EAttachmentRule` | Option for how we handle our rotation when we attach to Parent. |
| `ScaleRule` | `EAttachmentRule` | Option for how we handle our scale when we attach to Parent. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBeamEndPoint`

```text
SetBeamEndPoint(EmitterIndex: int32, NewEndPoint: FVector) -> void
```

Set the beam end point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to set it on |
| `NewEndPoint` | `FVector` | The value to set it to |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBeamSourcePoint`

```text
SetBeamSourcePoint(EmitterIndex: int32, NewSourcePoint: FVector, SourceIndex: int32) -> void
```

Set the beam source point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to set it on |
| `NewSourcePoint` | `FVector` | The value to set it to |
| `SourceIndex` | `int32` | Which beam within the emitter to set it on |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBeamSourceTangent`

```text
SetBeamSourceTangent(EmitterIndex: int32, NewTangentPoint: FVector, SourceIndex: int32) -> void
```

Set the beam source tangent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to set it on |
| `NewTangentPoint` | `FVector` | The value to set it to |
| `SourceIndex` | `int32` | Which beam within the emitter to set it on |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBeamSourceStrength`

```text
SetBeamSourceStrength(EmitterIndex: int32, NewSourceStrength: float, SourceIndex: int32) -> void
```

Set the beam source strength

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to set it on |
| `NewSourceStrength` | `float` | The value to set it to |
| `SourceIndex` | `int32` | Which beam within the emitter to set it on |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBeamTargetPoint`

```text
SetBeamTargetPoint(EmitterIndex: int32, NewTargetPoint: FVector, TargetIndex: int32) -> void
```

Set the beam target point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to set it on |
| `NewTargetPoint` | `FVector` | The value to set it to |
| `TargetIndex` | `int32` | Which beam within the emitter to set it on |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBeamTargetTangent`

```text
SetBeamTargetTangent(EmitterIndex: int32, NewTangentPoint: FVector, TargetIndex: int32) -> void
```

Set the beam target tangent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to set it on |
| `NewTangentPoint` | `FVector` | The value to set it to |
| `TargetIndex` | `int32` | Which beam within the emitter to set it on |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBeamTargetStrength`

```text
SetBeamTargetStrength(EmitterIndex: int32, NewTargetStrength: float, TargetIndex: int32) -> void
```

Set the beam target strength

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to set it on |
| `NewTargetStrength` | `float` | The value to set it to |
| `TargetIndex` | `int32` | Which beam within the emitter to set it on |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBeamEndPoint`

```text
GetBeamEndPoint(EmitterIndex: int32, OutEndPoint: FVector &) -> bool
```

Get the beam end point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to get the value of |
| `OutEndPoint` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true		EmitterIndex is valid and End point is set - OutEndPoint is valid |

### `GetBeamSourcePoint`

```text
GetBeamSourcePoint(EmitterIndex: int32, SourceIndex: int32, OutSourcePoint: FVector &) -> bool
```

Get the beam source point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to get |
| `SourceIndex` | `int32` | Which beam within the emitter to get |
| `OutSourcePoint` | `FVector &` | Value of source point |

**Returns**

| Type | Description |
|---|---|
| `bool` | true		EmitterIndex and SourceIndex are valid - OutSourcePoint is valid |

### `GetBeamSourceTangent`

```text
GetBeamSourceTangent(EmitterIndex: int32, SourceIndex: int32, OutTangentPoint: FVector &) -> bool
```

Get the beam source tangent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to get |
| `SourceIndex` | `int32` | Which beam within the emitter to get |
| `OutTangentPoint` | `FVector &` | Value of source tangent |

**Returns**

| Type | Description |
|---|---|
| `bool` | true		EmitterIndex and SourceIndex are valid - OutTangentPoint is valid |

### `GetBeamSourceStrength`

```text
GetBeamSourceStrength(EmitterIndex: int32, SourceIndex: int32, OutSourceStrength: float &) -> bool
```

Get the beam source strength

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to get |
| `SourceIndex` | `int32` | Which beam within the emitter to get |
| `OutSourceStrength` | `float &` | Value of source tangent |

**Returns**

| Type | Description |
|---|---|
| `bool` | true		EmitterIndex and SourceIndex are valid - OutSourceStrength is valid |

### `GetBeamTargetPoint`

```text
GetBeamTargetPoint(EmitterIndex: int32, TargetIndex: int32, OutTargetPoint: FVector &) -> bool
```

Get the beam target point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to get |
| `TargetIndex` | `int32` | Which beam within the emitter to get |
| `OutTargetPoint` | `FVector &` | Value of target point |

**Returns**

| Type | Description |
|---|---|
| `bool` | true		EmitterIndex and TargetIndex are valid - OutTargetPoint is valid |

### `GetBeamTargetTangent`

```text
GetBeamTargetTangent(EmitterIndex: int32, TargetIndex: int32, OutTangentPoint: FVector &) -> bool
```

Get the beam target tangent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to get |
| `TargetIndex` | `int32` | Which beam within the emitter to get |
| `OutTangentPoint` | `FVector &` | Value of target tangent |

**Returns**

| Type | Description |
|---|---|
| `bool` | true		EmitterIndex and TargetIndex are valid - OutTangentPoint is valid |

### `GetBeamTargetStrength`

```text
GetBeamTargetStrength(EmitterIndex: int32, TargetIndex: int32, OutTargetStrength: float &) -> bool
```

Get the beam target strength

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterIndex` | `int32` | The index of the emitter to get |
| `TargetIndex` | `int32` | Which beam within the emitter to get |
| `OutTargetStrength` | `float &` | Value of target tangent |

**Returns**

| Type | Description |
|---|---|
| `bool` | true		EmitterIndex and TargetIndex are valid - OutTargetStrength is valid |

### `SetEmitterEnable`

```text
SetEmitterEnable(EmitterName: FName, bNewEnableState: bool) -> void
```

EnablesDisables a sub-emitter

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterName` | `FName` | The name of the sub-emitter to set it on |
| `bNewEnableState` | `bool` | The value to set it to |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFloatParameter`

```text
SetFloatParameter(ParameterName: FName, Param: float) -> void
```

Change a named float parameter

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

Set a named vector instance parameter on this ParticleSystemComponent.
	 	Updates the parameter if it already exists, or creates a new entry if not.

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

Set a named color instance parameter on this ParticleSystemComponent.
	 	Updates the parameter if it already exists, or creates a new entry if not.

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

Set a named actor instance parameter on this ParticleSystemComponent.
	 	Updates the parameter if it already exists, or creates a new entry if not.

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

Set a named material instance parameter on this ParticleSystemComponent.
	 	Updates the parameter if it already exists, or creates a new entry if not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTemplate`

```text
SetTemplate(NewTemplate: UParticleSystem *) -> void
```

Change the ParticleSystem used by this ParticleSystemComponent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTemplate` | `UParticleSystem *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetNumActiveParticles`

```text
GetNumActiveParticles() -> int32
```

Get the current number of active particles in this system

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `BeginTrails`

```text
BeginTrails(InFirstSocketName: FName, InSecondSocketName: FName, InWidthMode: ETrailWidthMode, InWidth: float) -> void
```

Begins all trail emitters in this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFirstSocketName` | `FName` | The name of the first socket for the trail. |
| `InSecondSocketName` | `FName` | The name of the second socket for the trail. |
| `InWidthMode` | `ETrailWidthMode` | How the width value is applied to the trail. |
| `InWidth` | `float` | The width of the trail. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EndTrails`

```text
EndTrails() -> void
```

Ends all trail emitters in this component.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTrailSourceData`

```text
SetTrailSourceData(InFirstSocketName: FName, InSecondSocketName: FName, InWidthMode: ETrailWidthMode, InWidth: float) -> void
```

Sets the defining data for all trails in this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFirstSocketName` | `FName` | The name of the first socket for the trail. |
| `InSecondSocketName` | `FName` | The name of the second socket for the trail. |
| `InWidthMode` | `ETrailWidthMode` | How the width value is applied to the trail. |
| `InWidth` | `float` | The width of the trail. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSocketName`

```text
SetSocketName(InSocketName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocketName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ManuallyTickComponent`

```text
ManuallyTickComponent(DeltaTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_Activate`

```text
K2_Activate(bReset: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bReset` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_ActivateSystem`

```text
K2_ActivateSystem(bFlagAsJustAttached: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bFlagAsJustAttached` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_Deactivate`

```text
K2_Deactivate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DeactivateSystem`

```text
K2_DeactivateSystem() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CreateNamedDynamicMaterialInstance`

```text
CreateNamedDynamicMaterialInstance(InName: FName, SourceMaterial: UMaterialInterface *) -> UMaterialInstanceDynamic *
```

Creates a Dynamic Material Instance for the specified named material override, optionally from the supplied material.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InName` | `FName` | - |
| `SourceMaterial` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | - |

### `GetNamedMaterial`

```text
GetNamedMaterial(InName: FName) -> UMaterialInterface *
```

Returns a named material. If this named material is not found, returns NULL.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UMaterialInterface *` | - |

### `GenerateParticleEvent`

```text
GenerateParticleEvent(InEventName: FName, InEmitterTime: float, InLocation: FVector, InDirection: FVector, InVelocity: FVector) -> void
```

Record a kismet event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InEventName` | `FName` | The name of the event that fired. |
| `InEmitterTime` | `float` | The emitter time when the event fired. |
| `InLocation` | `FVector` | The location of the particle when the event fired. |
| `InDirection` | `FVector` | - |
| `InVelocity` | `FVector` | The velocity of the particle when the event fired. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVectorRandParameter`

```text
SetVectorRandParameter(ParameterName: FName, Param: FVector &, ParamLow: FVector &) -> void
```

Set a named random vector instance parameter on this ParticleSystemComponent.
	 	Updates the parameter if it already exists, or creates a new entry if not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `FVector &` | - |
| `ParamLow` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFloatRandParameter`

```text
SetFloatRandParameter(ParameterName: FName, Param: float, ParamLow: float) -> void
```

Set a named random float instance parameter on this ParticleSystemComponent.
	 	Updates the parameter if it already exists, or creates a new entry if not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `float` | - |
| `ParamLow` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RewindEmitterInstances`

```text
RewindEmitterInstances() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnSystemFinished`

```text
OnSystemFinished(PSystem: UParticleSystemComponent*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PSystem` | `UParticleSystemComponent*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
