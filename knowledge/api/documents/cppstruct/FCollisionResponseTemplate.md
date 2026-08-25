---
id: "api:cppstruct:FCollisionResponseTemplate"
title: "FCollisionResponseTemplate"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FCollisionResponseTemplate.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FCollisionResponseTemplate

Structure for collision response templates.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FName` | - |
| `CollisionEnabled` | `TEnumAsByte < ECollisionEnabled :: Type >` | - |
| `ObjectTypeName` | `FName` | - |
| `CustomResponses` | `TArray < FResponseChannel >` | Types of objects that this physics objects will collide with. |
| `HelpMessage` | `FString` | Help message for collision profile |
| `bCanModify` | `bool` | Help message for collision profile |
