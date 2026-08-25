---
id: "api:cppstruct:FVectorParameterNameAndCurves"
title: "FVectorParameterNameAndCurves"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FVectorParameterNameAndCurves.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FVectorParameterNameAndCurves

Structure representing an animated vector parameter and it's associated animation curve.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | The name of the vector parameter which is being animated. |
| `Index` | `int32` | - |
| `XCurve` | `FRichCurve` | The curve which contains the animation data for the x component of the vector parameter. |
| `YCurve` | `FRichCurve` | The curve which contains the animation data for the y component of the vector parameter. |
| `ZCurve` | `FRichCurve` | The curve which contains the animation data for the z component of the vector parameter. |
