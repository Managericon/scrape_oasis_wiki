---
id: "api:class:UParticleModuleKillBox"
title: "UParticleModuleKillBox"
source: "https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleKillBox.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UParticleModuleKillBox

## Inheritance

`UParticleModuleKillBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LowerLeftCorner` | `FRawDistributionVector` | The lower left corner of the box. |
| `UpperRightCorner` | `FRawDistributionVector` | The upper right corner of the box. |
| `bAbsolute` | `uint32` | If true, the box coordinates are in world space. |
| `bKillInside` | `uint32` | If true, particles INSIDE the box will be killed. <br>	 	If false (the default), particles OUTSIDE the box will be killed. |
| `bAxisAlignedAndFixedSize` | `uint32` | If true, the box will always be axis aligned and non-scalable. |

## Language

`cpp`
