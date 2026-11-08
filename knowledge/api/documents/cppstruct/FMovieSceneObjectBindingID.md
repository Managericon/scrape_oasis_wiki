---
id: "api:cppstruct:FMovieSceneObjectBindingID"
title: "FMovieSceneObjectBindingID"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneObjectBindingID.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FMovieSceneObjectBindingID

Persistent identifier to a specific object binding within a sequence hierarchy.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SequenceID` | `int32` | Sequence ID stored as an int32 so that it can be used in the blueprint VM |
| `Space` | `EMovieSceneObjectBindingSpace` | The binding's resolution space |
| `Guid` | `FGuid` | Identifier for the object binding within the sequence |
| `ResolveParentIndex` | `int32` | Parent index to resolve the sequence ID from. 0 = local, N>0 = Nth parent, -1 = fixed to root. |
