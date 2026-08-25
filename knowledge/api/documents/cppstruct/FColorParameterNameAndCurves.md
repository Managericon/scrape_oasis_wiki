---
id: "api:cppstruct:FColorParameterNameAndCurves"
title: "FColorParameterNameAndCurves"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FColorParameterNameAndCurves.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FColorParameterNameAndCurves

Structure representing an animated vector parameter and it's associated animation curve.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | The name of the vector parameter which is being animated. |
| `Index` | `int32` | - |
| `RedCurve` | `FRichCurve` | The curve which contains the animation data for the red component of the color parameter. |
| `GreenCurve` | `FRichCurve` | The curve which contains the animation data for the green component of the color parameter. |
| `BlueCurve` | `FRichCurve` | The curve which contains the animation data for the blue component of the color parameter. |
| `AlphaCurve` | `FRichCurve` | The curve which contains the animation data for the alpha component of the color parameter. |
