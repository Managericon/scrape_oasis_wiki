---
id: "api:class:UVectorFieldComponent"
title: "UVectorFieldComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UVectorFieldComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UVectorFieldComponent

A Component referencing a vector field.

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VectorField` | `UVectorField *` | The vector field asset. |
| `Intensity` | `float` | The intensity at which the vector field is applied. |
| `Tightness` | `float` | How tightly particles follow the vector field. |
| `bPreviewVectorField` | `uint32` | If true, the vector field is only used for preview visualizations. |

## Functions

### `SetIntensity`

```text
SetIntensity(NewIntensity: float) -> void
```

Set the intensity of the vector field.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewIntensity` | `float` | - The new intensity of the vector field. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
