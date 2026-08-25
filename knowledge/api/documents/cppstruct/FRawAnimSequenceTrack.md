---
id: "api:cppstruct:FRawAnimSequenceTrack"
title: "FRawAnimSequenceTrack"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FRawAnimSequenceTrack.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FRawAnimSequenceTrack

Raw keyframe data for one track.  Each array will contain either NumFrames elements or 1 element.
  One element is used as a simple compression scheme where if all keys are the same, they'll be
  reduced to 1 key that is constant over the entire sequence.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PosKeys` | `TArray < FVector >` | Position keys. |
| `RotKeys` | `TArray < FQuat >` | Rotation keys. |
| `ScaleKeys` | `TArray < FVector >` | Scale keys. |
