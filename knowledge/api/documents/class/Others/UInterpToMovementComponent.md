---
id: "api:class:UInterpToMovementComponent"
title: "UInterpToMovementComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UInterpToMovementComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UInterpToMovementComponent

Move the root component between a series of points over a given time  
 
  @see UMovementComponent

## Inheritance

`UMovementComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Duration` | `float` | How long to take to move from the first point to the last (or vice versa) |
| `bPauseOnImpact` | `uint32` | If true, will pause movement on impact. If false it will behave as if the end of the movement range was reached based on the BehaviourType. |
| `BehaviourType` | `EInterpToBehaviourType` | Movement behaviour of the component |
| `bForceSubStepping` | `uint32` | If true, forces sub-stepping to break up movement into discrete smaller steps to improve accuracy of the trajectory.<br>	  Objects that move in a straight line typically do not need to set this, as movement always uses continuous collision detection (sweeps) so collision is not missed.<br>	  Sub-stepping is automatically enabled when under the effects of gravity or when homing towards a target.<br>	  @see MaxSimulationTimeStep, MaxSimulationIterations |
| `MaxSimulationTimeStep` | `float` | Max time delta for each discrete simulation step.<br>	  Lowering this value can address issues with fast-moving objects or complex collision scenarios, at the cost of performance.<br>	 <br>	  WARNING: if (MaxSimulationTimeStep  MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.<br>	  @see MaxSimulationIterations, bForceSubStepping |
| `MaxSimulationIterations` | `int32` | Max number of iterations used for each discrete simulation step.<br>	  Increasing this value can address issues with fast-moving objects or complex collision scenarios, at the cost of performance.<br>	 <br>	  WARNING: if (MaxSimulationTimeStep  MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.<br>	  @see MaxSimulationTimeStep, bForceSubStepping |
| `ControlPoints` | `TArray < FInterpControlPoint >` | List of control points to visit. |

## Functions

### `StopSimulating`

```text
StopSimulating(HitResult: FHitResult &) -> void
```

Clears the reference to UpdatedComponent, fires stop event, and stops ticking.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HitResult` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestartMovement`

```text
RestartMovement(InitialDirection: float) -> void
```

Reset to start. Sets time to zero and direction to 1.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InitialDirection` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FinaliseControlPoints`

```text
FinaliseControlPoints() -> void
```

Initialise the control points array. Call after adding control points if they are add after begin play .

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnInterpToReverse`

```text
OnInterpToReverse(ImpactResult: const FHitResult&, Time: float) -> void
```

Called when InterpTo impacts something and reverse is enabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `const FHitResult&` | - |
| `Time` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInterpToStop`

```text
OnInterpToStop(ImpactResult: const FHitResult&, Time: float) -> void
```

Called when InterpTo has come to a stop.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `const FHitResult&` | - |
| `Time` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWaitBeginDelegate`

```text
OnWaitBeginDelegate(ImpactResult: const FHitResult&, Time: float) -> void
```

Called when InterpTo has come to a stop but will resume when possible.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `const FHitResult&` | - |
| `Time` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWaitEndDelegate`

```text
OnWaitEndDelegate(ImpactResult: const FHitResult&, Time: float) -> void
```

Called when InterpTo has resumed following a stop.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `const FHitResult&` | - |
| `Time` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnResetDelegate`

```text
OnResetDelegate(ImpactResult: const FHitResult&, Time: float) -> void
```

Called when InterpTo reached the end and reset back to start .

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `const FHitResult&` | - |
| `Time` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
