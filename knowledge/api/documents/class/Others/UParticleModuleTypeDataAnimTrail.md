---
id: "api:class:UParticleModuleTypeDataAnimTrail"
title: "UParticleModuleTypeDataAnimTrail"
source: "https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleTypeDataAnimTrail.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UParticleModuleTypeDataAnimTrail

## Inheritance

`UParticleModuleTypeDataBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bDeadTrailsOnDeactivate` | `uint32` | If true, when the system is deactivated, mark trails as dead.<br>	 	This means they will still render, but will not have more particles<br>	 	added to them, even if the system re-activates... |
| `bEnablePreviousTangentRecalculation` | `uint32` | If true, recalculate the previous tangent when a new particle is spawned |
| `bTangentRecalculationEveryFrame` | `uint32` | If true, recalculate tangents every frame to allow velocityacceleration to be applied |
| `TilingDistance` | `float` | The (estimated) covered distance to tile the 2nd UV set at.<br>	 	If 0.0, a second UV set will not be passed in. |
| `DistanceTessellationStepSize` | `float` | The distance step size for tessellation.<br>	 	# Tessellation Points = TruncToInt((Distance Between Spawned Particles)  DistanceTessellationStepSize)). If 0 then there is no distance tessellation. |
| `TangentTessellationStepSize` | `float` | The tangent scalar for tessellation.<br>	 	This is the degree change in the tangent direction [0...180] required to warrant an additional tessellation point. If 0 then there is no tangent tessellation. |
| `WidthTessellationStepSize` | `float` | The width step size for tessellation.<br>	 	This is the number of world units change in the width required to warrant an additional tessellation point. If 0 then there is no width tessellation. |

## Language

`cpp`
