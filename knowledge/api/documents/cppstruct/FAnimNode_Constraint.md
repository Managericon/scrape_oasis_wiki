---
id: "api:cppstruct:FAnimNode_Constraint"
title: "FAnimNode_Constraint"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_Constraint.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_Constraint

Constraint node to parent or world transform for rotationtranslation

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneToModify` | `FBoneReference` | Name of bone to control. This is the main bone chain to modify from. |
| `ConstraintSetup` | `TArray < FConstraint >` | List of constraints |
| `ConstraintWeights` | `TArray < float >` | Weight data - post edit syncs up to ConstraintSetups |
