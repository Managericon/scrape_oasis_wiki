---
id: "api:cppstruct:FCameraTrackingFocusSettings"
title: "FCameraTrackingFocusSettings"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FCameraTrackingFocusSettings.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FCameraTrackingFocusSettings

Settings to control tracking-focus mode.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActorToTrack` | `AActor *` | Focus distance will be tied to this actor's location. |
| `RelativeOffset` | `FVector` | Offset from actor position to track. Relative to actor if tracking an actor, relative to world otherwise. |
| `bDrawDebugTrackingFocusPoint` | `uint8` | True to draw a debug representation of the tracked position. |
