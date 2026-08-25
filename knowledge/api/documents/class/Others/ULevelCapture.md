---
id: "api:class:ULevelCapture"
title: "ULevelCapture"
source: "https://developer.gp.qq.com/api/class/detail/Others/ULevelCapture.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ULevelCapture

## Inheritance

`UMovieSceneCapture`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bAutoStartCapture` | `bool` | Specifies whether the capture should start immediately, or whether it will be invoked externally (through StartMovieCaptureStopMovieCapture exec commands) |
| `PrerequisiteActorId` | `FGuid` | Copy of the ID from PrerequisiteActor. Required because JSON serialization exports the path of the object, rather that its GUID |

## Language

`cpp`
