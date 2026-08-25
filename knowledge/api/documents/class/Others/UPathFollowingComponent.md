---
id: "api:class:UPathFollowingComponent"
title: "UPathFollowingComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPathFollowingComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPathFollowingComponent

## Inheritance

`UActorComponent` -> `IAIResourceInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MovementComp` | `UNavMovementComponent *` | associated movement component |
| `MyNavData` | `ANavigationData *` | navigation data for agent described in movement component |

## Functions

### `OnActorBump`

```text
OnActorBump(SelfActor: AActor *, OtherActor: AActor *, NormalImpulse: FVector, Hit: FHitResult &) -> void
```

called when moving agent collides with another actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelfActor` | `AActor *` | - |
| `OtherActor` | `AActor *` | - |
| `NormalImpulse` | `FVector` | - |
| `Hit` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPathActionType`

```text
GetPathActionType() -> EPathFollowingAction :: Type
```

**Returns**

| Type | Description |
|---|---|
| `EPathFollowingAction :: Type` | - |

### `GetPathDestination`

```text
GetPathDestination() -> FVector
```

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `OnNavDataRegistered`

```text
OnNavDataRegistered(NavData: ANavigationData *) -> void
```

called when NavigationSystem registers new navigation data type while this component
	 	instance has empty MyNavData. This is usually the case for AI agents hand-placed
	 	on levels.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NavData` | `ANavigationData *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
