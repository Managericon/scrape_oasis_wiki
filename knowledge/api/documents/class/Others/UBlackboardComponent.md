---
id: "api:class:UBlackboardComponent"
title: "UBlackboardComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBlackboardComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBlackboardComponent

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BrainComp` | `UBrainComponent *` | cached behavior tree component |
| `BlackboardAsset` | `UBlackboardData *` | data asset defining entries |
| `KeyInstances` | `TArray < UBlackboardKeyType * >` | instanced keys with custom data allocations |

## Functions

### `GetValueAsObject`

```text
GetValueAsObject(KeyName: FName &) -> UObject *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

### `GetValueAsClass`

```text
GetValueAsClass(KeyName: FName &) -> UClass *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `UClass *` | - |

### `GetValueAsEnum`

```text
GetValueAsEnum(KeyName: FName &) -> uint8
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `uint8` | - |

### `GetValueAsInt`

```text
GetValueAsInt(KeyName: FName &) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetValueAsFloat`

```text
GetValueAsFloat(KeyName: FName &) -> float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetValueAsBool`

```text
GetValueAsBool(KeyName: FName &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetValueAsString`

```text
GetValueAsString(KeyName: FName &) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetValueAsName`

```text
GetValueAsName(KeyName: FName &) -> FName
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `GetValueAsVector`

```text
GetValueAsVector(KeyName: FName &) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetValueAsRotator`

```text
GetValueAsRotator(KeyName: FName &) -> FRotator
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `SetValueAsObject`

```text
SetValueAsObject(KeyName: FName &, ObjectValue: UObject *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `ObjectValue` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetValueAsClass`

```text
SetValueAsClass(KeyName: FName &, ClassValue: UClass *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `ClassValue` | `UClass *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetValueAsEnum`

```text
SetValueAsEnum(KeyName: FName &, EnumValue: uint8) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `EnumValue` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetValueAsInt`

```text
SetValueAsInt(KeyName: FName &, IntValue: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `IntValue` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetValueAsFloat`

```text
SetValueAsFloat(KeyName: FName &, FloatValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `FloatValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetValueAsBool`

```text
SetValueAsBool(KeyName: FName &, BoolValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `BoolValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetValueAsString`

```text
SetValueAsString(KeyName: FName &, StringValue: FString) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `StringValue` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetValueAsName`

```text
SetValueAsName(KeyName: FName &, NameValue: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `NameValue` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetValueAsVector`

```text
SetValueAsVector(KeyName: FName &, VectorValue: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `VectorValue` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetValueAsRotator`

```text
SetValueAsRotator(KeyName: FName &, VectorValue: FRotator) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `VectorValue` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsVectorValueSet`

```text
IsVectorValueSet(KeyName: FName &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetLocationFromEntry`

```text
GetLocationFromEntry(KeyName: FName &, ResultLocation: FVector &) -> bool
```

return false if call failed (most probably no such entry in BB)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `ResultLocation` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetRotationFromEntry`

```text
GetRotationFromEntry(KeyName: FName &, ResultRotation: FRotator &) -> bool
```

return false if call failed (most probably no such entry in BB)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |
| `ResultRotation` | `FRotator &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ClearValue`

```text
ClearValue(KeyName: FName &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
