---
id: "api:class:UOceanCDLODMeshComponent"
title: "UOceanCDLODMeshComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UOceanCDLODMeshComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UOceanCDLODMeshComponent

## Inheritance

`UMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CDLODMeshOverrideMaterial` | `UMaterialInterface *` | The material used to rendering ocean |
| `MaxViewDistance` | `float` | - |
| `MaxCDLODDistance` | `float` | - |
| `LODDistanceRatio` | `float` | - |
| `LOD0Size` | `float` | - |
| `LODCount` | `int32` | - |
| `WaveFadeDistance` | `float` | . amplitude of wave have to fade as 0 for edge quads,this is the fade radius |
| `SeaLevel` | `float` | - |
| `Occlusioncoff` | `float` | - |
| `FFTSampleCount` | `int32` | - |
| `FFTSampleSize` | `float` | . FFT texture sampled by world position, used as  normalize sample position |
| `FFTFoamBlurNormalZ` | `FVector2D` | . X influence the foam shape<br>	. Y : Z of normal vector of FFT wave, at this moment this normal vector haven't be normalize, after z setted, normal vector will be normalized |
| `GerstnerFFTSoftness` | `FVector2D` | GerstnerFFTSoftness holds two waves blend factor in near sea<br>	 .X is Gerstner blend factor, if bigger than 1, wave fade rapidly<br>	 .Y is FFT blend factor, if smaller than 1, wave fade slowly |
| `GridSize` | `int32` | UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = OCeanCDLODMesh) |
| `ShapeUniformValue` | `TArray < int32 >` | - |

## Language

`cpp`
