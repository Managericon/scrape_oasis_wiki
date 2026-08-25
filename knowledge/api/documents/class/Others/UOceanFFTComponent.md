---
id: "api:class:UOceanFFTComponent"
title: "UOceanFFTComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UOceanFFTComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UOceanFFTComponent

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DisTexture` | `UTextureRenderTarget2D *` | - |
| `NormalMapTexture` | `UTextureRenderTarget2D *` | - |
| `FFTGridSize` | `int32` | Size of grid for FFT |
| `WaveAmplitude` | `float` | - |
| `FetchLength` | `float` | - |
| `WaveSwell` | `float` | - |
| `WindSpeed` | `FVector2D` | - |
| `SamplePatch` | `FVector2D` | - |
| `WaveSpeed` | `float` | Speed of time for FFT |
| `XYDisplaceFactor` | `float` | - |
| `JacobianFactor` | `float` | - |
| `FoamDissipationSpeed` | `float` | - |
| `FoamFalloffSpeed` | `float` | - |
| `FoamGenerationAmount` | `float` | - |
| `FoamGenerationThreshold` | `float` | - |
| `DisplaceTextureArray` | `TArray < UTexture2D * >` | - |
| `NormalTextureArray` | `TArray < UTexture2D * >` | - |
| `Frameinterval` | `int` | - |
| `FrameNum` | `int32` | - |
| `UpdateNeeded` | `bool` | - |
| `DisRTArray` | `TArray < UTextureRenderTarget2D * >` | - |
| `NormalRTArray` | `TArray < UTextureRenderTarget2D * >` | - |

## Functions

### `Update`

```text
Update(DeltaTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
