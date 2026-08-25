---
id: "api:class:ACharacter"
title: "ACharacter"
source: "https://developer.gp.qq.com/api/class/detail/Others/ACharacter.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
