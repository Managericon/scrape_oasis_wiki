---
id: "api:cppstruct:FPhysicalAnimationData"
title: "FPhysicalAnimationData"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FPhysicalAnimationData.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FPhysicalAnimationData

Stores info on the type of motor that will be used for a given bone

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BodyName` | `FName` | The body we will be driving. We specifically hide this from users since they provide the body name and bodies below in the component API. |
| `bIsLocalSimulation` | `uint8` | Whether the drive targets are in world space or local |
| `OrientationStrength` | `float` | The strength used to correct orientation error |
| `AngularVelocityStrength` | `float` | The strength used to correct angular velocity error |
| `PositionStrength` | `float` | The strength used to correct linear position error. Only used for non-local simulation |
| `VelocityStrength` | `float` | The strength used to correct linear velocity error. Only used for non-local simulation |
| `MaxLinearForce` | `float` | The max force used to correct linear errors |
| `MaxAngularForce` | `float` | The max force used to correct angular errors |
