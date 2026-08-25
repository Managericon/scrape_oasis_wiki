---
id: "api:class:UInterpTrackToggle"
title: "UInterpTrackToggle"
source: "https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackToggle.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UInterpTrackToggle

## Inheritance

`UInterpTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ToggleTrack` | `TArray < struct FToggleTrackKey >` | Array of events to fire off. |
| `bActivateSystemEachUpdate` | `uint32` | If true, the track will call ActivateSystem on the emitter each update (the old 'incorrect' behavior).<br>	 	If false (the default), the System will only be activated if it was previously inactive. |
| `bActivateWithJustAttachedFlag` | `uint32` | If true, the track will activate the system w the 'Just Attached' flag. |
| `bFireEventsWhenForwards` | `uint32` | If events should be fired when passed playing the sequence forwards. |
| `bFireEventsWhenBackwards` | `uint32` | If events should be fired when passed playing the sequence backwards. |
| `bFireEventsWhenJumpingForwards` | `uint32` | If true, events on this track are fired even when jumping forwads through a sequence - for example, skipping a cinematic. |

## Language

`cpp`
