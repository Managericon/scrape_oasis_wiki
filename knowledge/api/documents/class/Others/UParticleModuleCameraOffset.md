---
id: "api:class:UParticleModuleCameraOffset"
title: "UParticleModuleCameraOffset"
source: "https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleCameraOffset.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UParticleModuleCameraOffset

## Inheritance

`UParticleModuleCameraBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CameraOffset` | `FRawDistributionFloat` | The camera-relative offset to apply to sprite location |
| `bSpawnTimeOnly` | `uint32` | If true, the offset will only be processed at spawn time |
| `UpdateMethod` | `TEnumAsByte < enum EParticleCameraOffsetUpdateMethod >` | How to update the offset for this module.<br>	  DirectSet - Set the value directly (overwrite any previous setting)<br>	  Additive  - Add the offset of this module to the existing offset<br>	  Scalar    - Scale the existing offset by the value of this module |

## Language

`cpp`
