---
id: "api:cppstruct:FAnimNode_SequenceEvaluator"
title: "FAnimNode_SequenceEvaluator"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_SequenceEvaluator.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_SequenceEvaluator

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sequence` | `UAnimSequenceBase *` | - |
| `ExplicitTime` | `float` | - |
| `ExplicitTimeType` | `TEnumAsByte < ESequenceEvalTimeType :: Type >` | 输入时间类型： |
| `bShouldLoop` | `bool` | This only works if bTeleportToTargetTime is false OR this node is set to use SyncGroup |
| `bTeleportToExplicitTime` | `bool` | If true, teleport to explicit time, does NOT advance time (does not trigger notifies, does not extract Root Motion, etc.)<br>	Note: using a sync group forces advancing time regardless of what this option is set to. |
| `StartPosition` | `float` | - |
| `ReinitializationBehavior` | `TEnumAsByte < ESequenceEvalReinit :: Type >` | What to do when SequenceEvaluator is reinitialized |
| `bReinitialized` | `bool` | - |
| `CheckReTickFrameCounterSubValue` | `int32` | - |
| `bEnableTriggerNotify` | `bool` | - |
