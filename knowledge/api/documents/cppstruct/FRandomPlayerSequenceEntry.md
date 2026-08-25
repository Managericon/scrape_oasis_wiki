---
id: "api:cppstruct:FRandomPlayerSequenceEntry"
title: "FRandomPlayerSequenceEntry"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FRandomPlayerSequenceEntry.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FRandomPlayerSequenceEntry

The random player node holds a list of sequences and parameter ranges which will be played continuously
   In a random order. If shuffle mode is enabled then each entry will be played once before repeating any

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sequence` | `UAnimSequenceBase *` | Sequence to play when this entry is picked |
| `ChanceToPlay` | `float` | When not in shuffle mode, this is the chance this entry will play (normalized against all other sample chances) |
| `MinLoopCount` | `int32` | Minimum number of times this entry will loop before ending |
| `MaxLoopCount` | `int32` | Maximum number of times this entry will loop before ending |
| `MinPlayRate` | `float` | Minimum playrate for this entry |
| `MaxPlayRate` | `float` | Maximum playrate for this entry |
| `BlendIn` | `FAlphaBlend` | Blending properties used when this entry is blending in ontop of another entry |
