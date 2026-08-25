---
id: "api:class:UPaperTileMap"
title: "UPaperTileMap"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPaperTileMap.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPaperTileMap

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MapWidth` | `int32` | - |
| `MapHeight` | `int32` | - |
| `TileWidth` | `int32` | - |
| `TileHeight` | `int32` | - |
| `PixelsPerUnrealUnit` | `float` | - |
| `SeparationPerTileX` | `float` | - |
| `SeparationPerTileY` | `float` | - |
| `SeparationPerLayer` | `float` | - |
| `SelectedTileSet` | `TSoftObjectPtr < UPaperTileSet >` | - |
| `Material` | `UMaterialInterface *` | - |
| `TileLayers` | `TArray < UPaperTileLayer * >` | - |
| `CollisionThickness` | `float` | - |
| `SpriteCollisionDomain` | `TEnumAsByte < ESpriteCollisionMode :: Type >` | - |
| `ProjectionMode` | `TEnumAsByte < ETileMapProjectionMode :: Type >` | - |
| `HexSideLength` | `int32` | - |
| `BodySetup` | `UBodySetup *` | - |
| `LayerNameIndex` | `int32` | The naming index to start at when trying to create a new layer |

## Language

`cpp`
