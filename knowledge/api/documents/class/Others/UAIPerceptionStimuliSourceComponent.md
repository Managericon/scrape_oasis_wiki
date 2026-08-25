---
id: "api:class:UAIPerceptionStimuliSourceComponent"
title: "UAIPerceptionStimuliSourceComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAIPerceptionStimuliSourceComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAIPerceptionStimuliSourceComponent

Gives owning actor a way to auto-register as perception system's sense stimuli source

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bAutoRegisterAsSource` | `uint32` | - |
| `RegisterAsSourceForSenses` | `TArray < TSubclassOf < UAISense > >` | - |

## Functions

### `RegisterWithPerceptionSystem`

```text
RegisterWithPerceptionSystem() -> void
```

Registers owning actor as source of stimuli for senses specified in RegisterAsSourceForSenses. 
	 	Note that you don't have to do it if bAutoRegisterAsSource == true

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RegisterForSense`

```text
RegisterForSense(SenseClass: TSubclassOf < UAISense >) -> void
```

Registers owning actor as source for specified sense class

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SenseClass` | `TSubclassOf < UAISense >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnregisterFromPerceptionSystem`

```text
UnregisterFromPerceptionSystem() -> void
```

Unregister owning actor from being a source of sense stimuli

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnregisterFromSense`

```text
UnregisterFromSense(SenseClass: TSubclassOf < UAISense >) -> void
```

Unregisters owning actor from sources list of a specified sense class

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SenseClass` | `TSubclassOf < UAISense >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
