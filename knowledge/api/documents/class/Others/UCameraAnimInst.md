---
id: "api:class:UCameraAnimInst"
title: "UCameraAnimInst"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCameraAnimInst.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UCameraAnimInst

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CamAnim` | `UCameraAnim *` | which CameraAnim this is an instance of |
| `InterpGroupInst` | `UInterpGroupInst *` | the UInterpGroupInst used to do the interpolation |
| `PlayRate` | `float` | Multiplier for playback rate.  1.0 = normal. |
| `MoveTrack` | `UInterpTrackMove *` | cached movement track from the currently playing anim so we don't have to go find it every frame |
| `MoveInst` | `UInterpTrackInstMove *` | - |
| `PlaySpace` | `TEnumAsByte < ECameraAnimPlaySpace :: Type >` | - |

## Functions

### `SetCurrentTime`

```text
SetCurrentTime(NewTime: float) -> void
```

Jumps he camera anim to the given (unscaled) time.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Stop`

```text
Stop(bImmediate: bool) -> void
```

Stops this instance playing whatever animation it is playing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bImmediate` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDuration`

```text
SetDuration(NewDuration: float) -> void
```

Changes the running duration of this active anim, while maintaining playback position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewDuration` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetScale`

```text
SetScale(NewDuration: float) -> void
```

Changes the scale of the animation while playing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewDuration` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
