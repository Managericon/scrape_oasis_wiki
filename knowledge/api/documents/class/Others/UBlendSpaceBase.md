---
id: "api:class:UBlendSpaceBase"
title: "UBlendSpaceBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBlendSpaceBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBlendSpaceBase

Allows multiple animations to be blended between based on input parameters

## Inheritance

`UAnimationAsset` -> `IInterpolationIndexProvider`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bRotationBlendInMeshSpace` | `bool` | When you use blend per bone, allows rotation to blend in mesh space. This only works if this does not contain additive animation samples<br>	 This is more performance intensive |
| `AnimLength` | `float` | This animation length changes based on current input (resulting in different blend time) |
| `InterpolationParam` | `FInterpolationParameter` | Input interpolation parameter for all 3 axis, for each axis input, decide how you'd like to interpolate input to |
| `TargetWeightInterpolationSpeedPerSec` | `float` | Target weight interpolation. When target samples are set, how fast you'd like to get to target. Improve target blending.<br>	 i.e. for locomotion, if you interpolate input, when you move from left to right rapidly, you'll interpolate through forward, but if you use target weight interpolation,<br>	 you'll skip forward, but interpolate between left to right |
| `NotifyTriggerMode` | `TEnumAsByte < ENotifyTriggerMode :: Type >` | The current mode used by the blendspace to decide which animation notifies to fire. Valid options are: |
| `PerBoneBlend` | `TArray < FPerBoneInterpolation >` | Define target weight interpolation per bone. This will blend in different speed per each bone setting |
| `SampleIndexWithMarkers` | `int32` | Track index to get marker data from. Samples are tested for the suitability of marker based sync<br>	    during load and if we can use marker based sync we cache an index to a representative sample here |
| `SampleData` | `TArray < struct FBlendSample >` | Sample animation data |
| `GridSamples` | `TArray < struct FEditorElement >` | Grid samples, indexing scheme imposed by subclass |
| `BlendParameters` | `FBlendParameter` | Blend Parameters for each axis. |

## Language

`cpp`
