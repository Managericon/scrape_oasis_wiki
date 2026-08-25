---
id: "api:class:UPawnSensingComponent"
title: "UPawnSensingComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPawnSensingComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPawnSensingComponent

SensingComponent encapsulates sensory (ie sight and hearing) settings and functionality for an Actor,
  allowing the actor to seehear Pawns in the world. It does nothing on network clients.

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `HearingThreshold` | `float` | Max distance at which a makenoise(1.0) loudness sound can be heard, regardless of occlusion |
| `LOSHearingThreshold` | `float` | Max distance at which a makenoise(1.0) loudness sound can be heard if unoccluded (LOSHearingThreshold should be > HearingThreshold) |
| `SightRadius` | `float` | Maximum sight distance. |
| `SensingInterval` | `float` | Amount of time between pawn sensing updates. Use SetSensingInterval() to adjust this at runtime. A value <= 0 prevents any updates. |
| `HearingMaxSoundAge` | `float` | - |
| `bEnableSensingUpdates` | `uint32` | If true, component will perform sensing updates. At runtime change this using SetSensingUpdatesEnabled(). |
| `bOnlySensePlayers` | `uint32` | If true, will only sense player-controlled pawns in the world. Default: true |
| `bSeePawns` | `uint32` | If true, we will perform visibility tests and will trigger notifications when a Pawn is visible. Default: true |
| `bHearNoises` | `uint32` | If true, we will perform audibility tests and will be notified when a Pawn makes a noise that can be heard. Default: true<br>	  IMPORTANT NOTE: If we can see pawns (bSeePawns is true), and the pawn is visible, noise notifications are not triggered. |
| `PeripheralVisionAngle` | `float` | How far to the side AI can see, in degrees. Use SetPeripheralVisionAngle to change the value at runtime. |
| `PeripheralVisionCosine` | `float` | Cosine of limits of peripheral vision. Computed from PeripheralVisionAngle. |

## Functions

### `SetSensingInterval`

```text
SetSensingInterval(NewSensingInterval: float) -> void
```

Changes the SensingInterval.
	  If we are currently waiting for an interval, this can either extend or shorten that interval.
	  A value <= 0 prevents any updates.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewSensingInterval` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSensingUpdatesEnabled`

```text
SetSensingUpdatesEnabled(bEnabled: bool) -> void
```

Enables or disables sensing updates. The timer is reset in either case.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPeripheralVisionAngle`

```text
SetPeripheralVisionAngle(NewPeripheralVisionAngle: float) -> void
```

Sets PeripheralVisionAngle. Calculates PeripheralVisionCosine from PeripheralVisionAngle

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPeripheralVisionAngle` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPeripheralVisionAngle`

```text
GetPeripheralVisionAngle() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetPeripheralVisionCosine`

```text
GetPeripheralVisionCosine() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

## Delegates

### `OnSeePawn`

```text
OnSeePawn(Pawn: APawn*) -> void
```

Delegate to execute when we see a Pawn.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Pawn` | `APawn*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnHearNoise`

```text
OnHearNoise(Instigator: APawn*, Location: const FVector&, Volume: float) -> void
```

Delegate to execute when we hear a noise from a Pawn's PawnNoiseEmitterComponent.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Instigator` | `APawn*` | - |
| `Location` | `const FVector&` | - |
| `Volume` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
