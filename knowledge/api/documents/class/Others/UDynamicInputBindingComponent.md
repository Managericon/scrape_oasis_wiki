---
id: "api:class:UDynamicInputBindingComponent"
title: "UDynamicInputBindingComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UDynamicInputBindingComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UDynamicInputBindingComponent

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActionBindingClusters` | `TArray < FActionBindingCluster >` | - |
| `AxisBindingClusters` | `TArray < FAxisBindingCluster >` | - |

## Functions

### `BindAction`

```text
BindAction(ActionName: FName &, ActorInputEvent: EActorInputEvent, FunctionName: FName &, bConsumeInput: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActionName` | `FName &` | - |
| `ActorInputEvent` | `EActorInputEvent` | - |
| `FunctionName` | `FName &` | - |
| `bConsumeInput` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BindAxis`

```text
BindAxis(AxisName: FName &, FunctionName: FName &, bConsumeInput: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AxisName` | `FName &` | - |
| `FunctionName` | `FName &` | - |
| `bConsumeInput` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveActionBinding`

```text
RemoveActionBinding(ActionName: FName &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActionName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveAxisBinding`

```text
RemoveAxisBinding(AxisName: FName &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AxisName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BindActionCluster`

```text
BindActionCluster(Index: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BindAxisCluster`

```text
BindAxisCluster(Index: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveActionClusterBinding`

```text
RemoveActionClusterBinding(Index: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveAxisClusterBinding`

```text
RemoveAxisClusterBinding(Index: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
