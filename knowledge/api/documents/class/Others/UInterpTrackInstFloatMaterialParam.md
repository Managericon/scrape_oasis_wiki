---
id: "api:class:UInterpTrackInstFloatMaterialParam"
title: "UInterpTrackInstFloatMaterialParam"
source: "https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstFloatMaterialParam.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UInterpTrackInstFloatMaterialParam

## Inheritance

`UInterpTrackInst`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaterialInstances` | `TArray < UMaterialInstanceDynamic * >` | MIDs we're using to set the desired parameter. |
| `ResetFloats` | `TArray < float >` | Saved values for restoring state when exiting Matinee. |
| `PrimitiveMaterialRefs` | `TArray < struct FPrimitiveMaterialRef >` | Primitive components on which materials have been overridden. |
| `InstancedTrack` | `UInterpTrackFloatMaterialParam *` | track we are an instance of - used in the editor to propagate changes to the track's Materials array immediately |

## Language

`cpp`
