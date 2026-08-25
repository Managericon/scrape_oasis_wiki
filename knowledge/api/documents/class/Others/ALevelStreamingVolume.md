---
id: "api:class:ALevelStreamingVolume"
title: "ALevelStreamingVolume"
source: "https://developer.gp.qq.com/api/class/detail/Others/ALevelStreamingVolume.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ALevelStreamingVolume

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StreamingLevelNames` | `TArray < FName >` | Levels names affected by this level streaming volume. |
| `bEditorPreVisOnly` | `uint32` | If true, this streaming volume should only be used for editor streaming level previs. |
| `bDisabled` | `uint32` | If true, this streaming volume is ignored by the streaming volume code.  Used to either<br>	  disable a level streaming volume without disassociating it from the level, or to toggle<br>	  the control of a level's streaming between Kismet and volume streaming. |
| `StreamingUsage` | `TEnumAsByte < enum EStreamingVolumeUsage >` | Determines what this volume is used for, e.g. whether to control loading, loading and visibility or just visibilty (blocking on load) |

## Language

`cpp`
