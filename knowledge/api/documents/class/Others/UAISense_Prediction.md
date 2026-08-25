---
id: "api:class:UAISense_Prediction"
title: "UAISense_Prediction"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAISense_Prediction.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAISense_Prediction

## Inheritance

`UAISense`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RegisteredEvents` | `TArray < FAIPredictionEvent >` | - |

## Functions

### `RequestControllerPredictionEvent`

```text
RequestControllerPredictionEvent(Requestor: AAIController *, PredictedActor: AActor *, PredictionTime: float) -> void
```

Asks perception system to supply Requestor with PredictedActor's predicted location in PredictionTime seconds
	 	Location is being predicted based on PredicterActor's current location and velocity

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Requestor` | `AAIController *` | - |
| `PredictedActor` | `AActor *` | - |
| `PredictionTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RequestPawnPredictionEvent`

```text
RequestPawnPredictionEvent(Requestor: APawn *, PredictedActor: AActor *, PredictionTime: float) -> void
```

Asks perception system to supply Requestor with PredictedActor's predicted location in PredictionTime seconds
	 	Location is being predicted based on PredicterActor's current location and velocity

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Requestor` | `APawn *` | - |
| `PredictedActor` | `AActor *` | - |
| `PredictionTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
