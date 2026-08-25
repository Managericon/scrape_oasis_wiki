---
id: "api:class:AGameState"
title: "AGameState"
source: "https://developer.gp.qq.com/api/class/detail/Others/AGameState.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AGameState

GameState is a subclass of GameStateBase that behaves like a multiplayer match-based game.
  It is tied to functionality in GameMode.

## Inheritance

`AGameStateBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MatchState` | `FName` | What match state we are currently in |
| `PreviousMatchState` | `FName` | Previous map state, used to handle if multiple transitions happen per frame |
| `ElapsedTime` | `int32` | Elapsed game time since match has started. |

## Functions

### `OnRep_MatchState`

```text
OnRep_MatchState() -> void
```

Match state has changed

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_ElapsedTime`

```text
OnRep_ElapsedTime() -> void
```

Gives clients the chance to do something when time gets updates

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetGeneralCampNameByCampID`

```text
GetGeneralCampNameByCampID(CampID: int32) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CampID` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetGeneralCampRelation`

```text
GetGeneralCampRelation(CampAID: int32, CampBID: int32) -> ECampRelation
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CampAID` | `int32` | - |
| `CampBID` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `ECampRelation` | - |

### `GetGameModeGeneralDataAsset`

```text
GetGameModeGeneralDataAsset() -> UGameModeGeneralDataAsset *
```

**Returns**

| Type | Description |
|---|---|
| `UGameModeGeneralDataAsset *` | - |

## Language

`cpp`
