---
id: "api:class:UEnvQueryGenerator_Cone"
title: "UEnvQueryGenerator_Cone"
source: "https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_Cone.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UEnvQueryGenerator_Cone

## Inheritance

`UEnvQueryGenerator_ProjectedPoints`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AlignedPointsDistance` | `FAIDataProviderFloatValue` | Distance between each point of the same angle |
| `ConeDegrees` | `FAIDataProviderFloatValue` | Maximum degrees of the generated cone |
| `AngleStep` | `FAIDataProviderFloatValue` | The step of the angle increase. Angle step must be >=1<br>	   Smaller values generate less items |
| `Range` | `FAIDataProviderFloatValue` | Generation distance |
| `CenterActor` | `TSubclassOf < UEnvQueryContext >` | The actor (or actors) that will generate a cone in their facing direction |
| `bIncludeContextLocation` | `uint8` | Whether to include CenterActors' locations when generating items. <br>	 	Note that this option skips the MinAngledPointsDistance parameter. |

## Language

`cpp`
