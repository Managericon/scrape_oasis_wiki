---
id: "api:cppstruct:FAngularDriveConstraint"
title: "FAngularDriveConstraint"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAngularDriveConstraint.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAngularDriveConstraint

Angular Drive

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TwistDrive` | `FConstraintDrive` | Controls the twist (roll) constraint drive between current orientationvelocity and target orientationvelocity. This is available as long as the twist limit is set to free or limited. |
| `SwingDrive` | `FConstraintDrive` | Controls the cone constraint drive between current orientationvelocity and target orientationvelocity. This is available as long as there is at least one swing limit set to free or limited. |
| `SlerpDrive` | `FConstraintDrive` | Controls the SLERP (spherical lerp) drive between current orientationvelocity and target orientationvelocity. NOTE: This is only available when all three angular limits are either free or limited. Locking any angular limit will turn off the drive implicitly. |
| `OrientationTarget` | `FRotator` | Target orientation relative to the the body reference frame. |
| `AngularVelocityTarget` | `FVector` | Target angular velocity relative to the body reference frame. |
| `AngularDriveMode` | `TEnumAsByte < enum EAngularDriveMode :: Type >` | Whether motors use SLERP (spherical lerp) or decompose into a Swing motor (cone constraints) and Twist motor (roll constraints). NOTE: SLERP will NOT work if any of the angular constraints are locked. |
