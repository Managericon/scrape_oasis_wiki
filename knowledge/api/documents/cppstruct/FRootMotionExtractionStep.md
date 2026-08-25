---
id: "api:cppstruct:FRootMotionExtractionStep"
title: "FRootMotionExtractionStep"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FRootMotionExtractionStep.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FRootMotionExtractionStep

Struct defining a RootMotionExtractionStep.
  When extracting RootMotion we can encounter looping animations (wrap around), or different animations.
  We break those up into different steps, to help with RootMotion extraction, 
  as we can only extract a contiguous range per AnimSequence.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AnimSequence` | `UAnimSequence *` | AnimSequence ref |
| `StartPosition` | `float` | Start position to extract root motion from. |
| `EndPosition` | `float` | End position to extract root motion to. |
