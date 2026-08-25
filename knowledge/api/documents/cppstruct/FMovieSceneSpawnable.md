---
id: "api:cppstruct:FMovieSceneSpawnable"
title: "FMovieSceneSpawnable"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSpawnable.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FMovieSceneSpawnable

MovieSceneSpawnable describes an object that can be spawned for this MovieScene

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Guid` | `FGuid` | Unique identifier of the spawnable object. |
| `Name` | `FString` | Name label |
| `ObjectTemplate` | `UObject *` | - |
| `ChildPossessables` | `TArray < FGuid >` | Set of GUIDs to possessable object bindings that are bound to an object inside this spawnable |
| `Ownership` | `ESpawnOwnership` | Property indicating where ownership responsibility for this object lies |
| `GeneratedClass_DEPRECATED` | `UClass *` | Deprecated generated class |
