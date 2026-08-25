---
id: "api:cppstruct:FBPVariableDescription"
title: "FBPVariableDescription"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FBPVariableDescription.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FBPVariableDescription

Struct indicating a variable in the generated class

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VarName` | `FName` | Name of the variable |
| `VarGuid` | `FGuid` | A Guid that will remain constant even if the VarName changes |
| `VarType` | `FEdGraphPinType` | Type of the variable |
| `FriendlyName` | `FString` | Friendly name of the variable |
| `Category` | `FText` | Category this variable should be in |
| `PropertyFlags` | `uint64` | Property flags for this variable - Changed from int32 to uint64 |
| `RepNotifyFunc` | `FName` | - |
| `ReplicationCondition` | `TEnumAsByte < ELifetimeCondition >` | - |
| `MetaDataArray` | `TArray < struct FBPVariableMetaDataEntry >` | Metadata information for this variable |
| `DefaultValue` | `FString` | Optional new default value stored as string |
