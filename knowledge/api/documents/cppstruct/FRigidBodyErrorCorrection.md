---
id: "api:cppstruct:FRigidBodyErrorCorrection"
title: "FRigidBodyErrorCorrection"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FRigidBodyErrorCorrection.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FRigidBodyErrorCorrection

Rigid body error correction data

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LinearDeltaThresholdSq` | `float` | max squared position difference to perform velocity adjustment |
| `LinearInterpAlpha` | `float` | strength of snapping to desired linear velocity |
| `LinearRecipFixTime` | `float` | inverted duration after which linear velocity adjustment will fix error |
| `AngularDeltaThreshold` | `float` | max squared angle difference (in radians) to perform velocity adjustment |
| `AngularInterpAlpha` | `float` | strength of snapping to desired angular velocity |
| `BodySpeedThresholdSq` | `float` | min squared body speed to perform velocity adjustment |
| `AngularRecipFixTime` | `float` | inverted duration after which angular velocity adjustment will fix error |
