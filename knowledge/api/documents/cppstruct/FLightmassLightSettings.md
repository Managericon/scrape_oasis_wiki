---
id: "api:cppstruct:FLightmassLightSettings"
title: "FLightmassLightSettings"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FLightmassLightSettings.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FLightmassLightSettings

Per-light settings for Lightmass

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `IndirectLightingSaturation` | `float` | 0 will be completely desaturated, 1 will be unchanged |
| `ShadowExponent` | `float` | Controls the falloff of shadow penumbras |
| `bUseAreaShadowsForStationaryLight` | `bool` | Whether to use area shadows for stationary light precomputed shadowmaps.<br>	  Area shadows get softer the further they are from shadow casters, but require higher lightmap resolution to get the same quality where the shadow is sharp. |
