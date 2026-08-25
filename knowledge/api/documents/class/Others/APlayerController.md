---
id: "api:class:APlayerController"
title: "APlayerController"
source: "https://developer.gp.qq.com/api/class/detail/Others/APlayerController.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
