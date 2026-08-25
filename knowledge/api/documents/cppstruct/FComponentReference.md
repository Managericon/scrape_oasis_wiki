---
id: "api:cppstruct:FComponentReference"
title: "FComponentReference"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FComponentReference.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FComponentReference

Struct that allows for different ways to reference a component.
 	If just an Actor is specified, will return RootComponent of that Actor.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OtherActor` | `AActor *` | Pointer to a different Actor that owns the Component. |
| `ComponentProperty` | `FName` | Name of component property to use |
