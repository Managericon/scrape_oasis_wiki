---
id: "api:cppstruct:FLevelSequenceBindingReferences"
title: "FLevelSequenceBindingReferences"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FLevelSequenceBindingReferences.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FLevelSequenceBindingReferences

Structure that stores a one to many mapping from object binding ID, to object references that pertain to that ID.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BindingIdToReferences` | `TMap < FGuid , FLevelSequenceBindingReferenceArray >` | The map from object binding ID to an array of references that pertain to that ID |
