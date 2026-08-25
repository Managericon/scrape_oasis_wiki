---
id: "api:cppstruct:FCameraPreviewInfo"
title: "FCameraPreviewInfo"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FCameraPreviewInfo.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FCameraPreviewInfo

Preview APawn class for this track

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PawnClass` | `TSubclassOf < APawn >` | - |
| `AnimSeq` | `UAnimSequence *` | - |
| `Location` | `FVector` | for now this is read-only. It has maintenance issue to be resolved if I enable this. |
| `Rotation` | `FRotator` | - |
| `PawnInst` | `APawn *` | APawn Inst - CameraAnimInst doesn't really exist in editor |
