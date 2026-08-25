---
id: "api:cppstruct:FSoundClassAdjuster"
title: "FSoundClassAdjuster"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FSoundClassAdjuster.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FSoundClassAdjuster

Elements of data for sound group volume control

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SoundClassObject` | `USoundClass *` | The sound class this adjuster affects. |
| `VolumeAdjuster` | `float` | A multiplier applied to the volume. |
| `PitchAdjuster` | `float` | A multiplier applied to the pitch. |
| `bApplyToChildren` | `uint32` | Set to true to apply this adjuster to all children of the sound class. |
| `VoiceCenterChannelVolumeAdjuster` | `float` | A multiplier applied to VoiceCenterChannelVolume. |
