---
id: "api:class:UPhysicsHandleComponent"
title: "UPhysicsHandleComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPhysicsHandleComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPhysicsHandleComponent

Utility object for moving physics objects around.

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GrabbedComponent` | `UPrimitiveComponent *` | Component we are currently holding |
| `bSoftAngularConstraint` | `uint32` | - |
| `bSoftLinearConstraint` | `uint32` | - |
| `bInterpolateTarget` | `uint32` | - |
| `LinearDamping` | `float` | Linear damping of the handle spring. |
| `LinearStiffness` | `float` | Linear stiffness of the handle spring |
| `AngularDamping` | `float` | Angular stiffness of the handle spring |
| `AngularStiffness` | `float` | Angular stiffness of the handle spring |
| `InterpolationSpeed` | `float` | How quickly we interpolate the physics target transform |

## Functions

### `GrabComponent`

```text
GrabComponent(Component: UPrimitiveComponent *, InBoneName: FName, GrabLocation: FVector, bConstrainRotation: bool) -> ENGINE_API virtual void
```

Grab the specified component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent *` | - |
| `InBoneName` | `FName` | - |
| `GrabLocation` | `FVector` | - |
| `bConstrainRotation` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API virtual void` | - |

### `GrabComponentAtLocation`

```text
GrabComponentAtLocation(Component: UPrimitiveComponent *, InBoneName: FName, GrabLocation: FVector) -> ENGINE_API void
```

Grab the specified component at a given location. Does NOT constraint rotation which means the handle will pivot about GrabLocation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent *` | - |
| `InBoneName` | `FName` | - |
| `GrabLocation` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GrabComponentAtLocationWithRotation`

```text
GrabComponentAtLocationWithRotation(Component: UPrimitiveComponent *, InBoneName: FName, Location: FVector, Rotation: FRotator) -> ENGINE_API void
```

Grab the specified component at a given location and rotation. Constrains rotation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent *` | - |
| `InBoneName` | `FName` | - |
| `Location` | `FVector` | - |
| `Rotation` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `ReleaseComponent`

```text
ReleaseComponent() -> ENGINE_API virtual void
```

Release the currently held component

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API virtual void` | - |

### `GetGrabbedComponent`

```text
GetGrabbedComponent() -> ENGINE_API class UPrimitiveComponent *
```

Returns the currently grabbed component, or null if nothing is grabbed.

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API class UPrimitiveComponent *` | - |

### `SetTargetLocation`

```text
SetTargetLocation(NewLocation: FVector) -> ENGINE_API void
```

Set the target location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetTargetRotation`

```text
SetTargetRotation(NewRotation: FRotator) -> ENGINE_API void
```

Set the target rotation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRotation` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetTargetLocationAndRotation`

```text
SetTargetLocationAndRotation(NewLocation: FVector, NewRotation: FRotator) -> ENGINE_API void
```

Set target location and rotation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector` | - |
| `NewRotation` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GetTargetLocationAndRotation`

```text
GetTargetLocationAndRotation(TargetLocation: FVector &, TargetRotation: FRotator &) -> ENGINE_API void
```

Get the current location and rotation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetLocation` | `FVector &` | - |
| `TargetRotation` | `FRotator &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetLinearDamping`

```text
SetLinearDamping(NewLinearDamping: float) -> ENGINE_API void
```

Set linear damping

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLinearDamping` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetLinearStiffness`

```text
SetLinearStiffness(NewLinearStiffness: float) -> ENGINE_API void
```

Set linear stiffness

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLinearStiffness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetAngularDamping`

```text
SetAngularDamping(NewAngularDamping: float) -> ENGINE_API void
```

Set angular damping

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAngularDamping` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetAngularStiffness`

```text
SetAngularStiffness(NewAngularStiffness: float) -> ENGINE_API void
```

Set angular stiffness

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAngularStiffness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetInterpolationSpeed`

```text
SetInterpolationSpeed(NewInterpolationSpeed: float) -> ENGINE_API void
```

Set interpolation speed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewInterpolationSpeed` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

## Language

`cpp`
