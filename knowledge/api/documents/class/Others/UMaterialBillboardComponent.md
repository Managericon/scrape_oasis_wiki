---
id: "api:class:UMaterialBillboardComponent"
title: "UMaterialBillboardComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialBillboardComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialBillboardComponent

A 2d material that will be rendered always facing the camera.

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Elements` | `TArray < FMaterialSpriteElement >` | Current array of material billboard elements |

## Functions

### `SetElements`

```text
SetElements(NewElements: TArray < FMaterialSpriteElement > &) -> void
```

Set all elements of this material billboard component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewElements` | `TArray < FMaterialSpriteElement > &` | - |

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

## Language

`cpp`
