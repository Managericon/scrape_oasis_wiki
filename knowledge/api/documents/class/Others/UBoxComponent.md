---
id: "api:class:UBoxComponent"
title: "UBoxComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBoxComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBoxComponent

A box generally used for simple collision. Bounds are rendered as lines in the editor.

## Inheritance

`UShapeComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoxExtent` | `FVector` | The extents (radii dimensions) of the box |
| `LineThickness` | `float` | Used to control the line thickness when rendering |

## Functions

### `SetBoxExtent`

```text
SetBoxExtent(InBoxExtent: FVector, bUpdateOverlaps: bool) -> void
```

Change the box extent size. This is the unscaled size, before component scale is applied.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBoxExtent` | `FVector` | - |
| `bUpdateOverlaps` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetScaledBoxExtent`

```text
GetScaledBoxExtent() -> FVector
```

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetUnscaledBoxExtent`

```text
GetUnscaledBoxExtent() -> FVector
```

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

## Language

`cpp`
