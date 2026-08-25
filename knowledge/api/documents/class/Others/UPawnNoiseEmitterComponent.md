---
id: "api:class:UPawnNoiseEmitterComponent"
title: "UPawnNoiseEmitterComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPawnNoiseEmitterComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPawnNoiseEmitterComponent

PawnNoiseEmitterComponent tracks noise event data used by SensingComponents to hear a Pawn.
  This component is intended to exist on either a Pawn or its Controller. It does nothing on network clients.

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bAIPerceptionSystemCompatibilityMode` | `uint32` | - |
| `LastRemoteNoisePosition` | `FVector` | - |
| `NoiseLifetime` | `float` | - |
| `LastRemoteNoiseVolume` | `float` | - |
| `LastRemoteNoiseTime` | `float` | - |
| `LastLocalNoiseVolume` | `float` | - |
| `LastLocalNoiseTime` | `float` | - |

## Functions

### `MakeNoise`

```text
MakeNoise(NoiseMaker: AActor *, Loudness: float, NoiseLocation: FVector &) -> void
```

Cache noises instigated by the owning pawn for AI sensing

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NoiseMaker` | `AActor *` | - is the actual actor which made the noise |
| `Loudness` | `float` | - is the relative loudness of the noise (0.0 to 1.0) |
| `NoiseLocation` | `FVector &` | - is the position of the noise |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
