---
id: "api:cppstruct:FConeConstraint"
title: "FConeConstraint"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FConeConstraint.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FConeConstraint

Cone constraint

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Swing1LimitDegrees` | `float` | Angle of movement along the XY plane. This defines the first symmetric angle of the cone. |
| `Swing2LimitDegrees` | `float` | Angle of movement along the XZ plane. This defines the second symmetric angle of the cone. |
| `Swing1Motion` | `TEnumAsByte < enum EAngularConstraintMotion >` | Indicates whether the Swing1 limit is used. |
| `Swing2Motion` | `TEnumAsByte < enum EAngularConstraintMotion >` | Indicates whether the Swing2 limit is used. |
