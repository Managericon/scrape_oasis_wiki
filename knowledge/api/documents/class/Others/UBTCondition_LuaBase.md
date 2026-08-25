---
id: "api:class:UBTCondition_LuaBase"
title: "UBTCondition_LuaBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTCondition_LuaBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTCondition_LuaBase

Base class for lua based condition nodes. Do NOT use it for creating native c++ classes!
 
   Unlike task and attachments, condition have two execution chains:
    ExecutionStart-ExecutionFinish and ObserverActivated-ObserverDeactivated
   which makes automatic latent action cleanup impossible. Keep in mind, that
   you HAVE TO verify is given chain is still active after resuming from any
   latent action (like Delay, Timelines, etc).
 
   Helper functions:
   - IsConditionExecutionActive (true after ExecutionStart, until ExecutionFinish)
   - IsConditionObserverActive (true after ObserverActivated, until ObserverDeactivated)

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AIOwner` | `AAIController *` | Cached AIController owner of BehaviorTreeComponent. |
| `ObservedKeyNames` | `TArray < FName >` | blackboard key names that should be observed |
| `bCheckConditionOnlyBlackBoardChanges` | `uint32` | Applies only if Condition has any FBlackboardKeySelector property and if condition is<br>	 	set to abort BT flow. Is set to true ReceiveConditionCheck will be called only on changes<br>	  	to observed BB keys. If false or no BB keys observed ReceiveConditionCheck will be called every tick |
| `bIsObservingBB` | `uint32` | gets set to true if condition declared BB keys it can potentially observe |

## Functions

### `ReceiveTickAI`

```text
ReceiveTickAI(OwnerController: AAIController *, ControlledPawn: APawn *, DeltaSeconds: float) -> void
```

tick function

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

called on execution of underlying node

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

called when execution of underlying node is finished

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

called when observer is activated (flow controller)

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

called when observer is deactivated (flow controller)

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

called when testing if underlying node can be executed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsConditionExecutionActive`

```text
IsConditionExecutionActive() -> bool
```

check if condition is part of currently active branch

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsConditionObserverActive`

```text
IsConditionObserverActive() -> bool
```

check if condition's observer is currently active

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`
