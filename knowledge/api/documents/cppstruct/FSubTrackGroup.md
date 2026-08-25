---
id: "api:cppstruct:FSubTrackGroup"
title: "FSubTrackGroup"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FSubTrackGroup.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FSubTrackGroup

A small structure holding data for grouping subtracks. (For UI drawing purposes)

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GroupName` | `FString` | Name of the subtrack  group |
| `TrackIndices` | `TArray < int32 >` | Indices to tracks in the parent track subtrack array. |
| `bIsCollapsed` | `uint32` | If this group is collapsed |
| `bIsSelected` | `uint32` | If this group is selected |
