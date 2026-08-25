---
id: "api:class:UBTFunctionLibrary"
title: "UBTFunctionLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTFunctionLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTFunctionLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `GetOwnersBlackboard`

```text
GetOwnersBlackboard(NodeOwner: UBTNode *) -> UBlackboardComponent *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |

**Returns**

| Type | Description |
|---|---|
| `UBlackboardComponent *` | - |

### `GetOwnerComponent`

```text
GetOwnerComponent(NodeOwner: UBTNode *) -> UBehaviorTreeComponent *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |

**Returns**

| Type | Description |
|---|---|
| `UBehaviorTreeComponent *` | - |

### `GetBlackboardValueAsObject`

```text
GetBlackboardValueAsObject(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> UObject *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

### `GetBlackboardValueAsActor`

```text
GetBlackboardValueAsActor(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> AActor *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `GetBlackboardValueAsClass`

```text
GetBlackboardValueAsClass(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> UClass *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `UClass *` | - |

### `GetBlackboardValueAsEnum`

```text
GetBlackboardValueAsEnum(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> uint8
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `uint8` | - |

### `GetBlackboardValueAsInt`

```text
GetBlackboardValueAsInt(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetBlackboardValueAsFloat`

```text
GetBlackboardValueAsFloat(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetBlackboardValueAsBool`

```text
GetBlackboardValueAsBool(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetBlackboardValueAsString`

```text
GetBlackboardValueAsString(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetBlackboardValueAsName`

```text
GetBlackboardValueAsName(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> FName
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `GetBlackboardValueAsVector`

```text
GetBlackboardValueAsVector(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetBlackboardValueAsRotator`

```text
GetBlackboardValueAsRotator(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> FRotator
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `SetBlackboardValueAsObject`

```text
SetBlackboardValueAsObject(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: UObject *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlackboardValueAsClass`

```text
SetBlackboardValueAsClass(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: UClass *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `UClass *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlackboardValueAsEnum`

```text
SetBlackboardValueAsEnum(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: uint8) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlackboardValueAsInt`

```text
SetBlackboardValueAsInt(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlackboardValueAsFloat`

```text
SetBlackboardValueAsFloat(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlackboardValueAsBool`

```text
SetBlackboardValueAsBool(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlackboardValueAsString`

```text
SetBlackboardValueAsString(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: FString) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlackboardValueAsName`

```text
SetBlackboardValueAsName(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlackboardValueAsVector`

```text
SetBlackboardValueAsVector(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearBlackboardValueAsVector`

```text
ClearBlackboardValueAsVector(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> void
```

(DEPRECATED) Use ClearBlackboardValue instead

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlackboardValueAsRotator`

```text
SetBlackboardValueAsRotator(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &, Value: FRotator) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |
| `Value` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearBlackboardValue`

```text
ClearBlackboardValue(NodeOwner: UBTNode *, Key: FBlackboardKeySelector &) -> void
```

Resets indicated value to "not set" value, based on values type

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `Key` | `FBlackboardKeySelector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StartUsingExternalEvent`

```text
StartUsingExternalEvent(NodeOwner: UBTNode *, OwningActor: AActor *) -> void
```

Initialize variables marked as "instance memory" and set owning actor for blackboard operations

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |
| `OwningActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopUsingExternalEvent`

```text
StopUsingExternalEvent(NodeOwner: UBTNode *) -> void
```

Save variables marked as "instance memory" and clear owning actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NodeOwner` | `UBTNode *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
