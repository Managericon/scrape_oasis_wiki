---
id: "api:class:UParticleModuleVelocity"
title: "UParticleModuleVelocity"
source: "https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleVelocity.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UParticleModuleVelocity

## Inheritance

`UParticleModuleVelocityBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartVelocity` | `FRawDistributionVector` | The velocity to apply to a particle when it is spawned.<br>	 	Value is retrieved using the EmitterTime of the emitter. |
| `StartVelocityRadial` | `FRawDistributionFloat` | The velocity to apply to a particle along its radial direction.<br>	 	Direction is determined by subtracting the location of the emitter from the particle location at spawn.<br>	 	Value is retrieved using the EmitterTime of the emitter. |

## Language

`cpp`
