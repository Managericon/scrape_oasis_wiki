---
id: "api:cppstruct:FKSphylElem"
title: "FKSphylElem"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FKSphylElem.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FKSphylElem

Capsule shape used for collision. Z axis is capsule axis.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TM_DEPRECATED` | `FMatrix` | - |
| `Orientation_DEPRECATED` | `FQuat` | - |
| `Center` | `FVector` | Position of the capsule's origin |
| `Rotation` | `FRotator` | Rotation of the capsule |
| `Radius` | `float` | Radius of the capsule |
| `Length` | `float` | This is of line-segment ie. add Radius to both ends to find total length. |
