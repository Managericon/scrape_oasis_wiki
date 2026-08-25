---
id: "api:class:UGameplayTasksComponent"
title: "UGameplayTasksComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGameplayTasksComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGameplayTasksComponent

The core ActorComponent for interfacing with the GameplayAbilities System

## Inheritance

`UActorComponent` -> `IGameplayTaskOwnerInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SimulatedTasks` | `TArray < UGameplayTask * >` | Tasks that run on simulated proxies |
| `AutonomousTasks` | `TArray < UGameplayTask * >` | - |
| `TaskPriorityQueue` | `TArray < UGameplayTask * >` | - |
| `TickingTasks` | `TArray < UGameplayTask * >` | Array of currently active UGameplayTask that require ticking |
| `KnownTasks` | `TArray < UGameplayTask * >` | All known tasks (processed by this component) referenced for GC |

## Functions

### `OnRep_SimulatedTasks`

```text
OnRep_SimulatedTasks() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_AutonomousTasks`

```text
OnRep_AutonomousTasks() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_RunGameplayTask`

```text
K2_RunGameplayTask(TaskOwner: TScriptInterface < IGameplayTaskOwnerInterface >, Task: UGameplayTask *, Priority: uint8, AdditionalRequiredResources: TArray < TSubclassOf < UGameplayTaskResource > >, AdditionalClaimedResources: TArray < TSubclassOf < UGameplayTaskResource > >) -> EGameplayTaskRunResult
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskOwner` | `TScriptInterface < IGameplayTaskOwnerInterface >` | - |
| `Task` | `UGameplayTask *` | - |
| `Priority` | `uint8` | - |
| `AdditionalRequiredResources` | `TArray < TSubclassOf < UGameplayTaskResource > >` | - |
| `AdditionalClaimedResources` | `TArray < TSubclassOf < UGameplayTaskResource > >` | - |

**Returns**

| Type | Description |
|---|---|
| `EGameplayTaskRunResult` | - |

## Delegates

### `OnClaimedResourcesChange`

```text
OnClaimedResourcesChange(NewlyClaimed: FGameplayResourceSet, FreshlyReleased: FGameplayResourceSet) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewlyClaimed` | `FGameplayResourceSet` | - |
| `FreshlyReleased` | `FGameplayResourceSet` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
