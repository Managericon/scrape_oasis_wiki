---
id: "api:class:UInterpTrackParticleReplay"
title: "UInterpTrackParticleReplay"
source: "https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackParticleReplay.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UInterpTrackParticleReplay

## Inheritance

`UInterpTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TrackKeys` | `TArray < struct FParticleReplayTrackKey >` | Array of keys |
| `bIsCapturingReplay` | `uint32` | True in the editor if track should be used to capture replay frames instead of play them back |
| `FixedTimeStep` | `float` | Current replay fixed time quantum between frames (one over frame rate) |

## Language

`cpp`
