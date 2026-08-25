---
id: "api:class:APainCausingVolume"
title: "APainCausingVolume"
source: "https://developer.gp.qq.com/api/class/detail/Others/APainCausingVolume.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# APainCausingVolume

Volume that causes damage over time to any Actor that overlaps its collision.

## Inheritance

`APhysicsVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bPainCausing` | `uint32` | Whether volume currently causes damage. |
| `DamagePerSec` | `float` | Damage done per second to actors in this volume when bPainCausing=true |
| `DamageType` | `TSubclassOf < UDamageType >` | Type of damage done |
| `PainInterval` | `float` | If pain causing, time between damage applications. |
| `bEntryPain` | `uint32` | if bPainCausing, cause pain when something enters the volume in addition to damage each second |
| `BACKUP_bPainCausing` | `uint32` | Checkpointed bPainCausing value |
| `DamageInstigator` | `AController *` | Controller that gets credit for any damage caused by this volume |

## Language

`cpp`
