---
id: "api:class:UParticleModuleRotationOverLifetime"
title: "UParticleModuleRotationOverLifetime"
source: "https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleRotationOverLifetime.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UParticleModuleRotationOverLifetime

## Inheritance

`UParticleModuleRotationBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RotationOverLife` | `FRawDistributionFloat` | The rotation of the particle (1.0 = 360 degrees).<br>	 	The value is retrieved using the RelativeTime of the particle. |
| `Scale` | `uint32` | If true,  the particle rotation is multiplied by the value retrieved from RotationOverLife.<br>	 	If false, the particle rotation is incremented by the value retrieved from RotationOverLife. |

## Language

`cpp`
