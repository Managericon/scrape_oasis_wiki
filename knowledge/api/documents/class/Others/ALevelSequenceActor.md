---
id: "api:class:ALevelSequenceActor"
title: "ALevelSequenceActor"
source: "https://developer.gp.qq.com/api/class/detail/Others/ALevelSequenceActor.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ALevelSequenceActor

Actor responsible for controlling a specific level sequence in the world.

## Inheritance

`AActor` -> `IMovieSceneBindingOwnerInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bAutoPlay` | `bool` | - |
| `PlaybackSettings` | `FMovieSceneSequencePlaybackSettings` | - |
| `SequencePlayer` | `ULevelSequencePlayer *` | - |
| `LevelSequence` | `FSoftObjectPath` | - |
| `TempLevelSequence` | `ULevelSequence *` | - |
| `AdditionalEventReceivers` | `TArray < AActor * >` | - |
| `BurnInOptions` | `ULevelSequenceBurnInOptions *` | - |
| `BindingOverrides` | `UMovieSceneBindingOverrides *` | Mapping of actors to override the sequence bindings with |
| `bReduceFrequency` | `bool` | - |
| `ReduceFrameCount` | `int32` | - |
| `IgnoreFrameTolerance` | `float` | - |
| `bOverrideInstanceData` | `uint8` | Enable specification of dynamic instance data to be supplied to the sequence during playback |
| `DefaultInstanceData` | `UObject *` | Instance data that can be used to dynamically control sequence evaluation at runtime |
| `BurnInInstance` | `ULevelSequenceBurnIn *` | Burn-in widget |
| `OwnCharacter` | `AActor *` | 所属玩家, feishen, 20210623 |

## Functions

### `GetSequence`

```text
GetSequence(bLoad: bool, bInitializePlayer: bool) -> ULevelSequence *
```

Get the level sequence being played by this actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bLoad` | `bool` | Whether to load the sequence object if it is not already in memory. |
| `bInitializePlayer` | `bool` | Whether to initialize the player when the sequence has been loaded. |

**Returns**

| Type | Description |
|---|---|
| `ULevelSequence *` | Level sequence, or nullptr if not assigned or if it cannot be loaded. |

### `SetSequence`

```text
SetSequence(InSequence: ULevelSequence *) -> void
```

Set the level sequence being played by this actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSequence` | `ULevelSequence *` | The sequence object to set. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetEventReceivers`

```text
SetEventReceivers(AdditionalReceivers: TArray < AActor * >) -> void
```

Set an array of additional actors that will receive events triggerd from this sequence actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AdditionalReceivers` | `TArray < AActor * >` | An array of actors to receive events |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBinding`

```text
SetBinding(Binding: FMovieSceneObjectBindingID, Actors: TArray < AActor * > &, bAllowBindingsFromAsset: bool) -> void
```

Overrides the specified binding with the specified actors, optionally still allowing the bindings defined in the Level Sequence asset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Binding` | `FMovieSceneObjectBindingID` | - |
| `Actors` | `TArray < AActor * > &` | - |
| `bAllowBindingsFromAsset` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddBinding`

```text
AddBinding(Binding: FMovieSceneObjectBindingID, Actor: AActor *, bAllowBindingsFromAsset: bool) -> void
```

Adds the specified actor to the overridden bindings for the specified binding ID, optionally still allowing the bindings defined in the Level Sequence asset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Binding` | `FMovieSceneObjectBindingID` | - |
| `Actor` | `AActor *` | - |
| `bAllowBindingsFromAsset` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveBinding`

```text
RemoveBinding(Binding: FMovieSceneObjectBindingID, Actor: AActor *) -> void
```

Removes the specified actor from the specified binding's actor array

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Binding` | `FMovieSceneObjectBindingID` | - |
| `Actor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetBinding`

```text
ResetBinding(Binding: FMovieSceneObjectBindingID) -> void
```

Resets the specified binding back to the defaults defined by the Level Sequence asset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Binding` | `FMovieSceneObjectBindingID` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetBindings`

```text
ResetBindings() -> void
```

Resets all overridden bindings back to the defaults defined by the Level Sequence asset

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGCAddBinding`

```text
UGCAddBinding(Actor: AActor *, TrackName: FString) -> FMovieSceneObjectBindingID
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |
| `TrackName` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `FMovieSceneObjectBindingID` | - |

### `UGCRemoveBinding`

```text
UGCRemoveBinding(Actor: AActor *, TrackName: FString) -> FMovieSceneObjectBindingID
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |
| `TrackName` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `FMovieSceneObjectBindingID` | - |

### `ReceiveInitailizePlayer`

```text
ReceiveInitailizePlayer() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOwnCharacter`

```text
SetOwnCharacter(Actor: AActor *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
