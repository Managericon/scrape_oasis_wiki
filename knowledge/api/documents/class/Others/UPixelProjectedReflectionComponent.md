---
id: "api:class:UPixelProjectedReflectionComponent"
title: "UPixelProjectedReflectionComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPixelProjectedReflectionComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPixelProjectedReflectionComponent

UPixelProjectedReflectionComponent

## Inheritance

`USceneCaptureComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PreviewBox` | `UBoxComponent *` | - |
| `NormalDistortionStrength` | `float` | Controls the strength of normals when distorting the planar reflection. |
| `SkyDistanceFadeoutStart` | `float` | Receiving pixels at this distance from the reflection plane will begin to fade out the planar reflection. |
| `SkyDistanceFadeoutEnd` | `float` | Receiving pixels at this distance from the reflection plane will have completely faded out the planar reflection. |
| `DistanceFromPlaneFadeStart_DEPRECATED` | `float` | - |
| `DistanceFromPlaneFadeEnd_DEPRECATED` | `float` | - |
| `DistanceFromPlaneFadeoutStart` | `float` | Receiving pixels at this distance from the reflection plane will begin to fade out the planar reflection. |
| `DistanceFromPlaneFadeoutEnd` | `float` | Receiving pixels at this distance from the reflection plane will have completely faded out the planar reflection. |
| `AngleFromPlaneFadeStart` | `float` | Receiving pixels whose normal is at this angle from the reflection plane will begin to fade out the planar reflection. |
| `AngleFromPlaneFadeEnd` | `float` | Receiving pixels whose normal is at this angle from the reflection plane will have completely faded out the planar reflection. |
| `HeightAdjustmentVolumes` | `TArray < APixelProjectedReflectionHeightAdjustmentVolume * >` | - |
| `VisibilityVolumes` | `TArray < APixelProjectedReflectionVisibilityVolume * >` | - |

## Language

`cpp`
