---
id: "api:cppstruct:FMovieSceneBinding"
title: "FMovieSceneBinding"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneBinding.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FMovieSceneBinding

A set of tracks bound to runtime objects

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ObjectGuid` | `FGuid` | Object binding guid for runtime objects |
| `BindingName` | `FString` | Display name |
| `EditableDisplayName` | `FString` | EditTable Display name |
| `Tracks` | `TArray < UMovieSceneTrack * >` | All tracks in this binding |
