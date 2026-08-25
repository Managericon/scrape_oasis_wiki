---
id: "api:class:UMeshVertexPainterKismetLibrary"
title: "UMeshVertexPainterKismetLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMeshVertexPainterKismetLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMeshVertexPainterKismetLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `PaintVerticesSingleColor`

```text
PaintVerticesSingleColor(StaticMeshComponent: UStaticMeshComponent *, FillColor: FLinearColor &, bConvertToSRGB: bool) -> void
```

Paints vertex colors on a mesh component in a specified color.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StaticMeshComponent` | `UStaticMeshComponent *` | - |
| `FillColor` | `FLinearColor &` | - |
| `bConvertToSRGB` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PaintVerticesLerpAlongAxis`

```text
PaintVerticesLerpAlongAxis(StaticMeshComponent: UStaticMeshComponent *, StartColor: FLinearColor &, EndColor: FLinearColor &, Axis: EVertexPaintAxis, bConvertToSRGB: bool) -> void
```

Paints vertex colors on a mesh component lerping from the start to the end color along the specified axis.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StaticMeshComponent` | `UStaticMeshComponent *` | - |
| `StartColor` | `FLinearColor &` | - |
| `EndColor` | `FLinearColor &` | - |
| `Axis` | `EVertexPaintAxis` | - |
| `bConvertToSRGB` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemovePaintedVertices`

```text
RemovePaintedVertices(StaticMeshComponent: UStaticMeshComponent *) -> void
```

Removes vertex colors on a mesh component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StaticMeshComponent` | `UStaticMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
