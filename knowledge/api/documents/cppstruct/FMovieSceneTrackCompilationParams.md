---
id: "api:cppstruct:FMovieSceneTrackCompilationParams"
title: "FMovieSceneTrackCompilationParams"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneTrackCompilationParams.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FMovieSceneTrackCompilationParams

Movie scene compilation parameters. Serialized items contribute to a compiled template's cached hash

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bForEditorPreview` | `bool` | Whether we're generating for an editor preview, or for efficient runtime evaluation |
| `bDuringBlueprintCompile` | `bool` | Whether we're generating during a blueprint compile. As such, UObject types may not have been fully loaded. |
