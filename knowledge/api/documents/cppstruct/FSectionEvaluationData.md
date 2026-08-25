---
id: "api:cppstruct:FSectionEvaluationData"
title: "FSectionEvaluationData"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FSectionEvaluationData.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FSectionEvaluationData

Evaluation data that specifies information about what to evaluate for a given template

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ImplIndex` | `int32` | The implementation index we should evaluate (index into FMovieSceneEvaluationTrack::ChildTemplates) |
| `ForcedTime` | `float` | A forced time to evaluate this section at |
| `Flags` | `ESectionEvaluationFlags` | Additional flags for evaluating this section |
