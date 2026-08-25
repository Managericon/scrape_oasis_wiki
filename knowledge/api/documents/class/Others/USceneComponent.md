---
id: "api:class:USceneComponent"
title: "USceneComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/USceneComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# USceneComponent

A SceneComponent has a transform and supports attachment, but has no rendering or collision capabilities.
  Useful as a 'dummy' component in the hierarchy to offset others.

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PhysicsVolume` | `TWeakObjectPtr < APhysicsVolume >` | Physics Volume in which this SceneComponent is located |
| `AttachParent` | `USceneComponent *` | What we are currently attached to. If valid, RelativeLocation etc. are used relative to this object |
| `AttachSocketName` | `FName` | Optional socket name on AttachParent that we are attached to. |
| `AttachChildren` | `TArray < USceneComponent * >` | List of child SceneComponents that are attached to us. |
| `ClientAttachedChildren` | `TArray < USceneComponent * >` | Set of attached SceneComponents that were attached by the client so we can fix up AttachChildren when it is replicated to us. |
| `RelativeLocation` | `FVector` | Location of the component relative to its parent |
| `RelativeRotation` | `FRotator` | Rotation of the component relative to its parent |
| `RelativeScale3D` | `FVector` | Non-uniform scaling of the component relative to its parent.<br>		Note that scaling is always applied in local space (no shearing etc) |
| `ComponentToWorld` | `FTransform` | Current transform of the component, relative to the world |
| `ComponentVelocity` | `FVector` | Velocity of the component.<br>	 @see GetComponentVelocity() |
| `bComponentToWorldUpdated` | `uint8` | True if we have ever updated ComponentToWorld based on RelativeLocationRotationScale. Used at startup to make sure it is initialized. |
| `bAbsoluteLocation` | `uint8` | If RelativeLocation should be considered relative to the world, rather than the parent |
| `bAbsoluteRotation` | `uint8` | If RelativeRotation should be considered relative to the world, rather than the parent |
| `bAbsoluteScale` | `uint8` | If RelativeScale3D should be considered relative to the world, rather than the parent |
| `bVisible` | `uint8` | Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow. |
| `bHiddenInGame` | `uint8` | Whether to hide the primitive in game, if the primitive is Visible. |
| `bShouldUpdatePhysicsVolume` | `uint8` | Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.<br>	  @see GetPhysicsVolume() |
| `bBoundsChangeTriggersStreamingDataRebuild` | `uint8` | If true, a change in the bounds of the component will call trigger a streaming data rebuild |
| `bUseAttachParentBound` | `uint8` | If true, this component uses its parents bounds when attached.<br>	   This can be a significant optimization with many components attached together. |
| `bShouldUpdateOverLaps` | `uint8` | - |
| `bForceUpdateChildCompTransform` | `uint8` | - |
| `bEnableUpdateTransformOption` | `uint8` | - |
| `bUpdateTransformOptionConsiderAbsolute` | `uint8` | - |
| `bOpenServerOptLite` | `uint8` | Simplify server move<br>		by zoranouyang |
| `bShouldUseTeleportMove` | `uint8` | - |
| `bForceFrameInterpolate` | `uint8` | - |
| `bEnableParallelMove` | `uint8` | - |
| `Mobility` | `TEnumAsByte < EComponentMobility :: Type >` | How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor. |
| `DetailMode` | `TEnumAsByte < enum EDetailMode >` | If detail mode is >= system detail mode, primitive won't be rendered. |
| `UpdateTransformOption` | `EUpdateTransformOption` | - |
| `bIsFppLayerRecursive` | `uint8` | - |
| `bDisableFppLayerRecursive` | `uint8` | - |
| `bAbsoluteTranslation_DEPRECATED` | `uint8` | - |
| `bVisualizeComponent` | `uint8` | - |
| `bVisibilityMayChange` | `uint8` | Let Editor tool, like pvs, to know whether visibility may change |
| `RelativeTranslation_DEPRECATED` | `FVector` | - |

## Functions

### `GetBoundsOirgin`

```text
GetBoundsOirgin() -> FVector
```

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetBoundsBoxExtent`

