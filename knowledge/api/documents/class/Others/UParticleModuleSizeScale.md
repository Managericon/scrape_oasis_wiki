---
id: "api:class:UParticleModuleSizeScale"
title: "UParticleModuleSizeScale"
source: "https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleSizeScale.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UParticleModuleSizeScale

## Inheritance

`UParticleModuleSizeBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SizeScale` | `FRawDistributionVector` | The amount the BaseSize should be scaled before being used as the size of the particle. <br>	 	The value is retrieved using the RelativeTime of the particle during its update.<br>	 	NOTE: this module overrides any size adjustments made prior to this module in that frame. |
| `EnableX` | `uint32` | Ignored |
| `EnableY` | `uint32` | Ignored |
| `EnableZ` | `uint32` | Ignored |

## Language

`cpp`
