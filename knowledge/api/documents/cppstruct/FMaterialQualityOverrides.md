---
id: "api:cppstruct:FMaterialQualityOverrides"
title: "FMaterialQualityOverrides"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FMaterialQualityOverrides.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FMaterialQualityOverrides

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnableOverride` | `bool` | - |
| `bForceFullyRough` | `bool` | - |
| `bForceNonMetal` | `bool` | - |
| `bForceDisableLMDirectionality` | `bool` | - |
| `bForceLQReflections` | `bool` | - |
| `bHighDeviceSkipForceFullyRough` | `bool` | 仅在 ENABLE_DEVICE_LEVEL_SHADER_VARIANT 开启时生效 |
| `bHighDeviceSkipForceNonMetal` | `bool` | 仅在 ENABLE_DEVICE_LEVEL_SHADER_VARIANT 开启时生效 |
| `MobileCSMQuality` | `EMobileCSMQuality` | - |
| `MobilePointLightShadowQuality` | `EMobileCSMQuality` | - |
| `MobilePhotonShadowQuality` | `EMobileCSMQuality` | #if WITH_PHOTON_SHADOW |
