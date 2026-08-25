---
id: "api:class:ULevelSequence"
title: "ULevelSequence"
source: "https://developer.gp.qq.com/api/class/detail/Others/ULevelSequence.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ULevelSequence

Movie scene animation for Actors.

## Inheritance

`UMovieSceneSequence`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MovieScene` | `UMovieScene *` | Pointer to the movie scene that controls this animation. |
| `ObjectReferences` | `FLevelSequenceObjectReferenceMap` | Legacy object references - should be read-only. Not deprecated because they need to still be saved |
| `BindingReferences` | `FLevelSequenceBindingReferences` | References to bound objects. |
| `PossessedObjects_DEPRECATED` | `TMap < FString , FLevelSequenceObject >` | Deprecated property housing old possessed object bindings |
| `DirectorClass` | `UClass *` | The class that is used to spawn this level sequence's director instance.<br>	  Director instances are allocated on-demand one per sequence during evaluation and are used by event tracks for triggering events. |
| `DirectorBlueprint` | `UBlueprint *` | A pointer to the director blueprint that generates this sequence's DirectorClass. |

## Language

`cpp`
