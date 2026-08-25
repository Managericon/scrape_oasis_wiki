---
id: "api:class:UTileMapBlueprintLibrary"
title: "UTileMapBlueprintLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UTileMapBlueprintLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UTileMapBlueprintLibrary

A collection of utility methods for working with tile map components
 
  @see UPaperTileMap, UPaperTileMapComponent

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `GetTileUserData`

```text
GetTileUserData(Tile: FPaperTileInfo) -> FName
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Tile` | `FPaperTileInfo` | - |

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `GetTileTransform`

```text
GetTileTransform(Tile: FPaperTileInfo) -> FTransform
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Tile` | `FPaperTileInfo` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `BreakTile`

```text
BreakTile(Tile: FPaperTileInfo, TileIndex: int32 &, TileSet: UPaperTileSet * &, bFlipH: bool &, bFlipV: bool &, bFlipD: bool &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Tile` | `FPaperTileInfo` | - |
| `TileIndex` | `int32 &` | - |
| `TileSet` | `UPaperTileSet * &` | - |
| `bFlipH` | `bool &` | - |
| `bFlipV` | `bool &` | - |
| `bFlipD` | `bool &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MakeTile`

```text
MakeTile(TileIndex: int32, TileSet: UPaperTileSet *, bFlipH: bool, bFlipV: bool, bFlipD: bool) -> FPaperTileInfo
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TileIndex` | `int32` | - |
| `TileSet` | `UPaperTileSet *` | - |
| `bFlipH` | `bool` | - |
| `bFlipV` | `bool` | - |
| `bFlipD` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FPaperTileInfo` | - |

## Language

`cpp`
