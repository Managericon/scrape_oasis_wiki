---
id: "api:class:UBrainComponent"
title: "UBrainComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBrainComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBrainComponent

## Inheritance

`UActorComponent` -> `IAIResourceInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BlackboardComp` | `UBlackboardComponent *` | blackboard component |
| `AIOwner` | `AAIController *` | - |

## Functions

### `RestartLogic`

```text
RestartLogic() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopLogic`

```text
StopLogic(Reason: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reason` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PauseLogic`

```text
PauseLogic(Reason: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reason` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResumeLogic`

```text
ResumeLogic(Reason: FString &) -> EAILogicResuming :: Type
```

MUST be called by child implementations!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reason` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `EAILogicResuming :: Type` | indicates whether child class' ResumeLogic should be called (true) or has it been |

### `IsRunning`

```text
IsRunning() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsPaused`

```text
IsPaused() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`
