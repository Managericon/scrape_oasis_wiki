---
id: "api:class:UHLODProxy"
title: "UHLODProxy"
source: "https://developer.gp.qq.com/api/class/detail/Others/UHLODProxy.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UHLODProxy

This asset acts as a proxy to a static mesh for ALODActors to display

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ProxyMeshes` | `TArray < FHLODProxyMesh >` | All the mesh proxies we contain |
| `OwningMap` | `TSoftObjectPtr < UWorld >` | Keep hold of the level in the editor to allow for package cleaning etc. |

## Language

`cpp`
