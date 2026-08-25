---
id: "api:class:UParticleModuleKillHeight"
title: "UParticleModuleKillHeight"
source: "https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleKillHeight.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UParticleModuleKillHeight

## Inheritance

`UParticleModuleKillBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Height` | `FRawDistributionFloat` | The height at which to kill the particle. |
| `bAbsolute` | `uint32` | If true, the height should be treated as a world-space position. |
| `bFloor` | `uint32` | If true, the plane should be considered a floor - ie kill anything BELOW it.<br>	 	If false, if is a ceiling - ie kill anything ABOVE it. |
| `bApplyPSysScale` | `uint32` | If true, take the particle systems scale into account |

## Language

`cpp`
