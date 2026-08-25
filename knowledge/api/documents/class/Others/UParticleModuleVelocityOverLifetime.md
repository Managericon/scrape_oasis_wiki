---
id: "api:class:UParticleModuleVelocityOverLifetime"
title: "UParticleModuleVelocityOverLifetime"
source: "https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleVelocityOverLifetime.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UParticleModuleVelocityOverLifetime

## Inheritance

`UParticleModuleVelocityBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VelOverLife` | `FRawDistributionVector` | The scaling  value applied to the velocity.<br>	 	Value is retrieved using the RelativeTime of the particle. |
| `Absolute` | `uint32` | If true, the velocity will be SET to the value from the above dist.<br>	 	If false, the velocity will be scaled by the above dist. |

## Language

`cpp`
