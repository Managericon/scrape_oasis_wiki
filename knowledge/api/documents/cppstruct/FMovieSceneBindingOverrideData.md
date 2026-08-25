---
id: "api:cppstruct:FMovieSceneBindingOverrideData"
title: "FMovieSceneBindingOverrideData"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneBindingOverrideData.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FMovieSceneBindingOverrideData

Movie scene binding override data

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ObjectBindingId` | `FMovieSceneObjectBindingID` | Specifies the object binding to override. |
| `Object` | `TWeakObjectPtr < UObject >` | Specifies the object to override the binding with. |
| `bOverridesDefault` | `bool` | Specifies whether the default assignment should remain bound (false) or if this should completely override the default binding (false). |
