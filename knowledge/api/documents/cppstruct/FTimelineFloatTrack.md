---
id: "api:cppstruct:FTimelineFloatTrack"
title: "FTimelineFloatTrack"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FTimelineFloatTrack.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FTimelineFloatTrack

Struct that contains one entry for each vector interpolation performed by the timeline

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FloatCurve` | `UCurveFloat *` | Float curve to be evaluated |
| `TrackName` | `FName` | Name of track, usually set in Timeline Editor. Used by SetInterpFloatCurve function. |
| `FloatPropertyName` | `FName` | Name of property that we should update from this curve |
| `FloatProperty` | `UFloatProperty *` | Cached float property pointer |
