---
id: "api:cppstruct:FDebugFloatHistory"
title: "FDebugFloatHistory"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FDebugFloatHistory.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FDebugFloatHistory

Structure for recording float values and displaying them as an Histogram through DrawDebugFloatHistory.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Samples` | `TArray < float >` | Samples |
| `MaxSamples` | `float` | Max Samples to record. |
| `MinValue` | `float` | Min value to record. |
| `MaxValue` | `float` | Max value to record. |
| `bAutoAdjustMinMax` | `bool` | Auto adjust MinMax as new values are recorded? |
