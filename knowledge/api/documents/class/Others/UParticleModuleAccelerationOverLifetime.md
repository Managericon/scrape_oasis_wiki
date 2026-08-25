---
id: "api:class:UParticleModuleAccelerationOverLifetime"
title: "UParticleModuleAccelerationOverLifetime"
source: "https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleAccelerationOverLifetime.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UParticleModuleAccelerationOverLifetime

## Inheritance

`UParticleModuleAccelerationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AccelOverLife` | `FRawDistributionVector` | The acceleration of the particle over its lifetime.<br>	 	Value is obtained using the RelativeTime of the partice.<br>	 	The current and base velocity values of the particle <br>	 	are then updated using the formula <br>	 		velocity += acceleration DeltaTime<br>	 	where DeltaTime is the time passed since the last frame. |

## Language

`cpp`
