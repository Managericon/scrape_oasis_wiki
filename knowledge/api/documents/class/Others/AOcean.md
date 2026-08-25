---
id: "api:class:AOcean"
title: "AOcean"
source: "https://developer.gp.qq.com/api/class/detail/Others/AOcean.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AOcean

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OceanFFTComponent` | `UOceanFFTComponent *` | - |
| `OceanGerstnerComponent` | `UOceanGerstnerComponent *` | UPROPERTY(Category = Rendering, VisibleAnywhere, BlueprintReadOnly, meta = (AllowPrivateAccess = "true"))<br>	class UOceanMeshComponent OceanMeshComponent; |
| `OceanCDLODMeshComponent` | `UOceanCDLODMeshComponent *` | - |
| `Disfield` | `UTexture2D *` | - |
| `IndirectMap` | `UTexture2D *` | - |
| `DFResolutionUintNum` | `FVector2D` | baking information's(collected coastline informations) resolution is multiple of 126, texture is multiple of 128,this para record the multiples |
| `DistanceFieldParas` | `FVector4` | - |
| `bDistanceFieldinfoBaked` | `bool` | UPROPERTY(Category = DistanceField, EditAnywhere, BlueprintReadOnly, meta = (AllowPrivateAccess = "true"))<br>	float DistanceFieldBlurStep; |

## Language

`cpp`
