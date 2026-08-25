---
id: "api:cppstruct:FRBFParams"
title: "FRBFParams"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FRBFParams.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FRBFParams

Parameters used by RBF solver

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetDimensions` | `int32` | How many dimensions input data has |
| `Radius` | `float` | Default radius for each target, scaled by per-Target ScaleFactor |
| `Function` | `ERBFFunctionType` | - |
| `DistanceMethod` | `ERBFDistanceMethod` | - |
| `TwistAxis` | `TEnumAsByte < EBoneAxis >` | Axis to use when DistanceMethod is SwingAngle |
| `WeightThreshold` | `float` | Weight below which we shouldn't bother returning a contribution from a target |
