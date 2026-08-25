---
id: "api:cppstruct:FPropertyPathSegment"
title: "FPropertyPathSegment"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FPropertyPathSegment.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FPropertyPathSegment

A struct used for caching part of a property path.  Don't use this class directly.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FName` | The sub-component of the property path, a single value between .'s of the path |
| `ArrayIndex` | `int32` | The optional array index. |
| `Struct` | `UStruct *` | The cached Class or ScriptStruct that was used last to resolve Name to a property. |
| `Field` | `UField *` | The cached property on the Struct that this Name resolved to on it last time Resolve was called, if <br>	  the Struct doesn't change, this value is returned to avoid performing another Field lookup. |
