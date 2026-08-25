---
id: "api:class:UCheatManager"
title: "UCheatManager"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCheatManager.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
