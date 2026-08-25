---
id: "api:class:UMaterialInstanceDynamic"
title: "UMaterialInstanceDynamic"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialInstanceDynamic.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialInstanceDynamic

## Inheritance

`UMaterialInstance`

## Functions

### `SetScalarParameterValue`

```text
SetScalarParameterValue(ParameterName: FName, Value: float) -> void
```

Set a MID scalar (float) parameter value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_GetScalarParameterValue`

```text
K2_GetScalarParameterValue(ParameterName: FName) -> float
```

Get the current scalar (float) parameter value from an MID

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetTextureParameterValue`

```text
SetTextureParameterValue(ParameterName: FName, Value: UTexture *) -> void
```

Set an MID texture parameter value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Value` | `UTexture *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_GetTextureParameterValue`

```text
K2_GetTextureParameterValue(ParameterName: FName) -> UTexture *
```

Get the current MID texture parameter value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UTexture *` | - |

### `SetVectorParameterValue`

```text
SetVectorParameterValue(ParameterName: FName, Value: FLinearColor) -> void
```

Set an MID vector parameter value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Value` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_GetVectorParameterValue`

```text
K2_GetVectorParameterValue(ParameterName: FName) -> FLinearColor
```

Get the current MID vector parameter value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `K2_InterpolateMaterialInstanceParams`

```text
K2_InterpolateMaterialInstanceParams(SourceA: UMaterialInstance *, SourceB: UMaterialInstance *, Alpha: float) -> void
```

Interpolates the scalar and vector parameters of this material instance based on two other material instances, and an alpha blending factor
	  The output is the object itself (this).
	  Supports the case SourceA==this || SourceB==this
	  Both material have to be from the same base material

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceA` | `UMaterialInstance *` | value that is used for Alpha=0, silently ignores the case if 0 |
| `SourceB` | `UMaterialInstance *` | value that is used for Alpha=1, silently ignores the case if 0 |
| `Alpha` | `float` | usually in the range 0..1, values outside the range extrapolate |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_CopyMaterialInstanceParameters`

```text
K2_CopyMaterialInstanceParameters(Source: UMaterialInterface *) -> void
```

Copies over parameters given a material interface (copy each instance following the hierarchy)
	  Very slow implementation, avoid using at runtime. Hopefully we can replace ity later with something like CopyInterpParameters()
	  The output is the object itself (this).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Source` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CopyInterpParameters`

```text
CopyInterpParameters(Source: UMaterialInstance *) -> void
```

Copies over parameters given a material instance (only copy from the instance, not following the hierarchy)
	  much faster than K2_CopyMaterialInstanceParameters(),
	  The output is the object itself (this).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Source` | `UMaterialInstance *` | ignores the call if 0 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CopyParameterOverrides`

```text
CopyParameterOverrides(MaterialInstance: UMaterialInstance *) -> void
```

Copy parameter values from another material instance. This will copy only
	  parameters explicitly overridden in that material instance!!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MaterialInstance` | `UMaterialInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
