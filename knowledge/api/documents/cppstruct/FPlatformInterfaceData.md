---
id: "api:cppstruct:FPlatformInterfaceData"
title: "FPlatformInterfaceData"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FPlatformInterfaceData.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FPlatformInterfaceData

Struct that encompasses the most common types of data. This is the data payload
  of PlatformInterfaceDelegateResult.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DataName` | `FName` | An optional tag for this data |
| `Type` | `TEnumAsByte < enum EPlatformInterfaceDataType >` | Specifies which value is valid for this structure |
| `IntValue` | `int32` | Various typed result values |
| `FloatValue` | `float` | - |
| `StringValue` | `FString` | - |
| `ObjectValue` | `UObject *` | - |
