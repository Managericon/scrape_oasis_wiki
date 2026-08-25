---
id: "api:cppstruct:FRepAttachment"
title: "FRepAttachment"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FRepAttachment.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FRepAttachment

Handles attachment replication to clients. Movement replication will not happen while AttachParent is non-nullptr

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AttachParent` | `AActor *` | - |
| `LocationOffset` | `FVector_NetQuantize100` | - |
| `RelativeScale3D` | `FVector_NetQuantize100` | - |
| `RotationOffset` | `FRotator` | - |
| `AttachSocket` | `FName` | - |
| `AttachComponent` | `USceneComponent *` | - |
| `AttachParent_Direct` | `AActor *` | - |
| `bHasValidParent` | `bool` | - |
