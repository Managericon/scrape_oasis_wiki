---
id: "api:class:UDeviceProfile"
title: "UDeviceProfile"
source: "https://developer.gp.qq.com/api/class/detail/Others/UDeviceProfile.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UDeviceProfile

## Inheritance

`UTextureLODSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DeviceType` | `FString` | The type of this profile, I.e. IOS, Windows, PS4 etc |
| `BaseProfileName` | `FString` | The name of the parent profile of this object |
| `Parent` | `UObject *` | The parent object of this profile, it is the object matching this DeviceType with the BaseProfileName |
| `CVars` | `TArray < FString >` | The collection of CVars which is set from this profile |

## Language

`cpp`
