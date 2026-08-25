---
id: "api:cppstruct:FMovieSceneRootEvaluationTemplateInstance"
title: "FMovieSceneRootEvaluationTemplateInstance"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneRootEvaluationTemplateInstance.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FMovieSceneRootEvaluationTemplateInstance

Root evaluation template instance used to play back any sequence

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DirectorInstances` | `TMap < FMovieSceneSequenceID , UObject * >` | Map of director instances by sequence ID. Kept alive by this map assuming this struct is reference collected |
