---
id: "api:class:UAISenseConfig_Sight"
title: "UAISenseConfig_Sight"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAISenseConfig_Sight.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAISenseConfig_Sight

## Inheritance

`UAISenseConfig`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Implementation` | `TSubclassOf < UAISense_Sight >` | - |
| `SightRadius` | `float` | Maximum sight distance to notice a target. |
| `LoseSightRadius` | `float` | Maximum sight distance to see target that has been already seen. |
| `PeripheralVisionAngleDegrees` | `float` | How far to the side AI can see, in degrees. Use SetPeripheralVisionAngle to change the value at runtime. <br>	 	The value represents the angle measured in relation to the forward vector, not the whole range. |
| `DetectionByAffiliation` | `FAISenseAffiliationFilter` | - |
| `AutoSuccessRangeFromLastSeenLocation` | `float` | If not an InvalidRange (which is the default), we will always be able to see the target that has already been seen if they are within this range of their last seen location. |

## Language

`cpp`
