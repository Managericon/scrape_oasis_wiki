---
id: "api:class:UParticleModuleAttractorParticle"
title: "UParticleModuleAttractorParticle"
source: "https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleAttractorParticle.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UParticleModuleAttractorParticle

## Inheritance

`UParticleModuleAttractorBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EmitterName` | `FName` | The source emitter for attractors |
| `Range` | `FRawDistributionFloat` | The radial range of the attraction around the source particle.<br>	 	Particle-life relative. |
| `bStrengthByDistance` | `uint32` | The strength curve is a function of distance or of time. |
| `Strength` | `FRawDistributionFloat` | The strength of the attraction (negative values repel).<br>	 	Particle-life relative if StrengthByDistance is false. |
| `bAffectBaseVelocity` | `uint32` | If true, the velocity adjustment will be applied to the base velocity. |
| `SelectionMethod` | `TEnumAsByte < enum EAttractorParticleSelectionMethod >` | The method to use when selecting an attractor target particle from the emitter.<br>	 	One of the following:<br>	 	Random		- Randomly select a particle from the source emitter.  <br>	 	Sequential  - Select a particle using a sequential order. |
| `bRenewSource` | `uint32` | Whether the particle should grab a new particle if it's source expires. |
| `bInheritSourceVel` | `uint32` | Whether the particle should inherit the source veloctiy if it expires. |
| `LastSelIndex` | `int32` | - |

## Language

`cpp`
