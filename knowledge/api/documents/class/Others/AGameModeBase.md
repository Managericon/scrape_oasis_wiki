---
id: "api:class:AGameModeBase"
title: "AGameModeBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/AGameModeBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AGameModeBase

The GameModeBase defines the game being played. It governs the game rules, scoring, what actors
  are allowed to exist in this game type, and who may enter the game.
 
  It is only instanced on the server and will never exist on the client. 
 
  A GameModeBase actor is instantiated when the level is initialized for gameplay in
  C++ UGameEngine::LoadMap().  
  
  The class of this GameMode actor is determined by (in order) either the URL ?game=xxx, 
  the GameMode Override value set in the World Settings, or the DefaultGameMode entry set 
  in the game's Project Settings.

## Inheritance

`AInfo` -> `IVirtualParallelWorld`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OptionsString` | `FString` | Save options string and parse it when needed |
| `GameSessionClass` | `TSubclassOf < AGameSession >` | Class of GameSession, which handles login approval and online game interface |
| `GameStateClass` | `TSubclassOf < AGameStateBase >` | Class of GameState associated with this GameMode. |
| `PlayerControllerClass` | `TSubclassOf < APlayerController >` | The class of PlayerController to spawn for players logging in. |
| `PlayerStateClass` | `TSubclassOf < APlayerState >` | A PlayerState of this class will be associated with every player to replicate relevant player information to all clients. |
| `HUDClass` | `TSubclassOf < AHUD >` | HUD class this game uses. |
| `DefaultPawnClass` | `TSubclassOf < APawn >` | The default pawn class used by players. |
| `SpectatorClass` | `TSubclassOf < ASpectatorPawn >` | The pawn class used by the PlayerController for players when spectating. |
| `ReplaySpectatorPlayerControllerClass` | `TSubclassOf < APlayerController >` | The PlayerController class used when spectating a network replay. |
| `GameSession` | `AGameSession *` | Game Session handles login approval, arbitration, online game interface |
| `GameState` | `AGameStateBase *` | GameState is used to replicate game state relevant properties to all clients. |
| `DefaultPlayerName` | `FText` | The default player name assigned to players that join with no name specified. |
| `bUseSeamlessTravel` | `uint32` | Whether the game perform map travels using SeamlessTravel() which loads in the background and doesn't disconnect clients |
| `bUnlimitedRegionZ` | `uint32` | - |
| `bStartPlayersAsSpectators` | `uint32` | Whether players should immediately spawn when logging in, or stay as spectators until they manually spawn |
| `bPauseable` | `uint32` | Whether the game is pauseable. |

## Functions

### `GetDefaultPawnClassForController`

```text
GetDefaultPawnClassForController(InController: AController *) -> UClass *
```

Returns default pawn class for given controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InController` | `AController *` | - |

**Returns**

| Type | Description |
|---|---|
| `UClass *` | - |

### `GetNumPlayers`

```text
GetNumPlayers() -> int32
```

Returns number of active human players, excluding spectators

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetNumSpectators`

```text
GetNumSpectators() -> int32
```

Returns number of human players currently spectating

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `StartPlay`

```text
StartPlay() -> void
```

Transitions to calls BeginPlay on actors.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HasMatchStarted`

```text
HasMatchStarted() -> bool
```

Returns true if the match start callbacks have been called

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ShouldReset`

```text
ShouldReset(ActorToReset: AActor *) -> bool
```

Overridable function to determine whether an Actor should have Reset called when the game has Reset called on it.
	  Default implementation returns true

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActorToReset` | `AActor *` | The actor to make a determination for |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if ActorToReset should have Reset() called on it while restarting the game, |

### `ResetLevel`

```text
ResetLevel() -> void
```

Overridable function called when resetting level. This is used to reset the game state while staying in the same map
	  Default implementation calls Reset() on all actors except GameMode and Controllers

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReturnToMainMenuHost`

```text
ReturnToMainMenuHost() -> void
```

Return to main menu, and disconnect any players

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_PostLogin`

```text
K2_PostLogin(NewPlayer: APlayerController *) -> void
```

Notification that a player has successfully logged in, and has been given a player controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayer` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_OnLogout`

```text
K2_OnLogout(ExitingController: AController *) -> void
```

Implementable event when a Controller with a PlayerState leaves the game.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ExitingController` | `AController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HandleStartingNewPlayer`

```text
HandleStartingNewPlayer(NewPlayer: APlayerController *) -> void
```

Signals that a player is ready to enter the game, which may start it up

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayer` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MustSpectate`

```text
MustSpectate(NewPlayerController: APlayerController *) -> bool
```

Returns true if NewPlayerController may only join the server as a spectator.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayerController` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `CanSpectate`

```text
CanSpectate(Viewer: APlayerController *, ViewTarget: APlayerState *) -> bool
```

