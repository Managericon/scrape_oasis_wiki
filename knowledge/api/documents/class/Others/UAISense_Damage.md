---
id: "api:class:UAISense_Damage"
title: "UAISense_Damage"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAISense_Damage.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAISense_Damage

## Inheritance

`UAISense`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RegisteredEvents` | `TArray < FAIDamageEvent >` | - |

## Functions

### `ReportDamageEvent`

```text
ReportDamageEvent(WorldContextObject: UObject *, DamagedActor: AActor *, Instigator: AActor *, DamageAmount: float, EventLocation: FVector, HitLocation: FVector) -> void
```

EventLocation will be reported as Instigator's location at the moment of event happening

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `DamagedActor` | `AActor *` | - |
| `Instigator` | `AActor *` | - |
| `DamageAmount` | `float` | - |
| `EventLocation` | `FVector` | - |
| `HitLocation` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
