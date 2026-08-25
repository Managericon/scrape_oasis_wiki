---
id: "api:cppstruct:FInputAxisProperties"
title: "FInputAxisProperties"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FInputAxisProperties.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FInputAxisProperties

Configurable properties for control axes, used to transform raw input into game ready values.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DeadZone` | `float` | What the dead zone of the axis is.  For control axes such as analog sticks. |
| `Sensitivity` | `float` | Scaling factor to multiply raw value by. |
| `Exponent` | `float` | For applying curves to [0..1] axes, e.g. analog sticks |
| `bInvert` | `uint8` | Inverts reported values for this axis |
