---
id: "api:cppstruct:FGroupedTagEntry"
title: "FGroupedTagEntry"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FGroupedTagEntry.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FGroupedTagEntry

Grouped Tag Entry - Stores tags for a single category group

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GroupName` | `FName` | Group name (e.g. "StreamingType", "LODLevel") |
| `Tags` | `TArray < FName >` | Tags in this group |
| `bOverrideStaticMeshTags` | `bool` | Component-local flag: this group overrides the same StaticMesh tag group, even when Tags is empty. |
