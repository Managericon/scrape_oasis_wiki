---
id: "api:class:AGameMode"
title: "AGameMode"
source: "https://developer.gp.qq.com/api/class/detail/Others/AGameMode.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AGameMode

GameMode is a subclass of GameModeBase that behaves like a multiplayer match-based game.
  It has default behavior for picking spawn points and match state.
  If you want a simpler base, inherit from GameModeBase instead.

## Inheritance

`AGameModeBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MatchState` | `FName` | What match state we are currently in |
| `bDelayedStart` | `uint32` | Whether the game should immediately start when the first player logs in. Affects the default behavior of ReadyToStartMatch |
| `NumSpectators` | `int32` | Current number of spectators. |
| `NumPlayers` | `int32` | Current number of human players. |
| `NumBots` | `int32` | number of non-human players (AI controlled but participating as a player). |
| `MinRespawnDelay` | `float` | Minimum time before player can respawn after dying. |
| `NumTravellingPlayers` | `int32` | Number of players that are still traveling from a previous map |
| `EngineMessageClass` | `TSubclassOf < ULocalMessage >` | Contains strings describing localized game agnostic messages. |
| `InactivePlayerArray` | `TArray < APlayerState * >` | PlayerStates of players who have disconnected from the server (saved in case they reconnect) |
| `bEnabelPawnPool` | `bool` | Weather to enable Gamemode Pawn Pool |
| `InactivePlayerStateLifeSpan` | `float` | Time a playerstate will stick around in an inactive state after a player logout |
| `bHandleDedicatedServerReplays` | `bool` | If true, dedicated servers will record replays when HandleMatchHasStartedHandleMatchHasStopped is called |

## Functions

### `GetMatchState`

```text
GetMatchState() -> FName
```

Returns the current match state, this is an accessor to protect the state machine flow

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `IsMatchInProgress`

```text
IsMatchInProgress() -> bool
```

Returns true if the match state is InProgress or other gameplay state

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `HasMatchEnded`

```text
HasMatchEnded() -> bool
```

Returns true if the match state is WaitingPostMatch or later

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `StartMatch`

```text
StartMatch() -> void
```

Transition from WaitingToStart to InProgress. You can call this manually, will also get called if ReadyToStartMatch returns true

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EndMatch`

```text
EndMatch() -> void
```

Transition from InProgress to WaitingPostMatch. You can call this manually, will also get called if ReadyToEndMatch returns true

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestartGame`

```text
RestartGame() -> void
```

Restart the game, by default travel to the current map

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AbortMatch`

```text
AbortMatch() -> void
```

Report that a match has failed due to unrecoverable error

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_OnSetMatchState`

```text
K2_OnSetMatchState(NewState: FName) -> void
```

Implementable event to respond to match state changes

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewState` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReadyToStartMatch`

```text
ReadyToStartMatch() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | True if ready to Start Match. Games should override this |

### `ReadyToEndMatch`

```text
ReadyToEndMatch() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if ready to End Match. Games should override this |

### `Say`

```text
Say(Msg: FString &) -> void
```

Exec command to broadcast a string to all players

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Msg` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBandwidthLimit`

```text
SetBandwidthLimit(AsyncIOBandwidthLimit: float) -> void
```

Alters the synthetic bandwidth limit for a running game.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AsyncIOBandwidthLimit` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
