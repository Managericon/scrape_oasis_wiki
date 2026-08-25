---
id: "api:class:USphereComponent"
title: "USphereComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/USphereComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# USphereComponent

A sphere generally used for simple collision. Bounds are rendered as lines in the editor.

## Inheritance

`UShapeComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SphereRadius` | `float` | The radius of the sphere |

## Functions

### `SetSphereRadius`

```text
SetSphereRadius(InSphereRadius: float, bUpdateOverlaps: bool) -> void
```

Change the sphere radius. This is the unscaled radius, before component scale is applied.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSphereRadius` | `float` | - |
| `bUpdateOverlaps` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetScaledSphereRadius`

```text
GetScaledSphereRadius() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetUnscaledSphereRadius`

```text
GetUnscaledSphereRadius() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetShapeScale`

```text
GetShapeScale() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

## Language

`cpp`
