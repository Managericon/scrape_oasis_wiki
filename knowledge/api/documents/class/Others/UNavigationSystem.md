---
id: "api:class:UNavigationSystem"
title: "UNavigationSystem"
source: "https://developer.gp.qq.com/api/class/detail/Others/UNavigationSystem.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UNavigationSystem

## Inheritance

`UBlueprintFunctionLibrary`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MainNavData` | `ANavigationData *` | - |
| `AbstractNavData` | `ANavigationData *` | special navigation data for managing direct paths, not part of NavDataSet! |
| `CrowdManagerClass` | `TSubclassOf < UCrowdManagerBase >` | - |
| `bAutoCreateNavigationData` | `uint32` | Should navigation system spawn default Navigation Data when there's none and there are navigation bounds present? |
| `bAllowClientSideNavigation` | `uint32` | - |
| `bSupportRebuilding` | `uint32` | gets set to true if gathering navigation data (like in navoctree) is required due to the need of navigation generation<br>	 	Is always true in Editor Mode. In other modes it depends on bRebuildAtRuntime of every required NavigationData class' CDO |
| `ObstacleManagerClassPath` | `FSoftClassPath` | - |
| `bInitialBuildingLocked` | `uint32` | if set to true will result navigation system not rebuild navigation until<br>	 	a call to ReleaseInitialBuildingLock() is called. Does not influence<br>	 	editor-time generation (i.e. does influence PIE and Game).<br>	 	Defaults to false. |
| `bWholeWorldNavigable` | `uint32` | If set to true (default) navigation will be generated only within special navigation<br>	 	bounds volumes (like ANavMeshBoundsVolume). Set to false means navigation should be generated<br>	 	everywhere. |
| `bSkipAgentHeightCheckWhenPickingNavData` | `uint32` | false by default, if set to true will result in not caring about nav agent height<br>	 	when trying to match navigation data to passed in nav agent |
| `DataGatheringMode` | `ENavDataGatheringModeConfig` | - |
| `bGenerateNavigationOnlyAroundNavigationInvokers` | `uint32` | If set to true navigation will be generated only around registered "navigation enforcers"<br>		This has a range of consequences (including how navigation octree operates) so it needs to<br>		be a conscious decision.<br>		Once enabled results in whole world being navigable.<br>		@see RegisterNavigationInvoker |
| `ActiveTilesUpdateInterval` | `float` | Minimal time, in seconds, between active tiles set update |
| `SupportedAgents` | `TArray < FNavDataConfig >` | - |
| `DirtyAreasUpdateFreq` | `float` | update frequency for dirty areas on navmesh |
| `NavDataSet` | `TArray < ANavigationData * >` | - |
| `NavDataRegistrationQueue` | `TArray < ANavigationData * >` | - |
| `OperationMode` | `FNavigationSystemRunMode` | - |

## Functions

### `BP_ChangeRecastPartitioning`

```text
BP_ChangeRecastPartitioning(AgentName: FName, High: bool) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AgentName` | `FName` | - |
| `High` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `BP_BuildOne`

```text
BP_BuildOne(AgentName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AgentName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BP_DynamicBuildOne`

```text
BP_DynamicBuildOne(AgentName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AgentName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BP_Build`

```text
BP_Build() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BP_AddDynamicNavAffect`

```text
BP_AddDynamicNavAffect(AgentName: FName, InBounds: FBox &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AgentName` | `FName` | - |
| `InBounds` | `FBox &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `BP_IncrementalBuild`

```text
BP_IncrementalBuild(AgentName: FName) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AgentName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `BP_CancelBuild`

```text
BP_CancelBuild(AgentName: FName) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AgentName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `BP_GetNavigationData`

```text
BP_GetNavigationData(AgentName: FName) -> ANavigationData *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AgentName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `ANavigationData *` | - |

### `GetNavigationSystem`

```text
GetNavigationSystem(WorldContextObject: UObject *) -> UNavigationSystem *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `UNavigationSystem *` | - |

### `K2_ProjectPointToNavigation`

```text
K2_ProjectPointToNavigation(WorldContextObject: UObject *, Point: FVector &, ProjectedLocation: FVector &, NavData: ANavigationData *, FilterClass: TSubclassOf < UNavigationQueryFilter >, QueryExtent: FVector) -> bool
```

Project a point onto the NavigationData

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Point` | `FVector &` | - |
| `ProjectedLocation` | `FVector &` | - |
| `NavData` | `ANavigationData *` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |
| `QueryExtent` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `K2_GetRandomReachablePointInRadius`

```text
K2_GetRandomReachablePointInRadius(WorldContextObject: UObject *, Origin: FVector &, RandomLocation: FVector &, Radius: float, NavData: ANavigationData *, FilterClass: TSubclassOf < UNavigationQueryFilter >, ExtentRadius: float) -> bool
```

Generates a random location reachable from given Origin location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Origin` | `FVector &` | - |
| `RandomLocation` | `FVector &` | - |
| `Radius` | `float` | - |
| `NavData` | `ANavigationData *` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |
| `ExtentRadius` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | Return Value represents if the call was successful |

### `K2_GetRandomPointInNavigableRadius`

```text
K2_GetRandomPointInNavigableRadius(WorldContextObject: UObject *, Origin: FVector &, RandomLocation: FVector &, Radius: float, NavData: ANavigationData *, FilterClass: TSubclassOf < UNavigationQueryFilter >) -> bool
```

Generates a random location in navigable space within given radius of Origin.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Origin` | `FVector &` | - |
| `RandomLocation` | `FVector &` | - |
| `Radius` | `float` | - |
| `NavData` | `ANavigationData *` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | Return Value represents if the call was successful |

### `GetPathCost`

```text
GetPathCost(WorldContextObject: UObject *, PathStart: FVector &, PathEnd: FVector &, PathCost: float &, NavData: ANavigationData *, FilterClass: TSubclassOf < UNavigationQueryFilter >) -> ENavigationQueryResult :: Type
```

Potentially expensive. Use with caution. Consider using UPathFollowingComponent::GetRemainingPathCost instead

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PathStart` | `FVector &` | - |
| `PathEnd` | `FVector &` | - |
| `PathCost` | `float &` | - |
| `NavData` | `ANavigationData *` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |

**Returns**

| Type | Description |
|---|---|
| `ENavigationQueryResult :: Type` | - |

### `GetPathLength`

```text
GetPathLength(WorldContextObject: UObject *, PathStart: FVector &, PathEnd: FVector &, PathLength: float &, NavData: ANavigationData *, FilterClass: TSubclassOf < UNavigationQueryFilter >) -> ENavigationQueryResult :: Type
```

Potentially expensive. Use with caution

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PathStart` | `FVector &` | - |
| `PathEnd` | `FVector &` | - |
| `PathLength` | `float &` | - |
| `NavData` | `ANavigationData *` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |

**Returns**

| Type | Description |
|---|---|
| `ENavigationQueryResult :: Type` | - |

### `IsNavigationBeingBuilt`

```text
IsNavigationBeingBuilt(WorldContextObject: UObject *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsNavigationBeingBuiltOrLocked`

```text
IsNavigationBeingBuiltOrLocked(WorldContextObject: UObject *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SimpleMoveToActor`

```text
SimpleMoveToActor(Controller: AController *, Goal: AActor *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Controller` | `AController *` | - |
| `Goal` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SimpleMoveToLocation`

```text
SimpleMoveToLocation(Controller: AController *, Goal: FVector &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Controller` | `AController *` | - |
| `Goal` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FindPathToLocationSynchronously`

```text
FindPathToLocationSynchronously(WorldContextObject: UObject *, PathStart: FVector &, PathEnd: FVector &, PathfindingContext: AActor *, FilterClass: TSubclassOf < UNavigationQueryFilter >) -> UNavigationPath *
```

Finds path instantly, in a FindPath Synchronously.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PathStart` | `FVector &` | - |
| `PathEnd` | `FVector &` | - |
| `PathfindingContext` | `AActor *` | could be one of following: NavigationData (like Navmesh actor), Pawn or Controller. This parameter determines parameters of specific pathfinding query |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |

**Returns**

| Type | Description |
|---|---|
| `UNavigationPath *` | - |

### `FindPathToActorSynchronously`

```text
FindPathToActorSynchronously(WorldContextObject: UObject *, PathStart: FVector &, GoalActor: AActor *, TetherDistance: float, PathfindingContext: AActor *, FilterClass: TSubclassOf < UNavigationQueryFilter >) -> UNavigationPath *
```

Finds path instantly, in a FindPath Synchronously. Main advantage over FindPathToLocationSynchronously is that
	 	the resulting path will automatically get updated if goal actor moves more than TetherDistance away from last path node

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PathStart` | `FVector &` | - |
| `GoalActor` | `AActor *` | - |
| `TetherDistance` | `float` | - |
| `PathfindingContext` | `AActor *` | could be one of following: NavigationData (like Navmesh actor), Pawn or Controller. This parameter determines parameters of specific pathfinding query |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |

**Returns**

| Type | Description |
|---|---|
| `UNavigationPath *` | - |

### `NavigationRaycast`

```text
NavigationRaycast(WorldContextObject: UObject *, RayStart: FVector &, RayEnd: FVector &, HitLocation: FVector &, FilterClass: TSubclassOf < UNavigationQueryFilter >, Querier: AController *) -> bool
```

Performs navigation raycast on NavigationData appropriate for given Querier.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `RayStart` | `FVector &` | - |
| `RayEnd` | `FVector &` | - |
| `HitLocation` | `FVector &` | if line was obstructed this will be set to hit location. Otherwise it contains SegmentEnd |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |
| `Querier` | `AController *` | if not passed default navigation data will be used |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if line from RayStart to RayEnd was obstructed. Also, true when no navigation data present |

### `SetMaxSimultaneousTileGenerationJobsCount`

```text
SetMaxSimultaneousTileGenerationJobsCount(MaxNumberOfJobs: int32) -> void
```

will limit the number of simultaneously running navmesh tile generation jobs to specified number.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MaxNumberOfJobs` | `int32` | gets trimmed to be at least 1. You cannot use this function to pause navmesh generation |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetMaxSimultaneousTileGenerationJobsCount`

```text
ResetMaxSimultaneousTileGenerationJobsCount() -> void
```

Brings limit of simultaneous navmesh tile generation jobs back to Project Setting's default value

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RegisterNavigationInvoker`

```text
RegisterNavigationInvoker(Invoker: AActor *, TileGenerationRadius: float, TileRemovalRadius: float) -> void
```

Registers given actor as a "navigation enforcer" which means navigation system will
	 	make sure navigation is being generated in specified radius around it.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Invoker` | `AActor *` | - |
| `TileGenerationRadius` | `float` | - |
| `TileRemovalRadius` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnregisterNavigationInvoker`

```text
UnregisterNavigationInvoker(Invoker: AActor *) -> void
```

Removes given actor from the list of active navigation enforcers.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Invoker` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetGeometryGatheringMode`

```text
SetGeometryGatheringMode(NewMode: ENavDataGatheringModeConfig) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewMode` | `ENavDataGatheringModeConfig` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnNavigationBoundsUpdated`

```text
OnNavigationBoundsUpdated(NavVolume: ANavMeshBoundsVolume *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NavVolume` | `ANavMeshBoundsVolume *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ProjectPointToNavigation`

```text
ProjectPointToNavigation(WorldContextObject: UObject *, Point: FVector &, NavData: ANavigationData *, FilterClass: TSubclassOf < UNavigationQueryFilter >, QueryExtent: FVector) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Point` | `FVector &` | - |
| `NavData` | `ANavigationData *` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |
| `QueryExtent` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRandomReachablePointInRadius`

```text
GetRandomReachablePointInRadius(WorldContextObject: UObject *, Origin: FVector &, Radius: float, NavData: ANavigationData *, FilterClass: TSubclassOf < UNavigationQueryFilter >) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Origin` | `FVector &` | - |
| `Radius` | `float` | - |
| `NavData` | `ANavigationData *` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRandomPointInNavigableRadius`

```text
GetRandomPointInNavigableRadius(WorldContextObject: UObject *, Origin: FVector &, Radius: float, NavData: ANavigationData *, FilterClass: TSubclassOf < UNavigationQueryFilter >) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Origin` | `FVector &` | - |
| `Radius` | `float` | - |
| `NavData` | `ANavigationData *` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `UpdateDynamicGenerateTargetNav`

```text
UpdateDynamicGenerateTargetNav(IsAdd: bool, GenerateTargetNav: FDynamicGenerateTargetNavigation) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsAdd` | `bool` | - |
| `GenerateTargetNav` | `FDynamicGenerateTargetNavigation` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnNavDataRegisteredEvent`

```text
OnNavDataRegisteredEvent(NavData: ANavigationData*) -> void
```

UPROPERTY(BlueprintAssignable, Transient)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NavData` | `ANavigationData*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnNavigationGenerationFinishedDelegate`

```text
OnNavigationGenerationFinishedDelegate(NavData: ANavigationData*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NavData` | `ANavigationData*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