```text
GetBoundsBoxExtent() -> FVector
```

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `OnRep_Transform`

```text
OnRep_Transform() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_AttachParent`

```text
OnRep_AttachParent() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_AttachChildren`

```text
OnRep_AttachChildren() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_AttachSocketName`

```text
OnRep_AttachSocketName() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_Visibility`

```text
OnRep_Visibility(OldValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetRelativeLocation`

```text
K2_SetRelativeLocation(NewLocation: FVector, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Set the location of the component relative to its parent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector` | New location of the component relative to its parent. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetRelativeRotation`

```text
K2_SetRelativeRotation(NewRotation: FRotator, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Set the rotation of the component relative to its parent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRotation` | `FRotator` | New rotation of the component relative to its parent |
| `bSweep` | `bool` | Whether we sweep to the destination (currently not supported for rotation). |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetRelativeTransform`

```text
K2_SetRelativeTransform(NewTransform: FTransform &, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Set the transform of the component relative to its parent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTransform` | `FTransform &` | New transform of the component relative to its parent. |
| `bSweep` | `bool` | Whether we sweep to the destination (currently not supported for rotation). |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetRelativeTransform`

```text
GetRelativeTransform() -> FTransform
```

Returns the transform of the component relative to its parent

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `ResetRelativeTransform`

```text
ResetRelativeTransform() -> void
```

Reset the transform of the component relative to its parent. Sets relative location to zero, relative rotation to no rotation, and Scale to 1.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRelativeScale3D`

```text
SetRelativeScale3D(NewScale3D: FVector) -> void
```

Set the non-uniform scale of the component relative to its parent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewScale3D` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddRelativeLocation`

```text
K2_AddRelativeLocation(DeltaLocation: FVector, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the translation of the component relative to its parent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaLocation` | `FVector` | Change in location of the component relative to its parent |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddRelativeRotation`

```text
K2_AddRelativeRotation(DeltaRotation: FRotator, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta the rotation of the component relative to its parent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaRotation` | `FRotator` | Change in rotation of the component relative to is parent. |
| `bSweep` | `bool` | Whether we sweep to the destination (currently not supported for rotation). |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddLocalOffset`

```text
K2_AddLocalOffset(DeltaLocation: FVector, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the location of the component in its local reference frame

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaLocation` | `FVector` | Change in location of the component in its local reference frame. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddLocalRotation`

```text
K2_AddLocalRotation(DeltaRotation: FRotator, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the rotation of the component in its local reference frame

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaRotation` | `FRotator` | Change in rotation of the component in its local reference frame. |
| `bSweep` | `bool` | Whether we sweep to the destination (currently not supported for rotation). |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddLocalTransform`

```text
K2_AddLocalTransform(DeltaTransform: FTransform &, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the transform of the component in its local reference frame. Scale is unchanged.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTransform` | `FTransform &` | Change in transform of the component in its local reference frame. Scale is unchanged. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetWorldLocation`

```text
K2_SetWorldLocation(NewLocation: FVector, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Put this component at the specified location in world space. Updates relative location to achieve the final world location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector` | New location in world space for the component. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetWorldRotation`

```text
K2_SetWorldRotation(NewRotation: FRotator, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Put this component at the specified rotation in world space. Updates relative rotation to achieve the final world rotation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRotation` | `FRotator` | New rotation in world space for the component. |
| `bSweep` | `bool` | Whether we sweep to the destination (currently not supported for rotation). |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWorldScale3D`

```text
SetWorldScale3D(NewScale: FVector) -> void
```

Set the relative scale of the component to put it at the supplied scale in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewScale` | `FVector` | New scale in world space for this component. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetWorldTransform`

```text
K2_SetWorldTransform(NewTransform: FTransform &, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Set the transform of the component in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTransform` | `FTransform &` | New transform in world space for the component. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddWorldOffset`

```text
K2_AddWorldOffset(DeltaLocation: FVector, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the location of the component in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaLocation` | `FVector` | Change in location in world space for the component. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddWorldRotation`

```text
K2_AddWorldRotation(DeltaRotation: FRotator, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the rotation of the component in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaRotation` | `FRotator` | Change in rotation in world space for the component. |
| `bSweep` | `bool` | Whether we sweep to the destination (currently not supported for rotation). |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddWorldTransform`

```text
K2_AddWorldTransform(DeltaTransform: FTransform &, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the transform of the component in world space. Scale is unchanged.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTransform` | `FTransform &` | Change in transform in world space for the component. Scale is unchanged. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_GetComponentLocation`

```text
K2_GetComponentLocation() -> FVector
```

Return location of the component, in world space

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `K2_GetComponentRotation`

```text
K2_GetComponentRotation() -> FRotator
```

Returns rotation of the component, in world space.

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `K2_GetComponentScale`

```text
K2_GetComponentScale() -> FVector
```

Returns scale of the component, in world space.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `K2_GetComponentToWorld`

```text
K2_GetComponentToWorld() -> FTransform
```

Get the current component-to-world transform for this component

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `GetForwardVector`

```text
GetForwardVector() -> FVector
```

Get the forward (X) unit direction vector from this component, in world space.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetUpVector`

```text
GetUpVector() -> FVector
```

Get the up (Z) unit direction vector from this component, in world space.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRightVector`

```text
GetRightVector() -> FVector
```

Get the right (Y) unit direction vector from this component, in world space.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `IsSimulatingPhysics`

```text
IsSimulatingPhysics(BoneName: FName) -> bool
```

Returns whether the specified body is currently using physics simulation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsAnySimulatingPhysics`

```text
IsAnySimulatingPhysics() -> bool
```

Returns whether the specified body is currently using physics simulation

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetAttachParent`

```text
GetAttachParent() -> USceneComponent *
```

Get the SceneComponent we are attached to.

**Returns**

| Type | Description |
|---|---|
| `USceneComponent *` | - |

### `GetAttachSocketName`

```text
GetAttachSocketName() -> FName
```

Get the socket we are attached to.

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `GetParentComponents`

```text
GetParentComponents(Parents: TArray < USceneComponent * > &) -> void
```

Gets all parent components up to and including the root component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Parents` | `TArray < USceneComponent * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetNumChildrenComponents`

```text
GetNumChildrenComponents() -> int32
```

Gets the number of attached children components

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetChildComponent`

```text
GetChildComponent(ChildIndex: int32) -> USceneComponent *
```

Gets the attached child component at the specified location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ChildIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `USceneComponent *` | - |

### `GetChildrenComponents`

```text
GetChildrenComponents(bIncludeAllDescendants: bool, Children: TArray < USceneComponent * > &) -> void
```

Gets all the attached child components

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIncludeAllDescendants` | `bool` | Whether to include all descendants in the list of children (i.e. grandchildren, great grandchildren, etc.) |
| `Children` | `TArray < USceneComponent * > &` | The list of attached child components |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AttachTo`

```text
K2_AttachTo(InParent: USceneComponent *, InSocketName: FName, AttachType: EAttachLocation :: Type, bWeldSimulatedBodies: bool) -> bool
```

Attach this component to another scene component, optionally at a named socket. It is valid to call this on components whether or not they have been Registered.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InParent` | `USceneComponent *` | Parent to attach to. |
| `InSocketName` | `FName` | Optional socket to attach to on the parent. |
| `AttachType` | `EAttachLocation :: Type` | How to handle transform when attaching (Keep relative offset, keep world position, etc). |
| `bWeldSimulatedBodies` | `bool` | Whether to weld together simulated physics bodies. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if attachment is successful (or already attached to requested parentsocket), false if attachment is rejected and there is no change in AttachParent. |

### `K2_AttachToComponent`

```text
K2_AttachToComponent(Parent: USceneComponent *, SocketName: FName, LocationRule: EAttachmentRule, RotationRule: EAttachmentRule, ScaleRule: EAttachmentRule, bWeldSimulatedBodies: bool) -> bool
```

Attach this component to another scene component, optionally at a named socket. It is valid to call this on components whether or not they have been Registered.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Parent` | `USceneComponent *` | Parent to attach to. |
| `SocketName` | `FName` | Optional socket to attach to on the parent. |
| `LocationRule` | `EAttachmentRule` | How to handle translation when attaching. |
| `RotationRule` | `EAttachmentRule` | How to handle rotation when attaching. |
| `ScaleRule` | `EAttachmentRule` | How to handle scale when attaching. |
| `bWeldSimulatedBodies` | `bool` | Whether to weld together simulated physics bodies. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if attachment is successful (or already attached to requested parentsocket), false if attachment is rejected and there is no change in AttachParent. |

### `SnapTo`

```text
SnapTo(InParent: USceneComponent *, InSocketName: FName) -> bool
```

Zeroes out the relative transform of the component, and calls AttachTo(). Useful for attaching directly to a scene component or socket location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InParent` | `USceneComponent *` | - |
| `InSocketName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `DetachFromParent`

```text
DetachFromParent(bMaintainWorldPosition: bool, bCallModify: bool) -> void
```

Detach this component from whatever it is attached to. Automatically unwelds components that are welded together (See WeldTo)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bMaintainWorldPosition` | `bool` | If true, update the relative location of the component to keep its world position the same |
| `bCallModify` | `bool` | If true, call Modify() on the component and the current attach parent component |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DetachFromComponent`

```text
K2_DetachFromComponent(LocationRule: EDetachmentRule, RotationRule: EDetachmentRule, ScaleRule: EDetachmentRule, bCallModify: bool) -> void
```

Detach this component from whatever it is attached to. Automatically unwelds components that are welded together (See WeldTo)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LocationRule` | `EDetachmentRule` | How to handle translations when detaching. |
| `RotationRule` | `EDetachmentRule` | How to handle rotation when detaching. |
| `ScaleRule` | `EDetachmentRule` | How to handle scales when detaching. |
| `bCallModify` | `bool` | If true, call Modify() on the component and the current attach parent component |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAllSocketNames`

```text
GetAllSocketNames() -> TArray < FName >
```

Gets the names of all the sockets on the component.

**Returns**

| Type | Description |
|---|---|
| `TArray < FName >` | Get the names of all the sockets on the component. |

### `GetSocketTransform`

```text
GetSocketTransform(InSocketName: FName, TransformSpace: ERelativeTransformSpace) -> FTransform
```

Get world-space socket transform.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocketName` | `FName` | Name of the socket or the bone to get the transform |
| `TransformSpace` | `ERelativeTransformSpace` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | Socket transform in world space if socket if found. Otherwise it will return component's transform in world space. |

### `GetSocketLocation`

```text
GetSocketLocation(InSocketName: FName) -> FVector
```

Get world-space socket or bone location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocketName` | `FName` | Name of the socket or the bone to get the transform |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Socket transform in world space if socket if found. Otherwise it will return component's transform in world space. |

### `GetSocketRotation`

```text
GetSocketRotation(InSocketName: FName) -> FRotator
```

Get world-space socket or bone  FRotator rotation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocketName` | `FName` | Name of the socket or the bone to get the transform |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | Socket transform in world space if socket if found. Otherwise it will return component's transform in world space. |

### `GetSocketQuaternion`

```text
GetSocketQuaternion(InSocketName: FName) -> FQuat
```

Get world-space socket or bone FQuat rotation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocketName` | `FName` | Name of the socket or the bone to get the transform |

**Returns**

| Type | Description |
|---|---|
| `FQuat` | Socket transform in world space if socket if found. Otherwise it will return component's transform in world space. |

### `GetSocketScale`

```text
GetSocketScale(InSocketName: FName) -> FVector
```

Get world-space socket or bone scale.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocketName` | `FName` | Name of the socket or the bone to get the scale |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Socket scale in world space if socket if found. Otherwise it will return component's scale in world space. |

### `DoesSocketExist`

```text
DoesSocketExist(InSocketName: FName) -> bool
```

return true if socket with the given name exists

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocketName` | `FName` | Name of the socket or the bone to get the transform |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the socket with the given name exists. Otherwise, return false |

### `GetComponentVelocity`

```text
GetComponentVelocity() -> FVector
```

Get velocity of the component: either ComponentVelocity, or the velocity of the physics body if simulating physics.

**Returns**

| Type | Description |
|---|---|
| `FVector` | Velocity of the component |

### `IsVisible`

```text
IsVisible() -> bool
```

Is this component visible or not in game

**Returns**

| Type | Description |
|---|---|
| `bool` | true if visible |

### `SetVisibility`

```text
SetVisibility(bNewVisibility: bool, bPropagateToChildren: bool, bForceNoPropagate: bool) -> void
```

Set visibility of the component, if during game use this to turn onoff

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewVisibility` | `bool` | - |
| `bPropagateToChildren` | `bool` | - |
| `bForceNoPropagate` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ToggleVisibility`

```text
ToggleVisibility(bPropagateToChildren: bool) -> void
```

Toggle visibility of the component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bPropagateToChildren` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHiddenInGame`

```text
SetHiddenInGame(NewHidden: bool, bPropagateToChildren: bool) -> void
```

Changes the value of HiddenGame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewHidden` | `bool` | - The value to assign to HiddenGame. |
| `bPropagateToChildren` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsForceFrameInterpolate`

```text
IsForceFrameInterpolate() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetForceFrameInterpolate`

```text
SetForceFrameInterpolate(InForceFrameInterpolate: bool) -> void
```

set bForceDynamic

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InForceFrameInterpolate` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetComponentTransformViewTranslatedBP`

```text
GetComponentTransformViewTranslatedBP() -> FTransform
```

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `GetComponentLocal`

```text
GetComponentLocal(localTransform: FTransform &) -> FTransform
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `localTransform` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `GetPhysicsVolume`

```text
GetPhysicsVolume() -> APhysicsVolume *
```

Get the PhysicsVolume overlapping this component.

**Returns**

| Type | Description |
|---|---|
| `APhysicsVolume *` | - |

### `K2_SetRelativeLocationAndRotation`

```text
K2_SetRelativeLocationAndRotation(NewLocation: FVector, NewRotation: FRotator, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Set the location and rotation of the component relative to its parent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector` | New location of the component relative to its parent. |
| `NewRotation` | `FRotator` | New rotation of the component relative to its parent. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAbsolute`

```text
SetAbsolute(bNewAbsoluteLocation: bool, bNewAbsoluteRotation: bool, bNewAbsoluteScale: bool) -> void
```

Set which parts of the relative transform should be relative to parent, and which should be relative to world

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewAbsoluteLocation` | `bool` | - |
| `bNewAbsoluteRotation` | `bool` | - |
| `bNewAbsoluteScale` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsAbsoluteLocation`

```text
IsAbsoluteLocation(ContainsParent: bool) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ContainsParent` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `K2_SetWorldLocationAndRotation`

```text
K2_SetWorldLocationAndRotation(NewLocation: FVector, NewRotation: FRotator, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Set the relative location and rotation of the component to put it at the supplied pose in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector` | New location in world space for the component. |
| `NewRotation` | `FRotator` | New rotation in world space for the component. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetMobility`

```text
K2_SetMobility(NewMobility: EComponentMobility :: Type) -> void
```

Set how often this component is allowed to move during runtime. Causes a component re-register if the component is already registered

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewMobility` | `EComponentMobility :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFppLayerRecursive`

```text
SetFppLayerRecursive(InIsFppLayer: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIsFppLayer` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDisableFppLayerRecursive`

```text
SetDisableFppLayerRecursive(bDisable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bDisable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `PhysicsVolumeChangedDelegate`

```text
PhysicsVolumeChangedDelegate(NewVolume: APhysicsVolume*) -> void
```

Delegate that will be called when PhysicsVolume has been changed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewVolume` | `APhysicsVolume*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `TransformUpdatedDynamic`

```text
TransformUpdatedDynamic() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
