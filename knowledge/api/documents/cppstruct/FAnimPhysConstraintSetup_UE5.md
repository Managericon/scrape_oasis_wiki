---
id: "api:cppstruct:FAnimPhysConstraintSetup_UE5"
title: "FAnimPhysConstraintSetup_UE5"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimPhysConstraintSetup_UE5.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimPhysConstraintSetup_UE5

Constraint setup struct, holds data required to build a physics constraint

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LinearXLimitType` | `AnimPhysLinearConstraintType_UE5` | Whether to limit the linear X axis |
| `LinearYLimitType` | `AnimPhysLinearConstraintType_UE5` | Whether to limit the linear Y axis |
| `LinearZLimitType` | `AnimPhysLinearConstraintType_UE5` | Whether to limit the linear Z axis |
| `LinearAxesMin` | `FVector` | Minimum linear movement per-axis (Set zero here and in the max limit to lock) |
| `LinearAxesMax` | `FVector` | Maximum linear movement per-axis (Set zero here and in the min limit to lock) |
| `AngularConstraintType` | `AnimPhysAngularConstraintType_UE5` | Method to use when constraining angular motion |
| `TwistAxis` | `AnimPhysTwistAxis` | Axis to consider for twist when constraining angular motion (forward axis) |
| `AngularTargetAxis` | `AnimPhysTwistAxis` | The axis in the simulation pose to align to the Angular Target.<br>	  This is typically the axis pointing along the bone.<br>	  Note: This is affected by the Angular Spring Constant. |
| `ConeAngle` | `float` | Angle to use when constraining using a cone |
| `AngularLimitsMin` | `FVector` | - |
| `AngularLimitsMax` | `FVector` | - |
| `AngularTarget` | `FVector` | The axis to align the angular spring constraint to in the animation pose.<br>	  This typically points down the bone - so values of (1.0, 0.0, 0.0) are common,<br>	  but you can pick other values to align the spring to a different direction.<br>	  Note: This is affected by the Angular Spring Constant. |
| `AngularXAngle_DEPRECATED` | `float` | X-axis limit for angular motion when using the "Angular" constraint type (Set to 0 to lock, or 180 to remain free) |
| `AngularYAngle_DEPRECATED` | `float` | Y-axis limit for angular motion when using the "Angular" constraint type (Set to 0 to lock, or 180 to remain free) |
| `AngularZAngle_DEPRECATED` | `float` | Z-axis limit for angular motion when using the "Angular" constraint type (Set to 0 to lock, or 180 to remain free) |
