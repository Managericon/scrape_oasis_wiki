---
id: "api:class:UBrushComponent"
title: "UBrushComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBrushComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBrushComponent

A brush component defines a shape that can be modified within the editor. They are used both as part of BSP building, and for volumes.

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Brush` | `UModel *` | - |
| `BrushBodySetup` | `UBodySetup *` | Description of collision |
| `PrePivot_DEPRECATED` | `FVector` | Local space translation |
| `MeshCollisionProvider` | `UStaticMesh *` | - |

## Functions

### `SetMeshCollisionProvider`

```text
SetMeshCollisionProvider(Mesh: UStaticMesh *) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Mesh` | `UStaticMesh *` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

## Language

`cpp`
