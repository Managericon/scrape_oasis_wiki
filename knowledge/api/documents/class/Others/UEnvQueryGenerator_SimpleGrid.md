---
id: "api:class:UEnvQueryGenerator_SimpleGrid"
title: "UEnvQueryGenerator_SimpleGrid"
source: "https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_SimpleGrid.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UEnvQueryGenerator_SimpleGrid

Simple grid, generates points in 2D square around context

## Inheritance

`UEnvQueryGenerator_ProjectedPoints`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GridSize` | `FAIDataProviderFloatValue` | half of square's extent, like a radius |
| `SpaceBetween` | `FAIDataProviderFloatValue` | generation density |
| `GenerateAround` | `TSubclassOf < UEnvQueryContext >` | context |

## Language

`cpp`
