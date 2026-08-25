---
id: "api:class:UInterpTrackDirector"
title: "UInterpTrackDirector"
source: "https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackDirector.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UInterpTrackDirector

## Inheritance

`UInterpTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CutTrack` | `TArray < struct FDirectorTrackCut >` | Array of cuts between cameras. |
| `bSimulateCameraCutsOnClients` | `uint32` | True to allow clients to simulate their own camera cuts.  Can help with latency-induced timing issues. |
| `PreviewCamera` | `ACameraActor *` | The camera actor which the track is currently focused on. Only valid if this track or it's group is selected |

## Language

`cpp`
