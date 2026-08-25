---
id: "api:cppstruct:FAnimNode_Base"
title: "FAnimNode_Base"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_Base.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_Base

This is the base of all runtime animation nodes
 
  To create a new animation node:
    Create a struct derived from FAnimNode_Base - this is your runtime node
    Create a class derived from UAnimGraphNode_Base, containing an instance of your runtime node as a member - this is your visualeditor-only node

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NodeUID` | `int32` | - |
| `EvaluateGraphExposedInputs` | `FExposedValueHandler` | - |
| `bEnableAsyncInitNode` | `bool` | - |
| `bSkipAnimNodeEnabled` | `bool` | - |
| `SkipAnimNodeThresholdOverride` | `float` | - |
| `NodeTag` | `FName` | - |
