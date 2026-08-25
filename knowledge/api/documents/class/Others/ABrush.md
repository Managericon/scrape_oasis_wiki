---
id: "api:class:ABrush"
title: "ABrush"
source: "https://developer.gp.qq.com/api/class/detail/Others/ABrush.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ABrush

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BrushType` | `TEnumAsByte < enum EBrushType >` | Type of brush |
| `BrushColor` | `FColor` | - |
| `PolyFlags` | `int32` | - |
| `bColored` | `uint32` | - |
| `bSolidWhenSelected` | `uint32` | - |
| `bPlaceableFromClassBrowser` | `uint32` | If true, this brush class can be placed using the class browser like other simple class types |
| `bNotForClientOrServer` | `uint32` | If true, this brush is a builder or otherwise does not need to be loaded into the game |
| `Brush` | `UModel *` | - |
| `BrushComponent` | `UBrushComponent *` | - |
| `bInManipulation` | `uint32` | Flag set when we are in a manipulation (scaling, translation, brush builder param change etc.) |
| `SavedSelections` | `TArray < struct FGeomSelection >` | Stores selection information from geometry mode.  This is the only information that we can't<br>	  regenerate by looking at the source brushes following an undo operation. |

## Language

`cpp`
