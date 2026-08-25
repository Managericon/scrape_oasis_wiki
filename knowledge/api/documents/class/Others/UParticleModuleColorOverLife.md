---
id: "api:class:UParticleModuleColorOverLife"
title: "UParticleModuleColorOverLife"
source: "https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleColorOverLife.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UParticleModuleColorOverLife

## Inheritance

`UParticleModuleColorBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ColorOverLife` | `FRawDistributionVector` | The color to apply to the particle, as a function of the particle RelativeTime. |
| `AlphaOverLife` | `FRawDistributionFloat` | The alpha to apply to the particle, as a function of the particle RelativeTime. |
| `ColorOverLifeHDR` | `FRawDistributionVector` | Initial color for a particle as a function of Emitter time. |
| `AlphaOverLifeHDR` | `FRawDistributionFloat` | Initial alpha for a particle as a function of Emitter time. |
| `bClampAlpha` | `uint32` | If true, the alpha value will be clamped to the [0..1] range. |

## Language

`cpp`
