---
id: "api:class:UParticleModuleSubUVMovie"
title: "UParticleModuleSubUVMovie"
source: "https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleSubUVMovie.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UParticleModuleSubUVMovie

## Inheritance

`UParticleModuleSubUV`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bUseEmitterTime` | `uint32` | If true, use the emitter time to look up the frame rate.<br>	 	If false (default), use the particle relative time. |
| `FrameRate` | `FRawDistributionFloat` | The frame rate the SubUV images should be 'flipped' thru at. |
| `StartingFrame` | `int32` | The starting image index for the SubUV (1 = the first frame).<br>	 	Assumes order of Left->Right, Top->Bottom<br>	 	If greater than the last frame, it will clamp to the last one.<br>	 	If 0, then randomly selects a starting frame. |
| `bUseSmallImageIndex` | `uint32` | If true, ImageIndex will be limited in 0~NumFrames.<br>	 	If false (default), ImageIndex will increase all the time. |

## Language

`cpp`
