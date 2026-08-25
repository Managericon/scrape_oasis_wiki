---
id: "api:class:AEmitterCameraLensEffectBase"
title: "AEmitterCameraLensEffectBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/AEmitterCameraLensEffectBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AEmitterCameraLensEffectBase

## Inheritance

`AEmitter`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PS_CameraEffect` | `UParticleSystem *` | Particle System to use |
| `PS_CameraEffectNonExtremeContent_DEPRECATED` | `UParticleSystem *` | The effect to use for non extreme content |
| `BaseCamera` | `APlayerCameraManager *` | Camera this emitter is attached to, will be notified when emitter is destroyed |
| `RelativeTransform` | `FTransform` | Effect-to-camera transform to allow arbitrary placement of the particle system .<br>	  Note the X component of the location will be scaled with camera fov to keep the lens effect the same apparent size. |
| `BaseFOV` | `float` | This is the assumed FOV for which the effect was authored. The code will make automatic adjustments to make it look the same at different FOVs |
| `bAllowMultipleInstances` | `uint8` | true if multiple instances of this emitter can exist simultaneously, false otherwise. |
| `bResetWhenRetriggered` | `uint8` | If bAllowMultipleInstances is true and this effect is retriggered, the particle system will be reset if this is true |
| `EmittersToTreatAsSame` | `TArray < TSubclassOf < AEmitterCameraLensEffectBase > >` | If an emitter class in this array is currently playing, do not play this effect.<br>	   Useful for preventing multiple similar or expensive camera effects from playing simultaneously. |
| `DistFromCamera_DEPRECATED` | `float` | DEPRECATED(4.11) |

## Language

`cpp`
