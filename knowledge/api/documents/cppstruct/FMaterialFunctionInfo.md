---
id: "api:cppstruct:FMaterialFunctionInfo"
title: "FMaterialFunctionInfo"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FMaterialFunctionInfo.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FMaterialFunctionInfo

Stores information about a function that this material references, used to know when the material needs to be recompiled.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StateId` | `FGuid` | Id that the function had when this material was last compiled. |
| `Function` | `UMaterialFunction *` | The function which this material has a dependency on. |
