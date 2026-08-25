---
id: "api:class:ULevelSequencePlayer"
title: "ULevelSequencePlayer"
source: "https://developer.gp.qq.com/api/class/detail/Others/ULevelSequencePlayer.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ULevelSequencePlayer

ULevelSequencePlayer is used to actually "play" an level sequence asset at runtime.
 
  This class keeps track of playback state and provides functions for manipulating
  an level sequence while its playing.

## Inheritance

`UMovieSceneSequencePlayer`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AdditionalEventReceivers` | `TArray < UObject * >` | Array of additional event receivers |

## Functions

### `CreateLevelSequencePlayer`

```text
CreateLevelSequencePlayer(WorldContextObject: UObject *, LevelSequence: ULevelSequence *, Settings: FMovieSceneSequencePlaybackSettings, OutActor: ALevelSequenceActor * &) -> ULevelSequencePlayer *
```

Create a new level sequence player.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | Context object from which to retrieve a UWorld. |
| `LevelSequence` | `ULevelSequence *` | The level sequence to play. |
| `Settings` | `FMovieSceneSequencePlaybackSettings` | The desired playback settings |
| `OutActor` | `ALevelSequenceActor * &` | The level sequence actor created to play this sequence. |

**Returns**

| Type | Description |
|---|---|
| `ULevelSequencePlayer *` | - |

### `GetEventReceivers`

```text
GetEventReceivers() -> TArray < UObject * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < UObject * >` | - |

## Delegates

### `OnCameraCut`

```text
OnCameraCut(CameraComponent: UCameraComponent*) -> void
```

Event triggered when there is a camera cut

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CameraComponent` | `UCameraComponent*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
