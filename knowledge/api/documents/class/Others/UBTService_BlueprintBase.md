---
id: "api:class:UBTService_BlueprintBase"
title: "UBTService_BlueprintBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTService_BlueprintBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTService_BlueprintBase

Base class for blueprint based service nodes. Do NOT use it for creating native c++ classes!
 
   When service receives Deactivation event, all latent actions associated this instance are being removed.
   This prevents from resuming activity started by Activation, but does not handle external events.
   Please use them safely (unregister at abort) and call IsServiceActive() when in doubt.

## Inheritance

`UBTService`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AIOwner` | `AAIController *` | Cached AIController owner of BehaviorTreeComponent. |
| `ActorOwner` | `AActor *` | Cached actor owner of BehaviorTreeComponent. |
| `bShowPropertyDetails` | `uint32` | show detailed information about properties |
| `bShowEventDetails` | `uint32` | show detailed information about implemented events |

## Functions

### `ReceiveTick`

```text
ReceiveTick(OwnerActor: AActor *, DeltaSeconds: float) -> void
```

tick function

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |
| `DeltaSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveSearchStart`

```text
ReceiveSearchStart(OwnerActor: AActor *) -> void
```

task search enters branch of tree

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveActivation`

```text
ReceiveActivation(OwnerActor: AActor *) -> void
```

service became active

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveDeactivation`

```text
ReceiveDeactivation(OwnerActor: AActor *) -> void
```

service became inactive

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveTickAI`

```text
ReceiveTickAI(OwnerController: AAIController *, ControlledPawn: APawn *, DeltaSeconds: float) -> void
```

Alternative AI version of ReceiveTick function.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |
| `DeltaSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveSearchStartAI`

```text
ReceiveSearchStartAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

Alternative AI version of ReceiveSearchStart function.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveActivationAI`

```text
ReceiveActivationAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

Alternative AI version of ReceiveActivation function.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveDeactivationAI`

```text
ReceiveDeactivationAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

Alternative AI version of ReceiveDeactivation function.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsServiceActive`

```text
IsServiceActive() -> bool
```

check if service is currently being active

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`
