---
id: "api:cppstruct:FBranchingPointMarker"
title: "FBranchingPointMarker"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FBranchingPointMarker.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FBranchingPointMarker

AnimNotifies marked as BranchingPoints will create these markers on their BeginEnd times.
	They create stopping points when the Montage is being ticked to dispatch events.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NotifyIndex` | `int32` | - |
| `TriggerTime` | `float` | - |
| `NotifyEventType` | `TEnumAsByte < EAnimNotifyEventType :: Type >` | - |
