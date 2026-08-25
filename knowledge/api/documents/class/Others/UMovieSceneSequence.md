---
id: "api:class:UMovieSceneSequence"
title: "UMovieSceneSequence"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSequence.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMovieSceneSequence

Abstract base class for movie scene animations (C++ version).

## Inheritance

`UMovieSceneSignedObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EvaluationTemplate` | `FCachedMovieSceneEvaluationTemplate` | - |
| `TemplateParameters` | `FMovieSceneTrackCompilationParams` | - |
| `InstancedSubSequenceEvaluationTemplates` | `TMap < UObject * , FCachedMovieSceneEvaluationTemplate >` | - |
| `bParentContextsAreSignificant` | `bool` | true if the result of GetParentObject is significant in object resolution for LocateBoundObjects.<br>	  When true, if GetParentObject returns nullptr, the PlaybackContext will be used for LocateBoundObjects, other wise the object's parent will be used<br>	  When false, the PlaybackContext will always be used for LocateBoundObjects |

## Language

`cpp`
