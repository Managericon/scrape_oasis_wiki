---
id: "api:cppstruct:FConstraint"
title: "FConstraint"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FConstraint.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FConstraint

Constraint Set up

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetBone` | `FBoneReference` | Target Bone this is constraint to |
| `OffsetOption` | `EConstraintOffsetOption` | Maintain offset based on refpose or not.<br>	  <br>	  None - no offset<br>	  Offset_RefPose - offset is created based on reference pose<br>	  <br>	  In the future, we'd like to support custom offset, not just based on ref pose |
| `TransformType` | `ETransformConstraintType` | What transform type is constraint to - Translation, Rotation, Scale OR Parent. Parent overrides all component |
| `PerAxis` | `FFilterOptionPerAxis` | Per axis filter options - applied in their local space not in world space |
