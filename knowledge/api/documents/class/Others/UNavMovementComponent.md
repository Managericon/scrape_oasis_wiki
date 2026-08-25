---
id: "api:class:UNavMovementComponent"
title: "UNavMovementComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UNavMovementComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UNavMovementComponent

NavMovementComponent defines base functionality for MovementComponents that move any 'agent' that may be involved in AI pathfinding.

## Inheritance

`UMovementComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NavAgentProps` | `FNavAgentProperties` | Properties that define how the component can move. |
| `FixedPathBrakingDistance` | `float` | Braking distance override used with acceleration driven path following (bUseAccelerationForPaths) |
| `bUpdateNavAgentWithOwnersCollision` | `uint32` | If set to true NavAgentProps' radius and height will be updated with Owner's collision capsule size |
| `bUseAccelerationForPaths` | `uint32` | If set, pathfollowing will control character movement via acceleration values. If false, it will set velocities directly. |
| `bUseFixedBrakingDistanceForPaths` | `uint32` | If set, FixedPathBrakingDistance will be used for path following deceleration |
| `MovementState` | `FMovementProperties` | Expresses runtime state of character's movement. Put all temporal changes to movement properties here |

## Functions

### `StopActiveMovement`

```text
StopActiveMovement() -> void
```

Stops applying further movement (usually zeros acceleration).

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopMovementKeepPathing`

```text
StopMovementKeepPathing() -> void
```

Stops movement immediately (reset velocity) but keeps following current path

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsCrouching`

```text
IsCrouching() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if currently crouching |

### `IsFalling`

```text
IsFalling() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if currently falling (not flying, in a non-fluid volume, and not on the ground) |

### `IsMovingOnGround`

```text
IsMovingOnGround() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if currently moving on the ground (e.g. walking or driving) |

### `IsSwimming`

```text
IsSwimming() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if currently swimming (moving through a fluid volume) |

### `IsFlying`

```text
IsFlying() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if currently flying (moving through a non-fluid volume without resting on the ground) |

## Language

`cpp`
