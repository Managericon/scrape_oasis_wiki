---
id: "api:cppstruct:FPassiveSoundMixModifier"
title: "FPassiveSoundMixModifier"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FPassiveSoundMixModifier.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FPassiveSoundMixModifier

Structure containing information on a SoundMix to activate passively.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SoundMix` | `USoundMix *` | The SoundMix to activate |
| `MinVolumeThreshold` | `float` | Minimum volume level required to activate SoundMix. Below this value the SoundMix will not be active. |
| `MaxVolumeThreshold` | `float` | Maximum volume level required to activate SoundMix. Above this value the SoundMix will not be active. |
