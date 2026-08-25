---
id: "api:cppstruct:FSimplygonRemeshingSettings"
title: "FSimplygonRemeshingSettings"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FSimplygonRemeshingSettings.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FSimplygonRemeshingSettings

Settings used to ProxyLOD mesh(es).

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bActive` | `bool` | - |
| `ScreenSize` | `int32` | Screen size of the resulting proxy mesh in pixel size |
| `bRecalculateNormals` | `bool` | Should Simplygon recalculate normals for the proxy mesh? |
| `HardAngleThreshold` | `float` | Angle at which a hard edge is introduced between faces. |
| `MergeDistance` | `int32` | - |
| `bUseClippingPlane` | `bool` | - |
| `ClippingLevel` | `float` | - |
| `AxisIndex` | `int32` | - |
| `bPlaneNegativeHalfspace` | `bool` | - |
| `bUseMassiveLOD` | `bool` | - |
| `bUseAggregateLOD` | `bool` | - |
| `MaterialLODSettings` | `FSimplygonMaterialLODSettings` | - |
