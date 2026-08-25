---
id: "api:class:UPhysicsConstraintComponent"
title: "UPhysicsConstraintComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPhysicsConstraintComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPhysicsConstraintComponent

This is effectively a joint that allows you to connect 2 rigid bodies together. You can create different types of joints using the various parameters of this component.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConstraintActor1` | `AActor *` | Pointer to first Actor to constrain. |
| `ComponentName1` | `FConstrainComponentPropName` | Name of first component property to constrain. If Actor1 is NULL, will look within Owner.<br>	 	If this is NULL, will use RootComponent of Actor1 |
| `ConstraintActor2` | `AActor *` | Pointer to second Actor to constrain. |
| `ComponentName2` | `FConstrainComponentPropName` | Name of second component property to constrain. If Actor2 is NULL, will look within Owner. <br>	 	If this is NULL, will use RootComponent of Actor2 |
| `ConstraintSetup_DEPRECATED` | `UPhysicsConstraintTemplate *` | - |
| `OnConstraintBroken` | `FConstraintBrokenSignature` | Notification when constraint is broken. |
| `ConstraintInstance` | `FConstraintInstance` | All constraint settings |

## Functions

### `SetConstrainedComponents`

```text
SetConstrainedComponents(Component1: UPrimitiveComponent *, BoneName1: FName, Component2: UPrimitiveComponent *, BoneName2: FName) -> void
```

Directly specify component to connect. Will update frames based on current position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component1` | `UPrimitiveComponent *` | - |
| `BoneName1` | `FName` | - |
| `Component2` | `UPrimitiveComponent *` | - |
| `BoneName2` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BreakConstraint`

```text
BreakConstraint() -> void
```

Break this constraint

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearPositionDrive`

```text
SetLinearPositionDrive(bEnableDriveX: bool, bEnableDriveY: bool, bEnableDriveZ: bool) -> void
```

EnablesDisables linear position drive

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableDriveX` | `bool` | Indicates whether the drive for the X-Axis should be enabled |
| `bEnableDriveY` | `bool` | Indicates whether the drive for the Y-Axis should be enabled |
| `bEnableDriveZ` | `bool` | Indicates whether the drive for the Z-Axis should be enabled |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearVelocityDrive`

```text
SetLinearVelocityDrive(bEnableDriveX: bool, bEnableDriveY: bool, bEnableDriveZ: bool) -> void
```

EnablesDisables linear position drive

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableDriveX` | `bool` | Indicates whether the drive for the X-Axis should be enabled |
| `bEnableDriveY` | `bool` | Indicates whether the drive for the Y-Axis should be enabled |
| `bEnableDriveZ` | `bool` | Indicates whether the drive for the Z-Axis should be enabled |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularOrientationDrive`

```text
SetAngularOrientationDrive(bEnableSwingDrive: bool, bEnableTwistDrive: bool) -> void
```

EnablesDisables angular orientation drive. Only relevant if the AngularDriveMode is set to Twist and Swing

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableSwingDrive` | `bool` | Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |
| `bEnableTwistDrive` | `bool` | Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOrientationDriveTwistAndSwing`

```text
SetOrientationDriveTwistAndSwing(bEnableTwistDrive: bool, bEnableSwingDrive: bool) -> void
```

EnablesDisables angular orientation drive. Only relevant if the AngularDriveMode is set to Twist and Swing

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableTwistDrive` | `bool` | Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |
| `bEnableSwingDrive` | `bool` | Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOrientationDriveSLERP`

```text
SetOrientationDriveSLERP(bEnableSLERP: bool) -> void
```

EnablesDisables the angular orientation slerp drive. Only relevant if the AngularDriveMode is set to SLERP

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableSLERP` | `bool` | Indicates whether the SLERP drive should be enabled. Only relevant if the AngularDriveMode is set to SLERP |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularVelocityDrive`

