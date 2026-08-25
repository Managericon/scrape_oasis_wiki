---
id: "api:class:UMovieScenePropertyTrack"
title: "UMovieScenePropertyTrack"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMovieScenePropertyTrack.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMovieScenePropertyTrack

Base class for tracks that animate an object property

## Inheritance

`UMovieSceneNameableTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PropertyName` | `FName` | Name of the property being changed |
| `PropertyPath` | `FString` | Path to the property from the source object being changed |
| `Sections` | `TArray < UMovieSceneSection * >` | All the sections in this list |

## Language

`cpp`
