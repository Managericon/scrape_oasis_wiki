---
id: "api:class:UAISense_Blueprint"
title: "UAISense_Blueprint"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAISense_Blueprint.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAISense_Blueprint

## Inheritance

`UAISense`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ListenerDataType` | `TSubclassOf < UUserDefinedStruct >` | - |
| `ListenerContainer` | `TArray < UAIPerceptionComponent * >` | - |
| `UnprocessedEvents` | `TArray < UAISenseEvent * >` | - |

## Functions

### `OnUpdate`

```text
OnUpdate(EventsToProcess: TArray < UAISenseEvent * > &) -> float
```

returns requested amount of time to pass until next frame. 
	 	Return 0 to get update every frame (WARNING: hits performance)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EventsToProcess` | `TArray < UAISenseEvent * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `OnListenerRegistered`

```text
OnListenerRegistered(ActorListener: AActor *, PerceptionComponent: UAIPerceptionComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActorListener` | `AActor *` | - |
| `PerceptionComponent` | `UAIPerceptionComponent *` | is ActorListener's AIPerceptionComponent instance |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnListenerUpdated`

```text
OnListenerUpdated(ActorListener: AActor *, PerceptionComponent: UAIPerceptionComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActorListener` | `AActor *` | - |
| `PerceptionComponent` | `UAIPerceptionComponent *` | is ActorListener's AIPerceptionComponent instance |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnListenerUnregistered`

```text
OnListenerUnregistered(ActorListener: AActor *, PerceptionComponent: UAIPerceptionComponent *) -> void
```

called when a listener unregistered from this sense. Most often this is called due to actor's death

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActorListener` | `AActor *` | - |
| `PerceptionComponent` | `UAIPerceptionComponent *` | is ActorListener's AIPerceptionComponent instance |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAllListenerActors`

```text
GetAllListenerActors(ListenerActors: TArray < AActor * > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ListenerActors` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAllListenerComponents`

```text
GetAllListenerComponents(ListenerComponents: TArray < UAIPerceptionComponent * > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ListenerComponents` | `TArray < UAIPerceptionComponent * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_OnNewPawn`

```text
K2_OnNewPawn(NewPawn: APawn *) -> void
```

called when sense's instance gets notified about new pawn that has just been spawned

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
