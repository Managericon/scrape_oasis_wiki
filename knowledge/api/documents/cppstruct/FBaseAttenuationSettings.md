---
id: "api:cppstruct:FBaseAttenuationSettings"
title: "FBaseAttenuationSettings"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FBaseAttenuationSettings.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FBaseAttenuationSettings

Base class for attenuation settings.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DistanceAlgorithm` | `EAttenuationDistanceModel` | The type of attenuation as a function of distance to use. |
| `CustomAttenuationCurve` | `FRuntimeFloatCurve` | The custom volume attenuation curve to use. |
| `AttenuationShape` | `TEnumAsByte < enum EAttenuationShape :: Type >` | The shape of the non-custom attenuation method. |
| `dBAttenuationAtMax` | `float` | The attenuation volume at maximum distance in decibels, used for natural attenuation method. |
| `AttenuationShapeExtents` | `FVector` | The dimensions to use for the attenuation shape. Interpretation of the values differ per shape. |
| `ConeOffset` | `float` | The distance back from the sound's origin to begin the cone when using the cone attenuation shape. |
| `FalloffDistance` | `float` | The distance over which volume attenuation occurs. |
