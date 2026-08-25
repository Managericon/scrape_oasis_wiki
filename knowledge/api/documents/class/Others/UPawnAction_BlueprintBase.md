---
id: "api:class:UPawnAction_BlueprintBase"
title: "UPawnAction_BlueprintBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPawnAction_BlueprintBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPawnAction_BlueprintBase

## Inheritance

`UPawnAction`

## Functions

### `ActionStart`

```text
ActionStart(ControlledPawn: APawn *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ActionTick`

```text
ActionTick(ControlledPawn: APawn *, DeltaSeconds: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ControlledPawn` | `APawn *` | - |
| `DeltaSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ActionPause`

```text
ActionPause(ControlledPawn: APawn *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ActionResume`

```text
ActionResume(ControlledPawn: APawn *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ControlledPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ActionFinished`

```text
ActionFinished(ControlledPawn: APawn *, WithResult: EPawnActionResult :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ControlledPawn` | `APawn *` | - |
| `WithResult` | `EPawnActionResult :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
