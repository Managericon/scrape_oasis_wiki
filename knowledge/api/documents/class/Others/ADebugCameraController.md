---
id: "api:class:ADebugCameraController"
title: "ADebugCameraController"
source: "https://developer.gp.qq.com/api/class/detail/Others/ADebugCameraController.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
