---
id: "api:class:UAITask_MoveTo"
title: "UAITask_MoveTo"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAITask_MoveTo.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAITask_MoveTo

## Inheritance

`UAITask`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OnRequestFailed` | `FGenericGameplayTaskDelegate` | - |
| `MoveRequest` | `FAIMoveRequest` | parameters of move request |

## Functions

### `AIMoveTo`

```text
AIMoveTo(Controller: AAIController *, GoalLocation: FVector, GoalActor: AActor *, AcceptanceRadius: float, StopOnOverlap: EAIOptionFlag :: Type, AcceptPartialPath: EAIOptionFlag :: Type, bUsePathfinding: bool, bLockAILogic: bool, bUseContinuosGoalTracking: bool) -> UAITask_MoveTo *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Controller` | `AAIController *` | - |
| `GoalLocation` | `FVector` | - |
| `GoalActor` | `AActor *` | - |
| `AcceptanceRadius` | `float` | - |
| `StopOnOverlap` | `EAIOptionFlag :: Type` | - |
| `AcceptPartialPath` | `EAIOptionFlag :: Type` | - |
| `bUsePathfinding` | `bool` | - |
| `bLockAILogic` | `bool` | - |
| `bUseContinuosGoalTracking` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `UAITask_MoveTo *` | - |

## Delegates

### `OnMoveFinished`

```text
OnMoveFinished(Result: TEnumAsByte<EPathFollowingResult::Type>, AIController: AAIController*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Result` | `TEnumAsByte` | - |
| `AIController` | `AAIController*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
