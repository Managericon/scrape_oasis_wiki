---
id: "api:class:UParticleModuleSpawnBase"
title: "UParticleModuleSpawnBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleSpawnBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UParticleModuleSpawnBase

## Inheritance

`UParticleModule`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bProcessSpawnRate` | `uint32` | If true, the SpawnRate of the SpawnModule of the emitter will be processed.<br>	 	If mutliple Spawn modules are 'stacked' in an emitter, if ANY of them <br>	 	have this set to false, it will not process the SpawnModule SpawnRate. |
| `bProcessBurstList` | `uint32` | If true, the BurstList of the SpawnModule of the emitter will be processed.<br>	 	If mutliple Spawn modules are 'stacked' in an emitter, if ANY of them <br>	 	have this set to false, it will not process the SpawnModule BurstList. |

## Language

`cpp`
