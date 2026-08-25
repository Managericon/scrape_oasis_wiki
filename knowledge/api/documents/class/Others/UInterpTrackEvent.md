---
id: "api:class:UInterpTrackEvent"
title: "UInterpTrackEvent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackEvent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UInterpTrackEvent

## Inheritance

`UInterpTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EventTrack` | `TArray < struct FEventTrackKey >` | Array of events to fire off. |
| `bFireEventsWhenForwards` | `uint32` | If events should be fired when passed playing the sequence forwards. |
| `bFireEventsWhenBackwards` | `uint32` | If events should be fired when passed playing the sequence backwards. |
| `bFireEventsWhenJumpingForwards` | `uint32` | If true, events on this track are fired even when jumping forwads through a sequence - for example, skipping a cinematic. |
| `bUseCustomEventName` | `uint32` | If checked each key's event name is the exact name of the custom event function in level script that will be called |

## Language

`cpp`
