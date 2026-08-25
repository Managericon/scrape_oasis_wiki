---
id: "api:cppstruct:FRBFTarget"
title: "FRBFTarget"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FRBFTarget.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FRBFTarget

Data about a particular target in the RBF, including scaling factor

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ScaleFactor` | `float` | How large to scale |
| `bApplyCustomCurve` | `bool` | Whether we want to apply an additional custom curve when activating this target |
| `CustomCurve` | `FRichCurve` | Custom curve to apply to activation of this target, if bApplyCustomCurve is true |
