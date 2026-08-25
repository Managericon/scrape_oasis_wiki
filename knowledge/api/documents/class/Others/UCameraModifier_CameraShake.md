---
id: "api:class:UCameraModifier_CameraShake"
title: "UCameraModifier_CameraShake"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCameraModifier_CameraShake.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UCameraModifier_CameraShake

A UCameraModifier_CameraShake is a camera modifier that can apply a UCameraShake to 
  the owning camera.

## Inheritance

`UCameraModifier`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActiveShakes` | `TArray < UCameraShake * >` | List of active CameraShake instances |
| `SplitScreenShakeScale` | `float` | Scaling factor applied to all camera shakes in when in splitscreen mode. Normally used to reduce shaking, since shakes feel more intense in a smaller viewport. |
| `CacheShakeInsMap` | `TMap < TSubclassOf < UCameraShake > , FCacheCameraShakeData >` | - |

## Language

`cpp`
