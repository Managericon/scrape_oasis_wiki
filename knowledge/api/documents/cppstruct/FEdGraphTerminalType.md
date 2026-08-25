---
id: "api:cppstruct:FEdGraphTerminalType"
title: "FEdGraphTerminalType"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FEdGraphTerminalType.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FEdGraphTerminalType

Struct used to define information for terminal types, e.g. types that can be contained
   by a container. Currently can represent strongweak references to a type (only UObjects), 
   a structure, or a primitive. Support for "Container of Containers" is done by wrapping 
   a structure, rather than implicitly defining names for containers.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TerminalCategory` | `FString` | Category |
| `TerminalSubCategory` | `FString` | Sub-category |
| `TerminalSubCategoryObject` | `TWeakObjectPtr < UObject >` | Sub-category object |
| `bTerminalIsConst` | `bool` | Whether or not this pin is a immutable const value |
| `bTerminalIsWeakPointer` | `bool` | Whether or not this is a weak reference |
