---
id: "api:cppstruct:FDebugDisplayProperty"
title: "FDebugDisplayProperty"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FDebugDisplayProperty.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FDebugDisplayProperty

Debug property display functionality to interact with this, use "display", "displayall", "displayclear"
 
  @see UGameViewportClient
  @see FDebugDisplayProperty
  @see DrawStatsHUD

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Obj` | `UObject *` | the object whose property to display. If this is a class, all objects of that class are drawn. |
| `WithinClass` | `TSubclassOf < UObject >` | if Obj is a class and WithinClass is not nullptr, further limit the display to objects that have an Outer of WithinClass |
