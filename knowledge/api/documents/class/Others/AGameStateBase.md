---
id: "api:class:AGameStateBase"
title: "AGameStateBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/AGameStateBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AGameStateBase

GameStateBase is a class that manages the game's global state, and is spawned by GameModeBase.
  It exists on both the client and the server and is fully replicated.

## Inheritance

`AInfo`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GameModeClass` | `TSubclassOf < AGameModeBase >` | Class of the server's game mode, assigned by GameModeBase. |
| `AuthorityGameMode` | `AGameModeBase *` | Instance of the current game mode, exists only on the server. For non-authority clients, this will be NULL. |
| `SpectatorClass` | `TSubclassOf < ASpectatorPawn >` | Class used by spectators, assigned by GameModeBase. |
| `PlayerArray` | `TArray < APlayerState * >` | Array of all PlayerStates, maintained on both server and clients (PlayerStates are always relevant) |
| `bReplicatedHasBegunPlay` | `bool` | Replicated when GameModeBase->StartPlay has been called so the client will also start play |
| `ReplicatedWorldTimeSeconds` | `float` | Server TimeSeconds. Useful for syncing up animation and gameplay. |
| `ServerWorldTimeSecondsDelta` | `float` | The difference from the local world's TimeSeconds and the server world's TimeSeconds. |
| `ServerWorldTimeSecondsUpdateFrequency` | `float` | Frequency that the server updates the replicated TimeSeconds from the world. Set to zero to disable periodic updates. |
| `bRecordControllerReplay` | `bool` | If use rec ctrl in replay |
| `PauseInfo` | `bool` | - |

## Functions

### `GetServerWorldTimeSeconds`

```text
GetServerWorldTimeSeconds() -> float
```

Returns the simulated TimeSeconds on the server, will be synchronized on client and server

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetServerWorldTimeSecondsForReplay`

```text
GetServerWorldTimeSecondsForReplay() -> float
```

Returns the simulated TimeSeconds on the server while playing replay, with fastforward skipped time considered

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `HasBegunPlay`

```text
HasBegunPlay() -> bool
```

Returns true if the world has started play (called BeginPlay on actors)

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `HasMatchStarted`

```text
HasMatchStarted() -> bool
```

Returns true if the world has started match (called MatchStarted callbacks)

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetPlayerStartTime`

```text
GetPlayerStartTime(Controller: AController *) -> float
```

Returns the time that should be used as when a player started

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Controller` | `AController *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetPlayerRespawnDelay`

```text
GetPlayerRespawnDelay(Controller: AController *) -> float
```

Returns how much time needs to be spent before a player can respawn

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Controller` | `AController *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `OnRep_GameModeClass`

```text
OnRep_GameModeClass() -> void
```

GameModeBase class notification callback.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_SpectatorClass`

```text
OnRep_SpectatorClass() -> void
```

Callback when we receive the spectator class

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_ReplicatedHasBegunPlay`

```text
OnRep_ReplicatedHasBegunPlay() -> void
```

By default calls BeginPlay and StartMatch

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_ReplicatedWorldTimeSeconds`

```text
OnRep_ReplicatedWorldTimeSeconds(OldValue: float &) -> void
```

Allows clients to calculate ServerWorldTimeSecondsDelta

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldValue` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_RecordControllerReplay`

```text
OnRep_RecordControllerReplay() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_PauseInfo`

```text
OnRep_PauseInfo() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnPauseState`

```text
OnPauseState(bIsPause: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsPause` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
