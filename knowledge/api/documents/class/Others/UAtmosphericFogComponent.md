---
id: "api:class:UAtmosphericFogComponent"
title: "UAtmosphericFogComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAtmosphericFogComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAtmosphericFogComponent

Used to create fogging effects such as clouds.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SunMultiplier` | `float` | Global scattering factor. |
| `FogMultiplier` | `float` | Scattering factor on object. |
| `DensityMultiplier` | `float` | Fog density control factor. |
| `DensityOffset` | `float` | Fog density offset to control opacity [-1.f ~ 1.f]. |
| `DistanceScale` | `float` | Distance scale. |
| `AltitudeScale` | `float` | Altitude scale (only Z scale). |
| `DistanceOffset` | `float` | Distance offset, in km (to handle large distance) |
| `GroundOffset` | `float` | Ground offset. |
| `StartDistance` | `float` | Start Distance. |
| `SunDiscScale` | `float` | Distance offset, in km (to handle large distance) |
| `DefaultBrightness` | `float` | Default light brightness. Used when there is no sunlight placed in the level. Unit is lumens |
| `DefaultLightColor` | `FColor` | Default light color. Used when there is no sunlight placed in the level. |
| `bDisableSunDisk` | `uint32` | Disable Sun Disk rendering. |
| `bDisableGroundScattering` | `uint32` | Disable Color scattering from ground. |
| `PrecomputeParams` | `FAtmospherePrecomputeParameters` | - |
| `TransmittanceTexture_DEPRECATED` | `UTexture2D *` | - |
| `IrradianceTexture_DEPRECATED` | `UTexture2D *` | - |

## Functions

### `SetDefaultBrightness`

```text
SetDefaultBrightness(NewBrightness: float) -> ENGINE_API void
```

Set brightness of the light

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewBrightness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetDefaultLightColor`

```text
SetDefaultLightColor(NewLightColor: FLinearColor) -> ENGINE_API void
```

Set color of the light

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetSunMultiplier`

```text
SetSunMultiplier(NewSunMultiplier: float) -> ENGINE_API void
```

Set SunMultiplier

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewSunMultiplier` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetFogMultiplier`

```text
SetFogMultiplier(NewFogMultiplier: float) -> ENGINE_API void
```

Set FogMultiplier

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewFogMultiplier` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetDensityMultiplier`

```text
SetDensityMultiplier(NewDensityMultiplier: float) -> ENGINE_API void
```

Set DensityMultiplier

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewDensityMultiplier` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetDensityOffset`

```text
SetDensityOffset(NewDensityOffset: float) -> ENGINE_API void
```

Set DensityOffset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewDensityOffset` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetDistanceScale`

```text
SetDistanceScale(NewDistanceScale: float) -> ENGINE_API void
```

Set DistanceScale

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewDistanceScale` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetAltitudeScale`

```text
SetAltitudeScale(NewAltitudeScale: float) -> ENGINE_API void
```

Set AltitudeScale

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAltitudeScale` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetStartDistance`

```text
SetStartDistance(NewStartDistance: float) -> ENGINE_API void
```

Set StartDistance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewStartDistance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetDistanceOffset`

```text
SetDistanceOffset(NewDistanceOffset: float) -> ENGINE_API void
```

Set DistanceOffset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewDistanceOffset` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `DisableSunDisk`

```text
DisableSunDisk(NewSunDisk: bool) -> ENGINE_API void
```

Set DisableSunDisk

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewSunDisk` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `DisableGroundScattering`

```text
DisableGroundScattering(NewGroundScattering: bool) -> ENGINE_API void
```

Set DisableGroundScattering

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewGroundScattering` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetPrecomputeParams`

```text
SetPrecomputeParams(DensityHeight: float, MaxScatteringOrder: int32, InscatterAltitudeSampleNum: int32) -> ENGINE_API void
```

Set PrecomputeParams, only valid in Editor mode

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DensityHeight` | `float` | - |
| `MaxScatteringOrder` | `int32` | - |
| `InscatterAltitudeSampleNum` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `StartPrecompute`

```text
StartPrecompute() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
