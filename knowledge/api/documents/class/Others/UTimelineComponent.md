---
id: "api:class:UTimelineComponent"
title: "UTimelineComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UTimelineComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UTimelineComponent

TimelineComponent holds a series of events, floats, vectors or colors with associated keyframes.
  Events can be triggered at keyframes along the timeline. 
  Floats, vectors, and colors are interpolated between keyframes along the timeline.

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TheTimeline` | `FTimeline` | The actual timeline structure |
| `bIgnoreTimeDilation` | `uint32` | True if global time dilation should be ignored by this timeline, false otherwise. |

## Functions

### `Play`

```text
Play() -> ENGINE_API void
```

Start playback of timeline

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `PlayFromStart`

```text
PlayFromStart() -> ENGINE_API void
```

Start playback of timeline from the start

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `Reverse`

```text
Reverse() -> ENGINE_API void
```

Start playback of timeline in reverse

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `ReverseFromEnd`

```text
ReverseFromEnd() -> ENGINE_API void
```

Start playback of timeline in reverse from the end

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `Stop`

```text
Stop() -> ENGINE_API void
```

Stop playback of timeline

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `IsPlaying`

```text
IsPlaying() -> ENGINE_API bool
```

Get whether this timeline is playing or not.

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API bool` | - |

### `IsReversing`

```text
IsReversing() -> ENGINE_API bool
```

Get whether we are reversing or not

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API bool` | - |

### `SetPlaybackPosition`

```text
SetPlaybackPosition(NewPosition: float, bFireEvents: bool, bFireUpdate: bool) -> ENGINE_API void
```

Jump to a position in the timeline.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPosition` | `float` | - |
| `bFireEvents` | `bool` | If true, event functions that are between current position and new playback position will fire. |
| `bFireUpdate` | `bool` | If true, the update output exec will fire after setting the new playback position. |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GetPlaybackPosition`

```text
GetPlaybackPosition() -> ENGINE_API float
```

Get the current playback position of the Timeline

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API float` | - |

### `SetLooping`

```text
SetLooping(bNewLooping: bool) -> ENGINE_API void
```

true means we would loop, false means we should not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewLooping` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `IsLooping`

```text
IsLooping() -> ENGINE_API bool
```

Get whether we are looping or not

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API bool` | - |

### `SetPlayRate`

```text
SetPlayRate(NewRate: float) -> ENGINE_API void
```

Sets the new play rate for this timeline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRate` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GetPlayRate`

```text
GetPlayRate() -> ENGINE_API float
```

Get the current play rate for this timeline

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API float` | - |

### `SetNewTime`

```text
SetNewTime(NewTime: float) -> ENGINE_API void
```

Set the new playback position time to use

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GetTimelineLength`

```text
GetTimelineLength() -> ENGINE_API float
```

Get length of the timeline

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API float` | - |

### `SetTimelineLength`

```text
SetTimelineLength(NewLength: float) -> ENGINE_API void
```

Set length of the timeline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLength` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetTimelineLengthMode`

```text
SetTimelineLengthMode(NewLengthMode: ETimelineLengthMode) -> ENGINE_API void
```

Sets the length mode of the timeline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLengthMode` | `ETimelineLengthMode` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetIgnoreTimeDilation`

```text
SetIgnoreTimeDilation(bNewIgnoreTimeDilation: bool) -> ENGINE_API void
```

Set whether to ignore time dilation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewIgnoreTimeDilation` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GetIgnoreTimeDilation`

```text
GetIgnoreTimeDilation() -> ENGINE_API bool
```

Get whether to ignore time dilation.

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API bool` | - |

### `SetFloatCurve`

```text
SetFloatCurve(NewFloatCurve: UCurveFloat *, FloatTrackName: FName) -> ENGINE_API void
```

Update a certain float track's curve

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewFloatCurve` | `UCurveFloat *` | - |
| `FloatTrackName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetVectorCurve`

```text
SetVectorCurve(NewVectorCurve: UCurveVector *, VectorTrackName: FName) -> ENGINE_API void
```

Update a certain vector track's curve

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewVectorCurve` | `UCurveVector *` | - |
| `VectorTrackName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetLinearColorCurve`

```text
SetLinearColorCurve(NewLinearColorCurve: UCurveLinearColor *, LinearColorTrackName: FName) -> ENGINE_API void
```

Update a certain linear color track's curve

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLinearColorCurve` | `UCurveLinearColor *` | - |
| `LinearColorTrackName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `OnRep_Timeline`

```text
OnRep_Timeline() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
