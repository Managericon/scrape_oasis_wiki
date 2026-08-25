---
id: "api:class:UPaperFlipbookComponent"
title: "UPaperFlipbookComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPaperFlipbookComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPaperFlipbookComponent

## Inheritance

`UMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceFlipbook` | `UPaperFlipbook *` | Flipbook currently being played |
| `Material_DEPRECATED` | `UMaterialInterface *` | - |
| `PlayRate` | `float` | Current play rate of the flipbook |
| `bLooping` | `uint32` | Whether the flipbook should loop when it reaches the end, or stop |
| `bReversePlayback` | `uint32` | If playback should move the current position backwards instead of forwards |
| `bPlaying` | `uint32` | Are we currently playing (moving Position) |
| `AccumulatedTime` | `float` | Current position in the timeline |
| `CachedFrameIndex` | `int32` | Last frame index calculated |
| `SpriteColor` | `FLinearColor` | Vertex color to apply to the frames |
| `CachedBodySetup` | `UBodySetup *` | The cached body setup |

## Functions

### `SetFlipbook`

```text
SetFlipbook(NewFlipbook: UPaperFlipbook *) -> bool
```

Change the flipbook used by this instance (will reset the play time to 0 if it is a new flipbook).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewFlipbook` | `UPaperFlipbook *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetFlipbook`

```text
GetFlipbook() -> UPaperFlipbook *
```

Gets the flipbook used by this instance.

**Returns**

| Type | Description |
|---|---|
| `UPaperFlipbook *` | - |

### `SetSpriteColor`

```text
SetSpriteColor(NewColor: FLinearColor) -> void
```

Set color of the sprite

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Play`

```text
Play() -> void
```

Start playback of flipbook

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlayFromStart`

```text
PlayFromStart() -> void
```

Start playback of flipbook from the start

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Reverse`

```text
Reverse() -> void
```

Start playback of flipbook in reverse

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReverseFromEnd`

```text
ReverseFromEnd() -> void
```

Start playback of flipbook in reverse from the end

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Stop`

```text
Stop() -> void
```

Stop playback of flipbook

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsPlaying`

```text
IsPlaying() -> bool
```

Get whether this flipbook is playing or not.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsReversing`

```text
IsReversing() -> bool
```

Get whether we are reversing or not

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetPlaybackPositionInFrames`

```text
SetPlaybackPositionInFrames(NewFramePosition: int32, bFireEvents: bool) -> void
```

Jump to a position in the flipbook (expressed in frames). If bFireEvents is true, event functions will fire, otherwise they will not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewFramePosition` | `int32` | - |
| `bFireEvents` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPlaybackPositionInFrames`

```text
GetPlaybackPositionInFrames() -> int32
```

Get the current playback position (in frames) of the flipbook

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetPlaybackPosition`

```text
SetPlaybackPosition(NewPosition: float, bFireEvents: bool) -> void
```

Jump to a position in the flipbook (expressed in seconds). If bFireEvents is true, event functions will fire, otherwise they will not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPosition` | `float` | - |
| `bFireEvents` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPlaybackPosition`

```text
GetPlaybackPosition() -> float
```

Get the current playback position (in seconds) of the flipbook

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetLooping`

```text
SetLooping(bNewLooping: bool) -> void
```

true means we should loop, false means we should not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewLooping` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsLooping`

```text
IsLooping() -> bool
```

Get whether we are looping or not

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetPlayRate`

```text
SetPlayRate(NewRate: float) -> void
```

Sets the new play rate for this flipbook

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRate` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPlayRate`

```text
GetPlayRate() -> float
```

Get the current play rate for this flipbook

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetNewTime`

```text
SetNewTime(NewTime: float) -> void
```

Set the new playback position time to use

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetFlipbookLength`

```text
GetFlipbookLength() -> float
```

Get length of the flipbook (in seconds)

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetFlipbookLengthInFrames`

```text
GetFlipbookLengthInFrames() -> int32
```

Get length of the flipbook (in frames)

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetFlipbookFramerate`

```text
GetFlipbookFramerate() -> float
```

Get the nominal framerate that the flipbook will be played back at (ignoring PlayRate), in frames per second

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `OnRep_SourceFlipbook`

```text
OnRep_SourceFlipbook(OldFlipbook: UPaperFlipbook *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldFlipbook` | `UPaperFlipbook *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnFinishedPlaying`

```text
OnFinishedPlaying() -> void
```

Event called whenever a non-looping flipbook finishes playing (either reaching the beginning or the end, depending on the play direction)

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
