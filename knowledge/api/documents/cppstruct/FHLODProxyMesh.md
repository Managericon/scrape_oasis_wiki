---
id: "api:cppstruct:FHLODProxyMesh"
title: "FHLODProxyMesh"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FHLODProxyMesh.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FHLODProxyMesh

A mesh proxy entry

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LODActor` | `TLazyObjectPtr < ALODActor >` | The ALODActor that we were generated from |
| `StaticMesh` | `UStaticMesh *` | The mesh used to display this proxy |
| `Key` | `FName` | The key generated from an ALODActor. If this differs from that generated from the ALODActor, then the mesh needs regenerating. |
