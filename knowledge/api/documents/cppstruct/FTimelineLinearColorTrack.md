---
id: "api:cppstruct:FTimelineLinearColorTrack"
title: "FTimelineLinearColorTrack"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FTimelineLinearColorTrack.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FTimelineLinearColorTrack

Struct that contains one entry for each linear color interpolation performed by the timeline

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LinearColorCurve` | `UCurveLinearColor *` | Float curve to be evaluated |
| `TrackName` | `FName` | Name of track, usually set in Timeline Editor. Used by SetInterpLinearColorCurve function. |
| `LinearColorPropertyName` | `FName` | Name of property that we should update from this curve |
| `LinearColorProperty` | `UStructProperty *` | Cached linear color struct property pointer |
