---
id: "api:class:UProceduralFoliageSpawner"
title: "UProceduralFoliageSpawner"
source: "https://developer.gp.qq.com/api/class/detail/Others/UProceduralFoliageSpawner.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UProceduralFoliageSpawner

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RandomSeed` | `int32` | The seed used for generating the randomness of the simulation. |
| `TileSize` | `float` | Length of the tile (in cm) along one axis. The total area of the tile will be TileSizeTileSize. |
| `NumUniqueTiles` | `int32` | The number of unique tiles to generate. The final simulation is a procedurally determined combination of the various unique tiles. |
| `MinimumQuadTreeSize` | `float` | Minimum size of the quad tree used during the simulation. Reduce if too many instances are in splittable leaf quads (as warned in the log). |
| `FoliageTypes` | `TArray < FFoliageTypeObject >` | The types of foliage to procedurally spawn. |
| `bNeedsSimulation` | `bool` | - |

## Functions

### `Simulate`

```text
Simulate(NumSteps: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NumSteps` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
