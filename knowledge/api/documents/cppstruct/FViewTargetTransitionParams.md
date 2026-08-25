---
id: "api:cppstruct:FViewTargetTransitionParams"
title: "FViewTargetTransitionParams"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FViewTargetTransitionParams.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FViewTargetTransitionParams

A set of parameters to describe how to transition between view targets.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BlendTime` | `float` | Total duration of blend to pending view target. 0 means no blending. |
| `BlendFunction` | `TEnumAsByte < enum EViewTargetBlendFunction >` | Function to apply to the blend parameter. |
| `BlendExp` | `float` | Exponent, used by certain blend functions to control the shape of the curve. |
| `bLockOutgoing` | `uint32` | If true, lock outgoing viewtarget to last frame's camera POV for the remainder of the blend.<br>	  This is useful if you plan to teleport the old viewtarget, but don't want to affect the blend. |
| `bLockLocation` | `uint32` | - |
