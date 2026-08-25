---
id: "api:class:UMovieScene3DTransformSection"
title: "UMovieScene3DTransformSection"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMovieScene3DTransformSection.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMovieScene3DTransformSection

A 3D transform section

## Inheritance

`UMovieSceneSection` -> `IKeyframeSection<FTransformKey>`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TransformMask` | `FMovieSceneTransformMask` | - |
| `Translation` | `FRichCurve` | Translation curves |
| `Rotation` | `FRichCurve` | Rotation curves |
| `Scale` | `FRichCurve` | Scale curves |
| `ManualWeight` | `FRichCurve` | Manual weight curve |

## Language

`cpp`
