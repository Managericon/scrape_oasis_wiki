---
id: "api:class:UPawnActionsComponent"
title: "UPawnActionsComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPawnActionsComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPawnActionsComponent

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ControlledPawn` | `APawn *` | - |
| `ActionStacks` | `TArray < FPawnActionStack >` | - |
| `ActionEvents` | `TArray < FPawnActionEvent >` | - |
| `CurrentAction` | `UPawnAction *` | - |

## Functions

### `K2_PerformAction`

```text
K2_PerformAction(Pawn: APawn *, Action: UPawnAction *, Priority: TEnumAsByte < EAIRequestPriority :: Type >) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Pawn` | `APawn *` | - |
| `Action` | `UPawnAction *` | - |
| `Priority` | `TEnumAsByte < EAIRequestPriority :: Type >` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `K2_PushAction`

```text
K2_PushAction(NewAction: UPawnAction *, Priority: EAIRequestPriority :: Type, Instigator: UObject *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAction` | `UPawnAction *` | - |
| `Priority` | `EAIRequestPriority :: Type` | - |
| `Instigator` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `K2_AbortAction`

```text
K2_AbortAction(ActionToAbort: UPawnAction *) -> EPawnActionAbortState :: Type
```

Aborts given action instance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActionToAbort` | `UPawnAction *` | - |

**Returns**

| Type | Description |
|---|---|
| `EPawnActionAbortState :: Type` | - |

### `K2_ForceAbortAction`

```text
K2_ForceAbortAction(ActionToAbort: UPawnAction *) -> EPawnActionAbortState :: Type
```

Aborts given action instance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActionToAbort` | `UPawnAction *` | - |

**Returns**

| Type | Description |
|---|---|
| `EPawnActionAbortState :: Type` | - |

## Language

`cpp`
