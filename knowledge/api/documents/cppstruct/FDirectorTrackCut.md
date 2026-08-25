---
id: "api:cppstruct:FDirectorTrackCut"
title: "FDirectorTrackCut"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FDirectorTrackCut.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FDirectorTrackCut

A track type used for binding the view of a Player (attached to this tracks group) to the actor of a different group.
 
 
 Information for one cut in this track.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Time` | `float` | Time to perform the cut. |
| `TransitionTime` | `float` | Time taken to move view to new camera. |
| `TargetCamGroup` | `FName` | GroupName of UInterpGroup to cut viewpoint to. |
| `ShotNumber` | `int32` | Shot number for developer reference |
