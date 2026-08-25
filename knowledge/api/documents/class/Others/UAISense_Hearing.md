---
id: "api:class:UAISense_Hearing"
title: "UAISense_Hearing"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAISense_Hearing.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAISense_Hearing

## Inheritance

`UAISense`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NoiseEvents` | `TArray < FAINoiseEvent >` | - |
| `SpeedOfSoundSq` | `float` | Defaults to 0 to have instant notification. Setting to > 0 will result in delaying <br>	 	when AI hears the sound based on the distance from the source |

## Functions

### `ReportNoiseEvent`

```text
ReportNoiseEvent(WorldContextObject: UObject *, NoiseLocation: FVector, Loudness: float, Instigator: AActor *, MaxRange: float, Tag: FName) -> void
```

Report a noise event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `NoiseLocation` | `FVector` | Location of the noise. |
| `Loudness` | `float` | Loudness of the noise. If MaxRange is non-zero, modifies MaxRange, otherwise modifies the squared distance of the sensor's range. |
| `Instigator` | `AActor *` | Actor that triggered the noise. |
| `MaxRange` | `float` | Max range at which the sound can be heard, multiplied by Loudness. Values <= 0 mean no limit (still limited by listener's range however). |
| `Tag` | `FName` | Identifier for the event. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
