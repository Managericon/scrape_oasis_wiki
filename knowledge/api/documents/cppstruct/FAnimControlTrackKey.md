---
id: "api:cppstruct:FAnimControlTrackKey"
title: "FAnimControlTrackKey"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimControlTrackKey.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimControlTrackKey

Structure used for holding information for one animation played on the Anim Control track.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartTime` | `float` | Position in the Matinee sequence to start playing this animation. |
| `AnimSeq` | `UAnimSequence *` | Animation Sequence to play |
| `AnimStartOffset` | `float` | Time to start playing AnimSequence at. |
| `AnimEndOffset` | `float` | Time to end playing the AnimSequence at. |
| `AnimPlayRate` | `float` | Playback speed of this animation. |
| `bLooping` | `uint32` | Should this animation loop. |
| `bReverse` | `uint32` | Whether to play the animation in reverse or not. |
