---
id: "api:class:UPaperTileMapComponent"
title: "UPaperTileMapComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPaperTileMapComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPaperTileMapComponent

A component that handles rendering and collision for a single instance of a UPaperTileMap asset.
 
  This component is created when you drag a tile map asset from the content browser into a Blueprint, or
  contained inside of the actor created when you drag one into the level.
 
  NOTE: This is an early access preview class.  While not considered production-ready, it is a step beyond
  'experimental' and is being provided as a preview of things to come:
   - We will try to provide forward-compatibility for content you create.
   - The classes may change significantly in the future.
   - The code is in an early state and may not meet the desired polish  quality bar.
   - There is probably no documentation or example content yet.
   - They will be promoted out of 'Early Access' when they are production ready.
 
  @see UPrimitiveComponent, UPaperTileMap

## Inheritance

`UMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MapWidth_DEPRECATED` | `int32` | - |
| `MapHeight_DEPRECATED` | `int32` | - |
| `TileWidth_DEPRECATED` | `int32` | - |
| `TileHeight_DEPRECATED` | `int32` | - |
| `DefaultLayerTileSet_DEPRECATED` | `UPaperTileSet *` | - |
| `Material_DEPRECATED` | `UMaterialInterface *` | - |
| `TileLayers_DEPRECATED` | `TArray < UPaperTileLayer * >` | - |
| `TileMapColor` | `FLinearColor` | - |
| `UseSingleLayerIndex` | `int32` | - |
| `bUseSingleLayer` | `bool` | - |
| `TileMap` | `UPaperTileMap *` | - |
| `bShowPerTileGridWhenSelected` | `bool` | - |
| `bShowPerLayerGridWhenSelected` | `bool` | - |
| `bShowOutlineWhenUnselected` | `bool` | - |

## Functions

### `CreateNewTileMap`

```text
CreateNewTileMap(MapWidth: int32, MapHeight: int32, TileWidth: int32, TileHeight: int32, PixelsPerUnrealUnit: float, bCreateLayer: bool) -> void
```

Creates a new tile map of the specified size, replacing the TileMap reference (or dropping the previous owned one)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MapWidth` | `int32` | Width of the map (in tiles) |
| `MapHeight` | `int32` | Height of the map (in tiles) |
| `TileWidth` | `int32` | Width of one tile (in pixels) |
| `TileHeight` | `int32` | Height of one tile (in pixels) |
| `PixelsPerUnrealUnit` | `float` | - |
| `bCreateLayer` | `bool` | Should an empty layer be created? |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OwnsTileMap`

```text
OwnsTileMap() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetTileMap`

```text
SetTileMap(NewTileMap: UPaperTileMap *) -> bool
```

Change the PaperTileMap used by this instance.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTileMap` | `UPaperTileMap *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetMapSize`

```text
GetMapSize(MapWidth: int32 &, MapHeight: int32 &, NumLayers: int32 &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MapWidth` | `int32 &` | - |
| `MapHeight` | `int32 &` | - |
| `NumLayers` | `int32 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTile`

```text
GetTile(X: int32, Y: int32, Layer: int32) -> FPaperTileInfo
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `X` | `int32` | - |
| `Y` | `int32` | - |
| `Layer` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FPaperTileInfo` | - |

### `SetTile`

```text
SetTile(X: int32, Y: int32, Layer: int32, NewValue: FPaperTileInfo) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `X` | `int32` | - |
| `Y` | `int32` | - |
| `Layer` | `int32` | - |
| `NewValue` | `FPaperTileInfo` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResizeMap`

```text
ResizeMap(NewWidthInTiles: int32, NewHeightInTiles: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewWidthInTiles` | `int32` | - |
| `NewHeightInTiles` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddNewLayer`

```text
AddNewLayer() -> UPaperTileLayer *
```

**Returns**

| Type | Description |
|---|---|
| `UPaperTileLayer *` | - |

### `GetTileMapColor`

```text
GetTileMapColor() -> FLinearColor
```

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `SetTileMapColor`

```text
SetTileMapColor(NewColor: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLayerColor`

```text
GetLayerColor(Layer: int32) -> FLinearColor
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Layer` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `SetLayerColor`

```text
SetLayerColor(NewColor: FLinearColor, Layer: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewColor` | `FLinearColor` | - |
| `Layer` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MakeTileMapEditable`

```text
MakeTileMapEditable() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTileCornerPosition`

```text
GetTileCornerPosition(TileX: int32, TileY: int32, LayerIndex: int32, bWorldSpace: bool) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TileX` | `int32` | - |
| `TileY` | `int32` | - |
| `LayerIndex` | `int32` | - |
| `bWorldSpace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTileCenterPosition`

```text
GetTileCenterPosition(TileX: int32, TileY: int32, LayerIndex: int32, bWorldSpace: bool) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TileX` | `int32` | - |
| `TileY` | `int32` | - |
| `LayerIndex` | `int32` | - |
| `bWorldSpace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTilePolygon`

```text
GetTilePolygon(TileX: int32, TileY: int32, Points: TArray < FVector > &, LayerIndex: int32, bWorldSpace: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TileX` | `int32` | - |
| `TileY` | `int32` | - |
| `Points` | `TArray < FVector > &` | - |
| `LayerIndex` | `int32` | - |
| `bWorldSpace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDefaultCollisionThickness`

```text
SetDefaultCollisionThickness(Thickness: float, bRebuildCollision: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Thickness` | `float` | - |
| `bRebuildCollision` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLayerCollision`

```text
SetLayerCollision(Layer: int32, bHasCollision: bool, bOverrideThickness: bool, CustomThickness: float, bOverrideOffset: bool, CustomOffset: float, bRebuildCollision: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Layer` | `int32` | - |
| `bHasCollision` | `bool` | - |
| `bOverrideThickness` | `bool` | - |
| `CustomThickness` | `float` | - |
| `bOverrideOffset` | `bool` | - |
| `CustomOffset` | `float` | - |
| `bRebuildCollision` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RebuildCollision`

```text
RebuildCollision() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
