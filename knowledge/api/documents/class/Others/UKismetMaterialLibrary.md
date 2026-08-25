---
id: "api:class:UKismetMaterialLibrary"
title: "UKismetMaterialLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UKismetMaterialLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UKismetMaterialLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `SetScalarParameterValue`

```text
SetScalarParameterValue(WorldContextObject: UObject *, Collection: UMaterialParameterCollection *, ParameterName: FName, ParameterValue: float) -> ENGINE_API void
```

Sets a scalar parameter value on the material collection instance. Logs if ParameterName is invalid.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Collection` | `UMaterialParameterCollection *` | - |
| `ParameterName` | `FName` | - |
| `ParameterValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetVectorParameterValue`

```text
SetVectorParameterValue(WorldContextObject: UObject *, Collection: UMaterialParameterCollection *, ParameterName: FName, ParameterValue: FLinearColor &) -> ENGINE_API void
```

Sets a vector parameter value on the material collection instance. Logs if ParameterName is invalid.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Collection` | `UMaterialParameterCollection *` | - |
| `ParameterName` | `FName` | - |
| `ParameterValue` | `FLinearColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GetScalarParameterValue`

```text
GetScalarParameterValue(WorldContextObject: UObject *, Collection: UMaterialParameterCollection *, ParameterName: FName) -> ENGINE_API float
```

Gets a scalar parameter value from the material collection instance. Logs if ParameterName is invalid.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Collection` | `UMaterialParameterCollection *` | - |
| `ParameterName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API float` | - |

### `GetVectorParameterValue`

```text
GetVectorParameterValue(WorldContextObject: UObject *, Collection: UMaterialParameterCollection *, ParameterName: FName) -> ENGINE_API FLinearColor
```

Gets a vector parameter value from the material collection instance. Logs if ParameterName is invalid.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Collection` | `UMaterialParameterCollection *` | - |
| `ParameterName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FLinearColor` | - |

### `CreateDynamicMaterialInstance`

```text
CreateDynamicMaterialInstance(WorldContextObject: UObject *, Parent: UMaterialInterface *) -> ENGINE_API class UMaterialInstanceDynamic *
```

Creates a Dynamic Material Instance which you can modify during gameplay.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Parent` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API class UMaterialInstanceDynamic *` | - |

## Language

`cpp`
