---
id: "api:class:UAtmosphericSkyBoxComponent"
title: "UAtmosphericSkyBoxComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAtmosphericSkyBoxComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAtmosphericSkyBoxComponent

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RenderDynamicSky` | `bool` | - |
| `Material` | `UMaterialInterface *` | - |
| `NoiseTexture` | `UTexture2D *` | - |
| `StaticMesh` | `UStaticMesh *` | - |
| `RadiusScale` | `float` | - |
| `MeshRotation` | `FRotator` | - |
| `RainyDegree` | `float` | - |
| `Atmosphere` | `FTOD_AtmosphereParameters` | - |
| `Day` | `FTOD_DayParameters` | - |
| `Light` | `FTOD_LightParameters` | - |
| `CloudsPbr` | `FTOD_CloudPBRParameters` | - |
| `World` | `FTOD_WorldParameters` | - |
| `Cycle` | `FTOD_CycleParameters` | - |
| `TodTime` | `FTOD_Time` | - |
| `TodAnimation` | `FTOD_Animation` | - |
| `TodSunParams` | `FTOD_Sun` | - |
| `TodMoonParams` | `FTOD_Moon` | - |
| `TodSunAndMoonParams` | `FTOD_SunAndMoon` | - |
| `TodStarsParams` | `FTOD_Stars` | - |
| `TodSpecialSkyParams` | `FTOD_SpecialSky` | - |
| `SunActor` | `AActor *` | - |
| `MoonActor` | `AActor *` | - |
| `LightingChannels` | `FLightingChannels` | - |
| `MaterialInstancesDynamic` | `UMaterialInstanceDynamic *` | - |
| `bIsMaterialInstanceDirty` | `bool` | - |
| `FixedTimeOfDay` | `bool` | - |
| `FixedCurrTime` | `float` | - |
| `bNeedUpdate` | `bool` | - |

## Functions

### `SetFixedCurrTime`

```text
SetFixedCurrTime(time: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `time` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFixedTimeOfDay`

```text
SetFixedTimeOfDay(IsFiexd: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsFiexd` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNeedUpdate`

```text
SetNeedUpdate(NeedUpdate: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NeedUpdate` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMaterialInstancesDynamic`

```text
GetMaterialInstancesDynamic() -> UMaterialInstanceDynamic *
```

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | - |

## Language

`cpp`
