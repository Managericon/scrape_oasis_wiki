---
id: "api:class:UMultiBillBoardComponent"
title: "UMultiBillBoardComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMultiBillBoardComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMultiBillBoardComponent

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Elements` | `TArray < FBillBoardMaterialSpriteElement >` | Current array of material billboard elements |
| `BillboardDatas` | `TArray < FBillboardData >` | - |

## Functions

### `GetElements`

```text
GetElements() -> const TArray < FBillBoardMaterialSpriteElement > &
```

**Returns**

| Type | Description |
|---|---|
| `const TArray < FBillBoardMaterialSpriteElement > &` | - |

### `SetElements`

```text
SetElements(NewElements: TArray < FBillBoardMaterialSpriteElement > &) -> void
```

Set all elements of this material billboard component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewElements` | `TArray < FBillBoardMaterialSpriteElement > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddElement`

```text
AddElement(Material: UMaterialInterface *, DistanceToOpacityCurve: UCurveFloat *, bSizeIsInScreenSpace: bool, BaseSizeX: float, BaseSizeY: float, DistanceToSizeCurve: UCurveFloat *) -> void
```

Adds an element to the sprite.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Material` | `UMaterialInterface *` | - |
| `DistanceToOpacityCurve` | `UCurveFloat *` | - |
| `bSizeIsInScreenSpace` | `bool` | - |
| `BaseSizeX` | `float` | - |
| `BaseSizeY` | `float` | - |
| `DistanceToSizeCurve` | `UCurveFloat *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddBillBoard`

```text
K2_AddBillBoard(NewLocation: FVector, UV0: FVector2D, UV1: FVector2D) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector` | - |
| `UV0` | `FVector2D` | - |
| `UV1` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `RemoveBillboard`

```text
RemoveBillboard(ID: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ID` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearAllBillBoards`

```text
ClearAllBillBoards() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBillboardUV`

```text
SetBillboardUV(ID: int32, UV0: FVector2D, UV1: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ID` | `int32` | - |
| `UV0` | `FVector2D` | - |
| `UV1` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CreateMultiBillboardComponent`

```text
CreateMultiBillboardComponent(WorldContextObject: UObject *, MultiBillboardClass: TSubclassOf < UMultiBillBoardComponent >) -> UMultiBillBoardComponent *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `MultiBillboardClass` | `TSubclassOf < UMultiBillBoardComponent >` | - |

**Returns**

| Type | Description |
|---|---|
| `UMultiBillBoardComponent *` | - |

## Language

`cpp`
