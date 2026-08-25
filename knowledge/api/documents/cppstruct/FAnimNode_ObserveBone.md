---
id: "api:cppstruct:FAnimNode_ObserveBone"
title: "FAnimNode_ObserveBone"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_ObserveBone.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_ObserveBone

Debugging node that displays the current value of a bone in a specific space.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneToObserve` | `FBoneReference` | Name of bone to observe. |
| `DisplaySpace` | `TEnumAsByte < EBoneControlSpace >` | Reference frame to display the bone transform in. |
| `bRelativeToRefPose` | `bool` | Show the difference from the reference pose? |
| `Translation` | `FVector` | Translation of the bone being observed. |
| `Rotation` | `FRotator` | Rotation of the bone being observed. |
| `Scale` | `FVector` | Scale of the bone being observed. |
