---
id: "api:cppstruct:FEventTrackKey"
title: "FEventTrackKey"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FEventTrackKey.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FEventTrackKey

A track containing discrete events that are triggered as its played back. 
 	Events correspond to Outputs of the SeqAct_Interp in Kismet.
 	There is no PreviewUpdateTrack function for this type - events are not triggered in editor.
 
 Information for one event in the track.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Time` | `float` | - |
| `EventName` | `FName` | - |
