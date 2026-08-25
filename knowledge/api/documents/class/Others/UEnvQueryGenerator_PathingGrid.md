---
id: "api:class:UEnvQueryGenerator_PathingGrid"
title: "UEnvQueryGenerator_PathingGrid"
source: "https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_PathingGrid.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UEnvQueryGenerator_PathingGrid

Navigation grid, generates points on navmesh
   with paths tofrom context no further than given limit

## Inheritance

`UEnvQueryGenerator_SimpleGrid`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PathToItem` | `FAIDataProviderBoolValue` | pathfinding direction |
| `NavigationFilter` | `TSubclassOf < UNavigationQueryFilter >` | navigation filter to use in pathfinding |
| `ScanRangeMultiplier` | `FAIDataProviderFloatValue` | multiplier for max distance between point and context |

## Language

`cpp`
