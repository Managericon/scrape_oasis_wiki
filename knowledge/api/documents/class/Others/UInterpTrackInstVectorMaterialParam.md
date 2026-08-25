---
id: "api:class:UInterpTrackInstVectorMaterialParam"
title: "UInterpTrackInstVectorMaterialParam"
source: "https://developer.gp.qq.com/api/class/detail/Others/UInterpTrackInstVectorMaterialParam.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UInterpTrackInstVectorMaterialParam

## Inheritance

`UInterpTrackInst`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaterialInstances` | `TArray < UMaterialInstanceDynamic * >` | MIDs we're using to set the desired parameter. |
| `ResetVectors` | `TArray < FVector >` | Saved values for restoring state when exiting Matinee. |
| `PrimitiveMaterialRefs` | `TArray < struct FPrimitiveMaterialRef >` | Primitive components on which materials have been overridden. |
| `InstancedTrack` | `UInterpTrackVectorMaterialParam *` | Track we are an instance of - used in the editor to propagate changes to the track's Materials array immediately. |

## Language

`cpp`
