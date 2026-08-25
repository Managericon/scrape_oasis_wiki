---
id: "api:class:UAIPerceptionSystem"
title: "UAIPerceptionSystem"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAIPerceptionSystem.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAIPerceptionSystem

By design checks perception between hostile teams

## Inheritance

`UObject` -> `FTickableGameObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Senses` | `TArray < UAISense * >` | - |
| `PerceptionAgingRate` | `float` | - |

## Functions

### `ReportEvent`

```text
ReportEvent(PerceptionEvent: UAISenseEvent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PerceptionEvent` | `UAISenseEvent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReportPerceptionEvent`

```text
ReportPerceptionEvent(WorldContextObject: UObject *, PerceptionEvent: UAISenseEvent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PerceptionEvent` | `UAISenseEvent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RegisterPerceptionStimuliSource`

```text
RegisterPerceptionStimuliSource(WorldContextObject: UObject *, Sense: TSubclassOf < UAISense >, Target: AActor *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Sense` | `TSubclassOf < UAISense >` | - |
| `Target` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetSenseClassForStimulus`

```text
GetSenseClassForStimulus(WorldContextObject: UObject *, Stimulus: FAIStimulus &) -> TSubclassOf < UAISense >
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Stimulus` | `FAIStimulus &` | - |

**Returns**

| Type | Description |
|---|---|
| `TSubclassOf < UAISense >` | - |

### `OnPerceptionStimuliSourceEndPlay`

```text
OnPerceptionStimuliSourceEndPlay(Actor: AActor *, EndPlayReason: EEndPlayReason :: Type) -> void
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

## Language

`cpp`
