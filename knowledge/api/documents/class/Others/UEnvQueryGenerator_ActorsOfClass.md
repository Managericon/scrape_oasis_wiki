---
id: "api:class:UEnvQueryGenerator_ActorsOfClass"
title: "UEnvQueryGenerator_ActorsOfClass"
source: "https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_ActorsOfClass.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UEnvQueryGenerator_ActorsOfClass

## Inheritance

`UEnvQueryGenerator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SearchedActorClass` | `TSubclassOf < AActor >` | - |
| `GenerateOnlyActorsInRadius` | `FAIDataProviderBoolValue` | If true, this will only returns actors of the specified class within the SearchRadius of the SearchCenter context.  If false, it will return ALL actors of the specified class in the world. |
| `SearchRadius` | `FAIDataProviderFloatValue` | Max distance of path between point and context.  NOTE: Zero and negative values will never return any results if<br>	   UseRadius is true.  "Within" requires Distance < Radius.  Actors ON the circle (Distance == Radius) are excluded. |
| `SearchCenter` | `TSubclassOf < UEnvQueryContext >` | context |

## Language

`cpp`
