---
id: "api:class:UParticleModuleAcceleration"
title: "UParticleModuleAcceleration"
source: "https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleAcceleration.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UParticleModuleAcceleration

## Inheritance

`UParticleModuleAccelerationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Acceleration` | `FRawDistributionVector` | The initial acceleration of the particle.<br>	 	Value is obtained using the EmitterTime at particle spawn.<br>	 	Each frame, the current and base velocity of the particle <br>	 	is then updated using the formula <br>	 		velocity += acceleration  DeltaTime<br>	 	where DeltaTime is the time passed since the last frame. |
| `bApplyOwnerScale` | `uint32` | If true, then apply the particle system components scale <br>	 	to the acceleration value. |

## Language

`cpp`
