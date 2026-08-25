---
id: "api:class:UBTAttachment_LuaBase"
title: "UBTAttachment_LuaBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTAttachment_LuaBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTAttachment_LuaBase

Base class for lua based Attachment nodes. Do NOT use it for creating native c++ classes!
 
   When Attachment receives Deactivation event, all latent actions associated this instance are being removed.
   This prevents from resuming activity started by Activation, but does not handle external events.
   Please use them safely (unregister at abort) and call IsAttachmentActive() when in doubt.

## Inheritance

`UBTService`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AIOwner` | `AAIController *` | Cached AIController owner of BehaviorTreeComponent. |

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

### `ReceiveSearchStartAI`

```text
ReceiveSearchStartAI(OwnerController: AAIController *, ControlledPawn: APawn *) -> void
```

task search enters branch of tree

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

attachment became active

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

attachment became inactive

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerController` | `AAIController *` | - |
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsAttachmentActive`

```text
IsAttachmentActive() -> bool
```

check if attachment is currently being active

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`
