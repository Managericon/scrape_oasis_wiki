---
id: "api:class:AAudioVolume"
title: "AAudioVolume"
source: "https://developer.gp.qq.com/api/class/detail/Others/AAudioVolume.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AAudioVolume

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Priority` | `float` | Priority of this volume. In the case of overlapping volumes the one with the highest priority<br>	  is chosen. The order is undefined if two or more overlapping volumes have the same priority. |
| `bEnabled` | `uint32` | whether this volume is currently enabled and able to affect sounds |
| `Settings` | `FReverbSettings` | Reverb settings to use for this volume. |
| `AmbientZoneSettings` | `FInteriorSettings` | Interior settings used for this volume |

## Functions

### `SetPriority`

```text
SetPriority(NewPriority: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPriority` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetEnabled`

```text
SetEnabled(bNewEnabled: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetReverbSettings`

```text
SetReverbSettings(NewReverbSettings: FReverbSettings &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewReverbSettings` | `FReverbSettings &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInteriorSettings`

```text
SetInteriorSettings(NewInteriorSettings: FInteriorSettings &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewInteriorSettings` | `FInteriorSettings &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_bEnabled`

```text
OnRep_bEnabled() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
