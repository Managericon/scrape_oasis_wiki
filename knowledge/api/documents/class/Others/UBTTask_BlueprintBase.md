---
id: "api:class:UBTTask_BlueprintBase"
title: "UBTTask_BlueprintBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTTask_BlueprintBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTTask_BlueprintBase

Base class for blueprint based task nodes. Do NOT use it for creating native c++ classes!
 
   When task receives Abort event, all latent actions associated this instance are being removed.
   This prevents from resuming activity started by Execute, but does not handle external events.
   Please use them safely (unregister at abort) and call IsTaskExecuting() when in doubt.

## Inheritance

`UBTTaskNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AIOwner` | `AAIController *` | Cached AIController owner of BehaviorTreeComponent. |
| `ActorOwner` | `AActor *` | Cached actor owner of BehaviorTreeComponent. |
| `bShowPropertyDetails` | `uint32` | show detailed information about properties |

## Functions

### `ReceiveExecute`

```text
ReceiveExecute(OwnerActor: AActor *) -> void
```

entry point, task will stay active until FinishExecute is called.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveAbort`

```text
ReceiveAbort(OwnerActor: AActor *) -> void
```

if blueprint graph contains this event, task will stay active until FinishAbort is called

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

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

### `ReceiveExecuteAI`

```text
ReceiveExecuteAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

Alternative AI version of ReceiveExecute

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveAbortAI`

```text
ReceiveAbortAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

Alternative AI version of ReceiveAbort

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveTickAI`

```text
ReceiveTickAI(OwnerController: AAIController *, ControlledPawn: APawn *, DeltaSeconds: float) -> void
```

Alternative AI version of tick function.

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

### `FinishExecute`

```text
FinishExecute(bSuccess: bool) -> void
```

finishes task execution with Success or Fail result

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bSuccess` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FinishAbort`

```text
FinishAbort() -> void
```

aborts task execution

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFinishOnMessage`

```text
SetFinishOnMessage(MessageName: FName) -> void
```

task execution will be finished (with result 'Success') after receiving specified message

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MessageName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFinishOnMessageWithId`

```text
SetFinishOnMessageWithId(MessageName: FName, RequestID: int32) -> void
```

task execution will be finished (with result 'Success') after receiving specified message with indicated ID

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MessageName` | `FName` | - |
| `RequestID` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsTaskExecuting`

```text
IsTaskExecuting() -> bool
```

check if task is currently being executed

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsTaskAborting`

```text
IsTaskAborting() -> bool
```

check if task is currently being aborted

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`
