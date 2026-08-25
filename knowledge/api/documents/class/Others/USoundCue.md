---
id: "api:class:USoundCue"
title: "USoundCue"
source: "https://developer.gp.qq.com/api/class/detail/Others/USoundCue.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# USoundCue

The behavior of audio playback is defined within Sound Cues.

## Inheritance

`USoundBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bOverrideAttenuation` | `uint32` | Indicates whether attenuation should use the Attenuation Overrides or the Attenuation Settings asset |
| `FirstNode` | `USoundNode *` | - |
| `VolumeMultiplier` | `float` | Volume multiplier for the Sound Cue |
| `PitchMultiplier` | `float` | Pitch multiplier for the Sound Cue |
| `AttenuationOverrides` | `FSoundAttenuationSettings` | Attenuation settings to use if Override Attenuation is set to true |
| `SubtitlePriority` | `float` | - |
| `AllNodes` | `TArray < USoundNode * >` | - |
| `SoundCueGraph` | `UEdGraph *` | - |

## Language

`cpp`
