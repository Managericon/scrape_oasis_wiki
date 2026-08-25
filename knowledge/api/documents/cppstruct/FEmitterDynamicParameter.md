---
id: "api:cppstruct:FEmitterDynamicParameter"
title: "FEmitterDynamicParameter"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FEmitterDynamicParameter.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FEmitterDynamicParameter

Helper structure for displaying the parameter.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParamName` | `FName` | The parameter name - from the material DynamicParameter expression. READ-ONLY |
| `bUseEmitterTime` | `uint32` | If true, use the EmitterTime to retrieve the value, otherwise use Particle RelativeTime. |
| `bSpawnTimeOnly` | `uint32` | If true, only set the value at spawn time of the particle, otherwise update each frame. |
| `ValueMethod` | `TEnumAsByte < enum EEmitterDynamicParameterValue >` | Where to get the parameter value from. |
| `bScaleVelocityByParamValue` | `uint32` | If true, scale the velocity value selected in ValueMethod by the evaluated ParamValue. |
| `ParamValue` | `FRawDistributionFloat` | The distriubtion for the parameter value. |
