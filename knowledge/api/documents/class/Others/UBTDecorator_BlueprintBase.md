---
id: "api:class:UBTDecorator_BlueprintBase"
title: "UBTDecorator_BlueprintBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_BlueprintBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTDecorator_BlueprintBase

Base class for blueprint based decorator nodes. Do NOT use it for creating native c++ classes!
 
   Unlike task and services, decorator have two execution chains: 
    ExecutionStart-ExecutionFinish and ObserverActivated-ObserverDeactivated
   which makes automatic latent action cleanup impossible. Keep in mind, that
   you HAVE TO verify is given chain is still active after resuming from any
   latent action (like Delay, Timelines, etc).
 
   Helper functions:
   - IsDecoratorExecutionActive (true after ExecutionStart, until ExecutionFinish)
   - IsDecoratorObserverActive (true after ObserverActivated, until ObserverDeactivated)

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AIOwner` | `AAIController *` | Cached AIController owner of BehaviorTreeComponent. |
| `ActorOwner` | `AActor *` | Cached AIController owner of BehaviorTreeComponent. |
| `ObservedKeyNames` | `TArray < FName >` | blackboard key names that should be observed |
| `bShowPropertyDetails` | `uint32` | show detailed information about properties |
| `bCheckConditionOnlyBlackBoardChanges` | `uint32` | Applies only if Decorator has any FBlackboardKeySelector property and if decorator is <br>	 	set to abort BT flow. Is set to true ReceiveConditionCheck will be called only on changes <br>	  	to observed BB keys. If false or no BB keys observed ReceiveConditionCheck will be called every tick |
| `bIsObservingBB` | `uint32` | gets set to true if decorator declared BB keys it can potentially observe |

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

### `ReceiveExecutionStart`

```text
ReceiveExecutionStart(OwnerActor: AActor *) -> void
```

called on execution of underlying node

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveExecutionFinish`

```text
ReceiveExecutionFinish(OwnerActor: AActor *, NodeResult: EBTNodeResult :: Type) -> void
```

called when execution of underlying node is finished

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |
| `NodeResult` | `EBTNodeResult :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveObserverActivated`

```text
ReceiveObserverActivated(OwnerActor: AActor *) -> void
```

called when observer is activated (flow controller)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveObserverDeactivated`

```text
ReceiveObserverDeactivated(OwnerActor: AActor *) -> void
```

called when observer is deactivated (flow controller)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PerformConditionCheck`

```text
PerformConditionCheck(OwnerActor: AActor *) -> bool
```

called when testing if underlying node can be executed, must call FinishConditionCheck

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ReceiveTickAI`

```text
ReceiveTickAI(OwnerController: AAIController *, ControlledPawn: APawn *, DeltaSeconds: float) -> void
```

Alternative AI version of ReceiveTick

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

### `ReceiveExecutionStartAI`

```text
ReceiveExecutionStartAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

Alternative AI version of ReceiveExecutionStart

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveExecutionFinishAI`

```text
ReceiveExecutionFinishAI(OwnerController: AAIController *, ControlledPawn: APawn *, NodeResult: EBTNodeResult :: Type) -> void
```

Alternative AI version of ReceiveExecutionFinish

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |
| `NodeResult` | `EBTNodeResult :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveObserverActivatedAI`

```text
ReceiveObserverActivatedAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

Alternative AI version of ReceiveObserverActivated

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveObserverDeactivatedAI`

```text
ReceiveObserverDeactivatedAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

Alternative AI version of ReceiveObserverDeactivated

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PerformConditionCheckAI`

```text
PerformConditionCheckAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> bool
```

Alternative AI version of ReceiveConditionCheck

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsDecoratorExecutionActive`

```text
IsDecoratorExecutionActive() -> bool
```

check if decorator is part of currently active branch

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsDecoratorObserverActive`

```text
IsDecoratorObserverActive() -> bool
```

check if decorator's observer is currently active

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`
