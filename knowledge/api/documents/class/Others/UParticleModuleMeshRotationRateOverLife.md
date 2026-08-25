---
id: "api:class:UParticleModuleMeshRotationRateOverLife"
title: "UParticleModuleMeshRotationRateOverLife"
source: "https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleMeshRotationRateOverLife.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UParticleModuleMeshRotationRateOverLife

## Inheritance

`UParticleModuleRotationRateBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RotRate` | `FRawDistributionVector` | The rotation rate desired.<br>	 	The value is retrieved using the RelativeTime of the particle. |
| `bScaleRotRate` | `uint32` | If true, scale the current rotation rate by the value retrieved.<br>	 	Otherwise, set the rotation rate to the value retrieved. |

## Language

`cpp`
