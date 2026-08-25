---
id: "api:class:UMovieSceneSequencePlayer"
title: "UMovieSceneSequencePlayer"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSequencePlayer.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMovieSceneSequencePlayer

Abstract class that provides consistent player behaviour for various animation players

## Inheritance

`UObject` -> `IMovieScenePlayer`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Status` | `TEnumAsByte < EMovieScenePlayerStatus :: Type >` | Movie player status. |
| `bReversePlayback` | `uint32` | Whether we're currently playing in reverse. |
| `bPendingFirstUpdate` | `uint32` | True where we're waiting for the first update of the sequence after calling StartPlayingNextTick. |
| `Sequence` | `UMovieSceneSequence *` | The sequence to play back |
| `TimeCursorPosition` | `float` | The current time cursor position within the sequence (in seconds) |
| `StartTime` | `float` | Time time at which to start playing the sequence (defaults to the lower bound of the sequence's play range) |
| `EndTime` | `float` | Time time at which to end playing the sequence (defaults to the upper bound of the sequence's play range) |
| `CurrentNumLoops` | `int32` | The number of times we have looped in the current playback |
| `PlaybackSettings` | `FMovieSceneSequencePlaybackSettings` | Specific playback settings for the animation. |
| `RootTemplateInstance` | `FMovieSceneRootEvaluationTemplateInstance` | The root template instance we're evaluating |

## Functions

### `Play`

```text
Play() -> void
```

Start playback forwards from the current time cursor position, using the current play rate.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlayReverse`

```text
PlayReverse() -> void
```

Reverse playback.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ChangePlaybackDirection`

```text
ChangePlaybackDirection() -> void
```

Changes the direction of playback (go in reverse if it was going forward, or vice versa)

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SeekPosition`

```text
SeekPosition(NewTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlayLooping`

```text
PlayLooping(NumLoops: int32) -> void
```

Start playback from the current time cursor position, looping the specified number of times.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NumLoops` | `int32` | - The number of loops to play. -1 indicates infinite looping. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StartPlayingNextTick`

```text
StartPlayingNextTick() -> void
```

Start playback from the current time cursor position, using the current play rate. Does not update the animation until next tick.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Pause`

```text
Pause() -> void
```

Pause playback.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Scrub`

```text
Scrub() -> void
```

Scrub playback.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Stop`

```text
Stop() -> void
```

Stop playback.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GoToEndAndStop`

```text
GoToEndAndStop() -> void
```

Go to end and stop.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPlaybackPosition`

```text
GetPlaybackPosition() -> float
```

Get the current playback position

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetPlaybackPosition`

```text
SetPlaybackPosition(NewPlaybackPosition: float) -> void
```

Set the current playback position

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlaybackPosition` | `float` | - The new playback position to set. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPlaybackPostionWithloop`

```text
SetPlaybackPostionWithloop(NewTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTargetTimePostionWithloop`

```text
GetTargetTimePostionWithloop(NewTime: float) -> float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `JumpToPosition`

```text
JumpToPosition(NewPlaybackPosition: float) -> void
```

Jump to new playback position

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlaybackPosition` | `float` | - The new playback position to set. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `JumpToPositionEx`

```text
JumpToPositionEx(NewPlaybackPosition: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPlaybackPosition` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsPlaying`

```text
IsPlaying() -> bool
```

Check whether the sequence is actively playing.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsPaused`

```text
IsPaused() -> bool
```

Check whether the sequence is paused.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetLength`

```text
GetLength() -> float
```

Get the playback length of the sequence

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetPlayRate`

```text
GetPlayRate() -> float
```

Get the playback rate of this player.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `IsEvaluating`

```text
IsEvaluating() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetPlayRate`

```text
SetPlayRate(PlayRate: float) -> void
```

Set the playback rate of this player. Negative values will play the animation in reverse.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayRate` | `float` | - The new rate of playback for the animation. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPlayLoopCount`

```text
SetPlayLoopCount(NumLoops: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NumLoops` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPlaybackRange`

```text
SetPlaybackRange(NewStartTime: float, NewEndTime: float) -> void
```

Sets the range in time to be played back by this player, overriding the default range stored in the asset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewStartTime` | `float` | The new starting time for playback |
| `NewEndTime` | `float` | The new ending time for playback. Must be larger than the start time. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPlaybackStart`

```text
GetPlaybackStart() -> float
```

Get the offset within the level sequence to start playing

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetPlaybackStartSeconds`

```text
GetPlaybackStartSeconds() -> float
```

Get the offset seconds within the level sequence to start playing

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetPlaybackEnd`

```text
GetPlaybackEnd() -> float
```

Get the offset within the level sequence to finish playing

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetPlaybackEndSeconds`

```text
GetPlaybackEndSeconds() -> float
```

Get the offset seconds within the level sequence to finish playing

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetBoundObjects`

```text
GetBoundObjects(ObjectBinding: FMovieSceneObjectBindingID) -> TArray < UObject * >
```

Retrieve all objects currently bound to the specified binding identifier

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ObjectBinding` | `FMovieSceneObjectBindingID` | - |

**Returns**

| Type | Description |
|---|---|
| `TArray < UObject * >` | - |

## Delegates

### `OnPlay`

```text
OnPlay() -> void
```

Event triggered when the level sequence player is played

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPlayReverse`

```text
OnPlayReverse() -> void
```

Event triggered when the level sequence player is played in reverse

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnStop`

```text
OnStop() -> void
```

Event triggered when the level sequence player is stopped

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPause`

```text
OnPause() -> void
```

Event triggered when the level sequence player is paused

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnFinished`

```text
OnFinished() -> void
```

Event triggered when the level sequence player finishes naturally (without explicitly calling stop)

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnObjectSpawnedEvent`

```text
OnObjectSpawnedEvent(InObject: UObject*, InBindingID: const FGuid&, InSequenceID: FMovieSceneSequenceID) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObject` | `UObject*` | - |
| `InBindingID` | `const FGuid&` | - |
| `InSequenceID` | `FMovieSceneSequenceID` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
