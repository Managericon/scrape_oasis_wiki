---
id: "api:class:AController"
title: "AController"
source: "https://developer.gp.qq.com/api/class/detail/Others/AController.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
