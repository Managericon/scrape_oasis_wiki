---
id: "api:class:UDefaultLevelSequenceInstanceData"
title: "UDefaultLevelSequenceInstanceData"
source: "https://developer.gp.qq.com/api/class/detail/Others/UDefaultLevelSequenceInstanceData.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UDefaultLevelSequenceInstanceData

Default instance data class that level sequences understand. Implements IMovieSceneTransformOrigin.

## Inheritance

`UObject` -> `IMovieSceneTransformOrigin`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TransformOriginActor` | `AActor *` | When set, this actor's world position will be used as the transform origin for all absolute transform sections |
| `TransformOrigin` | `FTransform` | Specifies a transform that offsets all absolute transform sections in this sequence. Will compound with attach tracks. Scale is ignored. Not applied to Relative or Additive sections. |
| `ShouldIgnoreScale` | `bool` | - |

## Language

`cpp`
