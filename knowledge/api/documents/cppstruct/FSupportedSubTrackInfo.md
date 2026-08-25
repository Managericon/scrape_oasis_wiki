---
id: "api:cppstruct:FSupportedSubTrackInfo"
title: "FSupportedSubTrackInfo"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FSupportedSubTrackInfo.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FSupportedSubTrackInfo

Helper struct for creating sub tracks supported by this track

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SupportedClass` | `TSubclassOf < UInterpTrack >` | The sub track class which is supported by this track |
| `SubTrackName` | `FString` | The name of the subtrack |
| `GroupIndex` | `int32` | Index into the any subtrack group this subtrack belongs to (can be -1 for no group) |
