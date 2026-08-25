---
id: "api:class:UAISystem"
title: "UAISystem"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAISystem.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAISystem

## Inheritance

`UAISystemBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PerceptionSystemClassName` | `FSoftClassPath` | - |
| `HotSpotManagerClassName` | `FSoftClassPath` | - |
| `NavLocalGridManagerClassName` | `FSoftClassPath` | Class that will be used to spawn the hot spot manager, can be game-specific |
| `AcceptanceRadius` | `float` | Default AI movement's acceptance radius used to determine whether <br> 	  AI reached path's end |
| `PathfollowingRegularPathPointAcceptanceRadius` | `float` | Value used for pathfollowing's internal code to determine whether AI reached path's point. <br>	 	@note this value is not used for path's last point. @see AcceptanceRadius |
| `PathfollowingNavLinkAcceptanceRadius` | `float` | Similarly to PathfollowingRegularPathPointAcceptanceRadius used by pathfollowing's internals<br>	 	but gets applied only when next point on a path represents a begining of navigation link |
| `bFinishMoveOnGoalOverlap` | `bool` | - |
| `bAcceptPartialPaths` | `bool` | - |
| `bAllowStrafing` | `bool` | - |
| `bEnableBTAITasks` | `bool` | this property is just a transition-time flag - in the end we're going to switch over to Gameplay Tasks anyway, that's the goal. |
| `bAllowControllersAsEQSQuerier` | `bool` | if enable will make EQS not complaint about using Controllers as queriers. Default behavior (false) will <br>	 	in places automatically convert controllers to pawns, and complain if code user bypasses the conversion or uses<br>	 	pawn-less controller |
| `bEnableDebuggerPlugin` | `bool` | if set, GameplayDebuggerPlugin will be loaded on module's startup |
| `DefaultSightCollisionChannel` | `TEnumAsByte < ECollisionChannel >` | - |
| `BehaviorTreeManager` | `UBehaviorTreeManager *` | Behavior tree manager used by game |
| `EnvironmentQueryManager` | `UEnvQueryManager *` | Environment query manager used by game |
| `PerceptionSystem` | `UAIPerceptionSystem *` | - |
| `AllProxyObjects` | `TArray < UAIAsyncTaskBlueprintProxy * >` | - |
| `HotSpotManager` | `UAIHotSpotManager *` | - |
| `NavLocalGrids` | `UNavLocalGridManager *` | - |

## Functions

### `AIIgnorePlayers`

```text
AIIgnorePlayers() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AILoggingVerbose`

```text
AILoggingVerbose() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
