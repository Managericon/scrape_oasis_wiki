---
id: "api:class:UGameplayTask_SpawnActor"
title: "UGameplayTask_SpawnActor"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGameplayTask_SpawnActor.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGameplayTask_SpawnActor

Convenience task for spawning actors (optionally limiting the spawning to the network authority). If not the net authority, we will not spawn 
 	and Success will not be called. The nice thing this adds is the ability to modify expose on spawn properties while also implicitly checking 
 	network role before spawning.
 
 	Though this task doesn't do much - games can implement similar tasks that carry out game specific rules. For example a 'SpawnProjectile'
 	task that limits the available classes to the games projectile class, and that does game specific stuff on spawn (for example, determining
 	firing position from a weapon attachment).
 	
 	Long term we can also use this task as a sync point. If the executing client could wait execution until the server creates and replicates the 
 	actor down to him. We could potentially also use this to do predictive actor spawning  reconciliation.

## Inheritance

`UGameplayTask`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ClassToSpawn` | `TSubclassOf < AActor >` | - |

## Functions

### `SpawnActor`

```text
SpawnActor(TaskOwner: TScriptInterface < IGameplayTaskOwnerInterface >, SpawnLocation: FVector, SpawnRotation: FRotator, Class: TSubclassOf < AActor >, bSpawnOnlyOnAuthority: bool) -> UGameplayTask_SpawnActor *
```

Spawn new Actor on the network authority (server)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskOwner` | `TScriptInterface < IGameplayTaskOwnerInterface >` | - |
| `SpawnLocation` | `FVector` | - |
| `SpawnRotation` | `FRotator` | - |
| `Class` | `TSubclassOf < AActor >` | - |
| `bSpawnOnlyOnAuthority` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `UGameplayTask_SpawnActor *` | - |

### `BeginSpawningActor`

```text
BeginSpawningActor(WorldContextObject: UObject *, SpawnedActor: AActor * &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `SpawnedActor` | `AActor * &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `FinishSpawningActor`

```text
FinishSpawningActor(WorldContextObject: UObject *, SpawnedActor: AActor *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `SpawnedActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `Success`

```text
Success(SpawnedActor: AActor*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SpawnedActor` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DidNotSpawn`

```text
DidNotSpawn(SpawnedActor: AActor*) -> void
```

Called when we can't spawn: on clients or potentially on server if they fail to spawn (rare)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SpawnedActor` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
