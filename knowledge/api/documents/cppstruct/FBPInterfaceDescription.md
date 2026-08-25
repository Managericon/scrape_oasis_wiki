---
id: "api:cppstruct:FBPInterfaceDescription"
title: "FBPInterfaceDescription"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FBPInterfaceDescription.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FBPInterfaceDescription

Struct containing information about what interfaces are implemented in this blueprint

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Interface` | `TSubclassOf < UInterface >` | Reference to the interface class we're adding to this blueprint |
| `Graphs` | `TArray < UEdGraph * >` | References to the graphs associated with the required functions for this interface |
