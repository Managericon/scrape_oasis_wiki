---
id: "api:cppstruct:FAnimNode_TransitionPoseEvaluator"
title: "FAnimNode_TransitionPoseEvaluator"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_TransitionPoseEvaluator.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_TransitionPoseEvaluator

Animation data node for state machine transitions.
  Can be set to supply either the animation data from the transition source (From State) or the transition destination (To State).

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DataSource` | `TEnumAsByte < EEvaluatorDataSource :: Type >` | - |
| `EvaluatorMode` | `TEnumAsByte < EEvaluatorMode :: Mode >` | - |
| `FramesToCachePose` | `int32` | - |
| `CacheFramesRemaining` | `int32` | - |
