---
id: "api:class:AAmbientSound"
title: "AAmbientSound"
source: "https://developer.gp.qq.com/api/class/detail/Others/AAmbientSound.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AAmbientSound

A sound actor that can be placed in a level

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AudioComponent` | `UAudioComponent *` | Audio component that handles sound playing |

## Functions

### `FadeIn`

```text
FadeIn(FadeInDuration: float, FadeVolumeLevel: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FadeInDuration` | `float` | - |
| `FadeVolumeLevel` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FadeOut`

```text
FadeOut(FadeOutDuration: float, FadeVolumeLevel: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FadeOutDuration` | `float` | - |
| `FadeVolumeLevel` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AdjustVolume`

```text
AdjustVolume(AdjustVolumeDuration: float, AdjustVolumeLevel: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AdjustVolumeDuration` | `float` | - |
| `AdjustVolumeLevel` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Play`

```text
Play(StartTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Stop`

```text
Stop() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
