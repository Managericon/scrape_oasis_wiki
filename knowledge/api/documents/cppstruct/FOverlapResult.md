---
id: "api:cppstruct:FOverlapResult"
title: "FOverlapResult"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FOverlapResult.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FOverlapResult

Structure containing information about one hit of an overlap test

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Actor` | `TWeakObjectPtr < AActor >` | Actor that the check hit. |
| `Component` | `TWeakObjectPtr < UPrimitiveComponent >` | PrimitiveComponent that the check hit. |
| `bBlockingHit` | `uint32` | Indicates if this hit was requesting a block - if false, was requesting a touch instead |