Return whether Viewer is allowed to spectate from the point of view of ViewTarget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Viewer` | `APlayerController *` | - |
| `ViewTarget` | `APlayerState *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ChangeName`

```text
ChangeName(Controller: AController *, NewName: FString &, bNameChange: bool) -> void
```

Sets the name for a controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Controller` | `AController *` | The controller of the player to change the name of |
| `NewName` | `FString &` | The name to set the player to |
| `bNameChange` | `bool` | Whether the name is changing or if this is the first time it has been set |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_OnChangeName`

```text
K2_OnChangeName(Other: AController *, NewName: FString &, bNameChange: bool) -> void
```

Overridable event for GameMode blueprint to respond to a change name call

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Other` | `AController *` | - |
| `NewName` | `FString &` | The name to set the player to |
| `bNameChange` | `bool` | Whether the name is changing or if this is the first time it has been set |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ChoosePlayerStart`

```text
ChoosePlayerStart(Player: AController *) -> AActor *
```

Return the 'best' player start for this player to spawn from
	  Default implementation looks for a random unoccupied spot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `AController *` | is the controller for whom we are choosing a playerstart |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | AActor chosen as player start (usually a PlayerStart) |

### `FindPlayerStart`

```text
FindPlayerStart(Player: AController *, IncomingName: FString &) -> AActor *
```

Return the specific player start actor that should be used for the next spawn
	  This will either use a previously saved startactor, or calls ChoosePlayerStart

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `AController *` | The AController for whom we are choosing a Player Start |
| `IncomingName` | `FString &` | Specifies the tag of a Player Start to use |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | Actor chosen as player start (usually a PlayerStart) |

### `K2_FindPlayerStart`

```text
K2_FindPlayerStart(Player: AController *, IncomingName: FString &) -> AActor *
```

Return the specific player start actor that should be used for the next spawn
	  This will either use a previously saved startactor, or calls ChoosePlayerStart

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `AController *` | The AController for whom we are choosing a Player Start |
| `IncomingName` | `FString &` | Specifies the tag of a Player Start to use |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | Actor chosen as player start (usually a PlayerStart) |

### `PlayerCanRestart`

```text
PlayerCanRestart(Player: APlayerController *) -> bool
```

Returns true if it's valid to call RestartPlayer. By default will call Player->CanRestartPlayer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `RestartPlayer`

```text
RestartPlayer(NewPlayer: AController *) -> void
```

Tries to spawn the player's pawn, at the location returned by FindPlayerStart

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayer` | `AController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestartPlayerAtPlayerStart`

```text
RestartPlayerAtPlayerStart(NewPlayer: AController *, StartSpot: AActor *) -> void
```

Tries to spawn the player's pawn at the specified actor's location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayer` | `AController *` | - |
| `StartSpot` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestartPlayerAtTransform`

```text
RestartPlayerAtTransform(NewPlayer: AController *, SpawnTransform: FTransform &) -> void
```

Tries to spawn the player's pawn at a specific location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayer` | `AController *` | - |
| `SpawnTransform` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SpawnDefaultPawnFor`

```text
SpawnDefaultPawnFor(NewPlayer: AController *, StartSpot: AActor *) -> APawn *
```

Called during RestartPlayer to actually spawn the player's pawn, when using a start spot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayer` | `AController *` | - Controller for whom this pawn is spawned |
| `StartSpot` | `AActor *` | - Actor at which to spawn pawn |

**Returns**

| Type | Description |
|---|---|
| `APawn *` | a pawn of the default pawn class |

### `SpawnDefaultPawnAtTransform`

```text
SpawnDefaultPawnAtTransform(NewPlayer: AController *, SpawnTransform: FTransform &) -> APawn *
```

Called during RestartPlayer to actually spawn the player's pawn, when using a transform

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayer` | `AController *` | - Controller for whom this pawn is spawned |
| `SpawnTransform` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `APawn *` | a pawn of the default pawn class |

### `InitStartSpot`

```text
InitStartSpot(StartSpot: AActor *, NewPlayer: AController *) -> void
```

Called from RestartPlayerAtPlayerStart, can be used to initialize the start spawn actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartSpot` | `AActor *` | - |
| `NewPlayer` | `AController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_OnRestartPlayer`

```text
K2_OnRestartPlayer(NewPlayer: AController *) -> void
```

Implementable event called at the end of RestartPlayer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayer` | `AController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InitializeHUDForPlayer`

```text
InitializeHUDForPlayer(NewPlayer: APlayerController *) -> void
```

Initialize the AHUD object for a player. Games can override this to do something different

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlayer` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_OnSwapPlayerControllers`

```text
K2_OnSwapPlayerControllers(OldPC: APlayerController *, NewPC: APlayerController *) -> void
```

Called when a PlayerController is swapped to a new one during seamless travel

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldPC` | `APlayerController *` | - |
| `NewPC` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
