---
id: "api:cppstruct:FLevelSequenceObject"
title: "FLevelSequenceObject"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FLevelSequenceObject.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FLevelSequenceObject

Structure for animated Actor objects.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ObjectOrOwner` | `TLazyObjectPtr < UObject >` | The object or the owner of the object being possessed. |
| `ComponentName` | `FString` | Optional name of an ActorComponent. |
| `CachedComponent` | `TWeakObjectPtr < UObject >` | Cached pointer to the Actor component (only if ComponentName is set). |
