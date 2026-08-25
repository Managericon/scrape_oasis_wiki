---
id: "api:class:ADefaultPawn"
title: "ADefaultPawn"
source: "https://developer.gp.qq.com/api/class/detail/Others/ADefaultPawn.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ADefaultPawn

DefaultPawn implements a simple Pawn with spherical collision and built-in flying movement.
  @see UFloatingPawnMovement

## Inheritance

`APawn`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BaseTurnRate` | `float` | Base turn rate, in degsec. Other scaling may affect final turn rate. |
| `BaseLookUpRate` | `float` | Base lookup rate, in degsec. Other scaling may affect final lookup rate. |
| `MovementComponent` | `UPawnMovementComponent *` | DefaultPawn movement component |
| `CollisionComponent` | `USphereComponent *` | DefaultPawn collision component |
| `MeshComponent` | `UStaticMeshComponent *` | The mesh associated with this Pawn. |
| `bAddDefaultMovementBindings` | `uint32` | If true, adds default input bindings for movement and camera look. |

## Functions

### `MoveForward`

```text
MoveForward(Val: float) -> void
```

Input callback to move forward in local space (or backward if Val is negative).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Val` | `float` | Amount of movement in the forward direction (or backward if negative). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MoveRight`

```text
MoveRight(Val: float) -> void
```

Input callback to strafe right in local space (or left if Val is negative).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Val` | `float` | Amount of movement in the right direction (or left if negative). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MoveUp_World`

```text
MoveUp_World(Val: float) -> void
```

Input callback to move up in world space (or down if Val is negative).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Val` | `float` | Amount of movement in the world up direction (or down if negative). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `TurnAtRate`

```text
TurnAtRate(Rate: float) -> void
```

Called via input to turn at a given rate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rate` | `float` | This is a normalized rate, i.e. 1.0 means 100% of desired turn rate |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `LookUpAtRate`

```text
LookUpAtRate(Rate: float) -> void
```

Called via input to look up at a given rate (or down if Rate is negative).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rate` | `float` | This is a normalized rate, i.e. 1.0 means 100% of desired turn rate |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
