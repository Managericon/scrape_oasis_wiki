---
id: "api:class:AAIController"
title: "AAIController"
source: "https://developer.gp.qq.com/api/class/detail/Others/AAIController.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AAIController

AIController is the base class of controllers for AI-controlled Pawns.
  
  Controllers are non-physical actors that can be attached to a pawn to control its actions.
  AIControllers manage the artificial intelligence for the pawns they control.
  In networked games, they only exist on the server.

## Inheritance

`AController` -> `IAIPerceptionListenerInterface` -> `IGameplayTaskOwnerInterface` -> `IGenericTeamAgentInterface` -> `IVisualLoggerDebugSnapshotInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bStopAILogicOnUnposses` | `uint32` | By default AI's logic gets stopped when controlled Pawn is unpossesed. Setting this flag to false<br>	 	will make AI logic persist past loosing controll over a pawn |
| `bSkipExtraLOSChecks` | `uint32` | Skip extra line of sight traces to extremities of target being checked. |
| `bAllowStrafe` | `uint32` | Is strafing allowed during movement? |
| `bWantsPlayerState` | `uint32` | Specifies if this AI wants its own PlayerState. |
| `bSetControlRotationFromPawnOrientation` | `uint32` | Copy Pawn rotation to ControlRotation, if there is no focus point. |
| `PathFollowingComponent` | `UPathFollowingComponent *` | Component used for moving along a path. |
| `BrainComponent` | `UBrainComponent *` | Component responsible for behaviors. |
| `PerceptionComponent` | `UAIPerceptionComponent *` | - |
| `ActionsComp` | `UPawnActionsComponent *` | - |
| `Blackboard` | `UBlackboardComponent *` | blackboard |
| `CachedGameplayTasksComponent` | `UGameplayTasksComponent *` | - |
| `DefaultNavigationFilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |

## Functions

### `OnPossess`

```text
OnPossess(PossessedPawn: APawn *) -> void
```

Event called when PossessedPawn is possessed by this controller.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PossessedPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnUnpossess`

```text
OnUnpossess(UnpossessedPawn: APawn *) -> void
```

Gets triggered after given pawn has been unpossesed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UnpossessedPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MoveToActor`

```text
MoveToActor(Goal: AActor *, AcceptanceRadius: float, bStopOnOverlap: bool, bUsePathfinding: bool, bCanStrafe: bool, FilterClass: TSubclassOf < UNavigationQueryFilter >, bAllowPartialPath: bool) -> EPathFollowingRequestResult :: Type
```

Makes AI go toward specified Goal actor (destination will be continuously updated), aborts any active path following

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Goal` | `AActor *` | - |
| `AcceptanceRadius` | `float` | - finish move if pawn gets close enough |
| `bStopOnOverlap` | `bool` | - add pawn's radius to AcceptanceRadius |
| `bUsePathfinding` | `bool` | - use navigation data to calculate path (otherwise it will go in straight line) |
| `bCanStrafe` | `bool` | - set focus related flag: bAllowStrafe |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - navigation filter for pathfinding adjustments. If none specified DefaultNavigationFilterClass will be used |
| `bAllowPartialPath` | `bool` | - use incomplete path when goal can't be reached |

**Returns**

| Type | Description |
|---|---|
| `EPathFollowingRequestResult :: Type` | - |

### `MoveToLocation`

```text
MoveToLocation(Dest: FVector &, AcceptanceRadius: float, bStopOnOverlap: bool, bUsePathfinding: bool, bProjectDestinationToNavigation: bool, bCanStrafe: bool, FilterClass: TSubclassOf < UNavigationQueryFilter >, bAllowPartialPath: bool, bUseNavLink: bool) -> EPathFollowingRequestResult :: Type
```

