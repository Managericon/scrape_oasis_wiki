---
id: "api:cppstruct:FTViewTarget"
title: "FTViewTarget"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FTViewTarget.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FTViewTarget

A ViewTarget is the primary actor the camera is associated with.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Target` | `AActor *` | Target Actor used to compute POV |
| `POV` | `FMinimalViewInfo` | Computed point of view |
| `PlayerState` | `APlayerState *` | PlayerState (used to follow same player through pawn transitions, etc., when spectating) |
