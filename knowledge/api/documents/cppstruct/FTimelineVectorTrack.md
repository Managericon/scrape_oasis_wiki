---
id: "api:cppstruct:FTimelineVectorTrack"
title: "FTimelineVectorTrack"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FTimelineVectorTrack.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FTimelineVectorTrack

Struct that contains one entry for each vector interpolation performed by the timeline

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VectorCurve` | `UCurveVector *` | Vector curve to be evaluated |
| `TrackName` | `FName` | Name of track, usually set in Timeline Editor. Used by SetInterpVectorCurve function. |
| `VectorPropertyName` | `FName` | Name of property that we should update from this curve |
| `VectorProperty` | `UStructProperty *` | Cached vector struct property pointer |
