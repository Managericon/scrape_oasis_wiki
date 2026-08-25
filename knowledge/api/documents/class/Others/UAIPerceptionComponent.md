---
id: "api:class:UAIPerceptionComponent"
title: "UAIPerceptionComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAIPerceptionComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAIPerceptionComponent

AIPerceptionComponent is used to register as stimuli listener in AIPerceptionSystem
 	and gathers registered stimuli. UpdatePerception is called when component gets new stimuli (batched)

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SensesConfig` | `TArray < UAISenseConfig * >` | - |
| `DominantSense` | `TSubclassOf < UAISense >` | Indicated sense that takes precedence over other senses when determining sensed actor's location. <br>	 	Should be set to one of the senses configured in SensesConfig, or None. |
| `AIOwner` | `AAIController *` | - |

## Functions

### `OnOwnerEndPlay`

```text
OnOwnerEndPlay(Actor: AActor *, EndPlayReason: EEndPlayReason :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |
| `EndPlayReason` | `EEndPlayReason :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RequestStimuliListenerUpdate`

```text
RequestStimuliListenerUpdate() -> void
```

Notifies AIPerceptionSystem to update properties for this "stimuli listener"

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPerceivedHostileActors`

```text
GetPerceivedHostileActors(OutActors: TArray < AActor * > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutActors` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCurrentlyPerceivedActors`

```text
GetCurrentlyPerceivedActors(SenseToUse: TSubclassOf < UAISense >, OutActors: TArray < AActor * > &) -> void
```

If SenseToUse is none all actors currently perceived in any way will get fetched

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SenseToUse` | `TSubclassOf < UAISense >` | - |
| `OutActors` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetKnownPerceivedActors`

```text
GetKnownPerceivedActors(SenseToUse: TSubclassOf < UAISense >, OutActors: TArray < AActor * > &) -> void
```

If SenseToUse is none all actors ever perceived in any way (and not forgotten yet) will get fetched

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SenseToUse` | `TSubclassOf < UAISense >` | - |
| `OutActors` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPerceivedActors`

```text
GetPerceivedActors(SenseToUse: TSubclassOf < UAISense >, OutActors: TArray < AActor * > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SenseToUse` | `TSubclassOf < UAISense >` | - |
| `OutActors` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetActorsPerception`

```text
GetActorsPerception(Actor: AActor *, Info: FActorPerceptionBlueprintInfo &) -> bool
```

Retrieves whatever has been sensed about given actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |
| `Info` | `FActorPerceptionBlueprintInfo &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetSenseEnabled`

```text
SetSenseEnabled(SenseClass: TSubclassOf < UAISense >, bEnable: bool) -> void
```

Note that this works only if given sense has been already configured for
	 	this component instance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SenseClass` | `TSubclassOf < UAISense >` | - |
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnPerceptionUpdated`

```text
OnPerceptionUpdated(UpdatedActors: TArray<AActor*>) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UpdatedActors` | `TArray` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTargetPerceptionUpdated`

```text
OnTargetPerceptionUpdated(Actor: AActor*, Stimulus: FAIStimulus) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor*` | - |
| `Stimulus` | `FAIStimulus` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
