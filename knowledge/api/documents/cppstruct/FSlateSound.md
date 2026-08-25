---
id: "api:cppstruct:FSlateSound"
title: "FSlateSound"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FSlateSound.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FSlateSound

An intermediary to make UBaseSound available for Slate to play sounds

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ResourceObject` | `UObject *` | Pointer to the USoundBase. Holding onto it as a UObject because USoundBase is not available in Slate core.<br>	  Edited via FSlateSoundStructCustomization to ensure you can only set USoundBase assets on it. |
