---
id: "api:class:UAnimSequenceBase"
title: "UAnimSequenceBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAnimSequenceBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAnimSequenceBase

## Inheritance

`UAnimationAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Notifies` | `TArray < FAnimNotifyEvent >` | Animation notifies, sorted by time (earliest notification first). |
| `SequenceLength` | `float` | Length (in seconds) of this AnimSequence if played back with a speed of 1.0. |
| `RateScale` | `float` | Number for tweaking playback rate of this animation globally. |
| `bEnableExcludeNotifiesWhenPlayAsMontage` | `bool` | - |
| `RawCurveData` | `FRawCurveTracks` | Raw uncompressed float curve data |

## Functions

### `GetPlayLength`

```text
GetPlayLength() -> ENGINE_API virtual float
```

Returns the total play length of the montage, if played back with a speed of 1.0.

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API virtual float` | - |

## Language

`cpp`
