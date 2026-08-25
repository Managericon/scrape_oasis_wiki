---
id: "api:class:UCrowdFollowingComponent"
title: "UCrowdFollowingComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCrowdFollowingComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UCrowdFollowingComponent

## Inheritance

`UPathFollowingComponent` -> `ICrowdAgentInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CrowdAgentMoveDirection` | `FVector` | - |
| `CharacterMovement` | `UCharacterMovementComponent *` | - |
| `AvoidanceGroup_DEPRECATED` | `FNavAvoidanceMask` | DEPRECATED: Group mask for this agent - use property from CharacterMovementComponent instead |
| `GroupsToAvoid_DEPRECATED` | `FNavAvoidanceMask` | DEPRECATED: Will avoid other agents if they are in one of specified groups - use property from CharacterMovementComponent instead |
| `GroupsToIgnore_DEPRECATED` | `FNavAvoidanceMask` | DEPRECATED: Will NOT avoid other agents if they are in one of specified groups, higher priority than GroupsToAvoid - use property from CharacterMovementComponent instead |

## Functions

### `SuspendCrowdSteering`

```text
SuspendCrowdSteering(bSuspend: bool) -> void
```

master switch for crowd steering & avoidance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bSuspend` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
