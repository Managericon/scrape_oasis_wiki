---
id: "api:class:UMaterialParameterCollection"
title: "UMaterialParameterCollection"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialParameterCollection.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialParameterCollection

Asset class that contains a list of parameter names and their default values. 
  Any number of materials can reference these parameters and get new values when the parameter values are changed.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StateId` | `FGuid` | Used by materials using this collection to know when to recompile. |
| `ScalarParameters` | `TArray < FCollectionScalarParameter >` | - |
| `VectorParameters` | `TArray < FCollectionVectorParameter >` | - |

## Language

`cpp`
