---
id: "api:class:UAIBlueprintHelperLibrary"
title: "UAIBlueprintHelperLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAIBlueprintHelperLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAIBlueprintHelperLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `CreateMoveToProxyObject`

```text
CreateMoveToProxyObject(WorldContextObject: UObject *, Pawn: APawn *, Destination: FVector, TargetActor: AActor *, AcceptanceRadius: float, bStopOnOverlap: bool) -> UAIAsyncTaskBlueprintProxy *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Pawn` | `APawn *` | - |
| `Destination` | `FVector` | - |
| `TargetActor` | `AActor *` | - |
| `AcceptanceRadius` | `float` | - |
| `bStopOnOverlap` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `UAIAsyncTaskBlueprintProxy *` | - |

### `SendAIMessage`

```text
SendAIMessage(Target: APawn *, Message: FName, MessageSource: UObject *, bSuccess: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `APawn *` | - |
| `Message` | `FName` | - |
| `MessageSource` | `UObject *` | - |
| `bSuccess` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SpawnAIFromClass`

```text
SpawnAIFromClass(WorldContextObject: UObject *, PawnClass: TSubclassOf < APawn >, BehaviorTree: UBehaviorTree *, Location: FVector, Rotation: FRotator, bNoCollisionFail: bool) -> APawn *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PawnClass` | `TSubclassOf < APawn >` | - |
| `BehaviorTree` | `UBehaviorTree *` | - |
| `Location` | `FVector` | - |
| `Rotation` | `FRotator` | - |
| `bNoCollisionFail` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `APawn *` | - |

### `GetAIController`

```text
GetAIController(ControlledActor: AActor *) -> AAIController *
```

The way it works exactly is if the actor passed in is a pawn, then the function retrieves 
	 	pawn's controller cast to AIController. Otherwise the function returns actor cast to AIController.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ControlledActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `AAIController *` | - |

### `GetBlackboard`

```text
GetBlackboard(Target: AActor *) -> UBlackboardComponent *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `UBlackboardComponent *` | - |

### `LockAIResourcesWithAnimation`

```text
LockAIResourcesWithAnimation(AnimInstance: UAnimInstance *, bLockMovement: bool, LockAILogic: bool) -> void
```

locks indicated AI resources of animated pawn

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AnimInstance` | `UAnimInstance *` | - |
| `bLockMovement` | `bool` | - |
| `LockAILogic` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnlockAIResourcesWithAnimation`

```text
UnlockAIResourcesWithAnimation(AnimInstance: UAnimInstance *, bUnlockMovement: bool, UnlockAILogic: bool) -> void
```

unlocks indicated AI resources of animated pawn. Will unlock only animation-locked resources

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AnimInstance` | `UAnimInstance *` | - |
| `bUnlockMovement` | `bool` | - |
| `UnlockAILogic` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsValidAILocation`

```text
IsValidAILocation(Location: FVector) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Location` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsValidAIDirection`

```text
IsValidAIDirection(DirectionVector: FVector) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DirectionVector` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsValidAIRotation`

```text
IsValidAIRotation(Rotation: FRotator) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rotation` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetCurrentPath`

```text
GetCurrentPath(Controller: AController *) -> UNavigationPath *
```

Returns a copy of navigation path given controller is currently using. 
	 	The result being a copy means you won't be able to influence agent's pathfollowing 
	 	by manipulating received path

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Controller` | `AController *` | - |

**Returns**

| Type | Description |
|---|---|
| `UNavigationPath *` | - |

## Language

`cpp`
