---
id: "api:class:UReflectionCaptureComponent"
title: "UReflectionCaptureComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UReflectionCaptureComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UReflectionCaptureComponent

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CaptureOffsetComponent` | `UBillboardComponent *` | - |
| `ReflectionSourceType` | `EReflectionSourceType` | Indicates where to get the reflection source from. |
| `IndoorOutdoorMask` | `TEnumAsByte < EIndoorOutdoorMask >` | - |
| `Cubemap` | `UTextureCube *` | Cubemap to use for reflection if ReflectionSourceType is set to RS_SpecifiedCubemap. |
| `SourceCubemapAngle` | `float` | Angle to rotate the source cubemap when SourceType is set to SLS_SpecifiedCubemap. |
| `Brightness` | `float` | A brightness control to scale the captured scene's reflection intensity. |
| `CaptureOffset` | `FVector` | World space offset to apply before capturing. |
| `EnabledPlatform` | `EReflectionPlatform` | - |
| `StateId` | `FGuid` | - |

## Language

`cpp`
