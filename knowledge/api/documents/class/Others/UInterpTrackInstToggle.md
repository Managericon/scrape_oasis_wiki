---
id: "api:class:UInterpTrackInstToggle"
title: "UInterpTrackInstToggle"
source: "https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstToggle.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UInterpTrackInstToggle

## Inheritance

`UInterpTrackInst`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Action` | `TEnumAsByte < enum ETrackToggleAction >` | - |
| `LastUpdatePosition` | `float` | Position we were in last time we evaluated.<br>	 	During UpdateTrack, toggles between this time and the current time will be processed. |
| `bSavedActiveState` | `uint32` | Cached 'active' state for the toggleable actor before we possessed it; restored when Matinee exits |

## Language

`cpp`
