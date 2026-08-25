---
id: "api:class:UEnvQueryTest_Pathfinding"
title: "UEnvQueryTest_Pathfinding"
source: "https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryTest_Pathfinding.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UEnvQueryTest_Pathfinding

## Inheritance

`UEnvQueryTest`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TestMode` | `TEnumAsByte < EEnvTestPathfinding :: Type >` | testing mode |
| `Context` | `TSubclassOf < UEnvQueryContext >` | context: other end of pathfinding test |
| `PathFromContext` | `FAIDataProviderBoolValue` | pathfinding direction |
| `SkipUnreachable` | `FAIDataProviderBoolValue` | if set, items with failed path will be invalidated (PathCost, PathLength) |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | navigation filter to use in pathfinding |

## Language

`cpp`
