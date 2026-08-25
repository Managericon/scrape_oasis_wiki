---
id: "api:cppstruct:FSoundGroup"
title: "FSoundGroup"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FSoundGroup.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FSoundGroup

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SoundGroup` | `TEnumAsByte < ESoundGroup >` | - |
| `DisplayName` | `FString` | - |
| `bAlwaysDecompressOnLoad` | `uint32` | - |
| `DecompressedDuration` | `float` | Sound duration in seconds below which sounds are entirely expanded to PCM at load time<br>	  Disregarded if bAlwaysDecompressOnLoad is true |