Makes AI go toward specified Dest location, aborts any active path following

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Dest` | `FVector &` | - |
| `AcceptanceRadius` | `float` | - finish move if pawn gets close enough |
| `bStopOnOverlap` | `bool` | - add pawn's radius to AcceptanceRadius |
| `bUsePathfinding` | `bool` | - use navigation data to calculate path (otherwise it will go in straight line) |
| `bProjectDestinationToNavigation` | `bool` | - project location on navigation data before using it |
| `bCanStrafe` | `bool` | - set focus related flag: bAllowStrafe |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - navigation filter for pathfinding adjustments. If none specified DefaultNavigationFilterClass will be used |
| `bAllowPartialPath` | `bool` | - use incomplete path when goal can't be reached |
| `bUseNavLink` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `EPathFollowingRequestResult :: Type` | - |

### `GetMoveStatus`

```text
GetMoveStatus() -> EPathFollowingStatus :: Type
```

Returns status of path following

**Returns**

| Type | Description |
|---|---|
| `EPathFollowingStatus :: Type` | - |

### `HasPartialPath`

```text
HasPartialPath() -> bool
```

Returns true if the current PathFollowingComponent's path is partial (does not reach desired destination).

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetImmediateMoveDestination`

```text
GetImmediateMoveDestination() -> FVector
```

Returns position of current path segment's end.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SetMoveBlockDetection`

```text
SetMoveBlockDetection(bEnable: bool) -> void
```

Updates state of movement block detection.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RunBehaviorTree`

```text
RunBehaviorTree(BTAsset: UBehaviorTree *) -> bool
```

Starts executing behavior tree.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BTAsset` | `UBehaviorTree *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `UseBlackboard`

```text
UseBlackboard(BlackboardAsset: UBlackboardData *, BlackboardComponent: UBlackboardComponent * &) -> bool
```

Makes AI use the specified Blackboard asset & creates a Blackboard Component if one does not already exist.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BlackboardAsset` | `UBlackboardData *` | The Blackboard asset to use. |
| `BlackboardComponent` | `UBlackboardComponent * &` | The Blackboard component that was used or created to work with the passed-in Blackboard Asset. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if we successfully linked the blackboard asset to the blackboard component. |

### `ClaimTaskResource`

```text
ClaimTaskResource(ResourceClass: TSubclassOf < UGameplayTaskResource >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ResourceClass` | `TSubclassOf < UGameplayTaskResource >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnclaimTaskResource`

```text
UnclaimTaskResource(ResourceClass: TSubclassOf < UGameplayTaskResource >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ResourceClass` | `TSubclassOf < UGameplayTaskResource >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnUsingBlackBoard`

```text
OnUsingBlackBoard(BlackboardComp: UBlackboardComponent *, BlackboardAsset: UBlackboardData *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BlackboardComp` | `UBlackboardComponent *` | - |
| `BlackboardAsset` | `UBlackboardData *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetFocalPoint`

```text
GetFocalPoint() -> FVector
```

Retrieve the final position that controller should be looking at.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetFocalPointOnActor`

```text
GetFocalPointOnActor(Actor: AActor *) -> FVector
```

Retrieve the focal point this controller should focus to on given actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `K2_SetFocalPoint`

```text
K2_SetFocalPoint(FP: FVector) -> void
```

Set the position that controller should be looking at.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FP` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetFocus`

```text
K2_SetFocus(NewFocus: AActor *) -> void
```

Set Focus for actor, will set FocalPoint as a result.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewFocus` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetFocusActor`

```text
GetFocusActor() -> AActor *
```

Get the focused actor.

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `K2_ClearFocus`

```text
K2_ClearFocus() -> void
```

Clears Focus, will also clear FocalPoint as a result

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnGameplayTaskResourcesClaimed`

```text
OnGameplayTaskResourcesClaimed(NewlyClaimed: FGameplayResourceSet, FreshlyReleased: FGameplayResourceSet) -> void
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

### `GetPathFollowingComponent`

```text
GetPathFollowingComponent() -> UPathFollowingComponent *
```

Returns PathFollowingComponent subobject

**Returns**

| Type | Description |
|---|---|
| `UPathFollowingComponent *` | - |

### `GetAIPerceptionComponent`

```text
GetAIPerceptionComponent() -> UAIPerceptionComponent *
```

**Returns**

| Type | Description |
|---|---|
| `UAIPerceptionComponent *` | - |

## Delegates

### `ReceiveMoveCompleted`

```text
ReceiveMoveCompleted(RequestID: FAIRequestID, Result: EPathFollowingResult::Type) -> void
```

Blueprint notification that we've completed the current movement request

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RequestID` | `FAIRequestID` | - |
| `Result` | `EPathFollowingResult::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
