---
id: "api:cppstruct:FCollectionParameterBase"
title: "FCollectionParameterBase"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FCollectionParameterBase.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FCollectionParameterBase

Base struct for collection parameters

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | The name of the parameter.  Changing this name will break any blueprints that reference the parameter. |
| `Id` | `FGuid` | Uniquely identifies the parameter, used for fixing up materials that reference this parameter when renaming. |
