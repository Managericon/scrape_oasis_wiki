---
id: "api:cppstruct:FSubsurfaceProfileStruct"
title: "FSubsurfaceProfileStruct"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FSubsurfaceProfileStruct.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FSubsurfaceProfileStruct

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ScatterRadius` | `float` | in worldunreal units (cm) |
| `SubsurfaceColor` | `FLinearColor` | Specifies the how much of the diffuse light gets into the material,<br>	 can be seen as a per-channel mix factor between the original image,<br>	 and the SSS-filtered image (called "strength" in SeparableSSS, default there: 0.48, 0.41, 0.28) |
| `FalloffColor` | `FLinearColor` | defines the per-channel falloff of the gradients<br>	 produced by the subsurface scattering events, can be used to fine tune the color of the gradients<br>	 (called "falloff" in SeparableSSS, default there: 1, 0.37, 0.3) |
