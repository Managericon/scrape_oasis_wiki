---
id: "api:class:UInterpTrackAnimControl"
title: "UInterpTrackAnimControl"
source: "https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackAnimControl.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UInterpTrackAnimControl

## Inheritance

`UInterpTrackFloatBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SlotName` | `FName` | Name of slot to use when playing animation. Passed to Actor. <br>	 	When multiple tracks use the same slot name, they are each given a different ChannelIndex when SetAnimPosition is called. |
| `AnimSeqs` | `TArray < struct FAnimControlTrackKey >` | Track of different animations to play and when to start playing them. |
| `bSkipAnimNotifiers` | `uint32` | Skip all anim notifiers |

## Language

`cpp`
