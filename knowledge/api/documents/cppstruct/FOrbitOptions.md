---
id: "api:cppstruct:FOrbitOptions"
title: "FOrbitOptions"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FOrbitOptions.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FOrbitOptions

Container struct for holding options on the data updating for the module.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bProcessDuringSpawn` | `uint32` | Whether to process the data during spawning. |
| `bProcessDuringUpdate` | `uint32` | Whether to process the data during updating. |
| `bUseEmitterTime` | `uint32` | Whether to use emitter time during data retrieval. |
| `bUseParticleIDInsteadOfTime` | `uint32` | Whether to use particle ID instead of time (emitter time or particle time). |
| `ParticleIDLoop` | `uint32` | If >0, the distribution input will be ParticleID % ParticleIDLoop |
