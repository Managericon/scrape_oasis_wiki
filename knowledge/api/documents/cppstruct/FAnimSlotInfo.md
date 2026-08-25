---
id: "api:cppstruct:FAnimSlotInfo"
title: "FAnimSlotInfo"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimSlotInfo.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimSlotInfo

Struct used for passing information from Matinee to an Actor for blending animations during a sequence.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SlotName` | `FName` | Name of slot that we want to play the animtion in. |
| `ChannelWeights` | `TArray < float >` | Strength of each Channel within this Slot. Channel indexs are determined by track order in Matinee. |