```text
SetAngularVelocityDrive(bEnableSwingDrive: bool, bEnableTwistDrive: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableSwingDrive` | `bool` | - |
| `bEnableTwistDrive` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularVelocityDriveTwistAndSwing`

```text
SetAngularVelocityDriveTwistAndSwing(bEnableTwistDrive: bool, bEnableSwingDrive: bool) -> void
```

EnablesDisables angular velocity twist and swing drive. Only relevant if the AngularDriveMode is set to Twist and Swing

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableTwistDrive` | `bool` | Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |
| `bEnableSwingDrive` | `bool` | Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularVelocityDriveSLERP`

```text
SetAngularVelocityDriveSLERP(bEnableSLERP: bool) -> void
```

EnablesDisables the angular velocity slerp drive. Only relevant if the AngularDriveMode is set to SLERP

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableSLERP` | `bool` | Indicates whether the SLERP drive should be enabled. Only relevant if the AngularDriveMode is set to SLERP |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularDriveMode`

```text
SetAngularDriveMode(DriveMode: EAngularDriveMode :: Type) -> void
```

Switches the angular drive mode between SLERP and Twist And Swing

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DriveMode` | `EAngularDriveMode :: Type` | The angular drive mode to use. SLERP uses shortest spherical path, but will not work if any angular constraints are locked. Twist and Swing decomposes the path into the different angular degrees of freedom but may experience gimbal lock |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearPositionTarget`

```text
SetLinearPositionTarget(InPosTarget: FVector &) -> void
```

Sets the target position for the linear drive.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPosTarget` | `FVector &` | Target position |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearVelocityTarget`

```text
SetLinearVelocityTarget(InVelTarget: FVector &) -> void
```

Sets the target velocity for the linear drive.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVelTarget` | `FVector &` | Target velocity |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearDriveParams`

```text
SetLinearDriveParams(PositionStrength: float, VelocityStrength: float, InForceLimit: float) -> void
```

Sets the drive params for the linear drive.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PositionStrength` | `float` | Positional strength for the drive (stiffness) |
| `VelocityStrength` | `float` | Velocity strength of the drive (damping) |
| `InForceLimit` | `float` | Max force applied by the drive |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularOrientationTarget`

```text
SetAngularOrientationTarget(InPosTarget: FRotator &) -> void
```

Sets the target orientation for the angular drive.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPosTarget` | `FRotator &` | Target orientation |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularVelocityTarget`

```text
SetAngularVelocityTarget(InVelTarget: FVector &) -> void
```

Sets the target velocity for the angular drive.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVelTarget` | `FVector &` | Target velocity |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularDriveParams`

```text
SetAngularDriveParams(PositionStrength: float, VelocityStrength: float, InForceLimit: float) -> void
```

Sets the drive params for the angular drive.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PositionStrength` | `float` | Positional strength for the drive (stiffness) |
| `VelocityStrength` | `float` | Velocity strength of the drive (damping) |
| `InForceLimit` | `float` | Max force applied by the drive |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearXLimit`

```text
SetLinearXLimit(ConstraintType: ELinearConstraintMotion, LimitSize: float) -> void
```

Sets the LinearX Motion Type

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConstraintType` | `ELinearConstraintMotion` | New Constraint Type |
| `LimitSize` | `float` | Size of limit |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearYLimit`

```text
SetLinearYLimit(ConstraintType: ELinearConstraintMotion, LimitSize: float) -> void
```

Sets the LinearY Motion Type

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConstraintType` | `ELinearConstraintMotion` | New Constraint Type |
| `LimitSize` | `float` | Size of limit |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearZLimit`

```text
SetLinearZLimit(ConstraintType: ELinearConstraintMotion, LimitSize: float) -> void
```

Sets the LinearZ Motion Type

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConstraintType` | `ELinearConstraintMotion` | New Constraint Type |
| `LimitSize` | `float` | Size of limit |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularSwing1Limit`

```text
SetAngularSwing1Limit(MotionType: EAngularConstraintMotion, Swing1LimitAngle: float) -> void
```

Sets the Angular Swing1 Motion Type

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MotionType` | `EAngularConstraintMotion` | - |
| `Swing1LimitAngle` | `float` | Size of limit in degrees |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularSwing2Limit`

```text
SetAngularSwing2Limit(MotionType: EAngularConstraintMotion, Swing2LimitAngle: float) -> void
```

Sets the Angular Swing2 Motion Type

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MotionType` | `EAngularConstraintMotion` | - |
| `Swing2LimitAngle` | `float` | Size of limit in degrees |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularTwistLimit`

```text
SetAngularTwistLimit(ConstraintType: EAngularConstraintMotion, TwistLimitAngle: float) -> void
```

Sets the Angular Twist Motion Type

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConstraintType` | `EAngularConstraintMotion` | New Constraint Type |
| `TwistLimitAngle` | `float` | Size of limit in degrees |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearBreakable`

```text
SetLinearBreakable(bLinearBreakable: bool, LinearBreakThreshold: float) -> void
```

Sets the Linear Breakable properties

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bLinearBreakable` | `bool` | Whether it is possible to break the joint with linear force |
| `LinearBreakThreshold` | `float` | Force needed to break the joint |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularBreakable`

```text
SetAngularBreakable(bAngularBreakable: bool, AngularBreakThreshold: float) -> void
```

Sets the Angular Breakable properties

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bAngularBreakable` | `bool` | Whether it is possible to break the joint with angular force |
| `AngularBreakThreshold` | `float` | Torque needed to break the joint |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCurrentTwist`

```text
GetCurrentTwist() -> float
```

Gets the current Angular Twist of the constraint

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetCurrentSwing1`

```text
GetCurrentSwing1() -> float
```

Gets the current Swing1 of the constraint

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetCurrentSwing2`

```text
GetCurrentSwing2() -> float
```

Gets the current Swing2 of the constraint

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetConstraintReferenceFrame`

```text
SetConstraintReferenceFrame(Frame: EConstraintFrame :: Type, RefFrame: FTransform &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Frame` | `EConstraintFrame :: Type` | - |
| `RefFrame` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetConstraintReferencePosition`

```text
SetConstraintReferencePosition(Frame: EConstraintFrame :: Type, RefPosition: FVector &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Frame` | `EConstraintFrame :: Type` | - |
| `RefPosition` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetConstraintReferenceOrientation`

```text
SetConstraintReferenceOrientation(Frame: EConstraintFrame :: Type, PriAxis: FVector &, SecAxis: FVector &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Frame` | `EConstraintFrame :: Type` | - |
| `PriAxis` | `FVector &` | - |
| `SecAxis` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDisableCollision`

```text
SetDisableCollision(bDisableCollision: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bDisableCollision` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetConstraintForce`

```text
GetConstraintForce(OutLinearForce: FVector &, OutAngularForce: FVector &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutLinearForce` | `FVector &` | - |
| `OutAngularForce` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsBroken`

```text
IsBroken() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`
