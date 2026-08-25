---
id: "api:class:ACullDistanceVolume"
title: "ACullDistanceVolume"
source: "https://developer.gp.qq.com/api/class/detail/Others/ACullDistanceVolume.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ACullDistanceVolume

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CullDistances` | `TArray < struct FCullDistanceSizePair >` | Array of size and cull distance pairs. The code will calculate the sphere diameter of a primitive's BB and look for a best<br>	  fit in this array to determine which cull distance to use. |
| `bEnabled` | `uint32` | Whether the volume is currently enabled or not. |
| `bEnabledDeviceScale` | `uint32` | - |
| `VeryLowScale` | `float` | - |
| `LowScale` | `float` | - |
| `MidScale` | `float` | - |
| `HighScale` | `float` | - |

## Language

`cpp`
