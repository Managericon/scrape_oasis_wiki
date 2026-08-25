---
id: "api:class:UGameViewportClient"
title: "UGameViewportClient"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGameViewportClient.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGameViewportClient

A game viewport (FViewport) is a high-level abstract interface for the
  platform specific rendering, audio, and input subsystems.
  GameViewportClient is the engine's interface to a game viewport.
  Exactly one GameViewportClient is created for each instance of the game.  The
  only case (so far) where you might have a single instance of Engine, but
  multiple instances of the game (and thus multiple GameViewportClients) is when
  you have more than one PIE window running.
 
  Responsibilities:
  propagating input events to the global interactions list
 
  @see UGameViewportClient

## Inheritance

`UScriptViewportClient` -> `FExec`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ViewportConsole` | `UConsole *` | The viewport's console.   Might be null on consoles |
| `DebugProperties` | `TArray < struct FDebugDisplayProperty >` | @todo document |
| `World` | `UWorld *` | The relative world context for this viewport |
| `GameInstance` | `UGameInstance *` | - |

## Functions

### `SSSwapControllers`

```text
SSSwapControllers() -> void
```

Rotates controller ids among gameplayers, useful for testing splitscreen with only one controller.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ShowTitleSafeArea`

```text
ShowTitleSafeArea() -> void
```

Exec for toggling the display of the title safe area

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetConsoleTarget`

```text
SetConsoleTarget(PlayerIndex: int32) -> void
```

Sets the player which console commands will be executed in the context of.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
