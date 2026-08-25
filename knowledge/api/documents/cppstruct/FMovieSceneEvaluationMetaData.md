---
id: "api:cppstruct:FMovieSceneEvaluationMetaData"
title: "FMovieSceneEvaluationMetaData"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvaluationMetaData.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FMovieSceneEvaluationMetaData

Informational meta-data that applies to a given time range

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActiveSequences` | `TArray < FMovieSceneSequenceID >` | Array of sequences that are active in this time range. |
| `ActiveEntities` | `TArray < FMovieSceneOrderedEvaluationKey >` | Array of entities (tracks andor sections) that are active in this time range. |
