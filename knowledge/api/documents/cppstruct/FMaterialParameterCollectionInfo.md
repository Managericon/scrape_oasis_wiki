---
id: "api:cppstruct:FMaterialParameterCollectionInfo"
title: "FMaterialParameterCollectionInfo"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FMaterialParameterCollectionInfo.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FMaterialParameterCollectionInfo

Stores information about a parameter collection that this material references, used to know when the material needs to be recompiled.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StateId` | `FGuid` | Id that the collection had when this material was last compiled. |
| `ParameterCollection` | `UMaterialParameterCollection *` | The collection which this material has a dependency on. |
