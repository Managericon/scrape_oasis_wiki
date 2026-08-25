---
id: "api:class:UInterpTrackVisibility"
title: "UInterpTrackVisibility"
source: "https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackVisibility.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UInterpTrackVisibility

## Inheritance

`UInterpTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VisibilityTrack` | `TArray < struct FVisibilityTrackKey >` | Array of events to fire off. |
| `bFireEventsWhenForwards` | `uint32` | If events should be fired when passed playing the sequence forwards. |
| `bFireEventsWhenBackwards` | `uint32` | If events should be fired when passed playing the sequence backwards. |
| `bFireEventsWhenJumpingForwards` | `uint32` | If true, events on this track are fired even when jumping forwads through a sequence - for example, skipping a cinematic. |

## Language

`cpp`
