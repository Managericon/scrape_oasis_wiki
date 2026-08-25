---
id: "api:class:UObjectLibrary"
title: "UObjectLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UObjectLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UObjectLibrary

Class that holds a library of Objects

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ObjectBaseClass` | `UClass *` | Class that Objects must be of. If ContainsBlueprints is true, this is the native class that the blueprints are instances of and not UClass |
| `bHasBlueprintClasses` | `bool` | True if this library holds blueprint classes, false if it holds other objects |
| `Objects` | `TArray < UObject * >` | List of Objects in library |
| `WeakObjects` | `TArray < TWeakObjectPtr < UObject > >` | Weak pointers to objects |
| `bUseWeakReferences` | `bool` | If this library should use weak pointers |
| `bIsFullyLoaded` | `bool` | True if we've already fully loaded this library, can't do it twice |

## Language

`cpp`
